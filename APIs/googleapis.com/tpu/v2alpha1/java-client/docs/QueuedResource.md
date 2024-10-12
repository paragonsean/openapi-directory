

# QueuedResource

A QueuedResource represents a request for resources that will be placed in a queue and fulfilled when the necessary resources are available.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**bestEffort** | **Object** | BestEffort tier definition. |  [optional] |
|**createTime** | **String** | Output only. The time when the QueuedResource was created. |  [optional] [readonly] |
|**guaranteed** | [**Guaranteed**](Guaranteed.md) |  |  [optional] |
|**name** | **String** | Output only. Immutable. The name of the QueuedResource. |  [optional] [readonly] |
|**queueingPolicy** | [**QueueingPolicy**](QueueingPolicy.md) |  |  [optional] |
|**reservationName** | **String** | Name of the reservation in which the resource should be provisioned. Format: projects/{project}/locations/{zone}/reservations/{reservation} |  [optional] |
|**spot** | **Object** | Spot tier definition. |  [optional] |
|**state** | [**QueuedResourceState**](QueuedResourceState.md) |  |  [optional] |
|**tpu** | [**Tpu**](Tpu.md) |  |  [optional] |



