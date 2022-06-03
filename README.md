# WormGearLHAPDF

* To generate the LHAPDF files, use the command ```./genlhapdf -d results```
* The resulting files will be stored in ```results/data``` (they have already been generated)
* Note that index 0000 contains the mean value of the replicas.  Indices 0001 and above are the replicas.
* Use ```./plot.py``` to load the LHAPDF files and generate the three plots below
* The resulting plots will be stored in ```results/gallery``` (they have already been generated)
* To learn how to load and use the distributions and widths, look at the functions within ```plot.py```





Recreated plots from [JAM22][JAM22]:

Transversity PDFs:
![plot](./results/gallery/lhapdf-transversity-Q2=4.00000-bands.png)

Collins pion function (first moment):
![plot](./results/gallery/lhapdf-collinspi-Q2=4.00000-bands.png)

Widths for Collins pion function:
![plot](./results/gallery/lhapdf-collinspi-widths.png)


[JAM22]: https://arxiv.org/abs/2205.00999


