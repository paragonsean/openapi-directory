

# LoadBalancerService


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**destinationPort** | **Integer** | Port the Load Balancer will balance to |  |
|**healthCheck** | [**LoadBalancerServiceHealthCheck**](LoadBalancerServiceHealthCheck.md) |  |  |
|**http** | [**LoadBalancerServiceHTTP**](LoadBalancerServiceHTTP.md) |  |  [optional] |
|**listenPort** | **Integer** | Port the Load Balancer listens on |  |
|**protocol** | [**ProtocolEnum**](#ProtocolEnum) | Protocol of the Load Balancer |  |
|**proxyprotocol** | **Boolean** | Is Proxyprotocol enabled or not |  |



## Enum: ProtocolEnum

| Name | Value |
|---- | -----|
| TCP | &quot;tcp&quot; |
| HTTP | &quot;http&quot; |
| HTTPS | &quot;https&quot; |



