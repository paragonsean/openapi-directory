# GoogleCloudDataCatalogApi.GoogleCloudDatacatalogV1RoutineSpec

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bigqueryRoutineSpec** | [**GoogleCloudDatacatalogV1BigQueryRoutineSpec**](GoogleCloudDatacatalogV1BigQueryRoutineSpec.md) |  | [optional] 
**definitionBody** | **String** | The body of the routine. | [optional] 
**language** | **String** | The language the routine is written in. The exact value depends on the source system. For BigQuery routines, possible values are: * &#x60;SQL&#x60; * &#x60;JAVASCRIPT&#x60; | [optional] 
**returnType** | **String** | Return type of the argument. The exact value depends on the source system and the language. | [optional] 
**routineArguments** | [**[GoogleCloudDatacatalogV1RoutineSpecArgument]**](GoogleCloudDatacatalogV1RoutineSpecArgument.md) | Arguments of the routine. | [optional] 
**routineType** | **String** | The type of the routine. | [optional] 



## Enum: RoutineTypeEnum


* `ROUTINE_TYPE_UNSPECIFIED` (value: `"ROUTINE_TYPE_UNSPECIFIED"`)

* `SCALAR_FUNCTION` (value: `"SCALAR_FUNCTION"`)

* `PROCEDURE` (value: `"PROCEDURE"`)




