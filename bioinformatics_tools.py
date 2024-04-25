class bioinformaticsToolKit:
    #class attributes
    gene_to_aminoacid = { 
            'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M', 
            'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T', 
            'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K', 
            'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',                  
            'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L', 
            'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P', 
            'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q', 
            'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R', 
            'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V', 
            'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A', 
            'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E', 
            'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G', 
            'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S', 
            'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L', 
            'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_', 
            'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W', 
        } 
    def __init__(self):
        pass

    #Code for translating nucleic acids to protein sequence

    #setting up table of standard genetic code


    def translateNuc(self, data):
        translation = {}
        while len(data)>0:
            line = data.pop(0).upper()
            triplets = [line[i:i+3] for i in range(0, len(line), 3)]
            prot_seq = ''
            for codon in triplets:
                prot_seq += self.gene_to_aminoacid.get(codon,'?')
            translation[line]= prot_seq
        return translation

data = ['gtagta','gcccgccat']
toolkit = bioinformaticsToolKit()
print(toolkit.translateNuc(data))