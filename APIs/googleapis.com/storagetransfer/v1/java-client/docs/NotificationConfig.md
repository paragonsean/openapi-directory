

# NotificationConfig

Specification to configure notifications published to Pub/Sub. Notifications are published to the customer-provided topic using the following `PubsubMessage.attributes`: * `\"eventType\"`: one of the EventType values * `\"payloadFormat\"`: one of the PayloadFormat values * `\"projectId\"`: the project_id of the `TransferOperation` * `\"transferJobName\"`: the transfer_job_name of the `TransferOperation` * `\"transferOperationName\"`: the name of the `TransferOperation` The `PubsubMessage.data` contains a TransferOperation resource formatted according to the specified `PayloadFormat`.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**eventTypes** | [**List&lt;EventTypesEnum&gt;**](#List&lt;EventTypesEnum&gt;) | Event types for which a notification is desired. If empty, send notifications for all event types. |  [optional] |
|**payloadFormat** | [**PayloadFormatEnum**](#PayloadFormatEnum) | Required. The desired format of the notification message payloads. |  [optional] |
|**pubsubTopic** | **String** | Required. The &#x60;Topic.name&#x60; of the Pub/Sub topic to which to publish notifications. Must be of the format: &#x60;projects/{project}/topics/{topic}&#x60;. Not matching this format results in an INVALID_ARGUMENT error. |  [optional] |



## Enum: List&lt;EventTypesEnum&gt;

| Name | Value |
|---- | -----|
| EVENT_TYPE_UNSPECIFIED | &quot;EVENT_TYPE_UNSPECIFIED&quot; |
| TRANSFER_OPERATION_SUCCESS | &quot;TRANSFER_OPERATION_SUCCESS&quot; |
| TRANSFER_OPERATION_FAILED | &quot;TRANSFER_OPERATION_FAILED&quot; |
| TRANSFER_OPERATION_ABORTED | &quot;TRANSFER_OPERATION_ABORTED&quot; |



## Enum: PayloadFormatEnum

| Name | Value |
|---- | -----|
| PAYLOAD_FORMAT_UNSPECIFIED | &quot;PAYLOAD_FORMAT_UNSPECIFIED&quot; |
| NONE | &quot;NONE&quot; |
| JSON | &quot;JSON&quot; |



