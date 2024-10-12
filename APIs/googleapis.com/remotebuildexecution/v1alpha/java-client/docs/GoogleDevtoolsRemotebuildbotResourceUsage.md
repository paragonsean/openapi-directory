

# GoogleDevtoolsRemotebuildbotResourceUsage

ResourceUsage is the system resource usage of the host machine.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**botState** | [**BotStateEnum**](#BotStateEnum) |  |  [optional] |
|**cpuUsedPercent** | **Double** |  |  [optional] |
|**diskUsage** | [**GoogleDevtoolsRemotebuildbotResourceUsageStat**](GoogleDevtoolsRemotebuildbotResourceUsageStat.md) |  |  [optional] |
|**dockerRootDiskUsage** | [**GoogleDevtoolsRemotebuildbotResourceUsageStat**](GoogleDevtoolsRemotebuildbotResourceUsageStat.md) |  |  [optional] |
|**memoryUsage** | [**GoogleDevtoolsRemotebuildbotResourceUsageStat**](GoogleDevtoolsRemotebuildbotResourceUsageStat.md) |  |  [optional] |
|**totalDiskIoStats** | [**GoogleDevtoolsRemotebuildbotResourceUsageIOStats**](GoogleDevtoolsRemotebuildbotResourceUsageIOStats.md) |  |  [optional] |



## Enum: BotStateEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;UNSPECIFIED&quot; |
| IDLE | &quot;IDLE&quot; |
| BUSY | &quot;BUSY&quot; |



