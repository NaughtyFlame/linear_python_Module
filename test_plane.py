from plane import *

p1 = Plane(normal_vector=Vector(['-0.412', '3.806', '0.728']), constant_term='-3.46')
p2 = Plane(normal_vector=Vector(['1.03', '-9.515', '-1.82']), constant_term='8.65')
print 'first pair of planes are parallel?:{}'.format(p1.is_parallet_to(p2))
print 'first pair of planes are equal?:{}'.format(p1==p2)

p1 = Plane(normal_vector=Vector(['2.611', '5.528', '0.283']), constant_term='4.6')
p2 = Plane(normal_vector=Vector(['7.715', '8.306', '5.342']), constant_term='3.76')
print 'second pair of planes are parallel?:{}'.format(p1.is_parallet_to(p2))
print 'second pair of planes are equal?:{}'.format(p1==p2)

p1 = Plane(normal_vector=Vector(['-7.926', '8.625', '-7.212']), constant_term='-7.95')
p2 = Plane(normal_vector=Vector(['-2.642', '2.875', '-2.404']), constant_term='-2.44')
print 'third pair of planes are parallel?:{}'.format(p1.is_parallet_to(p2))
print 'third pair of planes are equal?:{}'.format(p1==p2)
