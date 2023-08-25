# CMS HLT@Phase2 Tracking Configurations 

This repository contains the instructions to run 

The old configs and workflows used for the Upgrade DAQ and HLT TDR in 2022 are under the `tdr_master` branch. In this branch we "restart" the setup in a more sensible way.

To setup your cmssw to have the ingredients to run the upgrade hlt tracking configs start with

```
scram p -n cmssw CMSSW_13_1_0
cd cmssw/src
cmsenv
git cms-merge-topic cms-hlt-upgrade-trk:CMSSW_13_1_0_phase2_hlt_tracking
scram b -j 4
```

-----
### Baseline Tracking Configuration

To run the *baseline* tracking configuration you can derive it from the simplified HLT menu in the release (since `12_3_X`) and customizing it to run *only* tracking + tracking validation:

```
cmsDriver.py Phase2 -s HLT:75e33 \
    --processName=HLTX \
     --conditions auto:phase2_realistic_T21  \
     --geometry Extended2026D95 \
     --era Phase2C17I13M9 \
     --eventcontent FEVTDEBUGHLT \
     --filein=/store/mc/Phase2Spring23DIGIRECOMiniAOD/TT_TuneCP5_14TeV-powheg-pythia8/GEN-SIM-DIGI-RAW-MINIAOD/PU200_131X_mcRun4_realistic_v5-v1/50000/023b71b9-1d38-4891-b5e6-d584032d2cc4.root \
     -n 10 \
     --nThreads 10 \
     --customise HLTrigger/Configuration/customizePhase2HLTTracking.customisePhase2HLTForTrackingOnly,HLTrigger/Configuration/customizePhase2HLTTracking.addTrackingValidation
```
Note that:
- if you want to run the whole menu skip the `customisePhase2HLTForTrackingOnly` customizer; [not working at the moment]
- if you don't want to run the validation skip `addTrackingValidation` customizer.

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
### Patatrack 2-Iteration Configuration

```
cmsDriver.py Phase2_Patatrack -s HLT:75e33 \
    --processName=HLTX \
     --conditions auto:phase2_realistic_T21 \
     --geometry Extended2026D95 \
     --era Phase2C17I13M9 \
     --eventcontent FEVTDEBUGHLT \
     --filein=/store/mc/Phase2Spring23DIGIRECOMiniAOD/TT_TuneCP5_14TeV-powheg-pythia8/GEN-SIM-DIGI-RAW-MINIAOD/PU200_131X_mcRun4_realistic_v5-v1/50000/023b71b9-1d38-4891-b5e6-d584032d2cc4.root \
     -n 10 \
     --nThreads 10 \
     --customise HLTrigger/Configuration/customizePhase2HLTTracking.customisePhase2HLTForTrackingOnly,HLTrigger/Configuration/customizePhase2HLTTracking.customisePhase2HLTForPatatrack,HLTrigger/Configuration/customizePhase2HLTTracking.addTrackingValidation
```

-----
### Patatrack Single Iteration (WIP)

A single iteration approach will be implemented in which the all the pixel tracks (including triplets) are produced and used as input for the `initialStep` tracks while the `highPtTriplet` step is dropped.
