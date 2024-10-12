

# Participant


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**approved** | **Boolean** |  |  [optional] |
|**participatedOn** | **OffsetDateTime** | The ISO8601 timestamp of the participant&#39;s action. For approvers, this is the time of their approval. For commenters and pull request reviewers who are not approvers, this is the time they last commented, or null if they have not commented. |  [optional] |
|**role** | [**RoleEnum**](#RoleEnum) |  |  [optional] |
|**state** | [**StateEnum**](#StateEnum) |  |  [optional] |
|**user** | [**Account**](Account.md) |  |  [optional] |



## Enum: RoleEnum

| Name | Value |
|---- | -----|
| PARTICIPANT | &quot;PARTICIPANT&quot; |
| REVIEWER | &quot;REVIEWER&quot; |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| APPROVED | &quot;approved&quot; |
| CHANGES_REQUESTED | &quot;changes_requested&quot; |



