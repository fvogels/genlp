import random
import pulp


def print_solutions(model):
    for var in model.variables():
        print(f'{var.name}: {var.value()}')


def example():
    model = pulp.LpProblem(sense=pulp.LpMaximize)
    x = pulp.LpVariable(name="x", lowBound=0)
    y = pulp.LpVariable(name="y", lowBound=0)

    # Constraints
    model += (2*x + y <= 10)
    model += (x + 3*y <= 10)

    # Goal
    model += x + y

    # Solve
    model.solve(pulp.PULP_CBC_CMD(msg=0))

    return model


def generate_maximization_problem(varnames = ['x', 'y', 'z'], nplanes=4):
    model = pulp.LpProblem(sense=pulp.LpMaximize)
    vars = [pulp.LpVariable(name=varname, lowBound=0) for varname in varnames]
    nvars = len(varnames)
    point = [random.randint(1,8) for _ in range(nvars)]
    maximization_coefficients = [random.randint(1,8) for _ in range(nvars)]

    for _ in range(nplanes):
        coefficients = [x + random.randint(-2,2) for x in maximization_coefficients]
        bound = [c * v for c, v in zip(coefficients, point)]
        model += sum(c * v for c, v in zip(coefficients, vars)) <= bound

    model += sum(c * v for c, v in zip(maximization_coefficients, vars))

    model.solve(pulp.PULP_CBC_CMD(msg=0))

    return model


def generate_minimization_problem(varnames = ['x', 'y', 'z'], nplanes=4):
    model = pulp.LpProblem(sense=pulp.LpMinimize)
    vars = [pulp.LpVariable(name=varname, lowBound=0) for varname in varnames]
    nvars = len(varnames)
    point = [random.randint(1,8) for _ in range(nvars)]
    maximization_coefficients = [random.randint(1,8) for _ in range(nvars)]

    for _ in range(nplanes):
        coefficients = [x + random.randint(-2,2) for x in maximization_coefficients]
        bound = [c * v for c, v in zip(coefficients, point)]
        model += sum(c * v for c, v in zip(coefficients, vars)) >= bound

    model += sum(c * v for c, v in zip(maximization_coefficients, vars))

    model.solve(pulp.PULP_CBC_CMD(msg=0))

    return model


varnames = 'xyz'
nplanes = 5
# model = generate_minimization_problem(varnames, nplanes)
model = generate_maximization_problem(varnames, nplanes)

print(model)
print_solutions(model)