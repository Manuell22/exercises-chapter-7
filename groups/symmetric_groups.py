from exercises-chapter-7.example_code.groups import Group
import numpy as np

class SymmetricGroup(Group):
    symbol = "S"

    def _validate(self, value):
        """Ensure that value is an allowed element value in this group."""
        if not isinstance(value, (np.ndarray, list, tuple))\
           and all(i not in value for i in range(self.n)):
            raise ValueError("must be a permutation")

    def operation(self, a, b):
        """Perform the group operation on two values.

        The group operation is addition modulo n.
        """
        return np.ndarray(a)[np.ndarray(b)]

