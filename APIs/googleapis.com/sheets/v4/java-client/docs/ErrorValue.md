

# ErrorValue

An error in a cell.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**message** | **String** | A message with more information about the error (in the spreadsheet&#39;s locale). |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | The type of error. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| ERROR_TYPE_UNSPECIFIED | &quot;ERROR_TYPE_UNSPECIFIED&quot; |
| ERROR | &quot;ERROR&quot; |
| NULL_VALUE | &quot;NULL_VALUE&quot; |
| DIVIDE_BY_ZERO | &quot;DIVIDE_BY_ZERO&quot; |
| VALUE | &quot;VALUE&quot; |
| REF | &quot;REF&quot; |
| NAME | &quot;NAME&quot; |
| NUM | &quot;NUM&quot; |
| N_A | &quot;N_A&quot; |
| LOADING | &quot;LOADING&quot; |



