from hash_bench.bench import ALGOS, run_bench

def test_sha3_registered():
    assert "sha3_256" in ALGOS

def test_sha3_runs():
    rows = run_bench(size_mb=0.25, iters=1, algos=["sha3_256"])
    assert rows and rows[0]["algo"] == "sha3_256"
    assert rows[0]["best_s"] > 0
