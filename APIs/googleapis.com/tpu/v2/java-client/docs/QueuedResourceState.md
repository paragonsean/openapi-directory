

# QueuedResourceState

QueuedResourceState defines the details of the QueuedResource request.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**acceptedData** | **Object** | Further data for the accepted state. |  [optional] |
|**activeData** | **Object** | Further data for the active state. |  [optional] |
|**creatingData** | **Object** | Further data for the creating state. |  [optional] |
|**deletingData** | **Object** | Further data for the deleting state. |  [optional] |
|**failedData** | [**FailedData**](FailedData.md) |  |  [optional] |
|**provisioningData** | **Object** | Further data for the provisioning state. |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | Output only. State of the QueuedResource request. |  [optional] [readonly] |
|**stateInitiator** | [**StateInitiatorEnum**](#StateInitiatorEnum) | Output only. The initiator of the QueuedResources&#39;s current state. Used to indicate whether the SUSPENDING/SUSPENDED state was initiated by the user or the service. |  [optional] [readonly] |
|**suspendedData** | **Object** | Further data for the suspended state. |  [optional] |
|**suspendingData** | **Object** | Further data for the suspending state. |  [optional] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| CREATING | &quot;CREATING&quot; |
| ACCEPTED | &quot;ACCEPTED&quot; |
| PROVISIONING | &quot;PROVISIONING&quot; |
| FAILED | &quot;FAILED&quot; |
| DELETING | &quot;DELETING&quot; |
| ACTIVE | &quot;ACTIVE&quot; |
| SUSPENDING | &quot;SUSPENDING&quot; |
| SUSPENDED | &quot;SUSPENDED&quot; |
| WAITING_FOR_RESOURCES | &quot;WAITING_FOR_RESOURCES&quot; |



## Enum: StateInitiatorEnum

| Name | Value |
|---- | -----|
| STATE_INITIATOR_UNSPECIFIED | &quot;STATE_INITIATOR_UNSPECIFIED&quot; |
| USER | &quot;USER&quot; |
| SERVICE | &quot;SERVICE&quot; |



