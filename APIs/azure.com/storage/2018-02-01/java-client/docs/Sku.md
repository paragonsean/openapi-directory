

# Sku

The SKU of the storage account.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**capabilities** | [**List&lt;SKUCapability&gt;**](SKUCapability.md) | The capability information in the specified sku, including file encryption, network acls, change notification, etc. |  [optional] [readonly] |
|**kind** | [**KindEnum**](#KindEnum) | Indicates the type of storage account. |  [optional] [readonly] |
|**locations** | **List&lt;String&gt;** | The set of locations that the SKU is available. This will be supported and registered Azure Geo Regions (e.g. West US, East US, Southeast Asia, etc.). |  [optional] [readonly] |
|**name** | [**NameEnum**](#NameEnum) | Gets or sets the sku name. Required for account creation; optional for update. Note that in older versions, sku name was called accountType. |  |
|**resourceType** | **String** | The type of the resource, usually it is &#39;storageAccounts&#39;. |  [optional] [readonly] |
|**restrictions** | [**List&lt;Restriction&gt;**](Restriction.md) | The restrictions because of which SKU cannot be used. This is empty if there are no restrictions. |  [optional] |
|**tier** | [**TierEnum**](#TierEnum) | Gets the sku tier. This is based on the SKU name. |  [optional] [readonly] |



## Enum: KindEnum

| Name | Value |
|---- | -----|
| STORAGE | &quot;Storage&quot; |
| STORAGE_V2 | &quot;StorageV2&quot; |
| BLOB_STORAGE | &quot;BlobStorage&quot; |



## Enum: NameEnum

| Name | Value |
|---- | -----|
| STANDARD_LRS | &quot;Standard_LRS&quot; |
| STANDARD_GRS | &quot;Standard_GRS&quot; |
| STANDARD_RAGRS | &quot;Standard_RAGRS&quot; |
| STANDARD_ZRS | &quot;Standard_ZRS&quot; |
| PREMIUM_LRS | &quot;Premium_LRS&quot; |



## Enum: TierEnum

| Name | Value |
|---- | -----|
| STANDARD | &quot;Standard&quot; |
| PREMIUM | &quot;Premium&quot; |



