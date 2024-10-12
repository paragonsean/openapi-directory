

# ImportContextBakImportOptions

Import parameters specific to SQL Server .BAK files

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**bakType** | [**BakTypeEnum**](#BakTypeEnum) | Type of the bak content, FULL or DIFF. |  [optional] |
|**encryptionOptions** | [**ImportContextBakImportOptionsEncryptionOptions**](ImportContextBakImportOptionsEncryptionOptions.md) |  |  [optional] |
|**noRecovery** | **Boolean** | Whether or not the backup importing will restore database with NORECOVERY option Applies only to Cloud SQL for SQL Server. |  [optional] |
|**recoveryOnly** | **Boolean** | Whether or not the backup importing request will just bring database online without downloading Bak content only one of \&quot;no_recovery\&quot; and \&quot;recovery_only\&quot; can be true otherwise error will return. Applies only to Cloud SQL for SQL Server. |  [optional] |
|**stopAt** | **String** | Optional. The timestamp when the import should stop. This timestamp is in the [RFC 3339](https://tools.ietf.org/html/rfc3339) format (for example, &#x60;2023-10-01T16:19:00.094&#x60;). This field is equivalent to the STOPAT keyword and applies to Cloud SQL for SQL Server only. |  [optional] |
|**stopAtMark** | **String** | Optional. The marked transaction where the import should stop. This field is equivalent to the STOPATMARK keyword and applies to Cloud SQL for SQL Server only. |  [optional] |
|**striped** | **Boolean** | Whether or not the backup set being restored is striped. Applies only to Cloud SQL for SQL Server. |  [optional] |



## Enum: BakTypeEnum

| Name | Value |
|---- | -----|
| BAK_TYPE_UNSPECIFIED | &quot;BAK_TYPE_UNSPECIFIED&quot; |
| FULL | &quot;FULL&quot; |
| DIFF | &quot;DIFF&quot; |
| TLOG | &quot;TLOG&quot; |



