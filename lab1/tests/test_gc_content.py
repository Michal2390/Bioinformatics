import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.gc_content import compute_file_gc


class TestGcContent(unittest.TestCase):
    def test_compute_file_gc(self) -> None:
        fasta = ">seq1\nACGTACGT\n>seq2\nGGGGTTTT\n"
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp) / "sample.fa"
            p.write_text(fasta, encoding="utf-8")
            gc, length = compute_file_gc(p)

        self.assertEqual(length, 16)
        self.assertAlmostEqual(gc, 50.0, places=6)


if __name__ == "__main__":
    unittest.main()
