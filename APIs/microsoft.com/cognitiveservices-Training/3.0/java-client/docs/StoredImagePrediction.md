

# StoredImagePrediction

result of an image classification request.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**created** | **OffsetDateTime** | Date this prediction was created. |  [optional] [readonly] |
|**domain** | **UUID** | Domain used for the prediction. |  [optional] [readonly] |
|**id** | **UUID** | Prediction Id. |  [optional] [readonly] |
|**iteration** | **UUID** | Iteration Id. |  [optional] [readonly] |
|**originalImageUri** | **String** | The URI to the original prediction image. |  [optional] [readonly] |
|**predictions** | [**List&lt;Prediction&gt;**](Prediction.md) | List of predictions. |  [optional] [readonly] |
|**project** | **UUID** | Project Id. |  [optional] [readonly] |
|**resizedImageUri** | **String** | The URI to the (resized) prediction image. |  [optional] [readonly] |
|**thumbnailUri** | **String** | The URI to the thumbnail of the original prediction image. |  [optional] [readonly] |



