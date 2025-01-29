# A-Modified-Pipeline-for-Face-Recognition
Project in Computational Science

## ONNX Runtime Python Package (TA)

When using ONNX Runtime in InsightFace, there are two installation options:

```bash
pip install onnxruntime
```
and

```bash
pip install onnxruntime-gpu
```

To enable GPU support for InsightFace, you must install the onnxruntime-gpu package. Additionally, a compatible version of CUDA and cuDNN must be installed on your system to ensure proper GPU functionality.
## Integration of Adaface in Insightface

InsightFace is installed as a Python library using:

pip install insightface

During installation, the default packages, including the ArcFace implementation, are installed. The default model provided in InsightFace is buffalo_l, which includes the following components:

    Face detection in the default setup is performed using RetinaFace.
    Face alignment utilizes both 2D and 3D key points.

The primary objective of this study is to integrate Adaface into the InsightFace framework. The faceanalysis class in InsightFace is used to extract feature vectors. To support Adaface, the input parameters of this class are modified to accept an Adaface model.

The faceanalysis class takes the following inputs:

    name: The name of the model.
    root: The directory where the model is located.
    allowed_modules: Defaults to None.

The Adaface model is moved to a directory located inside .insightface. To integrate Adaface, the name parameter is updated to the name of the directory where the ONNX-formatted Adaface model exists. This directory will also contain the other three models used for detection, alignment, and verification, which are not relevant to this project and therefore copied from the default buffalo_l directory. This allows the InsightFace pipeline to utilize the Adaface model for facial recognition tasks.

## Conversion of Adaface Model to ONNX

The default Adaface model, IR50 trained on the MS1MV2 dataset, is provided in the repository and is downloaded in ckpt format via the repository's README.

The inference.py script in the Adaface repository is originally hardcoded to only support the default IR50 MS1MV2 model. To enable compatibility with other models, such as IR101 trained on the WebFace12M, the script is modified. The function load_pretrained_model in inference.py is used to load model weights from the ckpt file for both the default and newly added models. The ONNX-formatted Adaface model is then integrated into the InsightFace recognition pipeline using a new directory placed in the .insightface directory, as mentioned above.

## Parallelization
Since InsightFace uses ONNX Runtime as its inference backend, paralleliza-tion and GPU support were enabled by installing onnxruntime-gpu insteadof onnxruntime, along with downloading compatible versions of CUDA andcuDNN.To utilize GPU acceleration, a computer with a GPU is required. Forthis project, we used a system equipped with a NVIDIA GeForce GTX 1650Ti grafic card. Regardless of whether the GPU processes images in a loopor as a batch, it efficiently leverages parallelization in both cases.When preparing the model, the buffalo l model pack was used as fol-lows:arcface_model = insightface.model_zoo.get_model(’buffalo_l’)

arcface_model.prepare(ctx_id=-1,providers=[’CUDAExecutionProvider’])ctx_id=-1 for CPU, 0 for GPUHere, ctx id is set to -1 for CPU support and 0 for GPU support.The provider is set to ’CPUExecutionProvider’ when using the CPU and’CUDAExecutionProvider’, when the GPU is used.4

