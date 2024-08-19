

# FileUploadQuestion

A file upload question. The API currently does not support creating file upload questions.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**folderId** | **String** | Required. The ID of the Drive folder where uploaded files are stored. |  [optional] |
|**maxFileSize** | **String** | Maximum number of bytes allowed for any single file uploaded to this question. |  [optional] |
|**maxFiles** | **Integer** | Maximum number of files that can be uploaded for this question in a single response. |  [optional] |
|**types** | [**List&lt;TypesEnum&gt;**](#List&lt;TypesEnum&gt;) | File types accepted by this question. |  [optional] |



## Enum: List&lt;TypesEnum&gt;

| Name | Value |
|---- | -----|
| FILE_TYPE_UNSPECIFIED | &quot;FILE_TYPE_UNSPECIFIED&quot; |
| ANY | &quot;ANY&quot; |
| DOCUMENT | &quot;DOCUMENT&quot; |
| PRESENTATION | &quot;PRESENTATION&quot; |
| SPREADSHEET | &quot;SPREADSHEET&quot; |
| DRAWING | &quot;DRAWING&quot; |
| PDF | &quot;PDF&quot; |
| IMAGE | &quot;IMAGE&quot; |
| VIDEO | &quot;VIDEO&quot; |
| AUDIO | &quot;AUDIO&quot; |



