

# AuditLogConfig

Provides the configuration for logging a type of permissions. Example: { \"audit_log_configs\": [ { \"log_type\": \"DATA_READ\", \"exempted_members\": [ \"user:jose@example.com\" ] }, { \"log_type\": \"DATA_WRITE\" } ] } This enables 'DATA_READ' and 'DATA_WRITE' logging, while exempting jose@example.com from DATA_READ logging.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**exemptedMembers** | **List&lt;String&gt;** | Specifies the identities that do not cause logging for this type of permission. Follows the same format of Binding.members. |  [optional] |
|**logType** | [**LogTypeEnum**](#LogTypeEnum) | The log type that this config enables. |  [optional] |



## Enum: LogTypeEnum

| Name | Value |
|---- | -----|
| LOG_TYPE_UNSPECIFIED | &quot;LOG_TYPE_UNSPECIFIED&quot; |
| ADMIN_READ | &quot;ADMIN_READ&quot; |
| DATA_WRITE | &quot;DATA_WRITE&quot; |
| DATA_READ | &quot;DATA_READ&quot; |



