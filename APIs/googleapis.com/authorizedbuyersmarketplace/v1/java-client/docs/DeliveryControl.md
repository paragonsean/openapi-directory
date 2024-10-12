

# DeliveryControl

Message contains details about how the deal will be paced.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**companionDeliveryType** | [**CompanionDeliveryTypeEnum**](#CompanionDeliveryTypeEnum) | Output only. Specifies roadblocking in a main companion lineitem. |  [optional] [readonly] |
|**creativeRotationType** | [**CreativeRotationTypeEnum**](#CreativeRotationTypeEnum) | Output only. Specifies strategy to use for selecting a creative when multiple creatives of the same size are available. |  [optional] [readonly] |
|**deliveryRateType** | [**DeliveryRateTypeEnum**](#DeliveryRateTypeEnum) | Output only. Specifies how the impression delivery will be paced. |  [optional] [readonly] |
|**frequencyCap** | [**List&lt;FrequencyCap&gt;**](FrequencyCap.md) | Output only. Specifies any frequency caps. Cannot be filtered within ListDealsRequest. |  [optional] [readonly] |
|**roadblockingType** | [**RoadblockingTypeEnum**](#RoadblockingTypeEnum) | Output only. Specifies the roadblocking type in display creatives. |  [optional] [readonly] |



## Enum: CompanionDeliveryTypeEnum

| Name | Value |
|---- | -----|
| COMPANION_DELIVERY_TYPE_UNSPECIFIED | &quot;COMPANION_DELIVERY_TYPE_UNSPECIFIED&quot; |
| DELIVERY_OPTIONAL | &quot;DELIVERY_OPTIONAL&quot; |
| DELIVERY_AT_LEAST_ONE | &quot;DELIVERY_AT_LEAST_ONE&quot; |
| DELIVERY_ALL | &quot;DELIVERY_ALL&quot; |



## Enum: CreativeRotationTypeEnum

| Name | Value |
|---- | -----|
| CREATIVE_ROTATION_TYPE_UNSPECIFIED | &quot;CREATIVE_ROTATION_TYPE_UNSPECIFIED&quot; |
| ROTATION_EVEN | &quot;ROTATION_EVEN&quot; |
| ROTATION_OPTIMIZED | &quot;ROTATION_OPTIMIZED&quot; |
| ROTATION_MANUAL | &quot;ROTATION_MANUAL&quot; |
| ROTATION_SEQUENTIAL | &quot;ROTATION_SEQUENTIAL&quot; |



## Enum: DeliveryRateTypeEnum

| Name | Value |
|---- | -----|
| DELIVERY_RATE_TYPE_UNSPECIFIED | &quot;DELIVERY_RATE_TYPE_UNSPECIFIED&quot; |
| EVENLY | &quot;EVENLY&quot; |
| FRONT_LOADED | &quot;FRONT_LOADED&quot; |
| AS_FAST_AS_POSSIBLE | &quot;AS_FAST_AS_POSSIBLE&quot; |



## Enum: RoadblockingTypeEnum

| Name | Value |
|---- | -----|
| ROADBLOCKING_TYPE_UNSPECIFIED | &quot;ROADBLOCKING_TYPE_UNSPECIFIED&quot; |
| ONLY_ONE | &quot;ONLY_ONE&quot; |
| ONE_OR_MORE | &quot;ONE_OR_MORE&quot; |
| AS_MANY_AS_POSSIBLE | &quot;AS_MANY_AS_POSSIBLE&quot; |
| ALL_ROADBLOCK | &quot;ALL_ROADBLOCK&quot; |
| CREATIVE_SET | &quot;CREATIVE_SET&quot; |



