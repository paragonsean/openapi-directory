

# RoomData

Room information

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**children** | [**List&lt;RoomData&gt;**](RoomData.md) | &amp;#128679; Deprecated since v4.10.0  List of rooms, where this room is a parent (if exist) |  [optional] |
|**cntDownloadShares** | **Integer** | Returns the number of Download Shares of this node. |  [optional] |
|**cntUploadShares** | **Integer** | Returns the number of Upload Shares of this node. |  [optional] |
|**createdAt** | **OffsetDateTime** | Expiration date |  [optional] |
|**createdBy** | [**UserInfo**](UserInfo.md) |  |  [optional] |
|**hasRecycleBin** | **Boolean** | &amp;#128679; Deprecated since v4.10.0  Is recycle bin active (for rooms only)  Recycle bin is always on (disabling is not possible). |  |
|**id** | **Long** | Room ID |  |
|**isEncrypted** | **Boolean** | Encryption state |  |
|**isFavorite** | **Boolean** | Node is marked as favorite (for rooms / folders only) |  [optional] |
|**isGranted** | **Boolean** | Is user granted room permissions |  |
|**name** | **String** | Name |  |
|**parentId** | **Long** | Parent node ID (room or folder) |  [optional] |
|**permissions** | [**NodePermissions**](NodePermissions.md) |  |  [optional] |
|**quota** | **Long** | Quota in byte |  [optional] |
|**recycleBinRetentionPeriod** | **Integer** | Retention period for deleted nodes in days |  |
|**size** | **Long** | Room size |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Node type |  [optional] |
|**updatedAt** | **OffsetDateTime** | Modification date |  [optional] |
|**updatedBy** | [**UserInfo**](UserInfo.md) |  |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| ROOM | &quot;room&quot; |



