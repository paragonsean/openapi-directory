

# FileNote

FileNote represents an SPDX File Information section: https://spdx.github.io/spdx-spec/4-file-information/

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**checksum** | **List&lt;String&gt;** | Provide a unique identifier to match analysis information on each specific file in a package |  [optional] |
|**fileType** | [**FileTypeEnum**](#FileTypeEnum) | This field provides information about the type of file identified |  [optional] |
|**title** | **String** | Identify the full path and filename that corresponds to the file information in this section |  [optional] |



## Enum: FileTypeEnum

| Name | Value |
|---- | -----|
| FILE_TYPE_UNSPECIFIED | &quot;FILE_TYPE_UNSPECIFIED&quot; |
| SOURCE | &quot;SOURCE&quot; |
| BINARY | &quot;BINARY&quot; |
| ARCHIVE | &quot;ARCHIVE&quot; |
| APPLICATION | &quot;APPLICATION&quot; |
| AUDIO | &quot;AUDIO&quot; |
| IMAGE | &quot;IMAGE&quot; |
| TEXT | &quot;TEXT&quot; |
| VIDEO | &quot;VIDEO&quot; |
| DOCUMENTATION | &quot;DOCUMENTATION&quot; |
| SPDX | &quot;SPDX&quot; |
| OTHER | &quot;OTHER&quot; |



