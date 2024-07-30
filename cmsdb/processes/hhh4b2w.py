"""
HHH -> bbbbww
"""

_all_ = [   
    #2022
    "hhh_bbbbww_c3_minus1p5_d4_minus0p5_22",
    "hhh_bbbbww_c3_minus1_d4_0_22",
    "hhh_bbbbww_c3_4_d4_9_22",
    "hhh_bbbbww_c3_1_d4_2_22",
    "hhh_bbbbww_c3_0_d4_minus1_22",
    #2023 - PRE
    "hhh_bbbbww_c3_19_d4_19",
    "hhh_bbbbww_c3_minus1p5_d4_minus0p5",
    "hhh_bbbbww_c3_1_d4_0",
    "hhh_bbbbww_c3_2_d4_minus1",
    "hhh_bbbbww_c3_0_d4_99",
    "hhh_bbbbww_c3_minus1_d4_0",
    "hhh_bbbbww_c3_1_d4_2",
    "hhh_bbbbww_c3_0_d4_0",
    #2023 - POST
    "hhh_bbbbww_c3_19_d4_19_post",
    "hhh_bbbbww_c3_minus1p5_d4_minus0p5_post",
    "hhh_bbbbww_c3_1_d4_0_post",
    "hhh_bbbbww_c3_2_d4_minus1_post",
    "hhh_bbbbww_c3_0_d4_minus1_post",
    "hhh_bbbbww_c3_0_d4_99_post",
    "hhh_bbbbww_c3_minus1_d4_0_post",
    "hhh_bbbbww_c3_minus1_d4_minus1_post",
    "hhh_bbbbww_c3_4_d4_9_post",
    "hhh_bbbbww_c3_1_d4_2_post",
]

from cmsdb.processes.hhh import (
    hhh,
    )
from scinum import Number

######################2022###############################################

hhh_bbbbww_c3_minus1p5_d4_minus0p5_22 = hhh.add_process(
    name="hhh_bbbbww_c3_minus1p5_d4_minus0p5_22", 
    id=200030,
    label=r"$HHH_{ggf}^{-1.5,-0.5} \rightarrow bbbbWW$",
    xsecs={13: Number(0.1), 13.6: Number(0.1)},  # TODO
)

hhh_bbbbww_c3_minus1_d4_0_22 = hhh.add_process(
    name="hhh_bbbbww_c3_minus1_d4_0_22", 
    id=200031,
    label=r"$HHH_{ggf}^{-1,0} \rightarrow bbbbWW$",
    xsecs={13: Number(0.1), 13.6: Number(0.1)},  # TODO
)

hhh_bbbbww_c3_4_d4_9_22 = hhh.add_process(
    name="hhh_bbbbww_c3_4_d4_9_22", 
    id=200032,
    label=r"$HHH_{ggf}^{4,9} \rightarrow bbbbWW$",
    xsecs={13: Number(0.1), 13.6: Number(0.1)},  # TODO
)

hhh_bbbbww_c3_1_d4_2_22 = hhh.add_process(
    name="hhh_bbbbww_c3_1_d4_2_22", 
    id=200033,
    label=r"$HHH_{ggf}^{1,2} \rightarrow bbbbWW$",
    xsecs={13: Number(0.1), 13.6: Number(0.1)},  # TODO
)

hhh_bbbbww_c3_0_d4_minus1_22 = hhh.add_process(
    name="hhh_bbbbww_c3_0_d4_minus1_22", 
    id=200034,
    label=r"$HHH_{ggf}^{0,-1} \rightarrow bbbbWW$",
    xsecs={13: Number(0.1), 13.6: Number(0.1)},  # TODO
)

################################PRE##########################################
hhh_bbbbww_c3_0_d4_0 = hhh.add_process(
    name="hhh_bbbbww_c3_0_d4_0", 
    id=200001,
    label=r"$HHH_{ggf}^{0,0} \rightarrow bbbbWW$",
    xsecs={13: Number(0.1), 13.6: Number(0.1)},  # TODO
)

hhh_bbbbww_c3_19_d4_19 = hhh.add_process(
    name="hhh_bbbbww_c3_19_d4_19", 
    id=200002,
    label=r"$HHH_{ggf}^{19,19} \rightarrow bbbbWW$",
    xsecs={13: Number(0.1), 13.6: Number(0.1)},  # TODO
)

hhh_bbbbww_c3_minus1p5_d4_minus0p5 = hhh.add_process(
    name="hhh_bbbbww_c3_minus1p5_d4_minus0p5", 
    id=200003,
    label=r"$HHH_{ggf}^{-1.5,-0.5} \rightarrow bbbbWW$",
    xsecs={13: Number(0.1), 13.6: Number(0.1)},  # TODO
)

hhh_bbbbww_c3_1_d4_0 = hhh.add_process(
    name="hhh_bbbbww_c3_1_d4_0", 
    id=200004,
    label=r"$HHH_{ggf}^{1,0} \rightarrow bbbbWW$",
    xsecs={13: Number(0.1), 13.6: Number(0.1)},  # TODO
)

hhh_bbbbww_c3_2_d4_minus1 = hhh.add_process(
    name="hhh_bbbbww_c3_2_d4_minus1", 
    id=200005,
    label=r"$HHH_{ggf}^{2,-1} \rightarrow bbbbWW$",
    xsecs={13: Number(0.1), 13.6: Number(0.1)},  # TODO
)

hhh_bbbbww_c3_0_d4_minus1 = hhh.add_process(
    name="hhh_bbbbww_c3_0_d4_minus1", 
    id=200019,
    label=r"$HHH_{ggf}^{0,-1} \rightarrow bbbbWW$",
    xsecs={13: Number(0.1), 13.6: Number(0.1)},  # TODO
)

hhh_bbbbww_c3_0_d4_99 = hhh.add_process(
    name="hhh_bbbbww_c3_0_d4_99", 
    id=200006,
    label=r"$HHH_{ggf}^{0,99} \rightarrow bbbbWW$",
    xsecs={13: Number(0.1), 13.6: Number(0.1)},  # TODO
)

hhh_bbbbww_c3_minus1_d4_0 = hhh.add_process(
    name="hhh_bbbbww_c3_minus1_d4_0", 
    id=200007,
    label=r"$HHH_{ggf}^{-1,0} \rightarrow bbbbWW$",
    xsecs={13: Number(0.1), 13.6: Number(0.1)},  # TODO
)

hhh_bbbbww_c3_1_d4_2 = hhh.add_process(
    name="hhh_bbbbww_c3_1_d4_2", 
    id=200008,
    label=r"$HHH_{ggf}^{1,2} \rightarrow bbbbWW$",
    xsecs={13: Number(0.1), 13.6: Number(0.1)},  # TODO
)

################################POST##########################################

hhh_bbbbww_c3_19_d4_19_post = hhh.add_process(
    name="hhh_bbbbww_c3_19_d4_19_post", 
    id=300009,
    label=r"$HHH_{ggf}^{19,19} \rightarrow bbbbWW$",
    xsecs={13: Number(0.1), 13.6: Number(0.1)},  # TODO
)

hhh_bbbbww_c3_minus1p5_d4_minus0p5_post = hhh.add_process(
    name="hhh_bbbbww_c3_minus1p5_d4_minus0p5_post", 
    id=300010,
    label=r"$HHH_{ggf}^{-1.5,-0.5} \rightarrow bbbbWW$",
    xsecs={13: Number(0.1), 13.6: Number(0.1)},  # TODO
)

hhh_bbbbww_c3_1_d4_0_post = hhh.add_process(
    name="hhh_bbbbww_c3_1_d4_0_post", 
    id=300011,
    label=r"$HHH_{ggf}^{1,0} \rightarrow bbbbWW$",
    xsecs={13: Number(0.1), 13.6: Number(0.1)},  # TODO
)

hhh_bbbbww_c3_2_d4_minus1_post = hhh.add_process(
    name="hhh_bbbbww_c3_2_d4_minus1_post", 
    id=300012,
    label=r"$HHH_{ggf}^{2,-1} \rightarrow bbbbWW$",
    xsecs={13: Number(0.1), 13.6: Number(0.1)},  # TODO
)

hhh_bbbww_c3_0_d4_minus1_post = hhh.add_process(
    name="hhh_bbbww_c3_0_d4_minus1_post", 
    id=300013,
    label=r"$HHH_{ggf}^{0,-1} \rightarrow bbbbWW$",
    xsecs={13: Number(0.1), 13.6: Number(0.1)},  # TODO
)

hhh_bbbbww_c3_0_d4_99_post = hhh.add_process(
    name="hhh_bbbbww_c3_0_d4_99_post", 
    id=300014,
    label=r"$HHH_{ggf}^{0,99} \rightarrow bbbbWW$",
    xsecs={13: Number(0.1), 13.6: Number(0.1)},  # TODO
)

hhh_bbbbww_c3_minus1_d4_0_post = hhh.add_process(
    name="hhh_bbbbww_c3_minus1_d4_0_post", 
    id=300015,
    label=r"$HHH_{ggf}^{1,0} \rightarrow bbbbWW$",
    xsecs={13: Number(0.1), 13.6: Number(0.1)},  # TODO
)

hhh_bbbbww_c3_minus1_d4_minus1_post = hhh.add_process(
    name="hhh_bbbbww_c3_minus1_d4_minus1_post", 
    id=300016,
    label=r"$HHH_{ggf}^{-1,-1} \rightarrow bbbbWW$",
    xsecs={13: Number(0.1), 13.6: Number(0.1)},  # TODO
)

hhh_bbbbww_c3_4_d4_9_post = hhh.add_process(
    name="hhh_bbbbww_c3_4_d4_9_post", 
    id=300017,
    label=r"$HHH_{ggf}^{4,9} \rightarrow bbbbWW$",
    xsecs={13: Number(0.1), 13.6: Number(0.1)},  # TODO
)

hhh_bbbbww_c3_1_d4_2_post = hhh.add_process(
    name="hhh_bbbbww_c3_1_d4_2_post", 
    id=300018,
    label=r"$HHH_{ggf}^{1,2} \rightarrow bbbbWW$",
    xsecs={13: Number(0.1), 13.6: Number(0.1)},  # TODO
)
