__author__ = 'wang'

fileExtensionDict = {'dcm': 'dicom',
                     'dcm.gz': 'dicom',
                     'nii': 'nifti',
                     'nii.gz': 'nifti',
                     'mnc': 'minc',
                     'mnc.gz': 'minc',
                     'v': 'v'}

fileExtensionTuple = ('.nii', '.dcm', '.mnc', '.nii.gz', '.dcm.gz', '.mnc.gz', '.v', '.v.gz')

scanTypeDict = {'4x5minute_frames_4i_16s__AV45': 'AV45',
                '4x5minute_frames_-_Iter_Bra_AV45': 'AV45',
                '50-70_min_dynamic-3D_4i_16s_AV45': 'AV45',
                'ADNI2_AV45__AC_': 'AV45',
                'ADNI_BRAIN_3D__AV45': 'AV45',
                'ADNI_Brain_PET__Raw_AV45': 'AV45',
                'ADNIGO_-_AV45_BRAIN_STUDY': 'AV45',
                'ADNI_GO_PRIMARY__AV45': 'AV45',
                'ASL_PERFUSION': 'ASL_PERFUSION',
                'AV45_Dyn_4x5min_2Di_336_2z_AllPass__AC_': 'AV45',
                'Average_DC': 'Average_DC',
                'Axial_DTI': 'Axial_DTI',
                'Dyn_ADNI-GO_128x,4i20s,256mmFOV,NoFilter___AV45': 'AV45',
                'Enhanced_Axial_DTI': 'Enhanced_Axial_DTI',
                'Extended_Resting_State_fMRI': 'ext-rsfmri',
                'Fractional_Aniso.': 'Fractional_Aniso',
                'Isotropic_image': 'Isotropic_image',
                'MoCoSeries': 'MoCoSeries',
                'MPR__GradWarp': 'MPR_GradWarp',
                'MPR__GradWarp__B1_Correction': 'MPR_GradWarp_B1_Correction',
                'MPR__GradWarp__B1_Correction__Mask': 'MPR_GradWarp_B1_Correction_Mask',
                'MPR-R__GradWarp': 'MPR-R__GradWarp',
                'MPR-R__GradWarp__B1_Correction': 'MPR-R_GradWarp_B1_Correction',
                'MPR-R__GradWarp__B1_Correction__Mask': 'MPR-R_GradWarp_B1_Correction_Mask',
                'MT1__GradWarp__N3m': 'MT1__GradWarp__N3m',
                'MT1__N3m': 'MT1__N3m',
                'Perfusion_Weighted': 'Perfusion_Weighted',
                'PET_AC_3D_BRAIN__AV45': 'AV45',
                'PET_Brain_AV_45__AV45': 'AV45',
                'PET_Brain_COR_ADNI_#2__AC__AV45': 'AV45',
                'relCBF': 'relCBF',
                'Spatially_Normalized,_Masked_and_N3_corrected_T1_image': '3T-T1-Spa_Norm_Mask_N3_Corr'}

databaseRoot = '/data/data03/sulantha/blablabla/lololol'
