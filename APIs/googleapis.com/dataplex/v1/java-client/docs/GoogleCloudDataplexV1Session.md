

# GoogleCloudDataplexV1Session

Represents an active analyze session running for a user.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createTime** | **String** | Output only. Session start time. |  [optional] [readonly] |
|**name** | **String** | Output only. The relative resource name of the content, of the form: projects/{project_id}/locations/{location_id}/lakes/{lake_id}/environment/{environment_id}/sessions/{session_id} |  [optional] [readonly] |
|**state** | [**StateEnum**](#StateEnum) | Output only. State of Session |  [optional] [readonly] |
|**userId** | **String** | Output only. Email of user running the session. |  [optional] [readonly] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| ACTIVE | &quot;ACTIVE&quot; |
| CREATING | &quot;CREATING&quot; |
| DELETING | &quot;DELETING&quot; |
| ACTION_REQUIRED | &quot;ACTION_REQUIRED&quot; |



