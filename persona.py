from os.path import exists

class Persona:
    def __init__(self):
        self.personas = {}
        self.DB = ( 'valores.txt' )

    def clean_DB(self):
        with open(self.DB, "w") as pen:
            pen.write("")
        
    def add_users(self, dni, name, last):
        if not (dni.isnumeric() and name.istitle() and last.istitle()):
            raise ValueError("Datos")
        if not (dni in self.personas.keys()):
            with open(self.DB, "a") as Pen:
                Pen.write(dni + " " + name + " " + last + "\n")
            self.personas[dni]= name + " " + last
            return 1

    def users_in_DB(self):
        lines = []
        with open(self.DB) as Data:
            for line in Data.readlines():
                self.personas[line.split()[0]] = line.split()[1] + " " + line.split()[2]

    def delete_users(self, dni):
        if not (dni in self.personas.keys()):
            raise ValueError("Dni")
        with open(self.DB, "r") as Data:
            for line in Data.readlines():
                if dni not in line.strip("\n"):
                    with open(self.DB, "w") as pen:
                        pen.write(line)
        del self.personas[dni]
        
