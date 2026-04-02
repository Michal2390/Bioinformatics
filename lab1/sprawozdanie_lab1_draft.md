# Sprawozdanie MBI Lab 1 (wersja robocza)

## Dane wejściowe
- Numer albumu: `307340`
- Wybrany indeks genomu: `307340 mod 150 = 140`
- Wybrany genom: `ftp://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/002/209/025/GCF_002209025.1_ASM220902v1/GCF_002209025.1_ASM220902v1_genomic.fna.gz`
- Lokalny plik referencyjny: `input/ref.fa`
- Długość genomu referencyjnego: `1,641,468 bp`

## 2.2 Generowanie odczytów (pIRS)
Parametry:
- pokrycie: `50x`
- insert mean: `400 bp`
- insert std: `20`
- długość odczytu: `100 bp`
- błąd podstawienia: `1%`

Fragment logu pIRS:
```text
[pIRS] Bases in reference sequences:    1641468
[pIRS] Read pairs simulated:            410367
[pIRS] Bases in reads:                  82073400
[pIRS] Coverage:                        50.00
[pIRS] Substitution error count:        1101362
[pIRS] Average substitution error rate: 1.342%
[pIRS] Insertion count:                 357
[pIRS] Deletion count:                  886
[pIRS] Average insertion rate:          0.00043%
[pIRS] Average deletion rate:           0.00108%
[pIRS] Average insertion length:        1.08
[pIRS] Average deletion length:         1.03
[pIRS] Fragments affected by GC bias:   8.07%
[pIRS] Bases masked by EAMSS algorithm: 0
```

Odpowiedzi:
1. Ile odczytów i jakiej długości?
   - `410,367` par odczytów, czyli `820,734` odczyty łącznie.
   - Długość pojedynczego odczytu: `100 bp`.

2. Głębokość pokrycia (obliczenie):
   - wzór: `coverage = (liczba_odczytów * długość_odczytu) / długość_genomu`
   - `coverage = (820734 * 100) / 1641468 = 50.0`
   - Wynik jest zgodny z założeniem `50x`.

3. Jak znaleźć odczyty z błędami?
   - Najprościej użyć pliku `output/pirs_reads_100_400.read.info` (zawiera informacje o symulowanych błędach dla par).
   - Alternatywnie: mapować FASTQ do referencji i identyfikować mismatch/indel.

4. Odległości między sparowanymi odczytami:
   - Z `output/pirs_reads_100_400.insert_len.distr`:
   - średnia: `399.5751 bp`
   - odchylenie standardowe: `20.004`
   - min/max: `307 / 486`
   - Wartości są zgodne z ustawieniami (`400`, `20`) w granicach losowości symulacji.

## 2.3 Asemblacja de novo (dnaasm)
Parametry dnaasm:
- `k=55`
- `genome_length=1641468`
- `insert_size_mean_inward=400`
- `insert_size_std_dev_inward=20`
- `single_edge_counter_threshold=5`
- wejście: `output/pirs_reads_100_400_1.fq`, `output/pirs_reads_100_400_2.fq`
- wyjście: `output/contigs.fa`

Fragment statystyk końcowych asemblacji (zgodny z wynikiem użytym w QUAST):
```text
[info] - num of sequences: 183
[info] - sum: 3267691
[info] - max: 355732
[info] - average: 17856.234973
[info] - median: 166
[info] - N50: 153901
```

Odpowiedzi:
1. Czy suma długości wygenerowanych sekwencji jest w przybliżeniu równa długości genomu?
   - Nie. Suma (`3,267,691`) jest ~2x większa od długości referencji (`1,641,468`).
   - Potwierdza to też QUAST: `Duplication ratio = 1.997`.
   - Powód: duplikacja/redundancja fragmentów i niedoskonała rekonstrukcja grafu przy de novo.

2. Czy plik wynikowy jest FASTA czy FASTQ?
   - `output/contigs.fa` jest w formacie FASTA.

3. Czy możliwa konwersja FASTA -> FASTQ?
   - Tak, ale trzeba sztucznie wygenerować linie jakości (Phred), bo FASTA ich nie zawiera.

4. Czy możliwa konwersja FASTQ -> FASTA?
   - Tak, po usunięciu linii jakości.
   - Utracona informacja: jakości baz (Phred scores).

## 2.4 Sprawdzenie wyników (QUAST)
Użyte polecenie:
```text
python /quast-5.3.0/quast.py -R ref.fa output/contigs.fa -o output/quast_results
```

Kluczowe metryki z `output/quast_results/report.txt`:
- `# contigs (>= 0 bp): 183`
- `# contigs: 45`
- `Largest contig: 355732`
- `Total length: 3245900`
- `Reference length: 1641468`
- `N50: 153901`
- `L50: 8`
- `GC (%): 30.46`
- `Reference GC (%): 30.55`
- `Genome fraction (%): 98.849`
- `# misassemblies: 1`
- `# mismatches per 100 kbp: 0.12`
- `# indels per 100 kbp: 0.56`

Zawartość `report.txt`:
```text
All statistics are based on contigs of size >= 500 bp, unless otherwise noted (e.g., "# contigs (>= 0 bp)" and "Total length (>= 0 bp)" include all contigs).

Assembly                     contigs
# contigs (>= 0 bp)          183
# contigs (>= 1000 bp)       40
# contigs (>= 5000 bp)       31
# contigs (>= 10000 bp)      30
# contigs (>= 25000 bp)      25
# contigs (>= 50000 bp)      22
Total length (>= 0 bp)       3267691
Total length (>= 1000 bp)    3242762
Total length (>= 5000 bp)    3214688
Total length (>= 10000 bp)   3207537
Total length (>= 25000 bp)   3140405
Total length (>= 50000 bp)   3022596
# contigs                    45
Largest contig               355732
Total length                 3245900
Reference length             1641468
GC (%)                       30.46
Reference GC (%)             30.55
N50                          153901
NG50                         189346
N90                          65492
NG90                         153903
auN                          172479.4
auNG                         341067.3
L50                          8
LG50                         3
L90                          21
LG90                         7
# misassemblies              1
# misassembled contigs       1
Misassembled contigs length  96901
# local misassemblies        0
# scaffold gap ext. mis.     0
# scaffold gap loc. mis.     31
# unaligned mis. contigs     0
# unaligned contigs          0 + 0 part
Unaligned length             0
Genome fraction (%)          98.849
Duplication ratio            1.997
# N's per 100 kbp            218.83
# mismatches per 100 kbp     0.12
# indels per 100 kbp         0.56
Largest alignment            355423
Total aligned length         3239639
NA50                         153733
NGA50                        189044
NA90                         65492
NGA90                        153749
auNA                         171162.1
auNGA                        338462.4
LA50                         8
LGA50                        3
LA90                         21
LGA90                        7
```

Odpowiedzi:
1. Czy wynik asemblacji jest satysfakcjonujący?
   - Częściowo tak: bardzo duże pokrycie genomu (`98.849%`) i brak niealigned contigs.
   - Jednocześnie jakość strukturalna nie jest idealna (`1` misassembly, `Duplication ratio ~2.0`, duża suma długości kontigów).

2. Czym są translokacje i czy QUAST je raportuje?
   - Translokacja: przeniesienie fragmentu DNA w inne miejsce genomu (często między regionami/chromosomami).
   - Tak, QUAST raportuje je w `output/quast_results/contigs_reports/misassemblies_report.txt`.
   - Dla tego wyniku: `# s. translocations = 0` (za to `# s. relocations = 1`).

## 3. Zadanie implementacyjne (GC-content)
- Skrypt: `scripts/gc_content.py` (Biopython)
- Test: `tests/test_gc_content.py`
- Wynik skryptu dla `input/ref.fa`:
  - `acgt_bases=1641468`
  - `gc_percent=30.5483`
- QUAST (`Reference GC (%)`): `30.55`

Porównanie:
- Wyniki są zgodne (różnica tylko przez zaokrąglenie):
  - skrypt: `30.5483%`
  - QUAST: `30.55%`
