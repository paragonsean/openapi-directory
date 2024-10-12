

# GoogleAppsCardV1SwitchControl

Either a toggle-style switch or a checkbox inside a `decoratedText` widget. [Google Workspace Add-ons and Chat apps](https://developers.google.com/workspace/extend): Only supported in the `decoratedText` widget.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**controlType** | [**ControlTypeEnum**](#ControlTypeEnum) | How the switch appears in the user interface. [Google Workspace Add-ons and Chat apps](https://developers.google.com/workspace/extend): |  [optional] |
|**name** | **String** | The name by which the switch widget is identified in a form input event. For details about working with form inputs, see [Receive form data](https://developers.google.com/chat/ui/read-form-data). |  [optional] |
|**onChangeAction** | [**GoogleAppsCardV1Action**](GoogleAppsCardV1Action.md) |  |  [optional] |
|**selected** | **Boolean** | When &#x60;true&#x60;, the switch is selected. |  [optional] |
|**value** | **String** | The value entered by a user, returned as part of a form input event. For details about working with form inputs, see [Receive form data](https://developers.google.com/chat/ui/read-form-data). |  [optional] |



## Enum: ControlTypeEnum

| Name | Value |
|---- | -----|
| SWITCH | &quot;SWITCH&quot; |
| CHECKBOX | &quot;CHECKBOX&quot; |
| CHECK_BOX | &quot;CHECK_BOX&quot; |



