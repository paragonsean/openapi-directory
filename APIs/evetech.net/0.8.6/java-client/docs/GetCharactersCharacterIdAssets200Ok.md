

# GetCharactersCharacterIdAssets200Ok

200 ok object

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**isBlueprintCopy** | **Boolean** | is_blueprint_copy boolean |  [optional] |
|**isSingleton** | **Boolean** | is_singleton boolean |  |
|**itemId** | **Long** | item_id integer |  |
|**locationFlag** | [**LocationFlagEnum**](#LocationFlagEnum) | location_flag string |  |
|**locationId** | **Long** | location_id integer |  |
|**locationType** | [**LocationTypeEnum**](#LocationTypeEnum) | location_type string |  |
|**quantity** | **Integer** | quantity integer |  |
|**typeId** | **Integer** | type_id integer |  |



## Enum: LocationFlagEnum

| Name | Value |
|---- | -----|
| ASSET_SAFETY | &quot;AssetSafety&quot; |
| AUTO_FIT | &quot;AutoFit&quot; |
| BOOSTER_BAY | &quot;BoosterBay&quot; |
| CARGO | &quot;Cargo&quot; |
| CORPSE_BAY | &quot;CorpseBay&quot; |
| DELIVERIES | &quot;Deliveries&quot; |
| DRONE_BAY | &quot;DroneBay&quot; |
| FIGHTER_BAY | &quot;FighterBay&quot; |
| FIGHTER_TUBE0 | &quot;FighterTube0&quot; |
| FIGHTER_TUBE1 | &quot;FighterTube1&quot; |
| FIGHTER_TUBE2 | &quot;FighterTube2&quot; |
| FIGHTER_TUBE3 | &quot;FighterTube3&quot; |
| FIGHTER_TUBE4 | &quot;FighterTube4&quot; |
| FLEET_HANGAR | &quot;FleetHangar&quot; |
| HANGAR | &quot;Hangar&quot; |
| HANGAR_ALL | &quot;HangarAll&quot; |
| HI_SLOT0 | &quot;HiSlot0&quot; |
| HI_SLOT1 | &quot;HiSlot1&quot; |
| HI_SLOT2 | &quot;HiSlot2&quot; |
| HI_SLOT3 | &quot;HiSlot3&quot; |
| HI_SLOT4 | &quot;HiSlot4&quot; |
| HI_SLOT5 | &quot;HiSlot5&quot; |
| HI_SLOT6 | &quot;HiSlot6&quot; |
| HI_SLOT7 | &quot;HiSlot7&quot; |
| HIDDEN_MODIFIERS | &quot;HiddenModifiers&quot; |
| IMPLANT | &quot;Implant&quot; |
| LO_SLOT0 | &quot;LoSlot0&quot; |
| LO_SLOT1 | &quot;LoSlot1&quot; |
| LO_SLOT2 | &quot;LoSlot2&quot; |
| LO_SLOT3 | &quot;LoSlot3&quot; |
| LO_SLOT4 | &quot;LoSlot4&quot; |
| LO_SLOT5 | &quot;LoSlot5&quot; |
| LO_SLOT6 | &quot;LoSlot6&quot; |
| LO_SLOT7 | &quot;LoSlot7&quot; |
| LOCKED | &quot;Locked&quot; |
| MED_SLOT0 | &quot;MedSlot0&quot; |
| MED_SLOT1 | &quot;MedSlot1&quot; |
| MED_SLOT2 | &quot;MedSlot2&quot; |
| MED_SLOT3 | &quot;MedSlot3&quot; |
| MED_SLOT4 | &quot;MedSlot4&quot; |
| MED_SLOT5 | &quot;MedSlot5&quot; |
| MED_SLOT6 | &quot;MedSlot6&quot; |
| MED_SLOT7 | &quot;MedSlot7&quot; |
| QUAFE_BAY | &quot;QuafeBay&quot; |
| RIG_SLOT0 | &quot;RigSlot0&quot; |
| RIG_SLOT1 | &quot;RigSlot1&quot; |
| RIG_SLOT2 | &quot;RigSlot2&quot; |
| RIG_SLOT3 | &quot;RigSlot3&quot; |
| RIG_SLOT4 | &quot;RigSlot4&quot; |
| RIG_SLOT5 | &quot;RigSlot5&quot; |
| RIG_SLOT6 | &quot;RigSlot6&quot; |
| RIG_SLOT7 | &quot;RigSlot7&quot; |
| SHIP_HANGAR | &quot;ShipHangar&quot; |
| SKILL | &quot;Skill&quot; |
| SPECIALIZED_AMMO_HOLD | &quot;SpecializedAmmoHold&quot; |
| SPECIALIZED_COMMAND_CENTER_HOLD | &quot;SpecializedCommandCenterHold&quot; |
| SPECIALIZED_FUEL_BAY | &quot;SpecializedFuelBay&quot; |
| SPECIALIZED_GAS_HOLD | &quot;SpecializedGasHold&quot; |
| SPECIALIZED_INDUSTRIAL_SHIP_HOLD | &quot;SpecializedIndustrialShipHold&quot; |
| SPECIALIZED_LARGE_SHIP_HOLD | &quot;SpecializedLargeShipHold&quot; |
| SPECIALIZED_MATERIAL_BAY | &quot;SpecializedMaterialBay&quot; |
| SPECIALIZED_MEDIUM_SHIP_HOLD | &quot;SpecializedMediumShipHold&quot; |
| SPECIALIZED_MINERAL_HOLD | &quot;SpecializedMineralHold&quot; |
| SPECIALIZED_ORE_HOLD | &quot;SpecializedOreHold&quot; |
| SPECIALIZED_PLANETARY_COMMODITIES_HOLD | &quot;SpecializedPlanetaryCommoditiesHold&quot; |
| SPECIALIZED_SALVAGE_HOLD | &quot;SpecializedSalvageHold&quot; |
| SPECIALIZED_SHIP_HOLD | &quot;SpecializedShipHold&quot; |
| SPECIALIZED_SMALL_SHIP_HOLD | &quot;SpecializedSmallShipHold&quot; |
| SUB_SYSTEM_BAY | &quot;SubSystemBay&quot; |
| SUB_SYSTEM_SLOT0 | &quot;SubSystemSlot0&quot; |
| SUB_SYSTEM_SLOT1 | &quot;SubSystemSlot1&quot; |
| SUB_SYSTEM_SLOT2 | &quot;SubSystemSlot2&quot; |
| SUB_SYSTEM_SLOT3 | &quot;SubSystemSlot3&quot; |
| SUB_SYSTEM_SLOT4 | &quot;SubSystemSlot4&quot; |
| SUB_SYSTEM_SLOT5 | &quot;SubSystemSlot5&quot; |
| SUB_SYSTEM_SLOT6 | &quot;SubSystemSlot6&quot; |
| SUB_SYSTEM_SLOT7 | &quot;SubSystemSlot7&quot; |
| UNLOCKED | &quot;Unlocked&quot; |
| WARDROBE | &quot;Wardrobe&quot; |



## Enum: LocationTypeEnum

| Name | Value |
|---- | -----|
| STATION | &quot;station&quot; |
| SOLAR_SYSTEM | &quot;solar_system&quot; |
| OTHER | &quot;other&quot; |



