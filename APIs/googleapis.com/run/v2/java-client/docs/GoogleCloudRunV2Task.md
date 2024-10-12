

# GoogleCloudRunV2Task

Task represents a single run of a container to completion.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**annotations** | **Map&lt;String, String&gt;** | Output only. Unstructured key value map that may be set by external tools to store and arbitrary metadata. They are not queryable and should be preserved when modifying objects. |  [optional] [readonly] |
|**completionTime** | **String** | Output only. Represents time when the Task was completed. It is not guaranteed to be set in happens-before order across separate operations. |  [optional] [readonly] |
|**conditions** | [**List&lt;GoogleCloudRunV2Condition&gt;**](GoogleCloudRunV2Condition.md) | Output only. The Condition of this Task, containing its readiness status, and detailed error information in case it did not reach the desired state. |  [optional] [readonly] |
|**containers** | [**List&lt;GoogleCloudRunV2Container&gt;**](GoogleCloudRunV2Container.md) | Holds the single container that defines the unit of execution for this task. |  [optional] |
|**createTime** | **String** | Output only. Represents time when the task was created by the system. It is not guaranteed to be set in happens-before order across separate operations. |  [optional] [readonly] |
|**deleteTime** | **String** | Output only. For a deleted resource, the deletion time. It is only populated as a response to a Delete request. |  [optional] [readonly] |
|**encryptionKey** | **String** | Output only. A reference to a customer managed encryption key (CMEK) to use to encrypt this container image. For more information, go to https://cloud.google.com/run/docs/securing/using-cmek |  [optional] [readonly] |
|**etag** | **String** | Output only. A system-generated fingerprint for this version of the resource. May be used to detect modification conflict during updates. |  [optional] [readonly] |
|**execution** | **String** | Output only. The name of the parent Execution. |  [optional] [readonly] |
|**executionEnvironment** | [**ExecutionEnvironmentEnum**](#ExecutionEnvironmentEnum) | The execution environment being used to host this Task. |  [optional] |
|**expireTime** | **String** | Output only. For a deleted resource, the time after which it will be permamently deleted. It is only populated as a response to a Delete request. |  [optional] [readonly] |
|**generation** | **String** | Output only. A number that monotonically increases every time the user modifies the desired state. |  [optional] [readonly] |
|**index** | **Integer** | Output only. Index of the Task, unique per execution, and beginning at 0. |  [optional] [readonly] |
|**job** | **String** | Output only. The name of the parent Job. |  [optional] [readonly] |
|**labels** | **Map&lt;String, String&gt;** | Output only. Unstructured key value map that can be used to organize and categorize objects. User-provided labels are shared with Google&#39;s billing system, so they can be used to filter, or break down billing charges by team, component, environment, state, etc. For more information, visit https://cloud.google.com/resource-manager/docs/creating-managing-labels or https://cloud.google.com/run/docs/configuring/labels |  [optional] [readonly] |
|**lastAttemptResult** | [**GoogleCloudRunV2TaskAttemptResult**](GoogleCloudRunV2TaskAttemptResult.md) |  |  [optional] |
|**logUri** | **String** | Output only. URI where logs for this execution can be found in Cloud Console. |  [optional] [readonly] |
|**maxRetries** | **Integer** | Number of retries allowed per Task, before marking this Task failed. |  [optional] |
|**name** | **String** | Output only. The unique name of this Task. |  [optional] [readonly] |
|**observedGeneration** | **String** | Output only. The generation of this Task. See comments in &#x60;Job.reconciling&#x60; for additional information on reconciliation process in Cloud Run. |  [optional] [readonly] |
|**reconciling** | **Boolean** | Output only. Indicates whether the resource&#39;s reconciliation is still in progress. See comments in &#x60;Job.reconciling&#x60; for additional information on reconciliation process in Cloud Run. |  [optional] [readonly] |
|**retried** | **Integer** | Output only. The number of times this Task was retried. Tasks are retried when they fail up to the maxRetries limit. |  [optional] [readonly] |
|**satisfiesPzs** | **Boolean** | Output only. Reserved for future use. |  [optional] [readonly] |
|**scheduledTime** | **String** | Output only. Represents time when the task was scheduled to run by the system. It is not guaranteed to be set in happens-before order across separate operations. |  [optional] [readonly] |
|**serviceAccount** | **String** | Email address of the IAM service account associated with the Task of a Job. The service account represents the identity of the running task, and determines what permissions the task has. If not provided, the task will use the project&#39;s default service account. |  [optional] |
|**startTime** | **String** | Output only. Represents time when the task started to run. It is not guaranteed to be set in happens-before order across separate operations. |  [optional] [readonly] |
|**timeout** | **String** | Max allowed time duration the Task may be active before the system will actively try to mark it failed and kill associated containers. This applies per attempt of a task, meaning each retry can run for the full timeout. |  [optional] |
|**uid** | **String** | Output only. Server assigned unique identifier for the Task. The value is a UUID4 string and guaranteed to remain unchanged until the resource is deleted. |  [optional] [readonly] |
|**updateTime** | **String** | Output only. The last-modified time. |  [optional] [readonly] |
|**volumes** | [**List&lt;GoogleCloudRunV2Volume&gt;**](GoogleCloudRunV2Volume.md) | A list of Volumes to make available to containers. |  [optional] |
|**vpcAccess** | [**GoogleCloudRunV2VpcAccess**](GoogleCloudRunV2VpcAccess.md) |  |  [optional] |



## Enum: ExecutionEnvironmentEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;EXECUTION_ENVIRONMENT_UNSPECIFIED&quot; |
| GEN1 | &quot;EXECUTION_ENVIRONMENT_GEN1&quot; |
| GEN2 | &quot;EXECUTION_ENVIRONMENT_GEN2&quot; |



