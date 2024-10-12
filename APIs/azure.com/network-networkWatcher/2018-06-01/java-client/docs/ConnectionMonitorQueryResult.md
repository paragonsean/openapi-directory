

# ConnectionMonitorQueryResult

List of connection states snapshots.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**sourceStatus** | [**SourceStatusEnum**](#SourceStatusEnum) | Status of connection monitor source. |  [optional] |
|**states** | [**List&lt;ConnectionStateSnapshot&gt;**](ConnectionStateSnapshot.md) | Information about connection states. |  [optional] |



## Enum: SourceStatusEnum

| Name | Value |
|---- | -----|
| UKNOWN | &quot;Uknown&quot; |
| ACTIVE | &quot;Active&quot; |
| INACTIVE | &quot;Inactive&quot; |



