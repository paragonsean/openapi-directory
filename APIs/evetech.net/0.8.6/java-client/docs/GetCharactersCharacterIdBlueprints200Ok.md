

# GetCharactersCharacterIdBlueprints200Ok

200 ok object

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**itemId** | **Long** | Unique ID for this item. |  |
|**locationFlag** | [**LocationFlagEnum**](#LocationFlagEnum) | Type of the location_id |  |
|**locationId** | **Long** | References a solar system, station or item_id if this blueprint is located within a container. If the return value is an item_id, then the Character AssetList API must be queried to find the container using the given item_id to determine the correct location of the Blueprint. |  |
|**materialEfficiency** | **Integer** | Material Efficiency Level of the blueprint. |  |
|**quantity** | **Integer** | A range of numbers with a minimum of -2 and no maximum value where -1 is an original and -2 is a copy. It can be a positive integer if it is a stack of blueprint originals fresh from the market (e.g. no activities performed on them yet). |  |
|**runs** | **Integer** | Number of runs remaining if the blueprint is a copy, -1 if it is an original. |  |
|**timeEfficiency** | **Integer** | Time Efficiency Level of the blueprint. |  |
|**typeId** | **Integer** | type_id integer |  |



## Enum: LocationFlagEnum

| Name | Value |
|---- | -----|
| AUTO_FIT | &quot;AutoFit&quot; |
| CARGO | &quot;Cargo&quot; |
| CORPSE_BAY | &quot;CorpseBay&quot; |
| DRONE_BAY | &quot;DroneBay&quot; |
| FLEET_HANGAR | &quot;FleetHangar&quot; |
| DELIVERIES | &quot;Deliveries&quot; |
| HIDDEN_MODIFIERS | &quot;HiddenModifiers&quot; |
| HANGAR | &quot;Hangar&quot; |
| HANGAR_ALL | &quot;HangarAll&quot; |
| LO_SLOT0 | &quot;LoSlot0&quot; |
| LO_SLOT1 | &quot;LoSlot1&quot; |
| LO_SLOT2 | &quot;LoSlot2&quot; |
| LO_SLOT3 | &quot;LoSlot3&quot; |
| LO_SLOT4 | &quot;LoSlot4&quot; |
| LO_SLOT5 | &quot;LoSlot5&quot; |
| LO_SLOT6 | &quot;LoSlot6&quot; |
| LO_SLOT7 | &quot;LoSlot7&quot; |
| MED_SLOT0 | &quot;MedSlot0&quot; |
| MED_SLOT1 | &quot;MedSlot1&quot; |
| MED_SLOT2 | &quot;MedSlot2&quot; |
| MED_SLOT3 | &quot;MedSlot3&quot; |
| MED_SLOT4 | &quot;MedSlot4&quot; |
| MED_SLOT5 | &quot;MedSlot5&quot; |
| MED_SLOT6 | &quot;MedSlot6&quot; |
| MED_SLOT7 | &quot;MedSlot7&quot; |
| HI_SLOT0 | &quot;HiSlot0&quot; |
| HI_SLOT1 | &quot;HiSlot1&quot; |
| HI_SLOT2 | &quot;HiSlot2&quot; |
| HI_SLOT3 | &quot;HiSlot3&quot; |
| HI_SLOT4 | &quot;HiSlot4&quot; |
| HI_SLOT5 | &quot;HiSlot5&quot; |
| HI_SLOT6 | &quot;HiSlot6&quot; |
| HI_SLOT7 | &quot;HiSlot7&quot; |
| ASSET_SAFETY | &quot;AssetSafety&quot; |
| LOCKED | &quot;Locked&quot; |
| UNLOCKED | &quot;Unlocked&quot; |
| IMPLANT | &quot;Implant&quot; |
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
| SPECIALIZED_FUEL_BAY | &quot;SpecializedFuelBay&quot; |
| SPECIALIZED_ORE_HOLD | &quot;SpecializedOreHold&quot; |
| SPECIALIZED_GAS_HOLD | &quot;SpecializedGasHold&quot; |
| SPECIALIZED_MINERAL_HOLD | &quot;SpecializedMineralHold&quot; |
| SPECIALIZED_SALVAGE_HOLD | &quot;SpecializedSalvageHold&quot; |
| SPECIALIZED_SHIP_HOLD | &quot;SpecializedShipHold&quot; |
| SPECIALIZED_SMALL_SHIP_HOLD | &quot;SpecializedSmallShipHold&quot; |
| SPECIALIZED_MEDIUM_SHIP_HOLD | &quot;SpecializedMediumShipHold&quot; |
| SPECIALIZED_LARGE_SHIP_HOLD | &quot;SpecializedLargeShipHold&quot; |
| SPECIALIZED_INDUSTRIAL_SHIP_HOLD | &quot;SpecializedIndustrialShipHold&quot; |
| SPECIALIZED_AMMO_HOLD | &quot;SpecializedAmmoHold&quot; |
| SPECIALIZED_COMMAND_CENTER_HOLD | &quot;SpecializedCommandCenterHold&quot; |
| SPECIALIZED_PLANETARY_COMMODITIES_HOLD | &quot;SpecializedPlanetaryCommoditiesHold&quot; |
| SPECIALIZED_MATERIAL_BAY | &quot;SpecializedMaterialBay&quot; |
| SUB_SYSTEM_SLOT0 | &quot;SubSystemSlot0&quot; |
| SUB_SYSTEM_SLOT1 | &quot;SubSystemSlot1&quot; |
| SUB_SYSTEM_SLOT2 | &quot;SubSystemSlot2&quot; |
| SUB_SYSTEM_SLOT3 | &quot;SubSystemSlot3&quot; |
| SUB_SYSTEM_SLOT4 | &quot;SubSystemSlot4&quot; |
| SUB_SYSTEM_SLOT5 | &quot;SubSystemSlot5&quot; |
| SUB_SYSTEM_SLOT6 | &quot;SubSystemSlot6&quot; |
| SUB_SYSTEM_SLOT7 | &quot;SubSystemSlot7&quot; |
| FIGHTER_BAY | &quot;FighterBay&quot; |
| FIGHTER_TUBE0 | &quot;FighterTube0&quot; |
| FIGHTER_TUBE1 | &quot;FighterTube1&quot; |
| FIGHTER_TUBE2 | &quot;FighterTube2&quot; |
| FIGHTER_TUBE3 | &quot;FighterTube3&quot; |
| FIGHTER_TUBE4 | &quot;FighterTube4&quot; |
| MODULE | &quot;Module&quot; |



