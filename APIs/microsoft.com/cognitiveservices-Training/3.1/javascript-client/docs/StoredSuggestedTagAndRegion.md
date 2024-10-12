# CustomVisionTrainingClient.StoredSuggestedTagAndRegion

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **Date** | Date this prediction was created. | [optional] [readonly] 
**domain** | **String** | Domain used for the prediction. | [optional] [readonly] 
**height** | **Number** | Height of the resized image. | [optional] [readonly] 
**id** | **String** | Prediction Id. | [optional] [readonly] 
**iteration** | **String** | Iteration Id. | [optional] [readonly] 
**originalImageUri** | **String** | The URI to the original prediction image. | [optional] [readonly] 
**predictionUncertainty** | **Number** | Uncertainty (entropy) of suggested tags or regions per image. | [optional] [readonly] 
**predictions** | [**[Prediction]**](Prediction.md) | List of predictions. | [optional] [readonly] 
**project** | **String** | Project Id. | [optional] [readonly] 
**resizedImageUri** | **String** | The URI to the (resized) prediction image. | [optional] [readonly] 
**thumbnailUri** | **String** | The URI to the thumbnail of the original prediction image. | [optional] [readonly] 
**width** | **Number** | Width of the resized image. | [optional] [readonly] 


