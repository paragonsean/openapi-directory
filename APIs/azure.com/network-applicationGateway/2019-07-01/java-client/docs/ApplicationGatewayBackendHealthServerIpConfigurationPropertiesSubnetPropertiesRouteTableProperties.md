

# ApplicationGatewayBackendHealthServerIpConfigurationPropertiesSubnetPropertiesRouteTableProperties

Route Table resource.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**disableBgpRoutePropagation** | **Boolean** | Whether to disable the routes learned by BGP on that route table. True means disable. |  [optional] |
|**provisioningState** | **ProvisioningState** |  |  [optional] |
|**routes** | [**List&lt;ApplicationGatewayBackendHealthServerIpConfigurationPropertiesSubnetPropertiesRouteTablePropertiesRoutesInner&gt;**](ApplicationGatewayBackendHealthServerIpConfigurationPropertiesSubnetPropertiesRouteTablePropertiesRoutesInner.md) | Collection of routes contained within a route table. |  [optional] |
|**subnets** | **List&lt;Subnet&gt;** | A collection of references to subnets. |  [optional] [readonly] |



