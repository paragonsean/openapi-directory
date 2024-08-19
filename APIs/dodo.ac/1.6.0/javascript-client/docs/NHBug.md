# Nookipedia.NHBug

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**catchphrases** | **[String]** | An array of possible catchphrases the player says after catching the bug. Most critters have just one, but some can have multiple. | [optional] 
**imageUrl** | **String** | Image of the bug. | [optional] 
**location** | **String** | Short descriptor of where the bug can be found. | [optional] 
**name** | **String** | Name of the bug. | [optional] 
**north** | [**NHBugNorth**](NHBugNorth.md) |  | [optional] 
**number** | **Number** | In-game bug number, marking position in the Critterpedia. | [optional] 
**rarity** | **String** | How rare the bug is. Note that this field is currently empty for most bugs as we do not yet know how exactly bug rarities are calculated in the game code. | [optional] 
**renderUrl** | **String** | Render of the bug. | [optional] 
**sellFlick** | **Number** | The number of Bells the bug can be sold to Flick for. This value is always 1.5x that of &#x60;sell_nook&#x60;. | [optional] 
**sellNook** | **Number** | The number of Bells the bug can be sold to Nook&#39;s store for. | [optional] 
**south** | [**NHBugSouth**](NHBugSouth.md) |  | [optional] 
**tankLength** | **Number** | The length of the tank when the bug is placed as a furniture item. | [optional] 
**tankWidth** | **Number** | The width of the tank when the bug is placed as a furniture item. | [optional] 
**totalCatch** | **Number** | The total number of bug the player has to have caught before this bug will start spawning. | [optional] 
**url** | **String** | Link to the respective Nookipedia article. | [optional] 


