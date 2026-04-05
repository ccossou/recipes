"""
Functions to compute quantities of water and salt depending on various parameters
"""


def salaison(meat, water, salt_per_kg):
    """
    Compute salt quantity needed in the water to achieve the desired salt rate in the meat/fish.

    :param float meat: meat mass in kg
    :param float water: Water mass in kg
    :param salt_per_kg: desired salt quantity (in grams) per kg of meat
    :return: Salt quantity in grams to add in the water
    """
    total_mass = meat + water
    sugar_per_kg = salt_per_kg / 10

    salt = total_mass * salt_per_kg
    sugar = total_mass * sugar_per_kg

    print("Salage:")
    print(f"* meat: {meat:.3f} kg")
    print(f"* water: {water:.3f} kg")
    print(f"* salt_per_kg: {salt_per_kg:.1f} g ({salt_per_kg/10:.1f} g/100g)")

    print(f"\nAdd to water:")
    print(f"* salt: {salt:.1f}g")
    print(f"* sugar: {sugar:.1f}g")


def dessalage(meat, in_salt_per_kg, out_salt_per_kg):
    """
    Compute the amount of water to use on the salted meat to remove the desired amount of salt.

    Note that you need to remove the initial salted water first.

    :param float meat: meat mass in kg
    :param in_salt_per_kg: actual salt quantity (in grams) per kg of meat
    :param out_salt_per_kg: desired salt quantity (in grams) per kg of meat
    :return: water quantity in kg to remove the desired quantity of salt from the meat
    """

    if in_salt_per_kg < out_salt_per_kg:
        msg = f"Out rate ({out_salt_per_kg:.1}g/kg) need to be smaller than in rate ({in_salt_per_kg:.1}g/kg))"
        raise ValueError(msg)
    water = meat * ((in_salt_per_kg / out_salt_per_kg) - 1)

    print("Dessalage:")
    print(f"* meat: {meat:.3f} kg")
    print(f"* avant dessalage: {in_salt_per_kg:.1f} g ({in_salt_per_kg/10:.1f} g/100g)")
    print(f"* après dessalage: {out_salt_per_kg:.1f} g ({out_salt_per_kg/10:.1f} g/100g)")

    print(f"\nWater needed: {water:.3f} kg")

def salaison_ajout_eau(water, salt_per_kg):
    """
    When you didn't used enough water initially, compute how much salt you need to add depending on how much water you
    added.

    :param float water: Water mass in kg
    :param salt_per_kg: desired salt quantity (in grams) per kg of meat
    """
    sugar_per_kg = salt_per_kg / 10

    salt = water * salt_per_kg
    sugar = water * sugar_per_kg

    print("Salaison, ajout eau:")
    print(f"* water: {water:.3f} kg")
    print(f"* salt_per_kg: {salt_per_kg:.1f} g ({salt_per_kg/10:.1f} g/100g)")

    print(f"\nAdd to water:")
    print(f"* salt: {salt:.1f}g")
    print(f"* sugar: {sugar:.1f}g")

# # salaison(meat=0.2, water=0.2, salt_per_kg=21)
# salaison(meat=0.21, water=0.2, salt_per_kg=42)
# salaison(meat=0.21, water=0.2, salt_per_kg=120)
# # salaison(meat=0.857, water=1, salt_per_kg=35)
#
# # Only use if you did not used enough water initially, to compute how much salt you need to add as well
# salaison_ajout_eau(water=0.02, salt_per_kg=42)

dessalage(meat=0.34, in_salt_per_kg=120, out_salt_per_kg=21)