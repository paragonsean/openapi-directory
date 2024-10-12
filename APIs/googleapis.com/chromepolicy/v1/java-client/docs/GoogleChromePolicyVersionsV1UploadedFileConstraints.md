

# GoogleChromePolicyVersionsV1UploadedFileConstraints

Constraints on the uploaded file of a file policy.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**sizeLimitBytes** | **String** | The size limit of uploaded files for a setting, in bytes. |  [optional] |
|**supportedContentTypes** | [**List&lt;SupportedContentTypesEnum&gt;**](#List&lt;SupportedContentTypesEnum&gt;) | File types that can be uploaded for a setting. |  [optional] |



## Enum: List&lt;SupportedContentTypesEnum&gt;

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;CONTENT_TYPE_UNSPECIFIED&quot; |
| PLAIN_TEXT | &quot;CONTENT_TYPE_PLAIN_TEXT&quot; |
| HTML | &quot;CONTENT_TYPE_HTML&quot; |
| IMAGE_JPEG | &quot;CONTENT_TYPE_IMAGE_JPEG&quot; |
| IMAGE_GIF | &quot;CONTENT_TYPE_IMAGE_GIF&quot; |
| IMAGE_PNG | &quot;CONTENT_TYPE_IMAGE_PNG&quot; |
| JSON | &quot;CONTENT_TYPE_JSON&quot; |
| ZIP | &quot;CONTENT_TYPE_ZIP&quot; |
| GZIP | &quot;CONTENT_TYPE_GZIP&quot; |
| CSV | &quot;CONTENT_TYPE_CSV&quot; |
| YAML | &quot;CONTENT_TYPE_YAML&quot; |
| IMAGE_WEBP | &quot;CONTENT_TYPE_IMAGE_WEBP&quot; |



