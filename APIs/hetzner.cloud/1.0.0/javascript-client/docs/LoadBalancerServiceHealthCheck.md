# HetznerCloudApi.LoadBalancerServiceHealthCheck

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**http** | [**LoadBalancerServiceHealthCheckHttp**](LoadBalancerServiceHealthCheckHttp.md) |  | [optional] 
**interval** | **Number** | Time interval in seconds health checks are performed | 
**port** | **Number** | Port the health check will be performed on | 
**protocol** | **String** | Type of the health check | 
**retries** | **Number** | Unsuccessful retries needed until a target is considered unhealthy; an unhealthy target needs the same number of successful retries to become healthy again | 
**timeout** | **Number** | Time in seconds after an attempt is considered a timeout | 



## Enum: ProtocolEnum


* `tcp` (value: `"tcp"`)

* `http` (value: `"http"`)




