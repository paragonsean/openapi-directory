

# Operation

An Operation resource. For successful operations that return an Operation resource, only the fields relevant to the operation are populated in the resource.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**apiWarning** | [**ApiWarning**](ApiWarning.md) |  |  [optional] |
|**backupContext** | [**BackupContext**](BackupContext.md) |  |  [optional] |
|**endTime** | **String** | The time this operation finished in UTC timezone in [RFC 3339](https://tools.ietf.org/html/rfc3339) format, for example &#x60;2012-11-15T16:19:00.094Z&#x60;. |  [optional] |
|**error** | [**OperationErrors**](OperationErrors.md) |  |  [optional] |
|**exportContext** | [**ExportContext**](ExportContext.md) |  |  [optional] |
|**importContext** | [**ImportContext**](ImportContext.md) |  |  [optional] |
|**insertTime** | **String** | The time this operation was enqueued in UTC timezone in [RFC 3339](https://tools.ietf.org/html/rfc3339) format, for example &#x60;2012-11-15T16:19:00.094Z&#x60;. |  [optional] |
|**kind** | **String** | This is always &#x60;sql#operation&#x60;. |  [optional] |
|**name** | **String** | An identifier that uniquely identifies the operation. You can use this identifier to retrieve the Operations resource that has information about the operation. |  [optional] |
|**operationType** | [**OperationTypeEnum**](#OperationTypeEnum) | The type of the operation. Valid values are: * &#x60;CREATE&#x60; * &#x60;DELETE&#x60; * &#x60;UPDATE&#x60; * &#x60;RESTART&#x60; * &#x60;IMPORT&#x60; * &#x60;EXPORT&#x60; * &#x60;BACKUP_VOLUME&#x60; * &#x60;RESTORE_VOLUME&#x60; * &#x60;CREATE_USER&#x60; * &#x60;DELETE_USER&#x60; * &#x60;CREATE_DATABASE&#x60; * &#x60;DELETE_DATABASE&#x60; |  [optional] |
|**selfLink** | **String** | The URI of this resource. |  [optional] |
|**startTime** | **String** | The time this operation actually started in UTC timezone in [RFC 3339](https://tools.ietf.org/html/rfc3339) format, for example &#x60;2012-11-15T16:19:00.094Z&#x60;. |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | The status of an operation. |  [optional] |
|**targetId** | **String** | Name of the database instance related to this operation. |  [optional] |
|**targetLink** | **String** |  |  [optional] |
|**targetProject** | **String** | The project ID of the target instance related to this operation. |  [optional] |
|**user** | **String** | The email address of the user who initiated this operation. |  [optional] |



## Enum: OperationTypeEnum

| Name | Value |
|---- | -----|
| SQL_OPERATION_TYPE_UNSPECIFIED | &quot;SQL_OPERATION_TYPE_UNSPECIFIED&quot; |
| IMPORT | &quot;IMPORT&quot; |
| EXPORT | &quot;EXPORT&quot; |
| CREATE | &quot;CREATE&quot; |
| UPDATE | &quot;UPDATE&quot; |
| DELETE | &quot;DELETE&quot; |
| RESTART | &quot;RESTART&quot; |
| BACKUP | &quot;BACKUP&quot; |
| SNAPSHOT | &quot;SNAPSHOT&quot; |
| BACKUP_VOLUME | &quot;BACKUP_VOLUME&quot; |
| DELETE_VOLUME | &quot;DELETE_VOLUME&quot; |
| RESTORE_VOLUME | &quot;RESTORE_VOLUME&quot; |
| INJECT_USER | &quot;INJECT_USER&quot; |
| CLONE | &quot;CLONE&quot; |
| STOP_REPLICA | &quot;STOP_REPLICA&quot; |
| START_REPLICA | &quot;START_REPLICA&quot; |
| PROMOTE_REPLICA | &quot;PROMOTE_REPLICA&quot; |
| CREATE_REPLICA | &quot;CREATE_REPLICA&quot; |
| CREATE_USER | &quot;CREATE_USER&quot; |
| DELETE_USER | &quot;DELETE_USER&quot; |
| UPDATE_USER | &quot;UPDATE_USER&quot; |
| CREATE_DATABASE | &quot;CREATE_DATABASE&quot; |
| DELETE_DATABASE | &quot;DELETE_DATABASE&quot; |
| UPDATE_DATABASE | &quot;UPDATE_DATABASE&quot; |
| FAILOVER | &quot;FAILOVER&quot; |
| DELETE_BACKUP | &quot;DELETE_BACKUP&quot; |
| RECREATE_REPLICA | &quot;RECREATE_REPLICA&quot; |
| TRUNCATE_LOG | &quot;TRUNCATE_LOG&quot; |
| DEMOTE_MASTER | &quot;DEMOTE_MASTER&quot; |
| MAINTENANCE | &quot;MAINTENANCE&quot; |
| ENABLE_PRIVATE_IP | &quot;ENABLE_PRIVATE_IP&quot; |
| DEFER_MAINTENANCE | &quot;DEFER_MAINTENANCE&quot; |
| CREATE_CLONE | &quot;CREATE_CLONE&quot; |
| RESCHEDULE_MAINTENANCE | &quot;RESCHEDULE_MAINTENANCE&quot; |
| START_EXTERNAL_SYNC | &quot;START_EXTERNAL_SYNC&quot; |
| LOG_CLEANUP | &quot;LOG_CLEANUP&quot; |
| AUTO_RESTART | &quot;AUTO_RESTART&quot; |
| REENCRYPT | &quot;REENCRYPT&quot; |
| SWITCHOVER | &quot;SWITCHOVER&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| SQL_OPERATION_STATUS_UNSPECIFIED | &quot;SQL_OPERATION_STATUS_UNSPECIFIED&quot; |
| PENDING | &quot;PENDING&quot; |
| RUNNING | &quot;RUNNING&quot; |
| DONE | &quot;DONE&quot; |



