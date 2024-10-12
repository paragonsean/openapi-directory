# DiscoveryEngineApi.GoogleCloudDiscoveryengineV1alphaCompleteQueryResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**querySuggestions** | [**[GoogleCloudDiscoveryengineV1alphaCompleteQueryResponseQuerySuggestion]**](GoogleCloudDiscoveryengineV1alphaCompleteQueryResponseQuerySuggestion.md) | Results of the matched query suggestions. The result list is ordered and the first result is a top suggestion. | [optional] 
**tailMatchTriggered** | **Boolean** | True if the returned suggestions are all tail suggestions. For tail matching to be triggered, include_tail_suggestions in the request must be true and there must be no suggestions that match the full query. | [optional] 


