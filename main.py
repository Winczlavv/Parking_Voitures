import random as rdm;

class Parking:

    def __init__(self,nb_places):
        self.P = []
        self.nb_places = nb_places
        for i in range(nb_places):
            self.P.append(rdm.randint(0,1))
        print(self.P)
    
    def se_garer(self,voiture):
        places_dispo = "Les places disponibles sont : "
        places_dispo_init = places_dispo
        for j in range(len(self.P)):
            if self.P[j] == 1:
                if (j+1) % 2 == 0 and voiture.color == "rouge":
                    places_dispo += str(j+1) + ","
                if (j+1) % 2 == 1 and voiture.color == "bleu":
                    places_dispo += str(j+1) + ","

        if voiture.color != "rouge" and voiture.color !="bleue" or places_dispo == places_dispo_init:
           places_dispo = "Vous ne pouvez pas vous garer. Passez votre chemin !."
        print(places_dispo.rstrip(places_dispo[-1]))
    
        
class Voiture:
    def __init__(self, color):
        self.color = color


parking = Parking(10)
voiture = Voiture("verte")
parking.se_garer(voiture)
        
            