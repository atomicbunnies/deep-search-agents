"""Application-level status for the Phase 0 scaffold."""

from dataclasses import dataclass


@dataclass(frozen=True)
class AppStatus:
    """Small, dependency-free status object used by the local application."""

    name: str = "Deep Web Search Agents"
    phase: str = "Phase 0 - Project Initialization"
    ready: bool = True


def get_status() -> AppStatus:
    """Return the current local application status."""

    return AppStatus()
