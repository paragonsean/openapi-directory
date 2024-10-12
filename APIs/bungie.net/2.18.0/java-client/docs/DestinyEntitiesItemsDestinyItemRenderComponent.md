

# DestinyEntitiesItemsDestinyItemRenderComponent

Many items can be rendered in 3D. When you request this block, you will obtain the custom data needed to render this specific instance of the item.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**artRegions** | **Map&lt;String, Integer&gt;** | A dictionary for rendering gear components, with:  key &#x3D; Art Arrangement Region Index  value &#x3D; The chosen Arrangement Index for the Region, based on the value of a stat on the item used for making the choice. |  [optional] |
|**useCustomDyes** | **Boolean** | If you should use custom dyes on this item, it will be indicated here. |  [optional] |



