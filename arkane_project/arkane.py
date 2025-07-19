# Arkane input file for the SN2 reaction from pre-formed complexes

# Define the species. Note that the reactant and product are the entire
# complexes, not the individual molecules.
species('ReactantComplex', 'reactant_complex.out')
species('ProductComplex', 'product_complex.out')

# Define the transition state, making sure to flag it as such.
# Arkane will use the single imaginary frequency from this file.
species('TS', 'ts.out', is_ts=True)

# Define the unimolecular reaction from the reactant complex to the
# product complex, passing through our calculated transition state.
reaction(
    label = 'SN2_Complex',
    reactants = ['ReactantComplex'],
    products = ['ProductComplex'],
    transitionState = 'TS',
)

# Tell Arkane to perform a kinetics job on our defined reaction.
kinetics('SN2_Complex')
