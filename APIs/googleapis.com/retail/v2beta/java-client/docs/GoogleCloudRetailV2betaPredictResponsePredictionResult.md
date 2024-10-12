

# GoogleCloudRetailV2betaPredictResponsePredictionResult

PredictionResult represents the recommendation prediction results.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | ID of the recommended product |  [optional] |
|**metadata** | **Map&lt;String, Object&gt;** | Additional product metadata / annotations. Possible values: * &#x60;product&#x60;: JSON representation of the product. Is set if &#x60;returnProduct&#x60; is set to true in &#x60;PredictRequest.params&#x60;. * &#x60;score&#x60;: Prediction score in double value. Is set if &#x60;returnScore&#x60; is set to true in &#x60;PredictRequest.params&#x60;. |  [optional] |



