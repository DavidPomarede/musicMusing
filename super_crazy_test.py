#p1 >> pads([12,-5,10,8])
#d1 >> pulse([10,-6,12,1])
#p2 >> pads([-6,5,-10,8])
#d2 >> pulse([-32,6,-12,-1])
#p3 >> pluck([5,4,0], dur=[1,1/2,1/2], amp=[1,3/4,3/4])
#p4 >> pads([2,4,8,0,4,3], dur=[1,1/2,1/2,1,1,1/2], amp=[1,3/4,3/4,1,3/4,3/4])

p5 >> bug([5,4,0], dur=[1/2,1/2,1/2], amp=[1,3/4,3/4])

#p6 >> pads([5,4,0], dur=[1,1,1], amp=[1,3/4,3/4])
#p7 >> feel([0,2,4], dur=[1,1/2,1/2], amp=[1,3/4,3/4])
#p8 >> pluck([0,2,4], dur=[1,1/2,1/2], amp=[1,3/4,3/4])
p9 >> jbass([5,4,0,2], dur=[1/2,1,1/2,1], amp=[1,3/4,3/4,3/4])

#print(FxList)
p8 >> jbass([2,0,4,5], dur=[1,1,1,1], amp=[1,3/4,3/4,3/4])

b1 >> bass([0,2,3,4], dur=4)
p1 >> pluck(dur=1/2).follow(b1) + (0,2,4) # This adds a triad to the bass notes
