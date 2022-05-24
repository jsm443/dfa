def match(pr, ac):
    """A method which match from the proposers (pr) to the accepter/rejecter ac

    Preconditions: pr must be a list of matchees whose priorities are elements of ac.
    ac must be a list of matchees whose priorities are empty or match the elements of
    pr."""
    num_proposers = pr.len
    choice = [0]*num_proposers
    matches = []*num_proposers
    proposer_id = 0
    for proposer in pr:
        matches[proposer_id] = proposer.priorities[choice[proposer_id]]

    for accepter in ac:
        num_matches = matches.count(accepter)
        if num_matches > 1:
            match_index = matches.index(accepter) #The index of the proposing matchee object
            prefrence = pr[match_index]
            #match_index_tracker = [] #tracks the positions of proposers whose choice are accepter
            while match_index != -1:
                #match_index_tracker.push(match_index)
                to_compare = pr[match_index]
                if accepter.priorities.index(prefrence)>accepter.priorities.index(to_compare):







'''
def propose(p, a):
    """Handles the proposals from proposers p (list) to aceepter/rejecter a (matchee)"""
    priorities = a.priorities
    choice = 0

    def track_accept_or_reject(priorities, a, choice):
        """Recursive function which takes in the priorities and accept/reject agent, and the choice # being examined
        returns the """
        location = a.find(priorities[choice])
        if location != -1:
            return p
        else:
            track_accept_or_reject(priorities, a, choice + 1)

    track_accept_or_reject(priorities, a, 0)
'''

