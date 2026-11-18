"""
Analizza una sequenza di mRNA in formato FASTA: calcola il contenuto di GC, la trascrizione in RNA e la traduzione in proteina a partire dal codone ATG.

Input:  data/insulina.fasta (trascritto del gene INS umano, NM_000207.3)
Output: results/report_insulina.txt (id, descrizione, lunghezze, GC, proteina)

Uso: lanciare dalla radice del progetto, altrimenti i percorsi relativi non funzionano.
poetry run python src/bio_sequenze/lettura.py
Richiede Biopython (installato con Poetry).
"""

from Bio import SeqIO
from Bio.SeqUtils import gc_fraction 

record = SeqIO.read("data/insulina.fasta", "fasta")

print(record.id)
print(record.description)
print(len(record.seq))

gc = gc_fraction(record.seq) * 100
print(f"GC contenuta in {record.id} : {gc:.2f} %")

rna = record.seq.transcribe()       # Converte DNA in RNA (T diventa U)
proteina_completa = record.seq.translate()   # Traduce dalla prima base, quindi fuori fase
# print(f"Modifica in rna: {rna} ed in proteina {proteina_completa}")

inizio = record.seq.find("ATG")         # "ATG" codone di inizio, prima c'è una regione non tradotta
print(f"inizio proteina {inizio}")      

cds = record.seq[inizio:]       # cds (coding sequence), parte che viene tradotta

proteina = cds.translate(to_stop=True)      # La traduzione si ferma al primo codone di stop
print(f"Inizio proteina {inizio}, risultato: {proteina} lunghezza {len(proteina)}")

with open("results/report_insulina.txt", "w", encoding="utf-8") as f:
    f.write(f"Identificativo: {record.id}\n")
    f.write(f"Descrizione: {record.description}\n")
    f.write(f"Lunghezza sequenza: {len(record.seq)}\n")
    f.write(f"Contenuto di GC: {gc:.2f}%\n")
    f.write(f"Proteina: {proteina}\n")
    f.write(f"Lunghezza proteina: {len(proteina)}\n")