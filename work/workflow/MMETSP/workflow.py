#Have a bunch of files representing the reference transcriptomes -> proteins from MMETSP
#Want to ready the MMETSPinfo.csv finding out which files have an associated taxonomy 
#Read MMETSPinfo.csv


#If they have an associated taxonomy do not delete them 
    #make every line starting with > just be the organism name
#else delete them

#now that all remains is a bunch of files with the organism name as the fasta headers

#run hmmsearch and return the best result from each organism

#concatenate these hits into one big fasta file

#run the normal workflow for generating a trimmed alignment 

#run iqtree returning tree

#add names from MMETSP and their taxa numbers to the newick file


#alter names to their ids 

