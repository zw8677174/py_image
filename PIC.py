# -*- coding:utf-8 -*-
class PIC:

    def __init__(self, data):
        self.size = dict(
            width=data['width'],
            heigh=data['heigh']
        )
        self.data = data['data']
        self.slip_num = 2
        self.time = 50
        self.start_point = dict()
        self.distant = dict()

    def show(self):
        return self.size

    def get_point(self, x=0, y=0):
        return self.data[x][y]

    def init_point(self):
        self.start_point = [
            {
                'value': 50,
                'sum_val': 0,
                'sum_num': 0
            },
            {
                'value': 200,
                'sum_val': 0,
                'sum_num': 0
            },
        ]
        self.distant = [0,0]

    def k_means_fuc(self):

        # init
        split_num = self.slip_num
        start_point = self.start_point
        distant = self.distant

        for i in range(self.size['width']):
            for j in range(self.size['heigh']):
                # one point for value in split points
                for k in range(split_num):
                    distant[k] = abs(self.data[i][j]-start_point[k]['value'])
                # got the smallest
                key = distant.index( min(distant) )
                # belong and add
                start_point[key]['sum_val'] += self.data[i][j]
                start_point[key]['sum_num'] += 1

        # replace split_points
        for i in range(split_num):
            start_point[i]['value'] = int(start_point[i]['sum_val'] / start_point[i]['sum_num'])
            start_point[i]['sum_val'] = 0
            start_point[i]['sum_num'] = 0

        self.start_point = start_point

    def iteration(self):
        for i in range(self.time):
            self.k_means_fuc()

    def result_data(self):

        split_num = self.slip_num
        start_point = self.start_point
        distant = self.distant

        for i in range(self.size['width']):
            for j in range(self.size['heigh']):
                # one point for value in split points
                for k in range(split_num):
                    distant[k] = abs(self.data[i][j]-start_point[k]['value'])
                # got the smallest
                key = distant.index( min(distant) )
                value = ran


















