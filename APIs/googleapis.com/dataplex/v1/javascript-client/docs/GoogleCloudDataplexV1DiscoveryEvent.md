# CloudDataplexApi.GoogleCloudDataplexV1DiscoveryEvent

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | [**GoogleCloudDataplexV1DiscoveryEventActionDetails**](GoogleCloudDataplexV1DiscoveryEventActionDetails.md) |  | [optional] 
**assetId** | **String** | The id of the associated asset. | [optional] 
**config** | [**GoogleCloudDataplexV1DiscoveryEventConfigDetails**](GoogleCloudDataplexV1DiscoveryEventConfigDetails.md) |  | [optional] 
**dataLocation** | **String** | The data location associated with the event. | [optional] 
**entity** | [**GoogleCloudDataplexV1DiscoveryEventEntityDetails**](GoogleCloudDataplexV1DiscoveryEventEntityDetails.md) |  | [optional] 
**lakeId** | **String** | The id of the associated lake. | [optional] 
**message** | **String** | The log message. | [optional] 
**partition** | [**GoogleCloudDataplexV1DiscoveryEventPartitionDetails**](GoogleCloudDataplexV1DiscoveryEventPartitionDetails.md) |  | [optional] 
**type** | **String** | The type of the event being logged. | [optional] 
**zoneId** | **String** | The id of the associated zone. | [optional] 



## Enum: TypeEnum


* `EVENT_TYPE_UNSPECIFIED` (value: `"EVENT_TYPE_UNSPECIFIED"`)

* `CONFIG` (value: `"CONFIG"`)

* `ENTITY_CREATED` (value: `"ENTITY_CREATED"`)

* `ENTITY_UPDATED` (value: `"ENTITY_UPDATED"`)

* `ENTITY_DELETED` (value: `"ENTITY_DELETED"`)

* `PARTITION_CREATED` (value: `"PARTITION_CREATED"`)

* `PARTITION_UPDATED` (value: `"PARTITION_UPDATED"`)

* `PARTITION_DELETED` (value: `"PARTITION_DELETED"`)




