elems = { 'G': [ "Ga", "Gd", "Ge", ], 'L': [ "La", "Li", "Lr", "Lu", ], 'N': [ "N", "Na", "Nb", "Nd", "Ne", "Ni", "No", "Np", ], 'U': [ "U", ], 'Y': [ "Y", "Yb", ], 'Z': [ "Zn", "Zr", ], 'V': [ "V", ], 'P': [ "P", "Pa", "Pb", "Pd", "Pm", "Po", "Pr", "Pt", "Pu", ], 'M': [ "Md", "Mg", "Mn", "Mo", "Mt", ], 'H': [ "H", "He", "Hf", "Hg", "Ho", "Hs", ], 'E': [ "Er", "Es", "Eu", ], 'F': [ "F", "Fe", "Fm", "Fr", ], 'J': [], 'B': [ "B", "Ba", "Be", "Bh", "Bi", "Bk", "Br", ], 'K': [ "K", "Kr", ], 'D': [ "Ds", "Db", "Dy", ], 'O': [ "O", "Os", ], 'I': [ "I", "In", "Ir", ], 'R': [ "Ra", "Rb", "Re", "Rf", "Rg", "Rh", "Rn", "Ru", ], 'S': [ "S", "Sb", "Sc", "Se", "Sg", "Si", "Sm", "Sn", "Sr", ], 'A': [ "Ac", "Ag", "Al", "Am", "Ar", "As", "At", "Au", ], 'T': [ "Ta", "Tb", "Tc", "Te", "Th", "Ti", "Tl", "Tm", ], 'W': [ "W", ], 'X': [ "Xe", ], 'C': [ "C", "Ca", "Cd", "Ce", "Cf", "Cl", "Cm", "Co", "Cr", "Cs", "Cu", ], 'Q': [] }

def is_elem(s):
    return s[0].upper()+s[1:] in elems[s[0].upper()]

def word_to_elem(word, so_far):
    if len(word) == 0:
        print("<", so_far, sep="")
        return
    if is_elem(word[0]):
        word_to_elem(word[1:], so_far + " " + word[0].upper())
    if len(word) >= 2 and is_elem(word[0:2]):
        word_to_elem(word[2:], so_far + " " + word[0].upper() + word[1])

while True:
    w = input("> ").replace(" ", "")
    if w == "q":
        exit()
    if not w.isalpha():
        print("only letters.")
        continue
    word_to_elem(w, "")
