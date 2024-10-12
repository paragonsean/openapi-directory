# RemoteBuildExecutionApi.GoogleDevtoolsRemotebuildexecutionAdminV1alphaInstance

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**featurePolicy** | [**GoogleDevtoolsRemotebuildexecutionAdminV1alphaFeaturePolicy**](GoogleDevtoolsRemotebuildexecutionAdminV1alphaFeaturePolicy.md) |  | [optional] 
**location** | **String** | The location is a GCP region. Currently only &#x60;us-central1&#x60; is supported. | [optional] 
**loggingEnabled** | **Boolean** | Output only. Whether stack driver logging is enabled for the instance. | [optional] [readonly] 
**name** | **String** | Output only. Instance resource name formatted as: &#x60;projects/[PROJECT_ID]/instances/[INSTANCE_ID]&#x60;. Name should not be populated when creating an instance since it is provided in the &#x60;instance_id&#x60; field. | [optional] [readonly] 
**schedulerNotificationConfig** | [**GoogleDevtoolsRemotebuildexecutionAdminV1alphaSchedulerNotificationConfig**](GoogleDevtoolsRemotebuildexecutionAdminV1alphaSchedulerNotificationConfig.md) |  | [optional] 
**state** | **String** | Output only. State of the instance. | [optional] [readonly] 



## Enum: StateEnum


* `STATE_UNSPECIFIED` (value: `"STATE_UNSPECIFIED"`)

* `CREATING` (value: `"CREATING"`)

* `RUNNING` (value: `"RUNNING"`)

* `INACTIVE` (value: `"INACTIVE"`)




