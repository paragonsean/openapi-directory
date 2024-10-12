

# Attributes26


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**auto** | **Boolean** | Bool of representing whether a user created the action. |  [optional] [readonly] |
|**comment** | **String** | A comment made explaining the reasoning of the action. |  [optional] [readonly] |
|**dateCreated** | **String** | The date the action was created. |  [optional] [readonly] |
|**fromState** | [**FromStateEnum**](#FromStateEnum) | The name of the state of the Schema Response prior to the creation of the action. |  [optional] |
|**toState** | [**ToStateEnum**](#ToStateEnum) | The name of the state of the Schema Response after the creation of the action |  [optional] |
|**trigger** | [**TriggerEnum**](#TriggerEnum) | The name of the trigger that caused the action. |  [optional] |
|**visible** | **Boolean** | Bool of representing whether the action is visible. |  [optional] [readonly] |



## Enum: FromStateEnum

| Name | Value |
|---- | -----|
| INITIAL | &quot;initial&quot; |
| IN_PROGRESS | &quot;in_progress&quot; |
| APPROVED | &quot;approved&quot; |
| PENDING_MODERATION | &quot;pending_moderation&quot; |



## Enum: ToStateEnum

| Name | Value |
|---- | -----|
| IN_PROGRESS | &quot;in_progress&quot; |
| APPROVED | &quot;approved&quot; |
| PENDING_MODERATION | &quot;pending_moderation&quot; |



## Enum: TriggerEnum

| Name | Value |
|---- | -----|
| SUBMIT | &quot;submit&quot; |
| APPROVE | &quot;approve&quot; |
| ACCEPT | &quot;accept&quot; |
| ADMIN_REJECT | &quot;admin_reject&quot; |
| MODERATOR_REJECT | &quot;moderator_reject&quot; |



