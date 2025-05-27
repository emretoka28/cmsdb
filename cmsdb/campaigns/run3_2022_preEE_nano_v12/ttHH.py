import cmsdb.processes as procs
from cmsdb.campaigns.run3_2022_preEE_nano_v12 import campaign_run3_2022_preEE_nano_v12 as cpn

cpn.add_dataset(
    name="ttHHto4b_madgraph",
    id=15267617,
    processes=[procs.ttHH],
    keys=[
        "/TTHHto4B_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=29,
    n_events=998582,
)