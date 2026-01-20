class correcting:
    def __init__(self, d1=0, d2=0, d3=0, d4=0, d5=0, d6=0, d7=0, d8=0, d9=0, d10=0, d11=0, d12=0, d13=0):
        self.a = d1
        self.b = d2
        self.c = d3
        self.d = d4
        self.e = d5
        self.f = d6
        self.g = d7
        self.h = d8
        self.i = d9
        self.j = d10
        self.k = d11
        self.l = d12
        self.m = d13
    
    def __str__(self):
        return "(" + str(self.a) + "," + str(self.b) + ","+ str(self.c) + ","+ str(self.d) + "," + str(self.e) + "," + str(self.f) + ","+ str(self.g) + ","+ str(self.h) + "," + str(self.i) + "," + str(self.j) + ","+ str(self.k) + ","+ str(self.l) + "," + str(self.m) +")^T"
    
class Hamming_24_37_e:
    def __init__(self, d1=0, d2=0, d3=0, d4=0, d5=0, d6=0, d7=0, d8=0, d9=0, d10=0, d11=0, d12=0, d13=0, d14=0, d15=0, d16=0, d17=0, d18=0, d19=0, d20=0, d21=0, d22=0, d23=0, d24=0, p1=0, p2=0, p3=0, p4=0, p5=0, p6=0, p7=0, p8=0, p9=0, p10=0, p11=0, p12=0, p13=0):
        self.a = d1
        self.b = d2
        self.c = d3
        self.d = d4
        self.e = d5
        self.f = d6
        self.g = d7
        self.h = d8
        self.i = d9
        self.j = d10
        self.k = d11
        self.l = d12
        self.m = d13
        self.n = d14
        self.o = d15
        self.p = d16
        self.q = d17
        self.r = d18
        self.s = d19
        self.t = d20
        self.u = d21
        self.v = d22
        self.w = d23
        self.x = d24
        self.y = p1
        self.z = p2
        self.aa = p3
        self.ab = p4
        self.ac = p5
        self.ad = p6
        self.ae = p7
        self.af = p8
        self.ag = p9
        self.ah = p10
        self.ai = p11
        self.aj = p12
        self.ak = p13
    
    def __add__(self,other):
        if type(other) == int:
            other = Hamming_24_37_e(other%2,other%2,other%2,other%2,other%2,other%2,other%2,other%2,other%2,other%2,other%2,other%2,other%2,other%2,other%2,other%2,other%2,other%2,other%2,other%2,other%2,other%2,other%2,other%2,other%2,other%2,other%2,other%2,other%2,other%2,other%2,other%2,other%2,other%2,other%2,other%2,other%2)
        return Hamming_24_37_e((self.a + other.a)%2, (self.b + other.b)%2, (self.c + other.c)%2, (self.d + other.d)%2,(self.e + other.e)%2, (self.f + other.f)%2, (self.g + other.g)%2, (self.h + other.h)%2,(self.i + other.i)%2, (self.j + other.j)%2, (self.k + other.k)%2, (self.l + other.l)%2,(self.m + other.m)%2, (self.n + other.n)%2, (self.o + other.o)%2, (self.p + other.p)%2,(self.q + other.q)%2, (self.r + other.r)%2, (self.s + other.s)%2, (self.t + other.t)%2,(self.u + other.u)%2, (self.v + other.v)%2, (self.w + other.w)%2, (self.x + other.x)%2, (self.y + other.y)%2,(self.z + other.z)%2, (self.aa + other.aa)%2, (self.ab + other.ab)%2, (self.ac + other.ac)%2,(self.ad + other.ad)%2, (self.ae + other.ae)%2, (self.af + other.af)%2, (self.ag + other.ag)%2,(self.ah + other.ah)%2, (self.ai + other.ai)%2, (self.aj + other.aj)%2, (self.ak + other.ak)%2)
    
    def __radd__(self,other):
        return self.__add__(other)
    
    def __mul__(self, other):
        return print("Wrong multiplication")

    def __rmul__(self,other):
        if other == "Hr":
            sum = (self.a + self.b + self.c + self.d + self.e + self.f + self.g + self.h + self.i + self.j + self.k + self.l + self.m + self.n + self.o + self.p + self.q + self.r + self.s + self.t + self.u + self.v + self.w + self.x)%2
            return correcting((self.y -(sum - self.n - self.u))%2, (self.z -(sum - self.m - self.t))%2, (self.aa -(sum - self.l - self.t))%2, (self.ab -(sum - self.k - self.s))%2, (self.ac -(sum - self.j - self.s))%2, (self.ad -(sum - self.i - self.r))%2, (self.ae -(sum - self.h - self.r - self.x))%2, (self.af -(sum - self.g - self.q - self.x))%2, (self.ag -(sum - self.f - self.q - self.w))%2, (self.ah -(sum - self.e - self.p - self.w))%2, (self.ai -(sum - self.d - self.p - self.v))%2, (self.aj -(sum - self.c - self.o - self.v))%2, (self.ak -(sum - self.b - self.o - self.u))%2)
        else:
            return print("Wrong multiplication")
        
        
    def __str__(self):
        return "(" + str(self.a) + "," + str(self.b) + ","+ str(self.c) + ","+ str(self.d) + "," + str(self.e) + "," + str(self.f) + ","+ str(self.g) + ","+ str(self.h) + "," + str(self.i) + "," + str(self.j) + ","+ str(self.k) + ","+ str(self.l) + "," + str(self.m) + "," + str(self.n) + ","+ str(self.o) + ","+ str(self.p) + "," + str(self.q) + "," + str(self.r) + ","+ str(self.s) + ","+ str(self.t) + "," + str(self.u) + "," + str(self.v) + ","+ str(self.w) + ","+ str(self.x) + ","+ str(self.y) + "," + str(self.z) + "," + str(self.aa) + ","+ str(self.ab) + ","+ str(self.ac) + "," + str(self.ad) + "," + str(self.ae) + ","+ str(self.af) + ","+ str(self.ag) + "," + str(self.ah) + "," + str(self.ai) + ","+ str(self.aj) + ","+ str(self.ak) + ")^T"



class Hamming_24_37_r:
    def __init__(self, d1=0, d2=0, d3=0, d4=0, d5=0, d6=0, d7=0, d8=0, d9=0, d10=0, d11=0, d12=0, d13=0, d14=0, d15=0, d16=0, d17=0, d18=0, d19=0, d20=0, d21=0, d22=0, d23=0, d24=0):
        self.a = d1
        self.b = d2
        self.c = d3
        self.d = d4
        self.e = d5
        self.f = d6
        self.g = d7
        self.h = d8
        self.i = d9
        self.j = d10
        self.k = d11
        self.l = d12
        self.m = d13
        self.n = d14
        self.o = d15
        self.p = d16
        self.q = d17
        self.r = d18
        self.s = d19
        self.t = d20
        self.u = d21
        self.v = d22
        self.w = d23
        self.x = d24

    
    def __add__(self,other):
            if type(other) == int:
                other = Hamming_24_37_r(other%2,other%2,other%2,other%2,other%2,other%2,other%2,other%2,other%2,other%2,other%2,other%2,other%2,other%2,other%2,other%2,other%2,other%2,other%2,other%2,other%2,other%2,other%2,other%2)
            return Hamming_24_37_r((self.a + other.a)%2, (self.b + other.b)%2, (self.c + other.c)%2, (self.d + other.d)%2,(self.e + other.e)%2, (self.f + other.f)%2, (self.g + other.g)%2, (self.h + other.h)%2,(self.i + other.i)%2, (self.j + other.j)%2, (self.k + other.k)%2, (self.l + other.l)%2,(self.m + other.m)%2, (self.n + other.n)%2, (self.o + other.o)%2, (self.p + other.p)%2,(self.q + other.q)%2, (self.r + other.r)%2, (self.s + other.s)%2, (self.t + other.t)%2,(self.u + other.u)%2, (self.v + other.v)%2, (self.w + other.w)%2, (self.x + other.x)%2)
    
    def __radd__(self,other):
        return self.__add__(other)

    def __mul__(self, other):
        return print("Wrong multiplication")

    def __rmul__(self,other):
        if other == "Gt":
            sum = (self.a + self.b + self.c + self.d + self.e + self.f + self.g + self.h + self.i + self.j + self.k + self.l + self.m + self.n + self.o + self.p + self.q + self.r + self.s + self.t + self.u + self.v + self.w + self.x)%2
            return Hamming_24_37_e(self.a, self.b, self.c, self.d, self.e, self.f, self.g, self.h, self.i, self.j, self.k, self.l, self.m, self.n, self.o, self.p, self.q, self.r, self.s, self.t, self.u, self.v, self.w, self.x, (sum - self.n - self.u)%2, (sum - self.m - self.t)%2, (sum - self.l - self.t)%2, (sum - self.k - self.s)%2, (sum - self.j - self.s)%2, (sum - self.i - self.r)%2, (sum - self.h - self.r - self.x)%2, (sum - self.g - self.q - self.x)%2, (sum - self.f - self.q - self.w)%2, (sum - self.e - self.p - self.w)%2, (sum - self.d - self.p - self.v)%2, (sum - self.c - self.o - self.v)%2, (sum - self.b - self.o - self.u)%2)
        else:
            return print("Wrong multiplication")
        
    def __str__(self):
        return "(" + str(self.a) + "," + str(self.b) + ","+ str(self.c) + ","+ str(self.d) + "," + str(self.e) + "," + str(self.f) + ","+ str(self.g) + ","+ str(self.h) + "," + str(self.i) + "," + str(self.j) + ","+ str(self.k) + ","+ str(self.l) + "," + str(self.m) + "," + str(self.n) + ","+ str(self.o) + ","+ str(self.p) + "," + str(self.q) + "," + str(self.r) + ","+ str(self.s) + ","+ str(self.t) + "," + str(self.u) + "," + str(self.v) + ","+ str(self.w) + ","+ str(self.x) +")^T"

p = Hamming_24_37_r(1,0,1,0)
q = Hamming_24_37_r(0,0,1,1)
print(p)
print("Hr"*("Gt"*p))