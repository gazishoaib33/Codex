"""Simple CLI to run sample coding problems."""

import argparse
import json

from problems import PROBLEMS


def list_problems() -> None:
    for name in sorted(PROBLEMS):
        print(name)


def run_problem(name: str, payload: str) -> None:
    if name not in PROBLEMS:
        raise SystemExit(f"Unknown problem: {name}")
    data = json.loads(payload) if payload else {}
    result = PROBLEMS[name](**data)
    print(result)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run sample Codex problems.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    subparsers.add_parser("list", help="List available problems")

    run_parser = subparsers.add_parser("run", help="Run a problem by name")
    run_parser.add_argument("name", help="Problem name")
    run_parser.add_argument(
        "--payload",
        default="",
        help='JSON payload with parameters (e.g. "{\\"limit\\": 10}")',
    )

    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    if args.command == "list":
        list_problems()
    elif args.command == "run":
        run_problem(args.name, args.payload)


if __name__ == "__main__":
    main()
