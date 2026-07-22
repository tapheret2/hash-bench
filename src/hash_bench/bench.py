from __future__ import annotations

import hashlib
import time
from typing import Any


ALGOS = {
    "md5": hashlib.md5,
    "sha1": hashlib.sha1,
    "sha256": hashlib.sha256,
    "blake2b": hashlib.blake2b,
    "blake2s": hashlib.blake2s,
    "sha512": hashlib.sha512,
    "sha3_256": hashlib.sha3_256,
    "sha3_512": hashlib.sha3_512,
}


def run_bench(size_mb: float = 4.0, iters: int = 3, algos: list[str] | None = None) -> list[dict[str, Any]]:
    size = int(size_mb * 1024 * 1024)
    data = b"x" * size
    names = algos or list(ALGOS.keys())
    results = []
    for name in names:
        factory = ALGOS[name]
        # warmup
        factory(data).digest()
        times = []
        for _ in range(iters):
            t0 = time.perf_counter()
            factory(data).digest()
            times.append(time.perf_counter() - t0)
        best = min(times)
        mbs = (size / (1024 * 1024)) / best if best > 0 else 0.0
        results.append({"algo": name, "best_s": best, "mb_s": mbs, "size_mb": size_mb, "iters": iters})
    results.sort(key=lambda r: r["mb_s"], reverse=True)
    return results


def digest_hex(algo: str, data: bytes) -> str:
    """One-shot hex digest for a registered algorithm."""
    if algo not in ALGOS:
        raise KeyError(f"unknown algo: {algo}")
    return ALGOS[algo](data).hexdigest()
