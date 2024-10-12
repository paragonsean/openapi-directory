# BigQueryApi.ScriptOptions

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**keyResultStatement** | **String** | Determines which statement in the script represents the \&quot;key result\&quot;, used to populate the schema and query results of the script job. Default is LAST. | [optional] 
**statementByteBudget** | **String** | Limit on the number of bytes billed per statement. Exceeding this budget results in an error. | [optional] 
**statementTimeoutMs** | **String** | Timeout period for each statement in a script. | [optional] 



## Enum: KeyResultStatementEnum


* `KEY_RESULT_STATEMENT_KIND_UNSPECIFIED` (value: `"KEY_RESULT_STATEMENT_KIND_UNSPECIFIED"`)

* `LAST` (value: `"LAST"`)

* `FIRST_SELECT` (value: `"FIRST_SELECT"`)




