# VertexAiApi.GoogleCloudAiplatformV1ModelExportFormat

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exportableContents** | **[String]** | Output only. The content of this Model that may be exported. | [optional] [readonly] 
**id** | **String** | Output only. The ID of the export format. The possible format IDs are: * &#x60;tflite&#x60; Used for Android mobile devices. * &#x60;edgetpu-tflite&#x60; Used for [Edge TPU](https://cloud.google.com/edge-tpu/) devices. * &#x60;tf-saved-model&#x60; A tensorflow model in SavedModel format. * &#x60;tf-js&#x60; A [TensorFlow.js](https://www.tensorflow.org/js) model that can be used in the browser and in Node.js using JavaScript. * &#x60;core-ml&#x60; Used for iOS mobile devices. * &#x60;custom-trained&#x60; A Model that was uploaded or trained by custom code. | [optional] [readonly] 



## Enum: [ExportableContentsEnum]


* `EXPORTABLE_CONTENT_UNSPECIFIED` (value: `"EXPORTABLE_CONTENT_UNSPECIFIED"`)

* `ARTIFACT` (value: `"ARTIFACT"`)

* `IMAGE` (value: `"IMAGE"`)




