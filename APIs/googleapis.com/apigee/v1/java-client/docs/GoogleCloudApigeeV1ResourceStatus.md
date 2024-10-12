

# GoogleCloudApigeeV1ResourceStatus

The status of a resource loaded in the runtime.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**resource** | **String** | The resource name. Currently only two resources are supported: EnvironmentGroup - organizations/{org}/envgroups/{envgroup} EnvironmentConfig - organizations/{org}/environments/{environment}/deployedConfig |  [optional] |
|**revisions** | [**List&lt;GoogleCloudApigeeV1RevisionStatus&gt;**](GoogleCloudApigeeV1RevisionStatus.md) | Revisions of the resource currently deployed in the instance. |  [optional] |
|**totalReplicas** | **Integer** | The total number of replicas that should have this resource. |  [optional] |
|**uid** | **String** | The uid of the resource. In the unexpected case that the instance has multiple uids for the same name, they should be reported under separate ResourceStatuses. |  [optional] |



