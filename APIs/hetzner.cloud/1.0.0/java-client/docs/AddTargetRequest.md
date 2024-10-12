

# AddTargetRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**ip** | [**LoadBalancerTargetIP**](LoadBalancerTargetIP.md) |  |  [optional] |
|**labelSelector** | [**AddTargetRequestLabelSelector**](AddTargetRequestLabelSelector.md) |  |  [optional] |
|**server** | [**AddTargetRequestServer**](AddTargetRequestServer.md) |  |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Type of the resource |  |
|**usePrivateIp** | **Boolean** | Use the private network IP instead of the public IP of the Server, requires the Server and Load Balancer to be in the same network. Default value is false. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| SERVER | &quot;server&quot; |
| LABEL_SELECTOR | &quot;label_selector&quot; |
| IP | &quot;ip&quot; |



