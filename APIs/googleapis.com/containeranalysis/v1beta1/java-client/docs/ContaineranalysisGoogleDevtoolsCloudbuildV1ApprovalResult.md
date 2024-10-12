

# ContaineranalysisGoogleDevtoolsCloudbuildV1ApprovalResult

ApprovalResult describes the decision and associated metadata of a manual approval of a build.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**approvalTime** | **String** | Output only. The time when the approval decision was made. |  [optional] [readonly] |
|**approverAccount** | **String** | Output only. Email of the user that called the ApproveBuild API to approve or reject a build at the time that the API was called. |  [optional] [readonly] |
|**comment** | **String** | Optional. An optional comment for this manual approval result. |  [optional] |
|**decision** | [**DecisionEnum**](#DecisionEnum) | Required. The decision of this manual approval. |  [optional] |
|**url** | **String** | Optional. An optional URL tied to this manual approval result. This field is essentially the same as comment, except that it will be rendered by the UI differently. An example use case is a link to an external job that approved this Build. |  [optional] |



## Enum: DecisionEnum

| Name | Value |
|---- | -----|
| DECISION_UNSPECIFIED | &quot;DECISION_UNSPECIFIED&quot; |
| APPROVED | &quot;APPROVED&quot; |
| REJECTED | &quot;REJECTED&quot; |



