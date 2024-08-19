# Nookipedia.NHSeaCreature

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**catchphrases** | **[String]** | An array of possible catchphrases the player says after catching the sea creature. Most critters have just one, but some can have multiple. | [optional] 
**imageUrl** | **String** | Image of the sea creature. | [optional] 
**name** | **String** | Name of the sea creature. | [optional] 
**north** | [**NHSeaCreatureNorth**](NHSeaCreatureNorth.md) |  | [optional] 
**number** | **Number** | In-game sea creature number, marking position in the Critterpedia. | [optional] 
**rarity** | **String** | How rare the sea creature is. Note that this field is currently empty for most sea creatures as we do not yet know how exactly sea creature rarities are calculated in the game code. | [optional] 
**renderUrl** | **String** | Render of the sea creature. | [optional] 
**sellNook** | **Number** | The number of Bells the sea creature can be sold to Nook&#39;s store for. | [optional] 
**shadowMovement** | **String** | Short descriptor of where the sea creature can be found. | [optional] 
**shadowSize** | **String** | Short descriptor of where the sea creature can be found. | [optional] 
**south** | [**NHSeaCreatureSouth**](NHSeaCreatureSouth.md) |  | [optional] 
**tankLength** | **Number** | The length of the tank when the sea creature is placed as a furniture item. | [optional] 
**tankWidth** | **Number** | The width of the tank when the sea creature is placed as a furniture item. | [optional] 
**totalCatch** | **Number** | The total number of sea creatures the player has to have caught before this sea creature will start spawning. | [optional] 
**url** | **String** | Link to the respective Nookipedia article. | [optional] 



## Enum: ShadowMovementEnum


* `Stationary` (value: `"Stationary"`)

* `Very slow` (value: `"Very slow"`)

* `Slow` (value: `"Slow"`)

* `Medium` (value: `"Medium"`)

* `Fast` (value: `"Fast"`)

* `Very fast` (value: `"Very fast"`)





## Enum: ShadowSizeEnum


* `X-Small` (value: `"X-Small"`)

* `Small` (value: `"Small"`)

* `Medium` (value: `"Medium"`)

* `Large` (value: `"Large"`)

* `X-Large` (value: `"X-Large"`)




