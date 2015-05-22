import FWCore.ParameterSet.Config as cms

from Configuration.Generator.HerwigppDefaults_cfi import *
from Configuration.Generator.HerwigppUE_EE_5C_cfi import *
from Configuration.Generator.HerwigppPDF_CTEQ6_LO_cfi import *									# Import CTEQ6L PDF as shower pdf
from Configuration.Generator.HerwigppEnergy_13TeV_cfi import *
from Configuration.Generator.HerwigppLHEFile_cfi import *
from Configuration.Generator.HerwigppMPI_SwitchOff_cfi import *

generator = cms.EDFilter("ThePEGHadronizerFilter",
	herwigDefaultsBlock,
	herwigppUESettingsBlock,
	herwigppPDFSettingsBlock,
	herwigppEnergySettingsBlock,
	herwigppLHEFileSettingsBlock,
	herwigppMPISettingsBlock,

	configFiles = cms.vstring(),
	parameterSets = cms.vstring(
		'hwpp_cmsDefaults',
		'hwpp_ue_EE5C',
		'hwpp_cm_13TeV',
		'hwpp_pdf_CTEQ6L1',			# Shower PDF matching with the tune
		'hwpp_LHE_MadGraph',
		'hwpp_mpi_switchOff',
	),

        crossSection = cms.untracked.double(-1),
        filterEfficiency = cms.untracked.double(1.0),
)
ProductionFilterSequence = cms.Sequence(generator)
