

# GoogleCloudAiplatformV1Study

A message representing a Study.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createTime** | **String** | Output only. Time at which the study was created. |  [optional] [readonly] |
|**displayName** | **String** | Required. Describes the Study, default value is empty string. |  [optional] |
|**inactiveReason** | **String** | Output only. A human readable reason why the Study is inactive. This should be empty if a study is ACTIVE or COMPLETED. |  [optional] [readonly] |
|**name** | **String** | Output only. The name of a study. The study&#39;s globally unique identifier. Format: &#x60;projects/{project}/locations/{location}/studies/{study}&#x60; |  [optional] [readonly] |
|**state** | [**StateEnum**](#StateEnum) | Output only. The detailed state of a Study. |  [optional] [readonly] |
|**studySpec** | [**GoogleCloudAiplatformV1StudySpec**](GoogleCloudAiplatformV1StudySpec.md) |  |  [optional] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| ACTIVE | &quot;ACTIVE&quot; |
| INACTIVE | &quot;INACTIVE&quot; |
| COMPLETED | &quot;COMPLETED&quot; |



