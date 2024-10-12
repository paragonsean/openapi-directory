# CloudTpuApi.QueuedResource

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createTime** | **String** | Output only. The time when the QueuedResource was created. | [optional] [readonly] 
**guaranteed** | [**Guaranteed**](Guaranteed.md) |  | [optional] 
**name** | **String** | Output only. Immutable. The name of the QueuedResource. | [optional] [readonly] 
**queueingPolicy** | [**QueueingPolicy**](QueueingPolicy.md) |  | [optional] 
**reservationName** | **String** | Optional. Name of the reservation in which the resource should be provisioned. Format: projects/{project}/locations/{zone}/reservations/{reservation} | [optional] 
**spot** | **Object** | Spot tier definition. | [optional] 
**state** | [**QueuedResourceState**](QueuedResourceState.md) |  | [optional] 
**tpu** | [**Tpu**](Tpu.md) |  | [optional] 


