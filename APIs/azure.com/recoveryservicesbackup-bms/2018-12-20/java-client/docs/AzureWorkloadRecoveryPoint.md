

# AzureWorkloadRecoveryPoint

Workload specific recovery point, specifically encapsulates full/diff recovery point

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**recoveryPointTimeInUTC** | **OffsetDateTime** | UTC time at which recovery point was created |  [optional] [readonly] |
|**type** | [**TypeEnum**](#TypeEnum) | Type of restore point |  [optional] [readonly] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| INVALID | &quot;Invalid&quot; |
| FULL | &quot;Full&quot; |
| LOG | &quot;Log&quot; |
| DIFFERENTIAL | &quot;Differential&quot; |



