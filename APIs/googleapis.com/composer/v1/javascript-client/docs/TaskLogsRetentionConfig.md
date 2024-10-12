# CloudComposerApi.TaskLogsRetentionConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**storageMode** | **String** | Optional. The mode of storage for Airflow workers task logs. For details, see go/composer-store-task-logs-in-cloud-logging-only-design-doc | [optional] 



## Enum: StorageModeEnum


* `TASK_LOGS_STORAGE_MODE_UNSPECIFIED` (value: `"TASK_LOGS_STORAGE_MODE_UNSPECIFIED"`)

* `CLOUD_LOGGING_AND_CLOUD_STORAGE` (value: `"CLOUD_LOGGING_AND_CLOUD_STORAGE"`)

* `CLOUD_LOGGING_ONLY` (value: `"CLOUD_LOGGING_ONLY"`)




