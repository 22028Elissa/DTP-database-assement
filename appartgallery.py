# docstring - Elissa Piao - Artgallery database project
#import
import sqlite3

#Constants and variables
DATABASE = "artgallery.db"

#functions

def print_all_artworks_with_artists():
    '''1Print all artworks with artists nicely'''
    db = sqlite3.connect(DATABASE)
    
    cursor = db.cursor()

    sql = "SELECT Artwork.Name, Artwork.style, Artwork.Year_made, Artwork.Price, Artist.Artist_name, Artist.Year_of_birth, Artist.Country FROM Artwork JOIN Artist ON Artist.id=Artwork.Artist;"

    cursor.execute(sql)

    results = cursor.fetchall()

    #loop through results

    print(f"                       Name               Style    Year made    Price($)             Artist Year born        Country\n")

    for Artwork in results:
            
            print(f"{Artwork[0]:>27}{Artwork[1]:>20}{Artwork[2]:>13}{Artwork[3]:>10}M{Artwork[4]:>20}{Artwork[5]:>10}{Artwork[6]:>15}")

        #loop finishes here
            
    db.close()

def print_all_artworks_sorted_(sortedway):
    '''Print all artworks  sorted by variable with artists'''
    db = sqlite3.connect(DATABASE)
    
    cursor = db.cursor()

    sql = f"SELECT Artwork.Name, Artist.Artist_name, Artwork.style, Artwork.Year_made, Artwork.Price FROM Artwork JOIN Artist ON Artist.id=Artwork.Artist ORDER BY {sortedway} ASC;"

    cursor.execute(sql)

    results = cursor.fetchall()

    #loop through results

    print(f"                       Name             Artist               Style     Year made    Price($)\n")

    for Artwork in results:
            
            print(f"{Artwork[0]:>27}{Artwork[1]:>20}{Artwork[2]:>20}{Artwork[3]:>13}{Artwork[4]:>10}M")

    #loop finishes here
        
    db.close()

def print_all_artists_sorted_(sortedway):
    '''Print all artworks with artists sorted by variable'''
    db = sqlite3.connect(DATABASE)
    
    cursor = db.cursor()

    sql = f"Select Artist_name, Year_of_birth, Country FROM Artist ORDER BY {sortedway} ASC;"

    cursor.execute(sql)

    results = cursor.fetchall()

    #loop through results

    print(f"                  Name   Year born        Country\n")

    for Artist in results:
            
            print(f"{Artist[0]:>22}{Artist[1]:>12}{Artist[2]:>15}")

    #loop finishes here
        
    db.close()

def print_all_artworks_sorted_with_where(specific):
    '''Print all artworks with Where sorted by variable with artists'''
    db = sqlite3.connect(DATABASE)
    
    cursor = db.cursor()

    sql = f"SELECT Artwork.Name, Artist.Artist_name, Artwork.style, Artwork.Year_made, Artwork.Price FROM Artwork JOIN Artist ON Artist.id=Artwork.Artist WHERE {column} = '{specific}' ORDER BY Artwork.Name ASC;"

    cursor.execute(sql)

    results = cursor.fetchall()

    #loop through results

    print(f"                       Name             Artist               Style     Year made    Price($)\n")

    for Artwork in results:
            
            print(f"{Artwork[0]:>27}{Artwork[1]:>20}{Artwork[2]:>20}{Artwork[3]:>13}{Artwork[4]:>10}M")

    #loop finishes here
        
    db.close()
 
def print_all_artists_sorted_with_where(specific):
    db = sqlite3.connect(DATABASE)
    
    cursor = db.cursor()

    sql = f"Select Artist_name, Year_of_birth, Country FROM Artist WHERE {column} = '{specific}' ORDER BY Artist_name ASC;"

    cursor.execute(sql)

    results = cursor.fetchall()

    #loop through results

    print(f"                  Name   Year born        Country\n")

    for Artist in results:
            
            print(f"{Artist[0]:>22}{Artist[1]:>12}{Artist[2]:>15}")

    #loop finishes here
        
    db.close()

def print_all_artworks_sorted_with_where_with_between(specific):
    '''Print all artworks with Where sorted by variable with artists'''
    db = sqlite3.connect(DATABASE)
    
    cursor = db.cursor()

    sql = f"SELECT Artwork.Name, Artist.Artist_name, Artwork.style, Artwork.Year_made, Artwork.Price FROM Artwork JOIN Artist ON Artist.id=Artwork.Artist WHERE {column} BETWEEN '{x}' AND '{y}' ORDER BY Artwork.Name ASC;"

    cursor.execute(sql)

    results = cursor.fetchall()

    #loop through results

    print(f"                       Name             Artist               Style     Year made    Price($)\n")

    for Artwork in results:
            
            print(f"{Artwork[0]:>27}{Artwork[1]:>20}{Artwork[2]:>20}{Artwork[3]:>13}{Artwork[4]:>10}M")

    #loop finishes here
        
    db.close()

def print_all_artists_sorted_with_where_with_between(x,y):
    db = sqlite3.connect(DATABASE)
    
    cursor = db.cursor()

    sql = f"Select Artist_name, Year_of_birth, Country FROM Artist WHERE {column} BETWEEN '{x}' AND '{y}' ORDER BY Artist_name ASC;"

    cursor.execute(sql)

    results = cursor.fetchall()

    #loop through results

    print(f"                  Name   Year born        Country\n")

    for Artist in results:
            
            print(f"{Artist[0]:>22}{Artist[1]:>12}{Artist[2]:>15}")

    #loop finishes here
        
    db.close()
#main code
#Welcome user
print("Welcome to the Art Gallery database!\n")
#username = input("What is your name?")
while True:
    userinput = input("\nHere are some options.\n\n1.View all artworks with artist information.\n2.View all artworks sorted alphabetically\n3.View all artworks sorted by year\n4.View all artworks sorted by price\n5.View all artists.\n6.View all artists sorted by country.\n7.View all artists sorted by year born\n8.Choose a specific column or name to sort by.\n9.Exit\n")
    if userinput == "1":
        print_all_artworks_with_artists()
    elif userinput == "2":
        sortedway = 'Artwork.Name'
        #sort by name alphabeticaalu
        print_all_artworks_sorted_(sortedway)
    elif userinput == "3":
        #sort by year it was made
        sortedway = 'Artwork.Year_made'
        print_all_artworks_sorted_(sortedway)
    elif userinput == "4":
        #price
        sortedway = 'Artwork.Price'
        print_all_artworks_sorted_(sortedway)
    elif userinput == "5":
        #artist price
        sortedway = 'Artist.Artist_name'
        print_all_artists_sorted_(sortedway)
    elif userinput == "6":
        sortedway = 'Artist.Country'
        print_all_artists_sorted_(sortedway)
    elif userinput == "7":
        sortedway = 'Artist.Year_of_birth'
        print_all_artists_sorted_(sortedway)
    elif userinput == "8":   
        eightinput = input("1.Specifics on Artworks.\n2.Specifics on Artworks.\n")
        if eightinput == "1":
            eightinput = input("\n1.To find one 'artwork'.\n2.Find all Artworks from one specific artist.\n3.All artworks with one style\n4.All artworks where the year made fall under(x-y)\n5.Exit\n")
            if eightinput == "1":
                column = "Artwork.Name"
                specific = input("Please type the name of the artwork you would like(correctly with capitals): ")
                print_all_artworks_sorted_with_where(specific)
                #make exceptions like invalid input
            elif eightinput == "2":
                column = "Artist.Artist_name"
                specific = input("Please type the name of the artist you would like(correctly with capitals): ")
                print_all_artists_sorted_with_where(specific)
            elif eightinput == "3":
                column = "Artwork.Style"
                specific = input("Please type the style of the artworks you would like(correctly with capitals): ")
                print_all_artworks_sorted_with_where(specific)
            elif eightinput == "4":
                column = "Artwork.Year_made"
                x,y = input("Please type the years of the artworks you would like(example- 1400,1500): ").split(",")
                while True:
                    try:
                        x = int(x)
                        y = int(y)
                        print_all_artworks_sorted_with_where_with_between(x,y)
                    except ValueError:
                        print("Please enter numbers seperated by a comma.")    
            else:
                print("That was not a valid option.") 
        if eightinput = "2":
            eightinput = input("\n1.To find one artist.\n2.Find all Artists from one Country.\n3.Find all Artworks by one artist.\n4.All artists born between the years you choose(x-y)\n5.Exit\n")
        else:
            print("That was not a valid option.")
            
    elif userinput == "9":   
        break 
    else:
        print("That was not a valid option. Please try again :O")
    
