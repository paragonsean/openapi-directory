# CampaignManager360Api.PricingSchedule

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**capCostOption** | **String** | Placement cap cost option. | [optional] 
**disregardOverdelivery** | **Boolean** | Whether cap costs are ignored by ad serving. | [optional] 
**endDate** | **Date** |  | [optional] 
**flighted** | **Boolean** | Whether this placement is flighted. If true, pricing periods will be computed automatically. | [optional] 
**floodlightActivityId** | **String** | Floodlight activity ID associated with this placement. This field should be set when placement pricing type is set to PRICING_TYPE_CPA. | [optional] 
**pricingPeriods** | [**[PricingSchedulePricingPeriod]**](PricingSchedulePricingPeriod.md) | Pricing periods for this placement. | [optional] 
**pricingType** | **String** | Placement pricing type. This field is required on insertion. | [optional] 
**startDate** | **Date** |  | [optional] 
**testingStartDate** | **Date** |  | [optional] 



## Enum: CapCostOptionEnum


* `NONE` (value: `"CAP_COST_NONE"`)

* `MONTHLY` (value: `"CAP_COST_MONTHLY"`)

* `CUMULATIVE` (value: `"CAP_COST_CUMULATIVE"`)





## Enum: PricingTypeEnum


* `CPM` (value: `"PRICING_TYPE_CPM"`)

* `CPC` (value: `"PRICING_TYPE_CPC"`)

* `CPA` (value: `"PRICING_TYPE_CPA"`)

* `FLAT_RATE_IMPRESSIONS` (value: `"PRICING_TYPE_FLAT_RATE_IMPRESSIONS"`)

* `FLAT_RATE_CLICKS` (value: `"PRICING_TYPE_FLAT_RATE_CLICKS"`)

* `CPM_ACTIVEVIEW` (value: `"PRICING_TYPE_CPM_ACTIVEVIEW"`)




