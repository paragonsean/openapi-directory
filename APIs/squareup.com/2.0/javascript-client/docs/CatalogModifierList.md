# SquareConnectApi.CatalogModifierList

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**modifiers** | [**[CatalogObject]**](CatalogObject.md) | The options included in the &#x60;CatalogModifierList&#x60;. You must include at least one &#x60;CatalogModifier&#x60;. Each CatalogObject must have type &#x60;MODIFIER&#x60; and contain &#x60;CatalogModifier&#x60; data. | [optional] 
**name** | **String** | The name for the &#x60;CatalogModifierList&#x60; instance. This is a searchable attribute for use in applicable query filters, and its value length is of Unicode code points. | [optional] 
**ordinal** | **Number** | Determines where this modifier list appears in a list of &#x60;CatalogModifierList&#x60; values. | [optional] 
**selectionType** | **String** | Indicates whether multiple options from the modifier list can be applied to a single &#x60;CatalogItem&#x60;. | [optional] 


