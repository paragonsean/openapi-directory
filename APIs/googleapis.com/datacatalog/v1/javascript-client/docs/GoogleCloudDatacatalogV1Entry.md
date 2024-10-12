# GoogleCloudDataCatalogApi.GoogleCloudDatacatalogV1Entry

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bigqueryDateShardedSpec** | [**GoogleCloudDatacatalogV1BigQueryDateShardedSpec**](GoogleCloudDatacatalogV1BigQueryDateShardedSpec.md) |  | [optional] 
**bigqueryTableSpec** | [**GoogleCloudDatacatalogV1BigQueryTableSpec**](GoogleCloudDatacatalogV1BigQueryTableSpec.md) |  | [optional] 
**businessContext** | [**GoogleCloudDatacatalogV1BusinessContext**](GoogleCloudDatacatalogV1BusinessContext.md) |  | [optional] 
**cloudBigtableSystemSpec** | [**GoogleCloudDatacatalogV1CloudBigtableSystemSpec**](GoogleCloudDatacatalogV1CloudBigtableSystemSpec.md) |  | [optional] 
**dataSource** | [**GoogleCloudDatacatalogV1DataSource**](GoogleCloudDatacatalogV1DataSource.md) |  | [optional] 
**dataSourceConnectionSpec** | [**GoogleCloudDatacatalogV1DataSourceConnectionSpec**](GoogleCloudDatacatalogV1DataSourceConnectionSpec.md) |  | [optional] 
**databaseTableSpec** | [**GoogleCloudDatacatalogV1DatabaseTableSpec**](GoogleCloudDatacatalogV1DatabaseTableSpec.md) |  | [optional] 
**datasetSpec** | [**GoogleCloudDatacatalogV1DatasetSpec**](GoogleCloudDatacatalogV1DatasetSpec.md) |  | [optional] 
**description** | **String** | Entry description that can consist of several sentences or paragraphs that describe entry contents. The description must not contain Unicode non-characters as well as C0 and C1 control codes except tabs (HT), new lines (LF), carriage returns (CR), and page breaks (FF). The maximum size is 2000 bytes when encoded in UTF-8. Default value is an empty string. | [optional] 
**displayName** | **String** | Display name of an entry. The maximum size is 500 bytes when encoded in UTF-8. Default value is an empty string. | [optional] 
**featureOnlineStoreSpec** | [**GoogleCloudDatacatalogV1FeatureOnlineStoreSpec**](GoogleCloudDatacatalogV1FeatureOnlineStoreSpec.md) |  | [optional] 
**filesetSpec** | [**GoogleCloudDatacatalogV1FilesetSpec**](GoogleCloudDatacatalogV1FilesetSpec.md) |  | [optional] 
**fullyQualifiedName** | **String** | [Fully Qualified Name (FQN)](https://cloud.google.com//data-catalog/docs/fully-qualified-names) of the resource. Set automatically for entries representing resources from synced systems. Settable only during creation, and read-only later. Can be used for search and lookup of the entries.  | [optional] 
**gcsFilesetSpec** | [**GoogleCloudDatacatalogV1GcsFilesetSpec**](GoogleCloudDatacatalogV1GcsFilesetSpec.md) |  | [optional] 
**integratedSystem** | **String** | Output only. Indicates the entry&#39;s source system that Data Catalog integrates with, such as BigQuery, Pub/Sub, or Dataproc Metastore. | [optional] [readonly] 
**labels** | **{String: String}** | Cloud labels attached to the entry. In Data Catalog, you can create and modify labels attached only to custom entries. Synced entries have unmodifiable labels that come from the source system. | [optional] 
**linkedResource** | **String** | The resource this metadata entry refers to. For Google Cloud Platform resources, &#x60;linked_resource&#x60; is the [Full Resource Name] (https://cloud.google.com/apis/design/resource_names#full_resource_name). For example, the &#x60;linked_resource&#x60; for a table resource from BigQuery is: &#x60;//bigquery.googleapis.com/projects/{PROJECT_ID}/datasets/{DATASET_ID}/tables/{TABLE_ID}&#x60; Output only when the entry is one of the types in the &#x60;EntryType&#x60; enum. For entries with a &#x60;user_specified_type&#x60;, this field is optional and defaults to an empty string. The resource string must contain only letters (a-z, A-Z), numbers (0-9), underscores (_), periods (.), colons (:), slashes (/), dashes (-), and hashes (#). The maximum size is 200 bytes when encoded in UTF-8. | [optional] 
**lookerSystemSpec** | [**GoogleCloudDatacatalogV1LookerSystemSpec**](GoogleCloudDatacatalogV1LookerSystemSpec.md) |  | [optional] 
**modelSpec** | [**GoogleCloudDatacatalogV1ModelSpec**](GoogleCloudDatacatalogV1ModelSpec.md) |  | [optional] 
**name** | **String** | Output only. The resource name of an entry in URL format. Note: The entry itself and its child resources might not be stored in the location specified in its name. | [optional] [readonly] 
**personalDetails** | [**GoogleCloudDatacatalogV1PersonalDetails**](GoogleCloudDatacatalogV1PersonalDetails.md) |  | [optional] 
**routineSpec** | [**GoogleCloudDatacatalogV1RoutineSpec**](GoogleCloudDatacatalogV1RoutineSpec.md) |  | [optional] 
**schema** | [**GoogleCloudDatacatalogV1Schema**](GoogleCloudDatacatalogV1Schema.md) |  | [optional] 
**serviceSpec** | [**GoogleCloudDatacatalogV1ServiceSpec**](GoogleCloudDatacatalogV1ServiceSpec.md) |  | [optional] 
**sourceSystemTimestamps** | [**GoogleCloudDatacatalogV1SystemTimestamps**](GoogleCloudDatacatalogV1SystemTimestamps.md) |  | [optional] 
**sqlDatabaseSystemSpec** | [**GoogleCloudDatacatalogV1SqlDatabaseSystemSpec**](GoogleCloudDatacatalogV1SqlDatabaseSystemSpec.md) |  | [optional] 
**type** | **String** | The type of the entry. For details, see [&#x60;EntryType&#x60;](#entrytype). | [optional] 
**usageSignal** | [**GoogleCloudDatacatalogV1UsageSignal**](GoogleCloudDatacatalogV1UsageSignal.md) |  | [optional] 
**userSpecifiedSystem** | **String** | Indicates the entry&#39;s source system that Data Catalog doesn&#39;t automatically integrate with. The &#x60;user_specified_system&#x60; string has the following limitations: * Is case insensitive. * Must begin with a letter or underscore. * Can only contain letters, numbers, and underscores. * Must be at least 1 character and at most 64 characters long. | [optional] 
**userSpecifiedType** | **String** | Custom entry type that doesn&#39;t match any of the values allowed for input and listed in the &#x60;EntryType&#x60; enum. When creating an entry, first check the type values in the enum. If there are no appropriate types for the new entry, provide a custom value, for example, &#x60;my_special_type&#x60;. The &#x60;user_specified_type&#x60; string has the following limitations: * Is case insensitive. * Must begin with a letter or underscore. * Can only contain letters, numbers, and underscores. * Must be at least 1 character and at most 64 characters long. | [optional] 



## Enum: IntegratedSystemEnum


* `INTEGRATED_SYSTEM_UNSPECIFIED` (value: `"INTEGRATED_SYSTEM_UNSPECIFIED"`)

* `BIGQUERY` (value: `"BIGQUERY"`)

* `CLOUD_PUBSUB` (value: `"CLOUD_PUBSUB"`)

* `DATAPROC_METASTORE` (value: `"DATAPROC_METASTORE"`)

* `DATAPLEX` (value: `"DATAPLEX"`)

* `CLOUD_SPANNER` (value: `"CLOUD_SPANNER"`)

* `CLOUD_BIGTABLE` (value: `"CLOUD_BIGTABLE"`)

* `CLOUD_SQL` (value: `"CLOUD_SQL"`)

* `LOOKER` (value: `"LOOKER"`)

* `VERTEX_AI` (value: `"VERTEX_AI"`)





## Enum: TypeEnum


* `ENTRY_TYPE_UNSPECIFIED` (value: `"ENTRY_TYPE_UNSPECIFIED"`)

* `TABLE` (value: `"TABLE"`)

* `MODEL` (value: `"MODEL"`)

* `DATA_STREAM` (value: `"DATA_STREAM"`)

* `FILESET` (value: `"FILESET"`)

* `CLUSTER` (value: `"CLUSTER"`)

* `DATABASE` (value: `"DATABASE"`)

* `DATA_SOURCE_CONNECTION` (value: `"DATA_SOURCE_CONNECTION"`)

* `ROUTINE` (value: `"ROUTINE"`)

* `LAKE` (value: `"LAKE"`)

* `ZONE` (value: `"ZONE"`)

* `SERVICE` (value: `"SERVICE"`)

* `DATABASE_SCHEMA` (value: `"DATABASE_SCHEMA"`)

* `DASHBOARD` (value: `"DASHBOARD"`)

* `EXPLORE` (value: `"EXPLORE"`)

* `LOOK` (value: `"LOOK"`)

* `FEATURE_ONLINE_STORE` (value: `"FEATURE_ONLINE_STORE"`)

* `FEATURE_VIEW` (value: `"FEATURE_VIEW"`)

* `FEATURE_GROUP` (value: `"FEATURE_GROUP"`)




