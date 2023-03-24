# CMS HLT@Phase2 Tracking Confgurations 

This repository contains the instructions to run 

The old configs and workflows used for the Upgrade DAQ and HLT TDR in 2022 are under the `tdr_master` branch. In this branch we "restart" the setup in a more sensible way.

To setup your cmssw to have the ingredients to run the upgrade hlt tracking configs start with

```
scram p -n cmssw CMSSW_13_0_0
cd cmssw/src
cmsenv
git cms-merge-topic cms-hlt-upgrade-trk:phase2_hlt_tracking
scram b -j 4
```

At the moment this has been tested with `13_0_0` and `13_1_0_pre4`


### Baseline Tracking Configuration

To run the *baseline* tracking configuration you can derive it from the simplified HLT menu in the release (since `12_3_X`) and customizing it to run *only* tracking + tracking validation:

```
cmsDriver.py Phase2 -s HLT:75e33 --processName=HLTX --conditions auto:phase2_realistic_T21 --geometry Extended2026D88 --era Phase2C17I13M9 --eventcontent FEVTDEBUGHLT --filein=/store/relval/CMSSW_12_4_0_pre3/RelValTTbar_14TeV/GEN-SIM-RECO/123X_mcRun4_realistic_v11_2026D88noPU-v1/2580000/4cb86d46-f780-4ce7-94df-9e0039e1953b.root -n 100 --nThreads 8
```

If you want to explore all the modules used run:

```
edmConfigDump Phase2_L1TrackTrigger_L1_HLT.py > HLT_75e33_cfg.py
```