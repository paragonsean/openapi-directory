# VertexAiApi.GoogleCloudAiplatformV1beta1SchemaPredictParamsVideoObjectTrackingPredictionParams

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**confidenceThreshold** | **Number** | The Model only returns predictions with at least this confidence score. Default value is 0.0 | [optional] 
**maxPredictions** | **Number** | The model only returns up to that many top, by confidence score, predictions per frame of the video. If this number is very high, the Model may return fewer predictions per frame. Default value is 50. | [optional] 
**minBoundingBoxSize** | **Number** | Only bounding boxes with shortest edge at least that long as a relative value of video frame size are returned. Default value is 0.0. | [optional] 


