from hash_bench import run_bench


def test_bench_smoke():
    rows = run_bench(size_mb=0.25, iters=1)
    assert len(rows) >= 3
    assert all("mb_s" in r for r in rows)
