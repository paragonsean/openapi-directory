

# Session

A representation of a session.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createTime** | **String** | Output only. The time when the session was created. |  [optional] [readonly] |
|**creator** | **String** | Output only. The email address of the user who created the session. |  [optional] [readonly] |
|**environmentConfig** | [**EnvironmentConfig**](EnvironmentConfig.md) |  |  [optional] |
|**jupyterSession** | [**JupyterConfig**](JupyterConfig.md) |  |  [optional] |
|**labels** | **Map&lt;String, String&gt;** | Optional. The labels to associate with the session. Label keys must contain 1 to 63 characters, and must conform to RFC 1035 (https://www.ietf.org/rfc/rfc1035.txt). Label values may be empty, but, if present, must contain 1 to 63 characters, and must conform to RFC 1035 (https://www.ietf.org/rfc/rfc1035.txt). No more than 32 labels can be associated with a session. |  [optional] |
|**name** | **String** | Required. The resource name of the session. |  [optional] |
|**runtimeConfig** | [**RuntimeConfig**](RuntimeConfig.md) |  |  [optional] |
|**runtimeInfo** | [**RuntimeInfo**](RuntimeInfo.md) |  |  [optional] |
|**sessionTemplate** | **String** | Optional. The session template used by the session.Only resource names, including project ID and location, are valid.Example: * https://www.googleapis.com/compute/v1/projects/[project_id]/locations/[dataproc_region]/sessionTemplates/[template_id] * projects/[project_id]/locations/[dataproc_region]/sessionTemplates/[template_id]The template must be in the same project and Dataproc region as the session. |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | Output only. A state of the session. |  [optional] [readonly] |
|**stateHistory** | [**List&lt;SessionStateHistory&gt;**](SessionStateHistory.md) | Output only. Historical state information for the session. |  [optional] [readonly] |
|**stateMessage** | **String** | Output only. Session state details, such as the failure description if the state is FAILED. |  [optional] [readonly] |
|**stateTime** | **String** | Output only. The time when the session entered the current state. |  [optional] [readonly] |
|**user** | **String** | Optional. The email address of the user who owns the session. |  [optional] |
|**uuid** | **String** | Output only. A session UUID (Unique Universal Identifier). The service generates this value when it creates the session. |  [optional] [readonly] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| CREATING | &quot;CREATING&quot; |
| ACTIVE | &quot;ACTIVE&quot; |
| TERMINATING | &quot;TERMINATING&quot; |
| TERMINATED | &quot;TERMINATED&quot; |
| FAILED | &quot;FAILED&quot; |



