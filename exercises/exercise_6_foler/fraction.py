class Fraction:

    def __init__(self, nom=0, den=0):
        if isinstance(nom, (int, float)) and isinstance(den, (int, float)):
            self.nom = nom
            self.den = den
        else:
            raise(TypeError)

        if nom == 0 and den == 0:
            raise(ValueError)

        
    def addition(self, other) -> "Fraction":
        if self.den == other.den:
            return Fraction(self.nom + other.nom, self.den)
        else:
            new_nom = (self.nom * other.den) + (other.nom * self.den) 
            new_den = self.den * other.den
            return Fraction(new_nom, new_den)

    def subtraction(self, other) -> "Fraction":
        if self.den == other.den:
            return Fraction(self.nom - other.nom, self.den)
        else:
            new_nom = (self.nom * other.den) - (other.nom * self.den) 
            new_den = self.den * other.den   
            return Fraction(new_nom, new_den)

    def multiplication(self, other) -> "Fraction":
        if isinstance(other, int | float):
            return Fraction(other*self.nom, self.den).mixed()
        else:
            return Fraction(self.nom*other.nom, self.den*other.den)

    def division(self, other) -> "Fraction":
        return Fraction(self.nom*other.den, self.den*other.nom)

    def simplify(self, value = None):  # simplifies to most simple form unless value is given
        gcf = 0
   
        if not (value): # no value given, find gcf
            r = max(self.den, self.nom)
            for n in range(r, 0, -1):
                if self.den % n == 0 and self.nom % n == 0:
                    gcf = n
                    break
            
            return Fraction(self.nom / gcf, self.den / gcf)
            
        else: # value given try it
            if self.den % value != 0 and self.nom % value == 0:
                print ("illegal value")
            else:
                return Fraction(self.nom / value, self.den / value)
         
    def __str__(self): # represent the fraction in a neat way for printing
    
        return(f"{self.nom} / {self.den}")

    def __repr__(self):
        return(f"{self.nom} / {self.den}")

    def mixed(self) -> str: # represent the fraction in mixed terms
            if abs(self.nom) < abs(self.den): # if nominator is smaller, cant get whole numbers
                return Fraction(self.nom, self.den)
            if (self.nom % self.den == 0):
                return Fraction(self.nom, self.den)
            else:
                return (f"{self.nom // self.den}, {self.nom - ((self.nom // self.den)*self.den)}/{self.den}")


    def __eq__(self, other):  # checks equality by overloading ==
        nom_factor = max(self.nom, other.nom) / min(self.nom, other.nom)
        den_factor = max(self.den, other.den) / min(self.den, other.den)

        return nom_factor == den_factor


