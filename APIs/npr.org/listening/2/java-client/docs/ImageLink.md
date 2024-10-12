

# ImageLink

An image, along with metadata for display

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**href** | **URI** | The link to be followed |  |
|**caption** | **String** | The caption of the image; can be used as alternate text for accessibility |  [optional] |
|**contentType** | [**ContentTypeEnum**](#ContentTypeEnum) | The MIME type of the response of this link; note that the enumerated list of possible values is not exhaustive and other MIME types could occur. The list should be treated as examples, rather than absolutes. |  |
|**image** | **String** | A unique identifier for the image |  [optional] |
|**producer** | **String** | The producer of the image; should be used for properly attributing the image when it exists |  [optional] |
|**provider** | **String** | The provider of the image; should be used for properly attributing the image when it exists |  [optional] |
|**rel** | [**RelEnum**](#RelEnum) | The crop type or intended display style/size; note that the enumerated list of possible values is not exhaustive and other values could occur. The list should be treated as examples, rather than absolutes. |  [optional] |



## Enum: ContentTypeEnum

| Name | Value |
|---- | -----|
| JPEG | &quot;image/jpeg&quot; |
| PNG | &quot;image/png&quot; |
| GIF | &quot;image/gif&quot; |



## Enum: RelEnum

| Name | Value |
|---- | -----|
| LOGO_SQUARE | &quot;logo_square&quot; |
| ICON | &quot;icon&quot; |
| WIDE | &quot;wide&quot; |
| STANDARD | &quot;standard&quot; |
| SQUARE | &quot;square&quot; |
| ENLARGEMENT | &quot;enlargement&quot; |
| CUSTOM | &quot;custom&quot; |



