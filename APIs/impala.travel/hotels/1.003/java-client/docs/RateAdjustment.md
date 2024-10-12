

# RateAdjustment


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**adjustmentId** | **UUID** | Unique identifier of this rate adjustment. |  [optional] |
|**amount** | **BigDecimal** | The percentage discount between 0 and 100. |  |
|**conditions** | [**Set&lt;AdjustmentConditionLengthOfStayRule&gt;**](AdjustmentConditionLengthOfStayRule.md) | A list of conditions for the adjustment to apply. |  |
|**type** | [**TypeEnum**](#TypeEnum) | The adjustment type. |  |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| PERCENTAGE | &quot;PERCENTAGE&quot; |



