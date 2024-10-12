

# GoogleAppsCardV1SelectionInput

A widget that creates one or more UI items that users can select. For example, a dropdown menu or checkboxes. You can use this widget to collect data that can be predicted or enumerated. For an example in Google Chat apps, see [Selection input](https://developers.google.com/chat/ui/widgets/selection-input). Chat apps can process the value of items that users select or input. For details about working with form inputs, see [Receive form data](https://developers.google.com/chat/ui/read-form-data). To collect undefined or abstract data from users, use the TextInput widget. [Google Workspace Add-ons and Chat apps](https://developers.google.com/workspace/extend):

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**externalDataSource** | [**GoogleAppsCardV1Action**](GoogleAppsCardV1Action.md) |  |  [optional] |
|**items** | [**List&lt;GoogleAppsCardV1SelectionItem&gt;**](GoogleAppsCardV1SelectionItem.md) | An array of selectable items. For example, an array of radio buttons or checkboxes. Supports up to 100 items. |  [optional] |
|**label** | **String** | The text that appears above the selection input field in the user interface. Specify text that helps the user enter the information your app needs. For example, if users are selecting the urgency of a work ticket from a drop-down menu, the label might be \&quot;Urgency\&quot; or \&quot;Select urgency\&quot;. |  [optional] |
|**multiSelectMaxSelectedItems** | **Integer** | For multiselect menus, the maximum number of items that a user can select. Minimum value is 1 item. If unspecified, defaults to 3 items. |  [optional] |
|**multiSelectMinQueryLength** | **Integer** | For multiselect menus, the number of text characters that a user inputs before the Chat app queries autocomplete and displays suggested items in the menu. If unspecified, defaults to 0 characters for static data sources and 3 characters for external data sources. |  [optional] |
|**name** | **String** | The name that identifies the selection input in a form input event. For details about working with form inputs, see [Receive form data](https://developers.google.com/chat/ui/read-form-data). |  [optional] |
|**onChangeAction** | [**GoogleAppsCardV1Action**](GoogleAppsCardV1Action.md) |  |  [optional] |
|**platformDataSource** | [**GoogleAppsCardV1PlatformDataSource**](GoogleAppsCardV1PlatformDataSource.md) |  |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | The type of items that are displayed to users in a &#x60;SelectionInput&#x60; widget. Selection types support different types of interactions. For example, users can select one or more checkboxes, but they can only select one value from a dropdown menu. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| CHECK_BOX | &quot;CHECK_BOX&quot; |
| RADIO_BUTTON | &quot;RADIO_BUTTON&quot; |
| SWITCH | &quot;SWITCH&quot; |
| DROPDOWN | &quot;DROPDOWN&quot; |
| MULTI_SELECT | &quot;MULTI_SELECT&quot; |



