

# AchievementDefinition

An achievement definition object.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**achievementType** | [**AchievementTypeEnum**](#AchievementTypeEnum) | The type of the achievement. |  [optional] |
|**description** | **String** | The description of the achievement. |  [optional] |
|**experiencePoints** | **String** | Experience points which will be earned when unlocking this achievement. |  [optional] |
|**formattedTotalSteps** | **String** | The total steps for an incremental achievement as a string. |  [optional] |
|**id** | **String** | The ID of the achievement. |  [optional] |
|**initialState** | [**InitialStateEnum**](#InitialStateEnum) | The initial state of the achievement. |  [optional] |
|**isRevealedIconUrlDefault** | **Boolean** | Indicates whether the revealed icon image being returned is a default image, or is provided by the game. |  [optional] |
|**isUnlockedIconUrlDefault** | **Boolean** | Indicates whether the unlocked icon image being returned is a default image, or is game-provided. |  [optional] |
|**kind** | **String** | Uniquely identifies the type of this resource. Value is always the fixed string &#x60;games#achievementDefinition&#x60;. |  [optional] |
|**name** | **String** | The name of the achievement. |  [optional] |
|**revealedIconUrl** | **String** | The image URL for the revealed achievement icon. |  [optional] |
|**totalSteps** | **Integer** | The total steps for an incremental achievement. |  [optional] |
|**unlockedIconUrl** | **String** | The image URL for the unlocked achievement icon. |  [optional] |



## Enum: AchievementTypeEnum

| Name | Value |
|---- | -----|
| STANDARD | &quot;STANDARD&quot; |
| INCREMENTAL | &quot;INCREMENTAL&quot; |



## Enum: InitialStateEnum

| Name | Value |
|---- | -----|
| HIDDEN | &quot;HIDDEN&quot; |
| REVEALED | &quot;REVEALED&quot; |
| UNLOCKED | &quot;UNLOCKED&quot; |



