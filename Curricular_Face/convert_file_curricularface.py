import torch
import os
import onnx
# Directory where CurricularFace model and architecture are located
os.chdir('C:/Users/hanna/Skola/Projektkurs/A-Modified-Pipeline-for-Face-Recognition')

# A-Modified-Pipeline-for-Face-Recognition/CurricularFace/backbone/CurricularFace_Backbone.pth
# Import the Backbone architecture from the provided model_irse.py
from CurricularFace.backbone.model_irse import IR_101

def load_curricularface_model(ckpt_path):
    """
    Loads the CurricularFace model from a checkpoint using the Backbone.

    Args:
        ckpt_path (str): Path to the CurricularFace model checkpoint.

    Returns:
        torch.nn.Module: Loaded CurricularFace model in evaluation mode.
    """
    # Initialize the model with IR_101 architecture
    model = IR_101(input_size=[112, 112])  # Adjust parameters if needed
    checkpoint = torch.load(ckpt_path, map_location='cpu',  weights_only=True)
    model.load_state_dict(checkpoint, strict=False)
    model.eval()
    return model

def convert_ckpt_to_onnx(ckpt_path='Curricular/Moels/CurricularFace_Backbone.pth', output_onnx_path='Curricular/curricularface_model.onnx'):
    """
    Converts the CurricularFace model checkpoint to ONNX format.

    Args:
        ckpt_path (str): Path to the CurricularFace model checkpoint.
        output_onnx_path (str): Path to save the ONNX model.
    """
    # Load the CurricularFace model
    model = load_curricularface_model(ckpt_path)

    # Use a dummy input for ONNX export
    dummy_input = torch.randn(1, 3, 112, 112)  # Example dummy input
    output = model(dummy_input)
    print(output)
    if isinstance(output, tuple):
        output = output[0]  # Select the primary output
    # Export the model to ONNX
    torch.onnx.export(
        model,
        dummy_input,
        output_onnx_path,
        export_params=True,
        opset_version=11,
        input_names=['input'],
        output_names=['output'],
        dynamic_axes={'input': {0: 'batch_size'}, 'output': {0: 'batch_size'}}
    )
    onnx_model = onnx.load('curricularface_model.onnx')
    onnx.checker.check_model(onnx_model)
    print("ONNX model is valid!")
    print(f"CurricularFace model has been converted to ONNX format and saved at '{output_onnx_path}'")

if __name__ == "__main__":
    # Specify the checkpoint and output paths

    convert_ckpt_to_onnx(
        ckpt_path='Curricular/Models/CurricularFace_Backbone.pth', #local paths
        output_onnx_path='Curricular/Models/curricularface_model.onnx'#local paths
    )
