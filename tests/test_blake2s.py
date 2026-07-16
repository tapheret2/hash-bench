from hash_bench import run_bench

def test_blake2s_present():
    rows = run_bench(size_mb=0.05, iters=1, algos=["blake2s"])
    assert rows and rows[0]["algo"] == "blake2s"
