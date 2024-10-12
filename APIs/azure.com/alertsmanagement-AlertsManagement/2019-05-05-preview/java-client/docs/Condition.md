

# Condition

condition to trigger an action rule

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**operator** | [**OperatorEnum**](#OperatorEnum) | operator for a given condition |  [optional] |
|**values** | **List&lt;String&gt;** | list of values to match for a given condition. |  [optional] |



## Enum: OperatorEnum

| Name | Value |
|---- | -----|
| EQUALS | &quot;Equals&quot; |
| NOT_EQUALS | &quot;NotEquals&quot; |
| CONTAINS | &quot;Contains&quot; |
| DOES_NOT_CONTAIN | &quot;DoesNotContain&quot; |



