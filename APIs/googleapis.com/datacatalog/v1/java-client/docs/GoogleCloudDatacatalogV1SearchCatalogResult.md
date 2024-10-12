

# GoogleCloudDatacatalogV1SearchCatalogResult

Result in the response to a search request. Each result captures details of one entry that matches the search.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**description** | **String** | Entry description that can consist of several sentences or paragraphs that describe entry contents. |  [optional] |
|**displayName** | **String** | The display name of the result. |  [optional] |
|**fullyQualifiedName** | **String** | Fully qualified name (FQN) of the resource. FQNs take two forms: * For non-regionalized resources: &#x60;{SYSTEM}:{PROJECT}.{PATH_TO_RESOURCE_SEPARATED_WITH_DOTS}&#x60; * For regionalized resources: &#x60;{SYSTEM}:{PROJECT}.{LOCATION_ID}.{PATH_TO_RESOURCE_SEPARATED_WITH_DOTS}&#x60; Example for a DPMS table: &#x60;dataproc_metastore:PROJECT_ID.LOCATION_ID.INSTANCE_ID.DATABASE_ID.TABLE_ID&#x60; |  [optional] |
|**integratedSystem** | [**IntegratedSystemEnum**](#IntegratedSystemEnum) | Output only. The source system that Data Catalog automatically integrates with, such as BigQuery, Cloud Pub/Sub, or Dataproc Metastore. |  [optional] [readonly] |
|**linkedResource** | **String** | The full name of the Google Cloud resource the entry belongs to. For more information, see [Full Resource Name] (/apis/design/resource_names#full_resource_name). Example: &#x60;//bigquery.googleapis.com/projects/PROJECT_ID/datasets/DATASET_ID/tables/TABLE_ID&#x60; |  [optional] |
|**modifyTime** | **String** | The last modification timestamp of the entry in the source system. |  [optional] |
|**relativeResourceName** | **String** | The relative name of the resource in URL format. Examples: * &#x60;projects/{PROJECT_ID}/locations/{LOCATION_ID}/entryGroups/{ENTRY_GROUP_ID}/entries/{ENTRY_ID}&#x60; * &#x60;projects/{PROJECT_ID}/tagTemplates/{TAG_TEMPLATE_ID}&#x60; |  [optional] |
|**searchResultSubtype** | **String** | Sub-type of the search result. A dot-delimited full type of the resource. The same type you specify in the &#x60;type&#x60; search predicate. Examples: &#x60;entry.table&#x60;, &#x60;entry.dataStream&#x60;, &#x60;tagTemplate&#x60;. |  [optional] |
|**searchResultType** | [**SearchResultTypeEnum**](#SearchResultTypeEnum) | Type of the search result. You can use this field to determine which get method to call to fetch the full resource. |  [optional] |
|**userSpecifiedSystem** | **String** | Custom source system that you can manually integrate Data Catalog with. |  [optional] |



## Enum: IntegratedSystemEnum

| Name | Value |
|---- | -----|
| INTEGRATED_SYSTEM_UNSPECIFIED | &quot;INTEGRATED_SYSTEM_UNSPECIFIED&quot; |
| BIGQUERY | &quot;BIGQUERY&quot; |
| CLOUD_PUBSUB | &quot;CLOUD_PUBSUB&quot; |
| DATAPROC_METASTORE | &quot;DATAPROC_METASTORE&quot; |
| DATAPLEX | &quot;DATAPLEX&quot; |
| CLOUD_SPANNER | &quot;CLOUD_SPANNER&quot; |
| CLOUD_BIGTABLE | &quot;CLOUD_BIGTABLE&quot; |
| CLOUD_SQL | &quot;CLOUD_SQL&quot; |
| LOOKER | &quot;LOOKER&quot; |
| VERTEX_AI | &quot;VERTEX_AI&quot; |



## Enum: SearchResultTypeEnum

| Name | Value |
|---- | -----|
| SEARCH_RESULT_TYPE_UNSPECIFIED | &quot;SEARCH_RESULT_TYPE_UNSPECIFIED&quot; |
| ENTRY | &quot;ENTRY&quot; |
| TAG_TEMPLATE | &quot;TAG_TEMPLATE&quot; |
| ENTRY_GROUP | &quot;ENTRY_GROUP&quot; |



