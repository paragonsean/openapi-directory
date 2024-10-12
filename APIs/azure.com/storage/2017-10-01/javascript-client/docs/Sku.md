# StorageManagement.Sku

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**capabilities** | [**[SKUCapability]**](SKUCapability.md) | The capability information in the specified sku, including file encryption, network acls, change notification, etc. | [optional] [readonly] 
**kind** | **String** | Indicates the type of storage account. | [optional] [readonly] 
**locations** | **[String]** | The set of locations that the SKU is available. This will be supported and registered Azure Geo Regions (e.g. West US, East US, Southeast Asia, etc.). | [optional] [readonly] 
**name** | **String** | Gets or sets the sku name. Required for account creation; optional for update. Note that in older versions, sku name was called accountType. | 
**resourceType** | **String** | The type of the resource, usually it is &#39;storageAccounts&#39;. | [optional] [readonly] 
**restrictions** | [**[Restriction]**](Restriction.md) | The restrictions because of which SKU cannot be used. This is empty if there are no restrictions. | [optional] 
**tier** | **String** | Gets the sku tier. This is based on the SKU name. | [optional] [readonly] 



## Enum: KindEnum


* `Storage` (value: `"Storage"`)

* `StorageV2` (value: `"StorageV2"`)

* `BlobStorage` (value: `"BlobStorage"`)





## Enum: NameEnum


* `Standard_LRS` (value: `"Standard_LRS"`)

* `Standard_GRS` (value: `"Standard_GRS"`)

* `Standard_RAGRS` (value: `"Standard_RAGRS"`)

* `Standard_ZRS` (value: `"Standard_ZRS"`)

* `Premium_LRS` (value: `"Premium_LRS"`)





## Enum: TierEnum


* `Standard` (value: `"Standard"`)

* `Premium` (value: `"Premium"`)




