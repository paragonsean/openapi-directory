# ServiceManagementApi.ConfigFile

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fileContents** | **Blob** | The bytes that constitute the file. | [optional] 
**filePath** | **String** | The file name of the configuration file (full or relative path). | [optional] 
**fileType** | **String** | The type of configuration file this represents. | [optional] 



## Enum: FileTypeEnum


* `FILE_TYPE_UNSPECIFIED` (value: `"FILE_TYPE_UNSPECIFIED"`)

* `SERVICE_CONFIG_YAML` (value: `"SERVICE_CONFIG_YAML"`)

* `OPEN_API_JSON` (value: `"OPEN_API_JSON"`)

* `OPEN_API_YAML` (value: `"OPEN_API_YAML"`)

* `FILE_DESCRIPTOR_SET_PROTO` (value: `"FILE_DESCRIPTOR_SET_PROTO"`)

* `PROTO_FILE` (value: `"PROTO_FILE"`)




