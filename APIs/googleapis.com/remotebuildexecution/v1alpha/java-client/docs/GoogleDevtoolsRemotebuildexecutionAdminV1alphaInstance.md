

# GoogleDevtoolsRemotebuildexecutionAdminV1alphaInstance

Instance conceptually encapsulates all Remote Build Execution resources for remote builds. An instance consists of storage and compute resources (for example, `ContentAddressableStorage`, `ActionCache`, `WorkerPools`) used for running remote builds. All Remote Build Execution API calls are scoped to an instance.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**featurePolicy** | [**GoogleDevtoolsRemotebuildexecutionAdminV1alphaFeaturePolicy**](GoogleDevtoolsRemotebuildexecutionAdminV1alphaFeaturePolicy.md) |  |  [optional] |
|**location** | **String** | The location is a GCP region. Currently only &#x60;us-central1&#x60; is supported. |  [optional] |
|**loggingEnabled** | **Boolean** | Output only. Whether stack driver logging is enabled for the instance. |  [optional] [readonly] |
|**name** | **String** | Output only. Instance resource name formatted as: &#x60;projects/[PROJECT_ID]/instances/[INSTANCE_ID]&#x60;. Name should not be populated when creating an instance since it is provided in the &#x60;instance_id&#x60; field. |  [optional] [readonly] |
|**schedulerNotificationConfig** | [**GoogleDevtoolsRemotebuildexecutionAdminV1alphaSchedulerNotificationConfig**](GoogleDevtoolsRemotebuildexecutionAdminV1alphaSchedulerNotificationConfig.md) |  |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | Output only. State of the instance. |  [optional] [readonly] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| CREATING | &quot;CREATING&quot; |
| RUNNING | &quot;RUNNING&quot; |
| INACTIVE | &quot;INACTIVE&quot; |



