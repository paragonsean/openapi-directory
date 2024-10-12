# HetznerCloudApi.LoadBalancerService

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**destinationPort** | **Number** | Port the Load Balancer will balance to | 
**healthCheck** | [**LoadBalancerServiceHealthCheck**](LoadBalancerServiceHealthCheck.md) |  | 
**http** | [**LoadBalancerServiceHTTP**](LoadBalancerServiceHTTP.md) |  | [optional] 
**listenPort** | **Number** | Port the Load Balancer listens on | 
**protocol** | **String** | Protocol of the Load Balancer | 
**proxyprotocol** | **Boolean** | Is Proxyprotocol enabled or not | 



## Enum: ProtocolEnum


* `tcp` (value: `"tcp"`)

* `http` (value: `"http"`)

* `https` (value: `"https"`)




