from base64 import decode, encode
import os
import requests
import gspread
import pandas as pd
from google_drive_downloader import GoogleDriveDownloader as gdd
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import shutil
import tkinter as tk
from tkinter import DISABLED, LEFT, Label, StringVar, ttk
from tkinter import messagebox
from tkinter.messagebox import showinfo
from PIL import Image, ImageTk
from datetime import date, timedelta
import matplotlib.pyplot as plt
from tkinter.filedialog import askdirectory

#Constants:

today=date.today()
fileName="./images/Credential.json" #Credential File

Logo='./images/LOGO.ico'
bztFcqDi1Gy='./images/JpgLogo.png'
downloadICon="./images/DownloadIcon.jpg"
JpgLogo='./images/JpgLogo.png'
SubmitIcon='./images/SubmitIcon.png'
DeleteIcon='./images/DeleteIcon.png'
StatusIcon='./images/StatusIcon.png'

my_img=Image.open(bztFcqDi1Gy)
resize_img=my_img.resize((600,120),Image.Resampling.LANCZOS)

my_img1=Image.open(downloadICon)
resize_my_img1=my_img1.resize((20,20),Image.Resampling.LANCZOS)

my_img2=Image.open(JpgLogo)
resize_my_img2=my_img2.resize((35,35),Image.Resampling.LANCZOS)

my_img3=Image.open(SubmitIcon)
resize_my_img3=my_img3.resize((40,20),Image.Resampling.LANCZOS)

my_img4=Image.open(DeleteIcon)
resize_my_img4=my_img4.resize((40,20),Image.Resampling.LANCZOS)

my_img5=Image.open(StatusIcon)
resize_my_img5=my_img5.resize((50,25),Image.Resampling.LANCZOS)


'''                                     --Fonts needed for the work:---                                                                    '''

Font_tuple0=('Helvetica',7,'bold')
Font_tuple1=('Helvetica',8,'bold')
Font_tuple2=('Helvetica',10,'bold')
Font_tuple3=('Helvetica',12,'bold')
Font_tuple4=('Helvetica',14,'bold')
Font_tuple5=('Helvetica',16,'bold')
Font_tuple6=('Consolas Bold Italic',18,'bold','italic')

#colors:
fg_0366fc="#0366fc"

#Padding:
padding={'padx':15,'pady':15}
# Gspread and spreadsheet:

#sa=gspread.service_account(filename=fileName)
#BATCH=sa.open("Copy of Batch 24062022")
#batch_tracker=BATCH.worksheet("Batch tracker")
#WorkSheet15=BATCH.worksheet("Feuille 15")
sa = ""
batch_tracker = ""


class UnwantedTestingstuff:
    '''                                          ----enumerate----                               '''
    def Testing_enumerate():
        list=["abc","dfg","zaea","dazeza"]
        for n,p in enumerate(list):
            print(n,p)
    '''
        Output:
        0 abc
        1 dfg
        2 zaea
        3 dazeza
    '''  
    '''                                        ----Downloading an image----                                                        ''' 
    def ImageDownloadfunc():
        SAVE_FOLDER="images"
        print("Downloading image:...")
        img='https://orderdesk-data.s3.amazonaws.com/amazon-customizations/29030/3b623fbf-60bb-4366-bf8c-0ecdde538282.jpg'
        response=requests.get(img)
        imagename=SAVE_FOLDER+ '/'+'TEST.jpg'
        with open(imagename,'wb')as file:
            file.write(response.content)
            
        print("Done")
    
    def filtermethode():
        numbers = [1, 2, 3, 4, 5, 6, 7]
        even_numbers_iterator = list(filter(lambda x: x!=1, numbers))
        print(even_numbers_iterator) # -> [2, 3, 4, 5, 6, 7]
        numbers=[[1,2],[1,''],[4,6],[8,7],[3,'']]
        print(list(filter(lambda x: x[1]=='',numbers))) # ->[[1, ''], [3, '']]
    
    def Dataclansing():
        ll=[['1', '204-4668679-9510767', 'Medium Rectangle', '1', 'https://orderdesk-data.s3.amazonaws.com/amazon-customizations/29030/3b623fbf-60bb-4366-bf8c-0ecdde538282.jpg', 'Love you both millions and billions', 'Bobby Kirkwood'],
            ['2', '204-4668679-9510767', 'LED Base', '1', 'nan', '', 'Bobby Kirkwood'],
            ['3', '026-8331225-5876303', 'AW2MN0', '1', 'https://orderdesk-data.s3.amazonaws.com/amazon-customizations/29030/204edc99-7bad-433e-9fee-cff8bd30e813.jpg', '', 'CLARE BLOOMFIELD'],
            ['4', '206-6495755-2541101', 'AW2MN0', '1', 'https://orderdesk-data.s3.amazonaws.com/amazon-customizations/29030/5284c6b7-7557-4ab0-99da-3ef335df1616.jpg', 'Love you lots B', 'Elrich Dup'],
            ['5', '206-6495755-2541101', 'LED Base', '1', 'nan', '', 'Elrich Dup'], ['6', '204-1092630-5911518', 'AW2MN0', '1', 'https://orderdesk-data.s3.amazonaws.com/amazon-customizations/29030/ad3a5684-e3fd-4b56-8e41-7caec2dee272.png', '', 'JULIANNE HATTON'], ['7', '112-3168939-6397842', 'AW2MN0', '1', 'https://orderdesk-data.s3.amazonaws.com/amazon-customizations/29030/c86e8361-0db2-48db-9ee7-d6f6e266386e.jpg', '', 'Jake Limond'], ['8', '305-3545399-3045966', 'AW2MN0', '1', 'https://orderdesk-data.s3.amazonaws.com/amazon-customizations/29030/0b34c6ad-26cf-4bc6-bc39-e735d37885e4.jpg', 'Zum 70. Geburtstag', 'Jens Silabetzschky'], ['9', '305-3545399-3045966', 'LED Base', '1', 'nan', '', 'Jens Silabetzschky'], ['10', '206-7847683-1282754', 'AW2MN0', '1', 'https://orderdesk-data.s3.amazonaws.com/amazon-customizations/29030/c5338cbe-7b15-4a84-8736-41638cc518cc.jpg', 'Luff yoo always xxx', 'Linsey Lynch'], ['11', '2555498524', 'XL Rectangle', '1', 'https://drive.google.com/drive/folders/1Dng-Lms0MxTILuH7L7EPg3x-vV0hjDOn', 'Lotta', 'Lisa Sbitnew'], ['12', '2555498524', 'LED Base', '1', 'nan', '', 'Lisa Sbitnew'], ['13', '2555498524', 'Gift Card', '1', 'nan', '', 'Lisa Sbitnew'], ['14', '205-0362332-6845142', 'XL Rectangle', '1', 'https://orderdesk-data.s3.amazonaws.com/amazon-customizations/29030/f190ac54-623b-4507-b5a7-ada45164d459.jpg', 'Love you x', 'Mark Howells'], ['15', '205-0362332-6845142', 'LED Base', '1', 'nan', '', 'Mark Howells'], ['16', '205-0362332-6845142', 'Cleaning Kit', '1', 'nan', '', 'Mark Howells'], ['17', '205-0362332-6845142', 'Bag', '1', 'nan', '', 'Mark Howells'], ['18', '205-0362332-6845142', 'KC2MN0', '1', 'https://orderdesk-data.s3.amazonaws.com/amazon-customizations/29030/f190ac54-623b-4507-b5a7-ada45164d459.jpg', '', 'Mark Howells'], ['19', '202-1914497-3336362', 'AW2MN0', '1', 'https://orderdesk-data.s3.amazonaws.com/amazon-customizations/29030/9f7fb341-436d-445f-8e86-5e7c1077008d.jpg', 'The King Of Turf\r\n       casper', 'Martin Smith'], ['20', '304-7602501-4381159', 'AW2MN0', '1', 'https://orderdesk-data.s3.amazonaws.com/amazon-customizations/29030/5d43db08-4822-4756-8a1c-35ef2b3d29e9.jpg', 'Wir lieben dich', 'Michèl Adam'], ['21', '203-2119132-9082721', 'AW2MN0', '1', 'https://orderdesk-data.s3.amazonaws.com/amazon-customizations/29030/14d16367-5311-4aa5-8f3b-26f2e350f621.jpg', 'Happy Birthday \r\nto a wonderful sister \r\nlove Muriel', 'Muriel TEAGE-ROWLAND'], ['22', '205-1850482-4442763', 'AW2MN0', '1', 'https://orderdesk-data.s3.amazonaws.com/amazon-customizations/29030/5b58a751-9dd2-4e2b-ad99-0c1b4b5bf217.jpg', 'Daisy’s Christening 5 June 22 love Nan & Grandad', 'Sharon Mitchell']] 

        ll=list(filter(lambda x: x[4][:5]=='https',ll))

        urlList=[]
        urlname=[]
        urltxt=[]
        for element in ll:
            urlList.append(element[4])
            urltxt.append(element[5])
            urlname.append(f'{element[2]} {element[-1]}')


        Batch_dict={"SKU/Name":urlname,
                    "URL":urlList,
                    'Text':urltxt}

        data=pd.DataFrame(Batch_dict)

        print(data)
        '''                           SKU/Name  ...                                               Text
                        0   Medium Rectangle Bobby Kirkwood  ...                Love you both millions and billions
                        1           AW2MN0 CLARE BLOOMFIELD  ...
                        2                 AW2MN0 Elrich Dup  ...                                    Love you lots B
                        3            AW2MN0 JULIANNE HATTON  ...
                        4                AW2MN0 Jake Limond  ...
                        5         AW2MN0 Jens Silabetzschky  ...                                 Zum 70. Geburtstag
                        6               AW2MN0 Linsey Lynch  ...                                Luff yoo always xxx
                        7         XL Rectangle Lisa Sbitnew  ...                                              Lotta
                        8         XL Rectangle Mark Howells  ...                                         Love you x
                        9               KC2MN0 Mark Howells  ...
                        10              AW2MN0 Martin Smith  ...                  The King Of Turf\r\n       casper
                        11               AW2MN0 Michèl Adam  ...                                    Wir lieben dich
                        12      AW2MN0 Muriel TEAGE-ROWLAND  ...  Happy Birthday \r\nto a wonderful sister \r\nl...
                        13           AW2MN0 Sharon Mitchell  ...   Daisy’s Christening 5 June 22 love Nan & Grandad '''
    
    def downloadingFromDrive():
        '''This functions uses from google_drive_downloader import GoogleDriveDownloader as gdd'''
        SAVE_FOLDER="images"

        print("Downloading image:...")
        #https://discuss.dizzycoding.com/python-download-files-from-google-drive-using-url/
        folder='https://drive.google.com/drive/folders/1Dng-Lms0MxTILuH7L7EPg3x-vV0hjDOn'
        url='https://drive.google.com/drive/folders/1Dng-Lms0MxTILuH7L7EPg3x-vV0hjDOn?usp=sharing'
        gdd.download_file_from_google_drive(file_id='1Dng-Lms0MxTILuH7L7EPg3x-vV0hjDOn',
                                            dest_path=SAVE_FOLDER+"/"+"TEST.zip",
                                            unzip=True)

        print('Done')
        
    def FilePathGetter():
        File='2555498524.jpg'
        print(f'Path of this file {File} is:\t ',os.path.abspath(File))                         
        #Path of this file 2555498524.jpg is:      C:\Users\admin\Downloads\Python_Project\2555498524.jpg 
        print("Moving file:...")
        src_path=os.path.abspath(File)
        dst_path=f'images/{File}'
        shutil.move(src_path,dst_path) #shell utilities
        print("File has been moved!")

class ImageDownloader:
    
    def ImageDownloadfunc(img:str,imagefolder:str):
        SAVE_FOLDER="images"
        print("Downloading image:...")
        img='https://orderdesk-data.s3.amazonaws.com/amazon-customizations/29030/3b623fbf-60bb-4366-bf8c-0ecdde538282.jpg'
        response=requests.get(img)

        imagefolder=SAVE_FOLDER+ '/'+'TEST.jpg'

        with open(imagefolder,'wb')as file:
            file.write(response.content)
            
        print("Done")   
         
    def Download_from_drive(folder:str,): 
        gauth=GoogleAuth()
        drive=GoogleDrive(gauth)

        folder="1Dng-Lms0MxTILuH7L7EPg3x-vV0hjDOn"

        directory='images/' #Directory         
        
        file_list=drive.ListFile({'q': f"'{folder}' in parents and trashed=false"}).GetList()
        for index, file in enumerate(file_list):
            #print(index+1,'file downloaded:\t',file["title"])            
            #split=os.path.splitext(file) => ('my_file', '.txt') 
            if not(os.path.exists(str(file['title']))):
                file.GetContentFile(file['title'])
                src_path=os.path.abspath(str(file["title"]))
                dst_path=directory+f'{str(file["title"])}'
                shutil.move(src_path,dst_path)
            else:
                print("Files already exists") #works
                  
class BatchImageDownloader:
    
    def LastRowID(self,worksheet,i:int) -> int:
        Last_rowList=list(filter(None,worksheet.col_values(i)))
        return len(Last_rowList)+1
    
    def BatchDatagetter(self,):
        OurBatch=batch_tracker.get(f'A2:G{self.LastRowID(self,batch_tracker,1)}')
        UlinkedLists=list(filter(lambda x: x[4][:5]!='https'),OurBatch) # -> List() of orders without link
        OurBatch=list(filter(lambda x: x[4][:5]=='https',OurBatch)) # -> List() of orders with links
        
             
BatchID=''
Current=''

class ImagesDownloaderApp(tk.Tk,): 

    def BatchIDGetter(self,):
        global BatchID        
        global Current
        global TextVariable

        TextVariable.set('Download files')
        try:
            sa.open(self.BatchEntry.get())
            if BatchID=='':
                BatchID=self.BatchEntry.get()                
                Current=BatchID
                messagebox.showinfo('Information',f'{BatchID} has been submitted!')
            else:
                BatchID=self.BatchEntry.get()
                messagebox.showinfo('Information',f'{Current} has been removed\n{BatchID} has been added!')
                Current=BatchID
            self.Status.state(['!disabled'])  #  // button.state(['disabled'])
            self.deleteBatch.state(['!disabled'])
            self.BatchEntry.delete(0,'end')
            self.BatchEntry.insert(0,"Enter the batch:...")
            self.DownloadButton.state(['!disabled'])    
        except:
            messagebox.showerror('Error','Could not open this batch.\n\nCheck here why:\n\n1) Add access to the Batch;OR\n2) Contact developer')
    
    def BatchIDDeletter(self):
        global BatchID
        messagebox.showinfo('Information',f'{BatchID} has been deleted from the data base.')
        BatchID=''
        self.Status.state(['disabled']) 
        self.deleteBatch.state(['disabled']) 
        #self.BatchEntry.delete(0,END)
        self.BatchEntry.delete(0,'end')
        self.BatchEntry.insert(0,"Enter the Batch:...") 
        self.DownloadButton.state(['disabled'])
    
    def SplittingUrl(self,Url=str)->str:
        i=len(Url)-1 
        while (i>=0):
            if Url[i]=='/':
                 return Url[i+1:len(Url)]
            i-=1
    
    def LastRowID(self,worksheet,i=int) -> int:
        Last_rowList=list(filter(None,worksheet.col_values(i)))
        return len(Last_rowList)+1        
    
    def FolderExistsCheck(self,folder=str):
        if not(os.path.exists(folder)):
            os.mkdir(folder)
    
    def ShopifyUrlgetter(self,Url=str)->str:
        ID=(Url.split("=")[2]).split("&")[0]
        AltUrl=f'https://cdn.getuploadkit.com/{ID}/Test.jpg'
        return AltUrl
    
    def BatchFileDownloader(self):
        global BatchID
        global TextVariable
        
        Batch=sa.open(BatchID)
        Batch_tracker=Batch.worksheet('Batch tracker')
        OurBatch=Batch_tracker.get(f'A2:G{self.LastRowID(Batch_tracker,1)}')
        LinkedLists=list(filter(lambda x: x[4][:5]=='https',OurBatch)) #Getting the list with the https links
        
        SAVE_FOLDER=askdirectory(title='Select the folder to download in')#Getting the directroy to download the files in
        TextVariable.set("Downloading:...")
        
        for element in LinkedLists:
            directory=SAVE_FOLDER+'\\'+f'{element[1]}'
            if element[4][:13]!='https://drive': # files type :https://orderdesk-data.s3.amazonaws
                #Creating the folder name inside the directory we selected:
                self.FolderExistsCheck(folder=directory)               
                response=requests.get(element[4]) #Getting the data of the url
                
                imagefolder=directory+'\\'+f'{element[0]}_{element[1]}_{element[2]}.jpg' # -> This is the image, editing the name and setting the extention
                txtfolder=directory+'\\'+f'{element[0]}_text.txt'#Setting up the text folder
                Clientfolder=directory+'\\'+f'{element[0]}_ClientInfo.txt'#Client information
                
                with open(imagefolder,'wb') as file:
                    file.write(response.content)
                with open(txtfolder,'w', encoding="utf-8") as file:
                    if element[-2]!='': file.write(element[-2])
                    else: file.write('No text for this order')
                with open(Clientfolder,'w') as file:
                    file.write(f'[OrderID:\t{element[1]}\nSku:\t{element[2]}\nClient_Name:\t{element[-1]}]')
            '''
            elif element[4][:13]=='https://drive': # files type https://drive
                gauth=GoogleAuth()
                drive=GoogleDrive(gauth)
                
                folder=self.SplittingUrl(Url=element[4])
                
                file_list=drive.ListFile({'q':f"'{folder}' in parents and trashed=false"}).GetList() #Gets the list of the existing files
                self.FolderExistsCheck(folder=directory)

                for file in file_list:
                    file.GetContentFile(file['title'])
                    src_path=os.path.abspath(str(file['title']))
                    dst_path=directory+'\\'+str(file['title'])
                    shutil.move(src_path,dst_path)#Moving the folder from the path downloaded to the one needed
                
                Clientfolder=directory+'\\'+f'{element[0]}_ClientInfo.txt'

                with open(Clientfolder,'w') as file:
                    file.write(f'[OrderID:\t{element[1]}\nSku:\t{element[2]}\nClient_Name:\t{element[-1]}]')
            else: # getting the files type : https://cdn.shopify.com                
                self.FolderExistsCheck(folder=directory) #Check whether or not directory=directory=SAVE_FOLDER+'\\'+f'{element[1]}' exists
                URL=element[4]
                Img=self.ShopifyUrlgetter(URL)
                response=requests.get(Img)   
                imagefolder=directory+'\\'+f'{element[0]}_{element[1]}_{element[2]}.jpg' # -> This is the image, editing the name and setting the extention
                txtfolder=directory+'\\'+f'{element[0]}_text.txt'#Setting up the text folder
                Clientfolder=directory+'\\'+f'{element[0]}_ClientInfo.txt'#Client information  
                #Writing in folder files:
                with open(imagefolder,'wb') as file:
                    file.write(response.content)
                with open(txtfolder,'w',encoding="utf-8") as file:
                    if element[-2]!='': file.write(element[-2])
                    else: file.write('No text for this order')
                with open(Clientfolder,'w') as file:
                    file.write(f'[OrderID:\t{element[1]}\nSku:\t{element[2]}\nClient_Name:\t{element[-1]}]') '''        
                
        BatchID=''
        self.DownloadButton.state(['disabled']) 
        TextVariable.set('Downloading : Finished')
        self.Status.state['disabled']
                
    def StatusArea(self):
        global BatchID
        Batch=sa.open(BatchID)
        Batch_Tracker=Batch.worksheet("Batch tracker")   
        Data=Batch_Tracker.get(f'A2:G{self.LastRowID(Batch_Tracker,1)}')
        UnlinkLists=list(filter(lambda x: x[4][:5]!="https",Data))
        AmazonList=list(filter(lambda x: x[4][:17]=='https://orderdesk',Data))
        DriveList=list(filter(lambda x: x[4][:13]=="https://drive",Data))
        ShopifyList=list(filter(lambda x: x[4][:19]=="https://cdn.shopify",Data))
        Dict={"Orders types":["Orders\nwithout link",
                              "Orders\nwith Amz\nlink",
                              "Orders\nwith Drive\nlink",
                              "Orders\nwith Shopify\nlink"],
              "Number of orders":[len(UnlinkLists),
                                  len(AmazonList),
                                  len(DriveList),
                                  len(ShopifyList)]}
        df= pd.DataFrame(Dict,columns=["Orders types","Number of orders"])
        colors=["Green","red","blue","purple"]
        plt.bar(df['Orders types'],df["Number of orders"],color=colors)
        plt.title("Orders types / Number of orders")
        plt.xlabel('Orders types')
        plt.ylabel('Number of ordrs')
        plt.grid(True)
        plt.show()
        
    def __init__(self,):
        global TextVariable
        super().__init__() #The super() function is used to give access to methods and properties of a parent or sibling class.
        #The super() function returns an object that represents the parent class.
        #configure the root window:
        self.Menubar=tk.Menu(self)
        self.filemenu=tk.Menu(self.Menubar,tearoff=0)
        
        self.filemenu.add_command(label="")
        
        
        self.title("Image Downloader")   
        self.iconbitmap(Logo)     
        
        TextVariable=tk.StringVar()        
        TextVariable.set('Download files')
        
        #Menu Bar:
        
        
        #Introductory:
        self.JPgLogo=ImageTk.PhotoImage(resize_my_img2)
        self.IntroLabel=ttk.Label(self, text="Image downloader:Done for batches", image=self.JPgLogo,compound=tk.BOTTOM
                                  ,foreground=fg_0366fc,font=Font_tuple6,justify='center')
        self.IntroLabel.pack()
        
        #Label Logo:
        self.LOGOImage=ImageTk.PhotoImage(resize_img)
        self.LogoImageLabel=ttk.Label(self,image=self.LOGOImage,justify='center')
        self.LogoImageLabel.pack()
        
        #button:
        self.frame=ttk.LabelFrame(self,text='',)
        self.frame.pack() 
        #Work inside frame:
        self.BatchEntry=ttk.Entry(self.frame,width=25,font=Font_tuple2)
        self.BatchEntry.grid(row=0,column=0,padx=10,pady=10,)
        self.BatchEntry.insert(0,"Enter the batch:...")
        
        
        self.SubmitImg=ImageTk.PhotoImage(resize_my_img3)
        self.submitBatch=ttk.Button(self.frame,text="Submit",image=self.SubmitImg,compound=tk.LEFT,command=self.BatchIDGetter)
        self.submitBatch.grid(row=0,column=1,padx=10)
        
        self.DeleteImg=ImageTk.PhotoImage(resize_my_img4)
        self.deleteBatch=ttk.Button(self.frame,text="Delete",image=self.DeleteImg,
                                    compound=tk.LEFT, command=self.BatchIDDeletter, state=DISABLED)
        self.deleteBatch.grid(row=0,column=2,)
        
        s=ttk.Style()
        s.configure('my.TButton',font=Font_tuple3)

        self.StatusImg=ImageTk.PhotoImage(resize_my_img5)

        self.Status=ttk.Button(self.frame,text=" Status situation",
                               style='my.TButton',state=DISABLED,image=self.StatusImg,compound=tk.LEFT,command=self.StatusArea)

        self.Status.grid(row=0,column=3,padx=60,ipadx=10,ipady=10)
        #Download button:
        s.configure('my1.TButton',font=Font_tuple4)
        self.Download_Icon=ImageTk.PhotoImage(resize_my_img1)
        
        self.DownloadButton=ttk.Button(self,textvariable=TextVariable,image=self.Download_Icon,compound=tk.LEFT,state=DISABLED,
                                       style='my1.TButton',command=self.BatchFileDownloader)
        self.DownloadButton.pack(pady=25,ipadx=10,ipady=10)
        

class ChartDrawer():
    def __init__(self,Country:list,Data:list) -> None:
        self.Country=Country
        self.Data=Data
    
    def Chart(self,Country,Data):
    
        plt.bar(Country,Data)
        plt.title('Country vs Data')
        plt.xlabel('Country')
        plt.ylabel('Data')
        plt.show()
        
    def Main(self):
        self.Chart(self.Country,self.Data)

Country=['USA','CANADA','Germany',
                 'UK','FRANCE']
Data=[45000,42000,52000,49000,47000]

    
if __name__=="__main__":    
    app=ImagesDownloaderApp()
    
    app.mainloop()



#Credits:
#{https://www.pythontutorial.net/tkinter/tkinter-object-oriented-window/
    #https://www.pythontutorial.net/tkinter/ttk-style/
    
#}


'''
Bug Reports:

When the client orders 2items the same dimensions:
PermissionError: [Errno 13] Permission denied:
'C:/Users/admin/Downloads/Python_Project/images\\113-8637738-9797040\\ClientInfo_AW2MN0.txt'
(FIXED)
'''