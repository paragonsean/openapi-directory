

# GoogleCloudRecommendationengineV1beta1PredictResponsePredictionResult

PredictionResult represents the recommendation prediction results.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | ID of the recommended catalog item |  [optional] |
|**itemMetadata** | **Map&lt;String, Object&gt;** | Additional item metadata / annotations. Possible values: * &#x60;catalogItem&#x60;: JSON representation of the catalogItem. Will be set if &#x60;returnCatalogItem&#x60; is set to true in &#x60;PredictRequest.params&#x60;. * &#x60;score&#x60;: Prediction score in double value. Will be set if &#x60;returnItemScore&#x60; is set to true in &#x60;PredictRequest.params&#x60;. |  [optional] |



