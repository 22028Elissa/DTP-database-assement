# docstring - Elissa Piao - Artgallery database project

#import
import sqlite3


#Constants and variables
DATABASE = "artgallery.db"



#functions

def print_all_artworks_with_artists():
    '''Print all artworks with artists nicely'''
    db = sqlite3.connect(DATABASE)
    
    cursor = db.cursor()

    sql = "SELECT Artwork.Name, Artwork.style, Artwork.Year_made, Artwork.Price, Artist.Artist_name, Artist.Date_of_birth, Artist.Country FROM Artwork JOIN Artist ON Artist.id=Artwork.Artist;"

    cursor.execute(sql)

    results = cursor.fetchall()

    #loop through results

    print(f"Name                     Style               Year made      Price     Artist         D.O.B     Country       ")

    for Artwork in results:
            
            print(f"{Artwork[0]:>25}{Artwork[1]:>20}{Artwork[2]:>15}{Artwork[3]:>10}M{Artwork[4]:>15}{Artwork[5]:>10}{Artwork[6]:>15}")

        #loop finishes here
            
    db.close()

#main code

while True:
    userinput = input("\nWelcome to the Art Gallery database!\nHere are some options.\n\n1.View all artworks with artist information.\n2.View all artworks sorted alphabetically\n3.View all artworks sorted by year\n4.View all artworks sorted by price\n10.View all artists.\n11.View all artists sorted by country.\n12.View all artists sorted by d.o.b.\n")
    if userinput == "1":
        print_all_artworks_with_artists()
    elif userinput == "2":
        print_all_artworks_sorted_alphabetically()
    elif userinput == "3":
        print_all_artworks_sorted_by_year_asc()
    elif userinput == "4":
        print_all_artworks_sorted_by_price_asc()
    #elif userinput == "10":

    #elif userinput == "11":

    #1elif userinput == "12":

    else:
        exit
    
