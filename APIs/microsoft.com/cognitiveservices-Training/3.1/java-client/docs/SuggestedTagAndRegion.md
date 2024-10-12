

# SuggestedTagAndRegion

Result of a suggested tags and regions request.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**created** | **OffsetDateTime** | Date this prediction was created. |  [optional] [readonly] |
|**id** | **UUID** | Prediction Id. |  [optional] [readonly] |
|**iteration** | **UUID** | Iteration Id. |  [optional] [readonly] |
|**predictionUncertainty** | **Double** | Uncertainty (entropy) of suggested tags or regions per image. |  [optional] [readonly] |
|**predictions** | [**List&lt;Prediction&gt;**](Prediction.md) | List of predictions. |  [optional] [readonly] |
|**project** | **UUID** | Project Id. |  [optional] [readonly] |



