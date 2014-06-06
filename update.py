"""
  Function:  updateChEMBL 
  --------------------

Download and install the latest version of ChEMBL.

momo.sander@googlemail.com
"""                                                  

def updateChEMBL(RELEASE, OPT_FILE): 
  import os
  import sys
  

  # On Mac...
  #os.system("ftp ftp://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/releases/chembl_%s/chembl_%s_mysql.tar.gz" %(RELEASE, RELEASE)) 
  # On Linux...
  os.system("wget ftp://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/releases/chembl_%s/chembl_%s_mysql.tar.gz" %(RELEASE, RELEASE))
  os.system("tar -zxvf chembl_%s_mysql.tar.gz" % RELEASE)
  os.system("mysqladmin --defaults-extra-file=%s DROP IF EXISTS chembl_%s" %(OPT_FILE, RELEASE))    
  os.system("mysqladmin --defaults-extra-file=%s CREATE chembl_%s" %(OPT_FILE, RELEASE))    
  os.system("mysql --defaults-extra-file=%s chembl_%s < chembl_%s_mysql/chembl_%s.mysqldump.sql" % ( OPT_FILE, RELEASE, RELEASE, RELEASE))

                                  	                                                     
if __name__ == '__main__':
  import sys                                        
  import os
  if len(sys.argv) != 3:                  
    print "specify RELEASE, OPT_FILE"
    sys.exit()                                                                             
                                        
  RELEASE = str(sys.argv[1])
  OPT_FILE = str(sys.argv[2])

  updateChEMBL(RELEASE, OPT_FILE)

                                             
