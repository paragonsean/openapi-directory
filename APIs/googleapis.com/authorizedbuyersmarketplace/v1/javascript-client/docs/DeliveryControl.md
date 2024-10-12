# AuthorizedBuyersMarketplaceApi.DeliveryControl

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**companionDeliveryType** | **String** | Output only. Specifies roadblocking in a main companion lineitem. | [optional] [readonly] 
**creativeRotationType** | **String** | Output only. Specifies strategy to use for selecting a creative when multiple creatives of the same size are available. | [optional] [readonly] 
**deliveryRateType** | **String** | Output only. Specifies how the impression delivery will be paced. | [optional] [readonly] 
**frequencyCap** | [**[FrequencyCap]**](FrequencyCap.md) | Output only. Specifies any frequency caps. Cannot be filtered within ListDealsRequest. | [optional] [readonly] 
**roadblockingType** | **String** | Output only. Specifies the roadblocking type in display creatives. | [optional] [readonly] 



## Enum: CompanionDeliveryTypeEnum


* `COMPANION_DELIVERY_TYPE_UNSPECIFIED` (value: `"COMPANION_DELIVERY_TYPE_UNSPECIFIED"`)

* `DELIVERY_OPTIONAL` (value: `"DELIVERY_OPTIONAL"`)

* `DELIVERY_AT_LEAST_ONE` (value: `"DELIVERY_AT_LEAST_ONE"`)

* `DELIVERY_ALL` (value: `"DELIVERY_ALL"`)





## Enum: CreativeRotationTypeEnum


* `CREATIVE_ROTATION_TYPE_UNSPECIFIED` (value: `"CREATIVE_ROTATION_TYPE_UNSPECIFIED"`)

* `ROTATION_EVEN` (value: `"ROTATION_EVEN"`)

* `ROTATION_OPTIMIZED` (value: `"ROTATION_OPTIMIZED"`)

* `ROTATION_MANUAL` (value: `"ROTATION_MANUAL"`)

* `ROTATION_SEQUENTIAL` (value: `"ROTATION_SEQUENTIAL"`)





## Enum: DeliveryRateTypeEnum


* `DELIVERY_RATE_TYPE_UNSPECIFIED` (value: `"DELIVERY_RATE_TYPE_UNSPECIFIED"`)

* `EVENLY` (value: `"EVENLY"`)

* `FRONT_LOADED` (value: `"FRONT_LOADED"`)

* `AS_FAST_AS_POSSIBLE` (value: `"AS_FAST_AS_POSSIBLE"`)





## Enum: RoadblockingTypeEnum


* `ROADBLOCKING_TYPE_UNSPECIFIED` (value: `"ROADBLOCKING_TYPE_UNSPECIFIED"`)

* `ONLY_ONE` (value: `"ONLY_ONE"`)

* `ONE_OR_MORE` (value: `"ONE_OR_MORE"`)

* `AS_MANY_AS_POSSIBLE` (value: `"AS_MANY_AS_POSSIBLE"`)

* `ALL_ROADBLOCK` (value: `"ALL_ROADBLOCK"`)

* `CREATIVE_SET` (value: `"CREATIVE_SET"`)




