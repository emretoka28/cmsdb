"""
HHH -> bbbbww
"""

_all_ = [   

    "hhh_bbbbww_c3_0_d4_0",
    "hhh_bbbbww_c3_0_d4_99",
    "hhh_bbbbww_c3_0_d4_m1",
    "hhh_bbbbww_c3_19_d4_19",
    "hhh_bbbbww_c3_1_d4_0",
    "hhh_bbbbww_c3_1_d4_2",
    "hhh_bbbbww_c3_2_d4_m1",
    "hhh_bbbbww_c3_4_d4_9",
    "hhh_bbbbww_c3_m1_d4_0",
    "hhh_bbbbww_c3_m1_d4_m1"


]

from cmsdb.processes.hhh import (
    hhh,
    )
from scinum import Number

################################PRE##########################################
hhh_bbbbww_c3_0_d4_0 = hhh.add_process(
    name="hhh_bbbbww_c3_0_d4_0", 
    id=200001,
    label=r"$HHH_{ggf}^{0,0} \rightarrow 4b2W$",
    xsecs={13: Number(0.1), 13.6: Number(0.001 * 0.099)}   #0.079 fb, default is pb
)

hhh_bbbbww_c3_0_d4_99 = hhh.add_process(
    name="hhh_bbbbww_c3_0_d4_99", 
    id=200002,
    label=r"$HHH_{ggf}^{0,99} \rightarrow 4b2W$",
    xsecs={13: Number(0.1), 13.6: Number(0.001 * 0.099)},  # TODO
)

hhh_bbbbww_c3_0_d4_m1 = hhh.add_process(
    name="hhh_bbbbww_c3_0_d4_m1", 
    id=200003,
    label=r"$HHH_{ggf}^{0,-1} \rightarrow 4b2W$",
    xsecs={13: Number(0.1), 13.6: Number(0.001 * 0.099)},  # TODO
)

hhh_bbbbww_c3_19_d4_19 = hhh.add_process(
    name="hhh_bbbbww_c3_19_d4_19", 
    id=200004,
    label=r"$HHH_{ggf}^{19,19} \rightarrow 4b2W$",
    xsecs={13: Number(0.1), 13.6: Number(0.001 * 0.099)},  # TODO
)

hhh_bbbbww_c3_1_d4_0 = hhh.add_process(
    name="hhh_bbbbww_c3_1_d4_0", 
    id=200005,
    label=r"$HHH_{ggf}^{1,0} \rightarrow 4b2W$",
    xsecs={13: Number(0.1), 13.6: Number(0.001 * 0.099)},  # TODO
)

hhh_bbbbww_c3_1_d4_2 = hhh.add_process(
    name="hhh_bbbbww_c3_1_d4_2", 
    id=200019,
    label=r"$HHH_{ggf}^{1,2} \rightarrow 4b2W$",
    xsecs={13: Number(0.1), 13.6: Number(0.001 * 0.099)},  # TODO
)

hhh_bbbbww_c3_2_d4_m1 = hhh.add_process(
    name="hhh_bbbbww_c3_2_d4_m1", 
    id=200006,
    label=r"$HHH_{ggf}^{2,-1} \rightarrow 4b2W$",
    xsecs={13: Number(0.1), 13.6: Number(0.001 * 0.099)},  # TODO
)

hhh_bbbbww_c3_4_d4_9 = hhh.add_process(
    name="hhh_bbbbww_c3_4_d4_9", 
    id=200007,
    label=r"$HHH_{ggf}^{4,9} \rightarrow 4b2W$",
    xsecs={13: Number(0.1), 13.6: Number(0.001 * 0.099)},  # TODO
)

hhh_bbbbww_c3_m1_d4_0 = hhh.add_process(
    name="hhh_bbbbww_c3_m1_d4_0", 
    id=200008,
    label=r"$HHH_{ggf}^{-1,0} \rightarrow 4b2W$",
    xsecs={13: Number(0.1), 13.6: Number(0.001 * 0.099)},  # TODO
)

hhh_bbbbww_c3_m1_d4_m1 = hhh.add_process(
    name="hhh_bbbbww_c3_m1_d4_m1", 
    id=200009,
    label=r"$HHH_{ggf}^{-1,-1} \rightarrow 4b2W$",
    xsecs={13: Number(0.1), 13.6: Number(0.001 * 0.099)},  # TODO
)

hhh_bbbbww_c3_m1p5_d4_m0p5 = hhh.add_process(
    name="hhh_bbbbww_c3_m1p5_d4_m0p5", 
    id=200010,
    label=r"$HHH_{ggf}^{-1.5,-0.5} \rightarrow 4b2W$",
    xsecs={13: Number(0.1), 13.6: Number(0.001 * 0.099)},  # TODO
)
