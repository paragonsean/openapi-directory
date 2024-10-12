# GoogleChatApi.ActionResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dialogAction** | [**DialogAction**](DialogAction.md) |  | [optional] 
**type** | **String** | Input only. The type of Chat app response. | [optional] 
**updatedWidget** | [**UpdatedWidget**](UpdatedWidget.md) |  | [optional] 
**url** | **String** | Input only. URL for users to authenticate or configure. (Only for &#x60;REQUEST_CONFIG&#x60; response types.) | [optional] 



## Enum: TypeEnum


* `TYPE_UNSPECIFIED` (value: `"TYPE_UNSPECIFIED"`)

* `NEW_MESSAGE` (value: `"NEW_MESSAGE"`)

* `UPDATE_MESSAGE` (value: `"UPDATE_MESSAGE"`)

* `UPDATE_USER_MESSAGE_CARDS` (value: `"UPDATE_USER_MESSAGE_CARDS"`)

* `REQUEST_CONFIG` (value: `"REQUEST_CONFIG"`)

* `DIALOG` (value: `"DIALOG"`)

* `UPDATE_WIDGET` (value: `"UPDATE_WIDGET"`)




