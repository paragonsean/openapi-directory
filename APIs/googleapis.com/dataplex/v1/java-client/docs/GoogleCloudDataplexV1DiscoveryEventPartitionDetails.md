

# GoogleCloudDataplexV1DiscoveryEventPartitionDetails

Details about the partition.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**entity** | **String** | The name to the containing entity resource. The name is the fully-qualified resource name. |  [optional] |
|**partition** | **String** | The name to the partition resource. The name is the fully-qualified resource name. |  [optional] |
|**sampledDataLocations** | **List&lt;String&gt;** | The locations of the data items (e.g., a Cloud Storage objects) sampled for metadata inference. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | The type of the containing entity resource. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| ENTITY_TYPE_UNSPECIFIED | &quot;ENTITY_TYPE_UNSPECIFIED&quot; |
| TABLE | &quot;TABLE&quot; |
| FILESET | &quot;FILESET&quot; |



