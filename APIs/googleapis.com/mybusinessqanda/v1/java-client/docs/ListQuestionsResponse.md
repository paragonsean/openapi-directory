

# ListQuestionsResponse

Response message for QuestionsAndAnswers.ListQuestions

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**nextPageToken** | **String** | If the number of questions exceeds the requested max page size, this field is populated with a token to fetch the next page of questions on a subsequent call. If there are no more questions, this field is not present in the response. |  [optional] |
|**questions** | [**List&lt;Question&gt;**](Question.md) | The requested questions, |  [optional] |
|**totalSize** | **Integer** | The total number of questions posted for this location across all pages. |  [optional] |



