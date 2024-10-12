# GoogleChatApi.GoogleAppsCardV1SelectionInput

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**externalDataSource** | [**GoogleAppsCardV1Action**](GoogleAppsCardV1Action.md) |  | [optional] 
**items** | [**[GoogleAppsCardV1SelectionItem]**](GoogleAppsCardV1SelectionItem.md) | An array of selectable items. For example, an array of radio buttons or checkboxes. Supports up to 100 items. | [optional] 
**label** | **String** | The text that appears above the selection input field in the user interface. Specify text that helps the user enter the information your app needs. For example, if users are selecting the urgency of a work ticket from a drop-down menu, the label might be \&quot;Urgency\&quot; or \&quot;Select urgency\&quot;. | [optional] 
**multiSelectMaxSelectedItems** | **Number** | For multiselect menus, the maximum number of items that a user can select. Minimum value is 1 item. If unspecified, defaults to 3 items. | [optional] 
**multiSelectMinQueryLength** | **Number** | For multiselect menus, the number of text characters that a user inputs before the Chat app queries autocomplete and displays suggested items in the menu. If unspecified, defaults to 0 characters for static data sources and 3 characters for external data sources. | [optional] 
**name** | **String** | The name that identifies the selection input in a form input event. For details about working with form inputs, see [Receive form data](https://developers.google.com/chat/ui/read-form-data). | [optional] 
**onChangeAction** | [**GoogleAppsCardV1Action**](GoogleAppsCardV1Action.md) |  | [optional] 
**platformDataSource** | [**GoogleAppsCardV1PlatformDataSource**](GoogleAppsCardV1PlatformDataSource.md) |  | [optional] 
**type** | **String** | The type of items that are displayed to users in a &#x60;SelectionInput&#x60; widget. Selection types support different types of interactions. For example, users can select one or more checkboxes, but they can only select one value from a dropdown menu. | [optional] 



## Enum: TypeEnum


* `CHECK_BOX` (value: `"CHECK_BOX"`)

* `RADIO_BUTTON` (value: `"RADIO_BUTTON"`)

* `SWITCH` (value: `"SWITCH"`)

* `DROPDOWN` (value: `"DROPDOWN"`)

* `MULTI_SELECT` (value: `"MULTI_SELECT"`)




