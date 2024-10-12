

# ModelFile

The file ids of the uploaded file

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**contentType** | **String** | The internet media type of the file |  [optional] |
|**fileId** | **String** | The id of the uploaded file |  |
|**fileUrl** | **String** | The path where the file can be located. |  [optional] |
|**hash** | [**Hash**](Hash.md) |  |  [optional] |
|**mimeCheck** | [**MimeCheckEnum**](#MimeCheckEnum) | The mime type validation check to see if the extension of this file matches it&#39;s content. Can be PASSED or FAILED |  [optional] |
|**name** | **String** | The name of the uploaded file |  |
|**size** | **Integer** | The number of bytes in the uploaded file |  |
|**uploadDate** | **Long** | The time in milliseconds when the file was uploaded |  |
|**virusScan** | [**VirusScan**](VirusScan.md) |  |  [optional] |



## Enum: MimeCheckEnum

| Name | Value |
|---- | -----|
| PASSED | &quot;PASSED&quot; |
| FAILED | &quot;FAILED&quot; |



