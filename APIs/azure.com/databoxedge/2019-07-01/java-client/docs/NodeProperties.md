

# NodeProperties

This class represents the nodes in a highly available cluster

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**nodeChassisSerialNumber** | **String** | Serial number of the Chassis |  [optional] [readonly] |
|**nodeDisplayName** | **String** | Display Name of the individual node |  [optional] [readonly] |
|**nodeFriendlySoftwareVersion** | **String** | Friendly software version name that is currently installed on the node |  [optional] [readonly] |
|**nodeHcsVersion** | **String** | HCS version that is currently installed on the node |  [optional] [readonly] |
|**nodeInstanceId** | **String** | Guid instance id of the node |  [optional] [readonly] |
|**nodeSerialNumber** | **String** | Serial number of the individual node |  [optional] [readonly] |
|**nodeStatus** | [**NodeStatusEnum**](#NodeStatusEnum) | The current status of the individual node |  [optional] [readonly] |



## Enum: NodeStatusEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;Unknown&quot; |
| UP | &quot;Up&quot; |
| DOWN | &quot;Down&quot; |
| REBOOTING | &quot;Rebooting&quot; |
| SHUTTING_DOWN | &quot;ShuttingDown&quot; |



