# CMS HLT@Phase2 Tracking Confgurations 

This repository contains the instructions to run 

The old configs and workflows used for the Upgrade DAQ and HLT TDR in 2022 are under the `tdr_master` branch. In this branch we "restart" the setup in a more sensible way.

To setup your cmssw to have the ingredients to run the upgrade hlt tracking configs start with

```
scram p -n cmssw CMSSW_13_2_0_pre2
cd cmssw/src
cmsenv
git cms-merge-topic cms-hlt-upgrade-trk:phase2_hlt_tracking_132
scram b -j 4
```

At the moment this has been tested with `13_2_0_pre2`

-----
### Baseline Tracking Configuration

To run the *baseline* tracking configuration you can derive it from the simplified HLT menu in the release (since `12_3_X`) and customizing it to run *only* tracking + tracking validation:

```
cmsDriver.py Phase2 -s HLT:75e33 \
    --processName=HLTX \
     --conditions 131X_mcRun4_realistic_v2 \
     --geometry Extended2026D95 \
     --era Phase2C17I13M9 \
     --eventcontent FEVTDEBUGHLT \
     --filein=/store/relval/CMSSW_13_1_0_pre1/RelValTTbar_14TeV/GEN-SIM-DIGI-RAW/PU_130X_mcRun4_realistic_v2_2026D95PU200-v2/00000/0413e17a-a6a1-422b-8da5-f237dfe5ac3b.root \
     -n 10 \
     --nThreads 10 \
     --customise HLTrigger/Configuration/customizePhase2HLTTracking.customisePhase2HLTForTrackingOnly,HLTrigger/Configuration/customizePhase2HLTTracking.addTrackingValidation
```
Note that:
- if you want to run the whole menu skip the `customisePhase2HLTForTrackingOnly` customizer;
- if you dont' want to run the validation skip `addTrackingValidation` customizer.

If you want to explore all the modules used run:

```
edmConfigDump Phase2_HLT.py > HLT_75e33_cfg.py
```

Once it runs, if you have run the validation with `addTrackingValidation`, you may run the *harvesting* with

```
harvestTrackValidationPlots.py Phase2HLT_DQM.root -o plots.root
```

and the plotter with 

```
makeTrackValidationPlots.py plots.root 
```

-----
### Patatrack Single Iteration (WIP)

At the moment only a single iteration approach has been implemented in which the all the pixel tracks (including triplets) are produced and used as inputo for the `initialStep` tracks while the `highPtTriplet` step is dropped. To run it use

```
cmsDriver.py Phase2_Patatrack -s HLT:75e33 \
    --processName=HLTX \
     --conditions 130X_mcRun4_realistic_v2 \
     --geometry Extended2026D95 \
     --era Phase2C17I13M9 \
     --eventcontent FEVTDEBUGHLT \
     --filein=/store/relval/CMSSW_13_0_0_pre4/RelValTTbar_14TeV/GEN-SIM-RECO/PU_130X_mcRun4_realistic_v2_2026D95PU200-v2/00000/00d45085-5103-411b-82ea-19d4b11bfd67.root 
     -n 10 \
     --nThreads 10 \
     --customise HLTrigger/Configuration/customizePhase2HLTTracking.customisePhase2HLTForTrackingOnly, HLTrigger/Configuration/customizePhase2HLTTracking.customisePhase2HLTForPatatrack, HLTrigger/Configuration/customizePhase2HLTTracking.addTrackingValidation
```

