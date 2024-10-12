

# CreateFileUploadRequest

Request model for creating an upload channel

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**classification** | [**ClassificationEnum**](#ClassificationEnum) | Classification ID:  * &#x60;1&#x60; - public  * &#x60;2&#x60; - internal  * &#x60;3&#x60; - confidential  * &#x60;4&#x60; - strictly confidential    (default: classification from parent room) |  [optional] |
|**directS3Upload** | **Boolean** | &amp;#128640; Since v4.15.0  Upload direct to S3 |  [optional] |
|**expiration** | [**ObjectExpiration**](ObjectExpiration.md) |  |  [optional] |
|**name** | **String** | File name |  |
|**notes** | **String** | User notes  Use empty string to remove. |  [optional] |
|**parentId** | **Long** | Parent node ID (room or folder) |  |
|**size** | **Long** | File size in byte |  [optional] |
|**timestampCreation** | **OffsetDateTime** | &amp;#128640; Since v4.22.0  Time the node was created on external file system  (default: current server datetime in UTC format) |  [optional] |
|**timestampModification** | **OffsetDateTime** | &amp;#128640; Since v4.22.0  Time the content of a node was last modified on external file system  (default: current server datetime in UTC format) |  [optional] |



## Enum: ClassificationEnum

| Name | Value |
|---- | -----|
| NUMBER_1 | 1 |
| NUMBER_2 | 2 |
| NUMBER_3 | 3 |
| NUMBER_4 | 4 |



