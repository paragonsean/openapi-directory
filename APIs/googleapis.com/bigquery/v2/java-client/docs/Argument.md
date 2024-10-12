

# Argument

Input/output argument of a function or a stored procedure.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**argumentKind** | [**ArgumentKindEnum**](#ArgumentKindEnum) | Optional. Defaults to FIXED_TYPE. |  [optional] |
|**dataType** | [**StandardSqlDataType**](StandardSqlDataType.md) |  |  [optional] |
|**isAggregate** | **Boolean** | Optional. Whether the argument is an aggregate function parameter. Must be Unset for routine types other than AGGREGATE_FUNCTION. For AGGREGATE_FUNCTION, if set to false, it is equivalent to adding \&quot;NOT AGGREGATE\&quot; clause in DDL; Otherwise, it is equivalent to omitting \&quot;NOT AGGREGATE\&quot; clause in DDL. |  [optional] |
|**mode** | [**ModeEnum**](#ModeEnum) | Optional. Specifies whether the argument is input or output. Can be set for procedures only. |  [optional] |
|**name** | **String** | Optional. The name of this argument. Can be absent for function return argument. |  [optional] |



## Enum: ArgumentKindEnum

| Name | Value |
|---- | -----|
| ARGUMENT_KIND_UNSPECIFIED | &quot;ARGUMENT_KIND_UNSPECIFIED&quot; |
| FIXED_TYPE | &quot;FIXED_TYPE&quot; |
| ANY_TYPE | &quot;ANY_TYPE&quot; |



## Enum: ModeEnum

| Name | Value |
|---- | -----|
| MODE_UNSPECIFIED | &quot;MODE_UNSPECIFIED&quot; |
| IN | &quot;IN&quot; |
| OUT | &quot;OUT&quot; |
| INOUT | &quot;INOUT&quot; |



