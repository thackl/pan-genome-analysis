import numpy as np, gzip, cPickle
from collections import defaultdict
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord  

def times(start): 
    import time
    t = int(time.time()-start)
    time_record=' %d minutes %d seconds (%d s)'%(t/60, t%60, t)
    return time_record

def read_fasta(filename):
    fa_dt={}
    for record in SeqIO.parse(filename, "fasta"):
        fa_dt[record.id]=str(record.seq)
    return fa_dt

def gbk_seq(each_gb_path, gbk_name):  
    # get sequence from gbk file
    gb = each_gb_path + gbk_name
    genome = SeqIO.read(gb,'genbank')
    allseq = genome.seq
    return allseq
    
def write_in_fa(write_file,Id, seq):
    #write_file=open(filename, 'wb');
    sequences = SeqRecord(Seq(seq), Id)
    SeqIO.write(sequences, write_file, "fasta")
    #write_file.close()

def load_pickle(filename):
    f = open(filename,"rb")
    p = cPickle.load(f)
    f.close()
    return(p)

def write_pickle(filename, data_out):
    write_file=open(filename, 'wb')
    cPickle.dump(data_out,write_file,protocol=2)
    write_file.close()

def write_json(data, file_name, indent=1):
    import json
    try:
        handle = open(file_name, 'w')
    except IOError:
        pass
    else:
        json.dump(data, handle, indent=indent)
        handle.close()

def check_exe(program):
    # Based on http://stackoverflow.com/questions/377017/test-if-executable-exists-in-python
    import os
    def is_exe(fpath):
        return os.path.isfile(fpath) and os.access(fpath, os.X_OK)

    fpath, fname = os.path.split(program)
    if fpath:
        if is_exe(program):
            print program + ' .. ok'
            return(program)
    else:
        for path in os.environ["PATH"].split(os.pathsep):
            path = path.strip('"')
            exe_file = os.path.join(path, program)
            if is_exe(exe_file):
                print program + ' .. ok [' +  exe_file + ']'
                return(program)

                
    print program + ' .. failed - required in PATH'
    exit()
