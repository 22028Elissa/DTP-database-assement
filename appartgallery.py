# docstring - Elissa Piao - Artgallery database project
#import
import sqlite3

#Constants and variables
DATABASE = "artgallery.db"

#functions
#import smtp library
import os
from email.message import EmailMessage
import ssl
import smtplib

#vufo musw shlt xyci
#Email information
email_sender = 'ilovemolang777@gmail.com'
email_password = 'vufomuswshltxyci'
email_receiver = '22028@burnside.school.nz'

#message of the email
subject = 'Thanks from sw4t art gallery.'
body = """
#LINK
Is this the artwork you wanted? If not email us back.
From Sweeeet Art Gallery <3 :3
"""

#Send the email
em = EmailMessage()
em['From'] = email_sender
em ['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)



#login/create acc

def print_all_artworks_with_artists():
    '''Print all artworks with artists nicely for option 1'''
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
    '''Print all artworks  sorted by variable with artists. Options 2-4'''
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
    '''Print all artworks with artists sorted by variable. Options 5-7'''
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
    '''Print all artworks with where sorted by variable. Options 8,1,1-2'''
    db = sqlite3.connect(DATABASE)
    
    cursor = db.cursor()

    sql = (f"SELECT Artwork.Name, Artist.Artist_name, Artwork.style, Artwork.Year_made, Artwork.Price FROM Artwork JOIN Artist ON Artist.id=Artwork.Artist WHERE {column} =  '{specific}' ORDER BY Artwork.Name ASC;")

    cursor.execute(sql)

    results = cursor.fetchall()

    #loop through results

    print(f"                       Name             Artist               Style     Year made    Price($)\n")

    for Artwork in results:
            
            print(f"{Artwork[0]:>27}{Artwork[1]:>20}{Artwork[2]:>20}{Artwork[3]:>13}{Artwork[4]:>10}M")

    #loop finishes here
        
    db.close()
 
def print_all_artists_sorted_with_where(specific):
    '''Print all artists with where sorted by variable. Options 8,2,1-3'''
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

def print_all_artworks_sorted_with_where_with_between(x,y):
    '''Print all artworks with where sorted by variable with between. Options 8,1,3'''
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
    '''Print all artists with where with between sorted by variable. Options 8,2,4'''
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
#print("If you would just like to view the artworks but don't want to buy them, username: guest, password: gpassword")
#while True:
#    log = input("\n1. Login\n2. Create account.\n")
#login system
#Loop fof user options.
while True:
    #Ask for user input
    userinput = input("\nHere are some options.\n\n1.View all artworks with artist information.\n2.View all artworks sorted alphabetically\n3.View all artworks sorted by year\n4.View all artworks sorted by price\n5.View all artists sorted alphabetically.\n6.View all artists sorted by year born.\n7.View all artists sorted by country\n8.Choose a specific column or name to sort by.\n9.Exit\n")
    if userinput == "1":
        #Print all artworks combined with artists table.
        print_all_artworks_with_artists()
    elif userinput == "2":
        #sort by artwork name alphabetically.
        sortedway = 'Artwork.Name'
        print_all_artworks_sorted_(sortedway)
    elif userinput == "3":
        #sort by year it was made ascending
        sortedway = 'Artwork.Year_made'
        print_all_artworks_sorted_(sortedway)
    elif userinput == "4":
        #View artwork table but sorted by price ascending.
        sortedway = 'Artwork.Price'
        print_all_artworks_sorted_(sortedway)
    elif userinput == "5":
        #View artists table but artists are sorted by name alphabetically.
        sortedway = 'Artist.Artist_name'
        print_all_artists_sorted_(sortedway)
    elif userinput == "6":
        #View artsits table but sorted by the  year the artists were born ascending.
        sortedway = 'Artist.Year_of_birth'
        print_all_artists_sorted_(sortedway)
    elif userinput == "7":
        #View artists table but sorted by the country they are from and the countries are sorted alphabetically.
        sortedway = 'Artist.Country'
        print_all_artists_sorted_(sortedway)
    elif userinput == "8":   
        #There are more options including user searches.
        eightinput = input("1.Specifics on Artworks.\n2.Specifics on Artists.\n3.Return\n")
        while True:    
            if eightinput == "1":
                #These are options relating to artworks.
                while True:
                    artvsartistinput = input("\n1.To find one 'artwork'.\n2.All artworks with one style\n3.All artworks where the year made falls under(x-y)\n4.Return\n")
                    if artvsartistinput == "1":
                        #this options finds a specific artwork the user searches for.
                        column = "Artwork.Name"
                        specific = input("Please type the name of the artwork you would like.(correctly with capitals): ")
                        print_all_artworks_sorted_with_where(specific)
                    elif artvsartistinput == "2":
                        #This option finds all artworks with a specific style the user would like.
                        column = "Artwork.Style"
                        specific = input("Please type the style of the artworks you would like.(correctly with capitals): ")
                        print_all_artworks_sorted_with_where(specific)
                    elif artvsartistinput == "3":
                        #This options finds all artworks made between 2 years the user chooses.
                        column = "Artwork.Year_made"
                        while True:
                            try:
                                x,y = input("Please type the years of the artworks you would like(example- 1400,1500): ").split(",")
                                x = int(x)
                                y = int(y)
                                print_all_artworks_sorted_with_where_with_between(x,y)
                                break
                            except ValueError:
                                #This catches exceptions where the input are not numbers.
                                print("Please enter numbers seperated by a comma.")    
                    elif artvsartistinput == "4":
                        break
                    else:
                        print("That was not a valid option.") 
            elif eightinput == "2":
                while True:
                    #These are options relating to artists. 
                    artistvsart = input("\n1.To find one artist.\n2.Find all Artists from one Country.\n3.Find all Artworks by one artist.\n4.Find all artists born in specific years.\n5.Return\n")
                    if artistvsart == "1":
                        #This brings up specific information about only one artist
                        column = "Artist.Artist_name"
                        specific = input("Please type the name of the artist you would like(correctly with capitals): ")
                        print_all_artists_sorted_with_where(specific)
                    elif artistvsart == "2":
                        #This find all artists from a country the user chooses.
                        column = "Artist.Country"
                        specific = input("Please type the name of the country you would like(correctly with capitals): ")
                        print_all_artists_sorted_with_where(specific)
                    elif artistvsart == "3":
                        #This finds all paintings from one specific artist.
                        column = "Artist.Artist_name"
                        specific = input("Please type the name of the artist for the artworks you would like(correctly with capitals): ")
                        print_all_artworks_sorted_with_where(specific)
                    elif artistvsart == "4":
                        column = "Year_of_birth"
                        #This finds all artists that were born between 2 years that the user chooses.
                        while True:
                            try:
                                x,y = input("Please type the years of artist's birth years you would like(example- 1400,1500): ").split(",")
                                x = int(x)
                                y = int(y)
                                print_all_artists_sorted_with_where_with_between(x,y)
                                break
                            except ValueError:
                                    print("Please enter numbers seperated by a comma.")    
                    elif artistvsart == "5":
                        break
                else:
                    print("That was not a valid option.") 
            elif eightinput == "3":
                break
            else:
                print("That was not a valid option.") 
    elif userinput == "9":   
        break 
    else:
        print("That was not a valid option. Please try again :O")  
    
    
