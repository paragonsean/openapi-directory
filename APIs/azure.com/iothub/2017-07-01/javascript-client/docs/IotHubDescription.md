# IotHubClient.IotHubDescription

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**etag** | **String** | The Etag field is *not* required. If it is provided in the response body, it must also be provided as a header per the normal ETag convention. | [optional] 
**properties** | [**IotHubProperties**](IotHubProperties.md) |  | [optional] 
**resourcegroup** | **String** | The name of the resource group that contains the IoT hub. A resource group name uniquely identifies the resource group within the subscription. | 
**sku** | [**IotHubSkuInfo**](IotHubSkuInfo.md) |  | 
**subscriptionid** | **String** | The subscription identifier. | 
**id** | **String** | The resource identifier. | [optional] [readonly] 
**location** | **String** | The resource location. | 
**name** | **String** | The resource name. | [optional] [readonly] 
**tags** | **{String: String}** | The resource tags. | [optional] 
**type** | **String** | The resource type. | [optional] [readonly] 


