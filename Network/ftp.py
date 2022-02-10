'''
Get the most recent weather forecast
'''

from ftplib import FTP

ftp = FTP('tgftp.nws.noaa.gov')
ftp.login()
ftp.cwd('/data/observations/metar/decoded')

'''
    EIAB – Abbeyshrule Aerodrome – Abbeyshrule, County Longford
    EIBN (BYT) – Bantry Aerodrome – Bantry, County Cork
    EIBR – Birr Aerodrome – Birr, County Offaly
    EICA (NNR) – Connemara Regional Airport – Inverin, Connemara
    EICB – Castlebar Airport – Castlebar, County Mayo
    EICK (ORK) – Cork International Airport – Cork
    EICL – Clonbullogue Aerodrome – Clonbullogue, County Offaly
    EICM (GWY) – Galway Airport – Carnmore, County Galway
    EICN – Coonagh Airport – Limerick, County Limerick
    EIDL (CFN) – Donegal Airport – Carrickfinn, County Donegal
    EIDW (DUB) – Dublin Airport – Dublin
    EIIM (IOR) – Inishmore Aerodrome (Kilronan Airport) – Kilronan, County Galway
    EIKL (KKY) – Kilkenny Airport – Kilkenny, County Kilkenny
    EIKN (NOC) – Ireland West Airport Knock – Knock, County Mayo
    EIKY (KIR) – Kerry Airport – Farranfore, County Kerry
    EIME – Casement Aerodrome – Baldonnel
    EIMH – Athboy Airfield – Athboy, County Meath
    EIMY – Moyne Aerodrome – Thurles, County Tipperary
    EINN (SNN) – Shannon Airport – Shannon, County Clare
    EIRT – Rathcoole Aerodrome – Rathcoole (Ráth Chúil), County Cork (Contae Chorcaí)
    EISG (SXL) – Sligo Airport – Strandhill, near Sligo
    EIWF (WAT) – Waterford Airport – Waterford
    EIWT (WST) – Weston Airport – Leixlip, County Kildare
    
    EGAA (BFS) – Belfast International Airport – Belfast, Northern Ireland
    EGAB (ENK) – Enniskillen/St Angelo Airport – Enniskillen, Northern Ireland
    EGAC (BHD) – George Best Belfast City Airport – Belfast, Northern Ireland
    EGAD – Newtownards Airport – Newtownards, Northern Ireland
    EGAE (LDY) – City of Derry Airport – Derry, Northern Ireland

'''

filename = 'EGAE.TXT'

with open(filename, 'wb') as ftpfile:
    ftp.retrbinary('RETR ' + filename, ftpfile.write)

ftp.quit()

with open(filename) as file:
    for row in file:
        print(row.strip())