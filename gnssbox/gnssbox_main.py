import sys
import os

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

# 通过站点文件绘制地图
from plot import plotSite

plotSite.plotSite(file=r"D:\Code\gnssbox\gnssbox\plot\site.info")

# 通过站点信息绘制站点图
# site = {'JOZE': {'L': 21.03139, 'B': 52.09722},
#         'TIXI': {'L': 128.86639, 'B': 71.63444},
#         'IISC': {'L': 77.57028, 'B': 13.02111}}
# plotSite.plotSite(site=site)

# 指定绘制范围
# site = {'JOZE': {'L': 21.03139, 'B': 52.09722},
#         'TIXI': {'L': 128.86639, 'B': 71.63444},
#         'IISC': {'L': 77.57028, 'B': 13.02111}}
# plotSite.plotSite(site=site, L=[0, 270], B=[-60, 60])
