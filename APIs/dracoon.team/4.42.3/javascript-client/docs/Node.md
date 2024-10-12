# DracoonApi.Node

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authParentId** | **Number** | &amp;#128640; Since v4.15.0  Auth parent room ID | [optional] 
**branchVersion** | **Number** | Version of last change in this node or a node further down the tree. | [optional] 
**children** | [**[Node]**](Node.md) | &amp;#128679; Deprecated since v4.10.0  Child nodes list (if requested)  (for rooms / folders only) | [optional] 
**classification** | **Number** | Classification ID:  * &#x60;1&#x60; - public  * &#x60;2&#x60; - internal  * &#x60;3&#x60; - confidential  * &#x60;4&#x60; - strictly confidential | [optional] 
**cntChildren** | **Number** | &amp;#128679; Deprecated since v4.11.0  Number of direct children  (no recursion; for rooms / folders only) | [optional] 
**cntComments** | **Number** | Returns the number of comments of this node. | [optional] 
**cntDeletedVersions** | **Number** | Number of deleted versions of this file / folder  (for rooms / folders only) | [optional] 
**cntDownloadShares** | **Number** | Returns the number of Download Shares of this node. | [optional] 
**cntFiles** | **Number** | &amp;#128640; Since v4.11.0  Amount of direct child files where this node is the parent node  (no recursion; for rooms / folders only) | [optional] 
**cntFolders** | **Number** | &amp;#128640; Since v4.11.0  Amount of direct child folders where this node is the parent node  (no recursion; for rooms / folders only) | [optional] 
**cntRooms** | **Number** | &amp;#128640; Since v4.11.0  Amount of direct child rooms where this node is the parent node  (no recursion; for rooms only) | [optional] 
**cntUploadShares** | **Number** | Returns the number of Upload Shares of this node. | [optional] 
**createdAt** | **Date** | Creation date | [optional] 
**createdBy** | [**UserInfo**](UserInfo.md) |  | [optional] 
**encryptionInfo** | [**EncryptionInfo**](EncryptionInfo.md) |  | [optional] 
**expireAt** | **Date** | Expiration date | [optional] 
**fileType** | **String** | File type / extension (for files only) | [optional] 
**hasActivitiesLog** | **Boolean** | Is activities log active (for rooms only) | [optional] [default to true]
**hash** | **String** | MD5 hash of file | [optional] 
**id** | **Number** | Node ID | 
**inheritPermissions** | **Boolean** | Inherit permissions from parent room  (default: &#x60;false&#x60; if &#x60;parentId&#x60; is &#x60;0&#x60;; otherwise: &#x60;true&#x60;) | [optional] 
**isBrowsable** | **Boolean** | &amp;#128640; Since v4.11.0  Determines whether node is browsable by client (for rooms only) | [optional] 
**isEncrypted** | **Boolean** | Encryption state | [optional] 
**isFavorite** | **Boolean** | Node is marked as favorite (for rooms / folders only) | [optional] 
**mediaToken** | **String** | Media server media token | [optional] 
**mediaType** | **String** | File media type (for files only) | [optional] 
**name** | **String** | Name | 
**notes** | **String** | User notes | [optional] 
**parentId** | **Number** | Parent node ID (room or folder) | [optional] 
**parentPath** | **String** | Parent node path  &#x60;/&#x60; if node is a root node (room) | [optional] 
**permissions** | [**NodePermissions**](NodePermissions.md) |  | [optional] 
**quota** | **Number** | Quota in byte | [optional] 
**recycleBinRetentionPeriod** | **Number** | Retention period for deleted nodes in days | [optional] 
**referenceId** | **Number** | &amp;#128640; Since v4.37.0  Reference ID. Identical across all versions of a file | [optional] 
**size** | **Number** | Node size in byte | [optional] 
**timestampCreation** | **Date** | &amp;#128640; Since v4.22.0  Time the node was created on external file system | [optional] 
**timestampModification** | **Date** | &amp;#128640; Since v4.22.0  Time the content of a node was last modified on external file system | [optional] 
**type** | **String** | Node type | 
**updatedAt** | **Date** | Modification date | [optional] 
**updatedBy** | [**UserInfo**](UserInfo.md) |  | [optional] 



## Enum: ClassificationEnum


* `1` (value: `1`)

* `2` (value: `2`)

* `3` (value: `3`)

* `4` (value: `4`)





## Enum: TypeEnum


* `room` (value: `"room"`)

* `folder` (value: `"folder"`)

* `file` (value: `"file"`)




