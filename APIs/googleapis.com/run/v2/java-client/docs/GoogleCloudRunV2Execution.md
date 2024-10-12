

# GoogleCloudRunV2Execution

Execution represents the configuration of a single execution. A execution an immutable resource that references a container image which is run to completion.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**annotations** | **Map&lt;String, String&gt;** | Output only. Unstructured key value map that may be set by external tools to store and arbitrary metadata. They are not queryable and should be preserved when modifying objects. |  [optional] [readonly] |
|**cancelledCount** | **Integer** | Output only. The number of tasks which reached phase Cancelled. |  [optional] [readonly] |
|**completionTime** | **String** | Output only. Represents time when the execution was completed. It is not guaranteed to be set in happens-before order across separate operations. |  [optional] [readonly] |
|**conditions** | [**List&lt;GoogleCloudRunV2Condition&gt;**](GoogleCloudRunV2Condition.md) | Output only. The Condition of this Execution, containing its readiness status, and detailed error information in case it did not reach the desired state. |  [optional] [readonly] |
|**createTime** | **String** | Output only. Represents time when the execution was acknowledged by the execution controller. It is not guaranteed to be set in happens-before order across separate operations. |  [optional] [readonly] |
|**deleteTime** | **String** | Output only. For a deleted resource, the deletion time. It is only populated as a response to a Delete request. |  [optional] [readonly] |
|**etag** | **String** | Output only. A system-generated fingerprint for this version of the resource. May be used to detect modification conflict during updates. |  [optional] [readonly] |
|**expireTime** | **String** | Output only. For a deleted resource, the time after which it will be permamently deleted. It is only populated as a response to a Delete request. |  [optional] [readonly] |
|**failedCount** | **Integer** | Output only. The number of tasks which reached phase Failed. |  [optional] [readonly] |
|**generation** | **String** | Output only. A number that monotonically increases every time the user modifies the desired state. |  [optional] [readonly] |
|**job** | **String** | Output only. The name of the parent Job. |  [optional] [readonly] |
|**labels** | **Map&lt;String, String&gt;** | Output only. Unstructured key value map that can be used to organize and categorize objects. User-provided labels are shared with Google&#39;s billing system, so they can be used to filter, or break down billing charges by team, component, environment, state, etc. For more information, visit https://cloud.google.com/resource-manager/docs/creating-managing-labels or https://cloud.google.com/run/docs/configuring/labels |  [optional] [readonly] |
|**launchStage** | [**LaunchStageEnum**](#LaunchStageEnum) | The least stable launch stage needed to create this resource, as defined by [Google Cloud Platform Launch Stages](https://cloud.google.com/terms/launch-stages). Cloud Run supports &#x60;ALPHA&#x60;, &#x60;BETA&#x60;, and &#x60;GA&#x60;. Note that this value might not be what was used as input. For example, if ALPHA was provided as input in the parent resource, but only BETA and GA-level features are were, this field will be BETA. |  [optional] |
|**logUri** | **String** | Output only. URI where logs for this execution can be found in Cloud Console. |  [optional] [readonly] |
|**name** | **String** | Output only. The unique name of this Execution. |  [optional] [readonly] |
|**observedGeneration** | **String** | Output only. The generation of this Execution. See comments in &#x60;reconciling&#x60; for additional information on reconciliation process in Cloud Run. |  [optional] [readonly] |
|**parallelism** | **Integer** | Output only. Specifies the maximum desired number of tasks the execution should run at any given time. Must be &lt;&#x3D; task_count. The actual number of tasks running in steady state will be less than this number when ((.spec.task_count - .status.successful) &lt; .spec.parallelism), i.e. when the work left to do is less than max parallelism. |  [optional] [readonly] |
|**reconciling** | **Boolean** | Output only. Indicates whether the resource&#39;s reconciliation is still in progress. See comments in &#x60;Job.reconciling&#x60; for additional information on reconciliation process in Cloud Run. |  [optional] [readonly] |
|**retriedCount** | **Integer** | Output only. The number of tasks which have retried at least once. |  [optional] [readonly] |
|**runningCount** | **Integer** | Output only. The number of actively running tasks. |  [optional] [readonly] |
|**satisfiesPzs** | **Boolean** | Output only. Reserved for future use. |  [optional] [readonly] |
|**startTime** | **String** | Output only. Represents time when the execution started to run. It is not guaranteed to be set in happens-before order across separate operations. |  [optional] [readonly] |
|**succeededCount** | **Integer** | Output only. The number of tasks which reached phase Succeeded. |  [optional] [readonly] |
|**taskCount** | **Integer** | Output only. Specifies the desired number of tasks the execution should run. Setting to 1 means that parallelism is limited to 1 and the success of that task signals the success of the execution. |  [optional] [readonly] |
|**template** | [**GoogleCloudRunV2TaskTemplate**](GoogleCloudRunV2TaskTemplate.md) |  |  [optional] |
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



