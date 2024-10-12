

# Routine

A user-defined function or a stored procedure.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**arguments** | [**List&lt;Argument&gt;**](Argument.md) | Optional. |  [optional] |
|**creationTime** | **String** | Output only. The time when this routine was created, in milliseconds since the epoch. |  [optional] [readonly] |
|**dataGovernanceType** | [**DataGovernanceTypeEnum**](#DataGovernanceTypeEnum) | Optional. If set to &#x60;DATA_MASKING&#x60;, the function is validated and made available as a masking function. For more information, see [Create custom masking routines](https://cloud.google.com/bigquery/docs/user-defined-functions#custom-mask). |  [optional] |
|**definitionBody** | **String** | Required. The body of the routine. For functions, this is the expression in the AS clause. If language&#x3D;SQL, it is the substring inside (but excluding) the parentheses. For example, for the function created with the following statement: &#x60;CREATE FUNCTION JoinLines(x string, y string) as (concat(x, \&quot;\\n\&quot;, y))&#x60; The definition_body is &#x60;concat(x, \&quot;\\n\&quot;, y)&#x60; (\\n is not replaced with linebreak). If language&#x3D;JAVASCRIPT, it is the evaluated string in the AS clause. For example, for the function created with the following statement: &#x60;CREATE FUNCTION f() RETURNS STRING LANGUAGE js AS &#39;return \&quot;\\n\&quot;;\\n&#39;&#x60; The definition_body is &#x60;return \&quot;\\n\&quot;;\\n&#x60; Note that both \\n are replaced with linebreaks. |  [optional] |
|**description** | **String** | Optional. The description of the routine, if defined. |  [optional] |
|**determinismLevel** | [**DeterminismLevelEnum**](#DeterminismLevelEnum) | Optional. The determinism level of the JavaScript UDF, if defined. |  [optional] |
|**etag** | **String** | Output only. A hash of this resource. |  [optional] [readonly] |
|**importedLibraries** | **List&lt;String&gt;** | Optional. If language &#x3D; \&quot;JAVASCRIPT\&quot;, this field stores the path of the imported JAVASCRIPT libraries. |  [optional] |
|**language** | [**LanguageEnum**](#LanguageEnum) | Optional. Defaults to \&quot;SQL\&quot; if remote_function_options field is absent, not set otherwise. |  [optional] |
|**lastModifiedTime** | **String** | Output only. The time when this routine was last modified, in milliseconds since the epoch. |  [optional] [readonly] |
|**remoteFunctionOptions** | [**RemoteFunctionOptions**](RemoteFunctionOptions.md) |  |  [optional] |
|**returnTableType** | [**StandardSqlTableType**](StandardSqlTableType.md) |  |  [optional] |
|**returnType** | [**StandardSqlDataType**](StandardSqlDataType.md) |  |  [optional] |
|**routineReference** | [**RoutineReference**](RoutineReference.md) |  |  [optional] |
|**routineType** | [**RoutineTypeEnum**](#RoutineTypeEnum) | Required. The type of routine. |  [optional] |
|**securityMode** | [**SecurityModeEnum**](#SecurityModeEnum) | Optional. The security mode of the routine, if defined. If not defined, the security mode is automatically determined from the routine&#39;s configuration. |  [optional] |
|**sparkOptions** | [**SparkOptions**](SparkOptions.md) |  |  [optional] |
|**strictMode** | **Boolean** | Optional. Use this option to catch many common errors. Error checking is not exhaustive, and successfully creating a procedure doesn&#39;t guarantee that the procedure will successfully execute at runtime. If &#x60;strictMode&#x60; is set to &#x60;TRUE&#x60;, the procedure body is further checked for errors such as non-existent tables or columns. The &#x60;CREATE PROCEDURE&#x60; statement fails if the body fails any of these checks. If &#x60;strictMode&#x60; is set to &#x60;FALSE&#x60;, the procedure body is checked only for syntax. For procedures that invoke themselves recursively, specify &#x60;strictMode&#x3D;FALSE&#x60; to avoid non-existent procedure errors during validation. Default value is &#x60;TRUE&#x60;. |  [optional] |



## Enum: DataGovernanceTypeEnum

| Name | Value |
|---- | -----|
| GOVERNANCE_TYPE_UNSPECIFIED | &quot;DATA_GOVERNANCE_TYPE_UNSPECIFIED&quot; |
| MASKING | &quot;DATA_MASKING&quot; |



## Enum: DeterminismLevelEnum

| Name | Value |
|---- | -----|
| DETERMINISM_LEVEL_UNSPECIFIED | &quot;DETERMINISM_LEVEL_UNSPECIFIED&quot; |
| DETERMINISTIC | &quot;DETERMINISTIC&quot; |
| NOT_DETERMINISTIC | &quot;NOT_DETERMINISTIC&quot; |



## Enum: LanguageEnum

| Name | Value |
|---- | -----|
| LANGUAGE_UNSPECIFIED | &quot;LANGUAGE_UNSPECIFIED&quot; |
| SQL | &quot;SQL&quot; |
| JAVASCRIPT | &quot;JAVASCRIPT&quot; |
| PYTHON | &quot;PYTHON&quot; |
| JAVA | &quot;JAVA&quot; |
| SCALA | &quot;SCALA&quot; |



## Enum: RoutineTypeEnum

| Name | Value |
|---- | -----|
| ROUTINE_TYPE_UNSPECIFIED | &quot;ROUTINE_TYPE_UNSPECIFIED&quot; |
| SCALAR_FUNCTION | &quot;SCALAR_FUNCTION&quot; |
| PROCEDURE | &quot;PROCEDURE&quot; |
| TABLE_VALUED_FUNCTION | &quot;TABLE_VALUED_FUNCTION&quot; |
| AGGREGATE_FUNCTION | &quot;AGGREGATE_FUNCTION&quot; |



## Enum: SecurityModeEnum

| Name | Value |
|---- | -----|
| SECURITY_MODE_UNSPECIFIED | &quot;SECURITY_MODE_UNSPECIFIED&quot; |
| DEFINER | &quot;DEFINER&quot; |
| INVOKER | &quot;INVOKER&quot; |



