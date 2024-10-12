

# GoogleCloudRecommendationengineV1beta1PredictResponse

Response message for predict method.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dryRun** | **Boolean** | True if the dryRun property was set in the request. |  [optional] |
|**itemsMissingInCatalog** | **List&lt;String&gt;** | IDs of items in the request that were missing from the catalog. |  [optional] |
|**metadata** | **Map&lt;String, Object&gt;** | Additional domain specific prediction response metadata. |  [optional] |
|**nextPageToken** | **String** | If empty, the list is complete. If nonempty, the token to pass to the next request&#39;s PredictRequest.page_token. |  [optional] |
|**recommendationToken** | **String** | A unique recommendation token. This should be included in the user event logs resulting from this recommendation, which enables accurate attribution of recommendation model performance. |  [optional] |
|**results** | [**List&lt;GoogleCloudRecommendationengineV1beta1PredictResponsePredictionResult&gt;**](GoogleCloudRecommendationengineV1beta1PredictResponsePredictionResult.md) | A list of recommended items. The order represents the ranking (from the most relevant item to the least). |  [optional] |



