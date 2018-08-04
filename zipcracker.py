"
ArkaFox 2018
Zip Password Cracker

Common script, but this is my try on it. Hope you like it.
arkafox@protonmail.com
"



import zipfile #Dealing with Zips
import optparse #Optparse (self-explanatory)
import threading #To create Threads (performance)
import time #Optional, information about time



def cracking(zip_file,password): #CrackingFunction

    try:
        zip_file.extractall(pwd=password) #Trys to extract the zip file with the argument password


        print("[+] Password found: %s" % password) #This line will only be executed if the pwd is correct, else it triggers exception
    except:
        pass #self-explanatory

    

def main(): #MainFunction

    start = time.time()  #start time


    #Optparse stuff

    parser = optparse.OptionParser("usage: python %s" % __file__ + ' -f <zipfile> -w <wordlist>')
    parser.add_option('-f', dest='zipfilename', type='string', help='specify zip file')
    parser.add_option('-w', dest='wordlist' , type='string' , help='specify dictionary file')

    (options, args) = parser.parse_args()
    if (options.zipfilename is None) | (options.wordlist is None):
        print(parser.usage)
        exit(0)

    else:

        wordlist = options.wordlist
        zipfilename = options.zipfilename

    

    zip_file = zipfile.ZipFile(zipfilename) #Creating a zip object

    wordlist_object = open(wordlist) #Creating the wordlist object

    for line in wordlist_object.readlines(): #reads lines in the wordlist

        password = line.strip('\n') #strips out the password, line by line

        t = Thread(cracking(zip_file,password)) #Creating a thread that calls the Cracking Function
        t.start() #Starts the Thread
        


    end = time.time() #End Time
    dif = (end - start) #Duration calculation
    print "Duration time: %r" % dif #Prints it

if __name__ == '__main__':
    main()
