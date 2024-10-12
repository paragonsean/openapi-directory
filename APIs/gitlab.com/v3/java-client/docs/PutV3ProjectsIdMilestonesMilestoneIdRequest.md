

# PutV3ProjectsIdMilestonesMilestoneIdRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**title** | **String** | The title of the milestone |  [optional] |
|**stateEvent** | [**StateEventEnum**](#StateEventEnum) | The state event of the milestone  |  [optional] |
|**description** | **String** | The description of the milestone |  [optional] |
|**dueDate** | **String** | The due date of the milestone. The ISO 8601 date format (%Y-%m-%d) |  [optional] |
|**startDate** | **String** | The start date of the milestone. The ISO 8601 date format (%Y-%m-%d) |  [optional] |



## Enum: StateEventEnum

| Name | Value |
|---- | -----|
| CLOSE | &quot;close&quot; |
| ACTIVATE | &quot;activate&quot; |



