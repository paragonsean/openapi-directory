

# Answer

Represents an answer to a question

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**author** | [**Author**](Author.md) |  |  [optional] |
|**createTime** | **String** | Output only. The timestamp for when the answer was written. Only retrieved during ListResponse fetching. |  [optional] [readonly] |
|**name** | **String** | Output only. The unique name for the answer locations/_*_/questions/_*_/answers/_* |  [optional] [readonly] |
|**text** | **String** | Required. The text of the answer. It should contain at least one non-whitespace character. The maximum length is 4096 characters. |  [optional] |
|**updateTime** | **String** | Output only. The timestamp for when the answer was last modified. |  [optional] [readonly] |
|**upvoteCount** | **Integer** | Output only. The number of upvotes for the answer. |  [optional] [readonly] |



