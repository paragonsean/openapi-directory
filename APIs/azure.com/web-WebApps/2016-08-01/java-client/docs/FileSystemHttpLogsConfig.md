

# FileSystemHttpLogsConfig

Http logs to file system configuration.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**enabled** | **Boolean** | True if configuration is enabled, false if it is disabled and null if configuration is not set. |  [optional] |
|**retentionInDays** | **Integer** | Retention in days. Remove files older than X days. 0 or lower means no retention. |  [optional] |
|**retentionInMb** | **Integer** | Maximum size in megabytes that http log files can use. When reached old log files will be removed to make space for new ones. Value can range between 25 and 100. |  [optional] |



