##################################################################
# -- This is used to make pile up reweight tree. --------------- #
# -- Usage: 1. ssh -Y dmpai@147.47.50.161                        #
#           2. su root                                           #
#           3. source /usr/local/ROOT/builddir/bin/thisroot.sh   #
#           4. cd /home/dmpai/TnP/ega_tnp_analysis               #
#           5. python pureweight.py                              #
#                                                                #
# -- Author: Dalmin Pai                                          #
##################################################################

import libPython.puReweighter as pu
#import etc.inputs.tnpSampleDef as tnpSamples
#import etc.inputs.tnpSampleDef_my as tnpSamples
import etc.inputs.tnpSampleDef_HN as tnpSamples
from libPython.tnpClassUtils import mkdir


puType = 0

#for sName in tnpSamples.Moriond17_80X.keys():    
#    sample = tnpSamples.Moriond17_80X[sName]
#for sName in tnpSamples.Moriond17_80X_my.keys():    
#    sample = tnpSamples.Moriond17_80X_my[sName]
for sName in tnpSamples.Moriond17_80X_HN.keys():    
    sample = tnpSamples.Moriond17_80X_HN[sName]
    if sample is None : continue
#    if not 'rec' in sName : continue
    if not 'Winter17' in sName : continue
#    if not 'DYee_powheg_Winter17' in sName: continue
    if not sample.isMC: continue
    
    trees = {}
#    trees['ele'] = 'GsfElectronToEleID'
    trees['ele'] = 'tnpEleIDs'
#    trees['pho'] = 'GsfElectronToPhoID'
#    trees['rec'] = 'GsfElectronToSC'
    for tree in trees:
#        dirout =  'eos/cms//store/group/phys_egamma/tnp/80X/pu/Winter17/'
#        dirout =  '/home/dmpai/pu/myWinter17/'
        dirout =  '/home/dmpai/pu/HNWinter17/'
        mkdir(dirout)
        
        if   puType == 0 : sample.set_puTree( dirout + '%s_%s.pu.puTree.root'   % (sample.name,tree) )
        elif puType == 1 : sample.set_puTree( dirout + '%s_%s.nVtx.puTree.root' % (sample.name,tree) )
        elif puType == 2 : sample.set_puTree( dirout + '%s_%s.rho.puTree.root'  % (sample.name,tree) )
        sample.set_tnpTree(trees[tree]+'/fitter_tree')
        sample.dump()
        pu.reweight(sample, puType )
    
