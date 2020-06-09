# Tarea de Computación Molecular Biologica: Dot plot
Abriendo los archivos fasta.txt y Q8BTM8.fasta.txt

```
from Bio import SeqIO
sequences = SeqIO.parse("P21333.fasta.txt", "fasta")
for record in sequences:
    data1 = str(record.seq.upper()) # the fasta file just have one sequence

sequences = SeqIO.parse("Q8BTM8.fasta.txt", "fasta")
for record in sequences:
	data2 = str(record.seq.upper()) # the fasta file just have one sequence
print("Datos de Q8BTM8.fasta")
print(data2)
```
**Experimentos**

Comparación de la proteína Filamin-A para ratones ("Q8BTM8") y para humanos ("P21333.fasta").
Ventana igual a 10 y con probabilidad de 23%.

![](https://github.com/cchavezlo/UNSA/blob/master/ComputacionMolecularBiologica/ventana10y023.jpg)

Comparación Virus de hepatitis A con otra proteína relacionada con el receptor de lipoproteínas de baja densidad de un GATO.

![](https://github.com/cchavezlo/UNSA/blob/master/ComputacionMolecularBiologica/Cap3.JPG)

Comparación de la supresor tumoral asociado a microtúbulos 1 (humano) con el virus de inmunodeficiencia de Simia en mono verde africano.

![](https://github.com/cchavezlo/UNSA/blob/master/ComputacionMolecularBiologica/Cap4.JPG)
