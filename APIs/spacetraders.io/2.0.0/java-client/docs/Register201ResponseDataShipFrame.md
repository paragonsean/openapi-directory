

# Register201ResponseDataShipFrame

The frame of the ship. The frame determines the number of modules and mounting points of the ship, as well as base fuel capacity. As the condition of the frame takes more wear, the ship will become more sluggish and less maneuverable.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**condition** | **Integer** | Condition is a range of 0 to 100 where 0 is completely worn out and 100 is brand new. |  [optional] |
|**description** | **String** |  |  |
|**fuelCapacity** | **Integer** |  |  |
|**moduleSlots** | **Integer** |  |  |
|**mountingPoints** | **Integer** |  |  |
|**name** | **String** |  |  |
|**requirements** | [**Register201ResponseDataShipFrameRequirements**](Register201ResponseDataShipFrameRequirements.md) |  |  |
|**symbol** | [**SymbolEnum**](#SymbolEnum) |  |  |



## Enum: SymbolEnum

| Name | Value |
|---- | -----|
| PROBE | &quot;FRAME_PROBE&quot; |
| DRONE | &quot;FRAME_DRONE&quot; |
| INTERCEPTOR | &quot;FRAME_INTERCEPTOR&quot; |
| RACER | &quot;FRAME_RACER&quot; |
| FIGHTER | &quot;FRAME_FIGHTER&quot; |
| FRIGATE | &quot;FRAME_FRIGATE&quot; |
| SHUTTLE | &quot;FRAME_SHUTTLE&quot; |
| EXPLORER | &quot;FRAME_EXPLORER&quot; |
| MINER | &quot;FRAME_MINER&quot; |
| LIGHT_FREIGHTER | &quot;FRAME_LIGHT_FREIGHTER&quot; |
| HEAVY_FREIGHTER | &quot;FRAME_HEAVY_FREIGHTER&quot; |
| TRANSPORT | &quot;FRAME_TRANSPORT&quot; |
| DESTROYER | &quot;FRAME_DESTROYER&quot; |
| CRUISER | &quot;FRAME_CRUISER&quot; |
| CARRIER | &quot;FRAME_CARRIER&quot; |



