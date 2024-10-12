

# GoogleCloudContactcenterinsightsV1IssueModel

The issue model resource.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createTime** | **String** | Output only. The time at which this issue model was created. |  [optional] [readonly] |
|**displayName** | **String** | The representative name for the issue model. |  [optional] |
|**inputDataConfig** | [**GoogleCloudContactcenterinsightsV1IssueModelInputDataConfig**](GoogleCloudContactcenterinsightsV1IssueModelInputDataConfig.md) |  |  [optional] |
|**issueCount** | **String** | Output only. Number of issues in this issue model. |  [optional] [readonly] |
|**languageCode** | **String** | Language of the model. |  [optional] |
|**modelType** | [**ModelTypeEnum**](#ModelTypeEnum) | Type of the model. |  [optional] |
|**name** | **String** | Immutable. The resource name of the issue model. Format: projects/{project}/locations/{location}/issueModels/{issue_model} |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | Output only. State of the model. |  [optional] [readonly] |
|**trainingStats** | [**GoogleCloudContactcenterinsightsV1IssueModelLabelStats**](GoogleCloudContactcenterinsightsV1IssueModelLabelStats.md) |  |  [optional] |
|**updateTime** | **String** | Output only. The most recent time at which the issue model was updated. |  [optional] [readonly] |



## Enum: ModelTypeEnum

| Name | Value |
|---- | -----|
| MODEL_TYPE_UNSPECIFIED | &quot;MODEL_TYPE_UNSPECIFIED&quot; |
| TYPE_V1 | &quot;TYPE_V1&quot; |
| TYPE_V2 | &quot;TYPE_V2&quot; |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| UNDEPLOYED | &quot;UNDEPLOYED&quot; |
| DEPLOYING | &quot;DEPLOYING&quot; |
| DEPLOYED | &quot;DEPLOYED&quot; |
| UNDEPLOYING | &quot;UNDEPLOYING&quot; |
| DELETING | &quot;DELETING&quot; |



