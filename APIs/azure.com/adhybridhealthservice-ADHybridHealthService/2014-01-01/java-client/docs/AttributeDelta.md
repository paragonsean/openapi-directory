

# AttributeDelta

The delta attributes.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**multiValued** | **Boolean** | Indicates if the attribute delta is multivalued or not. |  [optional] |
|**name** | **String** | The name of the attribute delta. |  [optional] |
|**operationType** | [**OperationTypeEnum**](#OperationTypeEnum) | The attribute delta operation type. |  [optional] |
|**valueType** | [**ValueTypeEnum**](#ValueTypeEnum) | The value type. |  [optional] |
|**values** | [**List&lt;ValueDelta&gt;**](ValueDelta.md) | The delta values. |  [optional] |



## Enum: OperationTypeEnum

| Name | Value |
|---- | -----|
| UNDEFINED | &quot;Undefined&quot; |
| ADD | &quot;Add&quot; |
| REPLACE | &quot;Replace&quot; |
| UPDATE | &quot;Update&quot; |
| DELETE | &quot;Delete&quot; |



## Enum: ValueTypeEnum

| Name | Value |
|---- | -----|
| UNDEFINED | &quot;Undefined&quot; |
| DN | &quot;Dn&quot; |
| BINARY | &quot;Binary&quot; |
| STRING | &quot;String&quot; |
| INTEGER | &quot;Integer&quot; |
| BOOLEAN | &quot;Boolean&quot; |



