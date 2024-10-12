# DracoonApi.AuditNodeResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auditUserPermissionList** | [**[AuditUserPermission]**](AuditUserPermission.md) | List of assigned users with permissions | 
**nodeCntChildren** | **Number** | Number of direct children  (no recursion; for rooms only) | 
**nodeCreatedAt** | **Date** | Creation date | [optional] 
**nodeCreatedBy** | [**UserInfo**](UserInfo.md) |  | [optional] 
**nodeHasActivitiesLog** | **Boolean** | Is activities log active (for rooms only) | [optional] [default to true]
**nodeHasRecycleBin** | **Boolean** | &amp;#128679; Deprecated since v4.10.0  Is recycle bin active (for rooms only)  Recycle bin is always on (disabling is not possible). | [optional] 
**nodeId** | **Number** | Node ID | 
**nodeIsEncrypted** | **Boolean** | Encryption state | [optional] 
**nodeName** | **String** | Node name | 
**nodeParentId** | **Number** | Parent node ID (room or folder) | [optional] 
**nodeParentPath** | **String** | Parent node path  &#x60;/&#x60; if node is a root node (room) | 
**nodeQuota** | **Number** | Quota in byte | [optional] 
**nodeRecycleBinRetentionPeriod** | **Number** | Retention period for deleted nodes in days | [optional] 
**nodeSize** | **Number** | Node size in byte | [optional] 
**nodeUpdatedAt** | **Date** | Modification date | [optional] 
**nodeUpdatedBy** | [**UserInfo**](UserInfo.md) |  | [optional] 


