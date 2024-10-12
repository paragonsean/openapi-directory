

# GoogleCloudRetailV2ImportMetadata

Metadata related to the progress of the Import operation. This is returned by the google.longrunning.Operation.metadata field.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createTime** | **String** | Operation create time. |  [optional] |
|**failureCount** | **String** | Count of entries that encountered errors while processing. |  [optional] |
|**notificationPubsubTopic** | **String** | Pub/Sub topic for receiving notification. If this field is set, when the import is finished, a notification is sent to specified Pub/Sub topic. The message data is JSON string of a Operation. Format of the Pub/Sub topic is &#x60;projects/{project}/topics/{topic}&#x60;. |  [optional] |
|**requestId** | **String** | Deprecated. This field is never set. |  [optional] |
|**successCount** | **String** | Count of entries that were processed successfully. |  [optional] |
|**updateTime** | **String** | Operation last update time. If the operation is done, this is also the finish time. |  [optional] |



