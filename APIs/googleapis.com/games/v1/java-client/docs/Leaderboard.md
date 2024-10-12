

# Leaderboard

The Leaderboard resource.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**iconUrl** | **String** | The icon for the leaderboard. |  [optional] |
|**id** | **String** | The leaderboard ID. |  [optional] |
|**isIconUrlDefault** | **Boolean** | Indicates whether the icon image being returned is a default image, or is game-provided. |  [optional] |
|**kind** | **String** | Uniquely identifies the type of this resource. Value is always the fixed string &#x60;games#leaderboard&#x60;. |  [optional] |
|**name** | **String** | The name of the leaderboard. |  [optional] |
|**order** | [**OrderEnum**](#OrderEnum) | How scores are ordered. |  [optional] |



## Enum: OrderEnum

| Name | Value |
|---- | -----|
| LARGER_IS_BETTER | &quot;LARGER_IS_BETTER&quot; |
| SMALLER_IS_BETTER | &quot;SMALLER_IS_BETTER&quot; |



