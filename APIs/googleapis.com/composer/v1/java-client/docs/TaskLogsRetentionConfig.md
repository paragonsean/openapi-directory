

# TaskLogsRetentionConfig

The configuration setting for Task Logs.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**storageMode** | [**StorageModeEnum**](#StorageModeEnum) | Optional. The mode of storage for Airflow workers task logs. For details, see go/composer-store-task-logs-in-cloud-logging-only-design-doc |  [optional] |



## Enum: StorageModeEnum

| Name | Value |
|---- | -----|
| TASK_LOGS_STORAGE_MODE_UNSPECIFIED | &quot;TASK_LOGS_STORAGE_MODE_UNSPECIFIED&quot; |
| CLOUD_LOGGING_AND_CLOUD_STORAGE | &quot;CLOUD_LOGGING_AND_CLOUD_STORAGE&quot; |
| CLOUD_LOGGING_ONLY | &quot;CLOUD_LOGGING_ONLY&quot; |



