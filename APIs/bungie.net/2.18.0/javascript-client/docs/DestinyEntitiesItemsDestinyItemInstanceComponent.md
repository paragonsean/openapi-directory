# BungieNetApi.DestinyEntitiesItemsDestinyItemInstanceComponent

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**breakerType** | **Number** | If populated, this item has a breaker type corresponding to the given value. See DestinyBreakerTypeDefinition for more details. | [optional] 
**breakerTypeHash** | **Number** | If populated, this is the hash identifier for the item&#39;s breaker type. See DestinyBreakerTypeDefinition for more details. | [optional] 
**canEquip** | **Boolean** | If this is an equippable item, you can check it here. There are permanent as well as transitory reasons why an item might not be able to be equipped: check cannotEquipReason for details. | [optional] 
**cannotEquipReason** | **Number** | If you cannot equip the item, this is a flags enum that enumerates all of the reasons why you couldn&#39;t equip the item. You may need to refine your UI further by using unlockHashesRequiredToEquip and equipRequiredLevel. | [optional] 
**damageType** | **Number** | If the item has a damage type, this is the item&#39;s current damage type. | [optional] 
**damageTypeHash** | **Number** | The current damage type&#39;s hash, so you can look up localized info and icons for it. | [optional] 
**energy** | [**DestinyEntitiesItemsDestinyItemInstanceEnergy**](DestinyEntitiesItemsDestinyItemInstanceEnergy.md) | IF populated, this item supports Energy mechanics (i.e. Armor 2.0), and these are the current details of its energy type and available capacity to spend energy points. | [optional] 
**equipRequiredLevel** | **Number** | If the item cannot be equipped until you reach a certain level, that level will be reflected here. | [optional] 
**isEquipped** | **Boolean** | Is the item currently equipped on the given character? | [optional] 
**itemLevel** | **Number** | The Item&#39;s \&quot;Level\&quot; has the most significant bearing on its stats, such as Light and Power. | [optional] 
**primaryStat** | [**DestinyDestinyStat**](DestinyDestinyStat.md) | The item stat that we consider to be \&quot;primary\&quot; for the item. For instance, this would be \&quot;Attack\&quot; for Weapons or \&quot;Defense\&quot; for armor. | [optional] 
**quality** | **Number** | The \&quot;Quality\&quot; of the item has a lesser - but still impactful - bearing on stats like Light and Power. | [optional] 
**unlockHashesRequiredToEquip** | **[Number]** | Sometimes, there are limitations to equipping that are represented by character-level flags called \&quot;unlocks\&quot;.  This is a list of flags that they need in order to equip the item that the character has not met. Use these to look up the descriptions to show in your UI by looking up the relevant DestinyUnlockDefinitions for the hashes. | [optional] 



## Enum: BreakerTypeEnum


* `0` (value: `0`)

* `1` (value: `1`)

* `2` (value: `2`)

* `3` (value: `3`)




