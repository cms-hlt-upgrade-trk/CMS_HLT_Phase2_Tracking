# CMS HLT@Phase2 Tracking Confgurations 


### Adding tracking sequence to your process

All the required modules are in `/wfs/` directory. First you need the raw2digi, tracking, validation, prevalidation, dqm sequences to be loaded
```
process.load('raw2digi_step_cff')
process.load("tracking_sequences_nol1")
process.load('validation_sequences')
process.load('prevalidation_sequences')
process.load('dqm_sequences')
```

then to run the various tracking sequence import the customization functions

```from customize_steps import *```

This is working in CMSSW_12_3_0

## Tracking configurations

### V6s

#### V6_1 (baseline)

The __v6_1__ configuration is the __baseline__ configuration consisting of two main iterations running after pixel tracks building.

1. PixelTracks and PixelVertices (Run2 like set up to have high PV tagging) production; 
2. initialStep iteration: seeded from pixel tracks, BS constrained; 
3. highPtTripletStep iteration: seeded with pixel triplet seeds, BS constrained; 

The final products are:

4. hltPhase2GeneralTracks: from the merge of initialStepTracks and highPtTripletStepTracks;
5. hltPhase2UnsortedOfflinePrimaryVertices: vertices with Deterministic Annealing built from hltPhase2GeneralTracks;

To run this configuration use

```cmsRun step3.py n=N ```

or use

```customizeOriginal_v6(process,timing)```

on your process. Note that this will overwrite your schedule and you would need to add your futher reco in the schedule after this. The `timing` variable is set to `False` by default. If set to `True` it basically drops prevalidation, validation and dqm steps.

#### V6_2 (baseline with patatrack pixel tracks)

The __v6_2__ configuration has the same iterations as the __baseline__ configuration with the difference that the pixel tracks, used as seeding for InitialStep, are reconstructed with Patatrack pixel tracks. Once the Patatrack CMSSW environment is set up you would need only to run:

```cmsRun step3.py n=N patatrack=True```

Or to use the 

```customizePixelTracksSoAonCPU(process,vertex=False)```

where the vertex flag indicates if the vertices has to be Patatrack-like (not the default option).

#### V6_3 (baseline with seeding only from patatrack pixel tracks)

The __v6_3__ configuration has the same iterations as the __baseline__ configuration with the difference that the pixel tracks are reconstructed with Patatrack pixel tracks and the further used both to seed the initial step iteration (being filtered to have > 3 hits) and the high pT triplet (being filtered to have exactly 3 hits)

```cmsRun step3.py allpata=True patatrack=True pixtrip=True keepBad=2 keepDup=2```

the `keepBad` and `keepDup` flags allow to keep pixelTracks that has been marked as fakes or duplicates so that they may be used as seeds for the next steps, where 2 indicates the minimal lenght of the pixel tracks to be kept is 2.


### V7s

#### V7_1

Historically was jumped for some mysterious reason ...

#### V7_2 (trimmed)

The __v7_2__ configuration is the configuration __trimmed__ around the vertices reconstructed as pixel vertices with pixel tracks. It consists of two main iterations running after pixel tracks building.

1. PixelTracks and PixelVertices (Run2 like set up to have high PV tagging) production; 
2. Pixel Vertices Trimming with: max number of vertices==10, min SumPt2 fraction w.r.t. leading = 0.1 and min SumPt2==10GeV;
2. initialStep iteration: seeded from pixel tracks, constrained to the trimmed PVs; 
3. highPtTripletStep iteration: seeded with pixel triplet seeds, constrained to the trimmed PVs; 

The final products are:

4. hltPhase2GeneralTracks: from the merge of initialStepTracks and highPtTripletStepTracks;
5. hltPhase2UnsortedOfflinePrimaryVertices: vertices with Deterministic Annealing built from hltPhase2GeneralTracks;

To run this configuration use

```cmsRun step3.py n=N wf=-4```

or either use 

```
customizeOriginalTrimmingInitial_v6(process,timing,fraction=FRAC,numVertex=NVTX,minSumPt2=SUMPT2)
customizeOriginalTrimmingTriplet_v6(process,timing,fraction=FRAC,numVertex=NVTX,minSumPt2=SUMPT2)
```

on your process where the suggested cuts are the above mentioned:

- `FRAC = 10` 
- `NVTX = 10`
- `SUMPT2 = 10`


#### V7_3 (trimmed with patatrack pixel tracks)

The __v7_3__ configuration has the same iterations as the __trimmed__ configuration with the difference that the pixel tracks, used as seeding for InitialStep, are reconstructed with Patatrack pixel tracks. Once the Patatrack CMSSW environment is set up you would need only to run:

```cmsRun step3.py n=N patatrack=True wf=-4```

Or to use the 

```
customizePixelTracksSoAonCPU(process,vertex=False)
customizeOriginalTrimmingInitial_v6(process,timing,fraction=FRAC,numVertex=NVTX,minSumPt2=SUMPT2)
customizeOriginalTrimmingTriplet_v6(process,timing,fraction=FRAC,numVertex=NVTX,minSumPt2=SUMPT2)
```

where the vertex flag indicates if the vertices has to be Patatrack-like (not the default option).

#### V7_4 (trimmed with seeding only from patatrack pixel tracks)

The __v7_4__ configuration has the same iterations as the __trimmed__ configuration with the difference that the pixel tracks are reconstructed with Patatrack pixel tracks and the further used both to seed the initial step iteration (being filtered to have > 3 hits) and the high pT triplet (being filtered to have exactly 3 hits)

```cmsRun step3.py allpata=True patatrack=True pixtrip=True wf=-4 keepBad=2 keepDup=2```

### Adding L1Vertex Region For PixelTracks

For __v6_2__, __v6_3__, __v7_3__ and __v7_4__ one may activate the region definition around the L1 vertex for pixel track seeds as

- __v6_2__ : `cmsRun step3.py n=N patatrack=True doregion=True`
- __v6_3__ : `cmsRun step3.py allpata=True patatrack=True pixtrip=True keepBad=2 keepDup=2 doregion=True`
- __v7_3__ : `cmsRun step3.py wf=-4 n=N patatrack=True doregion=True`
- __v7_4__ : `cmsRun step3.py wf=-4 allpata=True patatrack=True pixtrip=True keepBad=2 keepDup=2 doregion=True`

Or one may direclty act on the Pixel Tracks SoA producer (if defined in the process) with

```process.hltPhase2PixelTrackSoA.doRegion = True ```

### V8 (Single Iteration - WIP)

The __v8__ is a configuration with a single iteration seeded by Patatrack pixel tracks [WIP]


