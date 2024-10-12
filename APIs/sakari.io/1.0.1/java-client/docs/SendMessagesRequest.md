

# SendMessagesRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**contacts** | [**List&lt;ContactRequest&gt;**](ContactRequest.md) |  |  [optional] |
|**conversationStrategy** | **String** |  |  [optional] |
|**conversations** | **List&lt;String&gt;** | List of conversation ids to send messages to |  [optional] |
|**filters** | [**SendMessagesRequestFilters**](SendMessagesRequestFilters.md) |  |  [optional] |
|**media** | [**List&lt;SendMessagesRequestMediaInner&gt;**](SendMessagesRequestMediaInner.md) | List of media objects to attach to message |  [optional] |
|**phoneNumberFilter** | [**SendMessagesRequestPhoneNumberFilter**](SendMessagesRequestPhoneNumberFilter.md) |  |  [optional] |
|**template** | **String** |  |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) |  |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| SMS | &quot;SMS&quot; |
| MMS | &quot;MMS&quot; |



