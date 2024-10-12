

# GoogleCloudRunV2Job

Job represents the configuration of a single job, which references a container image that is run to completion.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**annotations** | **Map&lt;String, String&gt;** | Unstructured key value map that may be set by external tools to store and arbitrary metadata. They are not queryable and should be preserved when modifying objects. Cloud Run API v2 does not support annotations with &#x60;run.googleapis.com&#x60;, &#x60;cloud.googleapis.com&#x60;, &#x60;serving.knative.dev&#x60;, or &#x60;autoscaling.knative.dev&#x60; namespaces, and they will be rejected on new resources. All system annotations in v1 now have a corresponding field in v2 Job. This field follows Kubernetes annotations&#39; namespacing, limits, and rules. |  [optional] |
|**binaryAuthorization** | [**GoogleCloudRunV2BinaryAuthorization**](GoogleCloudRunV2BinaryAuthorization.md) |  |  [optional] |
|**client** | **String** | Arbitrary identifier for the API client. |  [optional] |
|**clientVersion** | **String** | Arbitrary version identifier for the API client. |  [optional] |
|**conditions** | [**List&lt;GoogleCloudRunV2Condition&gt;**](GoogleCloudRunV2Condition.md) | Output only. The Conditions of all other associated sub-resources. They contain additional diagnostics information in case the Job does not reach its desired state. See comments in &#x60;reconciling&#x60; for additional information on reconciliation process in Cloud Run. |  [optional] [readonly] |
|**createTime** | **String** | Output only. The creation time. |  [optional] [readonly] |
|**creator** | **String** | Output only. Email address of the authenticated creator. |  [optional] [readonly] |
|**deleteTime** | **String** | Output only. The deletion time. |  [optional] [readonly] |
|**etag** | **String** | Output only. A system-generated fingerprint for this version of the resource. May be used to detect modification conflict during updates. |  [optional] [readonly] |
|**executionCount** | **Integer** | Output only. Number of executions created for this job. |  [optional] [readonly] |
|**expireTime** | **String** | Output only. For a deleted resource, the time after which it will be permamently deleted. |  [optional] [readonly] |
|**generation** | **String** | Output only. A number that monotonically increases every time the user modifies the desired state. |  [optional] [readonly] |
|**labels** | **Map&lt;String, String&gt;** | Unstructured key value map that can be used to organize and categorize objects. User-provided labels are shared with Google&#39;s billing system, so they can be used to filter, or break down billing charges by team, component, environment, state, etc. For more information, visit https://cloud.google.com/resource-manager/docs/creating-managing-labels or https://cloud.google.com/run/docs/configuring/labels. Cloud Run API v2 does not support labels with &#x60;run.googleapis.com&#x60;, &#x60;cloud.googleapis.com&#x60;, &#x60;serving.knative.dev&#x60;, or &#x60;autoscaling.knative.dev&#x60; namespaces, and they will be rejected. All system labels in v1 now have a corresponding field in v2 Job. |  [optional] |
|**lastModifier** | **String** | Output only. Email address of the last authenticated modifier. |  [optional] [readonly] |
|**latestCreatedExecution** | [**GoogleCloudRunV2ExecutionReference**](GoogleCloudRunV2ExecutionReference.md) |  |  [optional] |
|**launchStage** | [**LaunchStageEnum**](#LaunchStageEnum) | The launch stage as defined by [Google Cloud Platform Launch Stages](https://cloud.google.com/terms/launch-stages). Cloud Run supports &#x60;ALPHA&#x60;, &#x60;BETA&#x60;, and &#x60;GA&#x60;. If no value is specified, GA is assumed. Set the launch stage to a preview stage on input to allow use of preview features in that stage. On read (or output), describes whether the resource uses preview features. For example, if ALPHA is provided as input, but only BETA and GA-level features are used, this field will be BETA on output. |  [optional] |
|**name** | **String** | The fully qualified name of this Job. Format: projects/{project}/locations/{location}/jobs/{job} |  [optional] |
|**observedGeneration** | **String** | Output only. The generation of this Job. See comments in &#x60;reconciling&#x60; for additional information on reconciliation process in Cloud Run. |  [optional] [readonly] |
|**reconciling** | **Boolean** | Output only. Returns true if the Job is currently being acted upon by the system to bring it into the desired state. When a new Job is created, or an existing one is updated, Cloud Run will asynchronously perform all necessary steps to bring the Job to the desired state. This process is called reconciliation. While reconciliation is in process, &#x60;observed_generation&#x60; and &#x60;latest_succeeded_execution&#x60;, will have transient values that might mismatch the intended state: Once reconciliation is over (and this field is false), there are two possible outcomes: reconciliation succeeded and the state matches the Job, or there was an error, and reconciliation failed. This state can be found in &#x60;terminal_condition.state&#x60;. If reconciliation succeeded, the following fields will match: &#x60;observed_generation&#x60; and &#x60;generation&#x60;, &#x60;latest_succeeded_execution&#x60; and &#x60;latest_created_execution&#x60;. If reconciliation failed, &#x60;observed_generation&#x60; and &#x60;latest_succeeded_execution&#x60; will have the state of the last succeeded execution or empty for newly created Job. Additional information on the failure can be found in &#x60;terminal_condition&#x60; and &#x60;conditions&#x60;. |  [optional] [readonly] |
|**satisfiesPzs** | **Boolean** | Output only. Reserved for future use. |  [optional] [readonly] |
|**template** | [**GoogleCloudRunV2ExecutionTemplate**](GoogleCloudRunV2ExecutionTemplate.md) |  |  [optional] |
|**terminalCondition** | [**GoogleCloudRunV2Condition**](GoogleCloudRunV2Condition.md) |  |  [optional] |
|**uid** | **String** | Output only. Server assigned unique identifier for the Execution. The value is a UUID4 string and guaranteed to remain unchanged until the resource is deleted. |  [optional] [readonly] |
|**updateTime** | **String** | Output only. The last-modified time. |  [optional] [readonly] |



## Enum: LaunchStageEnum

| Name | Value |
|---- | -----|
| LAUNCH_STAGE_UNSPECIFIED | &quot;LAUNCH_STAGE_UNSPECIFIED&quot; |
| UNIMPLEMENTED | &quot;UNIMPLEMENTED&quot; |
| PRELAUNCH | &quot;PRELAUNCH&quot; |
| EARLY_ACCESS | &quot;EARLY_ACCESS&quot; |
| ALPHA | &quot;ALPHA&quot; |
| BETA | &quot;BETA&quot; |
| GA | &quot;GA&quot; |
| DEPRECATED | &quot;DEPRECATED&quot; |



