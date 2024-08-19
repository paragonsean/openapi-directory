# Nookipedia.NHFish

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**catchphrases** | **[String]** | An array of possible catchphrases the player says after catching the fish. Most critters have just one, but some can have multiple. | [optional] 
**imageUrl** | **String** | Image of the fish. | [optional] 
**location** | **String** | Short descriptor of where the fish can be found. | [optional] 
**name** | **String** | Name of the fish. | [optional] 
**north** | [**NHFishNorth**](NHFishNorth.md) |  | [optional] 
**number** | **Number** | In-game fish number, marking position in the Critterpedia. | [optional] 
**rarity** | **String** | How rare the fish is. Note that this field is currently empty for most fish as we do not yet know how exactly fish rarities are calculated in the game code. | [optional] 
**renderUrl** | **String** | Render of the fish. | [optional] 
**sellCj** | **Number** | The number of Bells the fish can be sold to C.J. for. This value is always 1.5x that of &#x60;sell_nook&#x60;. | [optional] 
**sellNook** | **Number** | The number of Bells the fish can be sold to Nook&#39;s store for. | [optional] 
**shadowSize** | **String** | The size of the fish&#39;s shadow. | [optional] 
**south** | [**NHFishSouth**](NHFishSouth.md) |  | [optional] 
**tankLength** | **Number** | The length of the tank when the fish is placed as a furniture item. | [optional] 
**tankWidth** | **Number** | The width of the tank when the fish is placed as a furniture item. | [optional] 
**totalCatch** | **Number** | The total number of fish the player has to have caught before this fish will start spawning. | [optional] 
**url** | **String** | Link to the respective Nookipedia article. | [optional] 



## Enum: ShadowSizeEnum


* `X-Small` (value: `"X-Small"`)

* `Small` (value: `"Small"`)

* `Medium` (value: `"Medium"`)

* `Medium w/Fin` (value: `"Medium w/Fin"`)

* `Large` (value: `"Large"`)

* `Large w/Fin` (value: `"Large w/Fin"`)

* `X-Large` (value: `"X-Large"`)

* `XX-Large` (value: `"XX-Large"`)

* `Long` (value: `"Long"`)




