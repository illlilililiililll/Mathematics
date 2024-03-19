import pulp

A = pulp.LpVariable("A", lowBound=0) #있음_낮
a = pulp.LpVariable("a", lowBound=0) #있음_밤
B = pulp.LpVariable("B", lowBound=0) #없음_낮
b = pulp.LpVariable("b", lowBound=0) #없음_밤

model = pulp.LpProblem("test_lp", pulp.LpMinimize)

model += 2*A + 2.5*a + 1.8*B + 2*b

model += A+a >= 400
model += B+b >= 400
model += A+B+a+b == 1000
model += a >= (A+a)*0.4
model += b >= (B+b)*0.6

model.solve()

print(pulp.value(model.objective))

print(f"자녀가 있는 가구 - 낮 {int(A.varValue)}")
print(f"자녀가 있는 가구 - 밤 {int(a.varValue)}")
print(f"자녀가 없는 가구 - 낮 {int(B.varValue)}")
print(f"자녀가 없는 가구 - 밤 {int(b.varValue)}")