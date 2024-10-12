

# PortMapping

Returns the ports and associated IP addresses and ports of Amazon EC2 instances in your virtual private cloud (VPC) subnets. Custom routing is a port mapping protocol in Global Accelerator that statically associates port ranges with VPC subnets, which allows Global Accelerator to route to specific instances and ports within one or more subnets. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**acceleratorPort** | [**Integer**](Integer.md) |  |  [optional] |
|**endpointGroupArn** | [**String**](String.md) |  |  [optional] |
|**endpointId** | [**String**](String.md) |  |  [optional] |
|**destinationSocketAddress** | [**PortMappingDestinationSocketAddress**](PortMappingDestinationSocketAddress.md) |  |  [optional] |
|**protocols** | [**List**](List.md) |  |  [optional] |
|**destinationTrafficState** | [**CustomRoutingDestinationTrafficState**](CustomRoutingDestinationTrafficState.md) |  |  [optional] |



