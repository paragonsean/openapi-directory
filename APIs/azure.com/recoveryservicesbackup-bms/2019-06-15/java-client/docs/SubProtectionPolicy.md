

# SubProtectionPolicy

Sub-protection policy which includes schedule and retention

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**policyType** | [**PolicyTypeEnum**](#PolicyTypeEnum) | Type of backup policy type |  [optional] |
|**retentionPolicy** | [**RetentionPolicy**](RetentionPolicy.md) |  |  [optional] |
|**schedulePolicy** | [**SchedulePolicy**](SchedulePolicy.md) |  |  [optional] |



## Enum: PolicyTypeEnum

| Name | Value |
|---- | -----|
| INVALID | &quot;Invalid&quot; |
| FULL | &quot;Full&quot; |
| DIFFERENTIAL | &quot;Differential&quot; |
| LOG | &quot;Log&quot; |
| COPY_ONLY_FULL | &quot;CopyOnlyFull&quot; |



