import msgpack
import io
import sys
from benchmarker import Benchmarker

with Benchmarker() as bench:
    @bench('msgpack')
    def _(bm):
        in_ch = io.open(sys.argv[1], mode='rb')
        unpacker = msgpack.Unpacker(in_ch, encoding=str("utf-8"))
        for row in unpacker:
            pass
