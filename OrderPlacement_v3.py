from tkinter import *
import random
from datetime import timedelta, date
import os

integrationsprogramm = "Marketplace CH"


def main():

     ###############################
     def set_integrationsprogramm(selection):
          global integrationsprogramm
          integrationsprogramm = selection

     ###############################
     def create_order(xml_temp_file,num1,d_address,dd_type=''):

          with open(xml_temp_file, 'r', encoding="utf-8") as file :
               filedata = file.read()

          # Replace the header
          filedata = filedata.replace('_sup_', h1.get())
          filedata = filedata.replace('_supn_', h2.get())
          filedata = filedata.replace('_ord_', str(num1))
          filedata = filedata.replace('_d_address_', d_address)
          filedata = filedata.replace('_dd_type_', dd_type)
          # Replace position 1
          filedata = filedata.replace('_sku_', i1_1.get())
          filedata = filedata.replace('_gtin_', i1_2.get())
          filedata = filedata.replace('_pri_', i1_3.get())
          filedata = filedata.replace('_prix_', str(float(i1_3.get())*float(i1_4.get())))
          filedata = filedata.replace('_tax_', str(round(float(i1_3.get())*0.077,2)))
          filedata = filedata.replace('_qnt_', i1_4.get())
          filedata = filedata.replace('_ddate_', str(date.today() + timedelta(days=10)))
          # Replace position 2
          filedata = filedata.replace('_sku2_', i2_1.get())
          filedata = filedata.replace('_gtin2_', i2_2.get())
          filedata = filedata.replace('_pri2_', i2_3.get())
          filedata = filedata.replace('_prix2_', str(float(i2_3.get())*float(i2_4.get())))
          filedata = filedata.replace('_tax2_', str(round(float(i2_3.get())*0.077,2)))
          filedata = filedata.replace('_qnt2_', i2_4.get())
          filedata = filedata.replace('_ddate2_', str(date.today() + timedelta(days=10)))
          # Replace totals
          filedata = filedata.replace('_qntt_', str(int(i1_4.get())+int(i2_4.get())))
          filedata = filedata.replace('_prixt_', str(float(i1_3.get())*float(i1_4.get()) + float(i2_3.get())*float(i2_4.get())))


          # Write the file out again
          with open('GORDP_'+str(num1)+'.xml', 'w', encoding="utf-8") as filew:
               filew.write(filedata)
   

     ################################
     def create_orders():
          #print("SupplierId: %s\nSKU: %s" % (h1.get(), h2.get()))
          num1 = random.randint(60000000, 70000000)
          d_address = ''

          if integrationsprogramm == "Marketplace CH":
               xml_temp_file = os.getcwd()+'/ORDP_templates/template_GORDP_MP_CH.xml'
               with open(os.getcwd()+'/address_templates/address_private_customer.xml', 'r', encoding="utf-8") as file :
                    d_address = file.read()
               create_order(xml_temp_file,num1,d_address)
               with open(os.getcwd()+'/address_templates/address_company.xml', 'r', encoding="utf-8") as file :
                    d_address = file.read()
               create_order(xml_temp_file,num1+10,d_address)
          elif integrationsprogramm == "Marketplace CH EU-Hub Fiskalvertretung":
               xml_temp_file = os.getcwd()+'/ORDP_templates/template_GORDP_MP_CH_EU_F.xml'
               create_order(xml_temp_file,num1,d_address)
          elif integrationsprogramm == "Marketplace CH EU-Hub Keine Fiskalvertretung":
               xml_temp_file = os.getcwd()+'/ORDP_templates/template_GORDP_MP_CH_EU_oF.xml'
               create_order(xml_temp_file,num1,d_address)
          elif integrationsprogramm == "Retail DD CH":
               xml_temp_file = os.getcwd()+'/ORDP_templates/template_GORDP_DD_CH.xml'
               with open(os.getcwd()+'/address_templates/address_private_customer.xml', 'r', encoding="utf-8") as file :
                    d_address = file.read()
               create_order(xml_temp_file,num1,d_address)
               with open(os.getcwd()+'/address_templates/address_company.xml', 'r', encoding="utf-8") as file :
                    d_address = file.read()
               create_order(xml_temp_file,num1+10,d_address)
          elif integrationsprogramm == "Retail WD CH":
               xml_temp_file = os.getcwd()+'/ORDP_templates/template_GORDP_WD_CH.xml'
               dd_type = 'optional'
               with open(os.getcwd()+'/address_templates/address_wohlen.xml', 'r', encoding="utf-8") as file :
                    d_address = file.read()
               create_order(xml_temp_file,num1,d_address,dd_type)
               with open(os.getcwd()+'/address_templates/address_dintikon.xml', 'r', encoding="utf-8") as file :
                    d_address = file.read()
               create_order(xml_temp_file,num1+10,d_address,dd_type)
               with open(os.getcwd()+'/address_templates/address_roggwil.xml', 'r', encoding="utf-8") as file :
                    d_address = file.read()
               create_order(xml_temp_file,num1+20,d_address,dd_type)
               dd_type = 'fixed'
               with open(os.getcwd()+'/address_templates/address_oftringen.xml', 'r', encoding="utf-8") as file :
                    d_address = file.read()
               create_order(xml_temp_file,num1+30,d_address,dd_type)
          elif integrationsprogramm == "Retail WD EU":
               xml_temp_file = os.getcwd()+'/ORDP_templates/template_GORDP_WD_EU.xml'
               dd_type = 'fixed'
               create_order(xml_temp_file,num1,d_address,dd_type)
               dd_type = 'optional'
               create_order(xml_temp_file,num1+10,d_address,dd_type)
          elif integrationsprogramm == "Retail DD EU":
               xml_temp_file = os.getcwd()+'/ORDP_templates/template_GORDP_DD_EU.xml'
               with open(os.getcwd()+'/address_templates/address_private_customer_EU.xml', 'r', encoding="utf-8") as file :
                    d_address = file.read()
               create_order(xml_temp_file,num1,d_address)
               with open(os.getcwd()+'/address_templates/address_company_EU.xml', 'r', encoding="utf-8") as file :
                    d_address = file.read()
               create_order(xml_temp_file,num1+10,d_address)
          else:
               xml_temp_file = os.getcwd()+'/ORDP_templates/template_GORDP_MP_CH.xml'
               create_order(xml_temp_file,num1,d_address)

     master = Tk()
     Label(master, text="Supplier (Id, Name)",justify="left", anchor="w").grid(row=1)
     Label(master, text="Delivery Date Type").grid(row=2)
     Label(master, text="Position 1: (SKU, Gtin, Price, Quantity)").grid(row=3)
     Label(master, text="Position 2: (SKU, Gtin, Price, Quantity)").grid(row=4)
     

     h1 = Entry(master)
     h2 = Entry(master)
     i1_1 = Entry(master)
     i1_2 = Entry(master)
     i1_3 = Entry(master)
     i1_4 = Entry(master)
     i2_1 = Entry(master)
     i2_2 = Entry(master)
     i2_3 = Entry(master)
     i2_4 = Entry(master)

     h1.grid(row=1, column=1)
     h2.grid(row=1, column=2)
     i1_1.grid(row=3, column=1)
     i1_2.grid(row=3, column=2)
     i1_3.grid(row=3, column=3)
     i1_4.grid(row=3, column=4)
     i2_1.grid(row=4, column=1)
     i2_2.grid(row=4, column=2)
     i2_3.grid(row=4, column=3)
     i2_4.grid(row=4, column=4)

     h1.insert(END, '123456')
     h2.insert(END, 'Händlername')
     i1_1.insert(END, 'WN1234')
     i1_2.insert(END, '04064575370124')
     i1_3.insert(END, '1390.33')
     i1_4.insert(END, '4')
     i2_1.insert(END, 'AN1234')
     i2_2.insert(END, '04064575370124')
     i2_3.insert(END, '1390.33')
     i2_4.insert(END, '3')

     Button(master, text='Quit', command=master.quit).grid(row=10, column=0, sticky=W, pady=4)
     Button(master, text='Create GORDP', command=create_orders).grid(row=10, column=1, sticky=W, pady=4)

     # Dropdown menu options
     integrationsprogramme = [
     "Marketplace CH",
     "Marketplace CH EU-Hub Fiskalvertretung",
     "Marketplace CH EU-Hub Keine Fiskalvertretung",
     "Retail DD CH",
     "Retail DD EU",
     "TBD - Retail DD EU EU-Hub",
     "Retail WD CH",
     "Retail WD EU"
     ]

     # datatype of menu text
     clicked = StringVar()
     
     # initial menu text
     clicked.set( "Marketplace CH" )
     
     # Create Dropdown menu
     drop = OptionMenu( master , clicked , *integrationsprogramme, command=set_integrationsprogramm)
     drop.grid(row=0, column=0)

     master.mainloop( )


if __name__ == '__main__':
    main()