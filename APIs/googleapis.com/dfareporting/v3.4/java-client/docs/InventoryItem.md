

# InventoryItem

Represents a buy from the Planning inventory store.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **String** | Account ID of this inventory item. |  [optional] |
|**adSlots** | [**List&lt;AdSlot&gt;**](AdSlot.md) | Ad slots of this inventory item. If this inventory item represents a standalone placement, there will be exactly one ad slot. If this inventory item represents a placement group, there will be more than one ad slot, each representing one child placement in that placement group. |  [optional] |
|**advertiserId** | **String** | Advertiser ID of this inventory item. |  [optional] |
|**contentCategoryId** | **String** | Content category ID of this inventory item. |  [optional] |
|**estimatedClickThroughRate** | **String** | Estimated click-through rate of this inventory item. |  [optional] |
|**estimatedConversionRate** | **String** | Estimated conversion rate of this inventory item. |  [optional] |
|**id** | **String** | ID of this inventory item. |  [optional] |
|**inPlan** | **Boolean** | Whether this inventory item is in plan. |  [optional] |
|**kind** | **String** | Identifies what kind of resource this is. Value: the fixed string \&quot;dfareporting#inventoryItem\&quot;. |  [optional] |
|**lastModifiedInfo** | [**LastModifiedInfo**](LastModifiedInfo.md) |  |  [optional] |
|**name** | **String** | Name of this inventory item. For standalone inventory items, this is the same name as that of its only ad slot. For group inventory items, this can differ from the name of any of its ad slots. |  [optional] |
|**negotiationChannelId** | **String** | Negotiation channel ID of this inventory item. |  [optional] |
|**orderId** | **String** | Order ID of this inventory item. |  [optional] |
|**placementStrategyId** | **String** | Placement strategy ID of this inventory item. |  [optional] |
|**pricing** | [**Pricing**](Pricing.md) |  |  [optional] |
|**projectId** | **String** | Project ID of this inventory item. |  [optional] |
|**rfpId** | **String** | RFP ID of this inventory item. |  [optional] |
|**siteId** | **String** | ID of the site this inventory item is associated with. |  [optional] |
|**subaccountId** | **String** | Subaccount ID of this inventory item. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Type of inventory item. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| REGULAR | &quot;PLANNING_PLACEMENT_TYPE_REGULAR&quot; |
| CREDIT | &quot;PLANNING_PLACEMENT_TYPE_CREDIT&quot; |



