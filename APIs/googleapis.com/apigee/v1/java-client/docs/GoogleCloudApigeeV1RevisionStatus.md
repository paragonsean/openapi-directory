

# GoogleCloudApigeeV1RevisionStatus

The status of a specific resource revision.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**errors** | [**List&lt;GoogleCloudApigeeV1UpdateError&gt;**](GoogleCloudApigeeV1UpdateError.md) | Errors reported when attempting to load this revision. |  [optional] |
|**jsonSpec** | **String** | The json content of the resource revision. Large specs should be sent individually via the spec field to avoid hitting request size limits. |  [optional] |
|**replicas** | **Integer** | The number of replicas that have successfully loaded this revision. |  [optional] |
|**revisionId** | **String** | The revision of the resource. |  [optional] |



