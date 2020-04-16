'''
Constraint propagation
'''
from csp_lib.csp import CSP


def AC3(csp, queue=None, removals=None):
    """AC3 constraint propagation

    """
    if queue is None:
        #populate
        queue = [(c, n) for c in csp.curr_domains for n in csp.neighbors[c]]

    def compute(c, n):
        #funcion to check for constraints
        #initially false
        #return true if out of the curr loop
        check = False
        for x in csp.curr_domains[c]:
            if not any([csp.constraints(c, x, n, y) for y in csp.curr_domains[n]]):
                csp.prune(c, x, removals)
                check = True
            return check
    #check all elems in queue
    while queue:
        c, n = queue.pop()
        if compute(c, n):
            if csp.domains[c] is None:
                return False
            for x in csp.neighbors[c]:
                if (x, c) not in queue:
                    queue.append((x, c))
    return True

    # Hints:
    # Remember that:
    #    csp.variables is a list of variables
    #    csp.neighbors[x] is the neighbors of variable x
