

# GoogleCloudFunctionsV2Stage

Each Stage of the deployment process

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**message** | **String** | Message describing the Stage |  [optional] |
|**name** | [**NameEnum**](#NameEnum) | Name of the Stage. This will be unique for each Stage. |  [optional] |
|**resource** | **String** | Resource of the Stage |  [optional] |
|**resourceUri** | **String** | Link to the current Stage resource |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | Current state of the Stage |  [optional] |
|**stateMessages** | [**List&lt;GoogleCloudFunctionsV2StateMessage&gt;**](GoogleCloudFunctionsV2StateMessage.md) | State messages from the current Stage. |  [optional] |



## Enum: NameEnum

| Name | Value |
|---- | -----|
| NAME_UNSPECIFIED | &quot;NAME_UNSPECIFIED&quot; |
| ARTIFACT_REGISTRY | &quot;ARTIFACT_REGISTRY&quot; |
| BUILD | &quot;BUILD&quot; |
| SERVICE | &quot;SERVICE&quot; |
| TRIGGER | &quot;TRIGGER&quot; |
| SERVICE_ROLLBACK | &quot;SERVICE_ROLLBACK&quot; |
| TRIGGER_ROLLBACK | &quot;TRIGGER_ROLLBACK&quot; |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| NOT_STARTED | &quot;NOT_STARTED&quot; |
| IN_PROGRESS | &quot;IN_PROGRESS&quot; |
| COMPLETE | &quot;COMPLETE&quot; |



