# GoogleCloudDataCatalogApi.GoogleCloudDatacatalogV1beta1SearchCatalogResult

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**linkedResource** | **String** | The full name of the cloud resource the entry belongs to. See: https://cloud.google.com/apis/design/resource_names#full_resource_name. Example: * &#x60;//bigquery.googleapis.com/projects/projectId/datasets/datasetId/tables/tableId&#x60; | [optional] 
**modifyTime** | **String** | Last-modified timestamp of the entry from the managing system. | [optional] 
**relativeResourceName** | **String** | The relative resource name of the resource in URL format. Examples: * &#x60;projects/{project_id}/locations/{location_id}/entryGroups/{entry_group_id}/entries/{entry_id}&#x60; * &#x60;projects/{project_id}/tagTemplates/{tag_template_id}&#x60; | [optional] 
**searchResultSubtype** | **String** | Sub-type of the search result. This is a dot-delimited description of the resource&#39;s full type, and is the same as the value callers would provide in the \&quot;type\&quot; search facet. Examples: &#x60;entry.table&#x60;, &#x60;entry.dataStream&#x60;, &#x60;tagTemplate&#x60;. | [optional] 
**searchResultType** | **String** | Type of the search result. This field can be used to determine which Get method to call to fetch the full resource. | [optional] 



## Enum: SearchResultTypeEnum


* `SEARCH_RESULT_TYPE_UNSPECIFIED` (value: `"SEARCH_RESULT_TYPE_UNSPECIFIED"`)

* `ENTRY` (value: `"ENTRY"`)

* `TAG_TEMPLATE` (value: `"TAG_TEMPLATE"`)

* `ENTRY_GROUP` (value: `"ENTRY_GROUP"`)




