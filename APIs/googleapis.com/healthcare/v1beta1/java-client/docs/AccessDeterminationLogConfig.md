

# AccessDeterminationLogConfig

Configures consent audit log config for FHIR create, read, update, and delete (CRUD) operations. Cloud audit log for healthcare API must be [enabled](https://cloud.google.com/logging/docs/audit/configure-data-access#config-console-enable). The consent-related logs are included as part of `protoPayload.metadata`.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**logLevel** | [**LogLevelEnum**](#LogLevelEnum) | Optional. Controls the amount of detail to include as part of the audit logs. |  [optional] |



## Enum: LogLevelEnum

| Name | Value |
|---- | -----|
| LOG_LEVEL_UNSPECIFIED | &quot;LOG_LEVEL_UNSPECIFIED&quot; |
| DISABLED | &quot;DISABLED&quot; |
| MINIMUM | &quot;MINIMUM&quot; |
| VERBOSE | &quot;VERBOSE&quot; |



