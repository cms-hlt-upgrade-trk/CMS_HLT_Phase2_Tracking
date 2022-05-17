import FWCore.ParameterSet.Config as cms
from Configuration.StandardSequences.Reconstruction_cff import *
from RecoPixelVertexing.PixelLowPtUtilities.trackCleaner_cfi import *
from Configuration.StandardSequences.Reconstruction_cff import ClusterShapeTrajectoryFilter


########################################################################
######################## PSets && Constants


hltPhase2SeedFromProtoTracks = cms.PSet(
  TTRHBuilder = cms.string( "WithTrackAngle"), #hltESPTTRHBuilderPixelOnly" ),
  SeedMomentumForBOFF = cms.double( 5.0 ),
  propagator = cms.string( "PropagatorWithMaterial"),# previous PropagatorWithMaterialParabolicMf" ), # used also elsewhere though
  forceKinematicWithRegionDirection = cms.bool( False ),
  magneticField = cms.string( ""), # previous ParabolicMf" ),
  OriginTransverseErrorMultiplier = cms.double( 1.0 ),
  ComponentName = cms.string( "SeedFromConsecutiveHitsCreator" ),
  MinOneOverPtError = cms.double( 1.0 ) 
)

hltPhase2PSetPvClusterComparerForIT = cms.PSet(
  track_chi2_max = cms.double( 20.0 ),
  track_pt_max = cms.double( 100.0 ),
  track_prob_min = cms.double( -1.0 ),
  track_pt_min = cms.double( 1.0 )
)

layerListForPhase2 = ['BPix1+BPix2+BPix3+BPix4',
                       'BPix1+BPix2+BPix3+FPix1_pos','BPix1+BPix2+BPix3+FPix1_neg',
                       'BPix1+BPix2+FPix1_pos+FPix2_pos', 'BPix1+BPix2+FPix1_neg+FPix2_neg',
                       'BPix1+FPix1_pos+FPix2_pos+FPix3_pos', 'BPix1+FPix1_neg+FPix2_neg+FPix3_neg',
                       'FPix1_pos+FPix2_pos+FPix3_pos+FPix4_pos', 'FPix1_neg+FPix2_neg+FPix3_neg+FPix4_neg',
                       'FPix2_pos+FPix3_pos+FPix4_pos+FPix5_pos', 'FPix2_neg+FPix3_neg+FPix4_neg+FPix5_neg',
                       'FPix3_pos+FPix4_pos+FPix5_pos+FPix6_pos', 'FPix3_neg+FPix4_neg+FPix5_neg+FPix6_neg',
                       'FPix4_pos+FPix5_pos+FPix6_pos+FPix7_pos', 'FPix4_neg+FPix5_neg+FPix6_neg+FPix7_neg',
                       'FPix5_pos+FPix6_pos+FPix7_pos+FPix8_pos', 'FPix5_neg+FPix6_neg+FPix7_neg+FPix8_neg'
                       ]
layerListForPhase2Eta4 = layerListForPhase2 + ['FPix5_pos+FPix6_pos+FPix7_pos+FPix9_pos', 'FPix5_neg+FPix6_neg+FPix7_neg+FPix9_neg',
'FPix6_pos+FPix7_pos+FPix8_pos+FPix9_pos', 'FPix6_neg+FPix7_neg+FPix8_neg+FPix9_neg',
'FPix8_pos+FPix9_pos+FPix10_pos+FPix11_pos', 'FPix8_neg+FPix9_neg+FPix10_neg+FPix11_neg',
 'FPix11_pos+FPix9_pos+FPix10_pos+FPix12_pos', 'FPix9_neg+FPix10_neg+FPix11_neg+FPix12_neg']

tripletsLayers = [#'BPix1+BPix2+BPix3', 'BPix2+BPix3+BPix4',
                 #'BPix1+BPix3+BPix4', 'BPix1+BPix2+BPix4',
                 #'BPix2+BPix3+FPix1_pos', 'BPix2+BPix3+FPix1_neg',
                 #'BPix1+BPix2+FPix1_pos', 'BPix1+BPix2+FPix1_neg',
                 'BPix2+FPix1_pos+FPix2_pos', 'BPix2+FPix1_neg+FPix2_neg',
                 'BPix1+FPix1_pos+FPix2_pos', 'BPix1+FPix1_neg+FPix2_neg',
#
                 #'FPix1_pos+FPix2_pos+FPix3_pos', 'FPix1_neg+FPix2_neg+FPix3_neg',
                 'BPix1+FPix2_pos+FPix3_pos', 'BPix1+FPix2_neg+FPix3_neg',
#
                 'FPix2_pos+FPix3_pos+FPix4_pos', 'FPix2_neg+FPix3_neg+FPix4_neg',
                 'FPix3_pos+FPix4_pos+FPix5_pos', 'FPix3_neg+FPix4_neg+FPix5_neg',
                 'FPix4_pos+FPix5_pos+FPix6_pos', 'FPix4_neg+FPix5_neg+FPix6_neg',
                 'FPix5_pos+FPix6_pos+FPix7_pos', 'FPix5_neg+FPix6_neg+FPix7_neg',
                 #'FPix6_pos+FPix7_pos+FPix8_pos', 'FPix6_neg+FPix7_neg+FPix8_neg',
#  removed as redunant and covering effectively only eta>4   (here for documentation, to be optimized after TDR)
#                 ]
     ]

tripletsLayersEta4 = tripletsLayers +  ['BPix1+BPix2+FPix2_pos', 'BPix1+BPix2+FPix2_neg','BPix1+FPix1_pos+FPix3_pos',
                            'BPix1+FPix1_neg+FPix3_neg','FPix6_pos+FPix7_pos+FPix9_pos', 'FPix6_neg+FPix7_neg+FPix9_neg']




#######################################
###################### L1 Tracks step
#############

#hltPhase2TTTracksFromTracklet = TTTracksFromTrackletEmulation.clone()


hltPhase2VertexFromL1 = cms.EDProducer("L1ToVertex")

hltPhase2TrackFromL1 = cms.EDProducer("L1ToTrackFast",
    InputCollection = cms.InputTag("TTTracksFromTrackletEmulation","Level1TTTracks"),
    estimator = cms.string('hltPhase2L1TrackStepChi2Est'),
    propagator = cms.string('PropagatorWithMaterial'),
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"),
    maxEtaForTOB = cms.double(1.2),
    minEtaForTEC = cms.double(0.9),
    #TrajectoryBuilder = cms.string('GroupedCkfTrajectoryBuilder'),
    #TrajectoryBuilderPSet = cms.PSet(refToPSet_ = cms.string('hltPhase2L1TrackStepTrajectoryBuilder')),
    errorSFHitless = cms.double(1e-9)
    #TrajectoryBuilder = cms.string('GroupedCkfTrajectoryBuilder'),
    #TrajectoryBuilderPSet = cms.PSet( refToPSet_ = cms.string('L1TrackStepTrajectoryBuilder'))
)

hltPhase2L1TrackStepClusters = cms.EDProducer("TrackClusterRemoverPhase2",
    TrackQuality = cms.string('highPurity'),
    maxChi2 = cms.double(9.0),
    mightGet = cms.optional.untracked.vstring, # cmssw_11_1
    minNumberOfLayersWithMeasBeforeFiltering = cms.int32(0),
    oldClusterRemovalInfo = cms.InputTag(""),
    #overrideTrkQuals = cms.InputTag("initialStepSelector","initialStep"),
    overrideTrkQuals = cms.InputTag(""), # trackcutclassifier
    phase2OTClusters = cms.InputTag("siPhase2Clusters"),
    phase2pixelClusters = cms.InputTag("siPixelClusters"),
    trackClassifier = cms.InputTag("","QualityMasks"),
    trajectories = cms.InputTag("hltPhase2PixelTracks")
)

hltPhase2L1StepSeedClusterMask = seedClusterRemoverPhase2.clone(
    trajectories = cms.InputTag("hltPhase2L1TrackSeedsFromL1Tracks")
)

hltPhase2L1TrackSeedsFromL1Tracks = cms.EDProducer("SeedGeneratorFromL1TTracksEDProducer",
    InputCollection = cms.InputTag("TTTracksFromTrackletEmulation","Level1TTTracks"),
    estimator = cms.string('hltPhase2L1TrackStepChi2Est'),
    propagator = cms.string('PropagatorWithMaterial'),
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"),
    maxEtaForTOB = cms.double(1.2),
    minEtaForTEC = cms.double(0.9),
    #TrajectoryBuilder = cms.string('GroupedCkfTrajectoryBuilder'),
    #TrajectoryBuilderPSet = cms.PSet(refToPSet_ = cms.string('hltPhase2L1TrackStepTrajectoryBuilder')),
    errorSFHitless = cms.double(1e-9)
    #TrajectoryBuilder = cms.string('GroupedCkfTrajectoryBuilder'),
    #TrajectoryBuilderPSet = cms.PSet( refToPSet_ = cms.string('L1TrackStepTrajectoryBuilder'))
)

hltPhase2L1TracksSelectionHighPurity = cms.EDProducer( "TrackCollectionFilterCloner",
    minQuality = cms.string( "highPurity" ),
    copyExtras = cms.untracked.bool( True ),
    copyTrajectories = cms.untracked.bool( False ),
    originalSource = cms.InputTag( "hltPhase2L1CtfTracks" ),
    originalQualVals = cms.InputTag( 'hltPhase2L1TracksCutClassifier','QualityMasks' ),
    originalMVAVals = cms.InputTag( 'hltPhase2L1TracksCutClassifier','MVAValues' )
)

hltPhase2L1TrackStepTrajectoryFilter = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    minimumNumberOfHits = cms.int32(2),
    seedPairPenalty = cms.int32(0),
    chargeSignificance = cms.double(-1.0),
    minPt = cms.double(1.9),
    nSigmaMinPt = cms.double(3.0),
    minHitsMinPt = cms.int32(3),
    maxLostHits = cms.int32(999),
    maxConsecLostHits = cms.int32(1),
    maxNumberOfHits = cms.int32(100),

    maxLostHitsFraction = cms.double(1.1),
    constantValueForLostHitsFractionFilter = cms.double(2.),

    seedExtension = cms.int32(0),
    strictSeedExtension = cms.bool(False),
    pixelSeedExtension = cms.bool(False),

    minNumberOfHitsForLoopers           = cms.int32(13),
    minNumberOfHitsPerLoop              = cms.int32(4),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),

    maxCCCLostHits = cms.int32(9999),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('SiStripClusterChargeCutNone')
    ),
)

hltPhase2L1TrackStepTrajectoryFilterInOut = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(2.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    maxCCCLostHits = cms.int32(9999),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(999),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('SiStripClusterChargeCutNone')
    ),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(1.8), # ptcut previous 0.4
    minimumNumberOfHits = cms.int32(4),
    nSigmaMinPt = cms.double(3.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(1),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

hltPhase2L1TrackStepTrajectoryBuilder =  cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    bestHitOnly = cms.bool(True),
    propagatorAlong = cms.string('PropagatorWithMaterial'),
    propagatorOpposite = cms.string('PropagatorWithMaterialOpposite'),
    trajectoryFilter = cms.PSet(refToPSet_ = cms.string('hltPhase2L1TrackStepTrajectoryFilter')),
    inOutTrajectoryFilter = cms.PSet(refToPSet_ = cms.string('hltPhase2L1TrackStepTrajectoryFilterInOut')),
    # If true, then the inOutTrajectoryFilter will be ignored
    # and the trajectoryFilter will be used for in-out tracking too.
    useSameTrajFilter = cms.bool(True),
    # Maximum number of track candidates followed at each step of
    # track building
    maxCand = cms.int32(10),
    intermediateCleaning = cms.bool(True),
    # Chi2 added to track candidate if no hit found in layer
    lostHitPenalty = cms.double(30.0),
    foundHitBonus = cms.double(10.0),
    MeasurementTrackerName = cms.string(''),
    lockHits = cms.bool(False), #What does this do?
    TTRHBuilder = cms.string('WithTrackAngle'),
    updator = cms.string('KFUpdator'),
    # If true, track building will allow for possibility of no hit
    # in a given layer, even if it finds compatible hits there.
    alwaysUseInvalidHits = cms.bool(True),
    requireSeedHitsInRebuild = cms.bool(False), #(?)
    keepOriginalIfRebuildFails = cms.bool(True), #(?)
    estimator = cms.string('hltPhase2L1TrackStepChi2Est'),
    # Out-in tracking will not be attempted unless this many hits
    # are on track after in-out tracking phase.
    minNrOfHitsForRebuild = cms.int32(5),
    maxDPhiForLooperReconstruction = cms.double(2.0),
    maxPtForLooperReconstruction = cms.double(0),
    seedAs5DHit = cms.bool(False) #?
)

hltPhase2L1TrackStepChi2Est = cms.ESProducer("Chi2ChargeMeasurementEstimatorESProducer",
    ComponentName = cms.string('hltPhase2L1TrackStepChi2Est'),
    MaxChi2 = cms.double(30.0),
    MaxDisplacement = cms.double(0.5),
    MaxSagitta = cms.double(2),
    MinPtForHitRecoveryInGluedDet = cms.double(1000000000000),
    MinimalTolerance = cms.double(0.5),
    appendToDataLabel = cms.string(''),
    clusterChargeCut = cms.PSet(
        refToPSet_ = cms.string('SiStripClusterChargeCutNone')
    ),
    nSigma = cms.double(3.0),
    pTChargeCutThreshold = cms.double(15.0)
)

hltPhase2L1TrackCandidates= cms.EDProducer("CkfTrackCandidateMaker",
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"),
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    # During tracking, eliminate seeds used by an already found track
    RedundantSeedCleaner = cms.string('CachingSeedCleanerBySharedInput'),
    # Decide how to eliminate tracks sharing hits at end of tracking phase
    TrajectoryCleaner = cms.string('TrajectoryCleanerBySharedHits'),
    # Run cleaning after in-out tracking in addition to at end of tracking ?
    cleanTrajectoryAfterInOut = cms.bool(False),
    reverseTrajectories  =cms.bool(False),
    # Split matched strip tracker hits into mono/stereo components.
    useHitsSplitting = cms.bool(True),
    # After in-out tracking, do out-in tracking through the seeding
    # region and then further in.
    doSeedingRegionRebuilding = cms.bool(True),
    # Seed Producer
    maxNSeeds = cms.uint32(500000),
    maxSeedsBeforeCleaning = cms.uint32(10000),
    SimpleMagneticField = cms.string(''),
    src = cms.InputTag('hltPhase2L1TrackSeedsFromL1Tracks'),
    alias = cms.string('hltPhase2L1TrackCandidates'),
    TrajectoryBuilder = cms.string('GroupedCkfTrajectoryBuilder'),
    TrajectoryBuilderPSet = cms.PSet( refToPSet_ = cms.string('hltPhase2L1TrackStepTrajectoryBuilder')),
    TransientInitialStateEstimatorParameters = cms.PSet(
        numberMeasurementsForFit = cms.int32(4),
        propagatorAlongTISE = cms.string('PropagatorWithMaterial'),
        propagatorOppositeTISE = cms.string('PropagatorWithMaterialOpposite')
    ),
)

hltPhase2L1CtfTracks = cms.EDProducer( "TrackProducer",
    AlgorithmName = cms.string('hltIter0'),
    Fitter = cms.string('FlexibleKFFittingSmoother'),
    GeometricInnerState = cms.bool(False),
    MeasurementTracker = cms.string(''),
    MeasurementTrackerEvent = cms.InputTag( "MeasurementTrackerEvent"),
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    Propagator = cms.string('RungeKuttaTrackerPropagator'),
    SimpleMagneticField = cms.string(''),
    TTRHBuilder = cms.string('WithTrackAngle'),
    TrajectoryInEvent = cms.bool(False),
    alias = cms.untracked.string('ctfWithMaterialTracks'),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    clusterRemovalInfo = cms.InputTag(""),
    #src = cms.InputTag("L1TrackCandidates"),
    src = cms.InputTag("hltPhase2L1TrackCandidates"),
    useHitsSplitting = cms.bool(False),
    useSimpleMF = cms.bool(False)
)

hltPhase2L1StepSelector = cms.EDProducer("MultiTrackSelector",
    beamspot = cms.InputTag("offlineBeamSpot"),
    src = cms.InputTag("hltPhase2L1CtfTracks"),
    trackSelectors = cms.VPSet(
        cms.PSet(
            applyAbsCutsIfNoPV = cms.bool(False),
            applyAdaptedPVCuts = cms.bool(True),
            chi2n_no1Dmod_par = cms.double(9999),
            chi2n_par = cms.double(2.0),
            copyExtras = cms.untracked.bool(True),
            copyTrajectories = cms.untracked.bool(False),
            d0_par1 = cms.vdouble(0.8, 4.0),
            d0_par2 = cms.vdouble(0.6, 4.0),
            dz_par1 = cms.vdouble(0.9, 4.0),
            dz_par2 = cms.vdouble(0.8, 4.0),
            keepAllTracks = cms.bool(False),
            maxNumberLostLayers = cms.uint32(3),
            max_d0 = cms.double(100.0),
            max_eta = cms.double(9999.0),
            max_lostHitFraction = cms.double(1.0),
            max_minMissHitOutOrIn = cms.int32(99),
            max_relpterr = cms.double(9999.0),
            max_z0 = cms.double(100.0),
            minHitsToBypassChecks = cms.uint32(20),
            minNumber3DLayers = cms.uint32(3),
            minNumberLayers = cms.uint32(3),
            min_eta = cms.double(-9999.0),
            min_nhits = cms.uint32(0),
            nSigmaZ = cms.double(4.0),
            name = cms.string('L1StepLoose'),
            preFilterName = cms.string(''),
            qualityBit = cms.string('loose'),
            res_par = cms.vdouble(0.003, 0.002),
            vertexCut = cms.string('ndof>=2&!isFake'),
            vtxNumber = cms.int32(-1)
        ),
        cms.PSet(
            applyAbsCutsIfNoPV = cms.bool(False),
            applyAdaptedPVCuts = cms.bool(True),
            chi2n_no1Dmod_par = cms.double(9999),
            chi2n_par = cms.double(1.4),
            copyExtras = cms.untracked.bool(True),
            copyTrajectories = cms.untracked.bool(False),
            d0_par1 = cms.vdouble(0.7, 4.0),
            d0_par2 = cms.vdouble(0.5, 4.0),
            dz_par1 = cms.vdouble(0.8, 4.0),
            dz_par2 = cms.vdouble(0.7, 4.0),
            keepAllTracks = cms.bool(True),
            maxNumberLostLayers = cms.uint32(2),
            max_d0 = cms.double(100.0),
            max_eta = cms.double(9999.0),
            max_lostHitFraction = cms.double(1.0),
            max_minMissHitOutOrIn = cms.int32(99),
            max_relpterr = cms.double(9999.0),
            max_z0 = cms.double(100.0),
            minHitsToBypassChecks = cms.uint32(20),
            minNumber3DLayers = cms.uint32(3),
            minNumberLayers = cms.uint32(3),
            min_eta = cms.double(-9999.0),
            min_nhits = cms.uint32(0),
            nSigmaZ = cms.double(4.0),
            name = cms.string('L1StepTight'),
            preFilterName = cms.string('L1StepLoose'),
            qualityBit = cms.string('tight'),
            res_par = cms.vdouble(0.003, 0.002),
            vertexCut = cms.string('ndof>=2&!isFake'),
            vtxNumber = cms.int32(-1)
        ),
        cms.PSet(
            applyAbsCutsIfNoPV = cms.bool(False),
            applyAdaptedPVCuts = cms.bool(True),
            chi2n_no1Dmod_par = cms.double(9999),
            chi2n_par = cms.double(1.2),
            copyExtras = cms.untracked.bool(True),
            copyTrajectories = cms.untracked.bool(False),
            d0_par1 = cms.vdouble(0.6, 4.0),
            d0_par2 = cms.vdouble(0.45, 4.0),
            dz_par1 = cms.vdouble(0.7, 4.0),
            dz_par2 = cms.vdouble(0.55, 4.0),
            keepAllTracks = cms.bool(True),
            maxNumberLostLayers = cms.uint32(2),
            max_d0 = cms.double(100.0),
            max_eta = cms.double(9999.0),
            max_lostHitFraction = cms.double(1.0),
            max_minMissHitOutOrIn = cms.int32(99),
            max_relpterr = cms.double(9999.0),
            max_z0 = cms.double(100.0),
            minHitsToBypassChecks = cms.uint32(20),
            minNumber3DLayers = cms.uint32(3),
            minNumberLayers = cms.uint32(3),
            min_eta = cms.double(-9999.0),
            min_nhits = cms.uint32(0),
            nSigmaZ = cms.double(4.0),
            name = cms.string('L1StepCut'),
            preFilterName = cms.string('L1StepTight'),
            qualityBit = cms.string('highPurity'),
            res_par = cms.vdouble(0.003, 0.001),
            vertexCut = cms.string('ndof>=2&!isFake'),
            vtxNumber = cms.int32(-1)
        )
    ),
    useVertices = cms.bool(True),
    useVtxError = cms.bool(False),
    vertices = cms.InputTag("hltPhase2PixelVertices")
)

hltPhase2L1TracksCutClassifier = cms.EDProducer( "TrackCutClassifier",
    src = cms.InputTag( "hltPhase2L1CtfTracks" ),
    beamspot = cms.InputTag( "offlineBeamSpot" ),
    vertices = cms.InputTag( "hltPhase2PixelVertices" ), # pixelVertices previous hltPhase2FirstStepPrimaryVertices" ),
    qualityCuts = cms.vdouble( -0.7, 0.1, 0.7 ),
    mva = cms.PSet(
	minPixelHits = cms.vint32(0,0,3), ######
	maxDzWrtBS = cms.vdouble( 3.40282346639E38, 24.0, 15.0 ),
	dr_par = cms.PSet(
	  d0err = cms.vdouble( 0.003, 0.003, 0.003 ),
	  dr_par1 = cms.vdouble( 0.8, 0.7, 0.6 ),
	  dr_par2 = cms.vdouble( 0.6, 0.5, 0.45 ),
	  dr_exp = cms.vint32( 4, 4, 4 ),
	  d0err_par = cms.vdouble( 0.001, 0.001, 0.001 )
	),
	maxLostLayers = cms.vint32( 3, 2, 2 ),
	min3DLayers = cms.vint32( 3, 3, 3),
	dz_par = cms.PSet(
	  dz_par1 = cms.vdouble( 0.9, 0.8, 0.7 ),
	  dz_par2 = cms.vdouble( 0.8, 0.7, 0.55 ),
	  dz_exp = cms.vint32( 4, 4, 4 )
	),
	minNVtxTrk = cms.int32( 3 ), # offline 2, online 3 switching to 3
	maxDz = cms.vdouble( 0.5, 0.2, 3.40282346639E38 ), ##
	minNdof = cms.vdouble( 1.0E-5, 1.0E-5, 1.0E-5 ), ##
	maxChi2 = cms.vdouble( 9999.0, 25.0, 16.0 ),
	maxChi2n = cms.vdouble( 2.0, 1.4, 1.2),
	maxDr = cms.vdouble( 0.5, 0.03, 3.40282346639E38 ), ##
	minLayers = cms.vint32( 3, 3, 3 ) ##
    ),
    ignoreVertices = cms.bool( True )
)

hltPhase2InitialStepClusters = cms.EDProducer("TrackClusterRemoverPhase2",
    TrackQuality = cms.string('highPurity'),
    maxChi2 = cms.double(9.0),
    mightGet = cms.optional.untracked.vstring, # cmssw_11_1
    minNumberOfLayersWithMeasBeforeFiltering = cms.int32(0),
    oldClusterRemovalInfo = cms.InputTag(""),
    #overrideTrkQuals = cms.InputTag("initialStepSelector","initialStep"),
    overrideTrkQuals = cms.InputTag(""), # trackcutclassifier
    phase2OTClusters = cms.InputTag("siPhase2Clusters"),
    phase2pixelClusters = cms.InputTag("siPixelClusters"),
    trackClassifier = cms.InputTag("","QualityMasks"),
    trajectories = cms.InputTag("hltPhase2L1CtfTracks")
)

######### pixelCPE to be added

############## pixelTracks/Vertices

hltPhase2PixelTrackClusters = cms.EDProducer("TrackClusterRemoverPhase2",
        TrackQuality = cms.string(' '),
        maxChi2 = cms.double(9.0),
        mightGet = cms.optional.untracked.vstring, # cmssw_11_1
        minNumberOfLayersWithMeasBeforeFiltering = cms.int32(0),
        oldClusterRemovalInfo = cms.InputTag(""),
        #overrideTrkQuals = cms.InputTag("initialStepSelector","initialStep"),
        overrideTrkQuals = cms.InputTag(""), # trackcutclassifier
        phase2OTClusters = cms.InputTag("siPhase2Clusters"),
        phase2pixelClusters = cms.InputTag("siPixelClusters"),
        trackClassifier = cms.InputTag("","QualityMasks"),
        trajectories = cms.InputTag("hltPhase2L1CtfTracks")
    )



hltPhase2PixelTracksHitSeeds = cms.EDProducer( "CAHitQuadrupletEDProducer",
    CAHardPtCut = cms.double( 0.5 ), #hevjin 0.0
    SeedComparitorPSet = cms.PSet(
      clusterShapeHitFilter = cms.string( "ClusterShapeHitFilter" ),
      ComponentName = cms.string( "LowPtClusterShapeSeedComparitor" ),
      clusterShapeCacheSrc = cms.InputTag( "siPixelClusterShapeCache") # pixelVertices
    ),
    extraHitRPhitolerance = cms.double( 0.032 ),
    doublets = cms.InputTag( "hltPhase2PixelTracksHitDoublets" ),
    fitFastCircle = cms.bool( True ),
    CAThetaCut = cms.double( 0.0012 ), # 0.002 ),
    maxChi2 = cms.PSet(
      value2 = cms.double( 50.0 ),
      value1 = cms.double( 200.0 ),
      pt1 = cms.double( 0.7 ),
      enabled = cms.bool( True ),
      pt2 = cms.double( 2.0 )
    ),
    CAPhiCut = cms.double( 0.2 ),
    useBendingCorrection = cms.bool( True ),
    fitFastCircleChi2Cut = cms.bool( True )#,
)

layerListForPhase2Hevjin = ['BPix1+BPix2+BPix3+BPix4',
'BPix1+BPix2+BPix3+FPix1_pos',
'BPix1+BPix2+BPix3+FPix1_neg',
'BPix1+BPix2+FPix1_pos+FPix2_pos',
'BPix1+BPix2+FPix1_neg+FPix2_neg',
'BPix1+FPix1_pos+FPix2_pos+FPix3_pos',
'BPix1+FPix1_neg+FPix2_neg+FPix3_neg',
'FPix1_pos+FPix2_pos+FPix3_pos+FPix4_pos',
'FPix1_neg+FPix2_neg+FPix3_neg+FPix4_neg',
'FPix2_pos+FPix3_pos+FPix4_pos+FPix5_pos',
'FPix2_neg+FPix3_neg+FPix4_neg+FPix5_neg',
'FPix3_pos+FPix4_pos+FPix5_pos+FPix6_pos',
'FPix3_neg+FPix4_neg+FPix5_neg+FPix6_neg',
'FPix4_pos+FPix5_pos+FPix6_pos+FPix7_pos',
'FPix4_neg+FPix5_neg+FPix6_neg+FPix7_neg',
'FPix5_pos+FPix6_pos+FPix7_pos+FPix8_pos',
'FPix5_neg+FPix6_neg+FPix7_neg+FPix8_neg']

hltPhase2PixelTrackCleanerBySharedHits = cms.ESProducer( "PixelTrackCleanerBySharedHitsESProducer",
  useQuadrupletAlgo = cms.bool( False ),
  ComponentName = cms.string( "hltPhase2PixelTrackCleanerBySharedHits" ),
  appendToDataLabel = cms.string( "" )
)

hltPhase2PixelTrackFilterByKinematics = cms.EDProducer( "PixelTrackFilterByKinematicsProducer",
    nSigmaTipMaxTolerance = cms.double( 0.0 ),
    chi2 = cms.double( 1000.0 ),
    nSigmaInvPtTolerance = cms.double( 0.0 ),
    ptMin = cms.double( 0.9 ), #previous 0.1
    tipMax = cms.double( 1.0 )
)

hltPhase2PixelFitterByHelixProjections = cms.EDProducer( "PixelFitterByHelixProjectionsProducer",
    scaleErrorsForBPix1 = cms.bool( False ),
    scaleFactor = cms.double( 0.65 )
)

hltPhase2PixelTracksHitQuadruplets = cms.EDProducer( "CAHitQuadrupletEDProducer",
    CAHardPtCut = cms.double( 0.0 ),
    SeedComparitorPSet = cms.PSet(
      clusterShapeHitFilter = cms.string( "ClusterShapeHitFilter" ),
      ComponentName = cms.string( "LowPtClusterShapeSeedComparitor" ),
      clusterShapeCacheSrc = cms.InputTag( "siPixelClusterShapeCache") # pixelVertices
    ),
    extraHitRPhitolerance = cms.double( 0.032 ),
    doublets = cms.InputTag( "hltPhase2PixelTracksHitDoublets" ),
    fitFastCircle = cms.bool( True ),
    CAThetaCut = cms.double( 0.0012 ), # 0.002 ),
    maxChi2 = cms.PSet(
      value2 = cms.double( 50.0 ),
      value1 = cms.double( 200.0 ),
      pt1 = cms.double( 0.7 ),
      enabled = cms.bool( True ),
      pt2 = cms.double( 2.0 )
    ),
    CAPhiCut = cms.double( 0.2 ),
    useBendingCorrection = cms.bool( True ),
    fitFastCircleChi2Cut = cms.bool( True )#,
)

hltPhase2PixelTracksHitSeeds = hltPhase2PixelTracksHitQuadruplets.clone()

hltPhase2PixelTracksSeedLayers = cms.EDProducer( "SeedingLayersEDProducer",
    layerList = cms.vstring(
        'BPix1+BPix2+BPix3+BPix4',
        'BPix1+BPix2+BPix3+FPix1_pos',
        'BPix1+BPix2+BPix3+FPix1_neg',
        'BPix1+BPix2+FPix1_pos+FPix2_pos',
        'BPix1+BPix2+FPix1_neg+FPix2_neg',
        'BPix1+FPix1_pos+FPix2_pos+FPix3_pos',
        'BPix1+FPix1_neg+FPix2_neg+FPix3_neg',
        'FPix1_pos+FPix2_pos+FPix3_pos+FPix4_pos',
        'FPix1_neg+FPix2_neg+FPix3_neg+FPix4_neg',
        'FPix2_pos+FPix3_pos+FPix4_pos+FPix5_pos',
        'FPix2_neg+FPix3_neg+FPix4_neg+FPix5_neg',
        'FPix3_pos+FPix4_pos+FPix5_pos+FPix6_pos',
        'FPix3_neg+FPix4_neg+FPix5_neg+FPix6_neg',
        'FPix4_pos+FPix5_pos+FPix6_pos+FPix7_pos',
        'FPix4_neg+FPix5_neg+FPix6_neg+FPix7_neg',
        'FPix5_pos+FPix6_pos+FPix7_pos+FPix8_pos',
        'FPix5_neg+FPix6_neg+FPix7_neg+FPix8_neg'
#      'BPix1+BPix2+BPix3+BPix4',
#      'BPix1+BPix2+BPix3+FPix1_pos',
#      'BPix1+BPix2+BPix3+FPix1_neg',
#      'BPix1+BPix2+FPix1_pos+FPix2_pos',
#      'BPix1+BPix2+FPix1_neg+FPix2_neg',
#      'BPix1+FPix1_pos+FPix2_pos+FPix3_pos',
#      'BPix1+FPix1_neg+FPix2_neg+FPix3_neg'
    ),
    MTOB = cms.PSet(  ),
    TEC = cms.PSet(  ),
    MTID = cms.PSet(  ),
    FPix = cms.PSet(
        HitProducer = cms.string('siPixelRecHits'), #PreSplitting'),
        TTRHBuilder = cms.string('WithTrackAngle')
#      hitErrorRPhi = cms.double( 0.0051 ),
#      TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
#      useErrorsFromParam = cms.bool( True ),
#      hitErrorRZ = cms.double( 0.0036 ),
#      HitProducer = cms.string( "hltSiPixelRecHits" )
    ),
    MTEC = cms.PSet(  ),
    MTIB = cms.PSet(  ),
    TID = cms.PSet(  ),
    TOB = cms.PSet(  ),
    BPix = cms.PSet(
        HitProducer = cms.string('siPixelRecHits'), #PreSplitting'),
        TTRHBuilder = cms.string('WithTrackAngle')
#      hitErrorRPhi = cms.double( 0.0027 ),
#      TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
#      useErrorsFromParam = cms.bool( True ),
#      hitErrorRZ = cms.double( 0.006 ),
#      HitProducer = cms.string( "hltSiPixelRecHits" )
    ),
    TIB = cms.PSet(  ),
    mightGet = cms.optional.untracked.vstring
)

hltPhase2PixelTracksTrackingRegions = cms.EDProducer( "GlobalTrackingRegionFromBeamSpotEDProducer",
    RegionPSet = cms.PSet(
      nSigmaZ = cms.double( 4.0 ),
      beamSpot = cms.InputTag( "offlineBeamSpot" ),
      ptMin = cms.double( 0.9 ), # previous 0.8
      originRadius = cms.double( 0.02 ),
      precise = cms.bool( True )
    )
)

hltPhase2TrimmedVertexTrackingRegions = cms.EDProducer( "GlobalTrackingRegionWithVerticesEDProducer",
    RegionPSet = cms.PSet(
      useFixedError = cms.bool( True ),
      nSigmaZ = cms.double( 5.0 ),
      VertexCollection = cms.InputTag( "hltPhase2TrimmedPixelVertices" ), # hltPhase2TrimmedPixelVertices
      beamSpot = cms.InputTag( "offlineBeamSpot" ),
      useFoundVertices = cms.bool( True ),
      fixedError = cms.double( 0.6 ),
      sigmaZVertex = cms.double( 3.0 ),
      useFakeVertices = cms.bool( False ),
      ptMin = cms.double( 0.9 ), # previous 0.4
      originRadius = cms.double( 0.05 ), # previous 0.05
      precise = cms.bool( True ),
      useMultipleScattering = cms.bool( False )
    ),
    mightGet = cms.optional.untracked.vstring  # cmssw_11_1
)


hltPhase2PixelTracksHitDoublets = cms.EDProducer( "HitPairEDProducer",
    trackingRegions = cms.InputTag( "hltPhase2PixelTracksTrackingRegions" ),
    layerPairs = cms.vuint32( 0, 1, 2 ),
    clusterCheck = cms.InputTag("trackerClusterCheck"),
    produceSeedingHitSets = cms.bool( False ),
    produceIntermediateHitDoublets = cms.bool( True ),
    trackingRegionsSeedingLayers = cms.InputTag( "" ),
    maxElementTotal = cms.uint32( 50000000 ),
    maxElement = cms.uint32(50000000), # 0 ),
    seedingLayers = cms.InputTag( "hltPhase2PixelTracksSeedLayers" )
)

hltPhase2PixelTracks = cms.EDProducer("PixelTrackProducer",
    Cleaner = cms.string('hltPhase2PixelTrackCleanerBySharedHits'),
    passLabel = cms.string('hltPhase2PixelTracks'),
    Filter = cms.InputTag("hltPhase2PixelTrackFilterByKinematics"),
    Fitter = cms.InputTag("hltPhase2PixelFitterByHelixProjections"),
    SeedingHitSets = cms.InputTag("hltPhase2PixelTracksHitSeeds"),
    mightGet = cms.untracked.vstring("")#'RegionsSeedingHitSets_pixelTracksHitQuadruplets__RECO')
)

hltPhase2PixelVertices = cms.EDProducer( "PixelVertexProducer",
    WtAverage = cms.bool( True ),
    Method2 = cms.bool( True ),
    beamSpot = cms.InputTag( "offlineBeamSpot" ),
    PVcomparer = cms.PSet(  refToPSet_ = cms.string( "hltPhase2PSetPvClusterComparerForIT" ) ),
    Verbosity = cms.int32( 0 ),
    UseError = cms.bool( True ),
    TrackCollection = cms.InputTag( "hltPhase2PixelTracksClean" ),
    PtMin = cms.double( 2.0 ),
    NTrkMin = cms.int32( 2 ),
    ZOffset = cms.double( 5.0 ),
    Finder = cms.string( "DivisiveVertexFinder" ),
    ZSeparation = cms.double( 0.025 )
)

hltPhase2TrimmedPixelVertices = cms.EDProducer( "PixelVertexCollectionTrimmer",
    src = cms.InputTag( "hltPhase2PixelVertices" ),
    fractionSumPt2 = cms.double( 0.00000001 ),
    minSumPt2 = cms.double( -100.0 ),
    PVcomparer = cms.PSet(  refToPSet_ = cms.string( "hltPhase2PSetPvClusterComparerForIT" ) ),
    maxVtx = cms.uint32( 0 ) # > 200 # previous 100
)

#######

hltPhase2PixelTracksCutClassifier = cms.EDProducer( "TrackCutClassifier",
    src = cms.InputTag( "hltPhase2PixelTracks" ),
    beamspot = cms.InputTag( "offlineBeamSpot" ),
    vertices = cms.InputTag( "" ),
    qualityCuts = cms.vdouble( -0.7, 0.1, 0.7 ),
    mva = cms.PSet(
      minPixelHits = cms.vint32( 0, 3, 3 ),
      maxDzWrtBS = cms.vdouble( 3.40282346639E38, 3.40282346639E38, 60.0 ),
      dr_par = cms.PSet(
        d0err = cms.vdouble( 0.003, 0.003, 3.40282346639E38 ),
        dr_par2 = cms.vdouble( 0.3, 0.3, 3.40282346639E38 ),
        dr_par1 = cms.vdouble( 0.4, 0.4, 3.40282346639E38 ),
        dr_exp = cms.vint32( 4, 4, 4 ),
        d0err_par = cms.vdouble( 0.001, 0.001, 3.40282346639E38 )
      ),
      maxLostLayers = cms.vint32( 99, 99, 99 ),
      min3DLayers = cms.vint32( 0, 2, 3 ),
      dz_par = cms.PSet(
        dz_par1 = cms.vdouble( 0.4, 0.4, 3.40282346639E38 ),
        dz_par2 = cms.vdouble( 0.35, 0.35, 3.40282346639E38 ),
        dz_exp = cms.vint32( 4, 4, 4 )
      ),
      minNVtxTrk = cms.int32( 3 ),
      maxDz = cms.vdouble( 3.40282346639E38, 3.40282346639E38, 3.40282346639E38 ),
      minNdof = cms.vdouble( 1.0E-5, 1.0E-5, 1.0E-5 ),
      maxChi2 = cms.vdouble( 9999., 9999., 30.0 ),
      maxDr = cms.vdouble( 99., 99., 1. ),
      minLayers = cms.vint32( 0, 2, 3 )
    ),
    ignoreVertices = cms.bool( True ),
)

hltPhase2PixelTracksSelectionHighPurity = cms.EDProducer( "TrackCollectionFilterCloner",
    minQuality = cms.string( "highPurity" ),
    copyExtras = cms.untracked.bool( True ),
    copyTrajectories = cms.untracked.bool( False ),
    originalSource = cms.InputTag( "hltPhase2PixelTracks" ),
    originalQualVals = cms.InputTag( 'hltPhase2PixelTracksCutClassifier','QualityMasks' ),
    originalMVAVals = cms.InputTag( 'hltPhase2PixelTracksCutClassifier','MVAValues' )
)

#######

##########################
hltPhase2VertexMerger = cms.EDProducer("VertexMerger",
    maxFraction = cms.double(0.7),
    minSignificance = cms.double(2),
    secondaryVertices = cms.InputTag("hltPhase2InclusiveVertexFinder")
)

hltPhase2OfflinePrimaryVertices = cms.EDProducer("RecoChargedRefCandidatePrimaryVertexSorter",
    assignment = cms.PSet(
        DzCutForChargedFromPUVtxs = cms.double(0.2),
        EtaMinUseDz = cms.double(-1),
        NumOfPUVtxsForCharged = cms.uint32(0),
        OnlyUseFirstDz = cms.bool(False),
        PtMaxCharged = cms.double(-1),
        maxDistanceToJetAxis = cms.double(0.07),
        maxDtSigForPrimaryAssignment = cms.double(4.0),
        maxDxyForJetAxisAssigment = cms.double(0.1),
        maxDxyForNotReconstructedPrimary = cms.double(0.01),
        maxDxySigForNotReconstructedPrimary = cms.double(2),
        maxDzErrorForPrimaryAssignment = cms.double(0.05),
        maxDzForJetAxisAssigment = cms.double(0.1),
        maxDzForPrimaryAssignment = cms.double(0.1),
        maxDzSigForPrimaryAssignment = cms.double(5.0),
        maxJetDeltaR = cms.double(0.5),
        minJetPt = cms.double(25),
        preferHighRanked = cms.bool(False),
        useTiming = cms.bool(False),
        useVertexFit = cms.bool(True)
    ),
    jets = cms.InputTag("hltPhase2Ak4CaloJetsForTrk"),
    particles = cms.InputTag("hltPhase2TrackRefsForJetsBeforeSorting"),
    produceAssociationToOriginalVertices = cms.bool(False),
    produceNoPileUpCollection = cms.bool(False),
    producePileUpCollection = cms.bool(False),
    produceSortedVertices = cms.bool(True),
    qualityForPrimary = cms.int32(3),
    sorting = cms.PSet(

    ),
    trackTimeResoTag = cms.InputTag(""),
    trackTimeTag = cms.InputTag(""),
    usePVMET = cms.bool(True),
    vertices = cms.InputTag("hltPhase2UnsortedOfflinePrimaryVertices")
)

hltPhase2L1PrimaryVertex = cms.EDProducer("RecoChargedRefCandidatePrimaryVertexSorter",
    assignment = cms.PSet(
        DzCutForChargedFromPUVtxs = cms.double(0.2),
        EtaMinUseDz = cms.double(-1),
        NumOfPUVtxsForCharged = cms.int32(0),
        OnlyUseFirstDz = cms.bool(False),
        PtMaxCharged = cms.double(-1),
        maxDistanceToJetAxis = cms.double(0.07),
        maxDtSigForPrimaryAssignment = cms.double(4.0),
        maxDxyForJetAxisAssigment = cms.double(0.1),
        maxDxyForNotReconstructedPrimary = cms.double(0.01),
        maxDxySigForNotReconstructedPrimary = cms.double(2),
        maxDzErrorForPrimaryAssignment = cms.double(0.05),
        maxDzForJetAxisAssigment = cms.double(0.1),
        maxDzForPrimaryAssignment = cms.double(0.1),
        maxDzSigForPrimaryAssignment = cms.double(5.0),
        maxJetDeltaR = cms.double(0.5),
        minJetPt = cms.double(25),
        preferHighRanked = cms.bool(False),
        useTiming = cms.bool(False),
        useVertexFit = cms.bool(True)
    ),
    jets = cms.InputTag("hltPhase2Ak4CaloJetsForTrkL1"),
    particles = cms.InputTag("hltPhase2TrackRefsForJetsBeforeSortingL1"),
    produceAssociationToOriginalVertices = cms.bool(False),
    produceNoPileUpCollection = cms.bool(False),
    producePileUpCollection = cms.bool(False),
    produceSortedVertices = cms.bool(True),
    qualityForPrimary = cms.int32(3),
    sorting = cms.PSet(

    ),
    trackTimeResoTag = cms.InputTag(""),
    trackTimeTag = cms.InputTag(""),
    usePVMET = cms.bool(True),
    vertices = cms.InputTag("hltPhase2L1PrimaryVertexUnsorted")
)
hltPhase2OfflinePrimaryVerticesWithBS = cms.EDProducer("RecoChargedRefCandidatePrimaryVertexSorter",
    assignment = cms.PSet(
        DzCutForChargedFromPUVtxs = cms.double(0.2),
        EtaMinUseDz = cms.double(-1),
        NumOfPUVtxsForCharged = cms.uint32(0),
        OnlyUseFirstDz = cms.bool(False),
        PtMaxCharged = cms.double(-1),
        maxDistanceToJetAxis = cms.double(0.07),
        maxDtSigForPrimaryAssignment = cms.double(4.0),
        maxDxyForJetAxisAssigment = cms.double(0.1),
        maxDxyForNotReconstructedPrimary = cms.double(0.01),
        maxDxySigForNotReconstructedPrimary = cms.double(2),
        maxDzErrorForPrimaryAssignment = cms.double(0.05),
        maxDzForJetAxisAssigment = cms.double(0.1),
        maxDzForPrimaryAssignment = cms.double(0.1),
        maxDzSigForPrimaryAssignment = cms.double(5.0),
        maxJetDeltaR = cms.double(0.5),
        minJetPt = cms.double(25),
        preferHighRanked = cms.bool(False),
        useTiming = cms.bool(False),
        useVertexFit = cms.bool(True)
    ),
    jets = cms.InputTag("hltPhase2Ak4CaloJetsForTrk"),
    particles = cms.InputTag("hltPhase2TrackRefsForJetsBeforeSorting"),
    produceAssociationToOriginalVertices = cms.bool(False),
    produceNoPileUpCollection = cms.bool(False),
    producePileUpCollection = cms.bool(False),
    produceSortedVertices = cms.bool(True),
    qualityForPrimary = cms.int32(3),
    sorting = cms.PSet(

    ),
    trackTimeResoTag = cms.InputTag(""),
    trackTimeTag = cms.InputTag(""),
    usePVMET = cms.bool(True),
    vertices = cms.InputTag("hltPhase2UnsortedOfflinePrimaryVertices","WithBS")
)

hltPhase2InclusiveSecondaryVertices = cms.EDProducer("VertexMerger",
    maxFraction = cms.double(0.2),
    minSignificance = cms.double(10.0),
    secondaryVertices = cms.InputTag("hltPhase2TrackVertexArbitrator")
)

hltPhase2TrackRefsForJetsBeforeSorting = cms.EDProducer("ChargedRefCandidateProducer",
    particleType = cms.string('pi+'),
    src = cms.InputTag("hltPhase2TrackWithVertexRefSelectorBeforeSorting")
)

hltPhase2TrackRefsForJetsBeforeSortingL1 = cms.EDProducer("ChargedRefCandidateProducer",
    particleType = cms.string('pi+'),
    src = cms.InputTag("hltPhase2TrackWithVertexRefSelectorBeforeSortingL1")
)

hltPhase2Ak4CaloJetsForTrk = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(1),
    GhostArea = cms.double(0.01),
    Ghost_EtaMax = cms.double(5.0),
    Rho_EtaMax = cms.double(4.4),
    doAreaDiskApprox = cms.bool(False),
    doAreaFastjet = cms.bool(False),
    doPUOffsetCorr = cms.bool(False),
    doPVCorrection = cms.bool(True),
    doRhoFastjet = cms.bool(False),
    inputEMin = cms.double(0.0),
    inputEtMin = cms.double(0.3),
    jetAlgorithm = cms.string('AntiKt'),
    jetPtMin = cms.double(10.0),
    jetType = cms.string('CaloJet'),
    maxBadEcalCells = cms.uint32(9999999),
    maxBadHcalCells = cms.uint32(9999999),
    maxProblematicEcalCells = cms.uint32(9999999),
    maxProblematicHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    maxRecoveredHcalCells = cms.uint32(9999999),
    minSeed = cms.uint32(14327),
    nSigmaPU = cms.double(1.0),
    puPtMin = cms.double(10),
    rParam = cms.double(0.4),
    radiusPU = cms.double(0.5),
    src = cms.InputTag("caloTowerForTrk"),
    srcPVs = cms.InputTag("hltPhase2UnsortedOfflinePrimaryVertices"),
    useDeterministicSeed = cms.bool(True),
    voronoiRfact = cms.double(-0.9)
)

hltPhase2Ak4CaloJetsForTrkL1 = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(1),
    GhostArea = cms.double(0.01),
    Ghost_EtaMax = cms.double(5.0),
    Rho_EtaMax = cms.double(4.4),
    doAreaDiskApprox = cms.bool(False),
    doAreaFastjet = cms.bool(False),
    doPUOffsetCorr = cms.bool(False),
    doPVCorrection = cms.bool(True),
    doRhoFastjet = cms.bool(False),
    inputEMin = cms.double(0.0),
    inputEtMin = cms.double(0.3),
    jetAlgorithm = cms.string('AntiKt'),
    jetPtMin = cms.double(10.0),
    jetType = cms.string('CaloJet'),
    maxBadEcalCells = cms.uint32(9999999),
    maxBadHcalCells = cms.uint32(9999999),
    maxProblematicEcalCells = cms.uint32(9999999),
    maxProblematicHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    maxRecoveredHcalCells = cms.uint32(9999999),
    minSeed = cms.uint32(14327),
    nSigmaPU = cms.double(1.0),
    puPtMin = cms.double(10),
    rParam = cms.double(0.4),
    radiusPU = cms.double(0.5),
    src = cms.InputTag("caloTowerForTrk"),
    srcPVs = cms.InputTag("hltPhase2L1PrimaryVertexUnsorted"),
    useDeterministicSeed = cms.bool(True),
    voronoiRfact = cms.double(-0.9)
)
hltPhase2InclusiveVertexFinder = cms.EDProducer("InclusiveVertexFinder",
    beamSpot = cms.InputTag("offlineBeamSpot"),
    clusterizer = cms.PSet(
        clusterMaxDistance = cms.double(0.05),
        clusterMaxSignificance = cms.double(4.5),
        clusterMinAngleCosine = cms.double(0.5),
        distanceRatio = cms.double(20),
        maxTimeSignificance = cms.double(3.5),
        seedMax3DIPSignificance = cms.double(9999),
        seedMax3DIPValue = cms.double(9999),
        seedMin3DIPSignificance = cms.double(1.2),
        seedMin3DIPValue = cms.double(0.005)
    ),
    fitterRatio = cms.double(0.25),
    fitterSigmacut = cms.double(3),
    fitterTini = cms.double(256),
    maxNTracks = cms.uint32(30),
    maximumLongitudinalImpactParameter = cms.double(0.3),
    maximumTimeSignificance = cms.double(3),
    minHits = cms.uint32(8),
    minPt = cms.double(0.9), # ptcut previous 0.8
    primaryVertices = cms.InputTag("hltPhase2OfflinePrimaryVertices"),
    tracks = cms.InputTag("hltPhase2GeneralTracks"), ## hltPhase2
    useDirectVertexFitter = cms.bool(True),
    useVertexReco = cms.bool(True),
    vertexMinAngleCosine = cms.double(0.95),
    vertexMinDLen2DSig = cms.double(2.5),
    vertexMinDLenSig = cms.double(0.5),
    vertexReco = cms.PSet(
        finder = cms.string('avr'),
        primcut = cms.double(1),
        seccut = cms.double(3),
        smoothing = cms.bool(True)
    )
)

hltPhase2TrackVertexArbitrator = cms.EDProducer("TrackVertexArbitrator",
    beamSpot = cms.InputTag("offlineBeamSpot"),
    dLenFraction = cms.double(0.333),
    dRCut = cms.double(0.4),
    distCut = cms.double(0.04),
    fitterRatio = cms.double(0.25),
    fitterSigmacut = cms.double(3),
    fitterTini = cms.double(256),
    maxTimeSignificance = cms.double(3.5),
    primaryVertices = cms.InputTag("hltPhase2OfflinePrimaryVertices"),
    secondaryVertices = cms.InputTag("hltPhase2VertexMerger"),
    sigCut = cms.double(5),
    trackMinLayers = cms.int32(4),
    trackMinPixels = cms.int32(1),
    trackMinPt = cms.double(0.9), # ptcut previous 0.4
    tracks = cms.InputTag("hltPhase2GeneralTracks") ## hltPhase2
)

hltPhase2TrackWithVertexRefSelectorBeforeSorting = cms.EDProducer("TrackWithVertexRefSelector",
    copyExtras = cms.untracked.bool(False),
    copyTrajectories = cms.untracked.bool(False),
    d0Max = cms.double(999.0),
    dzMax = cms.double(999.0),
    etaMax = cms.double(5.0),
    etaMin = cms.double(0.0),
    nSigmaDtVertex = cms.double(0),
    nVertices = cms.uint32(0),
    normalizedChi2 = cms.double(999999.0),
    numberOfLostHits = cms.uint32(999),
    numberOfValidHits = cms.uint32(0),
    numberOfValidPixelHits = cms.uint32(0),
    maxOfValidPixelHits = cms.uint32(999),

    ptErrorCut = cms.double(9e+99),
    ptMax = cms.double(9e+99),
    ptMin = cms.double(0.9), # ptcut previous 0.3
    quality = cms.string('highPurity'),
    rhoVtx = cms.double(0.2),
    src = cms.InputTag("hltPhase2GeneralTracks"), ## hltPhase2
    timeResosTag = cms.InputTag(""),
    timesTag = cms.InputTag(""),
    useVtx = cms.bool(True),
    vertexTag = cms.InputTag("hltPhase2UnsortedOfflinePrimaryVertices"),
    vtxFallback = cms.bool(True),
    zetaVtx = cms.double(1.0)
)


hltPhase2TrackWithVertexRefSelectorBeforeSortingL1 = cms.EDProducer("TrackWithVertexRefSelector",
    copyExtras = cms.untracked.bool(False),
    copyTrajectories = cms.untracked.bool(False),
    d0Max = cms.double(999.0),
    dzMax = cms.double(999.0),
    etaMax = cms.double(5.0),
    etaMin = cms.double(0.0),
    nSigmaDtVertex = cms.double(0),
    nVertices = cms.uint32(0),
    normalizedChi2 = cms.double(999999.0),
    numberOfLostHits = cms.uint32(999),
    numberOfValidHits = cms.uint32(0),
    numberOfValidPixelHits = cms.uint32(0),
    maxOfValidPixelHits = cms.uint32(999),

    ptErrorCut = cms.double(9e+99),
    ptMax = cms.double(9e+99),
    ptMin = cms.double(0.9), # ptcut previous 0.3
    quality = cms.string('highPurity'),
    rhoVtx = cms.double(0.2),
    src = cms.InputTag("hltPhase2L1CtfTracks"), ## hltPhase2
    timeResosTag = cms.InputTag(""),
    timesTag = cms.InputTag(""),
    useVtx = cms.bool(True),
    vertexTag = cms.InputTag("hltPhase2L1PrimaryVertexUnsorted"),
    vtxFallback = cms.bool(True),
    zetaVtx = cms.double(1.0)
)

hltPhase2L1PrimaryVertexUnsorted = cms.EDProducer("PrimaryVertexProducer",
    TkClusParameters = cms.PSet(
        TkDAClusParameters = cms.PSet(
            Tmin = cms.double(2.0),
            Tpurge = cms.double(2.0),
            Tstop = cms.double(0.5),
            coolingFactor = cms.double(0.6),
            d0CutOff = cms.double(3.0),
            dzCutOff = cms.double(3.0),
            uniquetrkweight = cms.double(0.8),
            vertexSize = cms.double(0.006),
            zmerge = cms.double(0.01)
        ),
        algorithm = cms.string('DA_vect')
    ),
    TkFilterParameters = cms.PSet(
        algorithm = cms.string('filter'),
        maxD0Significance = cms.double(4.0),
        maxEta = cms.double(4.0),
        maxNormalizedChi2 = cms.double(10.0),
        minPixelLayersWithHits = cms.int32(2),
        minPt = cms.double(0.9), # ptcut previous 0.0
        minSiliconLayersWithHits = cms.int32(5),
        trackQuality = cms.string('any')
    ),
    TrackLabel = cms.InputTag("hltPhase2L1CtfTracks"), ## hltPhase2
    beamSpotLabel = cms.InputTag("offlineBeamSpot"),
    verbose = cms.untracked.bool(False),
    vertexCollections = cms.VPSet(
        cms.PSet(
            algorithm = cms.string('AdaptiveVertexFitter'),
            chi2cutoff = cms.double(2.5),
            label = cms.string(''),
            maxDistanceToBeam = cms.double(1.0),
            minNdof = cms.double(0.0),
            useBeamConstraint = cms.bool(False)
        ),
        cms.PSet(
            algorithm = cms.string('AdaptiveVertexFitter'),
            chi2cutoff = cms.double(2.5),
            label = cms.string('WithBS'),
            maxDistanceToBeam = cms.double(1.0),
            minNdof = cms.double(2.0),
            useBeamConstraint = cms.bool(True)
        )
    )
)

hltPhase2UnsortedOfflinePrimaryVertices = cms.EDProducer("PrimaryVertexProducer",
    TkClusParameters = cms.PSet(
        TkDAClusParameters = cms.PSet(
            Tmin = cms.double(2.0),
            Tpurge = cms.double(2.0),
            Tstop = cms.double(0.5),
            coolingFactor = cms.double(0.6),
            d0CutOff = cms.double(3.0),
            dzCutOff = cms.double(3.0),
            uniquetrkweight = cms.double(0.8),
            vertexSize = cms.double(0.006),
            zmerge = cms.double(0.01)
        ),
        algorithm = cms.string('DA_vect')
    ),
    TkFilterParameters = cms.PSet(
        algorithm = cms.string('filter'),
        maxD0Significance = cms.double(4.0),
        maxEta = cms.double(4.0),
        maxNormalizedChi2 = cms.double(10.0),
        minPixelLayersWithHits = cms.int32(2),
        minPt = cms.double(0.9), # ptcut previous 0.0
        minSiliconLayersWithHits = cms.int32(5),
        trackQuality = cms.string('any')
    ),
    TrackLabel = cms.InputTag("hltPhase2GeneralTracks"), ## hltPhase2
    beamSpotLabel = cms.InputTag("offlineBeamSpot"),
    verbose = cms.untracked.bool(False),
    vertexCollections = cms.VPSet(
        cms.PSet(
            algorithm = cms.string('AdaptiveVertexFitter'),
            chi2cutoff = cms.double(2.5),
            label = cms.string(''),
            maxDistanceToBeam = cms.double(1.0),
            minNdof = cms.double(0.0),
            useBeamConstraint = cms.bool(False)
        ),
        cms.PSet(
            algorithm = cms.string('AdaptiveVertexFitter'),
            chi2cutoff = cms.double(2.5),
            label = cms.string('WithBS'),
            maxDistanceToBeam = cms.double(1.0),
            minNdof = cms.double(2.0),
            useBeamConstraint = cms.bool(True)
        )
    )
)

hltPhase2FirstStepPrimaryVerticesUnsorted = cms.EDProducer("PrimaryVertexProducer",
    TkClusParameters = cms.PSet(
        TkDAClusParameters = cms.PSet(
            Tmin = cms.double(2.0),
            Tpurge = cms.double(2.0),
            Tstop = cms.double(0.5),
            coolingFactor = cms.double(0.6),
            d0CutOff = cms.double(3.0),
            dzCutOff = cms.double(3.0),
            uniquetrkweight = cms.double(0.8),
            vertexSize = cms.double(0.006),
            zmerge = cms.double(0.01)
        ),
        algorithm = cms.string('DA_vect')
    ),
    TkFilterParameters = cms.PSet(
        algorithm = cms.string('filter'),
        maxD0Significance = cms.double(4.0),
        maxEta = cms.double(4.0),
        maxNormalizedChi2 = cms.double(10.0),
        minPixelLayersWithHits = cms.int32(2),
        minPt = cms.double(0.9), # ptcut previous 0.0
        minSiliconLayersWithHits = cms.int32(5),
        trackQuality = cms.string('any')
    ),
    TrackLabel = cms.InputTag("hltPhase2InitialStepTracks"), ## hltPhase2
    beamSpotLabel = cms.InputTag("offlineBeamSpot"),
    verbose = cms.untracked.bool(False),
    vertexCollections = cms.VPSet(cms.PSet(
        algorithm = cms.string('AdaptiveVertexFitter'),
        chi2cutoff = cms.double(2.5),
        label = cms.string(''),
        maxDistanceToBeam = cms.double(1.0),
        minNdof = cms.double(0.0),
        useBeamConstraint = cms.bool(False)
    ))
)

hltPhase2FirstStepPrimaryVertices = cms.EDProducer("RecoChargedRefCandidatePrimaryVertexSorter",
    assignment = cms.PSet(
        maxDistanceToJetAxis = cms.double(0.07),
        maxDtSigForPrimaryAssignment = cms.double(4.0),
        maxDxyForJetAxisAssigment = cms.double(0.1),
        maxDxyForNotReconstructedPrimary = cms.double(0.01),
        maxDxySigForNotReconstructedPrimary = cms.double(2),
        maxDzErrorForPrimaryAssignment = cms.double(0.05),
        maxDzForJetAxisAssigment = cms.double(0.1),
        maxDzForPrimaryAssignment = cms.double(0.1),
        maxDzSigForPrimaryAssignment = cms.double(5.0),
        maxJetDeltaR = cms.double(0.5),
        minJetPt = cms.double(25),
        preferHighRanked = cms.bool(False),
        useTiming = cms.bool(False)
    ),
    jets = cms.InputTag("hltPhase2Ak4CaloJetsForTrk"),
    particles = cms.InputTag("hltPhase2InitialStepTrackRefsForJets"),  ## hltPhase2
    produceAssociationToOriginalVertices = cms.bool(False),
    produceNoPileUpCollection = cms.bool(False),
    producePileUpCollection = cms.bool(False),
    produceSortedVertices = cms.bool(True),
    qualityForPrimary = cms.int32(3),
    sorting = cms.PSet(

    ),
    trackTimeResoTag = cms.InputTag(""),
    trackTimeTag = cms.InputTag(""),
    usePVMET = cms.bool(True),
    vertices = cms.InputTag("hltPhase2FirstStepPrimaryVerticesUnsorted")
)

####

trackAlgoPriorityOrderL1Initial = cms.ESProducer("TrackAlgoPriorityOrderESProducer",
    ComponentName = cms.string('trackAlgoPriorityOrderL1Initial'),
    algoOrder = cms.vstring(
        'hltIter0',
        'initialStep'### v2
    ),
    appendToDataLabel = cms.string('')
)

hltPhase2TrackAlgoPriorityOrder = cms.ESProducer("TrackAlgoPriorityOrderESProducer",
    ComponentName = cms.string('hltPhase2TrackAlgoPriorityOrder'),
    algoOrder = cms.vstring(
        'initialStep',
        'highPtTripletStep'### v2
    ),
    appendToDataLabel = cms.string('')
)

hltPhase2GeneralTracks = cms.EDProducer("TrackListMerger",
    Epsilon = cms.double(-0.001),
    FoundHitBonus = cms.double(5.0),
    LostHitPenalty = cms.double(5.0),
    MaxNormalizedChisq = cms.double(1000.0),
    MinFound = cms.int32(3),
    MinPT = cms.double(0.9), # ptcut previous 0.05
    ShareFrac = cms.double(0.2),
    TrackProducers = cms.VInputTag(
        #"hltPhase2InitialStepTracks", "hltPhase2HighPtTripletStepTracks" ### v2
	"hltPhase2InitialStepTracksSelectionHighPurity", "hltPhase2HighPtTripletStepTracksSelectionHighPurity" ### v2 # trackcutclassifier
    ),
    allowFirstHitShare = cms.bool(False),
    copyExtras = cms.untracked.bool(True),
    copyMVA = cms.bool(False), # trackcutclassifier before True
    hasSelector = cms.vint32(
        0, 0#, 1#, 1, 1,  ### v2 # trackcutclassifier
        #1
    ),
    indivShareFrac = cms.vdouble(
        #1.0, 0.16#, 0.095, 0.09, 0.09, ### v2
        ##0.09
	1.0, 1.0 # trackcutclassifier
    ),
    makeReKeyedSeeds = cms.untracked.bool(False),
    newQuality = cms.string('confirmed'),
    selectedTrackQuals = cms.VInputTag(
        #cms.InputTag("initialStepSelector","initialStep"), cms.InputTag("highPtTripletStepSelector","highPtTripletStep")### v2
	cms.InputTag("hltPhase2InitialStepTracksSelectionHighPurity"), cms.InputTag("hltPhase2HighPtTripletStepTracksSelectionHighPurity") # trackcutclassifier

    ),
    setsToMerge = cms.VPSet(cms.PSet(
        pQual = cms.bool(True),
        tLists = cms.vint32(
            0, 1#, 2#, 3, 4, ### v2
            #5
        )
    )),
    trackAlgoPriorityOrder = cms.string('hltPhase2TrackAlgoPriorityOrder'),
    writeOnlyTrkQuals = cms.bool(False)
)

hltPhase2PixelTracksMerger = cms.EDProducer("TrackListMerger",
    Epsilon = cms.double(-0.001),
    FoundHitBonus = cms.double(5.0),
    LostHitPenalty = cms.double(5.0),
    MaxNormalizedChisq = cms.double(1000.0),
    MinFound = cms.int32(3),
    MinPT = cms.double(0.9), # ptcut previous 0.05
    ShareFrac = cms.double(0.19),
    TrackProducers = cms.VInputTag( 
     cms.InputTag("hltPhase2PixelTracksCleaner"),
cms.InputTag("hltPhase2PixelTripletsCleaner")

    ),
    allowFirstHitShare = cms.bool(True),
    copyExtras = cms.untracked.bool(True),
    copyMVA = cms.bool(False), # trackcutclassifier before True
    hasSelector = cms.vint32(
        0, 0#, 1#, 1, 1,  ### v2 # trackcutclassifier 
    ),
    indivShareFrac = cms.vdouble( 
        1.0, 1.0 # trackcutclassifier
    ),
    makeReKeyedSeeds = cms.untracked.bool(False),
    newQuality = cms.string('confirmed'),
    selectedTrackQuals = cms.VInputTag(
      cms.InputTag("hltPhase2PixelTracksCleaner"),
cms.InputTag("hltPhase2PixelTripletsCleaner") 
    ),
    setsToMerge = cms.VPSet(cms.PSet(
        pQual = cms.bool(True),
        tLists = cms.vint32(
            0, 1#, 2#, 3, 4, ### v2
            #5
        )
    )),
    trackAlgoPriorityOrder = cms.string('hltPhase2TrackAlgoPriorityOrder'),
    writeOnlyTrkQuals = cms.bool(False)
)


hltPhase2L1InitialMerger = cms.EDProducer("TrackListMerger",
    Epsilon = cms.double(-0.001),
    FoundHitBonus = cms.double(5.0),
    LostHitPenalty = cms.double(5.0),
    MaxNormalizedChisq = cms.double(1000.0),
    MinFound = cms.int32(3),
    MinPT = cms.double(0.9), # ptcut previous 0.05
    ShareFrac = cms.double(0.19),
    TrackProducers = cms.VInputTag(
        	   "hltPhase2L1CtfTracks","hltPhase2InitialStepTracksSelectionHighPurity"
            ),
    allowFirstHitShare = cms.bool(True),
    copyExtras = cms.untracked.bool(True),
    copyMVA = cms.bool(False), # trackcutclassifier before True
    hasSelector = cms.vint32(
        0, 0#, 1#, 1, 1,  ### v2 # trackcutclassifier
        #1
    ),
    indivShareFrac = cms.vdouble(
        #1.0, 0.16#, 0.095, 0.09, 0.09, ### v2
        ##0.09
	1.0, 1.0 # trackcutclassifier
    ),
    makeReKeyedSeeds = cms.untracked.bool(False),
    newQuality = cms.string('confirmed'),
    selectedTrackQuals = cms.VInputTag(
        #cms.InputTag("initialStepSelector","initialStep"), cms.InputTag("highPtTripletStepSelector","highPtTripletStep")### v2
    cms.InputTag(""),
    cms.InputTag("hltPhase2InitialStepTracksSelectionHighPurity")

    ),
    setsToMerge = cms.VPSet(cms.PSet(
        pQual = cms.bool(True),
        tLists = cms.vint32(
            0, 1#, 2#, 3, 4, ### v2
            #5
        )
    )),
    hltPhase2TrackAlgoPriorityOrder = cms.string('hltPhase2TrackAlgoPriorityOrderL1Initial'),
    writeOnlyTrkQuals = cms.bool(False)
)


########################################################################
########## highpttriplet

########## highpttriplet
hltPhase2HighPtTripletStepClusters = cms.EDProducer("TrackClusterRemoverPhase2",
    TrackQuality = cms.string('highPurity'),
    maxChi2 = cms.double(9.0),
    mightGet = cms.optional.untracked.vstring, # cmssw_11_1
    minNumberOfLayersWithMeasBeforeFiltering = cms.int32(0),
    oldClusterRemovalInfo = cms.InputTag(""),
    #overrideTrkQuals = cms.InputTag("initialStepSelector","initialStep"),
    overrideTrkQuals = cms.InputTag(""), # trackcutclassifier
    phase2OTClusters = cms.InputTag("siPhase2Clusters"),
    phase2pixelClusters = cms.InputTag("siPixelClusters"),
    trackClassifier = cms.InputTag("","QualityMasks"),
    trajectories = cms.InputTag("hltPhase2InitialStepTracksSelectionHighPurity")
)

hltPhase2HighPtTripletStepHitDoublets = cms.EDProducer("HitPairEDProducer",
    clusterCheck = cms.InputTag("trackerClusterCheck"),
    layerPairs = cms.vuint32(0, 1),
    maxElement = cms.uint32(50000000),
    maxElementTotal = cms.uint32(50000000),
    mightGet = cms.optional.untracked.vstring, # cmssw_11_1
    produceIntermediateHitDoublets = cms.bool(True),
    produceSeedingHitSets = cms.bool(False),
    seedingLayers = cms.InputTag("hltPhase2HighPtTripletStepSeedLayers"),
    trackingRegions = cms.InputTag("hltPhase2HighPtTripletStepTrackingRegions"),
    trackingRegionsSeedingLayers = cms.InputTag("")
)

hltPhase2HighPtTripletStepHitTriplets = cms.EDProducer("CAHitTripletEDProducer",
    CAHardPtCut = cms.double(0.5),
    CAPhiCut = cms.double(0.06),
    CAThetaCut = cms.double(0.003),
    SeedComparitorPSet = cms.PSet(
        ComponentName = cms.string('LowPtClusterShapeSeedComparitor'),
        clusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"),
        clusterShapeHitFilter = cms.string('ClusterShapeHitFilter')
    ),
    doublets = cms.InputTag("hltPhase2HighPtTripletStepHitDoublets"),
    extraHitRPhitolerance = cms.double(0.032),
    maxChi2 = cms.PSet(
        enabled = cms.bool(True),
        pt1 = cms.double(0.8),
        pt2 = cms.double(8),
        value1 = cms.double(100),
        value2 = cms.double(6)
    ),
    mightGet = cms.untracked.vstring('IntermediateHitDoublets_highPtTripletStepHitDoublets__RECO'),
    useBendingCorrection = cms.bool(True)
)

hltPhase2HighPtTripletStepSeedLayers = cms.EDProducer("SeedingLayersEDProducer",
    BPix = cms.PSet(
        HitProducer = cms.string('siPixelRecHits'),
        TTRHBuilder = cms.string('WithTrackAngle'),
        skipClusters = cms.InputTag("hltPhase2HighPtTripletStepClusters")
    ),
    FPix = cms.PSet(
        HitProducer = cms.string('siPixelRecHits'),
        TTRHBuilder = cms.string('WithTrackAngle'),
        skipClusters = cms.InputTag("hltPhase2HighPtTripletStepClusters")
    ),
    MTEC = cms.PSet(

    ),
    MTIB = cms.PSet(

    ),
    MTID = cms.PSet(

    ),
    MTOB = cms.PSet(

    ),
    TEC = cms.PSet(

    ),
    TIB = cms.PSet(

    ),
    TID = cms.PSet(

    ),
    TOB = cms.PSet(

    ),
    layerList = cms.vstring(
        'BPix1+BPix2+BPix3',
        'BPix2+BPix3+BPix4',
        'BPix1+BPix3+BPix4',
        'BPix1+BPix2+BPix4',
        'BPix2+BPix3+FPix1_pos',
        'BPix2+BPix3+FPix1_neg',
        'BPix1+BPix2+FPix1_pos',
        'BPix1+BPix2+FPix1_neg',
        'BPix2+FPix1_pos+FPix2_pos',
        'BPix2+FPix1_neg+FPix2_neg',
        'BPix1+FPix1_pos+FPix2_pos',
        'BPix1+FPix1_neg+FPix2_neg',
        'FPix1_pos+FPix2_pos+FPix3_pos',
        'FPix1_neg+FPix2_neg+FPix3_neg',
        'BPix1+FPix2_pos+FPix3_pos',
        'BPix1+FPix2_neg+FPix3_neg',
        'FPix2_pos+FPix3_pos+FPix4_pos',
        'FPix2_neg+FPix3_neg+FPix4_neg',
        'FPix3_pos+FPix4_pos+FPix5_pos',
        'FPix3_neg+FPix4_neg+FPix5_neg',
        'FPix4_pos+FPix5_pos+FPix6_pos',
        'FPix4_neg+FPix5_neg+FPix6_neg',
        'FPix5_pos+FPix6_pos+FPix7_pos',
        'FPix5_neg+FPix6_neg+FPix7_neg',
        'FPix6_pos+FPix7_pos+FPix8_pos',
        'FPix6_neg+FPix7_neg+FPix8_neg'
    ),
    mightGet = cms.optional.untracked.vstring
)

hltPhase2HighPtTripletStepSeeds = cms.EDProducer("SeedCreatorFromRegionConsecutiveHitsEDProducer",
    MinOneOverPtError = cms.double(1),
    OriginTransverseErrorMultiplier = cms.double(1),
    SeedComparitorPSet = cms.PSet(
        ComponentName = cms.string('none')
    ),
    SeedMomentumForBOFF = cms.double(5),
    TTRHBuilder = cms.string('WithTrackAngle'),
    forceKinematicWithRegionDirection = cms.bool(False),
    magneticField = cms.string(''),
    mightGet = cms.untracked.vstring('RegionsSeedingHitSets_hltPhase2HighPtTripletStepHitTriplets__RECO'),
    propagator = cms.string('PropagatorWithMaterial'),
    seedingHitSets = cms.InputTag("hltPhase2HighPtTripletStepHitTriplets")
)

hltPhase2HighPtTripletStepTrackCutClassifier = cms.EDProducer( "TrackCutClassifier",
    src = cms.InputTag( "hltPhase2HighPtTripletStepTracks" ),
    beamspot = cms.InputTag( "offlineBeamSpot" ),
    vertices = cms.InputTag( "hltPhase2PixelVertices" ), # pixelVertices previous hltPhase2FirstStepPrimaryVertices" ),
    qualityCuts = cms.vdouble( -0.7, 0.1, 0.7 ),
    mva = cms.PSet(
      minPixelHits = cms.vint32( 0, 0, 3 ), ##
      maxDzWrtBS = cms.vdouble( 3.40282346639E38, 24.0, 15.0 ),
      dr_par = cms.PSet(
        d0err = cms.vdouble( 0.003, 0.003, 0.003 ),
        dr_par2 = cms.vdouble( 0.6, 0.5, 0.45 ), ##
        dr_par1 = cms.vdouble( 0.7, 0.6, 0.6 ),
        dr_exp = cms.vint32( 4, 4, 4 ),
        d0err_par = cms.vdouble( 0.002, 0.002, 0.001 )
      ),
      maxLostLayers = cms.vint32( 3, 3, 2 ),
      min3DLayers = cms.vint32( 3, 3, 4 ),
      dz_par = cms.PSet(
        dz_par1 = cms.vdouble( 0.8, 0.7, 0.7 ),
        dz_par2 = cms.vdouble( 0.6, 0.6, 0.55 ),
        dz_exp = cms.vint32( 4, 4, 4 )
      ),
      minNVtxTrk = cms.int32( 3 ), ## offline 2, online 3 switching to 3
      maxDz = cms.vdouble( 0.5, 0.2, 3.40282346639E38 ), ##
      minNdof = cms.vdouble( 1.0E-5, 1.0E-5, 1.0E-5 ), ##
      maxChi2 = cms.vdouble( 9999.0, 9999.0, 9999.0 ),
      maxChi2n = cms.vdouble( 2.0, 1.0, 0.8 ),
      maxDr = cms.vdouble( 0.5, 0.03, 3.40282346639E38 ), ##
      minLayers = cms.vint32( 3, 3, 4 )
    ),
    ignoreVertices = cms.bool( False )
)

hltPhase2HighPtTripletStepTracksSelectionHighPurity = cms.EDProducer( "TrackCollectionFilterCloner",
    minQuality = cms.string( "highPurity" ),
    copyExtras = cms.untracked.bool( True ),
    copyTrajectories = cms.untracked.bool( False ),
    originalSource = cms.InputTag( "hltPhase2HighPtTripletStepTracks" ),
    originalQualVals = cms.InputTag( 'hltPhase2HighPtTripletStepTrackCutClassifier','QualityMasks' ),
    originalMVAVals = cms.InputTag( 'hltPhase2HighPtTripletStepTrackCutClassifier','MVAValues' )
)

hltPhase2HighPtTripletStepTrajectoryFilter = cms.PSet(
    ComponentType = cms.string('CompositeTrajectoryFilter'),
    filters = cms.VPSet(
        cms.PSet(
            refToPSet_ = cms.string('hltPhase2HighPtTripletStepTrajectoryFilterBase')
        ),
        cms.PSet(
            refToPSet_ = cms.string('ClusterShapeTrajectoryFilter')
        )
    )
    )

hltPhase2HighPtTripletStepTrajectoryFilterBase = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(1.0), # previous 2.0
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    maxCCCLostHits = cms.int32(0), # previous 9999
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(1), # previous 999
    maxLostHitsFraction = cms.double(999.0), # previous 0.1
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('SiStripClusterChargeCutNone')
    ),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.9), # ptcut previous 0.2
    minimumNumberOfHits = cms.int32(3),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(1), # previous 0
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)



hltPhase2HighPtTripletStepTrajectoryFilterInOut = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(2.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    maxCCCLostHits = cms.int32(9999),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(999),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('SiStripClusterChargeCutNone')
    ),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.9), # ptcut previous 0.4
    minimumNumberOfHits = cms.int32(4),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(1),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

hltPhase2HighPtTripletStepChi2Est = cms.ESProducer("Chi2ChargeMeasurementEstimatorESProducer",
    ComponentName = cms.string('hltPhase2HighPtTripletStepChi2Est'),
    MaxChi2 = cms.double(16.0), # previous 20.0
    MaxDisplacement = cms.double(0.5),
    MaxSagitta = cms.double(2),
    MinPtForHitRecoveryInGluedDet = cms.double(1000000.0), # previous 1000000000000
    MinimalTolerance = cms.double(0.5),
    appendToDataLabel = cms.string(''),
    clusterChargeCut = cms.PSet(
        refToPSet_ = cms.string('SiStripClusterChargeCutLoose') # previous SiStripClusterChargeCutNone
    ),
    nSigma = cms.double(3),
    pTChargeCutThreshold = cms.double(-1) # previous 15.0
)


hltPhase2HighPtTripletStepTrajectoryCleanerBySharedHits = cms.ESProducer("TrajectoryCleanerESProducer",
    ComponentName = cms.string('hltPhase2HighPtTripletStepTrajectoryCleanerBySharedHits'),
    ComponentType = cms.string('TrajectoryCleanerBySharedHits'),
    MissingHitPenalty = cms.double(20.0),
    ValidHitBonus = cms.double(5.0),
    allowSharedFirstHit = cms.bool(True),
    fractionShared = cms.double(0.16)
)



hltPhase2HighPtTripletStepTrajectoryBuilder = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'), #needs to stay like this for now
    #MeasurementTrackerName = cms.string(''), #??
    TTRHBuilder = cms.string('WithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(False), # previous True
    bestHitOnly = cms.bool(True),
    estimator = cms.string('hltPhase2HighPtTripletStepChi2Est'),
    foundHitBonus = cms.double(10.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('hltPhase2HighPtTripletStepTrajectoryFilterInOut') #??
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(False),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(1), # previous 3
    maxDPhiForLooperReconstruction = cms.double(2.0),
    maxPtForLooperReconstruction = cms.double(0.7),
    minNrOfHitsForRebuild = cms.int32(5),
    propagatorAlong = cms.string('PropagatorWithMaterialParabolicMf'), # previous PropagatorWithMaterial
    propagatorOpposite = cms.string('PropagatorWithMaterialParabolicMfOpposite'), # previous PropagatorWithMaterialOpposite
    requireSeedHitsInRebuild = cms.bool(True),
    seedAs5DHit = cms.bool(False), #cmssw_11_0
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('hltPhase2HighPtTripletStepTrajectoryFilter')
    ),
    #seedPairPenalty = cms.int32(0),
    #minPt = cms.double(0.9),
    #maxLostHitsFraction = cms.double(999.0), # previous 0.1
    #maxNumberOfHits = cms.int32(100),
    updator = cms.string('KFUpdator'),
    useSameTrajFilter = cms.bool(False)
)


hltPhase2HighPtTripletStepTrackCandidates = cms.EDProducer("CkfTrackCandidateMaker",
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"),
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    ### if we use 'CachingSeedCleanerBySharedInput' as the redundantseedcleaner
    ### then numHitsForSeedCleaner = cms.int32(4) and onlyPixelHitsForSeedCleaner = cms.bool(False) by default
    ### unless they are changed explicitly
    RedundantSeedCleaner = cms.string('CachingSeedCleanerBySharedInput'),
    #SimpleMagneticField = cms.string('ParabolicMf'), # previous ''
    #sTrajectoryBuilder = cms.string('GroupedCkfTrajectoryBuilder'), #needs to stay this way
    TrajectoryBuilderPSet = cms.PSet(
        refToPSet_ = cms.string('hltPhase2HighPtTripletStepTrajectoryBuilder')
    ),
    TrajectoryCleaner = cms.string('hltPhase2HighPtTripletStepTrajectoryCleanerBySharedHits'),
    TransientInitialStateEstimatorParameters = cms.PSet(
        numberMeasurementsForFit = cms.int32(4),
        propagatorAlongTISE = cms.string('PropagatorWithMaterialParabolicMf'), # previous PropagatorWithMaterial
        propagatorOppositeTISE = cms.string('PropagatorWithMaterialParabolicMfOpposite') # previous PropagatorWithMaterialOpposite
    ),
    cleanTrajectoryAfterInOut = cms.bool(True), #needs to stay True
    doSeedingRegionRebuilding = cms.bool(True), #needs to stay True
    maxNSeeds = cms.uint32(100000), # previous 500000
    maxSeedsBeforeCleaning = cms.uint32(1000), # previous 5000
    numHitsForSeedCleaner = cms.int32(50), #############
    onlyPixelHitsForSeedCleaner = cms.bool(True),  # previous ################
    phase2clustersToSkip = cms.InputTag("hltPhase2HighPtTripletStepClusters"),
    reverseTrajectories = cms.bool(False),
    src = cms.InputTag("hltPhase2HighPtTripletStepSeeds"),
    useHitsSplitting = cms.bool(False) # previous True
)


hltPhase2HighPtTripletStepTrackingRegions = cms.EDProducer("GlobalTrackingRegionFromBeamSpotEDProducer",
    RegionPSet = cms.PSet(
        beamSpot = cms.InputTag("offlineBeamSpot"),
        nSigmaZ = cms.double(4),
        originHalfLength = cms.double(0),
        originRadius = cms.double(0.02),
        precise = cms.bool(True),
        ptMin = cms.double(0.9), # ptcut previous 0.7
        useMultipleScattering = cms.bool(False)
    ),
    mightGet = cms.optional.untracked.vstring  # cmssw_11_1
)


hltPhase2HighPtTripletStepTracks = cms.EDProducer("TrackProducer",
    AlgorithmName = cms.string('highPtTripletStep'),
    Fitter = cms.string('FlexibleKFFittingSmoother'),
    GeometricInnerState = cms.bool(False),
    MeasurementTracker = cms.string(''),
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"),
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    Propagator = cms.string('RungeKuttaTrackerPropagator'),
    SimpleMagneticField = cms.string(''),
    TTRHBuilder = cms.string('WithTrackAngle'),  ## --> Template once corrected
    TrajectoryInEvent = cms.bool(False),
    alias = cms.untracked.string('ctfWithMaterialTracks'),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    clusterRemovalInfo = cms.InputTag(""),
    src = cms.InputTag("hltPhase2HighPtTripletStepTrackCandidates"),
    useHitsSplitting = cms.bool(False),
    useSimpleMF = cms.bool(False)
)


################################################################################################
########################  initial step

hltPhase2InitialStepHitDoublets = cms.EDProducer("HitPairEDProducer",
    clusterCheck = cms.InputTag("trackerClusterCheck"),
    layerPairs = cms.vuint32(0, 1, 2),
    maxElement = cms.uint32(50000000),
    maxElementTotal = cms.uint32(50000000),
    mightGet = cms.optional.untracked.vstring,  # cmssw_11_1
    produceIntermediateHitDoublets = cms.bool(True),
    produceSeedingHitSets = cms.bool(False),
    seedingLayers = cms.InputTag("hltPhase2InitialStepSeedLayers"),
    trackingRegions = cms.InputTag("hltPhase2InitialStepTrackingRegions"),
    trackingRegionsSeedingLayers = cms.InputTag("")
)

hltPhase2InitialStepHitQuadruplets = cms.EDProducer("CAHitQuadrupletEDProducer",
    CAHardPtCut = cms.double(0),
    CAOnlyOneLastHitPerLayerFilter = cms.optional.bool, # cmssw_11_1
    CAPhiCut = cms.double(0.175),
    CAThetaCut = cms.double(0.001),
    SeedComparitorPSet = cms.PSet(
        ComponentName = cms.string('LowPtClusterShapeSeedComparitor'),
        clusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"),
        clusterShapeHitFilter = cms.string('ClusterShapeHitFilter')
    ),
    doublets = cms.InputTag("hltPhase2InitialStepHitDoublets"),
    extraHitRPhitolerance = cms.double(0.032),
    fitFastCircle = cms.bool(True),
    fitFastCircleChi2Cut = cms.bool(True),
    maxChi2 = cms.PSet(
        enabled = cms.bool(True),
        pt1 = cms.double(0.7),
        pt2 = cms.double(2),
        value1 = cms.double(200),
        value2 = cms.double(50)
    ),
    mightGet = cms.untracked.vstring('IntermediateHitDoublets_initialStepHitDoublets__RECO'),
    useBendingCorrection = cms.bool(True)
)

hltPhase2InitialStepSeedLayers = cms.EDProducer("SeedingLayersEDProducer",
    BPix = cms.PSet(
        HitProducer = cms.string('siPixelRecHits'),
        TTRHBuilder = cms.string('WithTrackAngle')
    ),
    FPix = cms.PSet(
        HitProducer = cms.string('siPixelRecHits'),
        TTRHBuilder = cms.string('WithTrackAngle')
    ),
    MTEC = cms.PSet(

    ),
    MTIB = cms.PSet(

    ),
    MTID = cms.PSet(

    ),
    MTOB = cms.PSet(

    ),
    TEC = cms.PSet(

    ),
    TIB = cms.PSet(

    ),
    TID = cms.PSet(

    ),
    TOB = cms.PSet(

    ),
    layerList = cms.vstring(
        'BPix1+BPix2+BPix3+BPix4',
        'BPix1+BPix2+BPix3+FPix1_pos',
        'BPix1+BPix2+BPix3+FPix1_neg',
        'BPix1+BPix2+FPix1_pos+FPix2_pos',
        'BPix1+BPix2+FPix1_neg+FPix2_neg',
        'BPix1+FPix1_pos+FPix2_pos+FPix3_pos',
        'BPix1+FPix1_neg+FPix2_neg+FPix3_neg',
        'FPix1_pos+FPix2_pos+FPix3_pos+FPix4_pos',
        'FPix1_neg+FPix2_neg+FPix3_neg+FPix4_neg',
        'FPix2_pos+FPix3_pos+FPix4_pos+FPix5_pos',
        'FPix2_neg+FPix3_neg+FPix4_neg+FPix5_neg',
        'FPix3_pos+FPix4_pos+FPix5_pos+FPix6_pos',
        'FPix3_neg+FPix4_neg+FPix5_neg+FPix6_neg',
        'FPix4_pos+FPix5_pos+FPix6_pos+FPix7_pos',
        'FPix4_neg+FPix5_neg+FPix6_neg+FPix7_neg',
        'FPix5_pos+FPix6_pos+FPix7_pos+FPix8_pos',
        'FPix5_neg+FPix6_neg+FPix7_neg+FPix8_neg'
    ),
    mightGet = cms.optional.untracked.vstring # cmssw_11_1
)

#hltIter0PFLowPixelSeedsFromPixelTracks
hltPhase2InitialStepSeeds = cms.EDProducer( "SeedGeneratorFromProtoTracksEDProducer",
    useEventsWithNoVertex = cms.bool( True ),
    originHalfLength = cms.double(0.3), #10 1  previous 0.3 ),
    useProtoTrackKinematics = cms.bool( False ),
    usePV = cms.bool( False ),
    includeFourthHit = cms.bool(True),
    SeedCreatorPSet = cms.PSet(  refToPSet_ = cms.string( "hltPhase2SeedFromProtoTracks" ) ),
    InputVertexCollection = cms.InputTag(""),
    TTRHBuilder = cms.string( "WithTrackAngle"), #hltESPTTRHBuilderPixelOnly" ),
    InputCollection = cms.InputTag( "hltPhase2PixelTracks" ),
    originRadius = cms.double( 0.1 ) # 5 #0.5  previous 0.1
)

hltPhase2InitialStepTrackCutClassifier = cms.EDProducer( "TrackCutClassifier",
    src = cms.InputTag( "hltPhase2InitialStepTracks" ),
    beamspot = cms.InputTag( "offlineBeamSpot" ),
    vertices = cms.InputTag( "hltPhase2PixelVertices" ), # pixelVertices previous hltPhase2FirstStepPrimaryVertices" ),
    qualityCuts = cms.vdouble( -0.7, 0.1, 0.7 ),
    mva = cms.PSet(
	minPixelHits = cms.vint32(0,0,3), ######
	maxDzWrtBS = cms.vdouble( 3.40282346639E38, 24.0, 15.0 ),
	dr_par = cms.PSet(
	  d0err = cms.vdouble( 0.003, 0.003, 0.003 ),
	  dr_par1 = cms.vdouble( 0.8, 0.7, 0.6 ),
	  dr_par2 = cms.vdouble( 0.6, 0.5, 0.45 ),
	  dr_exp = cms.vint32( 4, 4, 4 ),
	  d0err_par = cms.vdouble( 0.001, 0.001, 0.001 )
	),
	maxLostLayers = cms.vint32( 3, 2, 2 ),
	min3DLayers = cms.vint32( 3, 3, 3),
	dz_par = cms.PSet(
	  dz_par1 = cms.vdouble( 0.9, 0.8, 0.7 ),
	  dz_par2 = cms.vdouble( 0.8, 0.7, 0.55 ),
	  dz_exp = cms.vint32( 4, 4, 4 )
	),
	minNVtxTrk = cms.int32( 3 ), # offline 2, online 3 switching to 3
	maxDz = cms.vdouble( 0.5, 0.2, 3.40282346639E38 ), ##
	minNdof = cms.vdouble( 1.0E-5, 1.0E-5, 1.0E-5 ), ##
	maxChi2 = cms.vdouble( 9999.0, 25.0, 16.0 ),
	maxChi2n = cms.vdouble( 2.0, 1.4, 1.2),
	maxDr = cms.vdouble( 0.5, 0.03, 3.40282346639E38 ), ##
	minLayers = cms.vint32( 3, 3, 3 ) ##
    ),
    ignoreVertices = cms.bool( False )
)

hltPhase2InitialStepTracksSelectionHighPurity = cms.EDProducer( "TrackCollectionFilterCloner",
    minQuality = cms.string( "highPurity" ),
    copyExtras = cms.untracked.bool( True ),
    copyTrajectories = cms.untracked.bool( False ),
    originalSource = cms.InputTag( "hltPhase2InitialStepTracks" ),
    originalQualVals = cms.InputTag('hltPhase2InitialStepTrackCutClassifier','QualityMasks' ),
    originalMVAVals = cms.InputTag('hltPhase2InitialStepTrackCutClassifier','MVAValues' )
)

hltPhase2InitialStepChi2Est = cms.ESProducer("Chi2ChargeMeasurementEstimatorESProducer",
    ComponentName = cms.string('hltPhase2InitialStepChi2Est'),
    MaxChi2 = cms.double(9.0), # previous 30.0
    MaxDisplacement = cms.double(0.5),
    MaxSagitta = cms.double(2),
    MinPtForHitRecoveryInGluedDet = cms.double(1000000.0), # previous 1000000000000
    MinimalTolerance = cms.double(0.5),
    appendToDataLabel = cms.string(''),
    clusterChargeCut = cms.PSet(
        refToPSet_ = cms.string('SiStripClusterChargeCutLoose')# SiStripClusterChargeCutNone
    ),
    nSigma = cms.double(3.0),
    pTChargeCutThreshold = cms.double(15.0)
)

hltPhase2InitialStepTrajectoryBuilder = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),# previous GroupedCkfTrajectoryBuilder --> CkfTrajectoryBuilder
    #MeasurementTrackerName = cms.string(''),
    TTRHBuilder = cms.string('WithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(False), # previous True
    bestHitOnly = cms.bool(True),
    estimator = cms.string('hltPhase2InitialStepChi2Est'),
    foundHitBonus = cms.double(10.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('hltPhase2InitialStepTrajectoryFilter') # previous CkfBaseTrajectoryFilter_block
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(True),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(1), # previous 3
    maxDPhiForLooperReconstruction = cms.double(2.0),
    maxPtForLooperReconstruction = cms.double(0.7),
    minNrOfHitsForRebuild = cms.int32(1),
    propagatorAlong = cms.string('PropagatorWithMaterialParabolicMf'), # previous PropagatorWithMaterial
    propagatorOpposite = cms.string('PropagatorWithMaterialParabolicMfOpposite'), # previous PropagatorWithMaterialOpposite
    requireSeedHitsInRebuild = cms.bool(True),
    seedAs5DHit = cms.bool(False), #cmssw_11_0
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('hltPhase2InitialStepTrajectoryFilter')
    ),
    #seedPairPenalty = cms.int32(0),
    #minPt = cms.double(0.9),
    #maxLostHitsFraction = cms.double(999.0), # previous 0.1
    #maxNumberOfHits = cms.int32(100),
    updator = cms.string('KFUpdator'),
    useSameTrajFilter = cms.bool(True)
)

hltPhase2InitialStepTrajectoryFilter = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(1.0), # previous 2
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    maxCCCLostHits = cms.int32(0), # previous 9999
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(1), # previous 999
    maxLostHitsFraction = cms.double(999), # previous 0.1
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('SiStripClusterChargeCutNone')
    ),
    minHitsMinPt = cms.int32(4), # previous 3
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.9), # previous 0.2 # ptcut previous 0.3
    minimumNumberOfHits = cms.int32(4), # previous 3
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

hltPhase2InitialStepTrackCandidates = cms.EDProducer("CkfTrackCandidateMaker",
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"),
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    ### if we use 'CachingSeedCleanerBySharedInput' as the redundantseedcleaner
    ### then numHitsForSeedCleaner = cms.int32(4) and onlyPixelHitsForSeedCleaner = cms.bool(False) by default
    ### unless they are changed explicitly
    RedundantSeedCleaner = cms.string('CachingSeedCleanerBySharedInput'),
    #SimpleMagneticField = cms.string('ParabolicMf'), # previous ''
    #TrajectoryBuilder = cms.string('GroupedCkfTrajectoryBuilder'), # previous GroupedCkfTrajectoryBuilder --> ''
    TrajectoryBuilderPSet = cms.PSet(
        refToPSet_ = cms.string('hltPhase2InitialStepTrajectoryBuilder')
    ),
    TrajectoryCleaner = cms.string('TrajectoryCleanerBySharedHits'),
    TransientInitialStateEstimatorParameters = cms.PSet(
        numberMeasurementsForFit = cms.int32(16),
        propagatorAlongTISE = cms.string('PropagatorWithMaterialParabolicMf'), # previous PropagatorWithMaterial
        propagatorOppositeTISE = cms.string('PropagatorWithMaterialParabolicMfOpposite') # previous PropagatorWithMaterialOpposite
    ),
    cleanTrajectoryAfterInOut = cms.bool(True), # previous True --> False
    doSeedingRegionRebuilding = cms.bool(True),# previous True --> False
    maxNSeeds = cms.uint32(100000), # previous 500000
    maxSeedsBeforeCleaning = cms.uint32(1000), # previous 5000
    numHitsForSeedCleaner = cms.int32(50), ##########
    onlyPixelHitsForSeedCleaner = cms.bool(True), ##########
    reverseTrajectories = cms.bool(False), # previous False, try both F/T for timing/performance
    src = cms.InputTag("hltPhase2InitialStepSeeds"),
    useHitsSplitting = cms.bool(False) # previous True
)

hltPhase2InitialStepTrackRefsForJets = cms.EDProducer("ChargedRefCandidateProducer",
    particleType = cms.string('pi+'),
    src = cms.InputTag("hltPhase2InitialStepTracks")
)

hltPhase2InitialStepTrackingRegions = cms.EDProducer("GlobalTrackingRegionFromBeamSpotEDProducer",
    RegionPSet = cms.PSet(
        beamSpot = cms.InputTag("offlineBeamSpot"),
        nSigmaZ = cms.double(4.0),
        originHalfLength = cms.double(0),
        originRadius = cms.double(0.03),
        precise = cms.bool(True),
        ptMin = cms.double(0.9), # ptcut previous 0.6
        useMultipleScattering = cms.bool(False)
    ),
    mightGet = cms.optional.untracked.vstring # cmssw_11_1
)

hltPhase2InitialStepTracks = cms.EDProducer("TrackProducer",
    AlgorithmName = cms.string('initialStep'),
    Fitter = cms.string('FlexibleKFFittingSmoother'),
    GeometricInnerState = cms.bool(False),
    MeasurementTracker = cms.string(''),
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"),
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    Propagator = cms.string('RungeKuttaTrackerPropagator'),
    SimpleMagneticField = cms.string(''),
    TTRHBuilder = cms.string('WithTrackAngle'), # cmssw_11_1 --> WithTrackAngleTemplate but not corrected yet
    TrajectoryInEvent = cms.bool(False),
    alias = cms.untracked.string('ctfWithMaterialTracks'),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    clusterRemovalInfo = cms.InputTag(""),
    src = cms.InputTag("hltPhase2InitialStepTrackCandidates"),
    useHitsSplitting = cms.bool(False),
    useSimpleMF = cms.bool(False)
)


####DA Vertexing

hltPhase2DAPrimaryVerticesUnsorted = cms.EDProducer("PrimaryVertexProducer",
    TkClusParameters = cms.PSet(
        TkDAClusParameters = cms.PSet(
            Tmin = cms.double(2.0),
            Tpurge = cms.double(2.0),
            Tstop = cms.double(0.5),
            coolingFactor = cms.double(0.6),
            d0CutOff = cms.double(3.0),
            dzCutOff = cms.double(3.0),
            uniquetrkweight = cms.double(0.8),
            vertexSize = cms.double(0.006),
            zmerge = cms.double(0.01)
),
algorithm = cms.string('DA_vect')
    ),
    TkFilterParameters = cms.PSet(
        algorithm = cms.string('filter'),
        maxD0Significance = cms.double(4.0),
        maxEta = cms.double(4.0),
        maxNormalizedChi2 = cms.double(10.0),
        minPixelLayersWithHits = cms.int32(2),
        minPt = cms.double(0.0),
        minSiliconLayersWithHits = cms.int32(0), ## DOES NOT HAVE ANY SENSE w/ PIXEL TRACKS, PLEASE SET TO 0 !!!!
        trackQuality = cms.string('any')
    ),
    TrackLabel = cms.InputTag("hltPhase2PixelTracks"),
    beamSpotLabel = cms.InputTag("offlineBeamSpot"),
    verbose = cms.untracked.bool(False),
    vertexCollections = cms.VPSet(cms.PSet(
        algorithm = cms.string('AdaptiveVertexFitter'),
        chi2cutoff = cms.double(2.5),
        label = cms.string(''),
        maxDistanceToBeam = cms.double(1.0),
        minNdof = cms.double(0.0),
        useBeamConstraint = cms.bool(False)
    ))
)



hltPhase2PixelTracksCleaner = cms.EDProducer("TrackWithVertexSelector",
    copyExtras = cms.untracked.bool(True),
    copyTrajectories = cms.untracked.bool(False),
    d0Max = cms.double(999.0),
    dzMax = cms.double(999.0),
    etaMax = cms.double(5.0),
    etaMin = cms.double(0.0),
    nSigmaDtVertex = cms.double(0),
    nVertices = cms.uint32(20),
    normalizedChi2 = cms.double(999999.0),
    numberOfLostHits = cms.uint32(999),
    numberOfValidHits = cms.uint32(0),
    numberOfValidPixelHits = cms.uint32(4),
    maxOfValidPixelHits = cms.uint32(99),
    ptErrorCut = cms.double(9999999.0),
    ptMax = cms.double(100000.0),
    ptMin = cms.double(0.0),
    quality = cms.string('any'),
    rhoVtx = cms.double(0.1),
    src = cms.InputTag("hltPhase2PixelTracks"),
    timeResosTag = cms.InputTag(""),
    timesTag = cms.InputTag(""),
    useVtx = cms.bool(True),
    vertexTag = cms.InputTag("hltPhase2PixelVertices"),
    vtxFallback = cms.bool(True),
    zetaVtx = cms.double(0.3)
)

hltPhase2PixelTripletsCleaner = cms.EDProducer("TrackWithVertexSelector",
    copyExtras = cms.untracked.bool(True),
    copyTrajectories = cms.untracked.bool(False),
    d0Max = cms.double(999.0),
    dzMax = cms.double(999.0),
    etaMax = cms.double(5.0),
    etaMin = cms.double(0.0),
    nSigmaDtVertex = cms.double(0),
    nVertices = cms.uint32(20),
    normalizedChi2 = cms.double(999999.0),
    numberOfLostHits = cms.uint32(999),
    numberOfValidHits = cms.uint32(0),
    numberOfValidPixelHits = cms.uint32(3),
    maxOfValidPixelHits = cms.uint32(3),
    ptErrorCut = cms.double(9999999.0),
    ptMax = cms.double(100000.0),
    ptMin = cms.double(0.0),
    quality = cms.string('any'),
    rhoVtx = cms.double(0.06),
    src = cms.InputTag("hltPhase2PixelTracks"),
    timeResosTag = cms.InputTag(""),
    timesTag = cms.InputTag(""),
    useVtx = cms.bool(True),
    vertexTag = cms.InputTag("hltPhase2PixelVertices"),
    vtxFallback = cms.bool(True),
    zetaVtx = cms.double(0.18)
)

hltPhase2PixelTripletsSelector= cms.EDProducer("RecoTrackViewRefSelector",
    algorithm = cms.vstring(),
    algorithmMaskContains = cms.vstring(),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    invertRapidityCut = cms.bool(False), # cmssw_11_1
    lip = cms.double(300.0),
    maxChi2 = cms.double(10000000.0),
    maxPhi = cms.double(3.2),
    maxRapidity = cms.double(4.5),
    min3DLayer = cms.int32(0),
    minHit = cms.int32(0),
    minLayer = cms.int32(0),
    minPhi = cms.double(-3.2),
    minPixelHit = cms.int32(2), maxPixelHit = cms.int32(3),
    minRapidity = cms.double(-4.5),
    originalAlgorithm = cms.vstring(),
    ptMin = cms.double(0.9), # previous 0.1
    quality = cms.vstring(''),
    src = cms.InputTag("hltPhase2PixelTracks"),
    tip = cms.double(120),
    minPixelLayer = cms.int32(2),
    usePV = cms.bool(False),
    vertexTag = cms.InputTag("")
)

hltPhase2PixelQuadrupletsSelector= cms.EDProducer("RecoTrackViewRefSelector",
    algorithm = cms.vstring(),
    algorithmMaskContains = cms.vstring(),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    invertRapidityCut = cms.bool(False), # cmssw_11_1
    lip = cms.double(300.0),
    maxChi2 = cms.double(10000.0),
    maxPhi = cms.double(3.2),
    maxRapidity = cms.double(4.5),
    min3DLayer = cms.int32(0),
    minHit = cms.int32(0),
    minLayer = cms.int32(2),
    minPhi = cms.double(-3.2),
    minPixelHit = cms.int32(4), maxPixelHit = cms.int32(99),
    minRapidity = cms.double(-4.5),
    minPixelLayer = cms.int32(3),
    originalAlgorithm = cms.vstring(),
    ptMin = cms.double(0.9), # previous 0.1
    quality = cms.vstring('any'),
    src = cms.InputTag("hltPhase2PixelTracks"),
    tip = cms.double(120),
    usePV = cms.bool(False),
    vertexTag = cms.InputTag("")#hltPhase2PixelVertices") #("hltPhase2OfflinePrimaryVertices")
)

hltPhase2PixelTracksClean = cms.EDProducer("RecoTrackViewRefSelector",
    algorithm = cms.vstring(),
    algorithmMaskContains = cms.vstring(),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    invertRapidityCut = cms.bool(False), # cmssw_11_1
    lip = cms.double(300.0),
    maxChi2 = cms.double(100.0),
    maxPhi = cms.double(3.2),
    maxRapidity = cms.double(4.5),
    min3DLayer = cms.int32(0),
    minHit = cms.int32(0),
    minLayer = cms.int32(2),
    minPhi = cms.double(-3.2),
    minPixelHit = cms.int32(0), maxPixelHit = cms.int32(99),
    minRapidity = cms.double(-4.5),
    minPixelLayer = cms.int32(0),
    originalAlgorithm = cms.vstring(),
    ptMin = cms.double(1.2), # previous 0.1
    quality = cms.vstring('any'),
    src = cms.InputTag("hltPhase2PixelTracks"),
    tip = cms.double(120),
    usePV = cms.bool(False),
    vertexTag = cms.InputTag("")#hltPhase2PixelVertices") #("hltPhase2OfflinePrimaryVertices")
)
