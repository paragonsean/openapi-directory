

# GoogleAppsCardV1CardHeader

Represents a card header. For an example in Google Chat apps, see [Card header](https://developers.google.com/chat/ui/widgets/card-header). [Google Workspace Add-ons and Chat apps](https://developers.google.com/workspace/extend):

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**imageAltText** | **String** | The alternative text of this image that&#39;s used for accessibility. |  [optional] |
|**imageType** | [**ImageTypeEnum**](#ImageTypeEnum) | The shape used to crop the image. [Google Workspace Add-ons and Chat apps](https://developers.google.com/workspace/extend): |  [optional] |
|**imageUrl** | **String** | The HTTPS URL of the image in the card header. |  [optional] |
|**subtitle** | **String** | The subtitle of the card header. If specified, appears on its own line below the &#x60;title&#x60;. |  [optional] |
|**title** | **String** | Required. The title of the card header. The header has a fixed height: if both a title and subtitle are specified, each takes up one line. If only the title is specified, it takes up both lines. |  [optional] |



## Enum: ImageTypeEnum

| Name | Value |
|---- | -----|
| SQUARE | &quot;SQUARE&quot; |
| CIRCLE | &quot;CIRCLE&quot; |



