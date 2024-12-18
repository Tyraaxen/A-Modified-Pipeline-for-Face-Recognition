import torch
from AdaFace.inference import load_pretrained_model, to_input

#Change to correct directory
import os
os.chdir('C:/Users/tyra_/Comp_Science_project/A-Modified-Pipeline-for-Face-Recognition/AdaFace')

def convert_ckpt_to_onnx(architecture='ir_50', output_onnx_path='model.onnx'):
    # Load the pre-trained model
    model = load_pretrained_model(architecture=architecture)

    # Use a dummy input or preprocess a real image
    dummy_input = torch.randn(1, 3, 112, 112)  # Example dummy input
    # Uncomment below to use a real image
    # from PIL import Image
    # pil_image = Image.open('path_to_image.jpg').convert('RGB')
    # dummy_input = to_input(pil_image)

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
    print(f"Model has been converted to ONNX format and saved at '{output_onnx_path}'")

# Right now Adaface seems to only support 'ir_50' which adaface_ir50_ms1mv2.ckpt and this is hardcoded in the inference file in the Adaface repo
if __name__ == "__main__":
    convert_ckpt_to_onnx(architecture='ir_50', output_onnx_path='adaface_model.onnx')



#import onnx

#model = onnx.load("C:/Users/tyra_/.insightface/models/adaface_custom/adaface_model.onnx")
#print("Model Outputs:")
#for output in model.graph.output:
#    print(output.name, output.type)
    
# Remove the second output (shape (1, 1))
#model.graph.output.remove(model.graph.output[1])

# Save the modified model
#onnx.save(model, "C:/Users/tyra_/.insightface/models/adaface_custom/adaface_model_modified.onnx")