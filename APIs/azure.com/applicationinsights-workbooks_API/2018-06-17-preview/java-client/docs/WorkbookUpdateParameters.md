

# WorkbookUpdateParameters

The parameters that can be provided when updating workbook properties properties.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**kind** | [**KindEnum**](#KindEnum) | The kind of workbook. Choices are user and shared. |  [optional] |
|**properties** | [**WorkbookPropertiesUpdateParameters**](WorkbookPropertiesUpdateParameters.md) |  |  [optional] |
|**tags** | **Map&lt;String, String&gt;** | Resource tags |  [optional] |



## Enum: KindEnum

| Name | Value |
|---- | -----|
| USER | &quot;user&quot; |
| SHARED | &quot;shared&quot; |



