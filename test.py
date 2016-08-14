print "hello world"

def function go_crazy():
	print  'go crazy!'
        r1 = rational(1,2)
        r2 = rational(2,3)
        print r1.add(r2)
	return 0

class rational:
    def __init__(self, a, b):
        self._a = a
        self._b = b

    def add(self, r):
        return rational(self._a - r.a, self._b - b)


go_crazy()

def function do_nothing():
	return
