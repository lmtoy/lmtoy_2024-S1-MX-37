# 2024-S1-MX-37

this SEQ project in intermediate bands suffered from a lot of birdies. Each main birdie has two satellites, 
so the list was:

	birdies=2176,2258,2261,2264,2433,2471,2474,2477,2643,2646,2649,2687,2856,2859,2862

See the *.birdies.tab files (and bstats for the channel based stats)

PI is interested in several lines, but spread out over the band, and the actual restfreq is
none of the lines.

restfreq=87.88,95.936

87.848    NH2CHO    4(1,3)-3(1,2)
87.925    HNCO      5-4                  strong detection   (fake vlsr=74)

95.91431  CH3OH     2(1,2)-1(1,1)
95.947    CH3CHO    5(0,5)-4(0,4)-E
95.963    CH3CHO    5(0,5)-4(0,4)-A
95.967    (CH3)2CO  17(17,0)-17(16,1)EE

With dv=200 and dw-200 we get all the lines in the center window. It is possible with pick a very small
dv,dw and focus on each line, with a higher order baseline subtraction that signal shows up better. We
did not persue this route here.



Related:
2018-S1-MU-45  restfreq=95.955
2021-S1-MX-14  restfreq=87.848 


## SB0 and SB1

To investigate the bad/wavy beams, several obsnums were taken with restfreq=87.88 in both banks (sourcename SB0)
and restfreq=95.936 (sourcename SB1)

