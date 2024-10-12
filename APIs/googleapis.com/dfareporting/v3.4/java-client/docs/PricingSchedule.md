

# PricingSchedule

Pricing Schedule

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**capCostOption** | [**CapCostOptionEnum**](#CapCostOptionEnum) | Placement cap cost option. |  [optional] |
|**endDate** | **LocalDate** |  |  [optional] |
|**flighted** | **Boolean** | Whether this placement is flighted. If true, pricing periods will be computed automatically. |  [optional] |
|**floodlightActivityId** | **String** | Floodlight activity ID associated with this placement. This field should be set when placement pricing type is set to PRICING_TYPE_CPA. |  [optional] |
|**pricingPeriods** | [**List&lt;PricingSchedulePricingPeriod&gt;**](PricingSchedulePricingPeriod.md) | Pricing periods for this placement. |  [optional] |
|**pricingType** | [**PricingTypeEnum**](#PricingTypeEnum) | Placement pricing type. This field is required on insertion. |  [optional] |
|**startDate** | **LocalDate** |  |  [optional] |
|**testingStartDate** | **LocalDate** |  |  [optional] |



## Enum: CapCostOptionEnum

| Name | Value |
|---- | -----|
| NONE | &quot;CAP_COST_NONE&quot; |
| MONTHLY | &quot;CAP_COST_MONTHLY&quot; |
| CUMULATIVE | &quot;CAP_COST_CUMULATIVE&quot; |



## Enum: PricingTypeEnum

| Name | Value |
|---- | -----|
| CPM | &quot;PRICING_TYPE_CPM&quot; |
| CPC | &quot;PRICING_TYPE_CPC&quot; |
| CPA | &quot;PRICING_TYPE_CPA&quot; |
| FLAT_RATE_IMPRESSIONS | &quot;PRICING_TYPE_FLAT_RATE_IMPRESSIONS&quot; |
| FLAT_RATE_CLICKS | &quot;PRICING_TYPE_FLAT_RATE_CLICKS&quot; |
| CPM_ACTIVEVIEW | &quot;PRICING_TYPE_CPM_ACTIVEVIEW&quot; |



