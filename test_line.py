from line import *


ell1 = Line(normal_vector=Vector(['4.046', '2.836']), constant_term='1.21')
ell2 = Line(normal_vector=Vector(['10.115', '7.09']), constant_term='3.025')
print 'intersection 1:', ell1.intersection_with(ell2)

ell1 = Line(normal_vector=Vector(['7.204', '3.182']), constant_term='8.68')
ell2 = Line(normal_vector=Vector(['8.172', '4.114']), constant_term='9.883')
print 'intersection 2:', ell1.intersection_with(ell2)

ell1 = Line(normal_vector=Vector(['1.182', '5.562']), constant_term='6.744')
ell2 = Line(normal_vector=Vector(['1.773', '8.343']), constant_term='9.525')
print 'intersection 3:', ell1.intersection_with(ell2)
