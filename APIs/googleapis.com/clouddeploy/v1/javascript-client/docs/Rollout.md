# CloudDeployApi.Rollout

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**annotations** | **{String: String}** | User annotations. These attributes can only be set and used by the user, and not by Cloud Deploy. See https://google.aip.dev/128#annotations for more details such as format and size limitations. | [optional] 
**approvalState** | **String** | Output only. Approval state of the &#x60;Rollout&#x60;. | [optional] [readonly] 
**approveTime** | **String** | Output only. Time at which the &#x60;Rollout&#x60; was approved. | [optional] [readonly] 
**controllerRollout** | **String** | Output only. Name of the &#x60;ControllerRollout&#x60;. Format is &#x60;projects/{project}/locations/{location}/deliveryPipelines/{deliveryPipeline}/releases/{release}/rollouts/a-z{0,62}&#x60;. | [optional] [readonly] 
**createTime** | **String** | Output only. Time at which the &#x60;Rollout&#x60; was created. | [optional] [readonly] 
**deployEndTime** | **String** | Output only. Time at which the &#x60;Rollout&#x60; finished deploying. | [optional] [readonly] 
**deployFailureCause** | **String** | Output only. The reason this rollout failed. This will always be unspecified while the rollout is in progress. | [optional] [readonly] 
**deployStartTime** | **String** | Output only. Time at which the &#x60;Rollout&#x60; started deploying. | [optional] [readonly] 
**deployingBuild** | **String** | Output only. The resource name of the Cloud Build &#x60;Build&#x60; object that is used to deploy the Rollout. Format is &#x60;projects/{project}/locations/{location}/builds/{build}&#x60;. | [optional] [readonly] 
**description** | **String** | Description of the &#x60;Rollout&#x60; for user purposes. Max length is 255 characters. | [optional] 
**enqueueTime** | **String** | Output only. Time at which the &#x60;Rollout&#x60; was enqueued. | [optional] [readonly] 
**etag** | **String** | This checksum is computed by the server based on the value of other fields, and may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding. | [optional] 
**failureReason** | **String** | Output only. Additional information about the rollout failure, if available. | [optional] [readonly] 
**labels** | **{String: String}** | Labels are attributes that can be set and used by both the user and by Cloud Deploy. Labels must meet the following constraints: * Keys and values can contain only lowercase letters, numeric characters, underscores, and dashes. * All characters must use UTF-8 encoding, and international characters are allowed. * Keys must start with a lowercase letter or international character. * Each resource is limited to a maximum of 64 labels. Both keys and values are additionally constrained to be &lt;&#x3D; 128 bytes. | [optional] 
**metadata** | [**Metadata**](Metadata.md) |  | [optional] 
**name** | **String** | Optional. Name of the &#x60;Rollout&#x60;. Format is &#x60;projects/{project}/locations/{location}/deliveryPipelines/{deliveryPipeline}/releases/{release}/rollouts/a-z{0,62}&#x60;. | [optional] 
**phases** | [**[Phase]**](Phase.md) | Output only. The phases that represent the workflows of this &#x60;Rollout&#x60;. | [optional] [readonly] 
**rollbackOfRollout** | **String** | Output only. Name of the &#x60;Rollout&#x60; that is rolled back by this &#x60;Rollout&#x60;. Empty if this &#x60;Rollout&#x60; wasn&#39;t created as a rollback. | [optional] [readonly] 
**rolledBackByRollouts** | **[String]** | Output only. Names of &#x60;Rollouts&#x60; that rolled back this &#x60;Rollout&#x60;. | [optional] [readonly] 
**state** | **String** | Output only. Current state of the &#x60;Rollout&#x60;. | [optional] [readonly] 
**targetId** | **String** | Required. The ID of Target to which this &#x60;Rollout&#x60; is deploying. | [optional] 
**uid** | **String** | Output only. Unique identifier of the &#x60;Rollout&#x60;. | [optional] [readonly] 



## Enum: ApprovalStateEnum


* `APPROVAL_STATE_UNSPECIFIED` (value: `"APPROVAL_STATE_UNSPECIFIED"`)

* `NEEDS_APPROVAL` (value: `"NEEDS_APPROVAL"`)

* `DOES_NOT_NEED_APPROVAL` (value: `"DOES_NOT_NEED_APPROVAL"`)

* `APPROVED` (value: `"APPROVED"`)

* `REJECTED` (value: `"REJECTED"`)





## Enum: DeployFailureCauseEnum


* `FAILURE_CAUSE_UNSPECIFIED` (value: `"FAILURE_CAUSE_UNSPECIFIED"`)

* `CLOUD_BUILD_UNAVAILABLE` (value: `"CLOUD_BUILD_UNAVAILABLE"`)

* `EXECUTION_FAILED` (value: `"EXECUTION_FAILED"`)

* `DEADLINE_EXCEEDED` (value: `"DEADLINE_EXCEEDED"`)

* `RELEASE_FAILED` (value: `"RELEASE_FAILED"`)

* `RELEASE_ABANDONED` (value: `"RELEASE_ABANDONED"`)

* `VERIFICATION_CONFIG_NOT_FOUND` (value: `"VERIFICATION_CONFIG_NOT_FOUND"`)

* `CLOUD_BUILD_REQUEST_FAILED` (value: `"CLOUD_BUILD_REQUEST_FAILED"`)

* `OPERATION_FEATURE_NOT_SUPPORTED` (value: `"OPERATION_FEATURE_NOT_SUPPORTED"`)





## Enum: StateEnum


* `STATE_UNSPECIFIED` (value: `"STATE_UNSPECIFIED"`)

* `SUCCEEDED` (value: `"SUCCEEDED"`)

* `FAILED` (value: `"FAILED"`)

* `IN_PROGRESS` (value: `"IN_PROGRESS"`)

* `PENDING_APPROVAL` (value: `"PENDING_APPROVAL"`)

* `APPROVAL_REJECTED` (value: `"APPROVAL_REJECTED"`)

* `PENDING` (value: `"PENDING"`)

* `PENDING_RELEASE` (value: `"PENDING_RELEASE"`)

* `CANCELLING` (value: `"CANCELLING"`)

* `CANCELLED` (value: `"CANCELLED"`)

* `HALTED` (value: `"HALTED"`)




