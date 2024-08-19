

# AdditionalLocation

Description of an additional API Management resource location.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**disableGateway** | **Boolean** | Property only valid for an Api Management service deployed in multiple locations. This can be used to disable the gateway in this additional location. |  [optional] |
|**gatewayRegionalUrl** | **String** | Gateway URL of the API Management service in the Region. |  [optional] [readonly] |
|**location** | **String** | The location name of the additional region among Azure Data center regions. |  |
|**privateIPAddresses** | **List&lt;String&gt;** | Private Static Load Balanced IP addresses of the API Management service which is deployed in an Internal Virtual Network in a particular additional location. Available only for Basic, Standard and Premium SKU. |  [optional] [readonly] |
|**publicIPAddresses** | **List&lt;String&gt;** | Public Static Load Balanced IP addresses of the API Management service in the additional location. Available only for Basic, Standard and Premium SKU. |  [optional] [readonly] |
|**sku** | [**ApiManagementServiceSkuProperties**](ApiManagementServiceSkuProperties.md) |  |  |
|**virtualNetworkConfiguration** | [**VirtualNetworkConfiguration**](VirtualNetworkConfiguration.md) |  |  [optional] |



