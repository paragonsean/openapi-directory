

# GoogleCloudApigeeV1SharedFlowRevision

The metadata describing a shared flow revision.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**configurationVersion** | [**GoogleCloudApigeeV1ConfigVersion**](GoogleCloudApigeeV1ConfigVersion.md) |  |  [optional] |
|**contextInfo** | **String** | A textual description of the shared flow revision. |  [optional] |
|**createdAt** | **String** | Time at which this shared flow revision was created, in milliseconds since epoch. |  [optional] |
|**description** | **String** | Description of the shared flow revision. |  [optional] |
|**displayName** | **String** | The human readable name of this shared flow. |  [optional] |
|**entityMetaDataAsProperties** | **Map&lt;String, String&gt;** | A Key-Value map of metadata about this shared flow revision. |  [optional] |
|**lastModifiedAt** | **String** | Time at which this shared flow revision was most recently modified, in milliseconds since epoch. |  [optional] |
|**name** | **String** | The resource ID of the parent shared flow. |  [optional] |
|**policies** | **List&lt;String&gt;** | A list of policy names included in this shared flow revision. |  [optional] |
|**resourceFiles** | [**GoogleCloudApigeeV1ResourceFiles**](GoogleCloudApigeeV1ResourceFiles.md) |  |  [optional] |
|**resources** | **List&lt;String&gt;** | A list of the resources included in this shared flow revision formatted as \&quot;{type}://{name}\&quot;. |  [optional] |
|**revision** | **String** | The resource ID of this revision. |  [optional] |
|**sharedFlows** | **List&lt;String&gt;** | A list of the shared flow names included in this shared flow revision. |  [optional] |
|**type** | **String** | The string \&quot;Application\&quot; |  [optional] |



