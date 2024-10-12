# DialogflowApi.GoogleCloudDialogflowV2beta1ListSuggestionsResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nextPageToken** | **String** | Optional. Token to retrieve the next page of results or empty if there are no more results in the list. | [optional] 
**suggestions** | [**[GoogleCloudDialogflowV2beta1Suggestion]**](GoogleCloudDialogflowV2beta1Suggestion.md) | Required. The list of suggestions. There will be a maximum number of items returned based on the page_size field in the request. &#x60;suggestions&#x60; is sorted by &#x60;create_time&#x60; in descending order. | [optional] 


