# CloudRunAdminApi.AuditLogConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exemptedMembers** | **[String]** | Specifies the identities that do not cause logging for this type of permission. Follows the same format of Binding.members. | [optional] 
**logType** | **String** | The log type that this config enables. | [optional] 



## Enum: LogTypeEnum


* `LOG_TYPE_UNSPECIFIED` (value: `"LOG_TYPE_UNSPECIFIED"`)

* `ADMIN_READ` (value: `"ADMIN_READ"`)

* `DATA_WRITE` (value: `"DATA_WRITE"`)

* `DATA_READ` (value: `"DATA_READ"`)




