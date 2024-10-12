# AzureMlWebServicesManagementClient.AssetItem

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **String** | Asset&#39;s Id. | [optional] 
**inputPorts** | [**{String: InputPort}**](InputPort.md) | Information about the asset&#39;s input ports. | [optional] 
**locationInfo** | [**BlobLocation**](BlobLocation.md) |  | 
**metadata** | **{String: String}** | If the asset is a custom module, this holds the module&#39;s metadata. | [optional] 
**name** | **String** | Asset&#39;s friendly name. | 
**outputPorts** | [**{String: OutputPort}**](OutputPort.md) | Information about the asset&#39;s output ports. | [optional] 
**parameters** | [**[ModuleAssetParameter]**](ModuleAssetParameter.md) | If the asset is a custom module, this holds the module&#39;s parameters. | [optional] 
**type** | **String** | Asset&#39;s type. | 



## Enum: TypeEnum


* `Module` (value: `"Module"`)

* `Resource` (value: `"Resource"`)




