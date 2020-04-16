

from csp_lib.backtrack_util import (first_unassigned_variable,
                                    unordered_domain_values,
                                    no_inference)

from csp_lib.csp import CSP


def backtracking_search(csp,
                        select_unassigned_variable=first_unassigned_variable,
                        order_domain_values=unordered_domain_values,
                        inference=no_inference):
    """backtracking_search
    Given a constraint satisfaction problem (CSP),
    a function handle for selecting variables, 
    a function handle for selecting elements of a domain,
    and a set of inferences, solve the CSP using backtrack search
    """

    # See Figure 6.5] of your book for details

    def backtrack(assignment):
        """Attempt to backtrack search with current assignment
        Returns None if there is no solution.  Otherwise, the
        csp should be in a goal state.
        """
        if vars_Assigned(csp):
            return dict(csp.curr_domains)

        var = select_unassigned_variable(assignment, csp)
        for val in order_domain_values(var, assignment, csp):
            if csp.nconflicts(var, val, assignment) is 0:
                csp.assign(var, val, assignment)
                removals = list()
                inf = inference(csp, var, val, assignment, removals)
                if inf is not None or inf:
                    removals += csp.suppose(var, val)
                    # recursivecall
                    rcrse = backtrack(assignment)
                    if rcrse is not None:
                        return rcrse
                    csp.restore(removals)
                    csp.unassign(var, assignment)
        return None
    # Call with empty assignments, variables accessed
    # through dynamic scoping (variables in outer
    # scope can be accessed in Python)
    result = backtrack({})
    assert result is None or csp.goal_test(result)
    return result


def vars_Assigned(csp):
    for v in csp.curr_domains:
        if len(csp.curr_domains[v]) is not 1:
            return False
    return True
