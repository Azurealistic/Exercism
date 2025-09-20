def to_rna(dna_strand):
    res = ""
    for c in dna_strand:
        match c:
            case 'G': res += 'C'
            case 'C': res += 'G'
            case 'T': res += 'A'
            case 'A': res += 'U'
    return res
