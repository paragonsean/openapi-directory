

# ConditionDistribution

The container that defines the fields for the conditions refinements. This container is returned when <b> fieldgroups</b> is set to <code>CONDITION_REFINEMENTS</code> or <code>FULL</code> in the request.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**condition** | **String** | The text describing the condition of the item, such as New or Used. For a list of condition names, see Item Condition IDs and Names. Code so that your app gracefully handles any future changes to this list. Note: In the US and Australian marketplaces, Condition ID 2000 now maps to an item condition of &#39;Certified Refurbished&#39;, but this item condition is only available for use for a select number of US and Australian sellers. For all other marketplaces besides the US and Australia, Condition ID 2000 still maps to &#39;Manufacturer Refurbished&#39;. |  [optional] |
|**conditionId** | **String** | The identifier of the condition. For example, 1000 is the identifier for NEW. Note: In the US and Australian marketplaces, Condition ID 2000 now maps to an item condition of &#39;Certified Refurbished&#39;, but this item condition is only available for use for a select number of US and Australian sellers. For all other marketplaces besides the US and Australia, Condition ID 2000 still maps to &#39;Manufacturer Refurbished&#39;. |  [optional] |
|**matchCount** | **Integer** | The number of items having the condition. |  [optional] |
|**refinementHref** | **String** | The HATEOAS reference of this condition. |  [optional] |



