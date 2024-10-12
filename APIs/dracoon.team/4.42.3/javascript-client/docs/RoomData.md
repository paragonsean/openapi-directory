# DracoonApi.RoomData

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**children** | [**[RoomData]**](RoomData.md) | &amp;#128679; Deprecated since v4.10.0  List of rooms, where this room is a parent (if exist) | [optional] 
**cntDownloadShares** | **Number** | Returns the number of Download Shares of this node. | [optional] 
**cntUploadShares** | **Number** | Returns the number of Upload Shares of this node. | [optional] 
**createdAt** | **Date** | Expiration date | [optional] 
**createdBy** | [**UserInfo**](UserInfo.md) |  | [optional] 
**hasRecycleBin** | **Boolean** | &amp;#128679; Deprecated since v4.10.0  Is recycle bin active (for rooms only)  Recycle bin is always on (disabling is not possible). | 
**id** | **Number** | Room ID | 
**isEncrypted** | **Boolean** | Encryption state | 
**isFavorite** | **Boolean** | Node is marked as favorite (for rooms / folders only) | [optional] 
**isGranted** | **Boolean** | Is user granted room permissions | 
**name** | **String** | Name | 
**parentId** | **Number** | Parent node ID (room or folder) | [optional] 
**permissions** | [**NodePermissions**](NodePermissions.md) |  | [optional] 
**quota** | **Number** | Quota in byte | [optional] 
**recycleBinRetentionPeriod** | **Number** | Retention period for deleted nodes in days | 
**size** | **Number** | Room size | [optional] 
**type** | **String** | Node type | [optional] 
**updatedAt** | **Date** | Modification date | [optional] 
**updatedBy** | [**UserInfo**](UserInfo.md) |  | [optional] 



## Enum: TypeEnum


* `room` (value: `"room"`)




