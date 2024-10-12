

# ReportData

A key-value element that will be displayed along with the report.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**title** | **String** | A string describing what this data field represents. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | The type of data contained in the value field. If not provided, then the value will be detected as a boolean, number or string. |  [optional] |
|**value** | **Object** | The value of the data element. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| BOOLEAN | &quot;BOOLEAN&quot; |
| DATE | &quot;DATE&quot; |
| DURATION | &quot;DURATION&quot; |
| LINK | &quot;LINK&quot; |
| NUMBER | &quot;NUMBER&quot; |
| PERCENTAGE | &quot;PERCENTAGE&quot; |
| TEXT | &quot;TEXT&quot; |



