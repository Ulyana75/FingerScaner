
class SpecialPointsFinder:
    @staticmethod
    def checkPoint(img, x, y):   # Считаем количество черных пикселей в окрестности точки
        k = 0
        for i in range(x - 1, x + 2):
            for j in range(y - 1, y + 2):
                if img[i][j] == 0:
                    k += 1
        return k - 1

    @staticmethod
    def findSpecialPoint(img):   # Получаем два кортежа: конечные точки и точки ветвления
        x, y = img.shape
        branch_points = []
        end_points = []
        for i in range(x):
            for j in range(y):
                t = 0
                if img[i][j] == 0:
                    try:
                        t = SpecialPointsFinder.checkPoint(img, i, j)
                    except:
                        pass
                    if t == 1:
                        end_points.append((i, j))
                    if t == 3:
                        branch_points.append((i, j))
        return SpecialPointsFinder.deleteNoisePoint((branch_points, end_points))

    @staticmethod
    def comparePoint(r, v):   # Сравниваем пары кортежей разных отпечатков в области 30х30 пикселей
        _all = 0
        match = 0
        for i in v[0]:
            x = range(i[0] - 15, i[0] + 15)
            y = range(i[1] - 15, i[1] + 15)
            _all += 1
            for j in r[0]:
                if j[0] in x and j[1] in y:
                    match += 1
                    break
        for i in v[1]:
            x = range(i[0] - 15, i[0] + 15)
            y = range(i[1] - 15, i[1] + 15)
            _all += 1
            for j in r[1]:
                if j[0] in x and j[1] in y:
                    match += 1
                    break

        return match, _all

    @staticmethod
    def removeSprouts(x, y):   # Удаление отростков
        for i in y:
            try:
                x.remove(i)
            except:
                pass
        return x

    @staticmethod
    def deleteNoisePoint(r):   # Поиск шумовых отростков
        tmp_end = []
        tmp_branch = []
        for i in r[1]:
            x = range(i[0] - 5, i[0] + 5)
            y = range(i[1] - 5, i[1] + 5)
            for j in r[0]:
                if j[0] in x and j[1] in y:
                    tmp_end.append(i)
                    tmp_branch.append(j)
        return SpecialPointsFinder.removeSprouts(r[0], tmp_branch), SpecialPointsFinder.removeSprouts(r[1], tmp_end)
