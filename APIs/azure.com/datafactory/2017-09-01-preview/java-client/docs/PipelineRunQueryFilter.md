

# PipelineRunQueryFilter

Query filter option for listing pipeline runs.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**operand** | [**OperandEnum**](#OperandEnum) | Parameter name to be used for filter. |  |
|**operator** | [**OperatorEnum**](#OperatorEnum) | Operator to be used for filter. |  |
|**values** | **List&lt;String&gt;** | List of filter values. |  |



## Enum: OperandEnum

| Name | Value |
|---- | -----|
| PIPELINE_NAME | &quot;PipelineName&quot; |
| STATUS | &quot;Status&quot; |
| RUN_START | &quot;RunStart&quot; |
| RUN_END | &quot;RunEnd&quot; |



## Enum: OperatorEnum

| Name | Value |
|---- | -----|
| EQUALS | &quot;Equals&quot; |
| NOT_EQUALS | &quot;NotEquals&quot; |
| IN | &quot;In&quot; |
| NOT_IN | &quot;NotIn&quot; |



