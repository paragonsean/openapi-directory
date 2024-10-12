# CampaignManager360Api.Pricing

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**capCostType** | **String** | Cap cost type of this inventory item. | [optional] 
**endDate** | **Date** |  | [optional] 
**flights** | [**[Flight]**](Flight.md) | Flights of this inventory item. A flight (a.k.a. pricing period) represents the inventory item pricing information for a specific period of time. | [optional] 
**groupType** | **String** | Group type of this inventory item if it represents a placement group. Is null otherwise. There are two type of placement groups: PLANNING_PLACEMENT_GROUP_TYPE_PACKAGE is a simple group of inventory items that acts as a single pricing point for a group of tags. PLANNING_PLACEMENT_GROUP_TYPE_ROADBLOCK is a group of inventory items that not only acts as a single pricing point, but also assumes that all the tags in it will be served at the same time. A roadblock requires one of its assigned inventory items to be marked as primary. | [optional] 
**pricingType** | **String** | Pricing type of this inventory item. | [optional] 
**startDate** | **Date** |  | [optional] 



## Enum: CapCostTypeEnum


* `NONE` (value: `"PLANNING_PLACEMENT_CAP_COST_TYPE_NONE"`)

* `MONTHLY` (value: `"PLANNING_PLACEMENT_CAP_COST_TYPE_MONTHLY"`)

* `CUMULATIVE` (value: `"PLANNING_PLACEMENT_CAP_COST_TYPE_CUMULATIVE"`)





## Enum: GroupTypeEnum


* `PACKAGE` (value: `"PLANNING_PLACEMENT_GROUP_TYPE_PACKAGE"`)

* `ROADBLOCK` (value: `"PLANNING_PLACEMENT_GROUP_TYPE_ROADBLOCK"`)





## Enum: PricingTypeEnum


* `IMPRESSIONS` (value: `"PLANNING_PLACEMENT_PRICING_TYPE_IMPRESSIONS"`)

* `CPM` (value: `"PLANNING_PLACEMENT_PRICING_TYPE_CPM"`)

* `CLICKS` (value: `"PLANNING_PLACEMENT_PRICING_TYPE_CLICKS"`)

* `CPC` (value: `"PLANNING_PLACEMENT_PRICING_TYPE_CPC"`)

* `CPA` (value: `"PLANNING_PLACEMENT_PRICING_TYPE_CPA"`)

* `FLAT_RATE_IMPRESSIONS` (value: `"PLANNING_PLACEMENT_PRICING_TYPE_FLAT_RATE_IMPRESSIONS"`)

* `FLAT_RATE_CLICKS` (value: `"PLANNING_PLACEMENT_PRICING_TYPE_FLAT_RATE_CLICKS"`)

* `CPM_ACTIVEVIEW` (value: `"PLANNING_PLACEMENT_PRICING_TYPE_CPM_ACTIVEVIEW"`)




