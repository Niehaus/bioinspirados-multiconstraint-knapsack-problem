class Util:
    def __init__(self, filepath):
        self._object_count = 0
        self._profit = []
        self._capacity = []
        self._constraints = []
        self._known_optimum = 0
        self._knapsack_count = 0

        file_as_str = open(filepath).read().split()

        self._knapsack_count = int(file_as_str.pop(0))
        self._object_count = int(file_as_str.pop(0))

        for _ in range(self._object_count):
            self._profit.append(int(file_as_str.pop(0)))

        for _ in range(self._knapsack_count):
            self._capacity.append(int(file_as_str.pop(0)))

        for i in range(self._knapsack_count):
            self._constraints.append([])
            for _ in range(self._object_count):
                self._constraints[i].append(int(file_as_str.pop(0)))

        self.known_optimum = int(file_as_str.pop(0))

    def show_entries(self):
        print(f'Capacidade das Mochilas: {self._capacity} \n'
              f'Quantidade de Mochilas: {self._knapsack_count} \n'
              f'Ótimo: {self.known_optimum}')

    @staticmethod
    def bigger(a, b):
        if a > b:
            return a
        else:
            return b

    def _weight(self, x, i):
        total_weight = 0

        for j in range(len(x)):
            if x[j]:
                total_weight += self._constraints[i][j]

        return total_weight

    def calculate_fo(self, x):
        function = 0

        for i in range(len(x)):
            if x[i] == 1:
                function += self._profit[i]

        penalty = sum(self._profit)

        for i in range(self._knapsack_count):
            function -= penalty * self.bigger(0, self._weight(x, i) - self._capacity[i])

        return function

    @property
    def object_count(self):
        return self._object_count
