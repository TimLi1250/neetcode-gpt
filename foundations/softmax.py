import numpy as np
from numpy.typing import NDArray


class Solution:

    def softmax(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        # z is a 1D NumPy array of logits
        # Hint: subtract max(z) for numerical stability before computing exp
        # return np.round(your_answer, 4)
        maximum = max(z)
        sum = 0
        for i in z:
            exp = i - maximum
            num = math.e ** exp
            sum += num
        z = [(math.e ** (i - maximum) / sum) for i in z]
        print(z)
        return np.round(z, 4)

