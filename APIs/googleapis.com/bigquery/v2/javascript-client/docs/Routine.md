# BigQueryApi.Routine

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**_arguments** | [**[Argument]**](Argument.md) | Optional. | [optional] 
**creationTime** | **String** | Output only. The time when this routine was created, in milliseconds since the epoch. | [optional] [readonly] 
**dataGovernanceType** | **String** | Optional. If set to &#x60;DATA_MASKING&#x60;, the function is validated and made available as a masking function. For more information, see [Create custom masking routines](https://cloud.google.com/bigquery/docs/user-defined-functions#custom-mask). | [optional] 
**definitionBody** | **String** | Required. The body of the routine. For functions, this is the expression in the AS clause. If language&#x3D;SQL, it is the substring inside (but excluding) the parentheses. For example, for the function created with the following statement: &#x60;CREATE FUNCTION JoinLines(x string, y string) as (concat(x, \&quot;\\n\&quot;, y))&#x60; The definition_body is &#x60;concat(x, \&quot;\\n\&quot;, y)&#x60; (\\n is not replaced with linebreak). If language&#x3D;JAVASCRIPT, it is the evaluated string in the AS clause. For example, for the function created with the following statement: &#x60;CREATE FUNCTION f() RETURNS STRING LANGUAGE js AS &#39;return \&quot;\\n\&quot;;\\n&#39;&#x60; The definition_body is &#x60;return \&quot;\\n\&quot;;\\n&#x60; Note that both \\n are replaced with linebreaks. | [optional] 
**description** | **String** | Optional. The description of the routine, if defined. | [optional] 
**determinismLevel** | **String** | Optional. The determinism level of the JavaScript UDF, if defined. | [optional] 
**etag** | **String** | Output only. A hash of this resource. | [optional] [readonly] 
**importedLibraries** | **[String]** | Optional. If language &#x3D; \&quot;JAVASCRIPT\&quot;, this field stores the path of the imported JAVASCRIPT libraries. | [optional] 
**language** | **String** | Optional. Defaults to \&quot;SQL\&quot; if remote_function_options field is absent, not set otherwise. | [optional] 
**lastModifiedTime** | **String** | Output only. The time when this routine was last modified, in milliseconds since the epoch. | [optional] [readonly] 
**remoteFunctionOptions** | [**RemoteFunctionOptions**](RemoteFunctionOptions.md) |  | [optional] 
**returnTableType** | [**StandardSqlTableType**](StandardSqlTableType.md) |  | [optional] 
**returnType** | [**StandardSqlDataType**](StandardSqlDataType.md) |  | [optional] 
**routineReference** | [**RoutineReference**](RoutineReference.md) |  | [optional] 
**routineType** | **String** | Required. The type of routine. | [optional] 
**securityMode** | **String** | Optional. The security mode of the routine, if defined. If not defined, the security mode is automatically determined from the routine&#39;s configuration. | [optional] 
**sparkOptions** | [**SparkOptions**](SparkOptions.md) |  | [optional] 
**strictMode** | **Boolean** | Optional. Use this option to catch many common errors. Error checking is not exhaustive, and successfully creating a procedure doesn&#39;t guarantee that the procedure will successfully execute at runtime. If &#x60;strictMode&#x60; is set to &#x60;TRUE&#x60;, the procedure body is further checked for errors such as non-existent tables or columns. The &#x60;CREATE PROCEDURE&#x60; statement fails if the body fails any of these checks. If &#x60;strictMode&#x60; is set to &#x60;FALSE&#x60;, the procedure body is checked only for syntax. For procedures that invoke themselves recursively, specify &#x60;strictMode&#x3D;FALSE&#x60; to avoid non-existent procedure errors during validation. Default value is &#x60;TRUE&#x60;. | [optional] 



## Enum: DataGovernanceTypeEnum


* `GOVERNANCE_TYPE_UNSPECIFIED` (value: `"DATA_GOVERNANCE_TYPE_UNSPECIFIED"`)

* `MASKING` (value: `"DATA_MASKING"`)





## Enum: DeterminismLevelEnum


* `DETERMINISM_LEVEL_UNSPECIFIED` (value: `"DETERMINISM_LEVEL_UNSPECIFIED"`)

* `DETERMINISTIC` (value: `"DETERMINISTIC"`)

* `NOT_DETERMINISTIC` (value: `"NOT_DETERMINISTIC"`)





## Enum: LanguageEnum


* `LANGUAGE_UNSPECIFIED` (value: `"LANGUAGE_UNSPECIFIED"`)

* `SQL` (value: `"SQL"`)

* `JAVASCRIPT` (value: `"JAVASCRIPT"`)

* `PYTHON` (value: `"PYTHON"`)

* `JAVA` (value: `"JAVA"`)

* `SCALA` (value: `"SCALA"`)





## Enum: RoutineTypeEnum


* `ROUTINE_TYPE_UNSPECIFIED` (value: `"ROUTINE_TYPE_UNSPECIFIED"`)

* `SCALAR_FUNCTION` (value: `"SCALAR_FUNCTION"`)

* `PROCEDURE` (value: `"PROCEDURE"`)

* `TABLE_VALUED_FUNCTION` (value: `"TABLE_VALUED_FUNCTION"`)

* `AGGREGATE_FUNCTION` (value: `"AGGREGATE_FUNCTION"`)





## Enum: SecurityModeEnum


* `SECURITY_MODE_UNSPECIFIED` (value: `"SECURITY_MODE_UNSPECIFIED"`)

* `DEFINER` (value: `"DEFINER"`)

* `INVOKER` (value: `"INVOKER"`)




