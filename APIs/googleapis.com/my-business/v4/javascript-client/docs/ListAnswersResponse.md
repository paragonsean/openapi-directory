# GoogleMyBusinessApi.ListAnswersResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**answers** | [**[Answer]**](Answer.md) | The requested answers. | [optional] 
**nextPageToken** | **String** | If the number of answers exceeds the requested max page size, this field is populated with a token to fetch the next page of answers on a subsequent call. If there are no more answers, this field is not present in the response. | [optional] 
**totalSize** | **Number** | The total number of answers posted for this question across all pages. | [optional] 


