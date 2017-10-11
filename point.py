# class Point

class Point:
    # 아래처럼 쓰지않는다
    # x = 0
    # y = 0
    # 자바의 this 는 파이썬에서는 self
    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    # def show(): <- 파라미터 안넣으면 에러는 안나지만...pycharm자체에서 에러를 냄
    def show(self):
    #두가지 방법으로 그리기
        print("{%d},{%d}점을 그렸습니다." % (self.x, self.y))
        #print("{0},{1}점을 그렸습니다.".format(self.x, self.y))


# pycharm에서 클라스메써드인지, 스테틱매써드인지 지정을 해달라는 에러
#
#        def static_method():
#            pass
#
#        def class_method():
#            pass
#

    @staticmethod
    def static_method():
        print("static_method() called")

    @classmethod
    def class_method(cls):
        print(cls.count_of_instance)
        print("class_method() called")
