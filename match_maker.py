def match(pr, ac):
    """A method which matches the proposers (pr) to the accepter/rejecter ac

    Preconditions: pr must be a list of matchees whose priorities are elements of ac.
    ac must be a list of matchees whose priorities are empty or match the elements of
    pr."""
    num_proposers = pr.len
    choice = [0]*num_proposers
    # Lists of each proposer (in orders) current proposed to acceptee.
    matches = []*num_proposers
    proposer_id = 0
    for proposer in pr:
        matches[proposer_id] = proposer.priorities[choice[proposer_id]]

    def match_index(cur_index):
        """Helper function to safely find the the index of the proposer in
         matches.  Takes cur_index as the current location of the examined
          match.  Enter -1 if examining a new match."""
        try:
            return matches[(
                cur_index + 1):].index(accepter)
        except:
            return -1

    def is_matched(match_set):
        """Returns true if the given match is completed and false otherwise"""
        for accepters in ac:
            if match_set.count(accepter) > 1:
                return False
        return True

    while not is_matched(matches):
        for accepter in ac:
            # the number of time the accepter dis proposed to.
            num_matches = matches.count(accepter)
            if num_matches > 1:
                match_index = match_index(-1)
                prefrence = pr[match_index]
                checked = [prefrence]
                match_index = matches[(match_index + 1):].index(accepter)
                # match_index_tracker = [] #tracks the positions of proposers whose choice are accepter
                while match_index != -1:
                    # match_index_tracker.push(match_index)
                    to_compare = pr[match_index:]
                    checked.append(to_compare)
                    if accepter.priorities.index(prefrence) < accepter.priorities.index(to_compare):
                        prefrence = pr[match_index]
                        match_index = match_index(match_index)
                    else:
                        match_index = match_index(match_index)
                while len(checked) > 0:
                    if checked[0] != prefrence:
                        checked[0].priorities.pop(0)
                        matches[matches.index(checked[0])
                                ] = checked[0].priorities[0]

    print(matches)
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
