import pulp

A = pulp.LpVariable("A", lowBound=0)
B = pulp.LpVariable("B", lowBound=0)

model = pulp.LpProblem("test_lp", pulp.LpMaximize)

model += 20*A + 40*B

model += 0.5*A + B <= 30
model += A + 2.5*B <= 60
model += A + 2*B <= 22

model.solve()

print(pulp.value(model.objective))

print(f"A {A.varValue}")
print(f"B {B.varValue}")