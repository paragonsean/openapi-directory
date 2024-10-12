

# GoogleAppsCardV1Icon

An icon displayed in a widget on a card. For an example in Google Chat apps, see [Icon](https://developers.google.com/chat/ui/widgets/icon). Supports [built-in](https://developers.google.com/chat/format-messages#builtinicons) and [custom](https://developers.google.com/chat/format-messages#customicons) icons. [Google Workspace Add-ons and Chat apps](https://developers.google.com/workspace/extend):

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**altText** | **String** | Optional. A description of the icon used for accessibility. If unspecified, the default value &#x60;Button&#x60; is provided. As a best practice, you should set a helpful description for what the icon displays, and if applicable, what it does. For example, &#x60;A user&#39;s account portrait&#x60;, or &#x60;Opens a new browser tab and navigates to the Google Chat developer documentation at https://developers.google.com/chat&#x60;. If the icon is set in a &#x60;Button&#x60;, the &#x60;altText&#x60; appears as helper text when the user hovers over the button. However, if the button also sets &#x60;text&#x60;, the icon&#39;s &#x60;altText&#x60; is ignored. |  [optional] |
|**iconUrl** | **String** | Display a custom icon hosted at an HTTPS URL. For example: &#x60;&#x60;&#x60; \&quot;iconUrl\&quot;: \&quot;https://developers.google.com/chat/images/quickstart-app-avatar.png\&quot; &#x60;&#x60;&#x60; Supported file types include &#x60;.png&#x60; and &#x60;.jpg&#x60;. |  [optional] |
|**imageType** | [**ImageTypeEnum**](#ImageTypeEnum) | The crop style applied to the image. In some cases, applying a &#x60;CIRCLE&#x60; crop causes the image to be drawn larger than a built-in icon. |  [optional] |
|**knownIcon** | **String** | Display one of the built-in icons provided by Google Workspace. For example, to display an airplane icon, specify &#x60;AIRPLANE&#x60;. For a bus, specify &#x60;BUS&#x60;. For a full list of supported icons, see [built-in icons](https://developers.google.com/chat/format-messages#builtinicons). |  [optional] |



## Enum: ImageTypeEnum

| Name | Value |
|---- | -----|
| SQUARE | &quot;SQUARE&quot; |
| CIRCLE | &quot;CIRCLE&quot; |



