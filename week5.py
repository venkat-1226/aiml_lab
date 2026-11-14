
# Bayesian Network

P_burglary = 0.002
P_earthquake = 0.001

P_alarm = {
    (True, True): 0.94,
    (True, False): 0.95,
    (False, True): 0.31,
    (False, False): 0.001
}

P_david = {True: 0.91, False: 0.05}
P_sophia = {True: 0.75, False: 0.02}

def joint_probability(alarm, burglary, earthquake,
                      david, sophia):

    pb = P_burglary if burglary else 1-P_burglary
    pe = P_earthquake if earthquake else 1-P_earthquake

    pa = P_alarm[(burglary, earthquake)]
    pa = pa if alarm else 1-pa

    pd = P_david[alarm] if david else 1-P_david[alarm]
    ps = P_sophia[alarm] if sophia else 1-P_sophia[alarm]

    return pb * pe * pa * pd * ps

# Test Case 1
print("Test Case 1")
print("Joint Probability:",
      joint_probability(True, False, False, True, True))

# Test Case 2
print("\nTest Case 2")
print("Joint Probability:",
      joint_probability(True, True, False, True, True))
