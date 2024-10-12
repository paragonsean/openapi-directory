# GoogleCloudDataCatalogApi.GoogleCloudDatacatalogV1beta1Entry

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bigqueryDateShardedSpec** | [**GoogleCloudDatacatalogV1beta1BigQueryDateShardedSpec**](GoogleCloudDatacatalogV1beta1BigQueryDateShardedSpec.md) |  | [optional] 
**bigqueryTableSpec** | [**GoogleCloudDatacatalogV1beta1BigQueryTableSpec**](GoogleCloudDatacatalogV1beta1BigQueryTableSpec.md) |  | [optional] 
**description** | **String** | Entry description, which can consist of several sentences or paragraphs that describe entry contents. Default value is an empty string. | [optional] 
**displayName** | **String** | Display information such as title and description. A short name to identify the entry, for example, \&quot;Analytics Data - Jan 2011\&quot;. Default value is an empty string. | [optional] 
**gcsFilesetSpec** | [**GoogleCloudDatacatalogV1beta1GcsFilesetSpec**](GoogleCloudDatacatalogV1beta1GcsFilesetSpec.md) |  | [optional] 
**integratedSystem** | **String** | Output only. This field indicates the entry&#39;s source system that Data Catalog integrates with, such as BigQuery or Pub/Sub. | [optional] [readonly] 
**linkedResource** | **String** | The resource this metadata entry refers to. For Google Cloud Platform resources, &#x60;linked_resource&#x60; is the [full name of the resource](https://cloud.google.com/apis/design/resource_names#full_resource_name). For example, the &#x60;linked_resource&#x60; for a table resource from BigQuery is: * //bigquery.googleapis.com/projects/projectId/datasets/datasetId/tables/tableId Output only when Entry is of type in the EntryType enum. For entries with user_specified_type, this field is optional and defaults to an empty string. | [optional] 
**name** | **String** | Output only. The Data Catalog resource name of the entry in URL format. Example: * projects/{project_id}/locations/{location}/entryGroups/{entry_group_id}/entries/{entry_id} Note that this Entry and its child resources may not actually be stored in the location in this name. | [optional] [readonly] 
**schema** | [**GoogleCloudDatacatalogV1beta1Schema**](GoogleCloudDatacatalogV1beta1Schema.md) |  | [optional] 
**sourceSystemTimestamps** | [**GoogleCloudDatacatalogV1beta1SystemTimestamps**](GoogleCloudDatacatalogV1beta1SystemTimestamps.md) |  | [optional] 
**type** | **String** | The type of the entry. Only used for Entries with types in the EntryType enum. | [optional] 
**usageSignal** | [**GoogleCloudDatacatalogV1beta1UsageSignal**](GoogleCloudDatacatalogV1beta1UsageSignal.md) |  | [optional] 
**userSpecifiedSystem** | **String** | This field indicates the entry&#39;s source system that Data Catalog does not integrate with. &#x60;user_specified_system&#x60; strings must begin with a letter or underscore and can only contain letters, numbers, and underscores; are case insensitive; must be at least 1 character and at most 64 characters long. | [optional] 
**userSpecifiedType** | **String** | Entry type if it does not fit any of the input-allowed values listed in &#x60;EntryType&#x60; enum above. When creating an entry, users should check the enum values first, if nothing matches the entry to be created, then provide a custom value, for example \&quot;my_special_type\&quot;. &#x60;user_specified_type&#x60; strings must begin with a letter or underscore and can only contain letters, numbers, and underscores; are case insensitive; must be at least 1 character and at most 64 characters long. Currently, only FILESET enum value is allowed. All other entries created through Data Catalog must use &#x60;user_specified_type&#x60;. | [optional] 



## Enum: IntegratedSystemEnum


* `INTEGRATED_SYSTEM_UNSPECIFIED` (value: `"INTEGRATED_SYSTEM_UNSPECIFIED"`)

* `BIGQUERY` (value: `"BIGQUERY"`)

* `CLOUD_PUBSUB` (value: `"CLOUD_PUBSUB"`)





## Enum: TypeEnum


* `ENTRY_TYPE_UNSPECIFIED` (value: `"ENTRY_TYPE_UNSPECIFIED"`)

* `TABLE` (value: `"TABLE"`)

* `MODEL` (value: `"MODEL"`)

* `DATA_STREAM` (value: `"DATA_STREAM"`)

* `FILESET` (value: `"FILESET"`)




