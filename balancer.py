from sympy import symbols, Eq, solve
import re
from rdkit import Chem
from rdkit.Chem import Draw

def parse_formula(formula):
    elements = re.findall(r'([A-Z][a-z]*)(\d*)', formula)
    result = {}
    for (element, count) in elements:
        result[element] = result.get(element, 0) + int(count) if count else 1
    return result

def parse_reaction(reaction):
    reactants_str, products_str = reaction.split("->")
    reactants = [r.strip() for r in reactants_str.split('+')]
    products = [p.strip() for p in products_str.split('+')]
    return reactants, products

def get_elements(reactants, products):
    elements = set()
    for compound in reactants + products:
        elements.update(parse_formula(compound).keys())
    return sorted(elements)

def build_matrix(reactants, products, elements):
    all_compounds = reactants + products
    matrix = []

    for element in elements:
        row = []
        for compound in all_compounds:
            formula = parse_formula(compound)
            count = formula.get(element, 0)
            # Reactants are negative
            if compound in reactants:
                row.append(-count)
            else:
                row.append(count)
        matrix.append(row)
    return matrix

def balance(reaction):
    reactants, products = parse_reaction(reaction)
    elements = get_elements(reactants, products)
    matrix = build_matrix(reactants, products, elements)

    coeffs = symbols(f'x0:{len(reactants) + len(products)}')
    equations = [Eq(sum(row[i] * coeffs[i] for i in range(len(coeffs))), 0) for row in matrix]
    equations.append(Eq(coeffs[0], 1))  # Fix first coefficient to 1

    sol = solve(equations, coeffs)

    balanced = [1] + [sol[c] for c in coeffs[1:]]
    return reactants, products, balanced

def draw_molecules(compounds):
    mols = [Chem.MolFromSmiles(compound) for compound in compounds]
    mols = [m for m in mols if m is not None]
    img = Draw.MolsToGridImage(mols, molsPerRow=3, subImgSize=(200, 200))
    return img
