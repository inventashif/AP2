#!/usr/bin/env python
import os
import sys
import threading
import subprocess

# Existing code...

def main():
    # Existing code...

    def getSubdomain(subData):
        # Existing code...

        try:
            # ... Existing code ...
            
            try:
                stdout_string = subprocess.check_output(['amass', '-version'], stderr=subprocess.STDOUT)
                print('\033[92m[-] Gathering Information...')
                time.sleep(2)
                
                print('\033[96m[-] Enumerating subdomains for ' + '\033[94m' + args.domain)
                with Spinner():
                    os.popen('amass enum -d ' + subData + ' -o amass_list.txt').read()

                print('\033[92m[-] Gathering Information...')
                time.sleep(2)
                
                print('\033[96m[-] Enumerating subdomains for ' + '\033[94m' + args.domain)
                with Spinner():
                    os.popen('knockpy ' + args.domain + ' -o knockpy_list.txt').read()
                    
                # ... Continue with existing code ...

            except subprocess.CalledProcessError as cpe:
                print('\033[96m[!] Amass or KnockPy not found\033[91m !!!\n\033[93m[-] Install them or use -f with subdomain.txt file.')
                sys.exit()

            except OSError as e:
                print('\033[96m[!] Amass or KnockPy not found\033[91m !!!\n\033[93m[-] Install them or use -f with subdomain.txt file.')
                sys.exit()

        except subprocess.CalledProcessError as cpe:
            print('\033[96m[!] Subfinder not found\033[91m !!!\n\033[93m[-] Install it or use -f with subdomain.txt file.')
            sys.exit()

        except OSError as e:
            print('\033[96m[!] Subfinder not found\033[91m !!!\n\033[93m[-] Install it or use -f with subdomain.txt file.')
            sys.exit()

        # ... Continue with existing code ...

    # ... Continue with existing code ...

if __name__ == "__main__":
    main()
