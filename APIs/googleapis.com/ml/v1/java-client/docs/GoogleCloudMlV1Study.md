

# GoogleCloudMlV1Study

A message representing a Study.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createTime** | **String** | Output only. Time at which the study was created. |  [optional] [readonly] |
|**inactiveReason** | **String** | Output only. A human readable reason why the Study is inactive. This should be empty if a study is ACTIVE or COMPLETED. |  [optional] [readonly] |
|**name** | **String** | Output only. The name of a study. |  [optional] [readonly] |
|**state** | [**StateEnum**](#StateEnum) | Output only. The detailed state of a study. |  [optional] [readonly] |
|**studyConfig** | [**GoogleCloudMlV1StudyConfig**](GoogleCloudMlV1StudyConfig.md) |  |  [optional] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| ACTIVE | &quot;ACTIVE&quot; |
| INACTIVE | &quot;INACTIVE&quot; |
| COMPLETED | &quot;COMPLETED&quot; |



