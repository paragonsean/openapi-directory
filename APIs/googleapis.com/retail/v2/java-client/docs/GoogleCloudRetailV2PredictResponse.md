

# GoogleCloudRetailV2PredictResponse

Response message for predict method.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**attributionToken** | **String** | A unique attribution token. This should be included in the UserEvent logs resulting from this recommendation, which enables accurate attribution of recommendation model performance. |  [optional] |
|**missingIds** | **List&lt;String&gt;** | IDs of products in the request that were missing from the inventory. |  [optional] |
|**results** | [**List&lt;GoogleCloudRetailV2PredictResponsePredictionResult&gt;**](GoogleCloudRetailV2PredictResponsePredictionResult.md) | A list of recommended products. The order represents the ranking (from the most relevant product to the least). |  [optional] |
|**validateOnly** | **Boolean** | True if the validateOnly property was set in the request. |  [optional] |



