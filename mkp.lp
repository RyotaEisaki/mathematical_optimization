\ Model mkp
\ LP format - for model browsing. Use MPS format to capture full model detail.
Maximize
  16 x(1) + 19 x(2) + 23 x(3) + 28 x(4)
Subject To
 R0: 2 x(1) + 3 x(2) + 4 x(3) + 5 x(4) <= 7
 R1: 3000 x(1) + 3500 x(2) + 5100 x(3) + 7200 x(4) <= 10000
Bounds
Binaries
 x(1) x(2) x(3) x(4)
End
