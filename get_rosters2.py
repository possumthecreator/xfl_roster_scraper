#/usr/bin/env python3
  
from lxml import html
import requests
import regex as re
import pdb


def run_dalren():
    page = requests.get('https://www.xfl.com/en-US/teams/dallas/renegades-articles/dallas-renegades-roster')
    tree = html.fromstring(page.content)

    # XPaths
    number = tree.xpath('//table/tbody/tr/td[1]//text()')
    first_name = tree.xpath('//table/tbody/tr/td[2]//text()')
    last_name = tree.xpath('//table/tbody/tr/td[3]//text()')
    #position = tree.xpath('//table/tbody/tr[>1]/td[4]//text()')
    #height = tree.xpath('//table/tbody/tr[!1]/td[5]//text()')
    #weight = tree.xpath('//table/tbody/tr[!1]/td[6]//text()')
    college = tree.xpath('//table/tbody/tr/td[7]//text()')

    print("\n\tDALLAS RENEGADES Roster\n")

    # Trying to iterate for each item in the list
    for i, (xnumber, xfirst_name, xlast_name, xcollege) in enumerate(zip(number, first_name, last_name, college)):
        print(xnumber, "\t", xfirst_name, xlast_name, "    \t\t", xcollege, "\n")

def run_dcdef():
    page = requests.get('https://www.xfl.com/en-US/teams/washington-dc/defenders-articles/dc-defenders-roster')
    tree = html.fromstring(page.content)

    # XPaths
    number = tree.xpath('//table/tbody/tr/td[1]//text()')
    first_name = tree.xpath('//table/tbody/tr/td[2]//text()')
    last_name = tree.xpath('//table/tbody/tr/td[3]//text()')
    #position = tree.xpath('//table/tbody/tr[>1]/td[4]//text()')
    #height = tree.xpath('//table/tbody/tr[!1]/td[5]//text()')
    #weight = tree.xpath('//table/tbody/tr[!1]/td[6]//text()')
    college = tree.xpath('//table/tbody/tr/td[7]//text()')

    print("\n\tDC DEFENDERS Roster\n")

    # Trying to iterate for each item in the list
    for i, (xnumber,xfirst_name, xlast_name, xcollege) in enumerate(zip(number, first_name, last_name, college)):
        print(xnumber, "\t", xfirst_name, xlast_name, "    \t\t", xcollege, "\n")

def run_hourou():
    page = requests.get('https://www.xfl.com/en-US/teams/houston/roughnecks-articles/houston-roughnecks-roster')
    tree = html.fromstring(page.content)
    p = re.compile(r'\W+')  # Set a regex expression to seperate first and last name (with plans to reverse)

    # XPaths
    number = tree.xpath('//table/tbody/tr/td[1]//text()')
    name = tree.xpath('//table/tbody/tr/td[2]//text()')
    #position = tree.xpath('//table/tbody/tr[>1]/td[3]//text()')
    #height = tree.xpath('//table/tbody/tr[!1]/td[4]//text()')
    #weight = tree.xpath('//table/tbody/tr[!1]/td[5]//text()')
    college = tree.xpath('//table/tbody/tr/td[6]//text()')
    
    print("\n\tHOUSTON ROUGHNECKS Roster\n")
   
    for i, (xnumber, xname, xcollege) in enumerate(zip(number, name, college)):
        print(xnumber, "\t", xname, "    \t\t", xcollege, "\n")

def run_lawil():
    page = requests.get('https://www.xfl.com/en-US/teams/los-angeles/wildcats-articles/la-wildcats-roster')
    tree = html.fromstring(page.content)

    # XPaths
    number = tree.xpath('//table/tbody/tr/td[1]//text()')
    first_name = tree.xpath('//table/tbody/tr/td[2]//text()')
    last_name = tree.xpath('//table/tbody/tr/td[3]//text()')
    #position = tree.xpath('//table/tbody/tr[>1]/td[4]//text()')
    #height = tree.xpath('//table/tbody/tr[!1]/td[5]//text()')
    #weight = tree.xpath('//table/tbody/tr[!1]/td[6]//text()')
    college = tree.xpath('//table/tbody/tr/td[7]//text()')

    print("\n\tLA WILDCATS Roster\n")

    # Trying to iterate for each item in the list
    for i, (xnumber,xfirst_name, xlast_name, xcollege) in enumerate(zip(number, first_name, last_name, college)):
        print(xnumber, "\t", xfirst_name, xlast_name, "    \t\t", xcollege, "\n")

def run_nygau():
    page = requests.get('https://www.xfl.com/en-US/teams/new-york/guardians-articles/new-york-guardians-roster')
    tree = html.fromstring(page.content)

    # XPaths
    number = tree.xpath('//table/tbody/tr/td[1]//text()')
    name = tree.xpath('//table/tbody/tr/td[2]//text()')
    #last_name = tree.xpath('//table/tbody/tr/td[3]//text()')
    #position = tree.xpath('//table/tbody/tr[>1]/td[3]//text()')
    #height = tree.xpath('//table/tbody/tr[!1]/td[4]//text()')
    #weight = tree.xpath('//table/tbody/tr[!1]/td[5]//text()')
    college = tree.xpath('//table/tbody/tr/td[6]//text()')

    print("\n\tNY GUARDIANS Roster\n")

    # Trying to iterate for each item in the list
    for i, (xnumber,xname, xcollege) in enumerate(zip(number, name, college)):
        print(xnumber, "\t", xname, "    \t\t", xcollege, "\n")

def run_stlbat():
    page = requests.get('https://www.xfl.com/en-US/teams/st-louis/battlehawks-articles/st-louis-battlehawks-roster')
    tree = html.fromstring(page.content)

    # XPaths
    number = tree.xpath('//table/tbody/tr/td[1]//text()')
    name = tree.xpath('//table/tbody/tr/td[2]//text()')
    #last_name = tree.xpath('//table/tbody/tr/td[3]//text()')
    #position = tree.xpath('//table/tbody/tr[>1]/td[3]//text()')
    #height = tree.xpath('//table/tbody/tr[!1]/td[4]//text()')
    #weight = tree.xpath('//table/tbody/tr[!1]/td[5]//text()')
    college = tree.xpath('//table/tbody/tr/td[6]//text()')

    print("\n\tST LOUIS BATTLEHAWKS Roster\n")

    # Trying to iterate for each item in the list
    for i, (xnumber,xname, xcollege) in enumerate(zip(number, name, college)):
        print(xnumber, "\t", xname, "    \t\t", xcollege, "\n")

def run_seadra():
    page = requests.get('https://www.xfl.com/en-US/teams/seattle/dragons-articles/seattle-dragons-roster')
    tree = html.fromstring(page.content)

    # XPaths
    number = tree.xpath('//table/tbody/tr/td[1]//text()')
    name = tree.xpath('//table/tbody/tr/td[2]//text()')
    #last_name = tree.xpath('//table/tbody/tr/td[3]//text()')
    #position = tree.xpath('//table/tbody/tr[>1]/td[3]//text()')
    #height = tree.xpath('//table/tbody/tr[!1]/td[4]//text()')
    #weight = tree.xpath('//table/tbody/tr[!1]/td[5]//text()')
    college = tree.xpath('//table/tbody/tr/td[6]//text()')

    print("\n\tSEATTLE DRAGONS Roster\n")

    # Trying to iterate for each item in the list
    for i, (xnumber,xname, xcollege) in enumerate(zip(number, name, college)):
        print(xnumber, "\t", xname, "    \t\t", xcollege, "\n")

def run_tbvip():
    page = requests.get('https://www.xfl.com/en-US/teams/tampa-bay/vipers-articles/tampa-bay-vipers-roster')
    tree = html.fromstring(page.content)

    # XPaths
    number = tree.xpath('//table/tbody/tr/td[1]//text()')
    name = tree.xpath('//table/tbody/tr/td[2]//text()')
    #last_name = tree.xpath('//table/tbody/tr/td[3]//text()')
    #position = tree.xpath('//table/tbody/tr[>1]/td[3]//text()')
    #height = tree.xpath('//table/tbody/tr[!1]/td[4]//text()')
    #weight = tree.xpath('//table/tbody/tr[!1]/td[5]//text()')
    college = tree.xpath('//table/tbody/tr/td[6]//text()')

    print("\n\tTAMPA BAY VIPERS Roster\n")

    # Trying to iterate for each item in the list
    for i, (xnumber,xname, xcollege) in enumerate(zip(number, name, college)):
        print(xnumber, "\t", xname, "    \t\t", xcollege, "\n")




#pdb.set_trace()
run_dalren()
run_dcdef()
run_hourou() #dif & name reversed
run_lawil()
run_nygau() #dif
run_stlbat() #dif
run_seadra() #dif
run_tbvip() #dif


