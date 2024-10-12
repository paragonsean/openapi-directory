

# DeliveryControl

Message contains details about how the deals will be paced.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**creativeBlockingLevel** | [**CreativeBlockingLevelEnum**](#CreativeBlockingLevelEnum) | Output only. Specified the creative blocking levels to be applied. |  [optional] [readonly] |
|**deliveryRateType** | [**DeliveryRateTypeEnum**](#DeliveryRateTypeEnum) | Output only. Specifies how the impression delivery will be paced. |  [optional] [readonly] |
|**frequencyCaps** | [**List&lt;FrequencyCap&gt;**](FrequencyCap.md) | Output only. Specifies any frequency caps. |  [optional] [readonly] |



## Enum: CreativeBlockingLevelEnum

| Name | Value |
|---- | -----|
| CREATIVE_BLOCKING_LEVEL_UNSPECIFIED | &quot;CREATIVE_BLOCKING_LEVEL_UNSPECIFIED&quot; |
| PUBLISHER_BLOCKING_RULES | &quot;PUBLISHER_BLOCKING_RULES&quot; |
| ADX_POLICY_BLOCKING_ONLY | &quot;ADX_POLICY_BLOCKING_ONLY&quot; |



## Enum: DeliveryRateTypeEnum

| Name | Value |
|---- | -----|
| DELIVERY_RATE_TYPE_UNSPECIFIED | &quot;DELIVERY_RATE_TYPE_UNSPECIFIED&quot; |
| EVENLY | &quot;EVENLY&quot; |
| FRONT_LOADED | &quot;FRONT_LOADED&quot; |
| AS_FAST_AS_POSSIBLE | &quot;AS_FAST_AS_POSSIBLE&quot; |



