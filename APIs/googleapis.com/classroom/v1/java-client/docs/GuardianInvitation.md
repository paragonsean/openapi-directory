

# GuardianInvitation

An invitation to become the guardian of a specified user, sent to a specified email address.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**creationTime** | **String** | The time that this invitation was created. Read-only. |  [optional] |
|**invitationId** | **String** | Unique identifier for this invitation. Read-only. |  [optional] |
|**invitedEmailAddress** | **String** | Email address that the invitation was sent to. This field is only visible to domain administrators. |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | The state that this invitation is in. |  [optional] |
|**studentId** | **String** | ID of the student (in standard format) |  [optional] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| GUARDIAN_INVITATION_STATE_UNSPECIFIED | &quot;GUARDIAN_INVITATION_STATE_UNSPECIFIED&quot; |
| PENDING | &quot;PENDING&quot; |
| COMPLETE | &quot;COMPLETE&quot; |



