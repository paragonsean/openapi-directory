

# DestinyEntitiesCharactersDestinyCharacterRenderComponent

Only really useful if you're attempting to render the character's current appearance in 3D, this returns a bare minimum of information, pre-aggregated, that you'll need to perform that rendering. Note that you need to combine this with other 3D assets and data from our servers.  Examine the Javascript returned by https://bungie.net/sharedbundle/spasm to see how we use this data, but be warned: the rabbit hole goes pretty deep.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**customDyes** | [**List&lt;DestinyDyeReference&gt;**](DestinyDyeReference.md) | Custom dyes, calculated by iterating over the character&#39;s equipped items. Useful for pre-fetching all of the dye data needed from our server. |  [optional] |
|**customization** | [**DestinyCharacterDestinyCharacterCustomization**](DestinyCharacterDestinyCharacterCustomization.md) | This is actually something that Spasm.js *doesn&#39;t* do right now, and that we don&#39;t return assets for yet. This is the data about what character customization options you picked. You can combine this with DestinyCharacterCustomizationOptionDefinition to show some cool info, and hopefully someday to actually render a user&#39;s face in 3D. We&#39;ll see if we ever end up with time for that. |  [optional] |
|**peerView** | [**DestinyCharacterDestinyCharacterPeerView**](DestinyCharacterDestinyCharacterPeerView.md) | A minimal view of:  - Equipped items  - The rendering-related custom options on those equipped items  Combined, that should be enough to render all of the items on the equipped character. |  [optional] |



