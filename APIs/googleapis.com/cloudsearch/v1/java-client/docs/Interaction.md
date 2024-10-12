

# Interaction

Represents an interaction between a user and an item.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**interactionTime** | **String** | The time when the user acted on the item. If multiple actions of the same type exist for a single user, only the most recent action is recorded. |  [optional] |
|**principal** | [**Principal**](Principal.md) |  |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) |  |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;UNSPECIFIED&quot; |
| VIEW | &quot;VIEW&quot; |
| EDIT | &quot;EDIT&quot; |



