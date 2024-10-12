

# VillagerNhDetails

An object that holds villager data specific to *New Horizons*. If the villager does not appear in *New Horizons*, this field will be set to null.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**catchphrase** | **String** | The default phrase a villager will use when speaking to the player. |  [optional] |
|**clothing** | **String** | The default clothing that the villager wears. |  [optional] |
|**clothingVariation** | **String** | The variation of the clothing (usually a color). |  [optional] |
|**favColors** | **List&lt;String&gt;** | The villager&#39;s favorite colors (giving the villager a gift with one of their favorite colors increases friendship points). |  [optional] |
|**favStyles** | **List&lt;String&gt;** | The villager&#39;s favorite clothing styles. |  [optional] |
|**hobby** | [**HobbyEnum**](#HobbyEnum) | The villager&#39;s primary hobby, which determines most of the activities they will do around the island (e.g. education villagers will frequently read books and visit the museum). Learn more at https://nookipedia.com/wiki/Hobbies |  [optional] |
|**houseExteriorUrl** | **String** | A rendered model of the villager&#39;s house exterior. Note that this is not an official Nintendo asset, but a render based of the in-game model. |  [optional] |
|**houseFlooring** | **String** | The flooring in the villager&#39;s house. |  [optional] |
|**houseInteriorUrl** | **String** | A screenshot of the villager&#39;s house interior. |  [optional] |
|**houseMusic** | **String** | The music in the villager&#39;s house. |  [optional] |
|**houseMusicNote** | **String** | Any notes about the villager&#39;s music. If populated, this is usually \&quot;Does not contain a stereo initially\&quot;, meaning that the villager&#39;s house will not play music unless provided with a stereo. |  [optional] |
|**houseWallpaper** | **String** | The wallpaper in the villager&#39;s house. |  [optional] |
|**iconUrl** | **String** | The villager&#39;s icon of their head. See https://nookipedia.com/wiki/Category:New_Horizons_character_icons for full list. |  [optional] |
|**imageUrl** | **String** | Image of the villager from *New Horizons*. |  [optional] |
|**photoUrl** | **String** | The villager&#39;s photo, received by the player after attaining a certain friendship level. See https://nookipedia.com/wiki/Category:New_Horizons_pictures for full list. |  [optional] |
|**quote** | **String** | The villager&#39;s quote, as found on the back of their in-game photo. |  [optional] |
|**subPersonality** | [**SubPersonalityEnum**](#SubPersonalityEnum) | Each personality in *New Horizons* has two sub-personalities, currently referred to as just A and B. The effect of a sub-personality is currently unknown. |  [optional] |



## Enum: HobbyEnum

| Name | Value |
|---- | -----|
| EDUCATION | &quot;Education&quot; |
| FASHION | &quot;Fashion&quot; |
| FITNESS | &quot;Fitness&quot; |
| MUSIC | &quot;Music&quot; |
| NATURE | &quot;Nature&quot; |
| PLAY | &quot;Play&quot; |



## Enum: SubPersonalityEnum

| Name | Value |
|---- | -----|
| A | &quot;A&quot; |
| B | &quot;B&quot; |



