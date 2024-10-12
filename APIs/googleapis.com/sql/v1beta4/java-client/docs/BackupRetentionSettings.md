

# BackupRetentionSettings

We currently only support backup retention by specifying the number of backups we will retain.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**retainedBackups** | **Integer** | Depending on the value of retention_unit, this is used to determine if a backup needs to be deleted. If retention_unit is &#39;COUNT&#39;, we will retain this many backups. |  [optional] |
|**retentionUnit** | [**RetentionUnitEnum**](#RetentionUnitEnum) | The unit that &#39;retained_backups&#39; represents. |  [optional] |



## Enum: RetentionUnitEnum

| Name | Value |
|---- | -----|
| RETENTION_UNIT_UNSPECIFIED | &quot;RETENTION_UNIT_UNSPECIFIED&quot; |
| COUNT | &quot;COUNT&quot; |



