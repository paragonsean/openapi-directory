# GoogleChatApi.GoogleAppsCardV1SelectionItem

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bottomText** | **String** | For multiselect menus, a text description or label that&#39;s displayed below the item&#39;s &#x60;text&#x60; field. | [optional] 
**selected** | **Boolean** | Whether the item is selected by default. If the selection input only accepts one value (such as for radio buttons or a dropdown menu), only set this field for one item. | [optional] 
**startIconUri** | **String** | For multiselect menus, the URL for the icon displayed next to the item&#39;s &#x60;text&#x60; field. Supports PNG and JPEG files. Must be an &#x60;HTTPS&#x60; URL. For example, &#x60;https://developers.google.com/chat/images/quickstart-app-avatar.png&#x60;. | [optional] 
**text** | **String** | The text that identifies or describes the item to users. | [optional] 
**value** | **String** | The value associated with this item. The client should use this as a form input value. For details about working with form inputs, see [Receive form data](https://developers.google.com/chat/ui/read-form-data). | [optional] 


