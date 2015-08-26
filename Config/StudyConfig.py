__author__ = 'Sulantha'

AllowedStudyList = ['ADNI', 'ADNI_OLD']
AllowedStepsList = ['Sort', 'Move', 'T1Beast', 'T1Process', 'ProcessAV45', 'ProcessFDG', 'ProcessFMRI', 'ProcessDTI']
AllowedVersions = ['1', '2', '3']
AllowedModalityList = ['T1', 'AV45', 'FDG', 'MT1__GradWarp__N3m', 'MT1__N3m']


ProcessingModalityAndPipelineTypePerStudy = dict(ADNI={'AV45':'AV45',
                                            'FDG':'FDG',
                                            'T1':'T1',
                                            'MPR':'T1',
                                            'MPR_N3':'T1',
                                            'MPR_B1':'T1',
                                            'MPR_B1_N3':'T1',
                                            'MPR_B1_N3S':'T1',
                                            'MPR-R_B1_N3':'T1',
                                            'MPR-R':'T1',
                                            'MPR-R_N3':'T1',
                                            'MPR_N3S':'T1',
                                            'MPR-R_N3S':'T1',
                                            'MPR-R_B1':'T1',
                                            'MPR-R_B1_N3S':'T1',
                                            'MT1_G_N3m':'T1',
                                            'MT1_N3m':'T1',
                                            'T1-SNMN3C':'T1',
                                            'MPR-R__N3':'T1',
                                            'MPR__N3S':'T1',
                                            'MPR__N3':'T1',
                                            'S_IR-SPGR':'T1',
                                            'AS_IR-SPGR':'T1',
                                            'AS_IR-FSPGR':'T1',
                                            'S_IR-FSPGR':'T1',
                                            'IR-FSPGR':'T1',
                                            'IR-FSPGR_Rep':'T1',
                                            'ext-rsfmri':'FMRI',
                                            'rsfmri':'FMRI',
                                            'A_rsfmri_EO':'FMRI'
                                                })

#This versioning dict should have an entry if the default processing version is not V1 - Still in test.
defaultVersioningForStudy = dict(ADNI={'T1': 'V1', 'AV45': 'V1', 'FDG': 'V1', 'MT1_G_N3m': 'V1', 'MT1_N3m': 'V1',
                                       'rsfmri': 'V1', 'ext-rsfmri': 'V1'})

ADNIDownloadRoot = '/data/backup-data02/ADNI/downloads/New2'
ADNIOLDDownloadRoot = '/data/backup-data02/ADNI/new_raw/EMCI'


studyDatabaseRootDict = dict(ADNI='/data/data03/Database', ADNI_OLD='/data/data03/Database')
