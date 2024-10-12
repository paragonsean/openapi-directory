# BigQueryApi.Argument

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**argumentKind** | **String** | Optional. Defaults to FIXED_TYPE. | [optional] 
**dataType** | [**StandardSqlDataType**](StandardSqlDataType.md) |  | [optional] 
**isAggregate** | **Boolean** | Optional. Whether the argument is an aggregate function parameter. Must be Unset for routine types other than AGGREGATE_FUNCTION. For AGGREGATE_FUNCTION, if set to false, it is equivalent to adding \&quot;NOT AGGREGATE\&quot; clause in DDL; Otherwise, it is equivalent to omitting \&quot;NOT AGGREGATE\&quot; clause in DDL. | [optional] 
**mode** | **String** | Optional. Specifies whether the argument is input or output. Can be set for procedures only. | [optional] 
**name** | **String** | Optional. The name of this argument. Can be absent for function return argument. | [optional] 



## Enum: ArgumentKindEnum


* `ARGUMENT_KIND_UNSPECIFIED` (value: `"ARGUMENT_KIND_UNSPECIFIED"`)

* `FIXED_TYPE` (value: `"FIXED_TYPE"`)

* `ANY_TYPE` (value: `"ANY_TYPE"`)





## Enum: ModeEnum


* `MODE_UNSPECIFIED` (value: `"MODE_UNSPECIFIED"`)

* `IN` (value: `"IN"`)

* `OUT` (value: `"OUT"`)

* `INOUT` (value: `"INOUT"`)




