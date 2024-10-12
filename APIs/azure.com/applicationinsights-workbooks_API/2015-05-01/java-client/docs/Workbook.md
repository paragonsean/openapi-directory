

# Workbook

An Application Insights workbook definition.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**kind** | [**KindEnum**](#KindEnum) | The kind of workbook. Choices are user and shared. |  [optional] |
|**properties** | [**WorkbookProperties**](WorkbookProperties.md) |  |  [optional] |
|**id** | **String** | Azure resource Id |  [optional] [readonly] |
|**location** | **String** | Resource location |  [optional] |
|**name** | **String** | Azure resource name |  [optional] [readonly] |
|**tags** | **Object** | Resource tags |  [optional] |
|**type** | **String** | Azure resource type |  [optional] [readonly] |



## Enum: KindEnum

| Name | Value |
|---- | -----|
| USER | &quot;user&quot; |
| SHARED | &quot;shared&quot; |



