

# ScriptOptions

Options related to script execution.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**keyResultStatement** | [**KeyResultStatementEnum**](#KeyResultStatementEnum) | Determines which statement in the script represents the \&quot;key result\&quot;, used to populate the schema and query results of the script job. Default is LAST. |  [optional] |
|**statementByteBudget** | **String** | Limit on the number of bytes billed per statement. Exceeding this budget results in an error. |  [optional] |
|**statementTimeoutMs** | **String** | Timeout period for each statement in a script. |  [optional] |



## Enum: KeyResultStatementEnum

| Name | Value |
|---- | -----|
| KEY_RESULT_STATEMENT_KIND_UNSPECIFIED | &quot;KEY_RESULT_STATEMENT_KIND_UNSPECIFIED&quot; |
| LAST | &quot;LAST&quot; |
| FIRST_SELECT | &quot;FIRST_SELECT&quot; |



