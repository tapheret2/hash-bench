from hash_bench.bench import digest_hex

def test_digest_hex_sha256_known():
    h = digest_hex("sha256", b"abc")
    assert h == "ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad"
