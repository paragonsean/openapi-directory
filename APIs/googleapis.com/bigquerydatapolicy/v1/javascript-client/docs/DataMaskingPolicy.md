# BigQueryDataPolicyApi.DataMaskingPolicy

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**predefinedExpression** | **String** | A predefined masking expression. | [optional] 
**routine** | **String** | The name of the BigQuery routine that contains the custom masking routine, in the format of &#x60;projects/{project_number}/datasets/{dataset_id}/routines/{routine_id}&#x60;. | [optional] 



## Enum: PredefinedExpressionEnum


* `PREDEFINED_EXPRESSION_UNSPECIFIED` (value: `"PREDEFINED_EXPRESSION_UNSPECIFIED"`)

* `SHA256` (value: `"SHA256"`)

* `ALWAYS_NULL` (value: `"ALWAYS_NULL"`)

* `DEFAULT_MASKING_VALUE` (value: `"DEFAULT_MASKING_VALUE"`)

* `LAST_FOUR_CHARACTERS` (value: `"LAST_FOUR_CHARACTERS"`)

* `FIRST_FOUR_CHARACTERS` (value: `"FIRST_FOUR_CHARACTERS"`)

* `EMAIL_MASK` (value: `"EMAIL_MASK"`)

* `DATE_YEAR_MASK` (value: `"DATE_YEAR_MASK"`)




