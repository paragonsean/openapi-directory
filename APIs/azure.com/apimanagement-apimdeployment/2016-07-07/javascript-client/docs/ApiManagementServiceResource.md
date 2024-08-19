# ApiManagementClient.ApiManagementServiceResource

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**etag** | **String** | ETag of the resource. | [optional] 
**id** | **String** | The ID of the created API Management service. | [optional] [readonly] 
**location** | **String** | Datacenter location of the API Management service. | 
**name** | **String** | Name of the API Management service. | [optional] [readonly] 
**type** | **String** | Resource type of the API Management service. | [optional] [readonly] 
**properties** | [**ApiManagementServiceProperties**](ApiManagementServiceProperties.md) |  | [optional] 
**sku** | [**ApiManagementServiceSkuProperties**](ApiManagementServiceSkuProperties.md) |  | [optional] 
**tags** | **{String: String}** | API Management service tags. A maximum of 10 tags can be provided for a resource, and each tag must have a key no greater than 128 characters (and a value no greater than 256 characters). | [optional] 


