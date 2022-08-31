import matchee


def match(pr, ac):
    """A method which matches the proposers (pr) to the accepter/rejecter ac

    Preconditions: pr must be a list of matchees whose priorities are elements of ac.
    ac must be a list of matchees whose priorities are empty or match the elements of
    pr."""
    num_proposers = len(pr)
    # Lists of each proposer (in orders) current proposed to acceptee.
    matches = [pr[0]] * num_proposers
    proposer_id = 0
    for proposer in pr:
        matches[proposer_id] = proposer.priorities[0]
        proposer_id += 1

    # at this point the "matches" array is each proposers first choice.

    def get_match_index(cur_index):
        """Helper function to safely find the the index of the proposer in
        matches.  Takes cur_index as the current location of the examined
         match.  Enter -1 if examining a new match."""
        try:
            return matches[(cur_index + 1) :].index(accepter) + cur_index + 1
        except:
            return -1

    def is_matched(match_set):
        """Returns true if the given match is completed and false otherwise"""
        for accepters in ac:
            if match_set.count(accepters) > 1:
                return False
        return True

    while not is_matched(matches):
        for accepter in ac:
            # the number of time the accepter is proposed to.
            num_matches = matches.count(accepter)
            if (
                num_matches > 1
            ):  # evaluates if an accepter is requested more than once by a proposer
                match_index = get_match_index(-1)
                prefrence = pr[match_index]
                checked = [prefrence]
                match_index = get_match_index(
                    match_index
                )  # finds the index of the given accepter in the matches array.  This also corresponds to the proposer index
                while match_index != -1:
                    to_compare = pr[match_index]
                    checked.append(to_compare)
                    if accepter.priorities.index(prefrence) < accepter.priorities.index(
                        to_compare
                    ):  # this is the case where the match that comes first in the proposers array is chosen over the later proposer by the accepter
                        match_index = get_match_index(match_index)
                    else:
                        prefrence = pr[match_index]
                        match_index = get_match_index(match_index)
                while len(checked) > 0:
                    if checked[0] != prefrence:
                        bad_match_index = pr.index(
                            checked[0]
                        )  # matches.index(checked[0].priorities[0])
                        checked[0].priorities = checked[0].priorities[1:]
                        new_match = checked[0].priorities[0]
                        matches[bad_match_index] = new_match

                    checked.pop(0)

    for m in matches:
        print(m)
