import math
from gnssbox.coordTran.xyz2blh import xyz2blh
from gnssbox.coordTran.blh2xyz import blh2xyz
# ABMF00GLP,2919786.0,-5383745.0,1774604.0,16.262,-61.528,-25.268
system = 'GRS80'
B,L,H = xyz2blh(-2888689.57218007,5199422.89566654,-2295975.49046198, system)
print(math.degrees(B),math.degrees(L),H)

X,Y,Z = blh2xyz(B,L,H,system)
print(X,Y,Z)