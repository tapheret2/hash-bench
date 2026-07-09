from hash_bench import run_bench

def test_sha3_256_present():
    rows = run_bench(size_mb=0.05, iters=1, algos=["sha3_256"])
    assert rows and rows[0]["algo"] == "sha3_256"
