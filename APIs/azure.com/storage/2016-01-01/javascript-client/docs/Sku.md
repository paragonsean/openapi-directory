# StorageManagementClient.Sku

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **String** | Gets or sets the sku name. Required for account creation; optional for update. Note that in older versions, sku name was called accountType. | 
**tier** | **String** | Gets the sku tier. This is based on the SKU name. | [optional] [readonly] 



## Enum: NameEnum


* `Standard_LRS` (value: `"Standard_LRS"`)

* `Standard_GRS` (value: `"Standard_GRS"`)

* `Standard_RAGRS` (value: `"Standard_RAGRS"`)

* `Standard_ZRS` (value: `"Standard_ZRS"`)

* `Premium_LRS` (value: `"Premium_LRS"`)





## Enum: TierEnum


* `Standard` (value: `"Standard"`)

* `Premium` (value: `"Premium"`)




