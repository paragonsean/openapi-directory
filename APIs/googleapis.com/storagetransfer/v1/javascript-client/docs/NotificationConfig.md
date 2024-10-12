# StorageTransferApi.NotificationConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**eventTypes** | **[String]** | Event types for which a notification is desired. If empty, send notifications for all event types. | [optional] 
**payloadFormat** | **String** | Required. The desired format of the notification message payloads. | [optional] 
**pubsubTopic** | **String** | Required. The &#x60;Topic.name&#x60; of the Pub/Sub topic to which to publish notifications. Must be of the format: &#x60;projects/{project}/topics/{topic}&#x60;. Not matching this format results in an INVALID_ARGUMENT error. | [optional] 



## Enum: [EventTypesEnum]


* `EVENT_TYPE_UNSPECIFIED` (value: `"EVENT_TYPE_UNSPECIFIED"`)

* `TRANSFER_OPERATION_SUCCESS` (value: `"TRANSFER_OPERATION_SUCCESS"`)

* `TRANSFER_OPERATION_FAILED` (value: `"TRANSFER_OPERATION_FAILED"`)

* `TRANSFER_OPERATION_ABORTED` (value: `"TRANSFER_OPERATION_ABORTED"`)





## Enum: PayloadFormatEnum


* `PAYLOAD_FORMAT_UNSPECIFIED` (value: `"PAYLOAD_FORMAT_UNSPECIFIED"`)

* `NONE` (value: `"NONE"`)

* `JSON` (value: `"JSON"`)




