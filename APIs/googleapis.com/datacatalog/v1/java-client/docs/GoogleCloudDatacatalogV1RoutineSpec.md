

# GoogleCloudDatacatalogV1RoutineSpec

Specification that applies to a routine. Valid only for entries with the `ROUTINE` type.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**bigqueryRoutineSpec** | [**GoogleCloudDatacatalogV1BigQueryRoutineSpec**](GoogleCloudDatacatalogV1BigQueryRoutineSpec.md) |  |  [optional] |
|**definitionBody** | **String** | The body of the routine. |  [optional] |
|**language** | **String** | The language the routine is written in. The exact value depends on the source system. For BigQuery routines, possible values are: * &#x60;SQL&#x60; * &#x60;JAVASCRIPT&#x60; |  [optional] |
|**returnType** | **String** | Return type of the argument. The exact value depends on the source system and the language. |  [optional] |
|**routineArguments** | [**List&lt;GoogleCloudDatacatalogV1RoutineSpecArgument&gt;**](GoogleCloudDatacatalogV1RoutineSpecArgument.md) | Arguments of the routine. |  [optional] |
|**routineType** | [**RoutineTypeEnum**](#RoutineTypeEnum) | The type of the routine. |  [optional] |



## Enum: RoutineTypeEnum

| Name | Value |
|---- | -----|
| ROUTINE_TYPE_UNSPECIFIED | &quot;ROUTINE_TYPE_UNSPECIFIED&quot; |
| SCALAR_FUNCTION | &quot;SCALAR_FUNCTION&quot; |
| PROCEDURE | &quot;PROCEDURE&quot; |



