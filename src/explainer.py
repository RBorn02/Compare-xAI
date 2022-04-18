from explainers import *
from src.utils import are_class_names_unique

valid_explainers = (
    Random,
    TreeShap,
    Saabas,
    Archipelago,
    ShapleyTaylorInteraction,
    Anova,
    KernelShap,
    Sage,
    ShapInteraction,
    Lime,
    Maple,
)
assert are_class_names_unique(valid_explainers), 'Duplicate explainer names'

valid_explainers_dico = {e.name: e for e in valid_explainers}
# not working yet
# BreakDown,  # need cpp14
# "shap": explainers.Shap,
# "shapr": explainers.ShapR,
# "brutekernelshap": explainers.BruteForceKernelShap,
# "l2x": explainers.L2X,

if __name__ == '__main__':
    import numpy as np

    test = Lime(predict_func=lambda x: x, X=np.array([[0, 0] * 5]))
    print(test)
