

# AchievementRevealResponse

An achievement reveal response

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**currentState** | [**CurrentStateEnum**](#CurrentStateEnum) | The current state of the achievement for which a reveal was attempted. This might be &#x60;UNLOCKED&#x60; if the achievement was already unlocked. |  [optional] |
|**kind** | **String** | Uniquely identifies the type of this resource. Value is always the fixed string &#x60;games#achievementRevealResponse&#x60;. |  [optional] |



## Enum: CurrentStateEnum

| Name | Value |
|---- | -----|
| REVEALED | &quot;REVEALED&quot; |
| UNLOCKED | &quot;UNLOCKED&quot; |



