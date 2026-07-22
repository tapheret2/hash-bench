from hash_bench.bench import digest_hex, ALGOS

def test_sha3_512_registered():
    assert "sha3_512" in ALGOS

def test_sha3_512_digest_len():
    h = digest_hex("sha3_512", b"abc")
    assert len(h) == 128
