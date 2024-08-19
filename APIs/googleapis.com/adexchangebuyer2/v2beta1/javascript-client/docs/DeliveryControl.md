# AdExchangeBuyerApiIi.DeliveryControl

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**creativeBlockingLevel** | **String** | Output only. Specified the creative blocking levels to be applied. | [optional] [readonly] 
**deliveryRateType** | **String** | Output only. Specifies how the impression delivery will be paced. | [optional] [readonly] 
**frequencyCaps** | [**[FrequencyCap]**](FrequencyCap.md) | Output only. Specifies any frequency caps. | [optional] [readonly] 



## Enum: CreativeBlockingLevelEnum


* `CREATIVE_BLOCKING_LEVEL_UNSPECIFIED` (value: `"CREATIVE_BLOCKING_LEVEL_UNSPECIFIED"`)

* `PUBLISHER_BLOCKING_RULES` (value: `"PUBLISHER_BLOCKING_RULES"`)

* `ADX_POLICY_BLOCKING_ONLY` (value: `"ADX_POLICY_BLOCKING_ONLY"`)





## Enum: DeliveryRateTypeEnum


* `DELIVERY_RATE_TYPE_UNSPECIFIED` (value: `"DELIVERY_RATE_TYPE_UNSPECIFIED"`)

* `EVENLY` (value: `"EVENLY"`)

* `FRONT_LOADED` (value: `"FRONT_LOADED"`)

* `AS_FAST_AS_POSSIBLE` (value: `"AS_FAST_AS_POSSIBLE"`)




