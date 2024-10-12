# VertexAiApi.GoogleCloudAiplatformV1SchemaPredictInstanceTextExtractionPredictionInstance

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | **String** | The text snippet to make the predictions on. | [optional] 
**key** | **String** | This field is only used for batch prediction. If a key is provided, the batch prediction result will by mapped to this key. If omitted, then the batch prediction result will contain the entire input instance. Vertex AI will not check if keys in the request are duplicates, so it is up to the caller to ensure the keys are unique. | [optional] 
**mimeType** | **String** | The MIME type of the text snippet. The supported MIME types are listed below. - text/plain | [optional] 


