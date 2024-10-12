

# DeprecatedEvent

A Google Chat app interaction event. To learn about interaction events, see [Receive and respond to interactions with your Google Chat app](https://developers.google.com/chat/api/guides/message-formats). To learn about event types and for example event payloads, see [Types of Google Chat app interaction events](https://developers.google.com/chat/api/guides/message-formats/events).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**action** | [**FormAction**](FormAction.md) |  |  [optional] |
|**common** | [**CommonEventObject**](CommonEventObject.md) |  |  [optional] |
|**configCompleteRedirectUrl** | **String** | The URL the Chat app should redirect the user to after they have completed an authorization or configuration flow outside of Google Chat. For more information, see [Connect a Chat app with other services &amp; tools](https://developers.google.com/chat/how-tos/connect-web-services-tools). |  [optional] |
|**dialogEventType** | [**DialogEventTypeEnum**](#DialogEventTypeEnum) | The type of [dialog](https://developers.google.com/chat/how-tos/dialogs) interaction event received. |  [optional] |
|**eventTime** | **String** | The timestamp indicating when the interaction event occurred. |  [optional] |
|**isDialogEvent** | **Boolean** | For &#x60;CARD_CLICKED&#x60; interaction events, whether the user interacted with a [dialog](https://developers.google.com/chat/how-tos/dialogs). |  [optional] |
|**message** | [**Message**](Message.md) |  |  [optional] |
|**space** | [**Space**](Space.md) |  |  [optional] |
|**threadKey** | **String** | The Chat app-defined key for the thread related to the interaction event. See [&#x60;spaces.messages.thread.threadKey&#x60;](/chat/api/reference/rest/v1/spaces.messages#Thread.FIELDS.thread_key) for more information. |  [optional] |
|**token** | **String** | A secret value that legacy Chat apps can use to verify if a request is from Google. Google randomly generates the token, and its value remains static. You can obtain, revoke, or regenerate the token from the [Chat API configuration page](https://console.cloud.google.com/apis/api/chat.googleapis.com/hangouts-chat) in the Google Cloud Console. Modern Chat apps don&#39;t use this field. It is absent from API responses and the [Chat API configuration page](https://console.cloud.google.com/apis/api/chat.googleapis.com/hangouts-chat). |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | The type of interaction event. For details, see [Types of Google Chat app interaction events](https://developers.google.com/chat/api/guides/message-formats/events). |  [optional] |
|**user** | [**User**](User.md) |  |  [optional] |



## Enum: DialogEventTypeEnum

| Name | Value |
|---- | -----|
| TYPE_UNSPECIFIED | &quot;TYPE_UNSPECIFIED&quot; |
| REQUEST_DIALOG | &quot;REQUEST_DIALOG&quot; |
| SUBMIT_DIALOG | &quot;SUBMIT_DIALOG&quot; |
| CANCEL_DIALOG | &quot;CANCEL_DIALOG&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;UNSPECIFIED&quot; |
| MESSAGE | &quot;MESSAGE&quot; |
| ADDED_TO_SPACE | &quot;ADDED_TO_SPACE&quot; |
| REMOVED_FROM_SPACE | &quot;REMOVED_FROM_SPACE&quot; |
| CARD_CLICKED | &quot;CARD_CLICKED&quot; |
| WIDGET_UPDATED | &quot;WIDGET_UPDATED&quot; |



