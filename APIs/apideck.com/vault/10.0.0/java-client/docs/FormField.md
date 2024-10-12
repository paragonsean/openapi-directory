

# FormField


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**allowCustomValues** | **Boolean** | Only applicable to select fields. Allow the user to add a custom value though the option select if the desired value is not in the option select list. |  [optional] |
|**customField** | **Boolean** |  |  [optional] |
|**description** | **String** | The description of the form field |  [optional] |
|**disabled** | **Boolean** | Indicates if the form field is displayed in a “read-only” mode. |  [optional] |
|**hidden** | **Boolean** | Indicates if the form field is not displayed but the value that is being stored on the connection. |  [optional] |
|**id** | **String** | The unique identifier of the form field. |  [optional] |
|**label** | **String** | The label of the field |  [optional] |
|**options** | [**List&lt;FormFieldOption&gt;**](FormFieldOption.md) |  |  [optional] |
|**placeholder** | **String** | The placeholder for the form field |  [optional] |
|**prefix** | **String** | Prefix to display in front of the form field. |  [optional] |
|**required** | **Boolean** | Indicates if the form field is required, which means it must be filled in before the form can be submitted |  [optional] |
|**sensitive** | **Boolean** | Indicates if the form field contains sensitive data, which will display the value as a masked input. |  [optional] |
|**suffix** | **String** | Suffix to display next to the form field. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) |  |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| TEXT | &quot;text&quot; |
| CHECKBOX | &quot;checkbox&quot; |
| TEL | &quot;tel&quot; |
| EMAIL | &quot;email&quot; |
| URL | &quot;url&quot; |
| TEXTAREA | &quot;textarea&quot; |
| SELECT | &quot;select&quot; |
| FILTERED_SELECT | &quot;filtered-select&quot; |
| MULTI_SELECT | &quot;multi-select&quot; |
| DATETIME | &quot;datetime&quot; |
| DATE | &quot;date&quot; |
| TIME | &quot;time&quot; |
| NUMBER | &quot;number&quot; |



