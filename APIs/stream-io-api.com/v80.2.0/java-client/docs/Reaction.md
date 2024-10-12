

# Reaction

Represents user reaction to a message

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createdAt** | **OffsetDateTime** | Date/time of creation |  [readonly] |
|**messageId** | **String** | ID of a message user reacted to |  |
|**score** | **Integer** | Reaction score. If not specified reaction has score of 1 |  |
|**type** | **String** | The type of reaction (e.g. &#39;like&#39;, &#39;laugh&#39;, &#39;wow&#39;) |  |
|**updatedAt** | **OffsetDateTime** | Date/time of the last update |  [readonly] |
|**user** | **UserObject** |  |  [optional] |
|**userId** | **String** | ID of a user who reacted to a message |  [optional] |



