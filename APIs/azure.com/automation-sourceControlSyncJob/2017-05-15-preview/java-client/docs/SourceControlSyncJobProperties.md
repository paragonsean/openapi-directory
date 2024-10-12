

# SourceControlSyncJobProperties

Definition of source control sync job properties.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**creationTime** | **OffsetDateTime** | The creation time of the job. |  [optional] [readonly] |
|**endTime** | **OffsetDateTime** | The end time of the job. |  [optional] [readonly] |
|**provisioningState** | [**ProvisioningStateEnum**](#ProvisioningStateEnum) | The provisioning state of the job. |  [optional] |
|**sourceControlSyncJobId** | **String** | The source control sync job id. |  [optional] |
|**startTime** | **OffsetDateTime** | The start time of the job. |  [optional] [readonly] |
|**syncType** | [**SyncTypeEnum**](#SyncTypeEnum) | The sync type. |  [optional] |



## Enum: ProvisioningStateEnum

| Name | Value |
|---- | -----|
| COMPLETED | &quot;Completed&quot; |
| FAILED | &quot;Failed&quot; |
| RUNNING | &quot;Running&quot; |



## Enum: SyncTypeEnum

| Name | Value |
|---- | -----|
| PARTIAL_SYNC | &quot;PartialSync&quot; |
| FULL_SYNC | &quot;FullSync&quot; |



