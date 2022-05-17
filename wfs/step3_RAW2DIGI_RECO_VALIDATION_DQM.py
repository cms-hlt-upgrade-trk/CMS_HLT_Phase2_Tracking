# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: step3 -s RAW2DIGI,RECO:reconstruction_trackingOnly,VALIDATION:@trackingOnlyValidation,DQM:@trackingOnlyDQM --conditions auto:phase2_realistic_T21 --datatier GEN-SIM-RECO,DQMIO -n 10 --eventcontent RECOSIM,DQM --geometry Extended2026D88 --era Phase2C11I13M9 --filein file:step2.root --fileout file:step3.root
import FWCore.ParameterSet.Config as cms

from Configuration.Eras.Era_Phase2C11I13M9_cff import Phase2C11I13M9

from SLHCUpgradeSimulations.Configuration.aging import customise_aging_1000
import FWCore.ParameterSet.VarParsing as VarParsing
from customize_steps import *

process = cms.Process('RECO',Phase2C11I13M9)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.Geometry.GeometryExtended2026D88Reco_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.RawToDigi_cff')
process.load('Configuration.StandardSequences.Reconstruction_cff')
process.load('Configuration.StandardSequences.Validation_cff')
process.load('DQMServices.Core.DQMStoreNonLegacy_cff')
process.load('DQMOffline.Configuration.DQMOfflineMC_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
process.load("FWCore.Services.DependencyGraph_cfi")

options = VarParsing.VarParsing('analysis')
options.register ('wf',-1, VarParsing.VarParsing.multiplicity.singleton,VarParsing.VarParsing.varType.int,"wf number")

options.register('timing',False,VarParsing.VarParsing.multiplicity.singleton,VarParsing.VarParsing.varType.bool,"only timing")
options.register('debug',False,VarParsing.VarParsing.multiplicity.singleton,VarParsing.VarParsing.varType.bool,"debug")

options.register('n',10,VarParsing.VarParsing.multiplicity.singleton,VarParsing.VarParsing.varType.int,"max events")
options.register('skip',0,VarParsing.VarParsing.multiplicity.singleton,VarParsing.VarParsing.varType.int,"events to skip")
options.register('threads',4,VarParsing.VarParsing.multiplicity.singleton,VarParsing.VarParsing.varType.int,"num of threads")

#L1 Tracks
options.register('l1extended',False,VarParsing.VarParsing.multiplicity.singleton,VarParsing.VarParsing.varType.bool,"l1 extended")
options.register('nol1',False,VarParsing.VarParsing.multiplicity.singleton,VarParsing.VarParsing.varType.bool,"do not include l1tracks in generaltracks")

#Pixel setups
options.register('pixtrip',False,VarParsing.VarParsing.multiplicity.singleton,VarParsing.VarParsing.varType.bool,"pixel Triplets")
options.register('onlypixel',False,VarParsing.VarParsing.multiplicity.singleton,VarParsing.VarParsing.varType.bool,"onlypixel")
options.register('protokin',False,VarParsing.VarParsing.multiplicity.singleton,VarParsing.VarParsing.varType.bool,"using proto tracks kinematics")

#Patatrack
options.register('mkfit',False,VarParsing.VarParsing.multiplicity.singleton,VarParsing.VarParsing.varType.bool,"running mkfit")
options.register('patatrack',False,VarParsing.VarParsing.multiplicity.singleton,VarParsing.VarParsing.varType.bool,"Patatrack Pixel Tracks")
options.register('clean',False,VarParsing.VarParsing.multiplicity.singleton,VarParsing.VarParsing.varType.bool,"Use Cleaned Patatrack Pixel Tracks")
options.register('allpata',False,VarParsing.VarParsing.multiplicity.singleton,VarParsing.VarParsing.varType.bool,"Seeding only from Patatrack Pixel Tracks")
options.register('doregion',False,VarParsing.VarParsing.multiplicity.singleton,VarParsing.VarParsing.varType.bool,"Seeding only from Patatrack Pixel Tracks")
options.register('rhoVtx',300,VarParsing.VarParsing.multiplicity.singleton,VarParsing.VarParsing.varType.int,"vtx for region rho distance (x1000)")
options.register('zVtx',100,VarParsing.VarParsing.multiplicity.singleton,VarParsing.VarParsing.varType.int,"vtx for region z distance (x1000)")
options.register('keepBad',99,VarParsing.VarParsing.multiplicity.singleton,VarParsing.VarParsing.varType.int,"keepBad")
options.register('keepDup',99,VarParsing.VarParsing.multiplicity.singleton,VarParsing.VarParsing.varType.int,"keepDup")

#Vetexing
options.register('davertex',False,VarParsing.VarParsing.multiplicity.singleton,VarParsing.VarParsing.varType.bool,"da pixel vertexing")
options.register('fullvertex',True,VarParsing.VarParsing.multiplicity.singleton,VarParsing.VarParsing.varType.bool,"full vertexing")
options.register('patavertex',False,VarParsing.VarParsing.multiplicity.singleton,VarParsing.VarParsing.varType.bool,"pata vertexing")
options.register('fastl1',False,VarParsing.VarParsing.multiplicity.singleton,VarParsing.VarParsing.varType.bool,"fastl1 vertexing")
options.register('froml1',False,VarParsing.VarParsing.multiplicity.singleton,VarParsing.VarParsing.varType.bool,"froml1 vertexing")

#EventContent
options.register('fullcontent',False,VarParsing.VarParsing.multiplicity.singleton,VarParsing.VarParsing.varType.bool,"full content")
options.register('recosim',False,VarParsing.VarParsing.multiplicity.singleton,VarParsing.VarParsing.varType.bool,"recosim content")

#Trimming&Vertexing
options.register('frac',10,VarParsing.VarParsing.multiplicity.singleton,VarParsing.VarParsing.varType.int,"vtx sum pt fraction (in %)")
options.register('nvtx',10,VarParsing.VarParsing.multiplicity.singleton,VarParsing.VarParsing.varType.int,"n trimmed vtx")
options.register('sumpt',10 ,VarParsing.VarParsing.multiplicity.singleton,VarParsing.VarParsing.varType.int,"minsumpt2 vtx")
options.register('zsep',5,VarParsing.VarParsing.multiplicity.singleton,VarParsing.VarParsing.varType.int,"z_sep (x1000)")
options.register('fromPV',True,VarParsing.VarParsing.multiplicity.singleton,VarParsing.VarParsing.varType.bool,"fromPV for ininitial step")

options.register('rI',250,VarParsing.VarParsing.multiplicity.singleton,VarParsing.VarParsing.varType.int,"vtx sum pt fraction (in %)")
options.register('zI',500,VarParsing.VarParsing.multiplicity.singleton,VarParsing.VarParsing.varType.int,"n trimmed vtx")
options.register('fE',100,VarParsing.VarParsing.multiplicity.singleton,VarParsing.VarParsing.varType.int,"minsumpt2 vtx")
options.register('oR',250,VarParsing.VarParsing.multiplicity.singleton,VarParsing.VarParsing.varType.int,"vtx sum pt fraction (in %)")

#Samples
options.register('susy',False,VarParsing.VarParsing.multiplicity.singleton,VarParsing.VarParsing.varType.bool,"Susy")
options.register('dyll',False,VarParsing.VarParsing.multiplicity.singleton,VarParsing.VarParsing.varType.bool,"DY ll")
options.register('ztt',False,VarParsing.VarParsing.multiplicity.singleton,VarParsing.VarParsing.varType.bool,"ZTT MC")
options.register('dstmmm',False,VarParsing.VarParsing.multiplicity.singleton,VarParsing.VarParsing.varType.bool,"DsTau3M MC")
options.register('bdksmm',False,VarParsing.VarParsing.multiplicity.singleton,VarParsing.VarParsing.varType.bool,"BdToKstarMuMu MC")
options.register('b0ksmm',False,VarParsing.VarParsing.multiplicity.singleton,VarParsing.VarParsing.varType.bool,"B0ToKstarMuMu")
options.register('bskkkk',False,VarParsing.VarParsing.multiplicity.singleton,VarParsing.VarParsing.varType.bool,"BsToPhiPhi_KKKK MC")
options.register('withl1',False,VarParsing.VarParsing.multiplicity.singleton,VarParsing.VarParsing.varType.bool,"loading files with l1 tracks already produced")
options.register('muons',False,VarParsing.VarParsing.multiplicity.singleton,VarParsing.VarParsing.varType.bool,"DYMM MC")
options.register('noPU',False,VarParsing.VarParsing.multiplicity.singleton,VarParsing.VarParsing.varType.bool,"noPU events")
options.register('PU200',False,VarParsing.VarParsing.multiplicity.singleton,VarParsing.VarParsing.varType.bool,"PU200 events")

#Miscs
options.register ('note','',VarParsing.VarParsing.multiplicity.singleton,VarParsing.VarParsing.varType.string, "noting")

options.parseArguments()

from MCs.inputFiles import PU200_122x
filelist = PU200_122x

if options.PU200:
    from MCs.inputFiles import PU200_122x
    filelist = PU200_122x

if options.noPU:
    from MCs.inputFiles import noPU_122x
    filelist = noPU_122x

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(options.n),
    output = cms.optional.untracked.allowed(cms.int32,cms.PSet)
)

# Input source
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(filelist),
    secondaryFileNames = cms.untracked.vstring()
)

process.options = cms.untracked.PSet(
    FailPath = cms.untracked.vstring(),
    IgnoreCompletely = cms.untracked.vstring(),
    Rethrow = cms.untracked.vstring(),
    SkipEvent = cms.untracked.vstring(),
    allowUnscheduled = cms.obsolete.untracked.bool,
    canDeleteEarly = cms.untracked.vstring(),
    deleteNonConsumedUnscheduledModules = cms.untracked.bool(True),
    dumpOptions = cms.untracked.bool(False),
    emptyRunLumiMode = cms.obsolete.untracked.string,
    eventSetup = cms.untracked.PSet(
        forceNumberOfConcurrentIOVs = cms.untracked.PSet(
            allowAnyLabel_=cms.required.untracked.uint32
        ),
        numberOfConcurrentIOVs = cms.untracked.uint32(0)
    ),
    fileMode = cms.untracked.string('FULLMERGE'),
    forceEventSetupCacheClearOnNewRun = cms.untracked.bool(False),
    makeTriggerResults = cms.obsolete.untracked.bool,
    numberOfConcurrentLuminosityBlocks = cms.untracked.uint32(0),
    numberOfConcurrentRuns = cms.untracked.uint32(1),
    numberOfStreams = cms.untracked.uint32(0),
    numberOfThreads = cms.untracked.uint32(options.threads),
    printDependencies = cms.untracked.bool(False),
    sizeOfStackForThreadsInKB = cms.optional.untracked.uint32,
    throwIfIllegalParameter = cms.untracked.bool(True),
    wantSummary = cms.untracked.bool(False)
)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('step3 nevts:10'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition
'''
process.RECOSIMoutput = cms.OutputModule("PoolOutputModule",
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('GEN-SIM-RECO'),
        filterName = cms.untracked.string('')
    ),
    fileName = cms.untracked.string('file:step3.root'),
    outputCommands = process.RECOSIMEventContent.outputCommands,
    splitLevel = cms.untracked.int32(0)
)

process.DQMoutput = cms.OutputModule("DQMRootOutputModule",
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('DQMIO'),
        filterName = cms.untracked.string('')
    ),
    fileName = cms.untracked.string('file:step3_inDQM.root'),
    outputCommands = process.DQMEventContent.outputCommands,
    splitLevel = cms.untracked.int32(0)
)
'''
# Additional output definition

# Other statements
process.mix.playback = True
process.mix.digitizers = cms.PSet()
for a in process.aliases: delattr(process, a)
process.RandomNumberGeneratorService.restoreStateLabel=cms.untracked.string("randomEngineStateProducer")
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:phase2_realistic_T21', '')

#print(" ########## debug - 1 - ########## ")

process.load('raw2digi_step_cff')
process.load("RecoJets.JetProducers.caloJetsForTrk_cff")
process.load("tracking_sequences")

#print(" ########## debug - 2 - ########## ")

if not options.timing:
    process.load("SimTracker.TrackAssociatorProducers.quickTrackAssociatorByHits_cfi")# import quickTrackAssociatorByHits
    process.load("SimTracker.TrackerHitAssociation.tpClusterProducer_cfi")# import tpClusterProducer
    process.load("Validation.RecoTrack.TrackValidation_cff")# import trackingParticlesBHadron,trackingParticlesConversion,trackingParticleNumberOfLayersProducer
    process.load("SimGeneral.TrackingAnalysis.simHitTPAssociation_cfi")# import simHitTPAssocProducer
    process.load("Validation.RecoTrack.associators_cff")

    process.load('validation_sequences')
    process.load('prevalidation_sequences')
    process.load('dqm_sequences')

#print(" ########## debug - 3 - ########## ")

# load the DQMStore and DQMRootOutputModule
# enable multithreading
process.load( "DQMServices.Core.DQMStore_cfi" )
process.DQMStore.enableMultiThread = True

#print(" ########## debug - 4 - ########## ")

process.options = cms.untracked.PSet(
    wantSummary = cms.untracked.bool( True ),
    sizeOfStackForThreadsInKB = cms.untracked.uint32( 10*1024 )
)

#print(" ########## debug - 5 - ########## ")

T = min(options.threads,options.n)

process.options.numberOfThreads=cms.untracked.uint32(T)
process.options.numberOfStreams=cms.untracked.uint32(T)

#######
# -1 - original v6
# 0 - l1tracks only
# 1 - pixeltracks + l1tracks
# 2 - pixelTracks + initial step + l1tracks
# 3 - initialstep + l1tracks
# 4 - pixelTracksTriplets + l1tracks
#

timing = options.timing

suff = str(options.wf)

#TRIMMING OPTIONS
if options.wf < -1:

    if not options.timing:
        process.hltPhase2PixelVertexAnalysisTrackingOnly.vertexRecoCollections = cms.VInputTag("hltPhase2PixelVertices", "hltPhase2SelectedPixelVertices","hltPhase2TrimmedPixelVertices")

    process.hltPhase2InitialStepSeeds.usePV = cms.bool(options.fromPV)
    process.hltPhase2PixelVerticesSequence = cms.Sequence(
        process.hltPhase2PixelVertices +
        process.hltPhase2TrimmedPixelVertices +
        process.hltPhase2PixelTracksCleaner
    )
    #Minimal reasonable setup
    process.hltPhase2TrimmedPixelVertices.fractionSumPt2 = cms.double( 0.01 )
    process.hltPhase2TrimmedPixelVertices.minSumPt2 = cms.double( 10.0 )
    process.hltPhase2TrimmedPixelVertices.maxVtx = cms.uint32( 100 ) # > 200 # previous 100

if options.onlypixel:
    options.wf = -100
    suff = "pixelonly"

if options.wf == -5:
    customizeSingleIt(process,timing)
    suff = "m5"
    if options.clean: 
        process.hltPhase2InitialStepSeeds.InputCollection = cms.InputTag("hltPhase2PixelTracksMerger") 

if options.wf == -8:
    customizeL1SingleIt(process,timing)
    suff = "m8"
    if options.clean: 
        process.hltPhase2InitialStepSeeds.InputCollection = cms.InputTag("hltPhase2PixelTracksMerger")

if options.wf == -6:
    l1_pixel_recovery_triplets(process,timing)
    customizeOriginalTrimmingInitial_v6(process,timing,fraction=options.frac/100.,numVertex=options.nvtx,minSumPt2=options.sumpt)
    customizeOriginalTrimmingTriplet_v6(process,timing,fraction=options.frac/100.,numVertex=options.nvtx,minSumPt2=options.sumpt)
    suff = "m6_0p%d_%d_%d"%(options.frac,options.nvtx,options.sumpt)
if options.wf == -7:
    l1_pixel_recovery_triplets(process,timing)
    customizeOriginalTrimmingInitial_v6(process,timing,fraction=options.frac/100.,numVertex=options.nvtx,minSumPt2=options.sumpt)
    customizeOriginalTrimmingTriplet_v6(process,timing,fraction=options.frac/100.,numVertex=options.nvtx,minSumPt2=options.sumpt)
    suff = "m7_0p%d_%d_%d"%(options.frac,options.nvtx,options.sumpt)
    process.hltPhase2InitialStepSeeds.InputVertexCollection = cms.InputTag("hltPhase2L1PrimaryVertex")
    hltPhase2TrimmedVertexTrackingRegions.VertexCollection = cms.InputTag( "hltPhase2L1PrimaryVertex" )
 
if options.wf == -4:
    suff = "m4_0p%d_%d_%d"%(options.frac,options.nvtx,options.sumpt)
    customizeOriginal_v6(process,timing)
    customizeOriginalTrimmingInitial_v6(process,timing,fraction=options.frac/100.,numVertex=options.nvtx,minSumPt2=options.sumpt)
    customizeOriginalTrimmingTriplet_v6(process,timing,fraction=options.frac/100.,numVertex=options.nvtx,minSumPt2=options.sumpt)
    process.hltPhase2PixelTracksCleaner.rhoVtx = options.rI / 1000.
    process.hltPhase2PixelTracksCleaner.zetaVtx = options.zI / 1000.
    process.hltPhase2HighPtTripletStepTrackingRegions.RegionPSet.fixedError = options.fE /1000.0
    process.hltPhase2HighPtTripletStepTrackingRegions.RegionPSet.originRadius = options.oR / 1000.0
    suff = suff + "_I_%d_%d_H_%d_%d"%(options.rI,options.zI,options.fE,options.oR)

if options.wf == -3:
    customizeOriginal_v6(process,timing)
    suff = "m3_0p%d_%d_%d"%(options.frac,options.nvtx,options.sumpt)
    customizeOriginalTrimmingTriplet_v6(process,timing,fraction=options.frac/100.,numVertex=options.nvtx,minSumPt2=options.sumpt)
if options.wf == -2:
    customizeOriginal_v6(process,timing)
    suff = "m2_0p%d_%d_%d"%(options.frac,options.nvtx,options.sumpt)
    customizeOriginalTrimmingInitial_v6(process,timing,fraction=options.frac/100.,numVertex=options.nvtx,minSumPt2=options.sumpt)

##ORIGINAL v6_1
if options.wf == -1:
    suff = "m1"
    customizeOriginal_v6(process,timing)
    process.hltPhase2TrimmedPixelVertices = process.MeasurementTrackerEvent.clone()

if options.allpata and options.patatrack:
    suff = suff + "_tripFromTracks"
    process.hltPhase2PixelTracksCleaner.rhoVtx = 100.0 
    process.hltPhase2PixelTracksCleaner.useVtx = False
    process.hltPhase2PixelTracksCleaner.zetaVtx = 100.0
    
    process.hltPhase2PixelTripletsCleaner.rhoVtx = 100.0 
    process.hltPhase2PixelTripletsCleaner.useVtx = False
    process.hltPhase2PixelTripletsCleaner.zetaVtx = 100.0
   
    process.hltPhase2InitialStepSeeds.InputCollection = cms.InputTag("hltPhase2PixelTracksCleaner")#hltPhase2PixelQuadrupletsSelector")#hltPhase2PixelTracksCleaner")#hltPhase2PixelQuadrupletsSelector")
    process.hltPhase2HighPtTripletStepSeeds = process.hltPhase2InitialStepSeeds.clone()
    process.hltPhase2HighPtTripletStepSeeds.InputCollection = cms.InputTag("hltPhase2PixelTripletsCleaner")
    
    if hasattr(process,"hltPhase2HighPtTripletStepHitDoublets"):
        delattr(process,"hltPhase2HighPtTripletStepHitDoublets")
    if hasattr(process,"hltPhase2HighPtTripletStepHitTriplets"):
        delattr(process,"hltPhase2HighPtTripletStepHitTriplets")

if options.allpata and options.clean and options.patatrack:
    process.hltPhase2PixelTracksCleaner.rhoVtx = options.rhoVtx /1000.0
    process.hltPhase2PixelTracksCleaner.zetaVtx = options.zVtx / 1000.0
    process.hltPhase2PixelTripletsCleaner.useVtx = True
    process.hltPhase2PixelTracksCleaner.useVtx = False
    process.hltPhase2PixelTripletsCleaner.rhoVtx = options.rhoVtx /1000.0
    process.hltPhase2PixelTripletsCleaner.zetaVtx = options.zVtx / 1000.0

    if options.froml1:
        process.hltPhase2PixelTracksCleaner.vertexTag = cms.InputTag("hltPhase2L1PrimaryVertex")
        process.hltPhase2PixelTracksCleaner.vertexTag = cms.InputTag("hltPhase2L1PrimaryVertex")

if options.patatrack and options.clean and not options.allpata:
    process.hltPhase2PixelTracksCleaner.rhoVtx = options.rhoVtx /1000.0
    process.hltPhase2PixelTracksCleaner.zetaVtx = options.zVtx / 1000.0
    process.hltPhase2PixelTripletsCleaner.useVtx = True
    process.hltPhase2PixelTracksCleaner.useVtx = False
    process.hltPhase2PixelTripletsCleaner.rhoVtx = options.rhoVtx /1000.0
    process.hltPhase2PixelTripletsCleaner.zetaVtx = options.zVtx / 1000.0

    process.hltPhase2InitialStepSeeds.InputCollection = cms.InputTag("hltPhase2PixelTracksMerger")

    if options.froml1:
        process.hltPhase2PixelTracksCleaner.vertexTag = cms.InputTag("hltPhase2L1PrimaryVertex")
        process.hltPhase2PixelTracksCleaner.vertexTag = cms.InputTag("hltPhase2L1PrimaryVertex")

else:
    process.hltPhase2PixelTracksMerger = process.hltPhase2PixelTracksCleaner.clone()   

#L1 Customizing
if options.wf == 0:
    suff = "purel1"
    customizeGeneralTracksToPureL1TracksStep(process,timing)
if options.wf == 1:
    customizeGeneralTracksToPixelL1TracksStep(process,timing)
if options.wf == 2:
    customizeGeneralTracksToInitialL1TracksStep(process,timing)
if options.wf == 3:
    customizeGeneralTracksToInitialL1TracksStep(process,timing)
if options.wf == 4:
    customizeTripletL1(process,timing)
if options.wf == 5:
    pixel_l1_recovery(process,timing)
if options.wf == 6:
    l1_pixel_recovery(process,timing)
if options.wf == 7:
    l1_pixel_recovery_triplets(process,timing)

if options.mkfit:
    customizeHighPtTripletForMkFit(process)

if options.onlypixel:
    customizePixelOnly(process,timing)

if options.debug:
    suff = suff + "_debug"
if options.ztt:
    suff = suff + "_ztt"
elif options.dstmmm:
    suff = suff + "_dstmmm"
elif options.bdksmm:
    suff = suff + "_bdksmm"
elif options.b0ksmm:
    suff = suff + "_b0ksmm"
elif options.bskkkk:
    suff = suff + "_bskkkk"
elif options.susy:
    suff = suff + "_susy"
elif options.dyll:
    suff = suff + "_dyll"
else:
    suff = suff + "_ttb"

suff = suff + "_skip_" + str(options.skip) + "_n_" + str(options.n)

if options.clean:
    suff = suff + "_zVtx" + str(options.zVtx)
    suff = suff + "_rhoVtx" + str(options.rhoVtx)
if options.l1extended:
    process.hltPhase2L1TrackSeedsFromL1Tracks.InputCollection = cms.InputTag("TTTracksFromExtendedTrackletEmulation","Level1TTTracks")
if options.fullvertex or not options.timing:
    process.schedule.extend([process.vertexing])
    suff = suff + "_fullvertexing"

if options.fastl1:
    process.hltPhase2L1PrimaryVertex.TrackLabel = cms.InputTag("hltPhase2TrackFromL1")
    suff = suff + "_fastl1vertex"
elif options.froml1 and not options.timing:
    process.hltPhase2VertexAnalysisL1.vertexRecoCollections = cms.VInputTag("hltPhase2L1PrimaryVertex","hltPhase2VertexFromL1")
    suff = suff + "_froml1vertex"
if options.patavertex:
    suff = suff + "_patavertex"
if options.patatrack:
    customizePixelTracksSoAonCPU(process,options.patavertex)
#    if options.wf == -5:
 #       process.hltPhase2InitialStepSeeds = process.hltPhase2SoAPixelSeeds.clone()
    process.hltPhase2PixelTrackSoA.doRegion = options.doregion
    process.hltPhase2PixelTracks.keepBad = options.keepBad
    process.hltPhase2PixelTracks.keepDup = options.keepDup
    if options.clean:
        suff = suff + "_clean"
    if options.keepBad < 99:
        suff = suff + "_keepBad_"+str(options.keepBad)
    if options.keepDup <99:
        suff = suff + "_keepDup_"+str(options.keepDup)
    if options.doregion:  
        if options.froml1:
            process.pixelVertexCoordinates.src = "hltPhase2L1PrimaryVertex"
            suff = suff + "_regionFomL1"
        ##process.pixelVertexCoordinates.src = "hltPhase2L1PrimaryVertex"
        #process.pixelVertexCoordinates.src = "hltPhase2L1PrimaryVertex"
        else:
            suff = suff + "_regionL1"
    
    if options.pixtrip:
        process.hltPhase2PixelTrackSoA.minHitsPerNtuplet = 3
        suff = suff + "_pixtrips"
    suff = suff + "_pata"
    process.quickTrackAssociatorByHits.Purity_SimToReco = cms.double(0.65)
if options.davertex:
    process.hltPhase2PixelVertices = process.hltPhase2DAPrimaryVerticesUnsorted.clone()
    suff = suff + "_da"
elif not options.patavertex:
    process.hltPhase2PixelVertices.ZSeparation = float(options.zsep) / 1000.0

if hasattr(process,"hltPhase2InitialStepSeeds"):    
    process.hltPhase2InitialStepSeeds.useProtoTrackKinematics = cms.bool(options.protokin)
if hasattr(process,"hltPhase2HighPtTripletStepSeeds"):
    if options.allpata==True or options.wf <=-5:
        process.hltPhase2HighPtTripletStepSeeds.useProtoTrackKinematics = cms.bool(options.protokin)

if not options.patatrack:
    process.hltPhase2PixelVertices.TrackCollection = cms.InputTag( "hltPhase2PixelTracks")
    
if options.protokin:
    suff = suff + "_protokin"

suff = suff + "_zsep_" + str(options.zsep)

suff = suff + "_" + options.note

if options.nol1:
    process.hltPhase2InitialStepTrackCandidates.phase2clustersToSkip = cms.InputTag("hltPhase2InitialStepClusters")
    process.hltPhase2HighPtTripletStepSeedLayers.FPix.skipClusters = cms.InputTag("hltPhase2HighPtTripletStepClusters")
    process.hltPhase2HighPtTripletStepSeedLayers.BPix.skipClusters = cms.InputTag("hltPhase2HighPtTripletStepClusters")
    process.hltPhase2HighPtTripletStepClusters.oldClusterRemovalInfo = cms.InputTag("hltPhase2InitialStepClusters")

    process.trackAlgoPriorityOrder.algoOrder = cms.vstring('initialStep','highPtTripletStep')
    process.hltPhase2GeneralTracks.TrackProducers = cms.VInputTag("hltPhase2InitialStepTracksSelectionHighPurity","hltPhase2HighPtTripletStepTracksSelectionHighPurity")
    process.hltPhase2GeneralTracks.hasSelector = cms.vint32(0,0,0)
    process.hltPhase2GeneralTracks.indivShareFrac = cms.vdouble(1.0,1.0)
    process.hltPhase2GeneralTracks.selectedTrackQuals= cms.VInputTag(cms.InputTag("hltPhase2InitialStepTracksSelectionHighPurity"),cms.InputTag("hltPhase2HighPtTripletStepTracksSelectionHighPurity"))
    process.hltPhase2GeneralTracks.setsToMerge.tLists = cms.vint32(0,1)

    suff = suff + "_nol1"

    #process.hltPhase2InitialStepTracks.clusterRemovalInfo = cms.InputTag("hltPhase2L1TrackStepClusters")
    if not options.timing:
        process.hltPhase2TrackValidatorTrackingOnly.label = cms.VInputTag(
        "hltPhase2GeneralTracks","hltPhase2CutsRecoTracksHighPtTripletStepHp",
        "hltPhase2CutsRecoTracksInitialStep", "hltPhase2CutsRecoTracksInitialStepHp","hltPhase2CutsRecoTracksHighPtTripletStep",
        "hltPhase2CutsRecoTracksInitialStepByOriginalAlgo", "hltPhase2CutsRecoTracksInitialStepByOriginalAlgoHp",
        "hltPhase2CutsRecoTracksHighPtTripletStepByOriginalAlgo","hltPhase2CutsRecoTracksHighPtTripletStepByAlgoMask",
        "hltPhase2CutsRecoTracksHighPtTripletStepByAlgoMaskHp",
        "hltPhase2GeneralTracksPt09", "hltPhase2CutsRecoTracksPt09Hp", "hltPhase2CutsRecoTracksBtvLike", "hltPhase2CutsRecoTracksInitialStepByAlgoMask",
        "hltPhase2CutsRecoTracksInitialStepByAlgoMaskHp", "hltPhase2CutsRecoTracksPt09InitialStep", "hltPhase2CutsRecoTracksPt09InitialStepHp",
        "hltPhase2CutsRecoTracksL1StepByOriginalAlgo","hltPhase2CutsRecoTracksL1StepByOriginalAlgoHp")
    
#DependecyGraph
#from FWCore.ParameterSet.Utilities import moduleLabelsInSequences
process.DependencyGraph.highlightModules = ["hltPhase2PixelTracks","hltPhase2PixelVertices","hltPhase2InitialStepTracks","hltPhase2InitialStepTrackCandidates"]

process.DependencyGraph.showPathDependencies = True
process.DependencyGraph.fileName = 'dependency' + suff + '.gv'


process.RECOSIMoutput = cms.OutputModule("PoolOutputModule",
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('GEN-SIM-RECO'),
        filterName = cms.untracked.string('')
    ),
    fileName = cms.untracked.string('file:step3_' + suff + '.root'),
    outputCommands = process.RECOSIMEventContent.outputCommands,
    splitLevel = cms.untracked.int32(0)
)

process.DQMoutput = cms.OutputModule("DQMRootOutputModule",
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('DQMIO'),
        filterName = cms.untracked.string('')
    ),
    fileName = cms.untracked.string('file:step3_inDQM_' + suff + '.root'),
    outputCommands = process.DQMEventContent.outputCommands,
    splitLevel = cms.untracked.int32(0)
)

process.FEVTDEBUGHLToutput = cms.OutputModule("PoolOutputModule",
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('GEN-SIM-DIGI-RAW-RECO-HLTDEBUG'),
        filterName = cms.untracked.string('')
    ),
    fileName = cms.untracked.string('file:step3_full_' + suff + '.root'),
    outputCommands = process.FEVTDEBUGHLTEventContent.outputCommands,
    splitLevel = cms.untracked.int32(0)
)

if not timing:
    process.DQMoutput_step = cms.EndPath( process.DQMoutput)
    process.schedule.extend([process.DQMoutput_step])

if options.fullcontent:

    process.FEVTDEBUGHLToutput = cms.OutputModule("PoolOutputModule",
        dataset = cms.untracked.PSet(
            dataTier = cms.untracked.string('GEN-SIM-DIGI-RAW-RECO-HLTDEBUG'),
            filterName = cms.untracked.string('')
        ),
        fileName = cms.untracked.string('file:step3_full_' + suff + '.root'),
        outputCommands = process.FEVTDEBUGHLTEventContent.outputCommands,
        splitLevel = cms.untracked.int32(0)
    )

    # process.FEVTDEBUGHLToutput.outputCommands.append('keep *')
    process.FEVTDEBUGHLToutput.outputCommands.append('keep *_hltPhase2GeneralTracks_*_*')
    process.FEVTDEBUGHLToutput.outputCommands.append('keep *_hltPhase2*PixelVertices_*_*')
    process.FEVTDEBUGHLToutput.outputCommands.append('keep *_hltPhase2PixelTracks_*_*')
    process.FEVTDEBUGHLToutput.outputCommands.append('keep *_hltPhase2HighPtTripletStepTracks_*_*')
    process.FEVTDEBUGHLToutput.outputCommands.append('keep *_hltPhase2InitialStepTracks_*_*')
    process.full_output_step = cms.EndPath(process.FEVTDEBUGHLToutput)
    process.schedule.extend([process.full_output_step])

elif options.recosim:

    process.RECOSIMoutput = cms.OutputModule("PoolOutputModule",
        dataset = cms.untracked.PSet(
            dataTier = cms.untracked.string('GEN-SIM-RECO'),
            filterName = cms.untracked.string('')
        ),
        fileName = cms.untracked.string('file:step3_reco_' + suff + '.root'),
        outputCommands = process.RECOSIMoutput.outputCommands,
        splitLevel = cms.untracked.int32(0)
    )

    # process.FEVTDEBUGHLToutput.outputCommands.append('keep *')
    process.RECOSIMoutput.outputCommands.append('keep *_hltPhase2GeneralTracks_*_*')
    process.RECOSIMoutput.outputCommands.append('keep *_hltPhase2*PixelVertices_*_*')
    process.RECOSIMoutput.outputCommands.append('keep *_hltPhase2PixelTracks_*_*')
    process.RECOSIMoutput.outputCommands.append('keep *_hltPhase2HighPtTripletStepTracks_*_*')
    process.RECOSIMoutput.outputCommands.append('keep *_hltPhase2InitialStepTracks_*_*')

    process.full_output_step = cms.EndPath(process.RECOSIMoutput)
    process.schedule.extend([process.full_output_step])

if 'PrescaleService' in process.__dict__:
    for pset in reversed(process.PrescaleService.prescaleTable):
        if not hasattr(process,pset.pathName.value()):
            process.PrescaleService.prescaleTable.remove(pset)


#print(" ########## debug - 6 - ########## ")
# Path and EndPath definitions
#process.raw2digi_step = cms.Path(process.RawToDigi)
#process.reconstruction_step = cms.Path(process.reconstruction_trackingOnly)
#process.prevalidation_step = cms.Path(process.globalPrevalidationTrackingOnly)
#process.validation_step = cms.EndPath(process.globalValidationTrackingOnly)
#process.dqmoffline_step = cms.EndPath(process.DQMOfflineTracking)
#process.dqmofflineOnPAT_step = cms.EndPath(process.PostDQMOffline)
#process.RECOSIMoutput_step = cms.EndPath(process.RECOSIMoutput)
#process.DQMoutput_step = cms.EndPath(process.DQMoutput)

#print(" ########## debug - 7 - ########## ")
# Schedule definition
#process.schedule = cms.Schedule(process.raw2digi_step,process.reconstruction_step,process.prevalidation_step,process.validation_step,process.dqmoffline_step,process.dqmofflineOnPAT_step,process.RECOSIMoutput_step,process.DQMoutput_step)
#process.schedule = cms.Schedule(process.raw2digi_step,process.reconstruction_step,process.validation_step,process.dqmofflineOnPAT_step,process.DQMoutput_step)
from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)

#print(" ########## debug - 8 - ########## ")

# customisation of the process.

# Automatic addition of the customisation function from SimGeneral.MixingModule.fullMixCustomize_cff
from SimGeneral.MixingModule.fullMixCustomize_cff import setCrossingFrameOn 

#call to customisation function setCrossingFrameOn imported from SimGeneral.MixingModule.fullMixCustomize_cff
process = setCrossingFrameOn(process)

# End of customisation functions

#print(" ########## debug - 9 - ########## ")
# Customisation from command line

#Have logErrorHarvester wait for the same EDProducers to finish as those providing data for the OutputModule
from FWCore.Modules.logErrorHarvester_cff import customiseLogErrorHarvesterUsingOutputCommands
process = customiseLogErrorHarvesterUsingOutputCommands(process)
#print(" ########## debug - 10 - ########## ")
# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion
#print(" ########## debug - 11 - ########## ")
