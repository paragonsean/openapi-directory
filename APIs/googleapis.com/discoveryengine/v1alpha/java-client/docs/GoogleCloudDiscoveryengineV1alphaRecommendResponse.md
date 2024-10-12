

# GoogleCloudDiscoveryengineV1alphaRecommendResponse

Response message for Recommend method.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**attributionToken** | **String** | A unique attribution token. This should be included in the UserEvent logs resulting from this recommendation, which enables accurate attribution of recommendation model performance. |  [optional] |
|**missingIds** | **List&lt;String&gt;** | IDs of documents in the request that were missing from the default Branch associated with the requested ServingConfig. |  [optional] |
|**results** | [**List&lt;GoogleCloudDiscoveryengineV1alphaRecommendResponseRecommendationResult&gt;**](GoogleCloudDiscoveryengineV1alphaRecommendResponseRecommendationResult.md) | A list of recommended Documents. The order represents the ranking (from the most relevant Document to the least). |  [optional] |
|**validateOnly** | **Boolean** | True if RecommendRequest.validate_only was set. |  [optional] |



