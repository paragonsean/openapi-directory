# ContactCenterAiInsightsApi.GoogleCloudContactcenterinsightsV1alpha1IssueModel

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createTime** | **String** | Output only. The time at which this issue model was created. | [optional] [readonly] 
**displayName** | **String** | The representative name for the issue model. | [optional] 
**inputDataConfig** | [**GoogleCloudContactcenterinsightsV1alpha1IssueModelInputDataConfig**](GoogleCloudContactcenterinsightsV1alpha1IssueModelInputDataConfig.md) |  | [optional] 
**issueCount** | **String** | Output only. Number of issues in this issue model. | [optional] [readonly] 
**languageCode** | **String** | Language of the model. | [optional] 
**modelType** | **String** | Type of the model. | [optional] 
**name** | **String** | Immutable. The resource name of the issue model. Format: projects/{project}/locations/{location}/issueModels/{issue_model} | [optional] 
**state** | **String** | Output only. State of the model. | [optional] [readonly] 
**trainingStats** | [**GoogleCloudContactcenterinsightsV1alpha1IssueModelLabelStats**](GoogleCloudContactcenterinsightsV1alpha1IssueModelLabelStats.md) |  | [optional] 
**updateTime** | **String** | Output only. The most recent time at which the issue model was updated. | [optional] [readonly] 



## Enum: ModelTypeEnum


* `MODEL_TYPE_UNSPECIFIED` (value: `"MODEL_TYPE_UNSPECIFIED"`)

* `TYPE_V1` (value: `"TYPE_V1"`)

* `TYPE_V2` (value: `"TYPE_V2"`)





## Enum: StateEnum


* `STATE_UNSPECIFIED` (value: `"STATE_UNSPECIFIED"`)

* `UNDEPLOYED` (value: `"UNDEPLOYED"`)

* `DEPLOYING` (value: `"DEPLOYING"`)

* `DEPLOYED` (value: `"DEPLOYED"`)

* `UNDEPLOYING` (value: `"UNDEPLOYING"`)

* `DELETING` (value: `"DELETING"`)




