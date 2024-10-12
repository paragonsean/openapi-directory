

# ConferenceListMembersResponse


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**_list** | **Object** | List of established conferences |  |
|**message** | [**MessageEnum**](#MessageEnum) | Response message |  |
|**success** | **Boolean** | Whether the request was successful or not |  |



## Enum: MessageEnum

| Name | Value |
|---- | -----|
| CONFERENCE_LIST_MEMBERS_EXECUTED | &quot;Conference ListMembers Executed&quot; |
| CONFERENCE_NAME_PARAMETER_MUST_BE_PRESENT | &quot;ConferenceName Parameter must be present&quot; |
| CONFERENCE_LIST_MEMBERS_FAILED_TO_PARSE_RESULT | &quot;Conference ListMembers Failed to parse result&quot; |
| CONFERENCE_LIST_MEMBERS_FAILED_CONFERENCE_NOT_FOUND | &quot;Conference ListMembers Failed -- Conference not found&quot; |



