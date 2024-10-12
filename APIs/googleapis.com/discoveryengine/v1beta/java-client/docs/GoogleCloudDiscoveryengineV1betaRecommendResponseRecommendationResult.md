

# GoogleCloudDiscoveryengineV1betaRecommendResponseRecommendationResult

RecommendationResult represents a generic recommendation result with associated metadata.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**document** | [**GoogleCloudDiscoveryengineV1betaDocument**](GoogleCloudDiscoveryengineV1betaDocument.md) |  |  [optional] |
|**id** | **String** | Resource ID of the recommended Document. |  [optional] |
|**metadata** | **Map&lt;String, Object&gt;** | Additional Document metadata / annotations. Possible values: * &#x60;score&#x60;: Recommendation score in double value. Is set if &#x60;returnScore&#x60; is set to true in RecommendRequest.params. |  [optional] |



