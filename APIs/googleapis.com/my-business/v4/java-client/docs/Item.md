

# Item

A single list item. Each variation of an item in the price list should have its own Item with its own price data.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**itemId** | **String** | Required. ID for the item. Price list, section, and item IDs cannot be duplicated within this Location. |  [optional] |
|**labels** | [**List&lt;Label&gt;**](Label.md) | Required. Language-tagged labels for the item. We recommend that item names be 140 characters or less, and descriptions 250 characters or less. At least one set of labels is required. |  [optional] |
|**price** | [**Money**](Money.md) |  |  [optional] |



