

# GoogleCloudAiplatformV1ModelExportFormat

Represents export format supported by the Model. All formats export to Google Cloud Storage.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**exportableContents** | [**List&lt;ExportableContentsEnum&gt;**](#List&lt;ExportableContentsEnum&gt;) | Output only. The content of this Model that may be exported. |  [optional] [readonly] |
|**id** | **String** | Output only. The ID of the export format. The possible format IDs are: * &#x60;tflite&#x60; Used for Android mobile devices. * &#x60;edgetpu-tflite&#x60; Used for [Edge TPU](https://cloud.google.com/edge-tpu/) devices. * &#x60;tf-saved-model&#x60; A tensorflow model in SavedModel format. * &#x60;tf-js&#x60; A [TensorFlow.js](https://www.tensorflow.org/js) model that can be used in the browser and in Node.js using JavaScript. * &#x60;core-ml&#x60; Used for iOS mobile devices. * &#x60;custom-trained&#x60; A Model that was uploaded or trained by custom code. |  [optional] [readonly] |



## Enum: List&lt;ExportableContentsEnum&gt;

| Name | Value |
|---- | -----|
| EXPORTABLE_CONTENT_UNSPECIFIED | &quot;EXPORTABLE_CONTENT_UNSPECIFIED&quot; |
| ARTIFACT | &quot;ARTIFACT&quot; |
| IMAGE | &quot;IMAGE&quot; |



