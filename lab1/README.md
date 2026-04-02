# MBI Lab 1 (album: 307340)

## Wybrany genom
- indeks z listy: `307340 mod 150 = 140`
- URL genomu: `ftp://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/002/209/025/GCF_002209025.1_ASM220902v1/GCF_002209025.1_ASM220902v1_genomic.fna.gz`
- lokalny FASTA: `input/ref.fa`

## Pliki wygenerowane
- `output/pirs_reads_100_400_1.fq`
- `output/pirs_reads_100_400_2.fq`
- `output/pirs_reads_100_400.read.info`
- `output/pirs_reads_100_400.insert_len.distr`
- `output/pirs_reads_100_400.error_rate.distr`
- `scripts/gc_content.py`

## Uruchamianie skryptu GC-content
```powershell
python -m pip install --disable-pip-version-check -r .\requirements.txt
python .\scripts\gc_content.py .\input\ref.fa
```

## Test skryptu GC-content
```powershell
python -m unittest .\tests\test_gc_content.py -v
```

## Parametry pIRS
```text
coverage: 50
insert mean: 400
insert sd: 20
read length: 100
substitution error rate: 0.01
```

