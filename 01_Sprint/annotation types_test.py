from typing import Sequence,Set, Union

var_sequence: Sequence[float] = [1.2, 2, 3]
# и принимает множество
var_sequence1: Set[Union[float, int]] = {1.2, 2, 3}

print(var_sequence1)
