

# Topic

A topic resource.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**ingestionDataSourceSettings** | [**IngestionDataSourceSettings**](IngestionDataSourceSettings.md) |  |  [optional] |
|**kmsKeyName** | **String** | Optional. The resource name of the Cloud KMS CryptoKey to be used to protect access to messages published on this topic. The expected format is &#x60;projects/_*_/locations/_*_/keyRings/_*_/cryptoKeys/_*&#x60;. |  [optional] |
|**labels** | **Map&lt;String, String&gt;** | Optional. See [Creating and managing labels] (https://cloud.google.com/pubsub/docs/labels). |  [optional] |
|**messageRetentionDuration** | **String** | Optional. Indicates the minimum duration to retain a message after it is published to the topic. If this field is set, messages published to the topic in the last &#x60;message_retention_duration&#x60; are always available to subscribers. For instance, it allows any attached subscription to [seek to a timestamp](https://cloud.google.com/pubsub/docs/replay-overview#seek_to_a_time) that is up to &#x60;message_retention_duration&#x60; in the past. If this field is not set, message retention is controlled by settings on individual subscriptions. Cannot be more than 31 days or less than 10 minutes. |  [optional] |
|**messageStoragePolicy** | [**MessageStoragePolicy**](MessageStoragePolicy.md) |  |  [optional] |
|**name** | **String** | Required. The name of the topic. It must have the format &#x60;\&quot;projects/{project}/topics/{topic}\&quot;&#x60;. &#x60;{topic}&#x60; must start with a letter, and contain only letters (&#x60;[A-Za-z]&#x60;), numbers (&#x60;[0-9]&#x60;), dashes (&#x60;-&#x60;), underscores (&#x60;_&#x60;), periods (&#x60;.&#x60;), tildes (&#x60;~&#x60;), plus (&#x60;+&#x60;) or percent signs (&#x60;%&#x60;). It must be between 3 and 255 characters in length, and it must not start with &#x60;\&quot;goog\&quot;&#x60;. |  [optional] |
|**satisfiesPzs** | **Boolean** | Optional. Reserved for future use. This field is set only in responses from the server; it is ignored if it is set in any requests. |  [optional] |
|**schemaSettings** | [**SchemaSettings**](SchemaSettings.md) |  |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | Output only. An output-only field indicating the state of the topic. |  [optional] [readonly] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| ACTIVE | &quot;ACTIVE&quot; |
| INGESTION_RESOURCE_ERROR | &quot;INGESTION_RESOURCE_ERROR&quot; |



