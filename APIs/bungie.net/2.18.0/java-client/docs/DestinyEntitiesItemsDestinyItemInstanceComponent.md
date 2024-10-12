

# DestinyEntitiesItemsDestinyItemInstanceComponent

If an item is \"instanced\", this will contain information about the item's instance that doesn't fit easily into other components. One might say this is the \"essential\" instance data for the item.  Items are instanced if they require information or state that can vary. For instance, weapons are Instanced: they are given a unique identifier, uniquely generated stats, and can have their properties altered. Non-instanced items have none of these things: for instance, Glimmer has no unique properties aside from how much of it you own.  You can tell from an item's definition whether it will be instanced or not by looking at the DestinyInventoryItemDefinition's definition.inventory.isInstanceItem property.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**breakerType** | [**BreakerTypeEnum**](#BreakerTypeEnum) | If populated, this item has a breaker type corresponding to the given value. See DestinyBreakerTypeDefinition for more details. |  [optional] |
|**breakerTypeHash** | **Integer** | If populated, this is the hash identifier for the item&#39;s breaker type. See DestinyBreakerTypeDefinition for more details. |  [optional] |
|**canEquip** | **Boolean** | If this is an equippable item, you can check it here. There are permanent as well as transitory reasons why an item might not be able to be equipped: check cannotEquipReason for details. |  [optional] |
|**cannotEquipReason** | **Integer** | If you cannot equip the item, this is a flags enum that enumerates all of the reasons why you couldn&#39;t equip the item. You may need to refine your UI further by using unlockHashesRequiredToEquip and equipRequiredLevel. |  [optional] |
|**damageType** | **Integer** | If the item has a damage type, this is the item&#39;s current damage type. |  [optional] |
|**damageTypeHash** | **Integer** | The current damage type&#39;s hash, so you can look up localized info and icons for it. |  [optional] |
|**energy** | [**DestinyEntitiesItemsDestinyItemInstanceEnergy**](DestinyEntitiesItemsDestinyItemInstanceEnergy.md) | IF populated, this item supports Energy mechanics (i.e. Armor 2.0), and these are the current details of its energy type and available capacity to spend energy points. |  [optional] |
|**equipRequiredLevel** | **Integer** | If the item cannot be equipped until you reach a certain level, that level will be reflected here. |  [optional] |
|**isEquipped** | **Boolean** | Is the item currently equipped on the given character? |  [optional] |
|**itemLevel** | **Integer** | The Item&#39;s \&quot;Level\&quot; has the most significant bearing on its stats, such as Light and Power. |  [optional] |
|**primaryStat** | [**DestinyDestinyStat**](DestinyDestinyStat.md) | The item stat that we consider to be \&quot;primary\&quot; for the item. For instance, this would be \&quot;Attack\&quot; for Weapons or \&quot;Defense\&quot; for armor. |  [optional] |
|**quality** | **Integer** | The \&quot;Quality\&quot; of the item has a lesser - but still impactful - bearing on stats like Light and Power. |  [optional] |
|**unlockHashesRequiredToEquip** | **List&lt;Integer&gt;** | Sometimes, there are limitations to equipping that are represented by character-level flags called \&quot;unlocks\&quot;.  This is a list of flags that they need in order to equip the item that the character has not met. Use these to look up the descriptions to show in your UI by looking up the relevant DestinyUnlockDefinitions for the hashes. |  [optional] |



## Enum: BreakerTypeEnum

| Name | Value |
|---- | -----|
| NUMBER_0 | 0 |
| NUMBER_1 | 1 |
| NUMBER_2 | 2 |
| NUMBER_3 | 3 |



