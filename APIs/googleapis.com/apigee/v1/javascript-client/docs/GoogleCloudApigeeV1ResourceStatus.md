# ApigeeApi.GoogleCloudApigeeV1ResourceStatus

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource** | **String** | The resource name. Currently only two resources are supported: EnvironmentGroup - organizations/{org}/envgroups/{envgroup} EnvironmentConfig - organizations/{org}/environments/{environment}/deployedConfig | [optional] 
**revisions** | [**[GoogleCloudApigeeV1RevisionStatus]**](GoogleCloudApigeeV1RevisionStatus.md) | Revisions of the resource currently deployed in the instance. | [optional] 
**totalReplicas** | **Number** | The total number of replicas that should have this resource. | [optional] 
**uid** | **String** | The uid of the resource. In the unexpected case that the instance has multiple uids for the same name, they should be reported under separate ResourceStatuses. | [optional] 


