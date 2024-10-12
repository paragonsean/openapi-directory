

# ResourceGroup

Resource group information.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | Gets the ID of the resource group. |  [optional] [readonly] |
|**location** | **String** | Gets or sets the location of the resource group. It cannot be changed after the resource group has been created. Has to be one of the supported Azure Locations, such as West US, East US, West Europe, East Asia, etc. |  |
|**name** | **String** | Gets or sets the Name of the resource group. |  [optional] |
|**properties** | [**ResourceGroupProperties**](ResourceGroupProperties.md) |  |  [optional] |
|**tags** | **Map&lt;String, String&gt;** | Gets or sets the tags attached to the resource group. |  [optional] |



