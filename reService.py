#!/usr/bin/python
#
#   File_name: reService.py
#   Writen_by: salim aka BLaCK_Assassin
#   
#   Date: Sat 11/28/2015
#
#
#
#
#
#

# Importing nessury modules
# os: for interacting with system command you can use subprocess
import os
# optparse: for parsing commandline args
import optparse
# time: for delaying after restarting service
import time
import sys



# main service restarting function
def service_restart(delay):
    # loop
    while True:
        # trying to handle Exceptions
        try:
            # trying to handle keyboardInterrupt
            try:
                # printing..
                os.system("echo \033[32m[ * ] Restarting service... ")
                # restarting the service
                os.system("/etc/init.d/networking restart")
		os.system("/etc/init.d/network-manager status")
		os.system("/etc/init.d/network-manager restart")
                # printing...
                print "[ * ] Done. :)"
                # printing...
                print "sleeping..."
                # delay
                time.sleep(int(delay))
            # handling keyboardInterrupt
            except KeyboardInterrupt:
                # printing...
                print "[ - ] Exiting... bye! :)"
                # exiting...
                exit(1)
        # handling Exceptions
        except Exception, e:
            # printing...
            print "Error: %s" % str(e)



def calc():
    min_var = input("Enter min to convert into second: ")
    print "min: %s sec: %s" % (str(min_var), str(min_var * 60)) 





# main function
def main():
    try:
        if sys.argv[1] == "--calc":
            calc()
            exit(1)
    except IndexError:
        print ""
    # Creating parser object
    parser = optparse.OptionParser("Usage:-\n\t\t-s, --sleep  -  Time delay before service_restart - time is in second\n\t\tExample: 10 means 10-second calculate in minute or hour\n\n\t\t--calc minute to second calculator\n\nExample: python reService.py -t 180 <= restart and wait for 3 min\n\t python reService.py --calc <= calculator")
    # adding option
    parser.add_option("-s", "--sleep", dest="time", help="Delay")
    # parsing args
    (options,args) = parser.parse_args()
    # checking if "time" is null
    if (options.time == None):
        # printing...
        print parser.usage
    else:
        # t var with commandline time var
        t = options.time
        # calling service_restart function with the delay args
        service_restart(int(t))




# runnging even in import mode
if __name__ == "__main__":
    # executing main function
    main()
    os.system("echo \033[32mCreated_By:- \033[31mBLaCK_Assassin")
        
