

# ChangeNotReimportedDelta

The delta in a change that is not re-imported.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**anchor** | **String** | The anchor. |  [optional] |
|**attributes** | [**List&lt;AttributeDelta&gt;**](AttributeDelta.md) | The attributes. |  [optional] |
|**dnAttributes** | [**List&lt;AttributeDelta&gt;**](AttributeDelta.md) | The delta attributes for distinguished names. |  [optional] |
|**operationType** | [**OperationTypeEnum**](#OperationTypeEnum) | The operation type. |  [optional] |



## Enum: OperationTypeEnum

| Name | Value |
|---- | -----|
| UNDEFINED | &quot;Undefined&quot; |
| NONE | &quot;None&quot; |
| ADD | &quot;Add&quot; |
| REPLACE | &quot;Replace&quot; |
| UPDATE | &quot;Update&quot; |
| DELETE | &quot;Delete&quot; |
| OBSOLETE | &quot;Obsolete&quot; |
| DELETE_ADD | &quot;DeleteAdd&quot; |



