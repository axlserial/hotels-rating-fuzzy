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

# --/ facilities quality /--
# Careless, Care, Excellent

facilities["careless"] = sk.trapmf(facilities.universe, [0, 0, 3, 4])
facilities["care"] = sk.trapmf(facilities.universe, [3.5, 5, 7, 8])
facilities["excellent"] = sk.trapmf(facilities.universe, [6, 8.5, 10.1, 10.1])

# --/ staff attentions /--
# Poor, Fair, Good, Excellent

staff["poor"] = sk.trapmf(staff.universe, [0, 0, 2, 4])
staff["fair"] = sk.trapmf(staff.universe, [3, 5, 6.5, 8])
staff["good"] = sk.trapmf(staff.universe, [6, 7, 8.5, 10])
staff["excellent"] = sk.trapmf(staff.universe, [8, 9, 10, 10.1])

# --/ price /--
# Cheap, Regular, Expensive

price["cheap"] = sk.trapmf(price.universe, [0, 0, 500, 700])
price["regular"] = sk.trapmf(price.universe, [450, 700, 1500, 1850])
price["expensive"] = sk.trapmf(price.universe, [1600, 2000, 15000, 15001])


# Definition output membership functions

# --/ hotel rating /--
# Very Poor, Poor, Fair, Good, Excellent

rating["very poor"] = sk.trapmf(rating.universe, [0, 0, 3, 3.5])
rating["poor"] = sk.trapmf(rating.universe, [1.5, 3.5, 5, 5.5])
rating["fair"] = sk.trapmf(rating.universe, [4, 5.5, 7, 7.5])
rating["good"] = sk.trapmf(rating.universe, [5.5, 7.5, 9, 10])
rating["excellent"] = sk.trapmf(rating.universe, [9, 9.5, 10, 10.1])


# Definition rules

# --/ rules /--

# Rule 1: if facilities is careless and Staff is poor and price is expensive then rating is very poor

rule1 = ctrl.Rule(
    facilities["careless"] and staff["poor"] and price["expensive"], rating["very poor"]
)

# Rule 2: if facilities is poor and price is regular then rating is poor

rule2 = ctrl.Rule(facilities["care"] and price["regular"], rating["poor"])

# Rule 3: if facilities is careless and Staff is fair or good and price is cheap regular then rating is fair

rule3 = ctrl.Rule(
    facilities["careless"] and staff["fair"] or staff["good"] and price["regular"],
    rating["fair"],
)

# Rule 4: if Staff is excellent and price is cheap then rating is good

rule4 = ctrl.Rule(staff["excellent"] and price["cheap"], rating["good"])

# Rule 5: if facilities is excellent and Staff is excellent and price is cheap or regular then rating is excellent

rule5 = ctrl.Rule(
    facilities["excellent"] and staff["excellent"] and price["cheap"] or price["regular"],
    rating["excellent"],
)


# Definition control system

rating_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5])
rating_hotel = ctrl.ControlSystemSimulation(rating_ctrl)

# Test

# --/ test 1 /--

rating_hotel.input["facilities"] = 9.0

rating_hotel.compute()

print(rating_hotel.output["rating"])