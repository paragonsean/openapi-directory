# CloudTpuApi.QueuedResourceState

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**acceptedData** | **Object** | Further data for the accepted state. | [optional] 
**activeData** | **Object** | Further data for the active state. | [optional] 
**creatingData** | **Object** | Further data for the creating state. | [optional] 
**deletingData** | **Object** | Further data for the deleting state. | [optional] 
**failedData** | [**FailedData**](FailedData.md) |  | [optional] 
**provisioningData** | **Object** | Further data for the provisioning state. | [optional] 
**state** | **String** | State of the QueuedResource request. | [optional] 
**stateInitiator** | **String** | Output only. The initiator of the QueuedResources&#39;s current state. Used to indicate whether the SUSPENDING/SUSPENDED state was initiated by the user or the service. | [optional] [readonly] 
**suspendedData** | **Object** | Further data for the suspended state. | [optional] 
**suspendingData** | **Object** | Further data for the suspending state. | [optional] 



## Enum: StateEnum


* `STATE_UNSPECIFIED` (value: `"STATE_UNSPECIFIED"`)

* `CREATING` (value: `"CREATING"`)

* `ACCEPTED` (value: `"ACCEPTED"`)

* `PROVISIONING` (value: `"PROVISIONING"`)

* `FAILED` (value: `"FAILED"`)

* `DELETING` (value: `"DELETING"`)

* `ACTIVE` (value: `"ACTIVE"`)

* `SUSPENDING` (value: `"SUSPENDING"`)

* `SUSPENDED` (value: `"SUSPENDED"`)

* `WAITING_FOR_RESOURCES` (value: `"WAITING_FOR_RESOURCES"`)





## Enum: StateInitiatorEnum


* `STATE_INITIATOR_UNSPECIFIED` (value: `"STATE_INITIATOR_UNSPECIFIED"`)

* `USER` (value: `"USER"`)

* `SERVICE` (value: `"SERVICE"`)




