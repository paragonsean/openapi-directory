

# NHSeaCreature


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**catchphrases** | **List&lt;String&gt;** | An array of possible catchphrases the player says after catching the sea creature. Most critters have just one, but some can have multiple. |  [optional] |
|**imageUrl** | **String** | Image of the sea creature. |  [optional] |
|**name** | **String** | Name of the sea creature. |  [optional] |
|**north** | [**NHSeaCreatureNorth**](NHSeaCreatureNorth.md) |  |  [optional] |
|**number** | **Integer** | In-game sea creature number, marking position in the Critterpedia. |  [optional] |
|**rarity** | **String** | How rare the sea creature is. Note that this field is currently empty for most sea creatures as we do not yet know how exactly sea creature rarities are calculated in the game code. |  [optional] |
|**renderUrl** | **String** | Render of the sea creature. |  [optional] |
|**sellNook** | **Integer** | The number of Bells the sea creature can be sold to Nook&#39;s store for. |  [optional] |
|**shadowMovement** | [**ShadowMovementEnum**](#ShadowMovementEnum) | Short descriptor of where the sea creature can be found. |  [optional] |
|**shadowSize** | [**ShadowSizeEnum**](#ShadowSizeEnum) | Short descriptor of where the sea creature can be found. |  [optional] |
|**south** | [**NHSeaCreatureSouth**](NHSeaCreatureSouth.md) |  |  [optional] |
|**tankLength** | **Float** | The length of the tank when the sea creature is placed as a furniture item. |  [optional] |
|**tankWidth** | **Float** | The width of the tank when the sea creature is placed as a furniture item. |  [optional] |
|**totalCatch** | **Integer** | The total number of sea creatures the player has to have caught before this sea creature will start spawning. |  [optional] |
|**url** | **String** | Link to the respective Nookipedia article. |  [optional] |



## Enum: ShadowMovementEnum

| Name | Value |
|---- | -----|
| STATIONARY | &quot;Stationary&quot; |
| VERY_SLOW | &quot;Very slow&quot; |
| SLOW | &quot;Slow&quot; |
| MEDIUM | &quot;Medium&quot; |
| FAST | &quot;Fast&quot; |
| VERY_FAST | &quot;Very fast&quot; |



## Enum: ShadowSizeEnum

| Name | Value |
|---- | -----|
| X_SMALL | &quot;X-Small&quot; |
| SMALL | &quot;Small&quot; |
| MEDIUM | &quot;Medium&quot; |
| LARGE | &quot;Large&quot; |
| X_LARGE | &quot;X-Large&quot; |



