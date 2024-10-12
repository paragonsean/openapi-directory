

# GoogleAppsCardV1TextInput

A field in which users can enter text. Supports suggestions and on-change actions. For an example in Google Chat apps, see [Text input](https://developers.google.com/chat/ui/widgets/text-input). Chat apps receive and can process the value of entered text during form input events. For details about working with form inputs, see [Receive form data](https://developers.google.com/chat/ui/read-form-data). When you need to collect undefined or abstract data from users, use a text input. To collect defined or enumerated data from users, use the SelectionInput widget. [Google Workspace Add-ons and Chat apps](https://developers.google.com/workspace/extend):

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**autoCompleteAction** | [**GoogleAppsCardV1Action**](GoogleAppsCardV1Action.md) |  |  [optional] |
|**hintText** | **String** | Text that appears below the text input field meant to assist users by prompting them to enter a certain value. This text is always visible. Required if &#x60;label&#x60; is unspecified. Otherwise, optional. |  [optional] |
|**initialSuggestions** | [**GoogleAppsCardV1Suggestions**](GoogleAppsCardV1Suggestions.md) |  |  [optional] |
|**label** | **String** | The text that appears above the text input field in the user interface. Specify text that helps the user enter the information your app needs. For example, if you are asking someone&#39;s name, but specifically need their surname, write &#x60;surname&#x60; instead of &#x60;name&#x60;. Required if &#x60;hintText&#x60; is unspecified. Otherwise, optional. |  [optional] |
|**name** | **String** | The name by which the text input is identified in a form input event. For details about working with form inputs, see [Receive form data](https://developers.google.com/chat/ui/read-form-data). |  [optional] |
|**onChangeAction** | [**GoogleAppsCardV1Action**](GoogleAppsCardV1Action.md) |  |  [optional] |
|**placeholderText** | **String** | Text that appears in the text input field when the field is empty. Use this text to prompt users to enter a value. For example, &#x60;Enter a number from 0 to 100&#x60;. [Google Chat apps](https://developers.google.com/chat): |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | How a text input field appears in the user interface. For example, whether the field is single or multi-line. |  [optional] |
|**value** | **String** | The value entered by a user, returned as part of a form input event. For details about working with form inputs, see [Receive form data](https://developers.google.com/chat/ui/read-form-data). |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| SINGLE_LINE | &quot;SINGLE_LINE&quot; |
| MULTIPLE_LINE | &quot;MULTIPLE_LINE&quot; |



