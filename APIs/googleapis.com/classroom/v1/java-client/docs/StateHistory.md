

# StateHistory

The history of each state this submission has been in.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**actorUserId** | **String** | The teacher or student who made the change. |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | The workflow pipeline stage. |  [optional] |
|**stateTimestamp** | **String** | When the submission entered this state. |  [optional] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| CREATED | &quot;CREATED&quot; |
| TURNED_IN | &quot;TURNED_IN&quot; |
| RETURNED | &quot;RETURNED&quot; |
| RECLAIMED_BY_STUDENT | &quot;RECLAIMED_BY_STUDENT&quot; |
| STUDENT_EDITED_AFTER_TURN_IN | &quot;STUDENT_EDITED_AFTER_TURN_IN&quot; |



