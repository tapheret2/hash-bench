from hash_bench import run_bench

def test_sha512_present():
    rows = run_bench(size_mb=0.1, iters=1, algos=["sha512"])
    assert rows and rows[0]["algo"] == "sha512"
