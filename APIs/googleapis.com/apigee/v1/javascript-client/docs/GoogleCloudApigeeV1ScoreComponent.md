# ApigeeApi.GoogleCloudApigeeV1ScoreComponent

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**calculateTime** | **String** | Time when score was calculated. | [optional] 
**dataCaptureTime** | **String** | Time in the requested time period when data was last captured to compute the score. | [optional] 
**drilldownPaths** | **[String]** | List of paths for next components. | [optional] 
**recommendations** | [**[GoogleCloudApigeeV1ScoreComponentRecommendation]**](GoogleCloudApigeeV1ScoreComponentRecommendation.md) | List of recommendations to improve API security. | [optional] 
**score** | **Number** | Score for the component. | [optional] 
**scorePath** | **String** | Path of the component. Example: /org@myorg/envgroup@myenvgroup/proxies/proxy@myproxy | [optional] 


