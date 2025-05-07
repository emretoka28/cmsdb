import cmsdb.processes as procs
from cmsdb.campaigns.run3_2022_preEE_nano_v12 import campaign_run3_2022_preEE_nano_v12 as cpn



############################RUN3-2022########################################################
cpn.add_dataset(
    name="hhh_bbbbww_c3_minus1p5_d4_minus0p5_22_amcatnlo",
    id=15006829,
    processes=[procs.hhh_bbbbww_c3_minus1p5_d4_minus0p5_22],
    keys=[
        "/HHHto4B2WtoLNu2Q_c3-minus1p5_d4-minus0p5_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=34,
    n_events=384631,
)

cpn.add_dataset(
    name="hhh_bbbbww_c3_minus1_d4_0_22_amcatnlo",
    id=15005268,
    processes=[procs.hhh_bbbbww_c3_minus1_d4_0_22],
    keys=[
        "/HHHto4B2WtoLNu2Q_c3-minus1_d4-0_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=18,
    n_events=395960,
)

cpn.add_dataset(
    name="hhh_bbbbww_c3_4_d4_9_22_amcatnlo",
    id=15005267,
    processes=[procs.hhh_bbbbww_c3_4_d4_9_22],
    keys=[
        "/HHHto4B2WtoLNu2Q_c3-4_d4-9_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=16,
    n_events=397306,
)

cpn.add_dataset(
    name="hhh_bbbbww_c3_1_d4_2_22_amcatnlo",
    id=15005238,
    processes=[procs.hhh_bbbbww_c3_1_d4_2_22],
    keys=[
        "/HHHto4B2WtoLNu2Q_c3-1_d4-2_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=16,
    n_events=396683,
)

cpn.add_dataset(
    name="hhh_bbbbww_c3_0_d4_minus1_22_amcatnlo",
    id=15006684,
    processes=[procs.hhh_bbbbww_c3_0_d4_minus1_22],
    keys=[
        "/HHHto4B2WtoLNu2Q_c3-0_d4-minus1_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22EENanoAODv11-126X_mcRun3_2022_realistic_postEE_v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=53,
    n_events=1378232,
)


# ############################RUN3-2023########################################################

cpn.add_dataset(
    name="hhh_bbbbww_c3_19_d4_19_amcatnlo",
    id=14967163,
    processes=[procs.hhh_bbbbww_c3_19_d4_19],
    keys=[
        "/HHHto4B2WtoLNu2Q_c3-19_d4-19_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=4,
    n_events=596995,
)

cpn.add_dataset(
    name="hhh_bbbbww_c3_minus1p5_d4_minus0p5_amcatnlo",
    id=14966427,
    processes=[procs.hhh_bbbbww_c3_minus1p5_d4_minus0p5],
    keys=[
        "/HHHto4B2WtoLNu2Q_c3-minus1p5_d4-minus0p5_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=25,
    n_events=597997,
)

cpn.add_dataset(
    name="hhh_bbbbww_c3_1_d4_0_amcatnlo",
    id=14969070,
    processes=[procs.hhh_bbbbww_c3_1_d4_0],
    keys=[
        "/HHHto4B2WtoLNu2Q_c3-1_d4-0_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=32,
    n_events=585997,
)

cpn.add_dataset(
    name="hhh_bbbbww_c3_2_d4_minus1_amcatnlo",
    id=14968936,
    processes=[procs.hhh_bbbbww_c3_2_d4_minus1],
    keys=[
        "/HHHto4B2WtoLNu2Q_c3-2_d4-minus1_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=26,
    n_events=587988,
)

cpn.add_dataset(
    name="hhh_bbbbww_c3_0_d4_minus1_amcatnlo",
    id=14968940,
    processes=[procs.hhh_bbbbww_c3_0_d4_minus1],
    keys=[
        "/HHHto4B2WtoLNu2Q_c3-0_d4-minus1_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=32,
    n_events=585990,
)

cpn.add_dataset(
    name="hhh_bbbbww_c3_0_d4_99_amcatnlo",
    id=14968341,
    processes=[procs.hhh_bbbbww_c3_0_d4_99],
    keys=[
        "/HHHto4B2WtoLNu2Q_c3-0_d4-99_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=15,
    n_events=593990,
)

cpn.add_dataset(
    name="hhh_bbbbww_c3_minus1_d4_0_amcatnlo",
    id=14968941,
    processes=[procs.hhh_bbbbww_c3_minus1_d4_0],
    keys=[
        "/HHHto4B2WtoLNu2Q_c3-minus1_d4-0_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=25,
    n_events=590993,
)

cpn.add_dataset(
    name="hhh_bbbbww_c3_1_d4_2_amcatnlo",
    id=14965770,
    processes=[procs.hhh_bbbbww_c3_1_d4_2],
    keys=[
        "/HHHto4B2WtoLNu2Q_c3-1_d4-2_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=29,
    n_events=595992,
)

cpn.add_dataset(
    name="hhh_bbbbww_c3_0_d4_0_amcatnlo",
    id=14968582,
    processes=[procs.hhh_bbbbww_c3_0_d4_0],
    keys=[
        "/HHHto4B2WtoLNu2Q_c3-0_d4-0_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=35,
    n_events=1555977,
)

