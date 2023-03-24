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
cmsDriver.py Phase2 -s HLT:75e33 --processName=HLTX --conditions 130X_mcRun4_realistic_v2 --geometry Extended2026D95 --era Phase2C17I13M9 --eventcontent FEVTDEBUGHLT --filein=/store/relval/CMSSW_13_0_0_pre4/RelValTTbar_14TeV/GEN-SIM-RECO/PU_130X_mcRun4_realistic_v2_2026D95PU200-v2/00000/00d45085-5103-411b-82ea-19d4b11bfd67.root -n 100 --nThreads 10 --customise HLTrigger/Configuration/customizePhase2HLTTracking.customisePhase2HLTForTrackingOnly
```

If you want to explore all the modules used run:

```
edmConfigDump Phase2_HLT.py > HLT_75e33_cfg.py
```

Once it runs you may run the *harvesting* with

```
harvestTrackValidationPlots.py Phase2HLT_DQM.root -o plots.root
```

and the plotter with 

```
makeTrackValidationPlots.py plots.root 
```