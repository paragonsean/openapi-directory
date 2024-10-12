# ApiManagementClient.AdditionalLocation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gatewayRegionalUrl** | **String** | Gateway URL of the API Management service in the Region. | [optional] [readonly] 
**location** | **String** | The location name of the additional region among Azure Data center regions. | 
**privateIPAddresses** | **[String]** | Private Static Load Balanced IP addresses of the API Management service which is deployed in an Internal Virtual Network in a particular additional location. Available only for Basic, Standard and Premium SKU. | [optional] [readonly] 
**publicIPAddresses** | **[String]** | Public Static Load Balanced IP addresses of the API Management service in the additional location. Available only for Basic, Standard and Premium SKU. | [optional] [readonly] 
**sku** | [**ApiManagementServiceSkuProperties**](ApiManagementServiceSkuProperties.md) |  | 
**virtualNetworkConfiguration** | [**VirtualNetworkConfiguration**](VirtualNetworkConfiguration.md) |  | [optional] 


