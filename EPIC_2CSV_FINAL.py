import csv
import os
import glob

# Script is designed to look into specified directory for patient txt files and generate csv files from the data

#path = os.path.normpath("U:/IT-Projects/IntegrisEpic/") # use normpath to be compatible with running the script on any OS
#filelist = os.listdir("U:/IT-Projects/IntegrisEpic/")
#path = os.path.normpath("/baylorbynum@gmail.com/Integris_EPIC/Project_Folder")
#filelist = os.listdir("/home/player/baylorbynum@gmail.com/Integris_EPIC/Project_Folder")
path = os.path.normpath("/raie/Data")
filelist = os.listdir("/raie/Data")


Loc = ['BMC', 'EDM', 'ICI', 'LKS', 'YKN']

fieldnames = ['facility ID', 'Hospital Account', 'Patient Class',
                  'IP Admission Date', 'Discharge Date', 'Patient Date of Death',
                  'Patient Last Name', 'Patient First Name', 'Patient Middle Initial',
                  'Patient SSN', 'Patient Date of Birth', 'Patient Gender', 'Patient Marital Status',
                  'Patient MRN', 'Patient Address: Street Line 1', 'Patient Address: Street Line 2',
                  'Patient Address: City', 'Patient Address: State', 'Patient Address: ZIP',
                  'Patient Home Phone', 'Patient Business Phone','Patient Email', 'Patient Employer Name',
                  'Patient Employer Address: Line 1', 'Patient Employer Address: Line 2',
                  'Patient Employer Address: City', 'Patient Employer Address: State',
                  'Patient Employer Address: ZIP', 'Patient Emergency Contact Name',
                  'Patient Emergency Contact Phone Numbers', 'Attending Provider Name',
                  'Attending Provider ID', 'Authorizing Provider Name', 'Authorizing Provider ID',
                  'Ordering Physician Name', 'Ordering Physician ID', 'Referring Physician Name',
                  'Referring Physician ID', 'Patient PCP Name', 'Patient PCP ID', 'Diagnosis #1 Code',
                  'Diagnosis #1 Description', 'Diagnosis #2 Code', 'Diagnosis #2 Description',
                  'Diagnosis #3 Code', 'Diagnosis #3 Description', 'Diagnosis #4 Code',
                  'Diagnosis #4 Description', 'Diagnosis #5 Code', 'Diagnosis #5 Description',
                  'Diagnosis #6 Code', 'Diagnosis #6 Description', 'Diagnosis #7 Code',
                  'Diagnosis #7 Description', 'Diagnosis #8 Code', 'Diagnosis #8 Description',
		  'Admitting Diagnosis #1', 'admitting Diagnosis #2', 'Admitting Diagnosis #3', 'Admitting Diagnosis #4', 'Admitting Diagnosis #5',
                  'Accident Type', 'Accident Date', 'End Exam Time', 'Service Area', 'Accession Number',
                  'Procedure Name', 'Reason for Exam', 'Ordering Comments', 'Clinical Indications',
                  'Clinical Indications Comments', 'Procedure Code', 'Procedure CPT Code', 'CPT Code Modifier #1',
                  'CPT Code Modifier #2', 'CPT Code Modifier #3', 'CPT Code Modifier #4', 'Research Study Codes',
                  'Radiologist Names', 'Signing Physicians', 'Signing Dates(s)', 'Signing Time',
                  'Guarantor First Name', 'Guarantor Last Name', 'Guarantor Address: Line 1', 'Guarantor Address: Line 2',
                  'Guarantor Address: City', 'Guarantor Address: State', 'Guarantor Address: Zip', 'Guarantor Home Phone',
                  'Guarantor Work Phone', 'Guarantor SSN', 'Guarantor Relationship to Patient', 'Guarantor Employer Name',
                  'Guarantor Employer Address: Line 1', 'Guarantor Employer Address: Line 2', 'Guarantor Employer Address: City',
                  'Guarantor Employer Address: State', 'Guarantor Employer Address: ZIP', 'Guarantor Employer Phone',
                  'Insurance Subscriber Employer', 'Insurance #1 Subscriber Name', 'Insurance #1 Subscriber Date of Birth',
                  'Insurance #1 Subscriber Gender', 'Insurance #1 Subscriber Address: Line 1', 'Insurance #1 Subscriber Address: Line 2',
                  'Insurance #1 Subscriber Address: City', 'Insurance #1 Subscriber Address: State', 'Insurance #1 Subscriber Address: ZIP',
                  'Insurance #1 Subscriber Phone', 'Insurance #1 Company Name', 'Insurance #1 Company Group Name',
                  'Insurance #1 Company Group Number', 'Insurance #1 Company Address: Line 1', 'Insurance #1 Company Address: Line 2',
                  'Insurance #1 Company Address: City', 'Insurance #1 Company Address: State', 'Insurance #1 Company Address: ZIP',
                  'Insurance #1 Company Phone', 'Insurance #1 Plan', 'Insurance #1 Policy Number', 'Insurance #1 Payor ID',
                  'Insurance #1 Patient Relationship to Subscriber', 'Insurance #2 Subscriber Name', 'Insurance #2 Subscriber Date of Birth',
                  'Insurance #2 Subscriber Gender', 'Insurance #2 Subscriber Address: Line 1', 'Insurance #2 Subscriber Address: Line 2',
                  'Insurance #2 Subscriber Address: City', 'Insurance #2 Subscriber Address: State', 'Insurance #2 Subscriber Address: ZIP',
                  'Insurance #2 Subscriber Phone', 'Insurance #2 Company Name', 'Insurance #2 Company Group Name',
                  'Insurance #2 Company Group Number', 'Insurance #2 Company Address: Line 1', 'Insurance #2 Company Address: Line 2',
                  'Insurance #2 Company Address: City', 'Insurance #2 Company Address: State', 'Insurance #2 Company Address: ZIP',
                  'Insurance #2 Company Phone', 'Insurance #2 Plan', 'Insurance #2 Policy Number', 'Insurance #2 Payor ID',
                  'Insurance #2 Patient Relationship to Subscriber', 'Insurance #3 Subscriber Name', 'Insurance #3 Subscriber Date of Birth',
                  'Insurance #3 Subscriber Gender', 'Insurance #3 Subscriber Address: Line 1', 'Insurance #3 Subscriber Address: Line 2',
                  'Insurance #3 Subscriber Address: City', 'Insurance #3 Subscriber Address: State', 'Insurance #3 Subscriber Address: ZIP',
                  'Insurance #3 Subscriber Phone', 'Insurance #3 Company Name', 'Insurance #3 Company Group Name',
                  'Insurance #3 Company Group Number', 'Insurance #3 Company Address: Line 1', 'Insurance #3 Company Address: Line 2',
                  'Insurance #3 Company Address: City', 'Insurance #3 Company Address: State', 'Insurance #3 Company Address: ZIP',
                  'Insurance #3 Company Phone', 'Insurance #3 Plan', 'Insurance #3 Policy Number', 'Insurance #3 Payor ID',
                  'Insurance #3 Patient Relationship to Subscriber', 'Narrative', 'Impression', 'Addemdum Text', 'Charge Guarantor']

''' open files and assign to an output with same filenamne in csv format with assigned field names for headers.
    Checks for filenames contain Loc names and iterates over those files. '''
for file in filelist: 
    if any(x in file for x in Loc): # Check if filenames contains 'Loc' names, this is to prevent it from outputing a none patient file in the directory
        infilename = file 
        output_filename = os.path.basename(str(infilename)) # strip string to get the filename
        outfilename = "{:.14}.csv".format(output_filename) # truncate filename to remove .txt and add .csv
            
        with open(outfilename, 'w') as outfile, open(infilename, 'r') as infile:
            patient_data = csv.reader(infile, delimiter='|')
            csv_file = csv.writer(outfile)
    
            csv_file.writerow(fieldnames) # write headers to output file

            for row in patient_data: # write patient data to output file
                # print(row)
                csv_file.writerow(row)
    
