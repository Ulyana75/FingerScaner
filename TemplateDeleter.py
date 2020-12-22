

class TemplateDeleter:
    @staticmethod
    def delete(img, w, h):   # Удаление пикселей, подходящих под основной набор шаблонов
        count = 0
        for i in range(1, h - 1):
            for j in range(1, w - 1):
                if img[j][i] == 0 and TemplateDeleter.deletable(img, j, i):
                    img[j][i] = 1
                    count += 1
        return count

    @staticmethod
    def deletable(img, x, y):   # Подготавливаем матрицу для проверки соответствия основному набору шаблонов
        a = []
        for i in range(y - 1, y + 2):
            for j in range(x - 1, x + 2):
                a.append(img[j][i])
        return TemplateDeleter.check(a)

    @staticmethod
    def check(a):   # Проверяем соответствие основному набору шаблонов
        t1 = [1, 1, 0, 0, 1, 0]
        t2 = [1, 1, 1, 0, 0, 0]
        t3 = [0, 1, 0, 0, 1, 1]
        t4 = [0, 0, 0, 1, 1, 1]
        t5 = [1, 1, 1, 0, 0, 0, 0]
        t6 = [1, 0, 1, 0, 0, 1, 0]
        t7 = [0, 0, 0, 0, 1, 1, 1]
        t8 = [0, 1, 0, 0, 1, 0, 1]

        t = [a[1], a[2], a[3], a[4], a[5], a[7]]
        if t == t1:
            return True
        t = [a[0], a[1], a[3], a[4], a[5], a[7]]
        if t == t2:
            return True
        t = [a[1], a[3], a[4], a[5], a[6], a[7]]
        if t == t3:
            return True
        t = [a[1], a[3], a[4], a[5], a[7], a[8]]
        if t == t4:
            return True
        t = [a[0], a[1], a[2], a[3], a[4], a[5], a[7]]
        if t == t5:
            return True
        t = [a[1], a[3], a[4], a[5], a[6], a[7], a[8]]
        if t == t7:
            return True
        t = [a[0], a[1], a[3], a[4], a[5], a[6], a[7]]
        if t == t6:
            return True
        t = [a[1], a[2], a[3], a[4], a[5], a[7], a[8]]
        if t == t8:
            return True
        return False

    @staticmethod
    def delete2(img, w, h):   # Удаляем пиксели по дополнительному набору шаблонов
        for i in range(1, h - 1):
            for j in range(1, w - 1):
                if img[j][i] == 0 and TemplateDeleter.deletable2(img, j, i):
                    img[j][i] = 1

    @staticmethod
    def deletable2(img, x, y):   # Подготавливаем матрицу
        a = []
        for i in range(y - 1, y + 2):
            for j in range(x - 1, x + 2):
                a.append(img[j][i])
        return TemplateDeleter.check2(a)

    @staticmethod
    def check2(a):   # Проверяем соответствие второму набору шаблонов
        t = [[1, 1, 1, 1, 0, 1, 1, 1, 1],

             [1, 1, 1, 1, 0, 1, 1, 0, 0],
             [1, 1, 1, 0, 0, 1, 0, 1, 1],
             [0, 0, 1, 1, 0, 1, 1, 1, 1],
             [1, 1, 0, 1, 0, 0, 1, 1, 1],

             [1, 1, 1, 1, 0, 1, 0, 0, 1],
             [0, 1, 1, 0, 0, 1, 1, 1, 1],
             [1, 0, 0, 1, 0, 1, 1, 1, 1],
             [1, 1, 1, 1, 0, 0, 1, 1, 0],

             [1, 1, 1, 1, 0, 1, 0, 0, 0],
             [0, 1, 1, 0, 0, 1, 0, 1, 1],
             [0, 0, 0, 1, 0, 1, 1, 1, 1],
             [1, 1, 0, 1, 0, 0, 1, 1, 0]]
        return a in t
