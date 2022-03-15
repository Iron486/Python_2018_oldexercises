# numpy.linspace() function
'''>>> np.linspace(2.0, 3.0, num=5 ) #num=5 it's an int value
array([ 2.  ,  2.25,  2.5 ,  2.75,  3.  ])
>>> np.linspace(2.0, 3.0, num=5, endpoint=False) #boolean value. Default is True
array([ 2. ,  2.2,  2.4,  2.6,  2.8])
>>> np.linspace(2.0, 3.0, num=5, retstep=True) #boolean value. Default is False
(array([ 2.  ,  2.25,  2.5 ,  2.75,  3.  ]), 0.25)'''
#numpy.arange() function
'''>>> np.arange(3) # The interval including start, but excluding stop
array([0, 1, 2])
>>> np.arange(3.0)
array([ 0.,  1.,  2.])
>>> np.arange(3,7)
array([3, 4, 5, 6])
>>> np.arange(3,7,2)
array([3, 5])''' #For float value results not often be consistent
