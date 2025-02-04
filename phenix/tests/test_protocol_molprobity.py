# ***************************************************************************
# * Authors:    Marta Martinez (mmmtnez@cnb.csic.es)
# *             Roberto Marabini (roberto@cnb.csic.es)
# *
# *
# * This program is free software; you can redistribute it and/or modify
# * it under the terms of the GNU General Public License as published by
# * the Free Software Foundation; either version 2 of the License, or
# * (at your option) any later version.
# *
# * This program is distributed in the hope that it will be useful,
# * but WITHOUT ANY WARRANTY; without even the implied warranty of
# * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# * GNU General Public License for more details.
# *
# * You should have received a copy of the GNU General Public License
# * along with this program; if not, write to the Free Software
# * Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA
# * 02111-1307  USA
# *
# *  All comments concerning this program package may be sent to the
# *  e-mail address 'scipion@cnb.csic.es'
# ***************************************************************************/

# protocol to test the validation method MolProbity
from chimera.protocols import ChimeraProtOperate
from pwem.protocols.protocol_import import (ProtImportPdb,
                                                    ProtImportVolumes)
from phenix.protocols.protocol_molprobity import PhenixProtRunMolprobity
from pyworkflow.tests import *
from phenix import PHENIXVERSION18, Plugin


class TestImportBase(BaseTest):
    @classmethod
    def setUpClass(cls):
        setupTestProject(cls)
        cls.dsModBuild = DataSet.getDataSet('model_building_tutorial')


class TestImportData(TestImportBase):
    """ Import map volumes and atomic structures(PDBx/mmCIF files)
    """

    def _importVolume(self):
        args = {'filesPath': self.dsModBuild.getFile('volumes/1ake_4-5A.mrc'),
                'samplingRate': 1.5,
                'setOrigCoord': False
                }
        protImportVol = self.newProtocol(ProtImportVolumes, **args)
        protImportVol.setObjLabel('import volume 1ake_4-5A\n with default '
                                  'origin\n')
        self.launchProtocol(protImportVol)
        volume = protImportVol.outputVolume
        return volume

    def _importVolume3(self):
        args = {'filesPath': self.dsModBuild.getFile(
            'volumes/emd_4116.map'),
                'samplingRate': 0.637,
                'setOrigCoord': False
                }
        protImportVol = self.newProtocol(ProtImportVolumes, **args)
        protImportVol.setObjLabel('import volume emd_4116\nwith default '
                                  'origin\n')
        self.launchProtocol(protImportVol)
        volume3 = protImportVol.outputVolume
        return volume3

    def _importVolCoot1(self):
        args = {'filesPath': self.dsModBuild.getFile(
            'volumes/coot1.mrc'),
            'samplingRate': 1.5,
            'setOrigCoord': False
            }
        protImportVol = self.newProtocol(ProtImportVolumes, **args)
        protImportVol.setObjLabel('import volume coot1.mrc\set'
                                  'origin default\n')
        self.launchProtocol(protImportVol)
        volume_coot1 = protImportVol.outputVolume
        return volume_coot1

    def _importVolCoot2(self):
        args = {'filesPath': self.dsModBuild.getFile(
            'volumes/coot2.mrc'),
            'samplingRate': 1.5,
            'setOrigCoord': True,
            'x': 12.0,
            'y': -7.5,
            'z': 10.5
            }
        protImportVol = self.newProtocol(ProtImportVolumes, **args)
        protImportVol.setObjLabel('import volume coot2.mrc\nset '
                                  'origin 12.0 -7.5 10.5\n')
        self.launchProtocol(protImportVol)
        volume_coot2 = protImportVol.outputVolume
        return volume_coot2

    def _importVolRefmac1(self):
        args = {'filesPath': self.dsModBuild.getFile(
            'volumes/refmac1.mrc'),
            'samplingRate': 1.5,
            'setOrigCoord': False
            }
        protImportVol = self.newProtocol(ProtImportVolumes, **args)
        protImportVol.setObjLabel('import volume refmac1.mrc\nset '
                                  'origin default\n')
        self.launchProtocol(protImportVol)
        volume_refmac1 = protImportVol.outputVolume
        return volume_refmac1

    def _importVolRefmac2(self):
        args = {'filesPath': self.dsModBuild.getFile(
            'volumes/refmac2.mrc'),
            'samplingRate': 1.5,
            'setOrigCoord': True,
            'x': 12.0,
            'y': -7.5,
            'z': 10.5
        }
        protImportVol = self.newProtocol(ProtImportVolumes, **args)
        protImportVol.setObjLabel('import volume refmac2.mrc\nset '
                                  'origin 12.0 -7.5 10.5\n')
        self.launchProtocol(protImportVol)
        volume_refmac2 = protImportVol.outputVolume
        return volume_refmac2

    def _importVolRefmac3(self):
        args = {'filesPath': self.dsModBuild.getFile(
            'volumes/refmac3.mrc'),
            'samplingRate': 1.5,
            'setOrigCoord': True,
            'x': 37.5,
            'y': 37.5,
            'z': 37.5
        }
        protImportVol = self.newProtocol(ProtImportVolumes, **args)
        protImportVol.setObjLabel('import volume refmac3.mrc\nset '
                                  'origin 37.5 37.5 37.5\n')
        self.launchProtocol(protImportVol)
        volume_refmac3 = protImportVol.outputVolume
        return volume_refmac3

    def _importStructurePDBWoVol(self):
        args = {'inputPdbData': ProtImportPdb.IMPORT_FROM_FILES,
                'pdbFile': self.dsModBuild.getFile(
                    'PDBx_mmCIF/1ake_start.pdb')
                }
        protImportPDB = self.newProtocol(ProtImportPdb, **args)
        protImportPDB.setObjLabel('import pdb\n 1ake_start')
        self.launchProtocol(protImportPDB)
        structure1_PDB = protImportPDB.outputPdb
        return structure1_PDB

    def _importStructurePDBWithVol(self):
        args = {'inputPdbData': ProtImportPdb.IMPORT_FROM_FILES,
                'pdbFile': self.dsModBuild.getFile(
                    'PDBx_mmCIF/1ake_start.pdb'),
                'inputVolume': self._importVolume()
                }
        protImportPDB = self.newProtocol(ProtImportPdb, **args)
        protImportPDB.setObjLabel('import pdb\n volume associated\n 1ake_start')
        self.launchProtocol(protImportPDB)
        structure2_PDB = protImportPDB.outputPdb
        self.assertTrue(structure2_PDB.getFileName())
        return structure2_PDB

    def _importStructuremmCIFWithVol2(self):
        args = {'inputPdbData': ProtImportPdb.IMPORT_FROM_ID,
                'pdbId': '5ni1',
                'inputVolume': self._importVolume3()
                }
        protImportPDB = self.newProtocol(ProtImportPdb, **args)
        protImportPDB.setObjLabel('import mmCIF\nvolume associated\n5ni1.cif')
        self.launchProtocol(protImportPDB)
        structure_6 = protImportPDB.outputPdb
        self.assertTrue(structure_6.getFileName())
        return structure_6

    def _importStructurePDBWoVol2(self):
        args = {'inputPdbData': ProtImportPdb.IMPORT_FROM_FILES,
                'pdbFile': self.dsModBuild.getFile(
                    'PDBx_mmCIF/3i3e_fitted.pdb'),
                }
        protImportPDB = self.newProtocol(ProtImportPdb, **args)
        protImportPDB.setObjLabel('import pdb\n 3i3e_fitted')
        self.launchProtocol(protImportPDB)
        structure5_PDB = protImportPDB.outputPdb
        return structure5_PDB

    def _importStructureMolProbity1(self):
        args = {'inputPdbData': ProtImportPdb.IMPORT_FROM_FILES,
                'pdbFile': self.dsModBuild.getFile(
                    'PDBx_mmCIF/jlv_chimeraOut0001.pdb'),
                }
        protImportPDB = self.newProtocol(ProtImportPdb, **args)
        protImportPDB.setObjLabel('import pdb\n jlv_chimeraOut0001')
        self.launchProtocol(protImportPDB)
        structure6_PDB = protImportPDB.outputPdb
        return structure6_PDB

    def _importStructureMolProbity2(self):
        args = {'inputPdbData': ProtImportPdb.IMPORT_FROM_FILES,
                'pdbFile': self.dsModBuild.getFile(
                    'PDBx_mmCIF/jlv_cootOut0016.pdb'),
                }
        protImportPDB = self.newProtocol(ProtImportPdb, **args)
        protImportPDB.setObjLabel('import pdb\n jlv_cootOut0016')
        self.launchProtocol(protImportPDB)
        structure7_PDB = protImportPDB.outputPdb
        return structure7_PDB

    def _importStructCoot1(self):
        args = {'inputPdbData': ProtImportPdb.IMPORT_FROM_FILES,
                'pdbFile': self.dsModBuild.getFile(
                    'PDBx_mmCIF/coot1.pdb'),
                }
        protImportPDB = self.newProtocol(ProtImportPdb, **args)
        protImportPDB.setObjLabel('import pdb\n coot1.pdb')
        self.launchProtocol(protImportPDB)
        structure_coot1 = protImportPDB.outputPdb
        return structure_coot1

    def _importStructCoot2(self):
        args = {'inputPdbData': ProtImportPdb.IMPORT_FROM_FILES,
                'pdbFile': self.dsModBuild.getFile(
                    'PDBx_mmCIF/coot2.pdb'),
                }
        protImportPDB = self.newProtocol(ProtImportPdb, **args)
        protImportPDB.setObjLabel('import pdb\n coot2.pdb')
        self.launchProtocol(protImportPDB)
        structure_coot2 = protImportPDB.outputPdb
        return structure_coot2

    def _importStructRefmac1(self):
        args = {'inputPdbData': ProtImportPdb.IMPORT_FROM_FILES,
                'pdbFile': self.dsModBuild.getFile(
                    'PDBx_mmCIF/refmac1.pdb'),
                }
        protImportPDB = self.newProtocol(ProtImportPdb, **args)
        protImportPDB.setObjLabel('import pdb\n refmac1.pdb')
        self.launchProtocol(protImportPDB)
        structure_refmac1 = protImportPDB.outputPdb
        return structure_refmac1

    def _importStructRefmac2(self):
        args = {'inputPdbData': ProtImportPdb.IMPORT_FROM_FILES,
                'pdbFile': self.dsModBuild.getFile(
                    'PDBx_mmCIF/refmac2.pdb'),
                }
        protImportPDB = self.newProtocol(ProtImportPdb, **args)
        protImportPDB.setObjLabel('import pdb\n refmac2.pdb')
        self.launchProtocol(protImportPDB)
        structure_refmac2 = protImportPDB.outputPdb
        return structure_refmac2

    def _importStructRefmac3(self):
        args = {'inputPdbData': ProtImportPdb.IMPORT_FROM_FILES,
                'pdbFile': self.dsModBuild.getFile(
                    'PDBx_mmCIF/refmac3.pdb'),
                }
        protImportPDB = self.newProtocol(ProtImportPdb, **args)
        protImportPDB.setObjLabel('import pdb\n refmac3.pdb')
        self.launchProtocol(protImportPDB)
        structure_refmac3 = protImportPDB.outputPdb
        return structure_refmac3

class TestMolprobityValidation2(TestImportData):
    """ Test the protocol of MolProbity validation
    """
    def checkResults(self, ramOutliers, ramFavored, rotOutliers, cbetaOutliers,
                     clashScore, overallScore, protMolProbity, places=0):
        # method to check MolProbity statistic results of the Final Results
        # Table
        try:
            self.assertAlmostEqual(protMolProbity.ramachandranOutliers.get(),
                                   ramOutliers, places)
            self.assertAlmostEqual(protMolProbity.ramachandranFavored.get(),
                                   ramFavored, places)
            self.assertAlmostEqual(protMolProbity.rotamerOutliers.get(),
                                   rotOutliers, places)
            self.assertAlmostEqual(protMolProbity.cbetaOutliers.get(),
                                   cbetaOutliers, places)
            self.assertAlmostEqual(protMolProbity.clashscore.get(),
                                   clashScore, places)
            self.assertAlmostEqual(protMolProbity.overallScore.get(),
                                   overallScore, places)
        except Exception as e:
            # print error since test does not print it
            print(("Exception error:", str(e)))
            raise self.failureException(str(e))
        
    def testMolProbityValidationFromPDB(self):
        """ This test checks that MolProbity validation protocol runs with an
        atomic structure; No Volume was provided and no error message is
        expected"""
        print("Run MolProbity validation protocol from imported pdb file " \
              "without imported or pdb-associated volume")

        # import PDB
        structure_PDB = self._importStructurePDBWoVol()
        self.assertTrue(structure_PDB.getFileName())
        self.assertFalse(structure_PDB.getVolume())
        args = {'inputStructure': structure_PDB,
                'numberOfThreads': 4
                }

        protMolProbity = self.newProtocol(PhenixProtRunMolprobity, **args)
        protMolProbity.setObjLabel('Molprobity validation\n'
                                   'no volume associated to pdb\n')
        self.launchProtocol(protMolProbity)

        # check MolProbity results
        self.checkResults(ramOutliers=0.94,
                          ramFavored=81.60,
                          rotOutliers=3.98,
                          cbetaOutliers=0,
                          clashScore=4.77,
                          overallScore=2.42,
                          protMolProbity=protMolProbity)

    def testMolProbityValidationFromVolume(self):
        """ This test checks that MolProbity validation protocol runs with a
        density volume; No atomic structure was provided and a error message is
        expected"""

        print("Run MolProbity validation protocol from imported volume file " \
              "without imported pdb")

        # import volume
        volume = self._importVolume()
        self.assertTrue(volume.getFileName())

        args = {'inputVolume': volume,
                'resolution': 3.5,
                'numberOfThreads': 4
               }

        protMolProbity = self.newProtocol(PhenixProtRunMolprobity, **args)
        protMolProbity.setObjLabel(
            'Molprobity validation\n volume and no pdb\n')

        try:
            self.launchProtocol(protMolProbity)
        except Exception as e:
            self.assertTrue(True)
            print("This test should return a error message as '" \
                  " Input atomic structure cannot be EMPTY.\n")

            return
        self.assertTrue(False)

    def testMolProbityValidationFromVolAssociatedToPDB(self):
        """ This test checks that MolProbity validation protocol runs with an
        atomic structure associated to volume
        """
        print("Run MolProbity validation protocol from imported pdb file " \
              "with pdb-associated volume")

        # import PDB
        structure2_PDB = self._importStructurePDBWithVol()
        self.assertTrue(structure2_PDB.getFileName())
        self.assertTrue(structure2_PDB.getVolume())

        # MolProbity
        args = {
                'resolution': 3.5,
                'inputStructure': structure2_PDB,
                'numberOfThreads': 4
                }
        protMolProbity = self.newProtocol(PhenixProtRunMolprobity, **args)
        protMolProbity.setObjLabel('MolProbity validation\n'
                                   'volume associated to pdb\nGood '
                                   'validation/bad correlation\n')
        self.launchProtocol(protMolProbity)

        # check MolProbity results
        self.checkResults(ramOutliers=0.94,
                          ramFavored=81.60,
                          rotOutliers=3.98,
                          cbetaOutliers=0,
                          clashScore=4.77,
                          overallScore=2.42,
                          protMolProbity=protMolProbity)

    def testMolProbityValidationFromVolAssociatedToCIF(self):
        """ This test checks that MolProbity validation protocol runs with an
        atomic structure associated to volume
        """
        print("Run MolProbity validation protocol from imported cif file " \
              "with cif-associated volume")

        # import PDB
        structure_6 = self._importStructuremmCIFWithVol2()
        self.assertTrue(structure_6.getFileName())
        self.assertTrue(structure_6.getVolume())

        # chimera operate to repair cif file
        extraCommands = ""
        extraCommands += "scipionwrite #3 " \
                         "prefix repaired_CIF_ChimeraX_\n"
        extraCommands += "exit\n"

        args = {'extraCommands': extraCommands,
                'pdbFileToBeRefined': structure_6
                }
        protChimera = self.newProtocol(ChimeraProtOperate, **args)
        protChimera.setObjLabel('chimera operate\n repairing CIF\n')
        self.launchProtocol(protChimera)
        result = eval("protChimera.repaired_CIF_ChimeraX_Atom_struct__3_%06d" % \
                      protChimera.getObjId())

        # MolProbity
        args = {
                'resolution': 2.2,
                'inputStructure': result,
                'numberOfThreads': 4
                }
        protMolProbity = self.newProtocol(PhenixProtRunMolprobity, **args)
        protMolProbity.setObjLabel('MolProbity validation\n'
                                   'volume associated to cif\nGood '
                                   'validation/bad correlation\n')
        self.launchProtocol(protMolProbity)

        # check MolProbity results
        self.checkResults(ramOutliers=0.00,
                          ramFavored=95.23,
                          rotOutliers=0.43,
                          cbetaOutliers=0,
                          clashScore=3.53,
                          overallScore=1.48,
                          protMolProbity=protMolProbity)

    def testMolProbityValidationFromVolumeAndPDB1(self):
        """ This test checks that MolProbity validation protocol runs with a
        volume provided directly as inputVol, the input PDB was fitted to
        the volume and refined previously by coot
         """
        print("Run MolProbity validation from imported volume and pdb file " \
              "previously fitted and refined by Coot")

        # Import Volume
        volume_coot1 = self._importVolCoot1()

        # import PDB
        structure_coot1 = self._importStructCoot1()

        # MolProbity
        args = {'inputVolume': volume_coot1,
                'resolution': 3.5,
                'inputStructure': structure_coot1,
                'numberOfThreads': 4
                }
        protMolProbity = self.newProtocol(PhenixProtRunMolprobity, **args)
        protMolProbity.setObjLabel('MolProbity validation\n coot1.mrc and '
                                   'coot1.pdb\n')
        self.launchProtocol(protMolProbity)

        # check MolProbity results
        self.checkResults(ramOutliers=0.94,
                          ramFavored=81.60,
                          rotOutliers=3.98,
                          cbetaOutliers=0,
                          clashScore=4.77,
                          overallScore=2.42,
                          protMolProbity=protMolProbity)

    def testMolProbityValidationFromVolumeAndPDB2(self):
        """ This test checks that MolProbity validation protocol runs with a
        volume provided directly as inputVol, the input PDB was fitted to
        the volume and refined previously by coot
         """
        print("Run MolProbity validation from imported volume and pdb file " \
              "previously fitted and refined by Coot")

        # Import Volume
        volume_coot2 = self._importVolCoot2()

        # import PDB
        structure_coot2 = self._importStructCoot2()

        # MolProbity
        args = {'inputVolume': volume_coot2,
                'resolution': 3.5,
                'inputStructure': structure_coot2,
                'numberOfThreads': 4
                }
        protMolProbity = self.newProtocol(PhenixProtRunMolprobity, **args)
        protMolProbity.setObjLabel('MolProbity validation\n coot2.mrc and '
                                   'coot2.pdb\n')
        self.launchProtocol(protMolProbity)

        # check MolProbity results
        self.checkResults(ramOutliers=0.94,
                          ramFavored=81.60,
                          rotOutliers=3.98,
                          cbetaOutliers=0,
                          clashScore=4.77,
                          overallScore=2.42,
                          protMolProbity=protMolProbity)

    def testMolProbityValidationFromVolumeAndPDB3(self):
        """ This test checks that MolProbity validation protocol runs with a
        volume provided directly as inputVol, the input PDB was fitted to
        the volume and refined previously by coot and refmac withouth mask
         """
        print("Run MolProbity validation from imported volume and pdb file " \
              "previously fitted and refined by Coot and Refmac without mask")

        # Import Volume
        volume_refmac1 = self._importVolRefmac1()

        # import PDB
        structure_refmac1 = self._importStructRefmac1()

        # MolProbity
        args = {'inputVolume': volume_refmac1,
                'resolution': 3.5,
                'inputStructure': structure_refmac1,
                'numberOfThreads': 4
                }
        protMolProbity = self.newProtocol(PhenixProtRunMolprobity, **args)
        protMolProbity.setObjLabel('MolProbity validation\n refmac1.mrc and '
                                   'refmac1.pdb\n')
        self.launchProtocol(protMolProbity)

        # check MolProbity results
        self.checkResults(ramOutliers=0.47,
                          ramFavored=84.43,
                          rotOutliers=6.25,
                          cbetaOutliers=1,
                          clashScore=4.77,
                          overallScore=2.52,
                          protMolProbity=protMolProbity)

    def testMolProbityValidationFromVolumeAndPDB4(self):
        """ This test checks that MolProbity validation protocol runs with a
        volume provided directly as inputVol, the input PDB was fitted to
        the volume and refined previously by coot and refmac withouth mask
         """
        print("Run MolProbity validation from imported volume and pdb file " \
              "previously fitted and refined by Coot and Refmac without mask")

        # Import Volume
        volume_refmac2 = self._importVolRefmac2()

        # import PDB
        structure_refmac2 = self._importStructRefmac2()

        # MolProbity
        args = {'inputVolume': volume_refmac2,
                'resolution': 3.5,
                'inputStructure': structure_refmac2,
                'numberOfThreads': 4
                }
        protMolProbity = self.newProtocol(PhenixProtRunMolprobity, **args)
        protMolProbity.setObjLabel('MolProbity validation\n refmac2.mrc and '
                                   'refmac2.pdb\n')
        self.launchProtocol(protMolProbity)

        # check MolProbity results
        self.checkResults(ramOutliers=0.47,
                          ramFavored=83.49,
                          rotOutliers=5.11,
                          cbetaOutliers=1,
                          clashScore=5.07,
                          overallScore=2.49,
                          protMolProbity=protMolProbity)

    def testMolProbityValidationFromVolumeAndPDB5(self):
        """ This test checks that MolProbity validation protocol runs with a
        volume provided directly as inputVol, the input PDB was fitted to
        the volume and refined previously by coot and refmac withouth mask
         """
        print("Run MolProbity validation from imported volume and pdb file " \
              "previously fitted and refined by Coot and Refmac without mask")

        # Import Volume
        volume_refmac3 = self._importVolRefmac3()

        # import PDB
        structure_refmac3 = self._importStructRefmac3()

        # MolProbity
        args = {'inputVolume': volume_refmac3,
                'resolution': 3.5,
                'inputStructure': structure_refmac3,
                'numberOfThreads': 4
                }
        protMolProbity = self.newProtocol(PhenixProtRunMolprobity, **args)
        protMolProbity.setObjLabel('MolProbity validation\n refmac3.mrc and '
                                   'refmac3.pdb\n')
        self.launchProtocol(protMolProbity)

        # check MolProbity results
        self.checkResults(ramOutliers=0.47,
                          ramFavored=83.96,
                          rotOutliers=5.68,
                          cbetaOutliers=1,
                          clashScore=4.77,
                          overallScore=2.50,
                          protMolProbity=protMolProbity)

    def testMolProbityValidationSeveralChains(self):
        """ This test checks that MolProbity validation protocol runs with a
        volume provided directly as inputVol, the input PDB was fitted to
        the volume and refined previously by coot and refmac in another project
         """
        print("Run MolProbity validation from imported volume and pdb file " \
              "already refined by Coot and Refmac in another project")

        # Import Volume
        volume3 = self._importVolume3()

        # import PDB
        structure5_PDB = self._importStructurePDBWoVol2()

        # MolProbity
        args = {'inputVolume': volume3,
                'resolution': 2.2,
                'inputStructure': structure5_PDB,
                'numberOfThreads': 4
                }
        protMolProbity = self.newProtocol(PhenixProtRunMolprobity, **args)
        protMolProbity.setObjLabel('MolProbity validation\n volume and pdb\n')
        self.launchProtocol(protMolProbity)

        # check MolProbity results
        if Plugin.getPhenixVersion() == PHENIXVERSION18:
            self.checkResults(ramOutliers=0.12,
                              ramFavored=95.86,
                              rotOutliers=0.52,
                              cbetaOutliers=0,
                              clashScore=9.70,
                              overallScore=1.80,
                              protMolProbity=protMolProbity)
        else:
            self.checkResults(ramOutliers=0.12,
                              ramFavored=95.86,
                              rotOutliers=0.52,
                              cbetaOutliers=0,
                              clashScore=9.74,
                              overallScore=1.80,
                              protMolProbity=protMolProbity)

    def testMolProbityValidationManyOutliers1(self):
        """ This test checks that MolProbity validation protocol runs with
        two independent pdbs provided directly without inputVol associated and
        allows the comparison of results
         """
        print("Run MolProbity validation to compare an imported pdb " \
              "files obtained in another project")

        # import first PDB
        structure6_PDB = self._importStructureMolProbity1()

        # MolProbity
        args = {
                'inputStructure': structure6_PDB,
                'numberOfThreads': 4
                }
        protMolProbity = self.newProtocol(PhenixProtRunMolprobity, **args)
        protMolProbity.setObjLabel('MolProbity validation\n pdb\n')
        self.launchProtocol(protMolProbity)

        # check MolProbity results
        self.checkResults(ramOutliers=0.20,
                          ramFavored=97.35,
                          rotOutliers=12.24,
                          cbetaOutliers=0,
                          clashScore=130.72,
                          overallScore=3.53,
                          protMolProbity=protMolProbity)

    def testMolProbityValidationManyOutliers2(self):
        """ This test checks that MolProbity validation protocol runs with
        two independent pdbs provided directly without inputVol associated and
        allows the comparison of results
            """
        print("Run MolProbity validation to compare an imported pdb " \
                  "files obtained in another project")

        # import second PDB (with higher number of Outliers)
        structure7_PDB = self._importStructureMolProbity2()

        # MolProbity
        args = {
                'inputStructure': structure7_PDB,
                'numberOfThreads': 4
                }
        protMolProbity = self.newProtocol(PhenixProtRunMolprobity, **args)
        protMolProbity.setObjLabel('MolProbity validation\n pdb\n')
        self.launchProtocol(protMolProbity)

        # check MolProbity results
        self.checkResults(ramOutliers=3.82,
                          ramFavored=89.09,
                          rotOutliers=31.35,
                          cbetaOutliers=746,
                          clashScore=276.52,
                          overallScore=4.61,
                          protMolProbity=protMolProbity)

