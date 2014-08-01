"""
  Function:  updateChEMBL 
  --------------------

Download and install the latest version of ChEMBL.

momo.sander@googlemail.com
"""                                                  

def updateChEMBL(RELEASE, OPT_FILE): 
    import os
    from subprocess import (call, Popen, PIPE)
    
    # On Mac...
    #os.system("ftp ftp://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/releases/chembl_%s/chembl_%s_mysql.tar.gz" %(RELEASE, RELEASE)) 
    # On Linux...
    if not os.path.isfile("chembl_%s_mysql/chembl_%s.mysqldump.sql" % (RELEASE, RELEASE)):
        rt = call(["wget", "ftp://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/releases/chembl_%s/chembl_%s_mysql.tar.gz" %(RELEASE, RELEASE)], stdout=PIPE)
        print("Downloaded ChEMBL, return code is " + rt)
        rt = call(["tar", "-zxvf", "chembl_%s_mysql.tar.gz" % RELEASE])
    rt = call(["mysql", "--defaults-extra-file=%s"%OPT_FILE, "-e", "DROP DATABASE IF EXISTS chembl_%s" %RELEASE])    
    rt = call(["mysql", "--defaults-extra-file=%s"%OPT_FILE, "-e", "CREATE DATABASE chembl_%s"%RELEASE])    
    rt = call("mysql --defaults-extra-file=%s chembl_%s < chembl_%s_mysql/chembl_%s.mysqldump.sql" % (OPT_FILE, RELEASE, RELEASE, RELEASE), shell = True)

                                  	                                                     
if __name__ == '__main__':
  import sys                                        
  import os
  if len(sys.argv) != 3:                  
    print "specify RELEASE, OPT_FILE"
    sys.exit()                                                                             
                                        
  RELEASE = str(sys.argv[1])
  OPT_FILE = str(sys.argv[2])

  updateChEMBL(RELEASE, OPT_FILE)

                                             
