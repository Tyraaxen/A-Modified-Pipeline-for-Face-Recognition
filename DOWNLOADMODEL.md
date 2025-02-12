steps:
1. Download a feature extractor model of your choice, we downloaded AdaFace ir_101 and Adaface ir_50 from the Adaface github repo.
2. If the file is not in ONNX format, use convert_file.py to convert it to ONNX format. The AdaFace models we used were in ckpt format so the code might not work if you have another format originally. In the function you have to specify which architecture the deep learning model has and the output path in which the model will be saved. 
3. Now you should have a model in ONNX format. The only thing left to do is to (possibly) remove one of the outputs of the model. This is because the AdaFace models have two outputs: the feature vector and a confidence score, but Insightface only accepts models that have one output: the feature vector. VART ÄR KODEN
4. Now you should have a ONNX file in the right format. You can now create a new model directory by navigating to  ~/.insightface/models/ on your computer, probably located in the home directry the installation was done under. There you will find the buffalo_l model. What you do then is that you create a new folder with a name of your choice- the name used for the directory in this code for the AdaFace ir_101 is adaface_101.

![Contents of models after adding custom model](Images\Instruction-images\contents_of_models.PNG)

Then copy the contents from the buffalo_l directory, **except** the feature extractor model into your new folder. The feature extractor model, <em>w600k_r50</em>, you substitute with your own model.

![The files to copy over](Images\Instruction-images\buffalo_l_folder_screenshot.PNG)

 This way you can use InsightFace as usual but with a new model for the feature extractor step.

5. Then you can call the model as you do the buffalo_l model, using app = FaceAnalysis(name='your_model_zoo') to load these models. The Adaface model is called by using app = FaceAnalysis(name='adaface_101'), i.e. the name of the folder you created in step 4.
