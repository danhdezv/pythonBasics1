class Subject:
    def __init__(self,name,score):
        self.name = name
        self.score = score

class Student(object):
    __private = 0
    def __init__(self, name,subject):
        self.name = name
        self.subjects = []
        for key, value in subject.items():
            self.subjects.append(Subject(key, value))
            print(key, "added whit" , value)
        print("hello ", self.name)

    def print_details(self):
        print("________________________________")
        print("Name: ", self.name)
        #print("Score: ", self.score)
        for subject in self.subjects:
            print( f"{subject.name} : {subject.score}" )

        print("Avarage: ",self.get_avarage() )
        print("________________________________")

    def get_avarage(self):
        """suma = 0
        for x in range ( len(self.score) ):
            suma += int( self.score[x] )
        return ( suma /  len(self.score) )
        """
        suma = 0
        for subject in self.subjects:
            suma += (subject.score)
        
        return  (suma / len(self.subjects) )
            #print( f" {ubject.score}" )


        ##return sum( self.score ) / len( self.score )
"""

student1 = Student("Juanito",[99,55,100])
student2 = Student("Pancho",[30,65,100])
student1.print_details()
student2.print_details()



#print(student1.__private)
"""


