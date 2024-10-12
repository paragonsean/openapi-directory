

# UpdateFolderRequest

Request model for updating folder's metadata

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**classification** | [**ClassificationEnum**](#ClassificationEnum) | &amp;#128640; Since v4.30.0  Classification ID:  * &#x60;1&#x60; - public  * &#x60;2&#x60; - internal  * &#x60;3&#x60; - confidential  * &#x60;4&#x60; - strictly confidential    Provided (or default) classification is taken from room  when file gets uploaded without any classification. |  [optional] |
|**name** | **String** | Folder name |  [optional] |
|**notes** | **String** | User notes  Use empty string to remove. |  [optional] |
|**timestampCreation** | **OffsetDateTime** | &amp;#128640; Since v4.22.0  Time the node was created on external file system  (default: current server datetime in UTC format) |  [optional] |
|**timestampModification** | **OffsetDateTime** | &amp;#128640; Since v4.22.0  Time the content of a node was last modified on external file system  (default: current server datetime in UTC format) |  [optional] |



## Enum: ClassificationEnum

| Name | Value |
|---- | -----|
| NUMBER_1 | 1 |
| NUMBER_2 | 2 |
| NUMBER_3 | 3 |
| NUMBER_4 | 4 |



