from tests import *

valid_tests = (
    CoughAndFever,
    CoughAndFever1090,
    DistributionNonUniformStatDep,
    DistributionUniformStatDep,
    DistributionNonUniformStatIndep,
)
valid_tests_dico = {e.name: e for e in valid_tests}

# not working yet
# "faithfulness": tests.Faithfulness,
# "roar_faithfulness": tests.ROARFaithfulness,
# "roar_monotonicity": tests.ROARMonotonicity,
# "monotonicity": tests.Monotonicity,
# "roar": tests.Roar,
# "shapley": tests.Shapley,
# "shapley_corr": tests.ShapleyCorr,
# "infidelity": tests.Infidelity
