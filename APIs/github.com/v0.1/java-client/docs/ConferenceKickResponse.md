

# ConferenceKickResponse


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**members** | **List&lt;String&gt;** | List of affected members |  [optional] |
|**message** | [**MessageEnum**](#MessageEnum) | Response message |  |
|**success** | **Boolean** | Whether the request was successful or not |  |



## Enum: MessageEnum

| Name | Value |
|---- | -----|
| CONFERENCE_KICK_EXECUTED | &quot;Conference Kick Executed&quot; |
| CONFERENCE_NAME_PARAMETER_MUST_BE_PRESENT | &quot;ConferenceName Parameter must be present&quot; |
| MEMBER_ID_PARAMETER_MUST_BE_PRESENT | &quot;MemberID Parameter must be present&quot; |
| CONFERENCE_KICK_FAILED_CONFERENCE_NOT_FOUND | &quot;Conference Kick Failed -- Conference not found&quot; |



