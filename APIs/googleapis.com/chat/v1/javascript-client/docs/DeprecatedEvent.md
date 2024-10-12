# GoogleChatApi.DeprecatedEvent

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | [**FormAction**](FormAction.md) |  | [optional] 
**common** | [**CommonEventObject**](CommonEventObject.md) |  | [optional] 
**configCompleteRedirectUrl** | **String** | The URL the Chat app should redirect the user to after they have completed an authorization or configuration flow outside of Google Chat. For more information, see [Connect a Chat app with other services &amp; tools](https://developers.google.com/chat/how-tos/connect-web-services-tools). | [optional] 
**dialogEventType** | **String** | The type of [dialog](https://developers.google.com/chat/how-tos/dialogs) interaction event received. | [optional] 
**eventTime** | **String** | The timestamp indicating when the interaction event occurred. | [optional] 
**isDialogEvent** | **Boolean** | For &#x60;CARD_CLICKED&#x60; interaction events, whether the user interacted with a [dialog](https://developers.google.com/chat/how-tos/dialogs). | [optional] 
**message** | [**Message**](Message.md) |  | [optional] 
**space** | [**Space**](Space.md) |  | [optional] 
**threadKey** | **String** | The Chat app-defined key for the thread related to the interaction event. See [&#x60;spaces.messages.thread.threadKey&#x60;](/chat/api/reference/rest/v1/spaces.messages#Thread.FIELDS.thread_key) for more information. | [optional] 
**token** | **String** | A secret value that legacy Chat apps can use to verify if a request is from Google. Google randomly generates the token, and its value remains static. You can obtain, revoke, or regenerate the token from the [Chat API configuration page](https://console.cloud.google.com/apis/api/chat.googleapis.com/hangouts-chat) in the Google Cloud Console. Modern Chat apps don&#39;t use this field. It is absent from API responses and the [Chat API configuration page](https://console.cloud.google.com/apis/api/chat.googleapis.com/hangouts-chat). | [optional] 
**type** | **String** | The type of interaction event. For details, see [Types of Google Chat app interaction events](https://developers.google.com/chat/api/guides/message-formats/events). | [optional] 
**user** | [**User**](User.md) |  | [optional] 



## Enum: DialogEventTypeEnum


* `TYPE_UNSPECIFIED` (value: `"TYPE_UNSPECIFIED"`)

* `REQUEST_DIALOG` (value: `"REQUEST_DIALOG"`)

* `SUBMIT_DIALOG` (value: `"SUBMIT_DIALOG"`)

* `CANCEL_DIALOG` (value: `"CANCEL_DIALOG"`)





## Enum: TypeEnum


* `UNSPECIFIED` (value: `"UNSPECIFIED"`)

* `MESSAGE` (value: `"MESSAGE"`)

* `ADDED_TO_SPACE` (value: `"ADDED_TO_SPACE"`)

* `REMOVED_FROM_SPACE` (value: `"REMOVED_FROM_SPACE"`)

* `CARD_CLICKED` (value: `"CARD_CLICKED"`)

* `WIDGET_UPDATED` (value: `"WIDGET_UPDATED"`)




