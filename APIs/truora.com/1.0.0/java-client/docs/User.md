

# User

Represents a user of API-key access control

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**email** | **String** | User email |  [optional] |
|**enabled** | **Boolean** | Indicates whether the user is allowed to access or not |  [optional] |
|**userCreationDate** | **String** | Date on which the user was created |  [optional] |
|**userStatus** | [**UserStatusEnum**](#UserStatusEnum) | Indicates whether the user is confirmed or needs to change their password |  [optional] |
|**username** | **String** | Username |  [optional] |



## Enum: UserStatusEnum

| Name | Value |
|---- | -----|
| FORCE_CHANGE_PASSWORD | &quot;FORCE_CHANGE_PASSWORD&quot; |
| CONFIRMED | &quot;CONFIRMED&quot; |



