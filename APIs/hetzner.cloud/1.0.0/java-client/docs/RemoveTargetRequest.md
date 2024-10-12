

# RemoveTargetRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**ip** | [**LoadBalancerTargetIP**](LoadBalancerTargetIP.md) |  |  [optional] |
|**labelSelector** | [**AddTargetRequestLabelSelector**](AddTargetRequestLabelSelector.md) |  |  [optional] |
|**server** | [**AddTargetRequestServer**](AddTargetRequestServer.md) |  |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Type of the resource |  |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| SERVER | &quot;server&quot; |
| LABEL_SELECTOR | &quot;label_selector&quot; |
| IP | &quot;ip&quot; |



