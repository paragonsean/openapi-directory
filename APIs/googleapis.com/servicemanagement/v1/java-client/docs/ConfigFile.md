

# ConfigFile

Generic specification of a source configuration file

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**fileContents** | **byte[]** | The bytes that constitute the file. |  [optional] |
|**filePath** | **String** | The file name of the configuration file (full or relative path). |  [optional] |
|**fileType** | [**FileTypeEnum**](#FileTypeEnum) | The type of configuration file this represents. |  [optional] |



## Enum: FileTypeEnum

| Name | Value |
|---- | -----|
| FILE_TYPE_UNSPECIFIED | &quot;FILE_TYPE_UNSPECIFIED&quot; |
| SERVICE_CONFIG_YAML | &quot;SERVICE_CONFIG_YAML&quot; |
| OPEN_API_JSON | &quot;OPEN_API_JSON&quot; |
| OPEN_API_YAML | &quot;OPEN_API_YAML&quot; |
| FILE_DESCRIPTOR_SET_PROTO | &quot;FILE_DESCRIPTOR_SET_PROTO&quot; |
| PROTO_FILE | &quot;PROTO_FILE&quot; |



