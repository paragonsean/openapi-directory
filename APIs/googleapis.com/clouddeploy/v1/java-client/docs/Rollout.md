

# Rollout

A `Rollout` resource in the Cloud Deploy API. A `Rollout` contains information around a specific deployment to a `Target`.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**annotations** | **Map&lt;String, String&gt;** | User annotations. These attributes can only be set and used by the user, and not by Cloud Deploy. See https://google.aip.dev/128#annotations for more details such as format and size limitations. |  [optional] |
|**approvalState** | [**ApprovalStateEnum**](#ApprovalStateEnum) | Output only. Approval state of the &#x60;Rollout&#x60;. |  [optional] [readonly] |
|**approveTime** | **String** | Output only. Time at which the &#x60;Rollout&#x60; was approved. |  [optional] [readonly] |
|**controllerRollout** | **String** | Output only. Name of the &#x60;ControllerRollout&#x60;. Format is &#x60;projects/{project}/locations/{location}/deliveryPipelines/{deliveryPipeline}/releases/{release}/rollouts/a-z{0,62}&#x60;. |  [optional] [readonly] |
|**createTime** | **String** | Output only. Time at which the &#x60;Rollout&#x60; was created. |  [optional] [readonly] |
|**deployEndTime** | **String** | Output only. Time at which the &#x60;Rollout&#x60; finished deploying. |  [optional] [readonly] |
|**deployFailureCause** | [**DeployFailureCauseEnum**](#DeployFailureCauseEnum) | Output only. The reason this rollout failed. This will always be unspecified while the rollout is in progress. |  [optional] [readonly] |
|**deployStartTime** | **String** | Output only. Time at which the &#x60;Rollout&#x60; started deploying. |  [optional] [readonly] |
|**deployingBuild** | **String** | Output only. The resource name of the Cloud Build &#x60;Build&#x60; object that is used to deploy the Rollout. Format is &#x60;projects/{project}/locations/{location}/builds/{build}&#x60;. |  [optional] [readonly] |
|**description** | **String** | Description of the &#x60;Rollout&#x60; for user purposes. Max length is 255 characters. |  [optional] |
|**enqueueTime** | **String** | Output only. Time at which the &#x60;Rollout&#x60; was enqueued. |  [optional] [readonly] |
|**etag** | **String** | This checksum is computed by the server based on the value of other fields, and may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding. |  [optional] |
|**failureReason** | **String** | Output only. Additional information about the rollout failure, if available. |  [optional] [readonly] |
|**labels** | **Map&lt;String, String&gt;** | Labels are attributes that can be set and used by both the user and by Cloud Deploy. Labels must meet the following constraints: * Keys and values can contain only lowercase letters, numeric characters, underscores, and dashes. * All characters must use UTF-8 encoding, and international characters are allowed. * Keys must start with a lowercase letter or international character. * Each resource is limited to a maximum of 64 labels. Both keys and values are additionally constrained to be &lt;&#x3D; 128 bytes. |  [optional] |
|**metadata** | [**Metadata**](Metadata.md) |  |  [optional] |
|**name** | **String** | Optional. Name of the &#x60;Rollout&#x60;. Format is &#x60;projects/{project}/locations/{location}/deliveryPipelines/{deliveryPipeline}/releases/{release}/rollouts/a-z{0,62}&#x60;. |  [optional] |
|**phases** | [**List&lt;Phase&gt;**](Phase.md) | Output only. The phases that represent the workflows of this &#x60;Rollout&#x60;. |  [optional] [readonly] |
|**rollbackOfRollout** | **String** | Output only. Name of the &#x60;Rollout&#x60; that is rolled back by this &#x60;Rollout&#x60;. Empty if this &#x60;Rollout&#x60; wasn&#39;t created as a rollback. |  [optional] [readonly] |
|**rolledBackByRollouts** | **List&lt;String&gt;** | Output only. Names of &#x60;Rollouts&#x60; that rolled back this &#x60;Rollout&#x60;. |  [optional] [readonly] |
|**state** | [**StateEnum**](#StateEnum) | Output only. Current state of the &#x60;Rollout&#x60;. |  [optional] [readonly] |
|**targetId** | **String** | Required. The ID of Target to which this &#x60;Rollout&#x60; is deploying. |  [optional] |
|**uid** | **String** | Output only. Unique identifier of the &#x60;Rollout&#x60;. |  [optional] [readonly] |



## Enum: ApprovalStateEnum

| Name | Value |
|---- | -----|
| APPROVAL_STATE_UNSPECIFIED | &quot;APPROVAL_STATE_UNSPECIFIED&quot; |
| NEEDS_APPROVAL | &quot;NEEDS_APPROVAL&quot; |
| DOES_NOT_NEED_APPROVAL | &quot;DOES_NOT_NEED_APPROVAL&quot; |
| APPROVED | &quot;APPROVED&quot; |
| REJECTED | &quot;REJECTED&quot; |



## Enum: DeployFailureCauseEnum

| Name | Value |
|---- | -----|
| FAILURE_CAUSE_UNSPECIFIED | &quot;FAILURE_CAUSE_UNSPECIFIED&quot; |
| CLOUD_BUILD_UNAVAILABLE | &quot;CLOUD_BUILD_UNAVAILABLE&quot; |
| EXECUTION_FAILED | &quot;EXECUTION_FAILED&quot; |
| DEADLINE_EXCEEDED | &quot;DEADLINE_EXCEEDED&quot; |
| RELEASE_FAILED | &quot;RELEASE_FAILED&quot; |
| RELEASE_ABANDONED | &quot;RELEASE_ABANDONED&quot; |
| VERIFICATION_CONFIG_NOT_FOUND | &quot;VERIFICATION_CONFIG_NOT_FOUND&quot; |
| CLOUD_BUILD_REQUEST_FAILED | &quot;CLOUD_BUILD_REQUEST_FAILED&quot; |
| OPERATION_FEATURE_NOT_SUPPORTED | &quot;OPERATION_FEATURE_NOT_SUPPORTED&quot; |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| SUCCEEDED | &quot;SUCCEEDED&quot; |
| FAILED | &quot;FAILED&quot; |
| IN_PROGRESS | &quot;IN_PROGRESS&quot; |
| PENDING_APPROVAL | &quot;PENDING_APPROVAL&quot; |
| APPROVAL_REJECTED | &quot;APPROVAL_REJECTED&quot; |
| PENDING | &quot;PENDING&quot; |
| PENDING_RELEASE | &quot;PENDING_RELEASE&quot; |
| CANCELLING | &quot;CANCELLING&quot; |
| CANCELLED | &quot;CANCELLED&quot; |
| HALTED | &quot;HALTED&quot; |



