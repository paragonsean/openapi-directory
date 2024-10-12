

# DataMaskingPolicy

The data masking policy that is used to specify data masking rule.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**predefinedExpression** | [**PredefinedExpressionEnum**](#PredefinedExpressionEnum) | A predefined masking expression. |  [optional] |
|**routine** | **String** | The name of the BigQuery routine that contains the custom masking routine, in the format of &#x60;projects/{project_number}/datasets/{dataset_id}/routines/{routine_id}&#x60;. |  [optional] |



## Enum: PredefinedExpressionEnum

| Name | Value |
|---- | -----|
| PREDEFINED_EXPRESSION_UNSPECIFIED | &quot;PREDEFINED_EXPRESSION_UNSPECIFIED&quot; |
| SHA256 | &quot;SHA256&quot; |
| ALWAYS_NULL | &quot;ALWAYS_NULL&quot; |
| DEFAULT_MASKING_VALUE | &quot;DEFAULT_MASKING_VALUE&quot; |
| LAST_FOUR_CHARACTERS | &quot;LAST_FOUR_CHARACTERS&quot; |
| FIRST_FOUR_CHARACTERS | &quot;FIRST_FOUR_CHARACTERS&quot; |
| EMAIL_MASK | &quot;EMAIL_MASK&quot; |
| DATE_YEAR_MASK | &quot;DATE_YEAR_MASK&quot; |



