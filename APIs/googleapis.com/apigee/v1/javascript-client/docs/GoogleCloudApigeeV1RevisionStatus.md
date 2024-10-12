# ApigeeApi.GoogleCloudApigeeV1RevisionStatus

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errors** | [**[GoogleCloudApigeeV1UpdateError]**](GoogleCloudApigeeV1UpdateError.md) | Errors reported when attempting to load this revision. | [optional] 
**jsonSpec** | **String** | The json content of the resource revision. Large specs should be sent individually via the spec field to avoid hitting request size limits. | [optional] 
**replicas** | **Number** | The number of replicas that have successfully loaded this revision. | [optional] 
**revisionId** | **String** | The revision of the resource. | [optional] 


