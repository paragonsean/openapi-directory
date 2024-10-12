

# InlineQuery

This object represents an incoming inline query. When the user sends an empty query, your bot could return some default or trending results.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**from** | [**User**](User.md) |  |  |
|**id** | **String** | Unique identifier for this query |  |
|**location** | [**Location**](Location.md) |  |  [optional] |
|**offset** | **String** | Offset of the results to be returned, can be controlled by the bot |  |
|**query** | **String** | Text of the query (up to 256 characters) |  |



