# ContainerAnalysisApi.FileNote

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**checksum** | **[String]** | Provide a unique identifier to match analysis information on each specific file in a package | [optional] 
**fileType** | **String** | This field provides information about the type of file identified | [optional] 
**title** | **String** | Identify the full path and filename that corresponds to the file information in this section | [optional] 



## Enum: FileTypeEnum


* `FILE_TYPE_UNSPECIFIED` (value: `"FILE_TYPE_UNSPECIFIED"`)

* `SOURCE` (value: `"SOURCE"`)

* `BINARY` (value: `"BINARY"`)

* `ARCHIVE` (value: `"ARCHIVE"`)

* `APPLICATION` (value: `"APPLICATION"`)

* `AUDIO` (value: `"AUDIO"`)

* `IMAGE` (value: `"IMAGE"`)

* `TEXT` (value: `"TEXT"`)

* `VIDEO` (value: `"VIDEO"`)

* `DOCUMENTATION` (value: `"DOCUMENTATION"`)

* `SPDX` (value: `"SPDX"`)

* `OTHER` (value: `"OTHER"`)




