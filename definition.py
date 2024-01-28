import numpy as np
import skfuzzy as sk
from skfuzzy import control as ctrl

# Definition input variables

# --/ facilities quality /--
# 1.0 - 10.0

facilities_range = np.arange(1, 10.1, 0.1)
facilities = ctrl.Antecedent(facilities_range, "facilities")

# --/ staff attentions /--
# 1.0 - 10.0

staff_range = np.arange(1, 10.1, 0.1)
staff = ctrl.Antecedent(staff_range, "staff")

# --/ price /--
# $0.00 - $15,000.00

price_range = np.arange(0, 15001, 0.01)
price = ctrl.Antecedent(price_range, "price")


# Definition output variables

# --/ hotel rating /--
# 1.0 - 10.0

rating_range = np.arange(1, 10.1, 0.1)
rating = ctrl.Consequent(rating_range, "rating")


# Definition membership functions
# TODO
