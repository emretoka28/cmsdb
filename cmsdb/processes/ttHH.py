
_all_ = [   

   "ttHH"

]

from cmsdb.processes.hh import (
    hh_ggf,
    )
from scinum import Number

################################PRE##########################################
ttHH = hh_ggf.add_process(
    name="ttHH", 
    id=400001,
    label=r"$t\bar{t}HH$",
    xsecs={13: Number(0.1), 13.6: Number(0.001 * 0.860)}   # xsec from: https://twiki.cern.ch/twiki/bin/view/LHCPhysics/LHCHWGHH#tthh
)