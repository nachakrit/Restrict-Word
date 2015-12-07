##Excample for plot
from pylab import *
def draw_pie(type):

    lis, dic, lis_type = find_inform()
    # make a square figure and axes
    figure(1, figsize=(10,10))
    ax = axes([0.1, 0.1, 0.8, 0.8])

    # The slices will be ordered and plotted counter-clockwise.
    labels = lis
    fracs = dic[lis_type[type]]
    explode=0

    pie(fracs, labels=labels,
    autopct='%1.1f%%', shadow=True, startangle=30)
                # The default startangle is 0, which would start
                # the Frogs slice on the x-axis.  With startangle=90,
                # everything is rotated counter-clockwise by 90 degrees,
                # so the plotting starts on the positive y-axis.

    title(lis_type[type] , bbox={'facecolor':'0.8', 'pad':5})
    show()
draw_pie(int(input()) - 1)
