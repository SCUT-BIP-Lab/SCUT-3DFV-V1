# SCUT-3DFV-V1
SCUT-3DFV-V1: the first publicly available 3D Finger Vein Dataset

--__code__: the matlab code for 3D finger vein reconstruction.  
--__datasamples__: data samples provided to understand this dataset in detail.  
--__datasamples/raw_images__: each capture get three raw images by the 3 different views of the 3D finger vein capture system.  
--__datasamples/3D_finger_vein_model__: reconstructed 3D point cloud based vein models with texture.  
--__datasamples/texture__: unwarpped full view vein texture images.  
--__datasamples/depth__: unwarpped full view depth images.  

# Short information
The SCUT-3DFV-V1 dataset consists of raw images captured by the 3D finger vein acquisition system, point cloud-based 3D finger vein models with vein texture, unwrapped full-view finger vein images and unwrapped full-view depth images. 203 fingers are collected from volunteers of their index finger and middle finger of both right and left hands. Each finger was acquired 14 times and the 3D finger vein model was reconstructed from three raw images captured from 3 views of the 3D finger vein acquisition system. To simulate the arbitrary rotation in realistic scenarios, the volunteers are asked to rotate their fingers in various poses. The first 6 of the 14 acquisitions, the data are collected with each finger in a normal pose with small rotation no more than ±30 degrees; for the next 6 of the 14 acquisitions, the data are collected with larger rotation no more than ±80 degrees; for the remaining 2 ones, rotation on the other directions besides axial direction is included. Finally, There are 1218 3D finger vein models for easy rotation and 2842 3D finger vein models for hard rotation.


# Request
The SCUT-3DFV-V1 dataset is publicly available (free of charge) to the research community.  
Unfortunately, due to privacy reasons, we cannot provide the database for commercial use.  

We have made part of the dataset available for download in the repo in order to get a detailed view of this data. Those interested in obtaining the whole SCUT-3DFV-V1 Dataset should download [release agreement](https://github.com/williamdyoung/SCUT-3DFV-V1/blob/main/SCUT-3DFV-V1%20Database%20Release%20Agreement.pdf), and send by e-mail one signed and scanned copy to scutbip@outlook.com.

While reporting results using the __SCUT-3DFV-V1 Dataset__, please cite the following article:  
@article{Kang2020StudyOA,  
  title={Study of a Full-View 3D Finger Vein Verification Technique},  
  author={Wenxiong Kang and H. Liu and Wei Luo and F. Deng},  
  journal={IEEE Transactions on Information Forensics and Security},  
  year={2020},  
  volume={15},  
  pages={1175-1189}  
}  

# Contact

Prof. Kang Wenxiong   
Biometrics and Intelligence Perception Lab.   
College of Automation Science and Engineering   
South China University of Technology   
Wushan RD.,Tianhe District,Guangzhou,P.R.China,510641      
auwxkang@scut.edu.cn   
