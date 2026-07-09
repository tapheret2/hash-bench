# hash-bench

![status](https://img.shields.io/badge/status-active-brightgreen) ![python](https://img.shields.io/badge/python-3.10%2B-blue) ![license](https://img.shields.io/badge/license-MIT-lightgrey)

Micro-benchmark CLI for Python `hashlib` (throughput MB/s). Handy DS systems lab toy.

## CLI

```bash
pip install -e ".[dev]"
hash-bench run --size-mb 8 --iters 5
```
