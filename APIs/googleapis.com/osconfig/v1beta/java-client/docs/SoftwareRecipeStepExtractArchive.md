

# SoftwareRecipeStepExtractArchive

Extracts an archive of the type specified in the specified directory.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**artifactId** | **String** | Required. The id of the relevant artifact in the recipe. |  [optional] |
|**destination** | **String** | Directory to extract archive to. Defaults to &#x60;/&#x60; on Linux or &#x60;C:\\&#x60; on Windows. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Required. The type of the archive to extract. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| ARCHIVE_TYPE_UNSPECIFIED | &quot;ARCHIVE_TYPE_UNSPECIFIED&quot; |
| TAR | &quot;TAR&quot; |
| TAR_GZIP | &quot;TAR_GZIP&quot; |
| TAR_BZIP | &quot;TAR_BZIP&quot; |
| TAR_LZMA | &quot;TAR_LZMA&quot; |
| TAR_XZ | &quot;TAR_XZ&quot; |
| ZIP | &quot;ZIP&quot; |



