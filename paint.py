#바로 Point를 이 안에서 정의
from point import Point


def test_bound_instance_method():
    p = Point()
    p.set_x(10)
    p.set_y(20)
    #print(p.get_x(), p.get_y())
    p.show()
    print(p.count_of_instance)


def test_unbound_class_method():
    p = Point()
    Point.set_x(p, 10)
    Point.set_y(p, 20)
    print(Point.get_x(p), Point.get_y(p))


def test_othermethod():
    Point.class_method()
    Point.static_method()


def main():
    # test_othermethod()
    # test_unbound_class_method()
    test_bound_instance_method()






if __name__ == '__main__':
    main()




