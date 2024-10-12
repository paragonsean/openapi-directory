# CloudAssetApi.Item

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**availablePackage** | [**SoftwarePackage**](SoftwarePackage.md) |  | [optional] 
**createTime** | **String** | When this inventory item was first detected. | [optional] 
**id** | **String** | Identifier for this item, unique across items for this VM. | [optional] 
**installedPackage** | [**SoftwarePackage**](SoftwarePackage.md) |  | [optional] 
**originType** | **String** | The origin of this inventory item. | [optional] 
**type** | **String** | The specific type of inventory, correlating to its specific details. | [optional] 
**updateTime** | **String** | When this inventory item was last modified. | [optional] 



## Enum: OriginTypeEnum


* `ORIGIN_TYPE_UNSPECIFIED` (value: `"ORIGIN_TYPE_UNSPECIFIED"`)

* `INVENTORY_REPORT` (value: `"INVENTORY_REPORT"`)





## Enum: TypeEnum


* `TYPE_UNSPECIFIED` (value: `"TYPE_UNSPECIFIED"`)

* `INSTALLED_PACKAGE` (value: `"INSTALLED_PACKAGE"`)

* `AVAILABLE_PACKAGE` (value: `"AVAILABLE_PACKAGE"`)




