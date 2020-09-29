# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 01:24:00 2020

@author: Martinez Garcia Isabel
2) Realice la representacián de la red semantica por medio de un programa
que permita implementar los siguientes verbos: Tiene, Vive y es.
"""


AnimalesEs = [("Tortuga","Oviparos"),
              ("Gallo","Oviparos"),
              ("Cocodrilo","Oviparos"),
              ("Iguana","Oviparos"),
              ("Gato","Viviparos"),
              ("Ballena","Viviparos"),
              ("Oso","Viviparos"),
              ("Delfin","Viviparos"),
              ("Viviparo","Mammalia"),
              ("Oviparo","Sauropsidos"),
              ("Sauropsidos","Tetrapodos"),
              ("Mammalia","Tetrapodos"),
              ("Tetrapodos","Vertebrados")
]
AnimalesVive = [("Tortuga","Tierra"),
                ("Tortuga","Agua"),
                ("Gallo","Tierra"),
                ("Cocodrilo","Tierra"),
                ("Cocodrilo","Agua"),
                ("Iguana","Tierra"),
                ("Gato","Tierra"),
                ("Ballena","Agua"),
                ("Oso","Tierra"),
                ("Delfin","Agua")               
]

AnimalesTiene = [("Gallo","Proteccion queratina(plumas o escamas)"),
                 ("Cocodrilo","Garras"),
                 ("Cocodrilo","Proteccion queratina(plumas o escamas)"),
                 ("Iguana","Proteccion queratina(plumas o escamas"),
                 ("Iguana","Garras"),
                 ("Gato","G.mamarias"),
                 ("Gato","Pelo"),
                 ("Gato","Garras"),
                 ("Oso","G.mamarias"),
                 ("Oso","Pelo"),
                 ("Oso","Garras"),     
                 ("Tortuga","Garras"),
                 ("Delfin","G.Mamarias")
]


def esta(A,CON,B):
	i = 0
	while i < len(CON):
		if CON[i][0] == A:
			if CON[i][1] == B:
				return True
		i = i + 1
	return False

def vervoEs(A,CON,B):
    return  esta(A,B,CON)
def vervoVive(A,CON,B):
    return  esta(A,B,CON)
def vervoTiene(A,CON,B):
    return  esta(A,B,CON)


print(vervoEs("Tortuga","Oviparos" , AnimalesEs)) #True 
print(vervoVive("Iguana","Viviparos", AnimalesEs)) #falso

print(vervoVive("Delfin","Agua" , AnimalesVive)) #True 
print(vervoVive("Delfin","Tierra" , AnimalesVive)) #falso

print(vervoTiene("Oso","Garras", AnimalesTiene)) #True 
print(vervoTiene("Oso","Proteccion queratina(plumas o escamas)", AnimalesTiene)) #False



 

    