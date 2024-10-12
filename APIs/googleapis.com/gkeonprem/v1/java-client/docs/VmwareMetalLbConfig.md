

# VmwareMetalLbConfig

Represents configuration parameters for the MetalLB load balancer.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**addressPools** | [**List&lt;VmwareAddressPool&gt;**](VmwareAddressPool.md) | Required. AddressPools is a list of non-overlapping IP pools used by load balancer typed services. All addresses must be routable to load balancer nodes. IngressVIP must be included in the pools. |  [optional] |



