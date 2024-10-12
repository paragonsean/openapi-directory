# VertexAiApi.GoogleCloudAiplatformV1SchemaPredictParamsVideoClassificationPredictionParams

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**confidenceThreshold** | **Number** | The Model only returns predictions with at least this confidence score. Default value is 0.0 | [optional] 
**maxPredictions** | **Number** | The Model only returns up to that many top, by confidence score, predictions per instance. If this number is very high, the Model may return fewer predictions. Default value is 10,000. | [optional] 
**oneSecIntervalClassification** | **Boolean** | Set to true to request classification for a video at one-second intervals. Vertex AI returns labels and their confidence scores for each second of the entire time segment of the video that user specified in the input WARNING: Model evaluation is not done for this classification type, the quality of it depends on the training data, but there are no metrics provided to describe that quality. Default value is false | [optional] 
**segmentClassification** | **Boolean** | Set to true to request segment-level classification. Vertex AI returns labels and their confidence scores for the entire time segment of the video that user specified in the input instance. Default value is true | [optional] 
**shotClassification** | **Boolean** | Set to true to request shot-level classification. Vertex AI determines the boundaries for each camera shot in the entire time segment of the video that user specified in the input instance. Vertex AI then returns labels and their confidence scores for each detected shot, along with the start and end time of the shot. WARNING: Model evaluation is not done for this classification type, the quality of it depends on the training data, but there are no metrics provided to describe that quality. Default value is false | [optional] 


