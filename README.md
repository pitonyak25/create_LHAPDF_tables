# create_LHAPDF_tables

* Copy the directory with the msr files that you want to convert into LHAPDF into this directory
* To generate the LHAPDF files, use the command ```./genlhapdf -d wdir -f function```
* The resulting files will be stored in ```wdir/data```
* The options for function are transversity, collinspi, Htildepi, and sivers
* Note that index 0000 contains the mean value of the replicas.  Indices 0001 and above are the replicas.
* Plots will be generated for the given function and will be stored in ```wdir/gallery```
* To learn how to load and use the distributions and widths, look at the functions within ```plot.py```







