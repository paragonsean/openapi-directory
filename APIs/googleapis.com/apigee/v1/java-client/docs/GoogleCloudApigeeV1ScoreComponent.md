

# GoogleCloudApigeeV1ScoreComponent

Component is an individual security element that is scored.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**calculateTime** | **String** | Time when score was calculated. |  [optional] |
|**dataCaptureTime** | **String** | Time in the requested time period when data was last captured to compute the score. |  [optional] |
|**drilldownPaths** | **List&lt;String&gt;** | List of paths for next components. |  [optional] |
|**recommendations** | [**List&lt;GoogleCloudApigeeV1ScoreComponentRecommendation&gt;**](GoogleCloudApigeeV1ScoreComponentRecommendation.md) | List of recommendations to improve API security. |  [optional] |
|**score** | **Integer** | Score for the component. |  [optional] |
|**scorePath** | **String** | Path of the component. Example: /org@myorg/envgroup@myenvgroup/proxies/proxy@myproxy |  [optional] |



