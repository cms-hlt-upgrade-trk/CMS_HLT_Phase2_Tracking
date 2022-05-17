import FWCore.ParameterSet.Config as cms
from tracking_modules import *
from generic_sequences import *
from L1Trigger.TrackFindingTracklet.Tracklet_cfi import *
from Configuration.StandardSequences.Reconstruction_cff import *
from RecoTracker.GeometryESProducer.TrackerRecoGeometryESProducer_cfi import *
from RecoTracker.MeasurementDet.MeasurementTrackerESProducer_cfi import *

####################################################
####### CPE Fix For Template When Track Angle
PixelCPEGenericESProducer = cms.ESProducer('PixelCPEGenericESProducer',
    LoadTemplatesFromDB = cms.bool(True),
    Alpha2Order = cms.bool(True),
    ClusterProbComputationFlag = cms.int32(0),
    useLAWidthFromDB = cms.bool(True),
    lAOffset = cms.double(0),
    lAWidthBPix = cms.double(0),
    lAWidthFPix = cms.double(0),
    doLorentzFromAlignment = cms.bool(False),
    useLAFromDB = cms.bool(True),
    xerr_barrel_l1 = cms.vdouble(
      0.00115,
      0.0012,
      0.00088
    ),
    yerr_barrel_l1 = cms.vdouble(
      0.00375,
      0.0023,
      0.0025,
      0.0025,
      0.0023,
      0.0023,
      0.0021,
      0.0021,
      0.0024
    ),
    xerr_barrel_ln = cms.vdouble(
      0.00115,
      0.0012,
      0.00088
    ),
    yerr_barrel_ln = cms.vdouble(
      0.00375,
      0.0023,
      0.0025,
      0.0025,
      0.0023,
      0.0023,
      0.0021,
      0.0021,
      0.0024
    ),
    xerr_endcap = cms.vdouble(
      0.002,
      0.002
    ),
    yerr_endcap = cms.vdouble(0.0021),
    xerr_barrel_l1_def = cms.double(0.0103),
    yerr_barrel_l1_def = cms.double(0.0021),
    xerr_barrel_ln_def = cms.double(0.0103),
    yerr_barrel_ln_def = cms.double(0.0021),
    xerr_endcap_def = cms.double(0.002),
    yerr_endcap_def = cms.double(0.00075),
    eff_charge_cut_highX = cms.double(1),
    eff_charge_cut_highY = cms.double(1),
    eff_charge_cut_lowX = cms.double(0),
    eff_charge_cut_lowY = cms.double(0),
    size_cutX = cms.double(3),
    size_cutY = cms.double(3),
    EdgeClusterErrorX = cms.double(50),
    EdgeClusterErrorY = cms.double(85),
    inflate_errors = cms.bool(False),
    inflate_all_errors_no_trk_angle = cms.bool(False),
    NoTemplateErrorsWhenNoTrkAngles = cms.bool(True),
    UseErrorsFromTemplates = cms.bool(True),
    TruncatePixelCharge = cms.bool(False),
    IrradiationBiasCorrection = cms.bool(False),
    DoCosmics = cms.bool(False),
    Upgrade = cms.bool(True),
    SmallPitch = cms.bool(False),
    ComponentName = cms.string('PixelCPEGeneric'),
    MagneticFieldRecord = cms.ESInputTag('', ''),
    appendToDataLabel = cms.string('')
)



####################################################
########################## Commonssoriginal_v7
#############


hltPhase2L1TTTracksEmulation = TTTracksFromTrackletEmulation.clone()

hltPhase2StartUp = cms.Sequence(
    offlineBeamSpot +
    itLocalReco +
     #cmssw_10_6
    otLocalReco +
    #caloLocalReco +
    trackerClusterCheck +
    caloTowerForTrk  
    )

hltPhase2InitialStepPVSequence = cms.Sequence(
    hltPhase2FirstStepPrimaryVerticesUnsorted +
    hltPhase2InitialStepTrackRefsForJets +
    caloTowerForTrk + # uses hbhereco, hfreco, horeco, ecalRecHit
    hltPhase2Ak4CaloJetsForTrk +  # uses caloTowerForTrk
    hltPhase2FirstStepPrimaryVertices
)

hltPhase2InitialStepSequence = cms.Sequence(
    #hltPhase2InitialStepSeedLayers +
    #hltPhase2InitialStepTrackingRegions +
    #hltPhase2InitialStepHitDoublets +
    #hltPhase2InitialStepHitQuadruplets +
    hltPhase2InitialStepSeeds +
    hltPhase2InitialStepTrackCandidates +
    hltPhase2InitialStepTracks +
    #hltPhase2InitialStepPVSequence + # use pixelVertices
    hltPhase2InitialStepTrackCutClassifier +
    hltPhase2InitialStepTracksSelectionHighPurity
)

####################################################
########################## Basic V7 setup
#############

hltPhase2PixelTracksSequence = cms.Sequence(
    hltPhase2PixelTrackFilterByKinematics +
    hltPhase2PixelFitterByHelixProjections +
    hltPhase2PixelTracksTrackingRegions +
    hltPhase2PixelTracksSeedLayers +
    hltPhase2PixelTracksHitDoublets +
    hltPhase2PixelTracksHitSeeds +
    hltPhase2PixelTracks +
    #hltPhase2PixelTracksCleaner +
    #hltPhase2PixelTripletsCleaner +
    hltPhase2PixelTripletsSelector +
    hltPhase2PixelQuadrupletsSelector + 
    hltPhase2PixelTracksClean 
#    hltPhase2PixelTracksMerger
)

hltPhase2PixelTracksSequenceL1 = cms.Sequence(
    hltPhase2PixelTrackClusters +
    hltPhase2PixelTrackFilterByKinematics +
    hltPhase2PixelFitterByHelixProjections +
    hltPhase2PixelTracksTrackingRegions +
    hltPhase2PixelTracksSeedLayers +
    hltPhase2PixelTracksHitDoublets +
    hltPhase2PixelTracksHitSeeds +
    hltPhase2PixelTracks +
    hltPhase2PixelTracksClean 
)

hltPhase2PixelVerticesSequence = cms.Sequence(
   hltPhase2PixelVertices +
    hltPhase2PixelTracksCleaner +
    hltPhase2PixelTripletsCleaner +
    hltPhase2PixelTripletsSelector +
    hltPhase2PixelQuadrupletsSelector +
    hltPhase2PixelTracksMerger

)


hltPhase2InitialStepSequenceFromPixelTracks = cms.Sequence(
    hltPhase2InitialStepSeeds +
    hltPhase2InitialStepTrackCandidates +
    hltPhase2InitialStepTracks +
    hltPhase2InitialStepTrackCutClassifier +
    hltPhase2InitialStepTracksSelectionHighPurity
)

hltPhase2HighPtTripletStepSequence = cms.Sequence(
    hltPhase2HighPtTripletStepClusters +
    hltPhase2HighPtTripletStepSeedLayers +
    hltPhase2HighPtTripletStepTrackingRegions +
    hltPhase2HighPtTripletStepHitDoublets +
    hltPhase2HighPtTripletStepHitTriplets +
    hltPhase2HighPtTripletStepSeeds +
    hltPhase2HighPtTripletStepTrackCandidates +
    hltPhase2HighPtTripletStepTracks +
    hltPhase2HighPtTripletStepTrackCutClassifier +
    hltPhase2HighPtTripletStepTracksSelectionHighPurity
)

original_v6 = cms.Path(
    hltPhase2StartUp +
    hltPhase2PixelTracksSequence + # pixeltracks
    hltPhase2PixelVerticesSequence +
##############################################
    hltPhase2InitialStepSequence +
    hltPhase2HighPtTripletStepSequence +
##############################################
    hltPhase2GeneralTracks
)

single_it = cms.Path(
    hltPhase2StartUp +
    hltPhase2PixelTracksSequence + # pixeltracks
    hltPhase2PixelVerticesSequence + # pixelvertices
##############################################
    hltPhase2InitialStepSequence +
    hltPhase2GeneralTracks
)

original_v7 = cms.Path(
    hltPhase2StartUp +
    hltPhase2PixelTracksSequence + # pixeltracks
    hltPhase2PixelVerticesSequence + # pixelvertices
    hltPhase2InitialStepSequenceFromPixelTracks +
    hltPhase2HighPtTripletStepSequence +
    hltPhase2GeneralTracks
)

####################################################
########################## Pure L1 setup (\w vertexing)
#############



hltPhase2L1TracksStepTrackRefsForJets = hltPhase2InitialStepTrackRefsForJets.clone()
hltPhase2L1TracksStepTrackRefsForJets.src = cms.InputTag("hltPhase2L1CtfTracks")

#hltPhase2Ak4CaloJetsForTrkL1 = hltPhase2Ak4CaloJetsForTrk.clone()
#hltPhase2Ak4CaloJetsForTrkL1.srcPVs = cms.InputTag("hltPhase2L1TracksStepPrimaryVerticesUnsorted")

#hltPhase2L1TracksStepPrimaryVertices = hltPhase2FirstStepPrimaryVertices.clone()
#hltPhase2L1TracksStepPrimaryVertices.jets = cms.InputTag("hltPhase2Ak4CaloJetsForTrkL1")
#hltPhase2L1TracksStepPrimaryVertices.particles = cms.InputTag("hltPhase2L1TracksStepTrackRefsForJets")

#hltPhase2L1PVSequence = cms.Sequence(
#    hltPhase2L1TracksStepPrimaryVerticesUnsorted +
#    hltPhase2L1TracksStepTrackRefsForJets +
#    caloTowerForTrk + # uses hbhereco, hfreco, horeco, ecalRecHit
#    hltPhase2Ak4CaloJetsForTrkL1 +  # uses caloTowerForTrk
#    hltPhase2L1TracksStepPrimaryVertices
#)


hltPhase2L1TracksTaskSeed = cms.Task(
            hltPhase2L1TrackSeedsFromL1Tracks
)
hltPhase2L1TracksSeqSeed = cms.Sequence(hltPhase2L1TracksTaskSeed) ##need this strange syntax to add mkFit steps

hltPhase2L1TracksSeqPattern = cms.Sequence(
            hltPhase2L1TracksSeqSeed +
            hltPhase2L1TrackCandidates +
            hltPhase2L1CtfTracks
)

hltPhase2L1TracksSequenceClassification = cms.Sequence(
            # hltPhase2L1PVSequence +
            hltPhase2L1TracksCutClassifier +#+
            hltPhase2L1TracksSelectionHighPurity)

hltPhase2L1TracksSequence = cms.Sequence(
    # hltPhase2TransientFromL1 +
    hltPhase2VertexFromL1 +
    # hltPhase2TrackFromL1 +
    hltPhase2L1TracksSeqSeed +
    hltPhase2L1TracksSeqPattern + 
    hltPhase2L1CtfTracks +
    hltPhase2L1PrimaryVertexUnsorted +  
    hltPhase2TrackWithVertexRefSelectorBeforeSortingL1 +
    hltPhase2TrackRefsForJetsBeforeSortingL1 +
    hltPhase2Ak4CaloJetsForTrkL1 +
    hltPhase2L1PrimaryVertex +
    hltPhase2L1TracksSequenceClassification +
    hltPhase2InitialStepClusters
)

pure_l1tracks = cms.Path(
    hltPhase2StartUp +
    hltPhase2PixelTracksSequence + # pixeltracks
    hltPhase2PixelVerticesSequence + # pixelvertices
    #TTTracksFromTrackletEmulation +
    hltPhase2L1TracksSequence +
    hltPhase2GeneralTracks
)

pixel_tracks = cms.Path(
    hltPhase2StartUp +
    hltPhase2PixelTracksSequence + # pixeltracks
    hltPhase2PixelVerticesSequence)

single_it_l1 = cms.Path(
    hltPhase2StartUp +
    hltPhase2L1TracksSequence +
    hltPhase2PixelTracksSequence + # pixeltracks
    hltPhase2PixelVerticesSequence + # pixelvertices
##############################################
    hltPhase2InitialStepSequence +
    hltPhase2GeneralTracks
)


hltPhase2InitialStepSequenceL1 = cms.Sequence(
    #hltPhase2InitialStepSeedLayers +
    #hltPhase2InitialStepTrackingRegions +
    #hltPhase2InitialStepHitDoublets +
    #hltPhase2InitialStepHitQuadruplets +
    hltPhase2InitialStepClusters +
    hltPhase2InitialStepSeeds +
    hltPhase2InitialStepTrackCandidates +
    hltPhase2InitialStepTracks +
    #hltPhase2InitialStepPVSequence + # use pixelVertices
    #hltPhase2InitialStepSelector
    hltPhase2InitialStepTrackCutClassifier +
    hltPhase2InitialStepTracksSelectionHighPurity
)


vertexReco = cms.Sequence(
    hltPhase2UnsortedOfflinePrimaryVertices +
    hltPhase2TrackWithVertexRefSelectorBeforeSorting +
    hltPhase2TrackRefsForJetsBeforeSorting + 
    #caloTowerForTrk +
    hltPhase2Ak4CaloJetsForTrk + # uses caloTowerForTrk
    hltPhase2OfflinePrimaryVertices +
    hltPhase2OfflinePrimaryVerticesWithBS +
    hltPhase2InclusiveVertexFinder +
    hltPhase2VertexMerger +
    hltPhase2TrackVertexArbitrator +
    hltPhase2InclusiveSecondaryVertices
)

initial_l1tracks = cms.Path(
    hltPhase2StartUp +
    hltPhase2PixelTracksSequence + # pixeltracks
    hltPhase2PixelVerticesSequence + # pixelvertices
    TTTracksFromTrackletEmulation +
    hltPhase2InitialStepSequenceL1 +
    hltPhase2L1TracksSequence +
    hltPhase2GeneralTracks
)


initial_l1tracks_mask = cms.Path(
    hltPhase2StartUp +
#   TTTracksFromTrackletEmulation +
    hltPhase2InitialStepSequenceL1 +
    hltPhase2PixelTracksSequence + # pixeltracks
    hltPhase2PixelVerticesSequence + # pixelvertices
    hltPhase2L1TracksSequence +
    hltPhase2GeneralTracks
)

triplet_l1tracks = cms.Path(
    hltPhase2StartUp +
    hltPhase2PixelTracksSequence +
    hltPhase2PixelVerticesSequence +
    TTTracksFromTrackletEmulation +
    hltPhase2L1TracksSequence +
    hltPhase2HighPtTripletStepSequence +
    hltPhase2GeneralTracks

)

pixeltriplet_l1 = cms.Path(
    hltPhase2StartUp +
    hltPhase2PixelTracksSequence +
    hltPhase2PixelVerticesSequence +
    TTTracksFromTrackletEmulation +
    hltPhase2L1TracksSequence +
    hltPhase2InitialStepSequenceL1 +
    hltPhase2GeneralTracks

)



l1_pixel_reco = cms.Path(
    hltPhase2StartUp +
    hltPhase2L1TracksSequence +
    hltPhase2PixelTracksSequence +
    hltPhase2PixelVerticesSequence +
    hltPhase2L1TracksSequenceClassification +
    hltPhase2InitialStepSequence +
    hltPhase2GeneralTracks

)

l1_pixel_reco_triplets = cms.Path(
    hltPhase2StartUp +
    hltPhase2L1TracksSequence +
    hltPhase2PixelTracksSequence +
    hltPhase2PixelVerticesSequence +
    hltPhase2L1TracksSequenceClassification +
    hltPhase2InitialStepSequenceL1 +
    hltPhase2HighPtTripletStepSequence +
    hltPhase2GeneralTracks
)

l1emulation = cms.Path
(
TTTracksFromTrackletEmulation
)

vertexing = cms.Path(
    caloLocalReco +
    vertexReco
)



#
#
#
#
# MC_Tracking_v7_L1_v1 = cms.Path(
#     itLocalReco +
#     offlineBeamSpot + #cmssw_10_6
#     hltPhase2TTTracksFromTracklet +
#     otLocalReco +
#     #caloLocalReco +
#     trackerClusterCheck +
#     hltPhase2PixelTracksSequence + # pixeltracks
#     hltPhase2PixelVerticesSequence + # pixelvertices
# ##############################################
#     hltPhase2InitialStepSequenceL1 +
#     hltPhase2L1TracksSequence +
#     #hltPhase2HighPtTripletStepSequence +
# ##############################################
#     hltPhase2GeneralTracks
# )
