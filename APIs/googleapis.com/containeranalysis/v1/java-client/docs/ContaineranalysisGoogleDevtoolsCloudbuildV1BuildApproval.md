

# ContaineranalysisGoogleDevtoolsCloudbuildV1BuildApproval

BuildApproval describes a build's approval configuration, state, and result.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**config** | [**ContaineranalysisGoogleDevtoolsCloudbuildV1ApprovalConfig**](ContaineranalysisGoogleDevtoolsCloudbuildV1ApprovalConfig.md) |  |  [optional] |
|**result** | [**ContaineranalysisGoogleDevtoolsCloudbuildV1ApprovalResult**](ContaineranalysisGoogleDevtoolsCloudbuildV1ApprovalResult.md) |  |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | Output only. The state of this build&#39;s approval. |  [optional] [readonly] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| PENDING | &quot;PENDING&quot; |
| APPROVED | &quot;APPROVED&quot; |
| REJECTED | &quot;REJECTED&quot; |
| CANCELLED | &quot;CANCELLED&quot; |



