

# Question

Represents a single question and some of its answers.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**author** | [**Author**](Author.md) |  |  [optional] |
|**createTime** | **String** | Output only. The timestamp for when the question was written. |  [optional] [readonly] |
|**name** | **String** | Immutable. The unique name for the question. locations/_*_/questions/_* This field will be ignored if set during question creation. |  [optional] |
|**text** | **String** | Required. The text of the question. It should contain at least three words and the total length should be greater than or equal to 10 characters. The maximum length is 4096 characters. |  [optional] |
|**topAnswers** | [**List&lt;Answer&gt;**](Answer.md) | Output only. A list of answers to the question, sorted by upvotes. This may not be a complete list of answers depending on the request parameters (answers_per_question) |  [optional] [readonly] |
|**totalAnswerCount** | **Integer** | Output only. The total number of answers posted for this question. |  [optional] [readonly] |
|**updateTime** | **String** | Output only. The timestamp for when the question was last modified. |  [optional] [readonly] |
|**upvoteCount** | **Integer** | Output only. The number of upvotes for the question. |  [optional] [readonly] |



