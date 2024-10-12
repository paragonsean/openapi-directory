# OsConfigApi.SoftwareRecipeStepExtractArchive

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**artifactId** | **String** | Required. The id of the relevant artifact in the recipe. | [optional] 
**destination** | **String** | Directory to extract archive to. Defaults to &#x60;/&#x60; on Linux or &#x60;C:\\&#x60; on Windows. | [optional] 
**type** | **String** | Required. The type of the archive to extract. | [optional] 



## Enum: TypeEnum


* `ARCHIVE_TYPE_UNSPECIFIED` (value: `"ARCHIVE_TYPE_UNSPECIFIED"`)

* `TAR` (value: `"TAR"`)

* `TAR_GZIP` (value: `"TAR_GZIP"`)

* `TAR_BZIP` (value: `"TAR_BZIP"`)

* `TAR_LZMA` (value: `"TAR_LZMA"`)

* `TAR_XZ` (value: `"TAR_XZ"`)

* `ZIP` (value: `"ZIP"`)




