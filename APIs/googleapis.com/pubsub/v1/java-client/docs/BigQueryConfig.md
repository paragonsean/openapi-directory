

# BigQueryConfig

Configuration for a BigQuery subscription.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dropUnknownFields** | **Boolean** | Optional. When true and use_topic_schema is true, any fields that are a part of the topic schema that are not part of the BigQuery table schema are dropped when writing to BigQuery. Otherwise, the schemas must be kept in sync and any messages with extra fields are not written and remain in the subscription&#39;s backlog. |  [optional] |
|**serviceAccountEmail** | **String** | Optional. The service account to use to write to BigQuery. The subscription creator or updater that specifies this field must have &#x60;iam.serviceAccounts.actAs&#x60; permission on the service account. If not specified, the Pub/Sub [service agent](https://cloud.google.com/iam/docs/service-agents), service-{project_number}@gcp-sa-pubsub.iam.gserviceaccount.com, is used. |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | Output only. An output-only field that indicates whether or not the subscription can receive messages. |  [optional] [readonly] |
|**table** | **String** | Optional. The name of the table to which to write data, of the form {projectId}.{datasetId}.{tableId} |  [optional] |
|**useTableSchema** | **Boolean** | Optional. When true, use the BigQuery table&#39;s schema as the columns to write to in BigQuery. &#x60;use_table_schema&#x60; and &#x60;use_topic_schema&#x60; cannot be enabled at the same time. |  [optional] |
|**useTopicSchema** | **Boolean** | Optional. When true, use the topic&#39;s schema as the columns to write to in BigQuery, if it exists. &#x60;use_topic_schema&#x60; and &#x60;use_table_schema&#x60; cannot be enabled at the same time. |  [optional] |
|**writeMetadata** | **Boolean** | Optional. When true, write the subscription name, message_id, publish_time, attributes, and ordering_key to additional columns in the table. The subscription name, message_id, and publish_time fields are put in their own columns while all other message properties (other than data) are written to a JSON object in the attributes column. |  [optional] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| ACTIVE | &quot;ACTIVE&quot; |
| PERMISSION_DENIED | &quot;PERMISSION_DENIED&quot; |
| NOT_FOUND | &quot;NOT_FOUND&quot; |
| SCHEMA_MISMATCH | &quot;SCHEMA_MISMATCH&quot; |
| IN_TRANSIT_LOCATION_RESTRICTION | &quot;IN_TRANSIT_LOCATION_RESTRICTION&quot; |



