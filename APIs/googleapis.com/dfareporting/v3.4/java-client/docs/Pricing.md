

# Pricing

Pricing Information

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**capCostType** | [**CapCostTypeEnum**](#CapCostTypeEnum) | Cap cost type of this inventory item. |  [optional] |
|**endDate** | **LocalDate** |  |  [optional] |
|**flights** | [**List&lt;Flight&gt;**](Flight.md) | Flights of this inventory item. A flight (a.k.a. pricing period) represents the inventory item pricing information for a specific period of time. |  [optional] |
|**groupType** | [**GroupTypeEnum**](#GroupTypeEnum) | Group type of this inventory item if it represents a placement group. Is null otherwise. There are two type of placement groups: PLANNING_PLACEMENT_GROUP_TYPE_PACKAGE is a simple group of inventory items that acts as a single pricing point for a group of tags. PLANNING_PLACEMENT_GROUP_TYPE_ROADBLOCK is a group of inventory items that not only acts as a single pricing point, but also assumes that all the tags in it will be served at the same time. A roadblock requires one of its assigned inventory items to be marked as primary. |  [optional] |
|**pricingType** | [**PricingTypeEnum**](#PricingTypeEnum) | Pricing type of this inventory item. |  [optional] |
|**startDate** | **LocalDate** |  |  [optional] |



## Enum: CapCostTypeEnum

| Name | Value |
|---- | -----|
| NONE | &quot;PLANNING_PLACEMENT_CAP_COST_TYPE_NONE&quot; |
| MONTHLY | &quot;PLANNING_PLACEMENT_CAP_COST_TYPE_MONTHLY&quot; |
| CUMULATIVE | &quot;PLANNING_PLACEMENT_CAP_COST_TYPE_CUMULATIVE&quot; |



## Enum: GroupTypeEnum

| Name | Value |
|---- | -----|
| PACKAGE | &quot;PLANNING_PLACEMENT_GROUP_TYPE_PACKAGE&quot; |
| ROADBLOCK | &quot;PLANNING_PLACEMENT_GROUP_TYPE_ROADBLOCK&quot; |



## Enum: PricingTypeEnum

| Name | Value |
|---- | -----|
| IMPRESSIONS | &quot;PLANNING_PLACEMENT_PRICING_TYPE_IMPRESSIONS&quot; |
| CPM | &quot;PLANNING_PLACEMENT_PRICING_TYPE_CPM&quot; |
| CLICKS | &quot;PLANNING_PLACEMENT_PRICING_TYPE_CLICKS&quot; |
| CPC | &quot;PLANNING_PLACEMENT_PRICING_TYPE_CPC&quot; |
| CPA | &quot;PLANNING_PLACEMENT_PRICING_TYPE_CPA&quot; |
| FLAT_RATE_IMPRESSIONS | &quot;PLANNING_PLACEMENT_PRICING_TYPE_FLAT_RATE_IMPRESSIONS&quot; |
| FLAT_RATE_CLICKS | &quot;PLANNING_PLACEMENT_PRICING_TYPE_FLAT_RATE_CLICKS&quot; |
| CPM_ACTIVEVIEW | &quot;PLANNING_PLACEMENT_PRICING_TYPE_CPM_ACTIVEVIEW&quot; |



