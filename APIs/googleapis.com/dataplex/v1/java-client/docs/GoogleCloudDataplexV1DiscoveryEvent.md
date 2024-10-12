

# GoogleCloudDataplexV1DiscoveryEvent

The payload associated with Discovery data processing.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**action** | [**GoogleCloudDataplexV1DiscoveryEventActionDetails**](GoogleCloudDataplexV1DiscoveryEventActionDetails.md) |  |  [optional] |
|**assetId** | **String** | The id of the associated asset. |  [optional] |
|**config** | [**GoogleCloudDataplexV1DiscoveryEventConfigDetails**](GoogleCloudDataplexV1DiscoveryEventConfigDetails.md) |  |  [optional] |
|**dataLocation** | **String** | The data location associated with the event. |  [optional] |
|**entity** | [**GoogleCloudDataplexV1DiscoveryEventEntityDetails**](GoogleCloudDataplexV1DiscoveryEventEntityDetails.md) |  |  [optional] |
|**lakeId** | **String** | The id of the associated lake. |  [optional] |
|**message** | **String** | The log message. |  [optional] |
|**partition** | [**GoogleCloudDataplexV1DiscoveryEventPartitionDetails**](GoogleCloudDataplexV1DiscoveryEventPartitionDetails.md) |  |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | The type of the event being logged. |  [optional] |
|**zoneId** | **String** | The id of the associated zone. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| EVENT_TYPE_UNSPECIFIED | &quot;EVENT_TYPE_UNSPECIFIED&quot; |
| CONFIG | &quot;CONFIG&quot; |
| ENTITY_CREATED | &quot;ENTITY_CREATED&quot; |
| ENTITY_UPDATED | &quot;ENTITY_UPDATED&quot; |
| ENTITY_DELETED | &quot;ENTITY_DELETED&quot; |
| PARTITION_CREATED | &quot;PARTITION_CREATED&quot; |
| PARTITION_UPDATED | &quot;PARTITION_UPDATED&quot; |
| PARTITION_DELETED | &quot;PARTITION_DELETED&quot; |



