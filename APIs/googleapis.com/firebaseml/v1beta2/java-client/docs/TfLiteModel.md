

# TfLiteModel

Information that is specific to TfLite models.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**automlModel** | **String** | The AutoML model id referencing a model you created with the AutoML API. The name should have format &#39;projects//locations//models/&#39; (This is the model resource name returned from the AutoML API) |  [optional] |
|**gcsTfliteUri** | **String** | The TfLite file containing the model. (Stored in Google Cloud). The gcs_tflite_uri should have form: gs://some-bucket/some-model.tflite Note: If you update the file in the original location, it is necessary to call UpdateModel for ML to pick up and validate the updated file. |  [optional] |
|**sizeBytes** | **String** | Output only. The size of the TFLite model |  [optional] [readonly] |



