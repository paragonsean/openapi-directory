

# AlertingBugtracker

Alerting bugtracker resource

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**eventTypes** | [**List&lt;EventTypesEnum&gt;**](#List&lt;EventTypesEnum&gt;) | Event types enabled for bugtracker |  [optional] |
|**settings** | [**BugtrackerGetSettings200ResponseSettings**](BugtrackerGetSettings200ResponseSettings.md) |  |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | bugtracker state |  [optional] |
|**tokenId** | **String** | ID of OAuth token |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | type of bugtracker |  [optional] |



## Enum: List&lt;EventTypesEnum&gt;

| Name | Value |
|---- | -----|
| NEW_CRASH_GROUP_CREATED | &quot;newCrashGroupCreated&quot; |
| NEW_APP_RELEASED | &quot;newAppReleased&quot; |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| ENABLED | &quot;enabled&quot; |
| DISABLED | &quot;disabled&quot; |
| UNAUTHORIZED | &quot;unauthorized&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| GITHUB | &quot;github&quot; |
| VSTS | &quot;vsts&quot; |
| JIRA | &quot;jira&quot; |



