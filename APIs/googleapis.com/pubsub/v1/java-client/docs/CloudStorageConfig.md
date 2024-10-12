

# CloudStorageConfig

Configuration for a Cloud Storage subscription.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**avroConfig** | [**AvroConfig**](AvroConfig.md) |  |  [optional] |
|**bucket** | **String** | Required. User-provided name for the Cloud Storage bucket. The bucket must be created by the user. The bucket name must be without any prefix like \&quot;gs://\&quot;. See the [bucket naming requirements] (https://cloud.google.com/storage/docs/buckets#naming). |  [optional] |
|**filenamePrefix** | **String** | Optional. User-provided prefix for Cloud Storage filename. See the [object naming requirements](https://cloud.google.com/storage/docs/objects#naming). |  [optional] |
|**filenameSuffix** | **String** | Optional. User-provided suffix for Cloud Storage filename. See the [object naming requirements](https://cloud.google.com/storage/docs/objects#naming). Must not end in \&quot;/\&quot;. |  [optional] |
|**maxBytes** | **String** | Optional. The maximum bytes that can be written to a Cloud Storage file before a new file is created. Min 1 KB, max 10 GiB. The max_bytes limit may be exceeded in cases where messages are larger than the limit. |  [optional] |
|**maxDuration** | **String** | Optional. The maximum duration that can elapse before a new Cloud Storage file is created. Min 1 minute, max 10 minutes, default 5 minutes. May not exceed the subscription&#39;s acknowledgement deadline. |  [optional] |
|**serviceAccountEmail** | **String** | Optional. The service account to use to write to Cloud Storage. The subscription creator or updater that specifies this field must have &#x60;iam.serviceAccounts.actAs&#x60; permission on the service account. If not specified, the Pub/Sub [service agent](https://cloud.google.com/iam/docs/service-agents), service-{project_number}@gcp-sa-pubsub.iam.gserviceaccount.com, is used. |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | Output only. An output-only field that indicates whether or not the subscription can receive messages. |  [optional] [readonly] |
|**textConfig** | **Object** | Configuration for writing message data in text format. Message payloads will be written to files as raw text, separated by a newline. |  [optional] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| ACTIVE | &quot;ACTIVE&quot; |
| PERMISSION_DENIED | &quot;PERMISSION_DENIED&quot; |
| NOT_FOUND | &quot;NOT_FOUND&quot; |
| IN_TRANSIT_LOCATION_RESTRICTION | &quot;IN_TRANSIT_LOCATION_RESTRICTION&quot; |



