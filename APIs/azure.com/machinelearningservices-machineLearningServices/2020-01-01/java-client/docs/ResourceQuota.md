

# ResourceQuota

The quota assigned to a resource.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | Specifies the resource ID. |  [optional] [readonly] |
|**limit** | **Long** | The maximum permitted quota of the resource. |  [optional] [readonly] |
|**name** | [**ResourceName**](ResourceName.md) |  |  [optional] |
|**type** | **String** | Specifies the resource type. |  [optional] [readonly] |
|**unit** | [**UnitEnum**](#UnitEnum) | An enum describing the unit of quota measurement. |  [optional] [readonly] |



## Enum: UnitEnum

| Name | Value |
|---- | -----|
| COUNT | &quot;Count&quot; |



