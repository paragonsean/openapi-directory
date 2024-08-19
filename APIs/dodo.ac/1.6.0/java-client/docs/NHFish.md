

# NHFish


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**catchphrases** | **List&lt;String&gt;** | An array of possible catchphrases the player says after catching the fish. Most critters have just one, but some can have multiple. |  [optional] |
|**imageUrl** | **String** | Image of the fish. |  [optional] |
|**location** | **String** | Short descriptor of where the fish can be found. |  [optional] |
|**name** | **String** | Name of the fish. |  [optional] |
|**north** | [**NHFishNorth**](NHFishNorth.md) |  |  [optional] |
|**number** | **Integer** | In-game fish number, marking position in the Critterpedia. |  [optional] |
|**rarity** | **String** | How rare the fish is. Note that this field is currently empty for most fish as we do not yet know how exactly fish rarities are calculated in the game code. |  [optional] |
|**renderUrl** | **String** | Render of the fish. |  [optional] |
|**sellCj** | **Integer** | The number of Bells the fish can be sold to C.J. for. This value is always 1.5x that of &#x60;sell_nook&#x60;. |  [optional] |
|**sellNook** | **Integer** | The number of Bells the fish can be sold to Nook&#39;s store for. |  [optional] |
|**shadowSize** | [**ShadowSizeEnum**](#ShadowSizeEnum) | The size of the fish&#39;s shadow. |  [optional] |
|**south** | [**NHFishSouth**](NHFishSouth.md) |  |  [optional] |
|**tankLength** | **Float** | The length of the tank when the fish is placed as a furniture item. |  [optional] |
|**tankWidth** | **Float** | The width of the tank when the fish is placed as a furniture item. |  [optional] |
|**totalCatch** | **Integer** | The total number of fish the player has to have caught before this fish will start spawning. |  [optional] |
|**url** | **String** | Link to the respective Nookipedia article. |  [optional] |



## Enum: ShadowSizeEnum

| Name | Value |
|---- | -----|
| X_SMALL | &quot;X-Small&quot; |
| SMALL | &quot;Small&quot; |
| MEDIUM | &quot;Medium&quot; |
| MEDIUM_W_FIN | &quot;Medium w/Fin&quot; |
| LARGE | &quot;Large&quot; |
| LARGE_W_FIN | &quot;Large w/Fin&quot; |
| X_LARGE | &quot;X-Large&quot; |
| XX_LARGE | &quot;XX-Large&quot; |
| LONG | &quot;Long&quot; |



