# CloudDataprocApi.ClusterStatus

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**detail** | **String** | Optional. Output only. Details of cluster&#39;s state. | [optional] [readonly] 
**state** | **String** | Output only. The cluster&#39;s state. | [optional] [readonly] 
**stateStartTime** | **String** | Output only. Time when this state was entered (see JSON representation of Timestamp (https://developers.google.com/protocol-buffers/docs/proto3#json)). | [optional] [readonly] 
**substate** | **String** | Output only. Additional state information that includes status reported by the agent. | [optional] [readonly] 



## Enum: StateEnum


* `UNKNOWN` (value: `"UNKNOWN"`)

* `CREATING` (value: `"CREATING"`)

* `RUNNING` (value: `"RUNNING"`)

* `ERROR` (value: `"ERROR"`)

* `ERROR_DUE_TO_UPDATE` (value: `"ERROR_DUE_TO_UPDATE"`)

* `DELETING` (value: `"DELETING"`)

* `UPDATING` (value: `"UPDATING"`)

* `STOPPING` (value: `"STOPPING"`)

* `STOPPED` (value: `"STOPPED"`)

* `STARTING` (value: `"STARTING"`)

* `REPAIRING` (value: `"REPAIRING"`)





## Enum: SubstateEnum


* `UNSPECIFIED` (value: `"UNSPECIFIED"`)

* `UNHEALTHY` (value: `"UNHEALTHY"`)

* `STALE_STATUS` (value: `"STALE_STATUS"`)




