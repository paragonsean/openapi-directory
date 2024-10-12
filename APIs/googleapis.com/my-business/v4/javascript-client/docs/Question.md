# GoogleMyBusinessApi.Question

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**author** | [**Author**](Author.md) |  | [optional] 
**createTime** | **String** | Output only. The timestamp for when the question was written. | [optional] 
**name** | **String** | Output only. The unique name for the question. accounts/_*_/locations/_*_/questions/_* | [optional] 
**text** | **String** | The text of the question. It should contain at least three words and the total length should be greater than or equal to 10 characters. The maximum length is 4096 characters. | [optional] 
**topAnswers** | [**[Answer]**](Answer.md) | Output only. A list of answers to the question, sorted by upvotes. This may not be a complete list of answers depending on the request parameters (answers_per_question) | [optional] 
**totalAnswerCount** | **Number** | Output only. The total number of answers posted for this question. | [optional] 
**updateTime** | **String** | Output only. The timestamp for when the question was last modified. | [optional] 
**upvoteCount** | **Number** | Output only. The number of upvotes for the question. | [optional] 


