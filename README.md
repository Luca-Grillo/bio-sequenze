# bio_sequenze

Piccolo progetto di bioinformatica in Python che analizza una sequenza di mRNA in formato FASTA con Biopython. Come esempio usa il trascritto del gene dell'insulina umana (INS, `NM_000207.3`).

## Cosa fa

- legge la sequenza da un file FASTA
- calcola il contenuto di GC
- trascrive il DNA in RNA
- individua il codone di inizio (ATG) e traduce in proteina fino al primo codone di stop
- salva i risultati in un report di testo

## Requisiti

- Python 3.13
- [Poetry](https://python-poetry.org/)

## Installazione

```
git clone git@github.com:Luca-Grillo/bio-sequenze.git
cd bio-sequenze
poetry install
```

## Uso

Dalla radice del progetto:

```
poetry run python src/bio_sequenze/lettura.py
```

Il programma legge `data/insulina.fasta` e scrive il report in `results/report_insulina.txt`.

## Esempio di output

Identificativo: NM_000207.3
Descrizione: NM_000207.3 Homo sapiens insulin (INS), transcript variant 1, mRNA
Lunghezza sequenza: 465
Contenuto di GC: 63.87%
Proteina: MALWMRLLPLLALLALWGPDPAAAFVNQHLCGSHLVEALYLVCGERGFFYTPKTRREAEDLQVGQVELGGGPGAGSLQPLALEGSLQKRGIVEQCCTSICSLYQLENYCN
Lunghezza proteina: 110


## Struttura del progetto

- `data/`: file FASTA in ingresso
- `src/bio_sequenze/`: codice sorgente
- `results/`: report generati

## Note

La traduzione parte dal primo ATG della sequenza, perché il trascritto contiene una regione non tradotta (5' UTR) prima della parte codificante.