

# GoogleCloudAssetV1p7beta1RelationshipAttributes

The relationship attributes which include `type`, `source_resource_type`, `target_resource_type` and `action`.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**action** | **String** | The detail of the relationship, e.g. &#x60;contains&#x60;, &#x60;attaches&#x60; |  [optional] |
|**sourceResourceType** | **String** | The source asset type. Example: &#x60;compute.googleapis.com/Instance&#x60; |  [optional] |
|**targetResourceType** | **String** | The target asset type. Example: &#x60;compute.googleapis.com/Disk&#x60; |  [optional] |
|**type** | **String** | The unique identifier of the relationship type. Example: &#x60;INSTANCE_TO_INSTANCEGROUP&#x60; |  [optional] |



