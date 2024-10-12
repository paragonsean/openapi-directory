

# AmenityMedia

Media is a digital content like image, video with associated text and description, several scales and some metadata can be provided also.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**description** | [**QualifiedFreeText**](QualifiedFreeText.md) |  |  [optional] |
|**href** | **URI** | href to display the original media.  |  [optional] |
|**mediaType** | [**MediaTypeEnum**](#MediaTypeEnum) | media type as per IANA (https://www.iana.org/assignments/media-types/media-types.xhtml) |  [optional] |
|**title** | **String** | media title |  [optional] |



## Enum: MediaTypeEnum

| Name | Value |
|---- | -----|
| APPLICATION | &quot;application&quot; |
| AUDIO | &quot;audio&quot; |
| FONT | &quot;font&quot; |
| EXAMPLE | &quot;example&quot; |
| IMAGE | &quot;image&quot; |
| MESSAGE | &quot;message&quot; |
| MODEL | &quot;model&quot; |
| MULTIPART | &quot;multipart&quot; |
| TEXT | &quot;text&quot; |
| VIDEO | &quot;video&quot; |



