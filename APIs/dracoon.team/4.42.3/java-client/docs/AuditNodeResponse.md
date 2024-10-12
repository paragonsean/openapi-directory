

# AuditNodeResponse

Audit node report

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**auditUserPermissionList** | [**List&lt;AuditUserPermission&gt;**](AuditUserPermission.md) | List of assigned users with permissions |  |
|**nodeCntChildren** | **Integer** | Number of direct children  (no recursion; for rooms only) |  |
|**nodeCreatedAt** | **OffsetDateTime** | Creation date |  [optional] |
|**nodeCreatedBy** | [**UserInfo**](UserInfo.md) |  |  [optional] |
|**nodeHasActivitiesLog** | **Boolean** | Is activities log active (for rooms only) |  [optional] |
|**nodeHasRecycleBin** | **Boolean** | &amp;#128679; Deprecated since v4.10.0  Is recycle bin active (for rooms only)  Recycle bin is always on (disabling is not possible). |  [optional] |
|**nodeId** | **Long** | Node ID |  |
|**nodeIsEncrypted** | **Boolean** | Encryption state |  [optional] |
|**nodeName** | **String** | Node name |  |
|**nodeParentId** | **Long** | Parent node ID (room or folder) |  [optional] |
|**nodeParentPath** | **String** | Parent node path  &#x60;/&#x60; if node is a root node (room) |  |
|**nodeQuota** | **Long** | Quota in byte |  [optional] |
|**nodeRecycleBinRetentionPeriod** | **Integer** | Retention period for deleted nodes in days |  [optional] |
|**nodeSize** | **Long** | Node size in byte |  [optional] |
|**nodeUpdatedAt** | **OffsetDateTime** | Modification date |  [optional] |
|**nodeUpdatedBy** | [**UserInfo**](UserInfo.md) |  |  [optional] |



