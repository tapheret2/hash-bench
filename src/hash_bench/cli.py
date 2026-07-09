from __future__ import annotations

import argparse
import json
import sys

from .bench import run_bench


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(prog="hash-bench")
    sub = p.add_subparsers(dest="cmd", required=True)
    r = sub.add_parser("run")
    r.add_argument("--size-mb", type=float, default=4.0)
    r.add_argument("--iters", type=int, default=3)
    r.add_argument("--json", action="store_true")
    args = p.parse_args(argv)
    if args.cmd == "run":
        rows = run_bench(size_mb=args.size_mb, iters=args.iters)
        if args.json:
            print(json.dumps(rows, indent=2))
        else:
            for row in rows:
                print(f"{row['algo']:10} {row['mb_s']:10.1f} MB/s  best={row['best_s']:.4f}s")
        return 0
    return 1


if __name__ == "__main__":
    sys.exit(main())
