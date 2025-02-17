# CurricularFace Model Conversion for InsightFace

This repository provides a guide to convert the **CurricularFace** model to a format that can be used with the **InsightFace** framework. Follow the steps below to download the pre-trained **IR101** model, convert it to ONNX format, and use it with **InsightFace**.
## 1. Clone into the CurriculaFace GitHub repo
[CurricularFace GitHub repository](https://github.com/HuangYG123/CurricularFace). 
## 2.  Model Download

The pre-trained **CurricularFace** model can be downloaded from the [CurricularFace GitHub repository](https://github.com/HuangYG123/CurricularFace). 

1. Navigate to the "Model" section in the repository’s README.
2. Download the pre-trained **IR101** model.

## 2. Conversion Process

Once the model is downloaded, it needs to be converted to ONNX format for use with the **InsightFace** framework. 

### Conversion Script

Use the `convert_file_curricularface.py` script to convert the downloaded **CurricularFace_Backbone.pth** file into the ONNX format. This script uses a skeleton for the IR101 model, allowing it to be passed into **CurricularFace** for conversion.

1. Move the downloaded **CurricularFace_Backbone.pth** into the directory Curricular_Face/Models
2. Run convert_file_curricularface.py, and make sure you fulfill the prerequisties in the top of the python script. 
3. The converted model will be saved in the specified directory. The resulting model file will be saved as curricularface_model_modified.onnx.


## 3. Models
The code supports IR_101 Curricualrface model, in ONNX format. 
## 4. Integration

The integration into Insightface can be done following the same steps as [Integration of Adaface in Insightface in the original README](A-Modified-Pipeline-for-Face-Recognition/DOWNLOADMODEL.md). Where the onnx model is the  <em>curricularface_model_modified.onnx </em> model, which is to be uploaded to the .insightface directory local on the computer. 

## References

- [CurricularFace GitHub repository](https://github.com/HuangYG123/CurricularFace)