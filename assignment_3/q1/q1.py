##############################################################
# Name : Kang Chin Shen
# Section : G3
##############################################################
import cvxpy as cp
import sympy as sp

def ilp(expr):
    """Check satisfiability of a propositional sentence via a ILP.
    Args:
        expr: a logic expression (in Sympy Format)
    Returns:
        (Boolean) True if satisfiable; Otherwise, false.
    """

    # Transform expr into cvxpy variables
    cvx_var = var_from_expr(expr)

    # Construct the objective: minimization
    objective = cp.Minimize(cp.sum(list(cvx_var.values()))) 

    # Construct the constraints
    constraints = define_constraints(expr, cvx_var)

    # Construct cvxpy problem
    problem = cp.Problem(objective, constraints)

    # Solve the problem using ECOS_BB solver
    problem.solve(solver='ECOS_BB')

    # Return the result
    return problem.status not in ('infeasible', 'unbounded')

def define_constraints(expr, var_dict):
    '''
    Args:
        expr: a CNF logic expression (in Sympy Format),
        var_dict: a dictionary with <key, value> as <variable_name:string, var:cvxpy_variable>
    Returns:
        a list of constraints with each clause separated by AND and >= 1
    '''

    # Create a list of clauses based on expr
    clauses = list(expr.args)

    # Create a list to store the constraints
    constraints = []

    # Iterate through clauses
    for clause in clauses:

        # Initialize LHS as 0
        LHS = 0

        # Create LHS for different scenarios
        if(clause.func is sp.Or):
            LHS = create_LHS(clause.args, var_dict)
        else:
            LHS = create_LHS([clause], var_dict)

        # Append constraint
        constraints.append(LHS >= 1)
    
    return constraints

        

# ---- Helper functions ----
def var_from_expr(expr):
    """
    Transform expr into cvxpy variables 
    """
    var_dict = {}
    for atom in expr.atoms():
        var_dict[str(atom)] = cp.Variable(boolean=True)    
    return var_dict

def create_LHS(symbols: list, var: dict):
    """Create left-hand side (LHS) of a constraint in ILP.

    This function returns the summation of a list of symbols which
    is used to construct constraints of this ILP.
    E.g. symbols = [x0, x1, ~x2] will be converted into `x0 + x1 +
    1 - x2, called expression. You can then use this expression to 
    construct:
        Equality constraint:   `x0 + x1 + 1 - x2 == 1`
        Inequality constraint: `x0 + x1 + 1 - x2 <= 1`

    Note:
        This function is not necessary. Please feel free to develop
        your own help function. 
    
    Args:
        symbols: a list contains sympy.core.symbol.Symbol (or strings)
        var: a dictionary contains cvxpy variables. 
    """

    con_LHS = 0
    for s in symbols:
        s = str(s)
        if s[0] == '~': # if its logic Not, plus `1-variable`
            con_LHS += 1-var[s[1:]]
        else:           # else, plus `variable`
            con_LHS += var[s]
    return con_LHS
