# AzureDedicatedHsmResourceProvider.Resource

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **String** | The Azure Resource Manager resource ID for the dedicated HSM. | [optional] [readonly] 
**location** | **String** | The supported Azure location where the dedicated HSM should be created. | 
**name** | **String** | The name of the dedicated HSM. | [optional] [readonly] 
**sku** | [**Sku**](Sku.md) |  | [optional] 
**tags** | **{String: String}** | Resource tags | [optional] 
**type** | **String** | The resource type of the dedicated HSM. | [optional] [readonly] 
**zones** | **[String]** | The Dedicated Hsm zones. | [optional] 


