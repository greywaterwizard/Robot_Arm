import math
x = 17
y = 21

L1 = 15
L2 = 15

angle2 = math.acos((x**2 + y**2 - L1**2 - L2**2)/(2*L1*L2))
angle1 = math.atan(y/x) - math.atan((L2*math.sin(angle2))/(L1+(L2*math.cos(angle2))))
deg_angle1 = math.degrees(angle1)
deg_angle2 = math.degrees(angle2)
print(f"Angle 1 is {deg_angle1}")
print(f"Angle 2 is {deg_angle2}")

zero_degrees = 500
one_eighty = 2500

pulse_one = int((2000*(deg_angle1/180))+500)
pulse_two = int((2000*(deg_angle2/180))+500)

print(pulse_one)
print(pulse_two)

pwm = PWM(0x40)
pwm.setPWMFreq(50)
pwm.setServoPulse(0, pulse_one)
pwm.setServoPulse(1, pulse_two)
