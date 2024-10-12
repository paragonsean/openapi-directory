

# Node

Node information (Node can be a room, folder or file)

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**authParentId** | **Long** | &amp;#128640; Since v4.15.0  Auth parent room ID |  [optional] |
|**branchVersion** | **Long** | Version of last change in this node or a node further down the tree. |  [optional] |
|**children** | [**List&lt;Node&gt;**](Node.md) | &amp;#128679; Deprecated since v4.10.0  Child nodes list (if requested)  (for rooms / folders only) |  [optional] |
|**classification** | [**ClassificationEnum**](#ClassificationEnum) | Classification ID:  * &#x60;1&#x60; - public  * &#x60;2&#x60; - internal  * &#x60;3&#x60; - confidential  * &#x60;4&#x60; - strictly confidential |  [optional] |
|**cntChildren** | **Integer** | &amp;#128679; Deprecated since v4.11.0  Number of direct children  (no recursion; for rooms / folders only) |  [optional] |
|**cntComments** | **Integer** | Returns the number of comments of this node. |  [optional] |
|**cntDeletedVersions** | **Integer** | Number of deleted versions of this file / folder  (for rooms / folders only) |  [optional] |
|**cntDownloadShares** | **Integer** | Returns the number of Download Shares of this node. |  [optional] |
|**cntFiles** | **Integer** | &amp;#128640; Since v4.11.0  Amount of direct child files where this node is the parent node  (no recursion; for rooms / folders only) |  [optional] |
|**cntFolders** | **Integer** | &amp;#128640; Since v4.11.0  Amount of direct child folders where this node is the parent node  (no recursion; for rooms / folders only) |  [optional] |
|**cntRooms** | **Integer** | &amp;#128640; Since v4.11.0  Amount of direct child rooms where this node is the parent node  (no recursion; for rooms only) |  [optional] |
|**cntUploadShares** | **Integer** | Returns the number of Upload Shares of this node. |  [optional] |
|**createdAt** | **OffsetDateTime** | Creation date |  [optional] |
|**createdBy** | [**UserInfo**](UserInfo.md) |  |  [optional] |
|**encryptionInfo** | [**EncryptionInfo**](EncryptionInfo.md) |  |  [optional] |
|**expireAt** | **OffsetDateTime** | Expiration date |  [optional] |
|**fileType** | **String** | File type / extension (for files only) |  [optional] |
|**hasActivitiesLog** | **Boolean** | Is activities log active (for rooms only) |  [optional] |
|**hash** | **String** | MD5 hash of file |  [optional] |
|**id** | **Long** | Node ID |  |
|**inheritPermissions** | **Boolean** | Inherit permissions from parent room  (default: &#x60;false&#x60; if &#x60;parentId&#x60; is &#x60;0&#x60;; otherwise: &#x60;true&#x60;) |  [optional] |
|**isBrowsable** | **Boolean** | &amp;#128640; Since v4.11.0  Determines whether node is browsable by client (for rooms only) |  [optional] |
|**isEncrypted** | **Boolean** | Encryption state |  [optional] |
|**isFavorite** | **Boolean** | Node is marked as favorite (for rooms / folders only) |  [optional] |
|**mediaToken** | **String** | Media server media token |  [optional] |
|**mediaType** | **String** | File media type (for files only) |  [optional] |
|**name** | **String** | Name |  |
|**notes** | **String** | User notes |  [optional] |
|**parentId** | **Long** | Parent node ID (room or folder) |  [optional] |
|**parentPath** | **String** | Parent node path  &#x60;/&#x60; if node is a root node (room) |  [optional] |
|**permissions** | [**NodePermissions**](NodePermissions.md) |  |  [optional] |
|**quota** | **Long** | Quota in byte |  [optional] |
|**recycleBinRetentionPeriod** | **Integer** | Retention period for deleted nodes in days |  [optional] |
|**referenceId** | **Long** | &amp;#128640; Since v4.37.0  Reference ID. Identical across all versions of a file |  [optional] |
|**size** | **Long** | Node size in byte |  [optional] |
|**timestampCreation** | **OffsetDateTime** | &amp;#128640; Since v4.22.0  Time the node was created on external file system |  [optional] |
|**timestampModification** | **OffsetDateTime** | &amp;#128640; Since v4.22.0  Time the content of a node was last modified on external file system |  [optional] |
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
| ROOM | &quot;room&quot; |
| FOLDER | &quot;folder&quot; |
| FILE | &quot;file&quot; |



