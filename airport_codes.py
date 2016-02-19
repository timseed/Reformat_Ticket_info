import pickle


class airport_codes(object):
    def __init__(self):
        self.airports = pickle.load(open("airport_codes.pickle", "rb"))

    def get(self, acode):
        if acode in self.airports:
            return self.airports[acode]
        else:
            return [None, None]

    def get_Country(self, acode):
        if acode in self.airports:
            return self.airports[acode][1]
        else:
            return None

    def get_Name(self, acode):
        if acode in self.airports:
            return self.airports[acode][0]
        else:
            return None


if __name__ == "__main__":

    runway = airport_codes()
    val = runway.get('MCT')
    if val[1] == 'Oman':
        print("Found MCT Ok")
    print('Get MCT Name: '+runway.get_Name('MCT'))
    print('Get MCT Country: '+runway.get_Country('MCT'))
    val = runway.get('666')
    if val[0] == None:
        print("Correct Missing airport now found")
    val = runway.get_Name('666')
    val = runway.get_Country('666')

