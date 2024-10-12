# BungieNetApi.DestinyDefinitionsDestinyVendorCategoryEntryDefinition

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**buyStringOverride** | **String** | The localized string for making purchases from this category, if it is different from the vendor&#39;s string for purchasing. | [optional] 
**categoryHash** | **Number** | The hashed identifier for the category. | [optional] 
**categoryIndex** | **Number** | The index of the category in the original category definitions for the vendor. | [optional] 
**disabledDescription** | **String** | If the category is disabled, this is the localized description to show. | [optional] 
**displayTitle** | **String** | The localized title of the category. | [optional] 
**hideFromRegularPurchase** | **Boolean** | True if this category doesn&#39;t allow purchases. | [optional] 
**hideIfNoCurrency** | **Boolean** | If you don&#39;t have the currency required to buy items from this category, should the items be hidden? | [optional] 
**isDisplayOnly** | **Boolean** | If true, this category only displays items: you can&#39;t purchase anything in them. | [optional] 
**isPreview** | **Boolean** | Sometimes a category isn&#39;t actually used to sell items, but rather to preview them. This implies different UI (and manual placement of the category in the UI) in the game, and special treatment. | [optional] 
**overlay** | [**DestinyDefinitionsDestinyVendorCategoryOverlayDefinition**](DestinyDefinitionsDestinyVendorCategoryOverlayDefinition.md) | If this category has an overlay prompt that should appear, this contains the details of that prompt. | [optional] 
**quantityAvailable** | **Number** | The amount of items that will be available when this category is shown. | [optional] 
**resetIntervalMinutesOverride** | **Number** |  | [optional] 
**resetOffsetMinutesOverride** | **Number** |  | [optional] 
**showUnavailableItems** | **Boolean** | If items aren&#39;t up for sale in this category, should we still show them (greyed out)? | [optional] 
**sortValue** | **Number** | Used in sorting items in vendors... but there&#39;s a lot more to it. Just go with the order provided in the itemIndexes property on the DestinyVendorCategoryComponent instead, it should be more reliable than trying to recalculate it yourself. | [optional] 
**vendorItemIndexes** | **[Number]** | A shortcut for the vendor item indexes sold under this category. Saves us from some expensive reorganization at runtime. | [optional] 


