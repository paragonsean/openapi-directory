

# TestCloudFileHash1

Hash, type, path and byte range of a file that is required in test run

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**checksum** | **String** | SHA256 hash of the file |  |
|**fileType** | [**FileTypeEnum**](#FileTypeEnum) | Type of the file |  |
|**relativePath** | **String** | Relative path of the file |  |



## Enum: FileTypeEnum

| Name | Value |
|---- | -----|
| DSYM_FILE | &quot;dsym-file&quot; |
| APP_FILE | &quot;app-file&quot; |
| TEST_FILE | &quot;test-file&quot; |



