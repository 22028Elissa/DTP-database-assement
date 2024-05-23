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

    sql = "SELECT Artwork.Name, Artwork.style, Artwork.Year_made, Artwork.Price, Artist.Artist_name, Artist.Year_of_birth, Artist.Country FROM Artwork JOIN Artist ON Artist.id=Artwork.Artist;"

    cursor.execute(sql)

    results = cursor.fetchall()

    #loop through results

    print(f"                       Name               Style    Year made    Price($)             Artist Year born        Country\n")

    for Artwork in results:
            
            print(f"{Artwork[0]:>27}{Artwork[1]:>20}{Artwork[2]:>13}{Artwork[3]:>10}M{Artwork[4]:>20}{Artwork[5]:>10}{Artwork[6]:>15}")

        #loop finishes here
            
    db.close()
def print_all_artworks_sorted_alphabetically():
    '''Print all artworks with artists sorted alphabetically(A-Z)'''
    db = sqlite3.connect(DATABASE)
    
    cursor = db.cursor()

    sql = "SELECT Artwork.Name, Artist.Artist_name, Artwork.style, Artwork.Year_made, Artwork.Price FROM Artwork JOIN Artist ON Artist.id=Artwork.Artist ORDER BY Artwork.Name ASC;"

    cursor.execute(sql)

    results = cursor.fetchall()

    #loop through results

    print(f"                       Name             Artist               Style     Year made    Price($)\n")

    for Artwork in results:
            
            print(f"{Artwork[0]:>27}{Artwork[1]:>20}{Artwork[2]:>20}{Artwork[3]:>13}{Artwork[4]:>10}M")

    #loop finishes here
        
    db.close()
def print_all_artworks_sorted_by_year_asc():
    '''Print all artworks with artists sorted year ascending'''
    db = sqlite3.connect(DATABASE)
    
    cursor = db.cursor()

    sql = "SELECT Artwork.Name, Artist.Artist_name, Artwork.style, Artwork.Year_made, Artwork.Price FROM Artwork JOIN Artist ON Artist.id=Artwork.Artist ORDER BY Artwork.Year_made ASC;"

    cursor.execute(sql)

    results = cursor.fetchall()

    #loop through results

    print(f"                       Name             Artist               Style    Year made    Price($)\n")

    for Artwork in results:
            
            print(f"{Artwork[0]:>27}{Artwork[1]:>20}{Artwork[2]:>20}{Artwork[3]:>13}{Artwork[4]:>10}M")
    
    #loop finishes here
        
    db.close()
def print_all_artworks_sorted_by_price_asc():
    '''Print all artworks with artists sorted by price ascending'''
    db = sqlite3.connect(DATABASE)
    
    cursor = db.cursor()

    sql = "SELECT Artwork.Name, Artist.Artist_name, Artwork.style, Artwork.Year_made, Artwork.Price FROM Artwork JOIN Artist ON Artist.id=Artwork.Artist ORDER BY Artwork.Price ASC;"

    cursor.execute(sql)

    results = cursor.fetchall()

    #loop through results

    print(f"                       Name             Artist               Style    Year made    Price($)\n")

    for Artwork in results:
            
            print(f"{Artwork[0]:>27}{Artwork[1]:>20}{Artwork[2]:>20}{Artwork[3]:>13}{Artwork[4]:>10}M")

    #loop finishes here
        
    db.close()
def print_all_artists_sorted_by_name_asc():
    '''Print all artworks with artists sorted name ascending'''
    db = sqlite3.connect(DATABASE)
    
    cursor = db.cursor()

    sql = "Select Artist_name, Year_of_birth, Country FROM Artist ORDER BY Artist_name ASC;"

    cursor.execute(sql)

    results = cursor.fetchall()

    #loop through results

    print(f"                  Name   Year born        Country\n")

    for Artist in results:
            
            print(f"{Artist[0]:>22}{Artist[1]:>12}{Artist[2]:>15}")

    #loop finishes here
        
    db.close()
def print_all_artists_sorted_by_yearborn_asc():
    '''Print all artworks with artists sorted yearborn ascending'''
    db = sqlite3.connect(DATABASE)
    
    cursor = db.cursor()

    sql = "Select Artist_name, Year_of_birth, Country FROM Artist ORDER BY Year_of_birth ASC;"

    cursor.execute(sql)

    results = cursor.fetchall()

    #loop through results

    print(f"                  Name   Year born        Country\n")

    for Artist in results:
            
            print(f"{Artist[0]:>22}{Artist[1]:>12}{Artist[2]:>15}")

    #loop finishes here
        
    db.close()
def print_all_artists_sorted_by_country_asc():
    '''Print all artworks with artists sorted by country ascending'''
    db = sqlite3.connect(DATABASE)
    
    cursor = db.cursor()

    sql = "Select Artist_name, Year_of_birth, Country FROM Artist ORDER BY Country ASC;"

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
    userinput = input("\nHere are some options.\n\n1.View all artworks with artist information.\n2.View all artworks sorted alphabetically\n3.View all artworks sorted by year\n4.View all artworks sorted by price\n5.View all artists.\n6.View all artists sorted by country.\n7.View all artists sorted by year born\n8.Exit\n")
    if userinput == "1":
        print_all_artworks_with_artists()
    elif userinput == "2":
        print_all_artworks_sorted_alphabetically()
    elif userinput == "3":
        print_all_artworks_sorted_by_year_asc()
    elif userinput == "4":
        print_all_artworks_sorted_by_price_asc()
    elif userinput == "5":
        print_all_artists_sorted_by_name_asc()
    elif userinput == "6":
        print_all_artists_sorted_by_yearborn_asc()
    elif userinput == "7":
        print_all_artists_sorted_by_country_asc()
    #elif userinput == "8":   
     
    elif userinput == "9":   
        break 
    else:
        print("That was not a valid option. Please try again :O")
    
#elif paintinguserinput = "b"
            #print_all_artworks_only_name()
        #Choose from a list\nC.
          # styleuserinput = input("What is the name of the style you would like?\na.Enter the name.\nb.Exit\n")
        #if paintinguserinput == "a":
         #   namepaintinguserinput = input("Enter the name: ")

        #    print_one_painting_user_input()
        #elif paintinguserinput == "b":
def print_one_painting_user_input():
    '''Print one painting that the user chooses'''
    db = sqlite3.connect(DATABASE)
    
    cursor = db.cursor()

    sql = "SELECT Name, Style, Artist_name, year_made, price,  FROM Artwork JOIN Artist ON Artist.id=Artwork.id WHERE name = '';"

    cursor.execute(sql)

    results = cursor.fetchall()

    #loop through results

    print(f"                       Name             Artist               Style     Year made    Price($)\n")

    
    print(f"{Artwork[0]:>27}{Artwork[1]:>20}{Artwork[2]:>20}{Artwork[3]:>13}{Artwork[4]:>10}M")
    
    #loop finishes here
        
    db.close()
