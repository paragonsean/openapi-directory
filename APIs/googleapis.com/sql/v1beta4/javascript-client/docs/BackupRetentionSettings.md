# CloudSqlAdminApi.BackupRetentionSettings

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**retainedBackups** | **Number** | Depending on the value of retention_unit, this is used to determine if a backup needs to be deleted. If retention_unit is &#39;COUNT&#39;, we will retain this many backups. | [optional] 
**retentionUnit** | **String** | The unit that &#39;retained_backups&#39; represents. | [optional] 



## Enum: RetentionUnitEnum


* `RETENTION_UNIT_UNSPECIFIED` (value: `"RETENTION_UNIT_UNSPECIFIED"`)

* `COUNT` (value: `"COUNT"`)




