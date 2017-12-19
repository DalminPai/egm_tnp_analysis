#############################################################
########## General settings
#############################################################
# flag to be Tested
cutpass80 = '(( abs(probe_sc_eta) < 0.8 && probe_Ele_nonTrigMVA > %f ) ||  ( abs(probe_sc_eta) > 0.8 && abs(probe_sc_eta) < 1.479&& probe_Ele_nonTrigMVA > %f ) || ( abs(probe_sc_eta) > 1.479 && probe_Ele_nonTrigMVA > %f ) )' % (0.967083,0.929117,0.726311)
cutpass90 = '(( abs(probe_sc_eta) < 0.8 && probe_Ele_nonTrigMVA > %f ) ||  ( abs(probe_sc_eta) > 0.8 && abs(probe_sc_eta) < 1.479&& probe_Ele_nonTrigMVA > %f ) || ( abs(probe_sc_eta) > 1.479 && probe_Ele_nonTrigMVA > %f ) )' % (0.913286,0.805013,0.358969)

HNEleID = '( el_pt > 10 && abs(el_sc_eta) < 2.5 && el_reliso03 < 0.08 && abs(el_dxy) < 0.01 && abs(el_dz) < 0.04 && el_3charge == 1 && el_passConversionVeto == 1 && el_dxysig < 4 && el_HNMVATight == 1 )'

## -- Test mva cut value in endcap for HNEleID -- ##
endcap_mvacut = 0.357
HNEleID_minus_HNMVA = '( el_pt > 10 && abs(el_sc_eta) < 2.5 && el_reliso03 < 0.08 && abs(el_dxy) < 0.01 && abs(el_dz) < 0.04 && el_3charge == 1 && el_passConversionVeto == 1 && el_dxysig < 4 )'
HNMVA = '( ( abs(el_sc_eta) < 0.8 && el_mva > 0.9 ) || ( 0.8 < abs(el_sc_eta) && abs(el_sc_eta) < 1.479 && el_mva > 0.825 ) || ( 1.479 < abs(el_sc_eta) && el_mva > %f ) )' % endcap_mvacut
HNEleID_v2 = HNEleID_minus_HNMVA + ' && ' + HNMVA


# flag to be Tested
flags = {
    'passingVeto'       : '(passingVeto   == 1)',
    'passingLoose'      : '(passingLoose  == 1)',
    'passingMedium'     : '(passingMedium == 1)',
    'passingTight'      : '(passingTight  == 1)',
    'passingVeto80X'    : '(passingVeto80X   == 1)',
    'passingLoose80X'   : '(passingLoose80X  == 1)',
    'passingMedium80X'  : '(passingMedium80X == 1)',
    'passingTight80X'   : '(passingTight80X  == 1)',
    'passingMVAwp80'    : cutpass80,
    'passingMVAwp90'    : cutpass90,
    'passingMVA80Xwp80' : '(passingMVA80Xwp80 == 1)',
    'passingMVA80Xwp90' : '(passingMVA80Xwp90 == 1)',
    'passingHNEleID'    : HNEleID,
    'passingHNEleID_v2' : HNEleID_v2
    }

#baseOutDir = 'results/Moriond17/tnpEleID/HN/' # Heavy-Neutrino SF job. pu-tree is not updated yet.
#baseOutDir = 'results/Moriond17/tnpEleID/HN_v2/' # Heavy-Neutrino SF job. pu-tree was updated.
baseOutDir = 'results/Moriond17/tnpEleID/HNEleID_v2/v_%f/' % endcap_mvacut  # Heavy-Neutrino SF job. pu-tree was updated. Test several mvacut.

#############################################################
########## samples definition  - preparing the samples
#############################################################
### samples are defined in etc/inputs/tnpSampleDef.py
### not: you can setup another sampleDef File in inputs
#import etc.inputs.tnpSampleDef as tnpSamples
import etc.inputs.tnpSampleDef_HN as tnpSamples
#tnpTreeDir = 'GsfElectronToEleID'
tnpTreeDir = 'tnpEleIDs'

samplesDef = {
    'data'   : tnpSamples.Moriond17_80X_HN['data_Run2016H'].clone(),
    'mcNom'  : tnpSamples.Moriond17_80X_HN['DY_madgraph_Winter17'].clone(),
    'mcAlt'  : tnpSamples.Moriond17_80X_HN['DY_amcatnlo_Winter17'].clone(),
#    'mcAlt'  : tnpSamples.Moriond17_80X['DYee_powheg_Winter17'].clone(),
    'tagSel' : tnpSamples.Moriond17_80X_HN['DY_madgraph_Winter17'].clone(),
}
## can add data sample easily
samplesDef['data'].add_sample( tnpSamples.Moriond17_80X_HN['data_Run2016G'] )
samplesDef['data'].add_sample( tnpSamples.Moriond17_80X_HN['data_Run2016F'] )
samplesDef['data'].add_sample( tnpSamples.Moriond17_80X_HN['data_Run2016E'] )
samplesDef['data'].add_sample( tnpSamples.Moriond17_80X_HN['data_Run2016D'] )
samplesDef['data'].add_sample( tnpSamples.Moriond17_80X_HN['data_Run2016C'] )
samplesDef['data'].add_sample( tnpSamples.Moriond17_80X_HN['data_Run2016B'] )

## some sample-based cuts... general cuts defined here after
## require mcTruth on MC DY samples and additional cuts
## all the samples MUST have different names (i.e. sample.name must be different for all)
## if you need to use 2 times the same sample, then rename the second one
#samplesDef['data'  ].set_cut('run >= 273726')
samplesDef['data' ].set_tnpTree(tnpTreeDir)
if not samplesDef['mcNom' ] is None: samplesDef['mcNom' ].set_tnpTree(tnpTreeDir)
if not samplesDef['mcAlt' ] is None: samplesDef['mcAlt' ].set_tnpTree(tnpTreeDir)
if not samplesDef['tagSel'] is None: samplesDef['tagSel'].set_tnpTree(tnpTreeDir)

if not samplesDef['mcNom' ] is None: samplesDef['mcNom' ].set_mcTruth()
if not samplesDef['mcAlt' ] is None: samplesDef['mcAlt' ].set_mcTruth()
if not samplesDef['tagSel'] is None: samplesDef['tagSel'].set_mcTruth()
if not samplesDef['tagSel'] is None:
    samplesDef['tagSel'].rename('mcAltSel_DY_madgraph')
 #   samplesDef['tagSel'].set_cut('tag_Ele_pt > 27  && tag_Ele_nonTrigMVA80X > 0.95')
    samplesDef['tagSel'].set_cut('tag_Ele_pt > 27  && tag_Ele_nonTrigMVA > 0.95')

## set MC weight, simple way (use tree weight) 
#weightName = 'totWeight'
#weightName = 'weight'
#if not samplesDef['mcNom' ] is None: samplesDef['mcNom' ].set_weight(weightName)
#if not samplesDef['mcAlt' ] is None: samplesDef['mcAlt' ].set_weight(weightName)
#if not samplesDef['tagSel'] is None: samplesDef['tagSel'].set_weight(weightName)

## set MC weight, can use several pileup rw for different data taking periods
#weightName = 'weights_2016_runGH.totWeight'
weightName = 'weights_2016_runAll.totWeight'
if not samplesDef['mcNom' ] is None: samplesDef['mcNom' ].set_weight(weightName)
if not samplesDef['mcAlt' ] is None: samplesDef['mcAlt' ].set_weight(weightName)
if not samplesDef['tagSel'] is None: samplesDef['tagSel'].set_weight(weightName)
#if not samplesDef['mcNom' ] is None: samplesDef['mcNom' ].set_puTree('/home/dmpai/pu/Winter17/DY_madgraph_Winter17_ele.pu.puTree.root')
#if not samplesDef['mcAlt' ] is None: samplesDef['mcAlt' ].set_puTree('/home/dmpai/pu/Winter17/DY_amcatnlo_Winter17_ele.pu.puTree.root')
if not samplesDef['mcNom' ] is None: samplesDef['mcNom' ].set_puTree('/home/dmpai/pu/HNWinter17/DY_madgraph_Winter17_ele.pu.puTree.root')
if not samplesDef['mcAlt' ] is None: samplesDef['mcAlt' ].set_puTree('/home/dmpai/pu/HNWinter17/DY_amcatnlo_Winter17_ele.pu.puTree.root')
#if not samplesDef['mcAlt' ] is None: samplesDef['mcAlt' ].set_puTree('eos/cms/store/group/phys_egamma/tnp/80X/pu/Winter17/DYee_powheg_Winter17_ele.pu.puTree.root')
#if not samplesDef['tagSel'] is None: samplesDef['tagSel'].set_puTree('/home/dmpai/pu/Winter17/DY_madgraph_Winter17_ele.pu.puTree.root')
if not samplesDef['tagSel'] is None: samplesDef['tagSel'].set_puTree('/home/dmpai/pu/HNWinter17/DY_madgraph_Winter17_ele.pu.puTree.root')


#############################################################
########## bining definition  [can be nD bining]
#############################################################
biningDef = [
   { 'var' : 'el_sc_eta' , 'type': 'float', 'bins': [-2.5,-2.0,-1.566,-1.4442, -0.8, 0.0, 0.8, 1.4442, 1.566, 2.0, 2.5] },
 #  { 'var' : 'probe_Ele_pt' , 'type': 'float', 'bins': [10,20,35,50,100,200,500] },
   { 'var' : 'el_pt' , 'type': 'float', 'bins': [10,20,35,50,90,150,500] },
]

#############################################################
########## Cuts definition for all samples
#############################################################
### cut
cutBase   = 'tag_Ele_pt > 30 && abs(tag_sc_eta) < 2.17 && el_q*tag_Ele_q < 0' # it is default!
#cutBase   = 'tag_Ele_pt > 40 && abs(tag_sc_eta) < 2.17 && probe_Ele_q*tag_Ele_q < 0'

# can add addtionnal cuts for some bins (first check bin number using tnpEGM --checkBins)
additionalCuts = { 
    0 : 'tag_Ele_trigMVA > 0.92 && sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45',
    1 : 'tag_Ele_trigMVA > 0.92 && sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45',
    2 : 'tag_Ele_trigMVA > 0.92 && sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45',
    3 : 'tag_Ele_trigMVA > 0.92 && sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45',
    4 : 'tag_Ele_trigMVA > 0.92 && sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45',
    5 : 'tag_Ele_trigMVA > 0.92 && sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45',
    6 : 'tag_Ele_trigMVA > 0.92 && sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45',
    7 : 'tag_Ele_trigMVA > 0.92 && sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45',
    8 : 'tag_Ele_trigMVA > 0.92 && sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45',
    9 : 'tag_Ele_trigMVA > 0.92 && sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45'
}

#### or remove any additional cut (default)
#additionalCuts = None

#############################################################
########## fitting params to tune fit by hand if necessary
#############################################################
tnpParNomFit = [
    ### default
    "meanP[-0.0,-5.0,5.0]","sigmaP[0.9,0.5,5.0]",
    "meanF[-0.0,-5.0,5.0]","sigmaF[0.9,0.5,5.0]",
    "acmsP[60.,50.,80.]","betaP[0.05,0.01,0.08]","gammaP[0.1, -2, 2]","peakP[90.0]",
    "acmsF[60.,50.,80.]","betaF[0.05,0.01,0.08]","gammaF[0.1, -2, 2]","peakF[90.0]",

    ## bin00
#    "meanP[-0.0,-5.0,5.0]","sigmaP[0.85]",
#    "meanF[-0.0,-5.0,5.0]","sigmaF[0.9,0.5,5.0]",
#    "acmsP[60.,50.,80.]","betaP[0.05,0.01,0.08]","gammaP[0.1,-2,2]","peakP[90.0]",
#    "acmsF[60.,50.,80.]","betaF[0.05,0.01,0.08]","gammaF[0.1,-2,2]","peakF[90.0]",

    ## bin03: ??
#    "meanP[-0.0,-5.0,5.0]","sigmaP[0.1]",
#    "meanF[-0.0,-5.0,5.0]","sigmaF[0.4]",
#    "acmsP[60.,50.,80.]","betaP[0.05,0.01,0.08]","gammaP[0.1,-2,2]","peakP[90.0]",
#    "acmsF[60.,50.,80.]","betaF[0.05,0.01,0.08]","gammaF[0.1,-2,2]","peakF[90.0]",

    ## bin04
#    "meanP[-0.0,-5.0,5.0]","sigmaP[0.65]",
#    "meanF[-0.0,-5.0,5.0]","sigmaF[0.9,0.5,5.0]",
#    "acmsP[60.,50.,80.]","betaP[0.05,0.01,0.08]","gammaP[0.1, -2, 2]","peakP[90.0]",
#    "acmsF[60.,50.,80.]","betaF[0.04,0.01,0.08]","gammaF[0.1, -2, 2]","peakF[90.0]",

    ## bin05
#    "meanP[-0.0,-5.0,5.0]","sigmaP[0.65]",
#    "meanF[-0.0,-5.0,5.0]","sigmaF[0.9,0.5,5.0]",
#    "acmsP[60.,50.,80.]","betaP[0.05,0.01,0.08]","gammaP[0.1, -2, 2]","peakP[90.0]",
#    "acmsF[60.,50.,80.]","betaF[0.03,0.01,0.08]","gammaF[0.1, -2, 2]","peakF[90.0]",

    ## bin06,41
#    "meanP[-0.0,-5.0,5.0]","sigmaP[0.8]",
#    "meanF[-0.0,-5.0,5.0]","sigmaF[0.9,0.5,5.0]",
#    "acmsP[60.,50.,80.]","betaP[0.05,0.01,0.08]","gammaP[0.1, -2, 2]","peakP[90.0]",
#    "acmsF[60.,50.,80.]","betaF[0.03,0.01,0.08]","gammaF[0.1, -2, 2]","peakF[90.0]",

    ## bin11,19,21
#    "meanP[-0.0,-5.0,5.0]","sigmaP[0.9]",
#    "meanF[-0.0,-5.0,5.0]","sigmaF[0.9,0.5,5.0]",
#    "acmsP[60.,50.,80.]","betaP[0.05,0.01,0.08]","gammaP[0.1, -2, 2]","peakP[90.0]",
#    "acmsF[60.,50.,80.]","betaF[0.05,0.01,0.08]","gammaF[0.1, -2, 2]","peakF[90.0]",

    ## bin12
#    "meanP[-0.0,-5.0,5.0]","sigmaP[0.9]",
#    "meanF[-0.0,-5.0,5.0]","sigmaF[1]",
#    "acmsP[60.,50.,80.]","betaP[0.05,0.01,0.08]","gammaP[0.1, -2, 2]","peakP[90.0]",
#    "acmsF[60.,50.,80.]","betaF[0.05,0.01,0.08]","gammaF[0.1, -2, 2]","peakF[90.0]",

    ## bin13,54
#    "meanP[-0.0,-5.0,5.0]","sigmaP[0.75]",
#    "meanF[-0.0,-5.0,5.0]","sigmaF[0.8]",
#    "acmsP[60.,50.,80.]","betaP[0.05,0.01,0.08]","gammaP[0.1, -2, 2]","peakP[90.0]",
#    "acmsF[60.,50.,80.]","betaF[0.05,0.01,0.08]","gammaF[0.1, -2, 2]","peakF[90.0]",

    ## bin14,55
#    "meanP[-0.0,-5.0,5.0]","sigmaP[0.6]",
#    "meanF[-0.0,-5.0,5.0]","sigmaF[0.7]",
#    "acmsP[60.,50.,80.]","betaP[0.05,0.01,0.08]","gammaP[0.1, -2, 2]","peakP[90.0]",
#    "acmsF[60.,50.,80.]","betaF[0.05,0.01,0.08]","gammaF[0.1, -2, 2]","peakF[90.0]",

    ## bin16,18
#    "meanP[-0.0,-5.0,5.0]","sigmaP[0.75]",
#    "meanF[-0.0,-5.0,5.0]","sigmaF[0.95]",
#    "acmsP[60.,50.,80.]","betaP[0.05,0.01,0.08]","gammaP[0.1, -2, 2]","peakP[90.0]",
#    "acmsF[60.,50.,80.]","betaF[0.05,0.01,0.08]","gammaF[0.1, -2, 2]","peakF[90.0]",

    ## bin27
#    "meanP[-0.0,-5.0,5.0]","sigmaP[1]",
#    "meanF[-0.0,-5.0,5.0]","sigmaF[0.8]",
#    "acmsP[60.,50.,80.]","betaP[0.05,0.01,0.08]","gammaP[0.1, -2, 2]","peakP[90.0]",
#    "acmsF[60.,50.,80.]","betaF[0.05,0.01,0.08]","gammaF[0.1, -2, 2]","peakF[90.0]",

    ## bin31,37,47
#    "meanP[-0.0,-5.0,5.0]","sigmaP[1.1]",
#    "meanF[-0.0,-5.0,5.0]","sigmaF[0.9,0.5,5.0]",
#    "acmsP[60.,50.,80.]","betaP[0.05,0.01,0.08]","gammaP[0.1, -2, 2]","peakP[90.0]",
#    "acmsF[60.,50.,80.]","betaF[0.05,0.01,0.08]","gammaF[0.1, -2, 2]","peakF[90.0]",

    ## bin32,49
#    "meanP[-0.0,-5.0,5.0]","sigmaP[1.1]",
#    "meanF[-0.0,-5.0,5.0]","sigmaF[1.1]",
#    "acmsP[60.,50.,80.]","betaP[0.05,0.01,0.08]","gammaP[0.1, -2, 2]","peakP[90.0]",
#    "acmsF[60.,50.,80.]","betaF[0.05,0.01,0.08]","gammaF[0.1, -2, 2]","peakF[90.0]",

    ## bin33,38
#    "meanP[-0.0,-5.0,5.0]","sigmaP[0.9,0.5,5]",
#    "meanF[-0.0,-5.0,5.0]","sigmaF[0.75]",
#    "acmsP[60.,50.,80.]","betaP[0.05,0.01,0.08]","gammaP[0.1, -2, 2]","peakP[90.0]",
#    "acmsF[60.,50.,80.]","betaF[0.05,0.01,0.08]","gammaF[0.1, -2, 2]","peakF[90.0]",

    ## bin39,43
#    "meanP[-0.0,-5.0,5.0]","sigmaP[0.9,0.5,5]",
#    "meanF[-0.0,-5.0,5.0]","sigmaF[0.9]",
#    "acmsP[60.,50.,80.]","betaP[0.05,0.01,0.08]","gammaP[0.1, -2, 2]","peakP[90.0]",
#    "acmsF[60.,50.,80.]","betaF[0.05,0.01,0.08]","gammaF[0.1, -2, 2]","peakF[90.0]",

    ## bin40
#    "meanP[-0.0,-5.0,5.0]","sigmaP[0.95]",
#    "meanF[-0.0,-5.0,5.0]","sigmaF[1.1]",
#    "acmsP[60.,50.,80.]","betaP[0.05,0.01,0.08]","gammaP[0.1, -2, 2]","peakP[90.0]",
#    "acmsF[60.,50.,80.]","betaF[0.05,0.01,0.08]","gammaF[0.1, -2, 2]","peakF[90.0]",

    ## bin42
#    "meanP[-0.0,-5.0,5.0]","sigmaP[1.5]",
#    "meanF[-0.0,-5.0,5.0]","sigmaF[1.5]",
#    "acmsP[60.,50.,80.]","betaP[0.05,0.01,0.08]","gammaP[0.1, -2, 2]","peakP[90.0]",
#    "acmsF[60.,50.,80.]","betaF[0.05,0.01,0.08]","gammaF[0.1, -2, 2]","peakF[90.0]",

     ## bin46
#    "meanP[-0.0,-5.0,5.0]","sigmaP[0.7]",
#    "meanF[-0.0,-5.0,5.0]","sigmaF[0.95]",
#    "acmsP[60.,50.,80.]","betaP[0.05,0.01,0.08]","gammaP[0.1, -2, 2]","peakP[90.0]",
#    "acmsF[60.,50.,80.]","betaF[0.05,0.01,0.08]","gammaF[0.1, -2, 2]","peakF[90.0]",

    ## bin48
#    "meanP[-0.0,-5.0,5.0]","sigmaP[0.4]",
#    "meanF[-0.0,-5.0,5.0]","sigmaF[0.9,0.5,5.0]",
#    "acmsP[60.,50.,80.]","betaP[0.05,0.01,0.08]","gammaP[0.1, -2, 2]","peakP[90.0]",
#    "acmsF[60.,50.,80.]","betaF[0.05,0.01,0.08]","gammaF[0.1, -2, 2]","peakF[90.0]",

    ## bin50
#    "meanP[-0.0,-5.0,5.0]","sigmaP[1.5]",
#    "meanF[-0.0,-5.0,5.0]","sigmaF[1.3]",
#    "acmsP[60.,50.,80.]","betaP[0.05,0.01,0.08]","gammaP[0.1, -2, 2]","peakP[90.0]",
#    "acmsF[60.,50.,80.]","betaF[0.05,0.01,0.08]","gammaF[0.1, -2, 2]","peakF[90.0]",

    ## bin51
#    "meanP[-0.0,-5.0,5.0]","sigmaP[1.1]",
#    "meanF[-0.0,-5.0,5.0]","sigmaF[1]",
#    "acmsP[60.,50.,80.]","betaP[0.05,0.01,0.08]","gammaP[0.1, -2, 2]","peakP[90.0]",
#    "acmsF[60.,50.,80.]","betaF[0.05,0.01,0.08]","gammaF[0.1, -2, 2]","peakF[90.0]",

    ## bin53
#    "meanP[-0.0,-5.0,5.0]","sigmaP[0.75]",
#    "meanF[-0.0,-5.0,5.0]","sigmaF[0.9,0.5,5.0]",
#    "acmsP[60.,50.,80.]","betaP[0.05,0.01,0.08]","gammaP[0.1, -2, 2]","peakP[90.0]",
#    "acmsF[60.,50.,80.]","betaF[0.03,0.01,0.08]","gammaF[0.1, -2, 2]","peakF[90.0]",

    ## bin56
#    "meanP[-0.0,-5.0,5.0]","sigmaP[0.67]",
#    "meanF[-0.0,-5.0,5.0]","sigmaF[1.2]",
#    "acmsP[60.,50.,80.]","betaP[0.05,0.01,0.08]","gammaP[0.1, -2, 2]","peakP[90.0]",
#    "acmsF[60.,50.,80.]","betaF[0.05,0.01,0.08]","gammaF[0.1, -2, 2]","peakF[90.0]",

    ## bin58
#    "meanP[-0.0,-5.0,5.0]","sigmaP[0.8]",
#    "meanF[-0.0,-5.0,5.0]","sigmaF[1.1]",
#    "acmsP[60.,50.,80.]","betaP[0.05,0.01,0.08]","gammaP[0.1, -2, 2]","peakP[90.0]",
#    "acmsF[60.,50.,80.]","betaF[0.05,0.01,0.08]","gammaF[0.1, -2, 2]","peakF[90.0]",

    ## bin59
#    "meanP[-0.0,-5.0,5.0]","sigmaP[1]",
#    "meanF[-0.0,-5.0,5.0]","sigmaF[1]",
#    "acmsP[60.,50.,80.]","betaP[0.05,0.01,0.08]","gammaP[0.1, -2, 2]","peakP[90.0]",
#    "acmsF[60.,50.,80.]","betaF[0.05,0.01,0.08]","gammaF[0.1, -2, 2]","peakF[90.0]",

    ]

tnpParAltSigFit = [
    ### default
#    "meanP[-0.0,-5.0,5.0]","sigmaP[1,0.7,6.0]","alphaP[2.0,1.2,3.5]" ,'nP[3,-5,5]',"sigmaP_2[1.5,0.5,6.0]","sosP[1,0.5,5.0]",
#    "meanF[-0.0,-5.0,5.0]","sigmaF[2,0.7,15.0]","alphaF[2.0,1.2,3.5]",'nF[3,-5,5]',"sigmaF_2[2.0,0.5,6.0]","sosF[1,0.5,5.0]",
#    "acmsP[60.,50.,75.]","betaP[0.04,0.01,0.06]","gammaP[0.1, 0.005, 1]","peakP[90.0]",
#    "acmsF[60.,50.,75.]","betaF[0.04,0.01,0.06]","gammaF[0.1, 0.005, 1]","peakF[90.0]",

    ### default in Arun's setting
    "meanP[-0.0,-5.0,5.0]","sigmaP[1,0.7,6.0]","alphaP[2.0,1.2,3.5]" ,'nP[3,-5,5]',"sigmaP_2[1.5,0.5,6.0]","sosP[1,0.5,5.0]",
    "meanF[-0.0,-5.0,5.0]","sigmaF[2,0.7,15.0]","alphaF[2.0,1.2,3.5]",'nF[3,-5,5]',"sigmaF_2[2.0,0.5,6.0]","sosF[1,0.5,5.0]",
    "acmsP[60.,50.,75.]","betaP[0.04,0.01,0.06]","gammaP[0.1, 0.005, 1]","peakP[90.0]",
    "acmsF[70.,50.,100.]","betaF[0.04,0.01,0.06]","gammaF[0.1, 0.005, 1]","peakF[90.0]",

    ### for bin 12~29
#    "meanP[-0.0,-5.0,5.0]","sigmaP[1.2,0.7,6.0]","alphaP[2,0.5,3.5]" ,'nP[9,-5,25]',"sigmaP_2[1.2,0.5,6.0]","sosP[1,0.5,5.0]",
#    "meanF[-0.0,-5.0,5.0]","sigmaF[1.2,0.7,15.0]","alphaF[2.1,0.3,3.5]",'nF[10,-5,25]',"sigmaF_2[1.7,0.5,6.0]","sosF[1,0.5,5.0]",
#    "acmsP[60.,50.,75.]","betaP[0.04,0.01,0.06]","gammaP[0.1, 0.005, 1]","peakP[90.0]",
#    "acmsF[70.,50.,100.]","betaF[0.04,0.01,0.06]","gammaF[0.1, 0.005, 1]","peakF[90.0]",

    ### for bin 31~39
    #"meanP[-0.0,-5.0,5.0]","sigmaP[1,0.7,6.0]","alphaP[-1.5,-3,-0.5]" ,'nP[1,-5,5]',"sigmaP_2[1.5,0.5,6.0]","sosP[1,0.5,5.0]",
    #"meanF[-0.0,-5.0,5.0]","sigmaF[1.5,0.7,15.0]","alphaF[-1.5,-3,-0.5]",'nF[1,-5,5]',"sigmaF_2[2,0.5,6.0]","sosF[1,0.5,5.0]",
    #"acmsP[60.,50.,75.]","betaP[0.04,0.01,0.06]","gammaP[0.1, 0.005, 1]","peakP[90.0]",
    #"acmsF[70.,50.,100.]","betaF[0.04,0.01,0.06]","gammaF[0.1, 0.005, 1]","peakF[90.0]",

    ### for bin 40~56
    #"meanP[-0,-5,5]","sigmaP[1.5,0.7,6]","alphaP[2,0.5,3.5]" ,'nP[5,-5,20]',"sigmaP_2[1.5,0.5,6]","sosP[1,0.5,5.0]",
    #"meanF[-0,-5,5]","sigmaF[2,0.7,15]","alphaF[2,0.3,3.5]",'nF[5,-5,20]',"sigmaF_2[2,0.5,6]","sosF[1,0.5,5.0]",
    #"acmsP[60.,50.,75.]","betaP[0.04,0.01,0.06]","gammaP[0.1, 0.005, 1]","peakP[90.0]",
    #"acmsF[70.,50.,100.]","betaF[0.04,0.01,0.06]","gammaF[0.1, 0.005, 1]","peakF[90.0]",

    ### test 00
#    "meanP[-0.0,-5.0,5.0]","sigmaP[1,0.7,6.0]","alphaP[2.0,1.2,3.5]" ,'nP[3,-5,5]',"sigmaP_2[1.5,0.5,6.0]","sosP[1,0.5,5.0]",
#    "meanF[-0.0,-5.0,5.0]","sigmaF[2.7,2.5,3.5]","alphaF[2.0,1.2,3.5]",'nF[3,-5,5]',"sigmaF_2[2.7,2.5,3.5]","sosF[1,0.5,5.0]",

    ### test 01
#    "meanP[-0.0,-5.0,5.0]","sigmaP[2,1,3.5]","alphaP[2.0,1.,3.5]",'nP[3,-5,5]',"sigmaP_2[2,0.5,2.5]","sosP[1,0.5,5.0]",
#    "meanF[-0.0,-5.0,5.0]","sigmaF[2.8,2.5,3.5]","alphaF[2.0,1.2,3.5]",'nF[3,-5,5]',"sigmaF_2[2.8,2.5,3.5]","sosF[1,0.5,5.0]",

    ### test 02
#    "meanP[-0.0,-5.0,5.0]","sigmaP[1.5,0.7,6.0]","alphaP[2.0,1.2,3.5]",'nP[3,-5,5]',"sigmaP_2[1.5,0.5,3.5]","sosP[1,0.5,5.0]",
#    "meanF[-0.0,-5.0,5.0]","sigmaF[2.7,2.5,3.5]","alphaF[2.0,1.2,3.5]",'nF[3,-5,5]',"sigmaF_2[3.5,2.5,4]","sosF[1,0.5,5.0]",

    ### test 03
#    "meanP[-0.0,-5.0,5.0]","sigmaP[1.9,1.5,2.5]","alphaP[2.0,1.2,3.5]",'nP[3,-5,5]',"sigmaP_2[1.9,1.5,2.5]","sosP[1,0.5,5.0]",
#    "meanF[-0.0,-5.0,5.0]","sigmaF[2.7,2.5,3.5]","alphaF[2.0,1.2,3.5]",'nF[3,-5,5]',"sigmaF_2[2.7,2.5,3.5]","sosF[1,0.5,5.0]",

    ### test 04
#    "meanP[-0.0,-5.0,5.0]","sigmaP[1.5,0.7,4.0]","alphaP[2.0,1.2,3.5]",'nP[3,-5,5]',"sigmaP_2[1.5,0.5,4.0]","sosP[1,0.5,5.0]",
#    "meanF[-0.0,-5.0,5.0]","sigmaF[1.,0.7,1.5]","alphaF[2.0,1.2,3.5]",'nF[3,-5,5]',"sigmaF_2[2.1,0.5,2.5]","sosF[1,0.5,5.0]",

    ### test 05
#    "meanP[-0.0,-5.0,5.0]","sigmaP[1.4,0.7,4.0]","alphaP[2.0,1.2,3.5]" ,'nP[3,-5,5]',"sigmaP_2[1.4,0.5,4.0]","sosP[1,0.5,5.0]",
#    "meanF[-0.0,-5.0,5.0]","sigmaF[1.4,0.7,4.0]","alphaF[2.0,1.2,3.5]",'nF[3,-5,5]',"sigmaF_2[1.4,0.5,1.5]","sosF[1,0.5,5.0]",

    ### test 07
#    "meanP[-0.0,-5.0,5.0]","sigmaP[1.5,0.7,6.0]","alphaP[2.0,1.2,3.5]",'nP[3,-5,5]',"sigmaP_2[1.5,0.5,3.3]","sosP[1,0.5,5.0]",
#    "meanF[-0.0,-5.0,5.0]","sigmaF[2.7,2.5,3.5]","alphaF[2.0,1.2,3.5]",'nF[3,-5,5]',"sigmaF_2[3.4,2.5,3.9]","sosF[1,0.5,5.0]",

    ### test 08
#    "meanP[-0.0,-5.0,5.0]","sigmaP[1.5,0.7,4.0]","alphaP[2.0,1.2,3.5]",'nP[3,-5,5]',"sigmaP_2[1.5,0.5,2.9]","sosP[1,0.5,5.0]",
#    "meanF[-0.0,-5.0,5.0]","sigmaF[3.3,3,4.5]","alphaF[2.0,1.2,3.5]",'nF[3,-5,5]',"sigmaF_2[3.3,3,4.5]","sosF[1,0.5,5.0]",

    ### test 11
#    "meanP[-0.0,-5.0,5.0]","sigmaP[1.9,0.7,4.0]","alphaP[2.0,1.2,3.5]",'nP[3,-5,5]',"sigmaP_2[1.9,0.5,4.0]","sosP[1,0.5,5.0]",
#    "meanF[-0.0,-5.0,5.0]","sigmaF[2.2,0.7,4.0]","alphaF[2.0,1.2,3.5]",'nF[3,-5,5]',"sigmaF_2[2.2,0.5,4.0]","sosF[1,0.5,5.0]",

    ### test 12
#    "meanP[-0.0,-5.0,5.0]","sigmaP[1.2,0.7,6.0]","alphaP[2,0.5,3.5]" ,'nP[9,-5,25]',"sigmaP_2[1.2,0.5,6.0]","sosP[1,0.5,5.0]",
#    "meanF[-0.0,-5.0,5.0]","sigmaF[3.5,3,15.0]","alphaF[2.1,0.3,3.5]",'nF[10,5,25]',"sigmaF_2[3.5,3,6.0]","sosF[1,0.5,5.0]",

    ### test 13
#    "meanP[-0.0,-5.0,5.0]","sigmaP[1.6,0.7,4.0]","alphaP[2.0,1.2,3.5]",'nP[3,-5,5]',"sigmaP_2[1.6,0.5,4.0]","sosP[1,0.5,5.0]",
#    "meanF[-0.0,-5.0,5.0]","sigmaF[2,0.7,4.0]","alphaF[2.0,1.2,3.5]",'nF[3,-5,5]',"sigmaF_2[2.0,0.5,4.0]","sosF[1,0.5,5.0]",

    ### test 14
#    "meanP[-0.0,-5.0,5.0]","sigmaP[1.4,0.7,4.0]","alphaP[2.0,1.2,3.5]",'nP[3,-5,5]',"sigmaP_2[1.4,0.5,4.0]","sosP[1,0.5,5.0]",
#    "meanF[-0.0,-5.0,5.0]","sigmaF[2,0.7,4.0]","alphaF[2.0,1.2,3.5]",'nF[3,-5,5]',"sigmaF_2[2.0,0.5,4.0]","sosF[1,0.5,5.0]",

    ### test 15
#    "meanP[-0.0,-5.0,5.0]","sigmaP[1.4,0.7,4.0]","alphaP[2.0,1.2,3.5]",'nP[3,-5,5]',"sigmaP_2[1.4,0.5,4.0]","sosP[1,0.5,5.0]",
#    "meanF[-0.0,-5.0,5.0]","sigmaF[1.6,0.7,4.0]","alphaF[2.0,1.2,3.5]",'nF[3,-5,5]',"sigmaF_2[1.6,0.5,4.0]","sosF[1,0.5,5.0]",

    ### test 17
#    "meanP[-0.0,-5.0,5.0]","sigmaP[1.2,0.7,6.0]","alphaP[2,0.5,3.5]" ,'nP[9,-5,25]',"sigmaP_2[1.2,0.5,6.0]","sosP[1,0.5,5.0]",
#    "meanF[-0.0,-5.0,5.0]","sigmaF[3.5,3,15.0]","alphaF[2.1,0.3,3.5]",'nF[20,15,25]',"sigmaF_2[3.5,3,6.0]","sosF[1,0.5,5.0]",

    ### test 18
#    "meanP[-0.0,-5.0,5.0]","sigmaP[1.8,0.7,4.0]","alphaP[2.0,1.2,3.5]",'nP[3,-5,5]',"sigmaP_2[1.8,0.5,4.0]","sosP[1,0.5,5.0]",
#    "meanF[-0.0,-5.0,5.0]","sigmaF[2.5,0.7,4.0]","alphaF[2.0,1.2,3.5]",'nF[3,0.5,5]',"sigmaF_2[2.5,0.5,4.0]","sosF[1,0.5,5.0]",

    ### test 20
#    "meanP[-0.0,-5.0,5.0]","sigmaP[1.4,0.7,4.0]","alphaP[2.0,1.2,3.5]",'nP[3,-5,5]',"sigmaP_2[1.5,0.5,4.0]","sosP[1,0.5,5.0]",
#    "meanF[-0.0,-5.0,5.0]","sigmaF[1.6,0.7,4.0]","alphaF[2.0,1.2,3.5]",'nF[3,-5,5]',"sigmaF_2[1.6,0.5,4.0]","sosF[1,0.5,5.0]",

    ### test 21
#    "meanP[-0.0,-5.0,5.0]","sigmaP[1.5,0.7,4.0]","alphaP[2.0,1.2,3.5]",'nP[3,-5,5]',"sigmaP_2[1.5,0.5,4.0]","sosP[1,0.5,5.0]",
#    "meanF[-0.0,-5.0,5.0]","sigmaF[2.,0.7,4.0]","alphaF[2.0,1.2,3.5]",'nF[3,-5,5]',"sigmaF_2[2.1,1.0,4.0]","sosF[1,0.5,5.0]",

    ### test 22
#    "meanP[-0.0,-5.0,5.0]","sigmaP[1.3,0.7,4.0]","alphaP[2.0,1.2,3.5]",'nP[3,-5,5]',"sigmaP_2[1.3,0.5,2]","sosP[1,0.5,5.0]",
#    "meanF[-0.0,-5.0,5.0]","sigmaF[3,2,4.0]","alphaF[2.0,1.2,3.5]",'nF[3,-5,5]',"sigmaF_2[3,0.5,4]","sosF[1,0.5,5.0]",

    ### test 24
#    "meanP[-0.0,-5.0,5.0]","sigmaP[1,0.7,4.0]","alphaP[2.0,1.2,3.5]",'nP[3,-5,5]',"sigmaP_2[1,0.5,4.0]","sosP[1,0.5,5.0]",
#    "meanF[-0.0,-5.0,5.0]","sigmaF[1.6,0.7,4.0]","alphaF[2.0,1.2,3.5]",'nF[3,-5,5]',"sigmaF_2[1.6,0.5,4.0]","sosF[1,0.5,5.0]",

    ### test 25
#    "meanP[-0.0,-5.0,5.0]","sigmaP[1,0.7,4.0]","alphaP[2.0,1.2,3.5]",'nP[3,-5,5]',"sigmaP_2[1,0.5,4.0]","sosP[1,0.5,5.0]",
#    "meanF[-0.0,-5.0,5.0]","sigmaF[1.1,0.7,4.0]","alphaF[2.0,1.2,3.5]",'nF[3,-5,5]',"sigmaF_2[1.1,0.5,4.0]","sosF[1,0.5,5.0]",

    ### test 
#    "meanP[-0.0,-5.0,5.0]","sigmaP[1.5,0.7,4.0]","alphaP[2.0,1.2,3.5]",'nP[3,-5,5]',"sigmaP_2[1.5,0.5,4.0]","sosP[1,0.5,5.0]",
#    "meanF[-0.0,-5.0,5.0]","sigmaF[2,0.7,4.0]","alphaF[2.0,1.2,3.5]",'nF[3,-5,5]',"sigmaF_2[2.0,0.5,4.0]","sosF[1,0.5,5.0]",

    ### test 
#    "meanP[-0.0,-5.0,5.0]","sigmaP[1.5,0.7,4.0]","alphaP[2.0,1.2,3.5]",'nP[3,-5,5]',"sigmaP_2[1.5,0.5,4.0]","sosP[1,0.5,5.0]",
#    "meanF[-0.0,-5.0,5.0]","sigmaF[2,0.7,4.0]","alphaF[2.0,1.2,3.5]",'nF[3,-5,5]',"sigmaF_2[2.0,0.5,4.0]","sosF[1,0.5,5.0]",

#    "acmsP[60.,50.,75.]","betaP[0.04,0.01,0.06]","gammaP[0.1, 0.005, 1]","peakP[90.0]",
#    "acmsF[60.,50.,75.]","betaF[0.04,0.01,0.06]","gammaF[0.1, 0.005, 1]","peakF[90.0]",

    ]
     
tnpParAltBkgFit = [
    "meanP[-0.0,-5.0,5.0]","sigmaP[0.9,0.5,5.0]",
    "meanF[-0.0,-5.0,5.0]","sigmaF[0.9,0.5,5.0]",
    "alphaP[0.,-5.,5.]",
    "alphaF[0.,-5.,5.]",
    ]
        
