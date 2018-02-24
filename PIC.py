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
                'value': 200,
                'sum_val': 0,
                'sum_num': 0
            }
        ]

    def k_means_fuc(self):
        for i in range(self.size['width']):
            for j in range(self.size['heigh']):
                # one point for value in split points
                self.get_belong(self.data[i][j])
                # got the smallest
                key = distant.index( min(distant) )
                # belong and add
                start_point[key]['sum_val'] += self.data[i][j]
                start_point[key]['sum_num'] += 1

        exit()
        # replace split_points
        # for i in range(split_num):
        #     start_point[i]['value'] = int(start_point[i]['sum_val'] / start_point[i]['sum_num'])
        #     start_point[i]['sum_val'] = 0
        #     start_point[i]['sum_num'] = 0
        #
        # self.start_point = start_point

    def get_belong(self, data):
        dist = []
        for key, value in enumerate(self.weight_points):
            dist.append(abs(data-value['value']))
        exit()














