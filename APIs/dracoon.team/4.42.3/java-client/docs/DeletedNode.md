

# DeletedNode

Deleted node information (Deleted node can be a folder or file)

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accessedAt** | **OffsetDateTime** | Last access date |  [optional] |
|**classification** | [**ClassificationEnum**](#ClassificationEnum) | Classification ID:  * &#x60;1&#x60; - public  * &#x60;2&#x60; - internal  * &#x60;3&#x60; - confidential  * &#x60;4&#x60; - strictly confidential    (default: classification from parent room) |  [optional] |
|**createdAt** | **OffsetDateTime** | Creation date |  [optional] |
|**createdBy** | [**UserInfo**](UserInfo.md) |  |  [optional] |
|**deletedAt** | **OffsetDateTime** | Deletion date |  [optional] |
|**deletedBy** | [**UserInfo**](UserInfo.md) |  |  [optional] |
|**expireAt** | **OffsetDateTime** | Expiration date |  [optional] |
|**id** | **Long** | Node ID |  [optional] |
|**isEncrypted** | **Boolean** | Encryption state |  [optional] |
|**name** | **String** | Node name |  |
|**notes** | **String** | User notes |  [optional] |
|**parentId** | **Long** | Parent node ID (room or folder) |  |
|**parentPath** | **String** | Parent node path  &#x60;/&#x60; if node is a root node (room) |  |
|**referenceId** | **Long** | &amp;#128640; Since v4.37.0  Reference ID. Identical across all versions of a file |  [optional] |
|**size** | **Long** | Node size in byte |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Node type |  |
|**updatedAt** | **OffsetDateTime** | Modification date |  [optional] |
|**updatedBy** | [**UserInfo**](UserInfo.md) |  |  [optional] |



## Enum: ClassificationEnum

| Name | Value |
|---- | -----|
| NUMBER_1 | 1 |
| NUMBER_2 | 2 |
| NUMBER_3 | 3 |
| NUMBER_4 | 4 |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| FOLDER | &quot;folder&quot; |
| FILE | &quot;file&quot; |



