

# ClusterStatus

The status of a cluster and its instances.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**detail** | **String** | Optional. Output only. Details of cluster&#39;s state. |  [optional] [readonly] |
|**state** | [**StateEnum**](#StateEnum) | Output only. The cluster&#39;s state. |  [optional] [readonly] |
|**stateStartTime** | **String** | Output only. Time when this state was entered (see JSON representation of Timestamp (https://developers.google.com/protocol-buffers/docs/proto3#json)). |  [optional] [readonly] |
|**substate** | [**SubstateEnum**](#SubstateEnum) | Output only. Additional state information that includes status reported by the agent. |  [optional] [readonly] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;UNKNOWN&quot; |
| CREATING | &quot;CREATING&quot; |
| RUNNING | &quot;RUNNING&quot; |
| ERROR | &quot;ERROR&quot; |
| ERROR_DUE_TO_UPDATE | &quot;ERROR_DUE_TO_UPDATE&quot; |
| DELETING | &quot;DELETING&quot; |
| UPDATING | &quot;UPDATING&quot; |
| STOPPING | &quot;STOPPING&quot; |
| STOPPED | &quot;STOPPED&quot; |
| STARTING | &quot;STARTING&quot; |
| REPAIRING | &quot;REPAIRING&quot; |



## Enum: SubstateEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;UNSPECIFIED&quot; |
| UNHEALTHY | &quot;UNHEALTHY&quot; |
| STALE_STATUS | &quot;STALE_STATUS&quot; |



