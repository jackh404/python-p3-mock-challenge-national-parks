# # # # # # # # # # # # #
#      NationalPark     #
# # # # # # # # # # # # #
class NationalPark:
    all = []
    
    def __init__(self, name):
        self.name = name
        NationalPark.add_to_all(self)
        
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        if(hasattr(self,'name')):
            raise Exception("Cannot change park name")
        if(isinstance(name,str) and 3 <= len(name)):
            self._name = name
        else:
            raise ValueError("Park name must be valid string 3 characters or more")
        
    def trips(self):
        return [trip for trip in Trip.all if trip.national_park == self]
    
    def visitors(self):
        visitor_list =[]
        for trip in self.trips():
            if trip.visitor not in visitor_list:
                visitor_list.append(trip.visitor)
        return visitor_list
    
    def total_visits(self):
        return len(self.trips())
    
    def best_visitor(self):
        if not self.trips():
            return None
        return max(self.visitors(),key=lambda visitor : visitor.total_visits_at_park(self))
    
    @classmethod
    def add_to_all(cls,park):
        cls.all.append(park)
    
# # # # # # # # # # # # #
#         Trip          #
# # # # # # # # # # # # #
class Trip:
    all = []
    
    def __init__(self, visitor, national_park, start_date, end_date):
        self.visitor = visitor
        self.national_park = national_park
        self.start_date = start_date
        self.end_date = end_date
        Trip.add_to_all(self)
        
    @property
    def start_date(self):
        return self._start_date
    @start_date.setter
    def start_date(self,date):
        if(isinstance(date,str) and len(date) >= 7):
            self._start_date = date
        else:
            raise ValueError("Date must be a valid string of the format 'May 5th'")
    
    @property
    def end_date(self):
        return self._end_date
    @end_date.setter
    def end_date(self,date):
        if(isinstance(date,str) and len(date) >= 7):
            self._end_date = date
        else:
            raise ValueError("Date must be a valid string of the format 'May 5th'")
            
    @property
    def visitor(self):
        return self._visitor
    @visitor.setter
    def visitor(self,visitor):
        if isinstance(visitor,Visitor):
            self._visitor = visitor
        else:
            raise ValueError("Visitors must be objects of the Visitor class")
        
    @property
    def national_park(self):
        return self._national_park
    @national_park.setter
    def national_park(self,park):
        if isinstance(park,NationalPark):
            self._national_park = park
        else:
            raise ValueError("Parks must be objects of the NationalPark class")
        
        
    @classmethod
    def add_to_all(cls,trip):
        cls.all.append(trip)

# # # # # # # # # # # # #
#        Visitor        #
# # # # # # # # # # # # #
class Visitor:
    all = []
    
    def __init__(self, name):
        self.name = name
        Visitor.add_to_all(self)
    
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,name):
        if(isinstance(name,str) and 1 <= len(name) <= 15):
            self._name = name
        else:
            raise ValueError("Visitor name must be valid string between 1 and 15 characters")
        
    def trips(self):
        return [trip for trip in Trip.all if trip.visitor == self]
    
    def national_parks(self):
        park_list = []
        for trip in self.trips():
            if trip.national_park not in park_list:
                park_list.append(trip.national_park)
        return park_list
    
    def total_visits_at_park(self, park):
        return [trip.national_park for trip in self.trips()].count(park)
    
    @classmethod
    def add_to_all(cls,visitor):
        cls.all.append(visitor)