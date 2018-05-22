# -*- coding:utf-8 -*-
class PIC:
    def __init__(self, data):
        self.size = dict(
            width=data['width'],
            heigh=data['heigh']
        )
        self.data = data['data']

        self.weight_points = self.init_weight_points()
        self.count_weight_points = len(self.weight_points)
        self.time = 50

    def show(self):
        return self.size

    def get_point(self, x=0, y=0):
        return self.data[x][y]

    @staticmethod
    def init_weight_points():
        return [
            {
                'value': 50,
                'sum_val': 0,
                'sum_num': 0
            },
            {
                'value': 150,
                'sum_val': 0,
                'sum_num': 0
            },
            {
                'value': 200,
                'sum_val': 0,
                'sum_num': 0
            }
        ]

    def k_means_fuc(self):
        for i in range(0, 20):
            self.k_means_once()
        for i in range(self.size['width']):
            for j in range(self.size['heigh']):
                self._set(i, j)
                pass
        return self.data

    def k_means_once(self):
        for i in range(self.size['width']):
            for j in range(self.size['heigh']):
                # one point for value in split points
                self.get_belong(self.data[i, j])
        self.reset_point()

    def reset_point(self):
        for index, point in enumerate(self.weight_points):
            if self.weight_points[index]['sum_num'] == 0:
                break
            self.weight_points[index]['value'] = int(
                self.weight_points[index]['sum_val'] / self.weight_points[index]['sum_num'])
            self.weight_points[index]['sum_val'] = 0
            self.weight_points[index]['sum_num'] = 0

    def get_belong(self, weight):
        most_close_distance = 99999
        most_close_index = 0
        for index, point in enumerate(self.weight_points):
            distance = abs(self.weight_points[index]['value'] - weight)
            if distance < most_close_distance:
                most_close_distance = distance
                most_close_index = index
        self.weight_points[most_close_index]['sum_val'] += weight
        self.weight_points[most_close_index]['sum_num'] += 1

    def _set(self, x, y):
        weight = self.data[x, y]
        most_close_distance = 9999
        for index, point in enumerate(self.weight_points):
            distance = abs(self.weight_points[index]['value'] - weight)
            if distance < most_close_distance:
                most_close_distance = distance
                most_close_index = index
        self.data[x, y] = self.weight_points[most_close_index]['value']

