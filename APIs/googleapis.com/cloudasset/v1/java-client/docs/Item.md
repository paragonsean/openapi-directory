

# Item

A single piece of inventory on a VM.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**availablePackage** | [**SoftwarePackage**](SoftwarePackage.md) |  |  [optional] |
|**createTime** | **String** | When this inventory item was first detected. |  [optional] |
|**id** | **String** | Identifier for this item, unique across items for this VM. |  [optional] |
|**installedPackage** | [**SoftwarePackage**](SoftwarePackage.md) |  |  [optional] |
|**originType** | [**OriginTypeEnum**](#OriginTypeEnum) | The origin of this inventory item. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | The specific type of inventory, correlating to its specific details. |  [optional] |
|**updateTime** | **String** | When this inventory item was last modified. |  [optional] |



## Enum: OriginTypeEnum

| Name | Value |
|---- | -----|
| ORIGIN_TYPE_UNSPECIFIED | &quot;ORIGIN_TYPE_UNSPECIFIED&quot; |
| INVENTORY_REPORT | &quot;INVENTORY_REPORT&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| TYPE_UNSPECIFIED | &quot;TYPE_UNSPECIFIED&quot; |
| INSTALLED_PACKAGE | &quot;INSTALLED_PACKAGE&quot; |
| AVAILABLE_PACKAGE | &quot;AVAILABLE_PACKAGE&quot; |



