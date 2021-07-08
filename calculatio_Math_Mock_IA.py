# Calculation for "Joint Probability of Getting A Five Star
# in Normal Lucky Draw of Genshin Impact" (Jessica Li)
# 
# Models developed by Jessica Li
# Code ©Cynthia Wang 2021

first_model = 0

for i in range(1, 90):
    first_model += 0.006 * (0.994)**(i-1) * i
first_model += (0.994)**89 * 90


second_model = 0

for i in range(1, 74):
    second_model += 0.006 * (0.994)**(i-1) * i

fail_probabilities = []

for j in range(74, 90):
    j_probability = (0.994)**73 * (0.006+(j-73)*0.06)
    for p in fail_probabilities:
        j_probability *= p
    fail_probabilities.append(1-(0.006+(j-73)*0.06))
    second_model += j_probability * j

print(1.0/first_model, 1.0/second_model)
