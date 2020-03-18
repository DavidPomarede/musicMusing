#p1 >> pads([12,-5,10,8])
#d1 >> pulse([10,-6,12,1])
p2 >> pads([-6,5,-10,8])
#d2 >> pulse([-32,6,-12,-1])
#p3 >> pluck([5,4,0], dur=[1,1/2,1/2], amp=[1,3/4,3/4])
#p4 >> pads([2,4,8,0,4,3], dur=[1,1/2,1/2,1,1,1/2], amp=[1,3/4,3/4,1,3/4,3/4])

p5 >> bug([5,4,0], dur=[1/2,1/2,1/2], amp=[1,3/4,3/4])

#p6 >> pads([5,4,0], dur=[1,1,1], amp=[1,3/4,3/4])
#p7 >> feel([0,2,4], dur=[1,1/2,1/2], amp=[1,3/4,3/4])
#p8 >> pluck([0,2,4], dur=[1,1/2,1/2], amp=[1,3/4,3/4])
p9 >> jbass([5,4,0,2], dur=[1/2,1,1/2,1], amp=[1,3/4,3/4,3/4])

p2.stop()

#print(FxList)
p8 >> jbass([2,0,4,5], dur=[1,1,1,1], amp=[1,3/4,3/4,3/4])

b1 >> bass([0,1,0,3], dur=4)
#p1 >> pluck(dur=1/2).follow(b1) + (0,2,4) 

# This adds a triad to the bass notes

d1 >> play("x-o-xyzC")

d2 >> play("4-o@xyzg")

d3 >> play("::-::-:~")
d3.sus = 2

Scale.default = Scale.minor

print(Samples)

k1 >> karp(dur=1/4, oct=6)

k1.benddelay(10)
#k1 >> karp(dur=1/4, oct=6)

p9.stop()

k2 >> karp(dur=1/8, oct=2)
k2.bend(2)

p4.benddelay(2) >> pluck([0, 0, 0,0], dur=[1, 1/2, 1, 1/2], amp=0.75) 
p4.benddelay()

# x--(-[--])o--o(-=)-
# x-~(-[1o])x--b(-z)-
d2.stop()

d1.stop()
d2.stop()
d3.stop()
d4.stop()

p1.stop()
p2.stop()
p3.stop()
p4.stop()

d1 >> play(P["x--(-[--])o--o(-=)-"].layer("mirror"),
	pan=(-1,1),
	dur=PDur(5,8),
	sample=-1,
	rate=var([1,4],[28,4]))

d1 >> play("x---", pan=(-1, 1), pshift=(0, 0.125)).spread()

d1.spread() >> play("x-o-", pan=[-1, 0, 1])

d1 = mute

Clock.bpm = 140

d2 >> play(PZip("Vs", "  n "), sample=10, hpf=var([0,4000],[28,4])).every(3, 'stutter', dur=1)

d3 >> play("[--]")

s1 >> swell((0,2,4,const(6)), dur=4) + var([])

Scale.default = "lydian"


