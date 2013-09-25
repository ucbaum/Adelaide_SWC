# tag_number: A8024   A-says where rodent was first sighted
# sightings
# size (oz)

#  is_large (>5oz)
#  is_small (<3 oz)
#  capture (month)


class Rodent:
    #first we create empty methods 
    #self is on the reodent object itself
    def __init__(self, tag_id,size):
        # this is the initializer
        self.tag_id=tag_id
        self.size=size
        self.sightings_per_month={}  #empty dictionary

    def is_large(self):
        #True is size is >5 oz. pass means do othing as yet
        return self.size>5

    def is_small(self):
        #True is size is >5 oz. pass means do othing as yet
        return self.size<3

    def is_plot(self):
        #return the letter of the plot at which it was first seen
        return self.tag_id[0]

    def capture (self, month):
        #we captured this rodent once this month
        if not month in self.sightings_per_month:
            self.sightings_per_month[month]=0
        self.sightings_per_month[month]+=1

