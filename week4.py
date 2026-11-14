
from sympy import symbols, Not, Implies, Xor, satisfiable

# Symbols
r = symbols('Rain')
h = symbols('Harry_Hagrid')
d = symbols('Harry_Dumbledore')

def test(name, kb):
    print("\n" + name)
    print("=" * 30)
    res = satisfiable(kb)
    print("Result:", res)

    if res is False:
        print("Contradiction")
    elif r in res:
        if res[r]:
            print("It rained")
        else:
            print("No rain")
    else:
        print("Rain cannot be determined")

# Test Case 1
kb1 = Implies(Not(r), h) & Xor(h, d) & d
test("Test Case 1", kb1)

# Test Case 2
kb2 = Implies(Not(r), h) & Xor(h, d) & (h & Not(r))
test("Test Case 2", kb2)