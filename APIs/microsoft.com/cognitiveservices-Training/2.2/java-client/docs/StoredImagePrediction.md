

# StoredImagePrediction

result of an image classification request.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**created** | **OffsetDateTime** |  |  [optional] [readonly] |
|**domain** | **UUID** | Domain used for the prediction. |  [optional] [readonly] |
|**id** | **UUID** |  |  [optional] [readonly] |
|**iteration** | **UUID** |  |  [optional] [readonly] |
|**originalImageUri** | **String** | The URI to the original prediction image. |  [optional] [readonly] |
|**predictions** | [**List&lt;Prediction&gt;**](Prediction.md) |  |  [optional] [readonly] |
|**project** | **UUID** |  |  [optional] [readonly] |
|**resizedImageUri** | **String** | The URI to the (resized) prediction image. |  [optional] [readonly] |
|**thumbnailUri** | **String** | The URI to the thumbnail of the original prediction image. |  [optional] [readonly] |



