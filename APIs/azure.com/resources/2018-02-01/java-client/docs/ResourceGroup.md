

# ResourceGroup

Resource group information.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | The ID of the resource group. |  [optional] [readonly] |
|**location** | **String** | The location of the resource group. It cannot be changed after the resource group has been created. It must be one of the supported Azure locations. |  |
|**managedBy** | **String** | The ID of the resource that manages this resource group. |  [optional] |
|**name** | **String** | The name of the resource group. |  [optional] |
|**properties** | [**ResourceGroupProperties**](ResourceGroupProperties.md) |  |  [optional] |
|**tags** | **Map&lt;String, String&gt;** | The tags attached to the resource group. |  [optional] |



