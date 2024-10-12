# DataBoxEdgeManagementClient.DataBoxEdgeDevice

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**etag** | **String** | The etag for the devices. | [optional] 
**location** | **String** | The location of the device. This is a supported and registered Azure geographical region (for example, West US, East US, or Southeast Asia). The geographical region of a device cannot be changed once it is created, but if an identical geographical region is specified on update, the request will succeed. | 
**properties** | [**DataBoxEdgeDeviceProperties**](DataBoxEdgeDeviceProperties.md) |  | [optional] 
**sku** | [**Sku**](Sku.md) |  | [optional] 
**tags** | **{String: String}** | The list of tags that describe the device. These tags can be used to view and group this device (across resource groups). | [optional] 
**id** | **String** | The path ID that uniquely identifies the object. | [optional] [readonly] 
**name** | **String** | The object name. | [optional] [readonly] 
**type** | **String** | The hierarchical type of the object. | [optional] [readonly] 


