

# GoogleAppsCardV1Button

A text, icon, or text and icon button that users can click. For an example in Google Chat apps, see [Button list](https://developers.google.com/chat/ui/widgets/button-list). To make an image a clickable button, specify an `Image` (not an `ImageComponent`) and set an `onClick` action. [Google Workspace Add-ons and Chat apps](https://developers.google.com/workspace/extend):

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**altText** | **String** | The alternative text that&#39;s used for accessibility. Set descriptive text that lets users know what the button does. For example, if a button opens a hyperlink, you might write: \&quot;Opens a new browser tab and navigates to the Google Chat developer documentation at https://developers.google.com/chat\&quot;. |  [optional] |
|**color** | [**Color**](Color.md) |  |  [optional] |
|**disabled** | **Boolean** | If &#x60;true&#x60;, the button is displayed in an inactive state and doesn&#39;t respond to user actions. |  [optional] |
|**icon** | [**GoogleAppsCardV1Icon**](GoogleAppsCardV1Icon.md) |  |  [optional] |
|**onClick** | [**GoogleAppsCardV1OnClick**](GoogleAppsCardV1OnClick.md) |  |  [optional] |
|**text** | **String** | The text displayed inside the button. |  [optional] |



