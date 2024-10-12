# VertexAiSearchForRetailApi.GoogleCloudRetailV2alphaCompleteQueryResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributeResults** | [**{String: GoogleCloudRetailV2alphaCompleteQueryResponseAttributeResult}**](GoogleCloudRetailV2alphaCompleteQueryResponseAttributeResult.md) | A map of matched attribute suggestions. This field is only available for \&quot;cloud-retail\&quot; dataset. Current supported keys: * &#x60;brands&#x60; * &#x60;categories&#x60; | [optional] 
**attributionToken** | **String** | A unique complete token. This should be included in the UserEvent.completion_detail for search events resulting from this completion, which enables accurate attribution of complete model performance. | [optional] 
**completionResults** | [**[GoogleCloudRetailV2alphaCompleteQueryResponseCompletionResult]**](GoogleCloudRetailV2alphaCompleteQueryResponseCompletionResult.md) | Results of the matching suggestions. The result list is ordered and the first result is top suggestion. | [optional] 
**recentSearchResults** | [**[GoogleCloudRetailV2alphaCompleteQueryResponseRecentSearchResult]**](GoogleCloudRetailV2alphaCompleteQueryResponseRecentSearchResult.md) | Deprecated. Matched recent searches of this user. The maximum number of recent searches is 10. This field is a restricted feature. If you want to enable it, contact Retail Search support. This feature is only available when CompleteQueryRequest.visitor_id field is set and UserEvent is imported. The recent searches satisfy the follow rules: * They are ordered from latest to oldest. * They are matched with CompleteQueryRequest.query case insensitively. * They are transformed to lower case. * They are UTF-8 safe. Recent searches are deduplicated. More recent searches will be reserved when duplication happens. | [optional] 


