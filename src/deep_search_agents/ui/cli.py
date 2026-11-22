"""Minimal local command-line interface for project initialization."""

import argparse

from deep_search_agents.app import get_status


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Deep Web Search Agents")
    parser.add_argument(
        "--status",
        action="store_true",
        help="show the local application status (the default)",
    )
    return parser


def main() -> None:
    args = build_parser().parse_args()
    status = get_status()
    if args.status or not args.status:
        print(f"{status.name} | {status.phase} | ready={status.ready}")
