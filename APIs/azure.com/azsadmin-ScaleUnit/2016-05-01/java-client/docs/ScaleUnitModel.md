

# ScaleUnitModel

Properties of a scale unit.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**isMultiNode** | **Boolean** | Denotes if more than one node in cluster. |  [optional] |
|**logicalFaultDomain** | **Integer** | Fault domain name of the cluster. |  [optional] |
|**model** | **String** | Model of the servers in the cluster. |  [optional] |
|**nodes** | **List&lt;String&gt;** | List of nodes in the server. |  [optional] |
|**scaleUnitType** | [**ScaleUnitTypeEnum**](#ScaleUnitTypeEnum) | Type of cluster. |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | Current state of the cluster. |  [optional] |
|**totalCapacity** | [**ScaleUnitCapacity**](ScaleUnitCapacity.md) |  |  [optional] |



## Enum: ScaleUnitTypeEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;Unknown&quot; |
| COMPUTE_ONLY | &quot;ComputeOnly&quot; |
| STORAGE_ONLY | &quot;StorageOnly&quot; |
| HYPER_CONVERGED | &quot;HyperConverged&quot; |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;Unknown&quot; |
| CREATING | &quot;Creating&quot; |
| RUNNING | &quot;Running&quot; |
| UPGRADING | &quot;Upgrading&quot; |
| DELETING | &quot;Deleting&quot; |



