

# ApplicationGatewayBackendHealthServerIpConfigurationPropertiesSubnetPropertiesRouteTableProperties

Route Table resource.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**disableBgpRoutePropagation** | **Boolean** | Gets or sets whether to disable the routes learned by BGP on that route table. True means disable. |  [optional] |
|**provisioningState** | **String** | The provisioning state of the resource. Possible values are: &#39;Updating&#39;, &#39;Deleting&#39;, and &#39;Failed&#39;. |  [optional] |
|**routes** | [**List&lt;ApplicationGatewayBackendHealthServerIpConfigurationPropertiesSubnetPropertiesRouteTablePropertiesRoutesInner&gt;**](ApplicationGatewayBackendHealthServerIpConfigurationPropertiesSubnetPropertiesRouteTablePropertiesRoutesInner.md) | Collection of routes contained within a route table. |  [optional] |
|**subnets** | **List&lt;Subnet&gt;** | A collection of references to subnets. |  [optional] [readonly] |



