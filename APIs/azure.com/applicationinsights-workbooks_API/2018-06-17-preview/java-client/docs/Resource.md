

# Resource

An azure resource object

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | Azure resource Id |  [optional] [readonly] |
|**kind** | [**KindEnum**](#KindEnum) | The kind of workbook. Choices are user and shared. |  [optional] |
|**location** | **String** | Resource location |  |
|**name** | **String** | Azure resource name. This is GUID value. The display name should be assigned within properties field. |  [optional] [readonly] |
|**tags** | **Map&lt;String, String&gt;** | Resource tags |  [optional] |
|**type** | **String** | Azure resource type |  [optional] [readonly] |



## Enum: KindEnum

| Name | Value |
|---- | -----|
| USER | &quot;user&quot; |
| SHARED | &quot;shared&quot; |



