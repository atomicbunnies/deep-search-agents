import subprocess
import sys
import unittest
from pathlib import Path

from deep_search_agents.app import get_status


class PhaseZeroSmokeTests(unittest.TestCase):
    def test_application_reports_ready(self) -> None:
        status = get_status()
        self.assertTrue(status.ready)
        self.assertEqual(status.phase, "Phase 0 - Project Initialization")

    def test_module_entry_point_runs_without_api_keys(self) -> None:
        project_root = Path(__file__).resolve().parents[1]
        result = subprocess.run(
            [sys.executable, "-m", "deep_search_agents", "--status"],
            cwd=project_root,
            env={"PYTHONPATH": str(project_root / "src")},
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("ready=True", result.stdout)


if __name__ == "__main__":
    unittest.main()
