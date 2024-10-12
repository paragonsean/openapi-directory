

# JobFilter

Filters that can be specified for the job

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**jobType** | [**JobTypeEnum**](#JobTypeEnum) | The job type. |  |
|**startTime** | **OffsetDateTime** | The start time of the job. |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | The job status. |  |



## Enum: JobTypeEnum

| Name | Value |
|---- | -----|
| BACKUP | &quot;Backup&quot; |
| CLONE | &quot;Clone&quot; |
| FAILOVER | &quot;Failover&quot; |
| DOWNLOAD_UPDATES | &quot;DownloadUpdates&quot; |
| INSTALL_UPDATES | &quot;InstallUpdates&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| INVALID | &quot;Invalid&quot; |
| RUNNING | &quot;Running&quot; |
| SUCCEEDED | &quot;Succeeded&quot; |
| FAILED | &quot;Failed&quot; |
| CANCELED | &quot;Canceled&quot; |
| PAUSED | &quot;Paused&quot; |
| SCHEDULED | &quot;Scheduled&quot; |



