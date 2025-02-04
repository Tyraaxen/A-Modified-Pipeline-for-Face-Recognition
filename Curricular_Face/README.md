# CurricularFace Model Conversion for InsightFace

This repository provides a guide to convert the **CurricularFace** model to a format that can be used with the **InsightFace** framework. Follow the steps below to download the pre-trained **IR101** model, convert it to ONNX format, and use it with **InsightFace**.

## Model Download

The pre-trained **CurricularFace** model can be downloaded from the [CurricularFace GitHub repository](https://github.com/HuangYG123/CurricularFace). 

1. Navigate to the "Model" section in the repository’s README.
2. Download the pre-trained **IR101** model.

## Conversion Process

Once the model is downloaded, it needs to be converted to ONNX format for use with the **InsightFace** framework. 

### Conversion Script

Use the `convert_file_curriculaface.py` script to convert the downloaded **CurricularFace.pth** file into the ONNX format. This script uses a skeleton for the IR101 model, allowing it to be passed into **CurricularFace** for conversion.

The following import is used to load the model:
```python
from CurricularFace.backbone.model_irse import IR_101

The converted model will be saved in the specified directory. The resulting model file will be saved as curricularface_model.onnx, it is NOT yet finished for implementation in Insightace, see under Models.


## Models
For implemetnation in Insightface, use the [text](Models/curricularface_model_modified.onnx).
It is the orignal converted curriclarface model adapted to only have one output.

## Integration
The integration into Insightface can be done following the same steps as [Integration of Adaface in Insightface in the orginal ReadME](A-Modified-Pipeline-for-Face-Recognition/README.md). Where the onnx model is the [text](Models/curricularface_model_modified.onnx) model, which is to be uploaded to the .insightface direcotry local on the computer. 

## References

- [CurricularFace GitHub repository](https://github.com/HuangYG123/CurricularFace)