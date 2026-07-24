from hash_bench.bench import blake2b_hex, sha3_256_hex


def test_blake2b_hex_len():
    assert len(blake2b_hex(b"abc")) == 64


def test_sha3_256_hex_len():
    assert len(sha3_256_hex(b"abc")) == 64
