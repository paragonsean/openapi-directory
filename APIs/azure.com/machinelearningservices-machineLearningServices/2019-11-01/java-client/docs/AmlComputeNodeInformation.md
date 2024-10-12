

# AmlComputeNodeInformation

Compute node information related to a AmlCompute.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**nodeId** | **String** | ID of the compute node. |  [optional] [readonly] |
|**nodeState** | [**NodeStateEnum**](#NodeStateEnum) | State of the compute node. Values are idle, running, preparing, unusable, leaving and preempted. |  [optional] [readonly] |
|**port** | **BigDecimal** | SSH port number of the node. |  [optional] [readonly] |
|**privateIpAddress** | **String** | Private IP address of the compute node. |  [optional] [readonly] |
|**publicIpAddress** | **String** | Public IP address of the compute node. |  [optional] [readonly] |
|**runId** | **String** | ID of the Experiment running on the node, if any else null. |  [optional] [readonly] |



## Enum: NodeStateEnum

| Name | Value |
|---- | -----|
| IDLE | &quot;idle&quot; |
| RUNNING | &quot;running&quot; |
| PREPARING | &quot;preparing&quot; |
| UNUSABLE | &quot;unusable&quot; |
| LEAVING | &quot;leaving&quot; |
| PREEMPTED | &quot;preempted&quot; |



