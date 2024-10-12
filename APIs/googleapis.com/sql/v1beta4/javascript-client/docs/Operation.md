# CloudSqlAdminApi.Operation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apiWarning** | [**ApiWarning**](ApiWarning.md) |  | [optional] 
**backupContext** | [**BackupContext**](BackupContext.md) |  | [optional] 
**endTime** | **String** | The time this operation finished in UTC timezone in [RFC 3339](https://tools.ietf.org/html/rfc3339) format, for example &#x60;2012-11-15T16:19:00.094Z&#x60;. | [optional] 
**error** | [**OperationErrors**](OperationErrors.md) |  | [optional] 
**exportContext** | [**ExportContext**](ExportContext.md) |  | [optional] 
**importContext** | [**ImportContext**](ImportContext.md) |  | [optional] 
**insertTime** | **String** | The time this operation was enqueued in UTC timezone in [RFC 3339](https://tools.ietf.org/html/rfc3339) format, for example &#x60;2012-11-15T16:19:00.094Z&#x60;. | [optional] 
**kind** | **String** | This is always &#x60;sql#operation&#x60;. | [optional] 
**name** | **String** | An identifier that uniquely identifies the operation. You can use this identifier to retrieve the Operations resource that has information about the operation. | [optional] 
**operationType** | **String** | The type of the operation. Valid values are: * &#x60;CREATE&#x60; * &#x60;DELETE&#x60; * &#x60;UPDATE&#x60; * &#x60;RESTART&#x60; * &#x60;IMPORT&#x60; * &#x60;EXPORT&#x60; * &#x60;BACKUP_VOLUME&#x60; * &#x60;RESTORE_VOLUME&#x60; * &#x60;CREATE_USER&#x60; * &#x60;DELETE_USER&#x60; * &#x60;CREATE_DATABASE&#x60; * &#x60;DELETE_DATABASE&#x60; | [optional] 
**selfLink** | **String** | The URI of this resource. | [optional] 
**startTime** | **String** | The time this operation actually started in UTC timezone in [RFC 3339](https://tools.ietf.org/html/rfc3339) format, for example &#x60;2012-11-15T16:19:00.094Z&#x60;. | [optional] 
**status** | **String** | The status of an operation. | [optional] 
**targetId** | **String** | Name of the database instance related to this operation. | [optional] 
**targetLink** | **String** |  | [optional] 
**targetProject** | **String** | The project ID of the target instance related to this operation. | [optional] 
**user** | **String** | The email address of the user who initiated this operation. | [optional] 



## Enum: OperationTypeEnum


* `SQL_OPERATION_TYPE_UNSPECIFIED` (value: `"SQL_OPERATION_TYPE_UNSPECIFIED"`)

* `IMPORT` (value: `"IMPORT"`)

* `EXPORT` (value: `"EXPORT"`)

* `CREATE` (value: `"CREATE"`)

* `UPDATE` (value: `"UPDATE"`)

* `DELETE` (value: `"DELETE"`)

* `RESTART` (value: `"RESTART"`)

* `BACKUP` (value: `"BACKUP"`)

* `SNAPSHOT` (value: `"SNAPSHOT"`)

* `BACKUP_VOLUME` (value: `"BACKUP_VOLUME"`)

* `DELETE_VOLUME` (value: `"DELETE_VOLUME"`)

* `RESTORE_VOLUME` (value: `"RESTORE_VOLUME"`)

* `INJECT_USER` (value: `"INJECT_USER"`)

* `CLONE` (value: `"CLONE"`)

* `STOP_REPLICA` (value: `"STOP_REPLICA"`)

* `START_REPLICA` (value: `"START_REPLICA"`)

* `PROMOTE_REPLICA` (value: `"PROMOTE_REPLICA"`)

* `CREATE_REPLICA` (value: `"CREATE_REPLICA"`)

* `CREATE_USER` (value: `"CREATE_USER"`)

* `DELETE_USER` (value: `"DELETE_USER"`)

* `UPDATE_USER` (value: `"UPDATE_USER"`)

* `CREATE_DATABASE` (value: `"CREATE_DATABASE"`)

* `DELETE_DATABASE` (value: `"DELETE_DATABASE"`)

* `UPDATE_DATABASE` (value: `"UPDATE_DATABASE"`)

* `FAILOVER` (value: `"FAILOVER"`)

* `DELETE_BACKUP` (value: `"DELETE_BACKUP"`)

* `RECREATE_REPLICA` (value: `"RECREATE_REPLICA"`)

* `TRUNCATE_LOG` (value: `"TRUNCATE_LOG"`)

* `DEMOTE_MASTER` (value: `"DEMOTE_MASTER"`)

* `MAINTENANCE` (value: `"MAINTENANCE"`)

* `ENABLE_PRIVATE_IP` (value: `"ENABLE_PRIVATE_IP"`)

* `DEFER_MAINTENANCE` (value: `"DEFER_MAINTENANCE"`)

* `CREATE_CLONE` (value: `"CREATE_CLONE"`)

* `RESCHEDULE_MAINTENANCE` (value: `"RESCHEDULE_MAINTENANCE"`)

* `START_EXTERNAL_SYNC` (value: `"START_EXTERNAL_SYNC"`)

* `LOG_CLEANUP` (value: `"LOG_CLEANUP"`)

* `AUTO_RESTART` (value: `"AUTO_RESTART"`)

* `REENCRYPT` (value: `"REENCRYPT"`)

* `SWITCHOVER` (value: `"SWITCHOVER"`)





## Enum: StatusEnum


* `SQL_OPERATION_STATUS_UNSPECIFIED` (value: `"SQL_OPERATION_STATUS_UNSPECIFIED"`)

* `PENDING` (value: `"PENDING"`)

* `RUNNING` (value: `"RUNNING"`)

* `DONE` (value: `"DONE"`)




