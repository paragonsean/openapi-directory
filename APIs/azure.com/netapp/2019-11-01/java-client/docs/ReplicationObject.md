

# ReplicationObject

Replication properties

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**endpointType** | [**EndpointTypeEnum**](#EndpointTypeEnum) | Indicates whether the local volume is the source or destination for the Volume Replication |  [optional] |
|**remoteVolumeRegion** | **String** | The remote region for the other end of the Volume Replication. |  [optional] |
|**remoteVolumeResourceId** | **String** | The resource ID of the remote volume. |  |
|**replicationId** | **String** | Id |  [optional] |
|**replicationSchedule** | [**ReplicationScheduleEnum**](#ReplicationScheduleEnum) | Schedule |  |



## Enum: EndpointTypeEnum

| Name | Value |
|---- | -----|
| SRC | &quot;src&quot; |
| DST | &quot;dst&quot; |



## Enum: ReplicationScheduleEnum

| Name | Value |
|---- | -----|
| _10MINUTELY | &quot;_10minutely&quot; |
| HOURLY | &quot;hourly&quot; |
| DAILY | &quot;daily&quot; |
| WEEKLY | &quot;weekly&quot; |
| MONTHLY | &quot;monthly&quot; |



