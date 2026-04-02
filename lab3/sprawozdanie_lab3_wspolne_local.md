# Sprawozdanie Lab3 - wersja wspolna lokalna

## Podsumowanie wynikow

- Typowa dlugosc odczytu: `151 bp`
- Rozmiar FASTQ/SAM/BAM: `26474782 / 31190659 / 4776208 B`
- Warianty przed filtracja: `3`
- Warianty po filtracji (`DP>10`): `3`
- Wybrany wariant (IGV): `chr1:156510654`, `GT=0/1`, `DP=40`
- Adnotacja VEP: 2x `intron_variant`, 1x `missense_variant`
- Zadanie implementacyjne: `IQGAP3 = 3` (plik `output/variants_per_gene.tsv`)

## Uwaga

Pipeline wykonano na syntetycznych odczytach `coriell_chr1.fq` (brak publicznego dostepu do
oryginalnego pliku z Teams).

