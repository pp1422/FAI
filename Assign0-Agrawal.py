
import sys

# open input file for reading 
def openInputFile(inputfile):
    try:
        #try to open the file
        myfile =  open(inputfile, "r");
        return myfile;
    #print error if the file cannot be opened
    except IOError:
        print "file invalid"
        sys.exit()

#validate command line arguments 
def validateCommandInput():
    #check if input filename is given as command line argument
    if len(sys.argv) == 2:
        return True  
    #return False if filename is not given as command 
    #line argument   
    else:
        return False

def parseFile(myfile):
    #Create a dictionary to store all userids and their login counts
    login_info = {}

    #parse the file to find out all users of the game the 
    #number of times each user logged in
    for line in myfile:
        #seperate event id, login date and user id fields
        event_id,login_date,userid = line.split()
        #if user id login info is already captured then just
        #increment the login counts by 1 else add userid to
        #login info dictionary
        if userid in login_info:
            login_info[userid] += 1
        else:
            login_info[userid] = 1
            
    return login_info

#print summary of user login for each user
def printSummary(login_info):
    print "Game User login summary"
    print "UserId : Login Times"
    #print user id and count of login times
    for key in login_info:
        print key,"\t",login_info[key]
    
#calculate average number of times users logged in     
def calcAvg(login_info):
    #calculate total login times of all users 
    total_login_times = len(login_info)
       
    #check if there is atleast single login   
    if total_login_times!=0:
        #calculate average logins of all users
        avg = sum(login_info.values())/float(total_login_times)
        #print the average rounded to 2 digits
        print "average login time of users " , round(avg,4)
    else:
        print "average = ", 0 
        
#main method         
def main(arg):
    #if input file name is given then calculate average
    if validateCommandInput() is True:
        #open input file
        login_file = openInputFile(sys.argv[1])
        #parse input file
        login_dict = parseFile(login_file)
        #print summary of login details
        printSummary(login_dict)
        #calculate average of login of each user
        calcAvg(login_dict)
        return
     
#execute main function     
main(sys.argv)   