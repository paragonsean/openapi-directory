# BitbucketApi.CommitFile

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | **String** |  | [optional] 
**commit** | [**Commit**](Commit.md) |  | [optional] 
**escapedPath** | **String** | The escaped version of the path as it appears in a diff. If the path does not require escaping this will be the same as path. | [optional] 
**path** | **String** | The path in the repository | [optional] 
**type** | **String** |  | 



## Enum: AttributesEnum


* `link` (value: `"link"`)

* `executable` (value: `"executable"`)

* `subrepository` (value: `"subrepository"`)

* `binary` (value: `"binary"`)

* `lfs` (value: `"lfs"`)




