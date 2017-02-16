import csv, os
#import sys
import time
from datetime import datetime 
#import io

path = os.path.normpath("/baylorbynum@gmail.com/Integris_EPIC/Project_Folder")
filelist = os.listdir("/home/player/baylorbynum@gmail.com/Integris_EPIC/Project_Folder")
#path = os.path.normpath("U:/IT-Projects/IntegrisEpic/")
#filelist = os.listdir("U:/IT-Projects/IntegrisEpic/")

Today = datetime.today().strftime("%Y-%m-%d-%H-%M-%S-%j")
DemoDT = datetime.today().strftime("%m%d%y")
ChgDT = datetime.today().strftime("%Y%m%d%H%M%S%j")

Loc = {'BMC': 'CBCO',
       'EDM': 'ED',
       'ICI': '',
       'LKS':'',
       'YKN':''}


DemoAbbrv = {'YKN':'YKRadAssoc',\
              'BMC':'BARadAssoc',\
              'ICI':'ICRadAssoc',\
              'LKS':'LWRadAssoc',\
              'EDM':'EDRadAssoc'}\
DiagAbbrv = {'YKN':'YKRadAssocCodes',\
              'BMC':'BARadAssocCodes',\
              'ICI':'ICRadAssocCodes',\
              'LKS':'LWRadAssocCodes',\
              'EDM':'EDRadAssocCodes'}
ORUAbbrv  = {'YKN':'YKN_RADASSOC',\
             'BMC':'BMC_RADASSOC',\
             'ICI':'CAN_RADASSOC',\
             'LKS':'LAK_RADASSOC',\
             'EDM':'EDM_RADASSOC'}
ChgAbbrv  = {'YKN':'intr03',\
             'BMC':'intr12',\
             'ICI':'intr17',\
             'EDM':'intr18',\
             'LKS':'intr19'}

for file in filelist:
        if file.endswith(".csv"):
                infilename = file
                print(infilename)
                output_filename = os.path.basename(str(infilename))
                fileDt = output_filename[11:14]
                ORUfilename = '{}{}.dat'.format(ORUAbbrv[fileDt], Today)
                DEMOfilename = '{}{}.txt'.format(DemoAbbrv[fileDt], DemoDT)
                DIAGfilename = '{}{}.txt'.format(DiagAbbrv[fileDt], DemoDT)
                CHGfilename = '{}{}.dat'.format(ChgAbbrv[fileDt], ChgDT)
                #print(ORUfilename)
                
                reader = csv.reader(open(infilename, 'r'), delimiter = '|')                     
                header_row = next(reader) # Get the top row
                remove_empty = next(reader) # discovered a empty row following the header
                #print(header_row)
                
                for row in reader:
                        item = row
                        data = item[0].split(',')
                        #print(data)
                        with open(ORUfilename, 'a') as outfile1:
                                #[13,6,7,8,10,11,14,16,17,18,19,29,37,63,9,36,60,66,67,72,78,78,79,80]
                                ORU_DOB = datetime.strptime(data[10], "%m/%d/%Y").strftime("%Y%m%d")
                                ORU_EXAMDT = datetime.strptime(data[3], "%m/%d/%Y").strftime("%Y%m%d")
                                ORU_DISCHARGE = datetime.strptime(data[4], "%m/%d/%Y").strftime("Y%m%d")
                                msh = 'MSH|^~\&|SMS|{}|MISYS|{}|20160324000200||ORU^R01|Q1511869790T2335379851||2.3||||||8859/1\r\n'.format(fileDt, fileDt)
                                pid = 'data|1|{13}|{13}||{6}^{7}^{8}||{DOB}|{11}|||W|{14}^^{16}^{17}^{18}^^^^000|000|{19}||ENG|M|NON|{60}^^^CD:000000000^^CD:000000000|{9}|||CD:000000000||0\r\n'.format(*data, DOB=ORU_DOB)
                                pv1 = 'PV1|1||num^ERTR^^num^^^num||||{34}^{37}^^^^^{fileDt}|{37}^{38}^^^^^{fileDt}||||||||||||||||||||||||||||||||||||{ORU_EXAMDT}|{ORU_DISCHARGE}000000\r\n'.format(*data, fileDt=fileDt, ORU_DISCHARGE=ORU_DISCHARGE, ORU_EXAMDT=ORU_EXAMDT) # BAPTIST EXAMLOC AND FACLOC PV1 PID[3] "Known_issues.txt"
                                orc = 'ORC|1||\r\n'
                                obr = 'OBR|1|||{72}^{66}||||{ORU_EXAMDT}000000|||||||||||||||||||||||{67}|00000^{78}|00000^{78} PHYSICIAN|Signed: {80} {81}||{ORU_EXAMDT}00000\r\n'.format(*data, ORU_EXAMDT=ORU_EXAMDT)# guessing which Radphy goes
                                obx = 'OBX|1||||{55}|||||||||{62}||{78}\r\n'.format(*data) # missing dictation location, serveDtTm?, guessing what Radphy goes here
                                nte = 'NTE|1|signature|{80}\n'.format(*data) # missing Signature Type, missing signature
                                outfile1.write(msh + pid + pv1 + orc + obr + obx + nte) 
                                
                        with open(CHGfilename, 'a') as outfile2: # data is written out with a header followed by rows pipe deliminated
                                #[6,7,13,34,35,66,67,72,78]
                                CHG_DOB = datetime.strptime(data[10], "%m/%d/%Y").strftime("%m%d%Y")
                                CHG_EXAM = datetime.strptime(data[3], "%m/%d/%Y").strftime("%m%d%Y")
                                #chg_header = 'RXX_PT_RXX_DT|RXX_PT_LNAME |RXX_PT_FNAME|RXX_PT_BDATE|RXX_MRN_NBR |RXX_FIN_NBR|RXX_PT_ENCNTR_TYPE|RXX_EXAM_DT|RXX_EXAM_TM|RXX_CPT|RXX_CHARGE_DESC|RXX_DOC_NBR|RXX_DOC_NAME|RXX_RAD_DOC_NAME|RXX_SERVICE_DT|RXX_SERVICE_TM|RXX_EXAM_REASON|RXX_SUB_BDATE|RXX_SEC_SUB_BDATE|'
                                chg = '{CHG_EXAM}|{6}|{7}|{CHG_DOB}|{13}|||{CHG_EXAM}||{72}|{66}|{35}|{34}|{78}|{CHG_EXAM}||{67}|'.format(*data, CHG_DOB=CHG_DOB, CHG_EXAM=CHG_EXAM) #FIN NBR, Doc ID, and guessing what is the Physician vs RAD_Physician
                                outfile2.write(chg)

                        with open(DEMOfilename, 'a') as outfile3:
                                
                                outfile3.write(' '+data[60]+' '*12+data[13]+' '*21+data[10]+' '*5+data[11]+data[9]+' '*202+data[6]+' '*35+data[7]+' '*25+data[14]+' '*70+data[16]
											  +' '*37+data[15]+' '*2+data[18]+' '*10+data[19]+' '*44+data[12])
'''
                                outfile3.seek(509) #guarLstNm
                                outfile3.write(data[])
                                
                                guarFstNm = outfile3.seek(544)

                                guarAddr1 = outfile3.seek(569)
                                guarCity  = outfile3.seek(639)
                                guarSt    = outfile3.seek(679)
                                guarZip   = outfile3.seek(671)
                                guarPh    = outfile3.seek(681)+outfile3.seek(689)
                                guarSS    = outfile3.seek(697)
                                guarRel   = outfile3.seek(707)
                                patEmplrLstNm = outfile3.seek(897)
                                patEmplrFstNm = outfile3.seek(932)
                                patEmplrAddr1 = outfile3.seek(957)
                                patEmplrCity = outfile3.seek(1027)
                                patEmplrSt = outfile3.seek(1057)
                                patEmplrZip = outfile3.seek(1059)
                                patEmplrPh  = outfile3.seek(1069)+outfile3.seek(1078)

                                ins1Cd        = outfile3.seek(60)
                                ins1Nm        = outfile3.seek(1089)
                                ins1Addr1     = outfile3.seek(1109)

                                ins1City      = outfile3.seek(1129)
                                ins1St        = outfile3.seek(1141)
                                ins1Zip       = outfile3.seek(1143)
                                ins1Ph        = outfile3.seek(1149)

                                ins1Pol       = outfile3.seek(64)
                                ins1Grp       = outfile3.seek(75)
                                ins1Auth      = outfile3.seek(2402)
                                priInsurLstNm = outfile3.seek(1502)
                                priInsurFstNm = outfile3.seek(1537)
                                priInsurAddr1 = outfile3.seek(1562)
                                priInsurCity  = outfile3.seek(1632)

                                priInsurSt    = outfile3.seek(1672)
                                priInsurZip   = outfile3.seek(1674)
                                priInsurPh    = outfile3.seek(1674)+outfile3.seek(1682)

                                priInsurRel   = outfile3.seek(1690)

                                priInsurGrpId  = outfile3.seek(98)
                                ins2Cd        = outfile3.seek(118)
                                ins2Nm        = outfile3.seek(1173)
                                ins2Addr1     = outfile3.seek(1193)

                                ins2City      = outfile3.seek(1213)
                                ins2St        = outfile3.seek(1225)
                                ins2Zip       = outfile3.seek(1228)
                                ins2Ph        = outfile3.seek(1233)

                                ins2Pol       = outfile3.seek(122)
                                ins2Grp       = outfile3.seek(133)
                                ins2Auth      = outfile3.seek(2417)
                                secInsurLstNm = outfile3.seek(1857)
                                secInsurFstNm = outfile3.seek(1892)
                                secInsurAddr1 = outfile3.seek(1917)
                                secInsurCity  = outfile3.seek(1987)
                                secInsurSt    = outfile3.seek(2017)
                                secInsurZip   = outfile3.seek(2019)
                                secInsurPh    = outfile3.seek(2029)+outfile3.seek(2037)

                                secInsurRel   = outfile3.seek(2045)

                                secInsurGrpId  = outfile3.seek(156)
                                ins3Cd        = outfile3.seek(176)
                                ins3Nm        = outfile3.seek(1257)
                                ins3Addr1     = outfile3.seek(1278)

                                ins3City      = outfile3.seek(1297)
                                ins3St        = outfile3.seek(1379)
                                ins3Zip       = outfile3.seek(1312)
                                ins3Ph        = outfile3.seek(1317)

                                ins3Pol       = outfile3.seek(180)
                                ins3Grp       = outfile3.seek(191)
                                ins3Auth      = outfile3.seek(2432)
                                terInsurLstNm = outfile3.seek(2212)
                                terInsurFstNm = outfile3.seek(2247)
                                terInsurAddr1 = outfile3.seek(2272)
                                terInsurCity  = outfile3.seek(2342)

                                terInsurSt    = outfile3.seek(2372)
                                terInsurZip   = outfile3.seek(2374)
                                terInsurPh    = outfile3.seek(2384)+outfile3.seek(2392)


                                terInsurRel   = outfile3.seek(2400)

                                terInsurGrpId  = outfile3.seek(214)'''
                                
                reader.close()  
