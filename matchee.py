class Matchee(object):
    """
    An instance of a unique object to match with Attributes
        name: the name of the matchee (String)
        priorities: List
    """

    # @property
    # def name(self):
    #     """The name of the matchee"""
    #     return self._name

    # @name.setter
    # def name(self, value):
    #     self._name = value

    # @property
    # def priorities(self):
    #     """The priorities of that matchee
    #     Must be a list"""
    #     return self.priorities

    # @priorities.setter
    # def priorities(self, value):
    #     assert type(value) == list, "value %s is not a list" % repr(value)
    #     self._priorities = value

    # Initializer
    def __init__(self, name, priorities):
        """Constructor for a matchee object with the given name and priorities"""
        self.name = name
        self.priorities = priorities

    def __repr__(self):
        return self.name
