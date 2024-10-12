# Opendatasoft.OdsApi

All URIs are relative to *https://public.opendatasoft.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**aggregateDatasets_1**](OdsApi.md#aggregateDatasets_1) | **GET** /{source}/aggregates | 
[**aggregateRecords_1**](OdsApi.md#aggregateRecords_1) | **GET** /{source}/datasets/{dataset_id}/aggregates | 
[**downloadDatasetAttachement_0**](OdsApi.md#downloadDatasetAttachement_0) | **GET** /{source}/datasets/{dataset_id}/attachments/{attachment_id} | 
[**downloadDatasetSnapshot_0**](OdsApi.md#downloadDatasetSnapshot_0) | **GET** /{source}/datasets/{dataset_id}/snapshots/{snapshot_id} | 
[**exportDatasetsCSV_0**](OdsApi.md#exportDatasetsCSV_0) | **GET** /{source}/exports/csv | 
[**exportDatasetsJson_0**](OdsApi.md#exportDatasetsJson_0) | **GET** /{source}/exports/json | 
[**exportDatasetsRDF_0**](OdsApi.md#exportDatasetsRDF_0) | **GET** /{source}/exports/rdf | 
[**exportDatasetsRSS_0**](OdsApi.md#exportDatasetsRSS_0) | **GET** /{source}/exports/rss | 
[**exportDatasetsTTL_0**](OdsApi.md#exportDatasetsTTL_0) | **GET** /{source}/exports/ttl | 
[**exportDatasetsXLS_0**](OdsApi.md#exportDatasetsXLS_0) | **GET** /{source}/exports/xls | 
[**exportRecordsCSV_0**](OdsApi.md#exportRecordsCSV_0) | **GET** /{source}/datasets/{dataset_id}/exports/csv | 
[**exportRecordsGEOJSON_0**](OdsApi.md#exportRecordsGEOJSON_0) | **GET** /{source}/datasets/{dataset_id}/exports/geojson | 
[**exportRecordsICAL_0**](OdsApi.md#exportRecordsICAL_0) | **GET** /{source}/datasets/{dataset_id}/exports/ical | 
[**exportRecordsJSON_0**](OdsApi.md#exportRecordsJSON_0) | **GET** /{source}/datasets/{dataset_id}/exports/json | 
[**exportRecordsOV2_0**](OdsApi.md#exportRecordsOV2_0) | **GET** /{source}/datasets/{dataset_id}/exports/ov2 | 
[**exportRecordsSHP_0**](OdsApi.md#exportRecordsSHP_0) | **GET** /{source}/datasets/{dataset_id}/exports/shp | 
[**exportRecordsXLS_0**](OdsApi.md#exportRecordsXLS_0) | **GET** /{source}/datasets/{dataset_id}/exports/xls | 
[**getDatasetAttachements_0**](OdsApi.md#getDatasetAttachements_0) | **GET** /{source}/datasets/{dataset_id}/attachments | 
[**getDatasetFile_0**](OdsApi.md#getDatasetFile_0) | **GET** /{source}/datasets/{dataset_id}/files/{file_id} | 
[**getDatasetReuse_0**](OdsApi.md#getDatasetReuse_0) | **GET** /{source}/datasets/{dataset_id}/reuses/{reuse_id} | 
[**getDatasetReuses_0**](OdsApi.md#getDatasetReuses_0) | **GET** /{source}/datasets/{dataset_id}/reuses | 
[**getDatasetSnapshots_0**](OdsApi.md#getDatasetSnapshots_0) | **GET** /{source}/datasets/{dataset_id}/snapshots | 
[**getDataset_0**](OdsApi.md#getDataset_0) | **GET** /{source}/datasets/{dataset_id} | 
[**getDatasetsFacets_1**](OdsApi.md#getDatasetsFacets_1) | **GET** /{source}/facets | 
[**getDatasets_0**](OdsApi.md#getDatasets_0) | **GET** /{source}/datasets | 
[**getMetadataTemplate_0**](OdsApi.md#getMetadataTemplate_0) | **GET** /{source}/metadata_templates/{metadata_template_type}/{metadata_template_name} | 
[**getMetadataTemplatesType_0**](OdsApi.md#getMetadataTemplatesType_0) | **GET** /{source}/metadata_templates/{metadata_template_type} | 
[**getMetadataTemplatesTypes_0**](OdsApi.md#getMetadataTemplatesTypes_0) | **GET** /{source}/metadata_templates | 
[**getPage_0**](OdsApi.md#getPage_0) | **GET** /pages/{slug} | 
[**getPages_0**](OdsApi.md#getPages_0) | **GET** /pages | 
[**getRecord_0**](OdsApi.md#getRecord_0) | **GET** /{source}/datasets/{dataset_id}/records/{record_id} | 
[**getRecordsFacets_1**](OdsApi.md#getRecordsFacets_1) | **GET** /{source}/datasets/{dataset_id}/facets | 
[**getRecords_0**](OdsApi.md#getRecords_0) | **GET** /{source}/datasets/{dataset_id}/records | 
[**getRoot_0**](OdsApi.md#getRoot_0) | **GET** / | 
[**getSource_0**](OdsApi.md#getSource_0) | **GET** /{source} | 
[**sendDatasetFeedback_0**](OdsApi.md#sendDatasetFeedback_0) | **PUT** /{source}/datasets/{dataset_id}/feedback | 



## aggregateDatasets_1

> AggregateDatasets200Response aggregateDatasets_1(source, opts)



**Deprecated, use &#x60;/datasets&#x60; instead.** 

### Example

```javascript
import Opendatasoft from 'opendatasoft';
let defaultClient = Opendatasoft.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure HTTP basic authorization: basic
let basic = defaultClient.authentications['basic'];
basic.username = 'YOUR USERNAME';
basic.password = 'YOUR PASSWORD';

let apiInstance = new Opendatasoft.OdsApi();
let source = "'catalog'"; // String | Each source represents a different catalog of datasets you'll be able to query.  There are 2 sources available:  * catalog: the catalog of datasets on your portal * opendatasoft: Opendatasoft's repository of public datasets, also available at   [data.opendatasoft.com](https://data.opendatasoft.com/page/home/) 
let opts = {
  'select': "select_example", // String | A select expression can be used to add, remove or change fields to return. An expression can be:   - a wildcard ('*'): return all fields   - a field name: return only this field   - an include/exclude function. Include (resp exclude) all field matching include/exclude expression. This expression can contain wildcard. For example: include(spa*) will return all fields begining with 'spa'   - a complex expression: return the result of this expression. A label can be set for this expression, in that case, field will be named with this label. For instance: 'size * 2 as bigger_size' will return a new field named bigger_size and containing the double of size field value. 
  'where': ["null"], // [String] | An array of filters.  A filter is a text expression performing a simple full-text search that can also include logical operations (NOT, AND, OR...) as well as lots of other functions, thus performing more complex and more precise searches.  Read [the query language reference](https://docs.opendatasoft.com/api/explore/v2.html#where-clause) for more details. 
  'groupBy': "groupBy_example", // String | A group by expression defines a grouping function for an aggregation. It can be:  - a field name: group result by each value of this field  - a range function: group result by range  - a date function: group result by date It is possible to specify a custom name with the 'as name' notation. For instance: group_by='city_field as city'. 
  'orderBy': ["null"], // [String] | A comma-separated list of field names or aggregations to sort on, followed by an order (`asc` or `desc`).  Sorts results according to the specified fields' values in ascending order by default. To sort results in descending order, use the `desc` keyword.  Example: `sum(age) desc, name asc` 
  'limit': 10, // Number | Number of items to return.  To use in conjonction with offset to implement pagination.  Limit maximum value is 100. To retrive more data use export entry points. The default value is 10. 
  'offset': 0, // Number | Index of the first item to return (starting at 0).  To use in conjonction with limit to implement pagination. 
  'facet': ["null"], // [String] | A facet is a field used for simple filtering (through the parameters refine and exclude) or exploration (with the endpoint `/facets`).  Facets can be configured in the back-office or with this parameter.  Read [the facets documentation](https://help.opendatasoft.com/apis/ods-search-v2/#facets) for more details. 
  'refine': ["null"], // [String] | An array of facet filters. For example **city:Paris** or **modified:2019/12**. The request will only include the selected facet value.  Read [filtering with facets value](https://help.opendatasoft.com/apis/ods-search-v2/#filtering-with-facets-values) for more details.  *Not to be confused with a where filter. Refining with a facet is equivalent to selecting an entry in the left navigation panel.*  *refine is not available for monitoring sources* 
  'exclude': ["null"] // [String] | An array of facet filters. For example **city:Paris** or **modified:2019/12**. The request will exclude the defined facet value.  Read [filtering with facets value](https://help.opendatasoft.com/apis/ods-search-v2/#filtering-with-facets-values) for more details.  *Not to be confused with a where filter. Excluding a facet value is equivalent to removing an entry in the left navigation panel.*  *exclude is not available for monitoring sources* 
};
apiInstance.aggregateDatasets_1(source, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source** | **String**| Each source represents a different catalog of datasets you&#39;ll be able to query.  There are 2 sources available:  * catalog: the catalog of datasets on your portal * opendatasoft: Opendatasoft&#39;s repository of public datasets, also available at   [data.opendatasoft.com](https://data.opendatasoft.com/page/home/)  | [default to &#39;catalog&#39;]
 **select** | **String**| A select expression can be used to add, remove or change fields to return. An expression can be:   - a wildcard (&#39;*&#39;): return all fields   - a field name: return only this field   - an include/exclude function. Include (resp exclude) all field matching include/exclude expression. This expression can contain wildcard. For example: include(spa*) will return all fields begining with &#39;spa&#39;   - a complex expression: return the result of this expression. A label can be set for this expression, in that case, field will be named with this label. For instance: &#39;size * 2 as bigger_size&#39; will return a new field named bigger_size and containing the double of size field value.  | [optional] 
 **where** | [**[String]**](String.md)| An array of filters.  A filter is a text expression performing a simple full-text search that can also include logical operations (NOT, AND, OR...) as well as lots of other functions, thus performing more complex and more precise searches.  Read [the query language reference](https://docs.opendatasoft.com/api/explore/v2.html#where-clause) for more details.  | [optional] 
 **groupBy** | **String**| A group by expression defines a grouping function for an aggregation. It can be:  - a field name: group result by each value of this field  - a range function: group result by range  - a date function: group result by date It is possible to specify a custom name with the &#39;as name&#39; notation. For instance: group_by&#x3D;&#39;city_field as city&#39;.  | [optional] 
 **orderBy** | [**[String]**](String.md)| A comma-separated list of field names or aggregations to sort on, followed by an order (&#x60;asc&#x60; or &#x60;desc&#x60;).  Sorts results according to the specified fields&#39; values in ascending order by default. To sort results in descending order, use the &#x60;desc&#x60; keyword.  Example: &#x60;sum(age) desc, name asc&#x60;  | [optional] 
 **limit** | **Number**| Number of items to return.  To use in conjonction with offset to implement pagination.  Limit maximum value is 100. To retrive more data use export entry points. The default value is 10.  | [optional] [default to 10]
 **offset** | **Number**| Index of the first item to return (starting at 0).  To use in conjonction with limit to implement pagination.  | [optional] [default to 0]
 **facet** | [**[String]**](String.md)| A facet is a field used for simple filtering (through the parameters refine and exclude) or exploration (with the endpoint &#x60;/facets&#x60;).  Facets can be configured in the back-office or with this parameter.  Read [the facets documentation](https://help.opendatasoft.com/apis/ods-search-v2/#facets) for more details.  | [optional] 
 **refine** | [**[String]**](String.md)| An array of facet filters. For example **city:Paris** or **modified:2019/12**. The request will only include the selected facet value.  Read [filtering with facets value](https://help.opendatasoft.com/apis/ods-search-v2/#filtering-with-facets-values) for more details.  *Not to be confused with a where filter. Refining with a facet is equivalent to selecting an entry in the left navigation panel.*  *refine is not available for monitoring sources*  | [optional] 
 **exclude** | [**[String]**](String.md)| An array of facet filters. For example **city:Paris** or **modified:2019/12**. The request will exclude the defined facet value.  Read [filtering with facets value](https://help.opendatasoft.com/apis/ods-search-v2/#filtering-with-facets-values) for more details.  *Not to be confused with a where filter. Excluding a facet value is equivalent to removing an entry in the left navigation panel.*  *exclude is not available for monitoring sources*  | [optional] 

### Return type

[**AggregateDatasets200Response**](AggregateDatasets200Response.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## aggregateRecords_1

> AggregateDatasets200Response aggregateRecords_1(source, datasetId, opts)



**Deprecated, use &#x60;/records&#x60; instead.** 

### Example

```javascript
import Opendatasoft from 'opendatasoft';
let defaultClient = Opendatasoft.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure HTTP basic authorization: basic
let basic = defaultClient.authentications['basic'];
basic.username = 'YOUR USERNAME';
basic.password = 'YOUR PASSWORD';

let apiInstance = new Opendatasoft.OdsApi();
let source = "'catalog'"; // String | Each source represents a different catalog of datasets you'll be able to query.  There are 2 sources available:  * catalog: the catalog of datasets on your portal * opendatasoft: Opendatasoft's repository of public datasets, also available at   [data.opendatasoft.com](https://data.opendatasoft.com/page/home/) 
let datasetId = "datasetId_example"; // String | Dataset identifier.  Can be found in the \"information\" tab of the dataset page. 
let opts = {
  'select': "select_example", // String | A select expression can be used to add, remove or change fields to return. An expression can be:   - a wildcard ('*'): return all fields   - a field name: return only this field   - an include/exclude function. Include (resp exclude) all field matching include/exclude expression. This expression can contain wildcard. For example: include(spa*) will return all fields begining with 'spa'   - a complex expression: return the result of this expression. A label can be set for this expression, in that case, field will be named with this label. For instance: 'size * 2 as bigger_size' will return a new field named bigger_size and containing the double of size field value. 
  'where': ["null"], // [String] | An array of filters.  A filter is a text expression performing a simple full-text search that can also include logical operations (NOT, AND, OR...) as well as lots of other functions, thus performing more complex and more precise searches.  Read [the query language reference](https://docs.opendatasoft.com/api/explore/v2.html#where-clause) for more details. 
  'groupBy': "groupBy_example", // String | A group by expression defines a grouping function for an aggregation. It can be:  - a field name: group result by each value of this field  - a range function: group result by range  - a date function: group result by date It is possible to specify a custom name with the 'as name' notation. For instance: group_by='city_field as city'. 
  'orderBy': ["null"], // [String] | A comma-separated list of field names or aggregations to sort on, followed by an order (`asc` or `desc`).  Sorts results according to the specified fields' values in ascending order by default. To sort results in descending order, use the `desc` keyword.  Example: `sum(age) desc, name asc` 
  'limit': 10, // Number | Number of items to return.  To use in conjonction with offset to implement pagination.  Limit maximum value is 100. To retrive more data use export entry points. The default value is 10. 
  'offset': 0, // Number | Index of the first item to return (starting at 0).  To use in conjonction with limit to implement pagination. 
  'facet': ["null"], // [String] | A facet is a field used for simple filtering (through the parameters refine and exclude) or exploration (with the endpoint `/facets`).  Facets can be configured in the back-office or with this parameter.  Read [the facets documentation](https://help.opendatasoft.com/apis/ods-search-v2/#facets) for more details. 
  'refine': ["null"], // [String] | An array of facet filters. For example **city:Paris** or **modified:2019/12**. The request will only include the selected facet value.  Read [filtering with facets value](https://help.opendatasoft.com/apis/ods-search-v2/#filtering-with-facets-values) for more details.  *Not to be confused with a where filter. Refining with a facet is equivalent to selecting an entry in the left navigation panel.*  *refine is not available for monitoring sources* 
  'exclude': ["null"] // [String] | An array of facet filters. For example **city:Paris** or **modified:2019/12**. The request will exclude the defined facet value.  Read [filtering with facets value](https://help.opendatasoft.com/apis/ods-search-v2/#filtering-with-facets-values) for more details.  *Not to be confused with a where filter. Excluding a facet value is equivalent to removing an entry in the left navigation panel.*  *exclude is not available for monitoring sources* 
};
apiInstance.aggregateRecords_1(source, datasetId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source** | **String**| Each source represents a different catalog of datasets you&#39;ll be able to query.  There are 2 sources available:  * catalog: the catalog of datasets on your portal * opendatasoft: Opendatasoft&#39;s repository of public datasets, also available at   [data.opendatasoft.com](https://data.opendatasoft.com/page/home/)  | [default to &#39;catalog&#39;]
 **datasetId** | **String**| Dataset identifier.  Can be found in the \&quot;information\&quot; tab of the dataset page.  | 
 **select** | **String**| A select expression can be used to add, remove or change fields to return. An expression can be:   - a wildcard (&#39;*&#39;): return all fields   - a field name: return only this field   - an include/exclude function. Include (resp exclude) all field matching include/exclude expression. This expression can contain wildcard. For example: include(spa*) will return all fields begining with &#39;spa&#39;   - a complex expression: return the result of this expression. A label can be set for this expression, in that case, field will be named with this label. For instance: &#39;size * 2 as bigger_size&#39; will return a new field named bigger_size and containing the double of size field value.  | [optional] 
 **where** | [**[String]**](String.md)| An array of filters.  A filter is a text expression performing a simple full-text search that can also include logical operations (NOT, AND, OR...) as well as lots of other functions, thus performing more complex and more precise searches.  Read [the query language reference](https://docs.opendatasoft.com/api/explore/v2.html#where-clause) for more details.  | [optional] 
 **groupBy** | **String**| A group by expression defines a grouping function for an aggregation. It can be:  - a field name: group result by each value of this field  - a range function: group result by range  - a date function: group result by date It is possible to specify a custom name with the &#39;as name&#39; notation. For instance: group_by&#x3D;&#39;city_field as city&#39;.  | [optional] 
 **orderBy** | [**[String]**](String.md)| A comma-separated list of field names or aggregations to sort on, followed by an order (&#x60;asc&#x60; or &#x60;desc&#x60;).  Sorts results according to the specified fields&#39; values in ascending order by default. To sort results in descending order, use the &#x60;desc&#x60; keyword.  Example: &#x60;sum(age) desc, name asc&#x60;  | [optional] 
 **limit** | **Number**| Number of items to return.  To use in conjonction with offset to implement pagination.  Limit maximum value is 100. To retrive more data use export entry points. The default value is 10.  | [optional] [default to 10]
 **offset** | **Number**| Index of the first item to return (starting at 0).  To use in conjonction with limit to implement pagination.  | [optional] [default to 0]
 **facet** | [**[String]**](String.md)| A facet is a field used for simple filtering (through the parameters refine and exclude) or exploration (with the endpoint &#x60;/facets&#x60;).  Facets can be configured in the back-office or with this parameter.  Read [the facets documentation](https://help.opendatasoft.com/apis/ods-search-v2/#facets) for more details.  | [optional] 
 **refine** | [**[String]**](String.md)| An array of facet filters. For example **city:Paris** or **modified:2019/12**. The request will only include the selected facet value.  Read [filtering with facets value](https://help.opendatasoft.com/apis/ods-search-v2/#filtering-with-facets-values) for more details.  *Not to be confused with a where filter. Refining with a facet is equivalent to selecting an entry in the left navigation panel.*  *refine is not available for monitoring sources*  | [optional] 
 **exclude** | [**[String]**](String.md)| An array of facet filters. For example **city:Paris** or **modified:2019/12**. The request will exclude the defined facet value.  Read [filtering with facets value](https://help.opendatasoft.com/apis/ods-search-v2/#filtering-with-facets-values) for more details.  *Not to be confused with a where filter. Excluding a facet value is equivalent to removing an entry in the left navigation panel.*  *exclude is not available for monitoring sources*  | [optional] 

### Return type

[**AggregateDatasets200Response**](AggregateDatasets200Response.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## downloadDatasetAttachement_0

> downloadDatasetAttachement_0(source, datasetId, attachmentId)



Download attachment 

### Example

```javascript
import Opendatasoft from 'opendatasoft';
let defaultClient = Opendatasoft.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure HTTP basic authorization: basic
let basic = defaultClient.authentications['basic'];
basic.username = 'YOUR USERNAME';
basic.password = 'YOUR PASSWORD';

let apiInstance = new Opendatasoft.OdsApi();
let source = "'catalog'"; // String | Each source represents a different catalog of datasets you'll be able to query.  There are 2 sources available:  * catalog: the catalog of datasets on your portal * opendatasoft: Opendatasoft's repository of public datasets, also available at   [data.opendatasoft.com](https://data.opendatasoft.com/page/home/) 
let datasetId = "datasetId_example"; // String | Dataset identifier.  Can be found in the \"information\" tab of the dataset page. 
let attachmentId = "attachmentId_example"; // String | 
apiInstance.downloadDatasetAttachement_0(source, datasetId, attachmentId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source** | **String**| Each source represents a different catalog of datasets you&#39;ll be able to query.  There are 2 sources available:  * catalog: the catalog of datasets on your portal * opendatasoft: Opendatasoft&#39;s repository of public datasets, also available at   [data.opendatasoft.com](https://data.opendatasoft.com/page/home/)  | [default to &#39;catalog&#39;]
 **datasetId** | **String**| Dataset identifier.  Can be found in the \&quot;information\&quot; tab of the dataset page.  | 
 **attachmentId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## downloadDatasetSnapshot_0

> downloadDatasetSnapshot_0(source, datasetId, snapshotId, opts)



List of all snapshots for this dataset. 

### Example

```javascript
import Opendatasoft from 'opendatasoft';
let defaultClient = Opendatasoft.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure HTTP basic authorization: basic
let basic = defaultClient.authentications['basic'];
basic.username = 'YOUR USERNAME';
basic.password = 'YOUR PASSWORD';

let apiInstance = new Opendatasoft.OdsApi();
let source = "'catalog'"; // String | Each source represents a different catalog of datasets you'll be able to query.  There are 2 sources available:  * catalog: the catalog of datasets on your portal * opendatasoft: Opendatasoft's repository of public datasets, also available at   [data.opendatasoft.com](https://data.opendatasoft.com/page/home/) 
let datasetId = "datasetId_example"; // String | Dataset identifier.  Can be found in the \"information\" tab of the dataset page. 
let snapshotId = "snapshotId_example"; // String | 
let opts = {
  'timezone': "'UTC'" // String | Set timezone for datetime fields
};
apiInstance.downloadDatasetSnapshot_0(source, datasetId, snapshotId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source** | **String**| Each source represents a different catalog of datasets you&#39;ll be able to query.  There are 2 sources available:  * catalog: the catalog of datasets on your portal * opendatasoft: Opendatasoft&#39;s repository of public datasets, also available at   [data.opendatasoft.com](https://data.opendatasoft.com/page/home/)  | [default to &#39;catalog&#39;]
 **datasetId** | **String**| Dataset identifier.  Can be found in the \&quot;information\&quot; tab of the dataset page.  | 
 **snapshotId** | **String**|  | 
 **timezone** | **String**| Set timezone for datetime fields | [optional] [default to &#39;UTC&#39;]

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## exportDatasetsCSV_0

> File exportDatasetsCSV_0(source, opts)



Export catalog (source) in CSV format 

### Example

```javascript
import Opendatasoft from 'opendatasoft';
let defaultClient = Opendatasoft.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure HTTP basic authorization: basic
let basic = defaultClient.authentications['basic'];
basic.username = 'YOUR USERNAME';
basic.password = 'YOUR PASSWORD';

let apiInstance = new Opendatasoft.OdsApi();
let source = "'catalog'"; // String | Each source represents a different catalog of datasets you'll be able to query.  There are 2 sources available:  * catalog: the catalog of datasets on your portal * opendatasoft: Opendatasoft's repository of public datasets, also available at   [data.opendatasoft.com](https://data.opendatasoft.com/page/home/) 
let opts = {
  'where': ["null"], // [String] | An array of filters.  A filter is a text expression performing a simple full-text search that can also include logical operations (NOT, AND, OR...) as well as lots of other functions, thus performing more complex and more precise searches.  Read [the query language reference](https://docs.opendatasoft.com/api/explore/v2.html#where-clause) for more details. 
  'limit': 10, // Number | Number of items to return.  To use in conjonction with offset to implement pagination.  Limit maximum value is 100. To retrive more data use export entry points. The default value is 10. 
  'offset': 0, // Number | Index of the first item to return (starting at 0).  To use in conjonction with limit to implement pagination. 
  'search': ["null"], // [String] | An array of full text search.  A full text search performs a prefixed text search for each provided terms in all visible fields of a catalog/dataset. 
  'facet': ["null"], // [String] | A facet is a field used for simple filtering (through the parameters refine and exclude) or exploration (with the endpoint `/facets`).  Facets can be configured in the back-office or with this parameter.  Read [the facets documentation](https://help.opendatasoft.com/apis/ods-search-v2/#facets) for more details. 
  'refine': ["null"], // [String] | An array of facet filters. For example **city:Paris** or **modified:2019/12**. The request will only include the selected facet value.  Read [filtering with facets value](https://help.opendatasoft.com/apis/ods-search-v2/#filtering-with-facets-values) for more details.  *Not to be confused with a where filter. Refining with a facet is equivalent to selecting an entry in the left navigation panel.*  *refine is not available for monitoring sources* 
  'exclude': ["null"], // [String] | An array of facet filters. For example **city:Paris** or **modified:2019/12**. The request will exclude the defined facet value.  Read [filtering with facets value](https://help.opendatasoft.com/apis/ods-search-v2/#filtering-with-facets-values) for more details.  *Not to be confused with a where filter. Excluding a facet value is equivalent to removing an entry in the left navigation panel.*  *exclude is not available for monitoring sources* 
  'timezone': "'UTC'", // String | Set timezone for datetime fields
  'includeAppMetas': false, // Boolean | Explicitely request application metas for each datasets. 
  'delimiter': "';'" // String | Provide a different delimiter (default ',').
};
apiInstance.exportDatasetsCSV_0(source, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source** | **String**| Each source represents a different catalog of datasets you&#39;ll be able to query.  There are 2 sources available:  * catalog: the catalog of datasets on your portal * opendatasoft: Opendatasoft&#39;s repository of public datasets, also available at   [data.opendatasoft.com](https://data.opendatasoft.com/page/home/)  | [default to &#39;catalog&#39;]
 **where** | [**[String]**](String.md)| An array of filters.  A filter is a text expression performing a simple full-text search that can also include logical operations (NOT, AND, OR...) as well as lots of other functions, thus performing more complex and more precise searches.  Read [the query language reference](https://docs.opendatasoft.com/api/explore/v2.html#where-clause) for more details.  | [optional] 
 **limit** | **Number**| Number of items to return.  To use in conjonction with offset to implement pagination.  Limit maximum value is 100. To retrive more data use export entry points. The default value is 10.  | [optional] [default to 10]
 **offset** | **Number**| Index of the first item to return (starting at 0).  To use in conjonction with limit to implement pagination.  | [optional] [default to 0]
 **search** | [**[String]**](String.md)| An array of full text search.  A full text search performs a prefixed text search for each provided terms in all visible fields of a catalog/dataset.  | [optional] 
 **facet** | [**[String]**](String.md)| A facet is a field used for simple filtering (through the parameters refine and exclude) or exploration (with the endpoint &#x60;/facets&#x60;).  Facets can be configured in the back-office or with this parameter.  Read [the facets documentation](https://help.opendatasoft.com/apis/ods-search-v2/#facets) for more details.  | [optional] 
 **refine** | [**[String]**](String.md)| An array of facet filters. For example **city:Paris** or **modified:2019/12**. The request will only include the selected facet value.  Read [filtering with facets value](https://help.opendatasoft.com/apis/ods-search-v2/#filtering-with-facets-values) for more details.  *Not to be confused with a where filter. Refining with a facet is equivalent to selecting an entry in the left navigation panel.*  *refine is not available for monitoring sources*  | [optional] 
 **exclude** | [**[String]**](String.md)| An array of facet filters. For example **city:Paris** or **modified:2019/12**. The request will exclude the defined facet value.  Read [filtering with facets value](https://help.opendatasoft.com/apis/ods-search-v2/#filtering-with-facets-values) for more details.  *Not to be confused with a where filter. Excluding a facet value is equivalent to removing an entry in the left navigation panel.*  *exclude is not available for monitoring sources*  | [optional] 
 **timezone** | **String**| Set timezone for datetime fields | [optional] [default to &#39;UTC&#39;]
 **includeAppMetas** | **Boolean**| Explicitely request application metas for each datasets.  | [optional] [default to false]
 **delimiter** | **String**| Provide a different delimiter (default &#39;,&#39;). | [optional] [default to &#39;;&#39;]

### Return type

**File**

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/csv


## exportDatasetsJson_0

> File exportDatasetsJson_0(source, opts)



Export catalog (source) in JSON format 

### Example

```javascript
import Opendatasoft from 'opendatasoft';
let defaultClient = Opendatasoft.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure HTTP basic authorization: basic
let basic = defaultClient.authentications['basic'];
basic.username = 'YOUR USERNAME';
basic.password = 'YOUR PASSWORD';

let apiInstance = new Opendatasoft.OdsApi();
let source = "'catalog'"; // String | Each source represents a different catalog of datasets you'll be able to query.  There are 2 sources available:  * catalog: the catalog of datasets on your portal * opendatasoft: Opendatasoft's repository of public datasets, also available at   [data.opendatasoft.com](https://data.opendatasoft.com/page/home/) 
let opts = {
  'where': ["null"], // [String] | An array of filters.  A filter is a text expression performing a simple full-text search that can also include logical operations (NOT, AND, OR...) as well as lots of other functions, thus performing more complex and more precise searches.  Read [the query language reference](https://docs.opendatasoft.com/api/explore/v2.html#where-clause) for more details. 
  'limit': 10, // Number | Number of items to return.  To use in conjonction with offset to implement pagination.  Limit maximum value is 100. To retrive more data use export entry points. The default value is 10. 
  'offset': 0, // Number | Index of the first item to return (starting at 0).  To use in conjonction with limit to implement pagination. 
  'search': ["null"], // [String] | An array of full text search.  A full text search performs a prefixed text search for each provided terms in all visible fields of a catalog/dataset. 
  'facet': ["null"], // [String] | A facet is a field used for simple filtering (through the parameters refine and exclude) or exploration (with the endpoint `/facets`).  Facets can be configured in the back-office or with this parameter.  Read [the facets documentation](https://help.opendatasoft.com/apis/ods-search-v2/#facets) for more details. 
  'refine': ["null"], // [String] | An array of facet filters. For example **city:Paris** or **modified:2019/12**. The request will only include the selected facet value.  Read [filtering with facets value](https://help.opendatasoft.com/apis/ods-search-v2/#filtering-with-facets-values) for more details.  *Not to be confused with a where filter. Refining with a facet is equivalent to selecting an entry in the left navigation panel.*  *refine is not available for monitoring sources* 
  'exclude': ["null"], // [String] | An array of facet filters. For example **city:Paris** or **modified:2019/12**. The request will exclude the defined facet value.  Read [filtering with facets value](https://help.opendatasoft.com/apis/ods-search-v2/#filtering-with-facets-values) for more details.  *Not to be confused with a where filter. Excluding a facet value is equivalent to removing an entry in the left navigation panel.*  *exclude is not available for monitoring sources* 
  'pretty': false, // Boolean | Activate pretty print
  'timezone': "'UTC'", // String | Set timezone for datetime fields
  'includeAppMetas': false // Boolean | Explicitely request application metas for each datasets. 
};
apiInstance.exportDatasetsJson_0(source, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source** | **String**| Each source represents a different catalog of datasets you&#39;ll be able to query.  There are 2 sources available:  * catalog: the catalog of datasets on your portal * opendatasoft: Opendatasoft&#39;s repository of public datasets, also available at   [data.opendatasoft.com](https://data.opendatasoft.com/page/home/)  | [default to &#39;catalog&#39;]
 **where** | [**[String]**](String.md)| An array of filters.  A filter is a text expression performing a simple full-text search that can also include logical operations (NOT, AND, OR...) as well as lots of other functions, thus performing more complex and more precise searches.  Read [the query language reference](https://docs.opendatasoft.com/api/explore/v2.html#where-clause) for more details.  | [optional] 
 **limit** | **Number**| Number of items to return.  To use in conjonction with offset to implement pagination.  Limit maximum value is 100. To retrive more data use export entry points. The default value is 10.  | [optional] [default to 10]
 **offset** | **Number**| Index of the first item to return (starting at 0).  To use in conjonction with limit to implement pagination.  | [optional] [default to 0]
 **search** | [**[String]**](String.md)| An array of full text search.  A full text search performs a prefixed text search for each provided terms in all visible fields of a catalog/dataset.  | [optional] 
 **facet** | [**[String]**](String.md)| A facet is a field used for simple filtering (through the parameters refine and exclude) or exploration (with the endpoint &#x60;/facets&#x60;).  Facets can be configured in the back-office or with this parameter.  Read [the facets documentation](https://help.opendatasoft.com/apis/ods-search-v2/#facets) for more details.  | [optional] 
 **refine** | [**[String]**](String.md)| An array of facet filters. For example **city:Paris** or **modified:2019/12**. The request will only include the selected facet value.  Read [filtering with facets value](https://help.opendatasoft.com/apis/ods-search-v2/#filtering-with-facets-values) for more details.  *Not to be confused with a where filter. Refining with a facet is equivalent to selecting an entry in the left navigation panel.*  *refine is not available for monitoring sources*  | [optional] 
 **exclude** | [**[String]**](String.md)| An array of facet filters. For example **city:Paris** or **modified:2019/12**. The request will exclude the defined facet value.  Read [filtering with facets value](https://help.opendatasoft.com/apis/ods-search-v2/#filtering-with-facets-values) for more details.  *Not to be confused with a where filter. Excluding a facet value is equivalent to removing an entry in the left navigation panel.*  *exclude is not available for monitoring sources*  | [optional] 
 **pretty** | **Boolean**| Activate pretty print | [optional] [default to false]
 **timezone** | **String**| Set timezone for datetime fields | [optional] [default to &#39;UTC&#39;]
 **includeAppMetas** | **Boolean**| Explicitely request application metas for each datasets.  | [optional] [default to false]

### Return type

**File**

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## exportDatasetsRDF_0

> File exportDatasetsRDF_0(source, opts)



Export catalog (source) in RDF/XML format 

### Example

```javascript
import Opendatasoft from 'opendatasoft';
let defaultClient = Opendatasoft.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure HTTP basic authorization: basic
let basic = defaultClient.authentications['basic'];
basic.username = 'YOUR USERNAME';
basic.password = 'YOUR PASSWORD';

let apiInstance = new Opendatasoft.OdsApi();
let source = "'catalog'"; // String | Each source represents a different catalog of datasets you'll be able to query.  There are 2 sources available:  * catalog: the catalog of datasets on your portal * opendatasoft: Opendatasoft's repository of public datasets, also available at   [data.opendatasoft.com](https://data.opendatasoft.com/page/home/) 
let opts = {
  'where': ["null"], // [String] | An array of filters.  A filter is a text expression performing a simple full-text search that can also include logical operations (NOT, AND, OR...) as well as lots of other functions, thus performing more complex and more precise searches.  Read [the query language reference](https://docs.opendatasoft.com/api/explore/v2.html#where-clause) for more details. 
  'limit': 10, // Number | Number of items to return.  To use in conjonction with offset to implement pagination.  Limit maximum value is 100. To retrive more data use export entry points. The default value is 10. 
  'offset': 0, // Number | Index of the first item to return (starting at 0).  To use in conjonction with limit to implement pagination. 
  'search': ["null"], // [String] | An array of full text search.  A full text search performs a prefixed text search for each provided terms in all visible fields of a catalog/dataset. 
  'facet': ["null"], // [String] | A facet is a field used for simple filtering (through the parameters refine and exclude) or exploration (with the endpoint `/facets`).  Facets can be configured in the back-office or with this parameter.  Read [the facets documentation](https://help.opendatasoft.com/apis/ods-search-v2/#facets) for more details. 
  'refine': ["null"], // [String] | An array of facet filters. For example **city:Paris** or **modified:2019/12**. The request will only include the selected facet value.  Read [filtering with facets value](https://help.opendatasoft.com/apis/ods-search-v2/#filtering-with-facets-values) for more details.  *Not to be confused with a where filter. Refining with a facet is equivalent to selecting an entry in the left navigation panel.*  *refine is not available for monitoring sources* 
  'exclude': ["null"], // [String] | An array of facet filters. For example **city:Paris** or **modified:2019/12**. The request will exclude the defined facet value.  Read [filtering with facets value](https://help.opendatasoft.com/apis/ods-search-v2/#filtering-with-facets-values) for more details.  *Not to be confused with a where filter. Excluding a facet value is equivalent to removing an entry in the left navigation panel.*  *exclude is not available for monitoring sources* 
  'timezone': "'UTC'", // String | Set timezone for datetime fields
  'includeAppMetas': false // Boolean | Explicitely request application metas for each datasets. 
};
apiInstance.exportDatasetsRDF_0(source, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source** | **String**| Each source represents a different catalog of datasets you&#39;ll be able to query.  There are 2 sources available:  * catalog: the catalog of datasets on your portal * opendatasoft: Opendatasoft&#39;s repository of public datasets, also available at   [data.opendatasoft.com](https://data.opendatasoft.com/page/home/)  | [default to &#39;catalog&#39;]
 **where** | [**[String]**](String.md)| An array of filters.  A filter is a text expression performing a simple full-text search that can also include logical operations (NOT, AND, OR...) as well as lots of other functions, thus performing more complex and more precise searches.  Read [the query language reference](https://docs.opendatasoft.com/api/explore/v2.html#where-clause) for more details.  | [optional] 
 **limit** | **Number**| Number of items to return.  To use in conjonction with offset to implement pagination.  Limit maximum value is 100. To retrive more data use export entry points. The default value is 10.  | [optional] [default to 10]
 **offset** | **Number**| Index of the first item to return (starting at 0).  To use in conjonction with limit to implement pagination.  | [optional] [default to 0]
 **search** | [**[String]**](String.md)| An array of full text search.  A full text search performs a prefixed text search for each provided terms in all visible fields of a catalog/dataset.  | [optional] 
 **facet** | [**[String]**](String.md)| A facet is a field used for simple filtering (through the parameters refine and exclude) or exploration (with the endpoint &#x60;/facets&#x60;).  Facets can be configured in the back-office or with this parameter.  Read [the facets documentation](https://help.opendatasoft.com/apis/ods-search-v2/#facets) for more details.  | [optional] 
 **refine** | [**[String]**](String.md)| An array of facet filters. For example **city:Paris** or **modified:2019/12**. The request will only include the selected facet value.  Read [filtering with facets value](https://help.opendatasoft.com/apis/ods-search-v2/#filtering-with-facets-values) for more details.  *Not to be confused with a where filter. Refining with a facet is equivalent to selecting an entry in the left navigation panel.*  *refine is not available for monitoring sources*  | [optional] 
 **exclude** | [**[String]**](String.md)| An array of facet filters. For example **city:Paris** or **modified:2019/12**. The request will exclude the defined facet value.  Read [filtering with facets value](https://help.opendatasoft.com/apis/ods-search-v2/#filtering-with-facets-values) for more details.  *Not to be confused with a where filter. Excluding a facet value is equivalent to removing an entry in the left navigation panel.*  *exclude is not available for monitoring sources*  | [optional] 
 **timezone** | **String**| Set timezone for datetime fields | [optional] [default to &#39;UTC&#39;]
 **includeAppMetas** | **Boolean**| Explicitely request application metas for each datasets.  | [optional] [default to false]

### Return type

**File**

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/rdf+xml


## exportDatasetsRSS_0

> File exportDatasetsRSS_0(source, opts)



Export catalog (source) in RSS format 

### Example

```javascript
import Opendatasoft from 'opendatasoft';
let defaultClient = Opendatasoft.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure HTTP basic authorization: basic
let basic = defaultClient.authentications['basic'];
basic.username = 'YOUR USERNAME';
basic.password = 'YOUR PASSWORD';

let apiInstance = new Opendatasoft.OdsApi();
let source = "'catalog'"; // String | Each source represents a different catalog of datasets you'll be able to query.  There are 2 sources available:  * catalog: the catalog of datasets on your portal * opendatasoft: Opendatasoft's repository of public datasets, also available at   [data.opendatasoft.com](https://data.opendatasoft.com/page/home/) 
let opts = {
  'where': ["null"], // [String] | An array of filters.  A filter is a text expression performing a simple full-text search that can also include logical operations (NOT, AND, OR...) as well as lots of other functions, thus performing more complex and more precise searches.  Read [the query language reference](https://docs.opendatasoft.com/api/explore/v2.html#where-clause) for more details. 
  'limit': 10, // Number | Number of items to return.  To use in conjonction with offset to implement pagination.  Limit maximum value is 100. To retrive more data use export entry points. The default value is 10. 
  'offset': 0, // Number | Index of the first item to return (starting at 0).  To use in conjonction with limit to implement pagination. 
  'search': ["null"], // [String] | An array of full text search.  A full text search performs a prefixed text search for each provided terms in all visible fields of a catalog/dataset. 
  'facet': ["null"], // [String] | A facet is a field used for simple filtering (through the parameters refine and exclude) or exploration (with the endpoint `/facets`).  Facets can be configured in the back-office or with this parameter.  Read [the facets documentation](https://help.opendatasoft.com/apis/ods-search-v2/#facets) for more details. 
  'refine': ["null"], // [String] | An array of facet filters. For example **city:Paris** or **modified:2019/12**. The request will only include the selected facet value.  Read [filtering with facets value](https://help.opendatasoft.com/apis/ods-search-v2/#filtering-with-facets-values) for more details.  *Not to be confused with a where filter. Refining with a facet is equivalent to selecting an entry in the left navigation panel.*  *refine is not available for monitoring sources* 
  'exclude': ["null"], // [String] | An array of facet filters. For example **city:Paris** or **modified:2019/12**. The request will exclude the defined facet value.  Read [filtering with facets value](https://help.opendatasoft.com/apis/ods-search-v2/#filtering-with-facets-values) for more details.  *Not to be confused with a where filter. Excluding a facet value is equivalent to removing an entry in the left navigation panel.*  *exclude is not available for monitoring sources* 
  'timezone': "'UTC'", // String | Set timezone for datetime fields
  'includeAppMetas': false // Boolean | Explicitely request application metas for each datasets. 
};
apiInstance.exportDatasetsRSS_0(source, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source** | **String**| Each source represents a different catalog of datasets you&#39;ll be able to query.  There are 2 sources available:  * catalog: the catalog of datasets on your portal * opendatasoft: Opendatasoft&#39;s repository of public datasets, also available at   [data.opendatasoft.com](https://data.opendatasoft.com/page/home/)  | [default to &#39;catalog&#39;]
 **where** | [**[String]**](String.md)| An array of filters.  A filter is a text expression performing a simple full-text search that can also include logical operations (NOT, AND, OR...) as well as lots of other functions, thus performing more complex and more precise searches.  Read [the query language reference](https://docs.opendatasoft.com/api/explore/v2.html#where-clause) for more details.  | [optional] 
 **limit** | **Number**| Number of items to return.  To use in conjonction with offset to implement pagination.  Limit maximum value is 100. To retrive more data use export entry points. The default value is 10.  | [optional] [default to 10]
 **offset** | **Number**| Index of the first item to return (starting at 0).  To use in conjonction with limit to implement pagination.  | [optional] [default to 0]
 **search** | [**[String]**](String.md)| An array of full text search.  A full text search performs a prefixed text search for each provided terms in all visible fields of a catalog/dataset.  | [optional] 
 **facet** | [**[String]**](String.md)| A facet is a field used for simple filtering (through the parameters refine and exclude) or exploration (with the endpoint &#x60;/facets&#x60;).  Facets can be configured in the back-office or with this parameter.  Read [the facets documentation](https://help.opendatasoft.com/apis/ods-search-v2/#facets) for more details.  | [optional] 
 **refine** | [**[String]**](String.md)| An array of facet filters. For example **city:Paris** or **modified:2019/12**. The request will only include the selected facet value.  Read [filtering with facets value](https://help.opendatasoft.com/apis/ods-search-v2/#filtering-with-facets-values) for more details.  *Not to be confused with a where filter. Refining with a facet is equivalent to selecting an entry in the left navigation panel.*  *refine is not available for monitoring sources*  | [optional] 
 **exclude** | [**[String]**](String.md)| An array of facet filters. For example **city:Paris** or **modified:2019/12**. The request will exclude the defined facet value.  Read [filtering with facets value](https://help.opendatasoft.com/apis/ods-search-v2/#filtering-with-facets-values) for more details.  *Not to be confused with a where filter. Excluding a facet value is equivalent to removing an entry in the left navigation panel.*  *exclude is not available for monitoring sources*  | [optional] 
 **timezone** | **String**| Set timezone for datetime fields | [optional] [default to &#39;UTC&#39;]
 **includeAppMetas** | **Boolean**| Explicitely request application metas for each datasets.  | [optional] [default to false]

### Return type

**File**

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/xml


## exportDatasetsTTL_0

> File exportDatasetsTTL_0(source, opts)



Export catalog (source) in TTL (turtle/rdf) format 

### Example

```javascript
import Opendatasoft from 'opendatasoft';
let defaultClient = Opendatasoft.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure HTTP basic authorization: basic
let basic = defaultClient.authentications['basic'];
basic.username = 'YOUR USERNAME';
basic.password = 'YOUR PASSWORD';

let apiInstance = new Opendatasoft.OdsApi();
let source = "'catalog'"; // String | Each source represents a different catalog of datasets you'll be able to query.  There are 2 sources available:  * catalog: the catalog of datasets on your portal * opendatasoft: Opendatasoft's repository of public datasets, also available at   [data.opendatasoft.com](https://data.opendatasoft.com/page/home/) 
let opts = {
  'where': ["null"], // [String] | An array of filters.  A filter is a text expression performing a simple full-text search that can also include logical operations (NOT, AND, OR...) as well as lots of other functions, thus performing more complex and more precise searches.  Read [the query language reference](https://docs.opendatasoft.com/api/explore/v2.html#where-clause) for more details. 
  'limit': 10, // Number | Number of items to return.  To use in conjonction with offset to implement pagination.  Limit maximum value is 100. To retrive more data use export entry points. The default value is 10. 
  'offset': 0, // Number | Index of the first item to return (starting at 0).  To use in conjonction with limit to implement pagination. 
  'search': ["null"], // [String] | An array of full text search.  A full text search performs a prefixed text search for each provided terms in all visible fields of a catalog/dataset. 
  'facet': ["null"], // [String] | A facet is a field used for simple filtering (through the parameters refine and exclude) or exploration (with the endpoint `/facets`).  Facets can be configured in the back-office or with this parameter.  Read [the facets documentation](https://help.opendatasoft.com/apis/ods-search-v2/#facets) for more details. 
  'refine': ["null"], // [String] | An array of facet filters. For example **city:Paris** or **modified:2019/12**. The request will only include the selected facet value.  Read [filtering with facets value](https://help.opendatasoft.com/apis/ods-search-v2/#filtering-with-facets-values) for more details.  *Not to be confused with a where filter. Refining with a facet is equivalent to selecting an entry in the left navigation panel.*  *refine is not available for monitoring sources* 
  'exclude': ["null"], // [String] | An array of facet filters. For example **city:Paris** or **modified:2019/12**. The request will exclude the defined facet value.  Read [filtering with facets value](https://help.opendatasoft.com/apis/ods-search-v2/#filtering-with-facets-values) for more details.  *Not to be confused with a where filter. Excluding a facet value is equivalent to removing an entry in the left navigation panel.*  *exclude is not available for monitoring sources* 
  'timezone': "'UTC'", // String | Set timezone for datetime fields
  'includeAppMetas': false // Boolean | Explicitely request application metas for each datasets. 
};
apiInstance.exportDatasetsTTL_0(source, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source** | **String**| Each source represents a different catalog of datasets you&#39;ll be able to query.  There are 2 sources available:  * catalog: the catalog of datasets on your portal * opendatasoft: Opendatasoft&#39;s repository of public datasets, also available at   [data.opendatasoft.com](https://data.opendatasoft.com/page/home/)  | [default to &#39;catalog&#39;]
 **where** | [**[String]**](String.md)| An array of filters.  A filter is a text expression performing a simple full-text search that can also include logical operations (NOT, AND, OR...) as well as lots of other functions, thus performing more complex and more precise searches.  Read [the query language reference](https://docs.opendatasoft.com/api/explore/v2.html#where-clause) for more details.  | [optional] 
 **limit** | **Number**| Number of items to return.  To use in conjonction with offset to implement pagination.  Limit maximum value is 100. To retrive more data use export entry points. The default value is 10.  | [optional] [default to 10]
 **offset** | **Number**| Index of the first item to return (starting at 0).  To use in conjonction with limit to implement pagination.  | [optional] [default to 0]
 **search** | [**[String]**](String.md)| An array of full text search.  A full text search performs a prefixed text search for each provided terms in all visible fields of a catalog/dataset.  | [optional] 
 **facet** | [**[String]**](String.md)| A facet is a field used for simple filtering (through the parameters refine and exclude) or exploration (with the endpoint &#x60;/facets&#x60;).  Facets can be configured in the back-office or with this parameter.  Read [the facets documentation](https://help.opendatasoft.com/apis/ods-search-v2/#facets) for more details.  | [optional] 
 **refine** | [**[String]**](String.md)| An array of facet filters. For example **city:Paris** or **modified:2019/12**. The request will only include the selected facet value.  Read [filtering with facets value](https://help.opendatasoft.com/apis/ods-search-v2/#filtering-with-facets-values) for more details.  *Not to be confused with a where filter. Refining with a facet is equivalent to selecting an entry in the left navigation panel.*  *refine is not available for monitoring sources*  | [optional] 
 **exclude** | [**[String]**](String.md)| An array of facet filters. For example **city:Paris** or **modified:2019/12**. The request will exclude the defined facet value.  Read [filtering with facets value](https://help.opendatasoft.com/apis/ods-search-v2/#filtering-with-facets-values) for more details.  *Not to be confused with a where filter. Excluding a facet value is equivalent to removing an entry in the left navigation panel.*  *exclude is not available for monitoring sources*  | [optional] 
 **timezone** | **String**| Set timezone for datetime fields | [optional] [default to &#39;UTC&#39;]
 **includeAppMetas** | **Boolean**| Explicitely request application metas for each datasets.  | [optional] [default to false]

### Return type

**File**

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/turtle


## exportDatasetsXLS_0

> File exportDatasetsXLS_0(source, opts)



Export catalog (source) in XLS (Excel) format 

### Example

```javascript
import Opendatasoft from 'opendatasoft';
let defaultClient = Opendatasoft.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure HTTP basic authorization: basic
let basic = defaultClient.authentications['basic'];
basic.username = 'YOUR USERNAME';
basic.password = 'YOUR PASSWORD';

let apiInstance = new Opendatasoft.OdsApi();
let source = "'catalog'"; // String | Each source represents a different catalog of datasets you'll be able to query.  There are 2 sources available:  * catalog: the catalog of datasets on your portal * opendatasoft: Opendatasoft's repository of public datasets, also available at   [data.opendatasoft.com](https://data.opendatasoft.com/page/home/) 
let opts = {
  'where': ["null"], // [String] | An array of filters.  A filter is a text expression performing a simple full-text search that can also include logical operations (NOT, AND, OR...) as well as lots of other functions, thus performing more complex and more precise searches.  Read [the query language reference](https://docs.opendatasoft.com/api/explore/v2.html#where-clause) for more details. 
  'limit': 10, // Number | Number of items to return.  To use in conjonction with offset to implement pagination.  Limit maximum value is 100. To retrive more data use export entry points. The default value is 10. 
  'offset': 0, // Number | Index of the first item to return (starting at 0).  To use in conjonction with limit to implement pagination. 
  'search': ["null"], // [String] | An array of full text search.  A full text search performs a prefixed text search for each provided terms in all visible fields of a catalog/dataset. 
  'facet': ["null"], // [String] | A facet is a field used for simple filtering (through the parameters refine and exclude) or exploration (with the endpoint `/facets`).  Facets can be configured in the back-office or with this parameter.  Read [the facets documentation](https://help.opendatasoft.com/apis/ods-search-v2/#facets) for more details. 
  'refine': ["null"], // [String] | An array of facet filters. For example **city:Paris** or **modified:2019/12**. The request will only include the selected facet value.  Read [filtering with facets value](https://help.opendatasoft.com/apis/ods-search-v2/#filtering-with-facets-values) for more details.  *Not to be confused with a where filter. Refining with a facet is equivalent to selecting an entry in the left navigation panel.*  *refine is not available for monitoring sources* 
  'exclude': ["null"], // [String] | An array of facet filters. For example **city:Paris** or **modified:2019/12**. The request will exclude the defined facet value.  Read [filtering with facets value](https://help.opendatasoft.com/apis/ods-search-v2/#filtering-with-facets-values) for more details.  *Not to be confused with a where filter. Excluding a facet value is equivalent to removing an entry in the left navigation panel.*  *exclude is not available for monitoring sources* 
  'timezone': "'UTC'", // String | Set timezone for datetime fields
  'includeAppMetas': false // Boolean | Explicitely request application metas for each datasets. 
};
apiInstance.exportDatasetsXLS_0(source, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source** | **String**| Each source represents a different catalog of datasets you&#39;ll be able to query.  There are 2 sources available:  * catalog: the catalog of datasets on your portal * opendatasoft: Opendatasoft&#39;s repository of public datasets, also available at   [data.opendatasoft.com](https://data.opendatasoft.com/page/home/)  | [default to &#39;catalog&#39;]
 **where** | [**[String]**](String.md)| An array of filters.  A filter is a text expression performing a simple full-text search that can also include logical operations (NOT, AND, OR...) as well as lots of other functions, thus performing more complex and more precise searches.  Read [the query language reference](https://docs.opendatasoft.com/api/explore/v2.html#where-clause) for more details.  | [optional] 
 **limit** | **Number**| Number of items to return.  To use in conjonction with offset to implement pagination.  Limit maximum value is 100. To retrive more data use export entry points. The default value is 10.  | [optional] [default to 10]
 **offset** | **Number**| Index of the first item to return (starting at 0).  To use in conjonction with limit to implement pagination.  | [optional] [default to 0]
 **search** | [**[String]**](String.md)| An array of full text search.  A full text search performs a prefixed text search for each provided terms in all visible fields of a catalog/dataset.  | [optional] 
 **facet** | [**[String]**](String.md)| A facet is a field used for simple filtering (through the parameters refine and exclude) or exploration (with the endpoint &#x60;/facets&#x60;).  Facets can be configured in the back-office or with this parameter.  Read [the facets documentation](https://help.opendatasoft.com/apis/ods-search-v2/#facets) for more details.  | [optional] 
 **refine** | [**[String]**](String.md)| An array of facet filters. For example **city:Paris** or **modified:2019/12**. The request will only include the selected facet value.  Read [filtering with facets value](https://help.opendatasoft.com/apis/ods-search-v2/#filtering-with-facets-values) for more details.  *Not to be confused with a where filter. Refining with a facet is equivalent to selecting an entry in the left navigation panel.*  *refine is not available for monitoring sources*  | [optional] 
 **exclude** | [**[String]**](String.md)| An array of facet filters. For example **city:Paris** or **modified:2019/12**. The request will exclude the defined facet value.  Read [filtering with facets value](https://help.opendatasoft.com/apis/ods-search-v2/#filtering-with-facets-values) for more details.  *Not to be confused with a where filter. Excluding a facet value is equivalent to removing an entry in the left navigation panel.*  *exclude is not available for monitoring sources*  | [optional] 
 **timezone** | **String**| Set timezone for datetime fields | [optional] [default to &#39;UTC&#39;]
 **includeAppMetas** | **Boolean**| Explicitely request application metas for each datasets.  | [optional] [default to false]

### Return type

**File**

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: xls


## exportRecordsCSV_0

> File exportRecordsCSV_0(source, datasetId, opts)



Export dataset in CSV format 

### Example

```javascript
import Opendatasoft from 'opendatasoft';
let defaultClient = Opendatasoft.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure HTTP basic authorization: basic
let basic = defaultClient.authentications['basic'];
basic.username = 'YOUR USERNAME';
basic.password = 'YOUR PASSWORD';

let apiInstance = new Opendatasoft.OdsApi();
let source = "'catalog'"; // String | Each source represents a different catalog of datasets you'll be able to query.  There are 2 sources available:  * catalog: the catalog of datasets on your portal * opendatasoft: Opendatasoft's repository of public datasets, also available at   [data.opendatasoft.com](https://data.opendatasoft.com/page/home/) 
let datasetId = "datasetId_example"; // String | Dataset identifier.  Can be found in the \"information\" tab of the dataset page. 
let opts = {
  'select': "select_example", // String | A select expression can be used to add, remove or change fields to return. An expression can be:   - a wildcard ('*'): return all fields   - a field name: return only this field   - an include/exclude function. Include (resp exclude) all field matching include/exclude expression. This expression can contain wildcard. For example: include(spa*) will return all fields begining with 'spa'   - a complex expression: return the result of this expression. A label can be set for this expression, in that case, field will be named with this label. For instance: 'size * 2 as bigger_size' will return a new field named bigger_size and containing the double of size field value. 
  'where': ["null"], // [String] | An array of filters.  A filter is a text expression performing a simple full-text search that can also include logical operations (NOT, AND, OR...) as well as lots of other functions, thus performing more complex and more precise searches.  Read [the query language reference](https://docs.opendatasoft.com/api/explore/v2.html#where-clause) for more details. 
  'sort': ["null"], // [String] | **Deprecated, use `order_by` instead.**  A list of field names, each possibly prefixed with a minus (-).  Sorts results according to the specified fields' values. By default, the sort is ascending (from the smallest value to the biggest value). A minus sign (‘-‘) may be used to perform a descending sort. Sorting is only available on numeric fields (int, double, date and datetime) and on text fields which have the sortable annotation. 
  'orderBy': ["null"], // [String] | A comma-separated list of field names or aggregations to sort on, followed by an order (`asc` or `desc`).  Sorts results according to the specified fields' values in ascending order by default. To sort results in descending order, use the `desc` keyword.  Example: `sum(age) desc, name asc` 
  'limit': -1, // Number | Number of items to return in export.  Use -1 (default) to retrieve all records 
  'offset': 0, // Number | Index of the first item to return (starting at 0).  To use in conjonction with limit to implement pagination. 
  'facet': ["null"], // [String] | A facet is a field used for simple filtering (through the parameters refine and exclude) or exploration (with the endpoint `/facets`).  Facets can be configured in the back-office or with this parameter.  Read [the facets documentation](https://help.opendatasoft.com/apis/ods-search-v2/#facets) for more details. 
  'refine': ["null"], // [String] | An array of facet filters. For example **city:Paris** or **modified:2019/12**. The request will only include the selected facet value.  Read [filtering with facets value](https://help.opendatasoft.com/apis/ods-search-v2/#filtering-with-facets-values) for more details.  *Not to be confused with a where filter. Refining with a facet is equivalent to selecting an entry in the left navigation panel.*  *refine is not available for monitoring sources* 
  'exclude': ["null"], // [String] | An array of facet filters. For example **city:Paris** or **modified:2019/12**. The request will exclude the defined facet value.  Read [filtering with facets value](https://help.opendatasoft.com/apis/ods-search-v2/#filtering-with-facets-values) for more details.  *Not to be confused with a where filter. Excluding a facet value is equivalent to removing an entry in the left navigation panel.*  *exclude is not available for monitoring sources* 
  'timezone': "'UTC'", // String | Set timezone for datetime fields
  'delimiter': "';'" // String | Provide a different delimiter (default ',').
};
apiInstance.exportRecordsCSV_0(source, datasetId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source** | **String**| Each source represents a different catalog of datasets you&#39;ll be able to query.  There are 2 sources available:  * catalog: the catalog of datasets on your portal * opendatasoft: Opendatasoft&#39;s repository of public datasets, also available at   [data.opendatasoft.com](https://data.opendatasoft.com/page/home/)  | [default to &#39;catalog&#39;]
 **datasetId** | **String**| Dataset identifier.  Can be found in the \&quot;information\&quot; tab of the dataset page.  | 
 **select** | **String**| A select expression can be used to add, remove or change fields to return. An expression can be:   - a wildcard (&#39;*&#39;): return all fields   - a field name: return only this field   - an include/exclude function. Include (resp exclude) all field matching include/exclude expression. This expression can contain wildcard. For example: include(spa*) will return all fields begining with &#39;spa&#39;   - a complex expression: return the result of this expression. A label can be set for this expression, in that case, field will be named with this label. For instance: &#39;size * 2 as bigger_size&#39; will return a new field named bigger_size and containing the double of size field value.  | [optional] 
 **where** | [**[String]**](String.md)| An array of filters.  A filter is a text expression performing a simple full-text search that can also include logical operations (NOT, AND, OR...) as well as lots of other functions, thus performing more complex and more precise searches.  Read [the query language reference](https://docs.opendatasoft.com/api/explore/v2.html#where-clause) for more details.  | [optional] 
 **sort** | [**[String]**](String.md)| **Deprecated, use &#x60;order_by&#x60; instead.**  A list of field names, each possibly prefixed with a minus (-).  Sorts results according to the specified fields&#39; values. By default, the sort is ascending (from the smallest value to the biggest value). A minus sign (‘-‘) may be used to perform a descending sort. Sorting is only available on numeric fields (int, double, date and datetime) and on text fields which have the sortable annotation.  | [optional] 
 **orderBy** | [**[String]**](String.md)| A comma-separated list of field names or aggregations to sort on, followed by an order (&#x60;asc&#x60; or &#x60;desc&#x60;).  Sorts results according to the specified fields&#39; values in ascending order by default. To sort results in descending order, use the &#x60;desc&#x60; keyword.  Example: &#x60;sum(age) desc, name asc&#x60;  | [optional] 
 **limit** | **Number**| Number of items to return in export.  Use -1 (default) to retrieve all records  | [optional] [default to -1]
 **offset** | **Number**| Index of the first item to return (starting at 0).  To use in conjonction with limit to implement pagination.  | [optional] [default to 0]
 **facet** | [**[String]**](String.md)| A facet is a field used for simple filtering (through the parameters refine and exclude) or exploration (with the endpoint &#x60;/facets&#x60;).  Facets can be configured in the back-office or with this parameter.  Read [the facets documentation](https://help.opendatasoft.com/apis/ods-search-v2/#facets) for more details.  | [optional] 
 **refine** | [**[String]**](String.md)| An array of facet filters. For example **city:Paris** or **modified:2019/12**. The request will only include the selected facet value.  Read [filtering with facets value](https://help.opendatasoft.com/apis/ods-search-v2/#filtering-with-facets-values) for more details.  *Not to be confused with a where filter. Refining with a facet is equivalent to selecting an entry in the left navigation panel.*  *refine is not available for monitoring sources*  | [optional] 
 **exclude** | [**[String]**](String.md)| An array of facet filters. For example **city:Paris** or **modified:2019/12**. The request will exclude the defined facet value.  Read [filtering with facets value](https://help.opendatasoft.com/apis/ods-search-v2/#filtering-with-facets-values) for more details.  *Not to be confused with a where filter. Excluding a facet value is equivalent to removing an entry in the left navigation panel.*  *exclude is not available for monitoring sources*  | [optional] 
 **timezone** | **String**| Set timezone for datetime fields | [optional] [default to &#39;UTC&#39;]
 **delimiter** | **String**| Provide a different delimiter (default &#39;,&#39;). | [optional] [default to &#39;;&#39;]

### Return type

**File**

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/csv


## exportRecordsGEOJSON_0

> File exportRecordsGEOJSON_0(source, datasetId, opts)



Export dataset in GEOJSON format 

### Example

```javascript
import Opendatasoft from 'opendatasoft';
let defaultClient = Opendatasoft.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure HTTP basic authorization: basic
let basic = defaultClient.authentications['basic'];
basic.username = 'YOUR USERNAME';
basic.password = 'YOUR PASSWORD';

let apiInstance = new Opendatasoft.OdsApi();
let source = "'catalog'"; // String | Each source represents a different catalog of datasets you'll be able to query.  There are 2 sources available:  * catalog: the catalog of datasets on your portal * opendatasoft: Opendatasoft's repository of public datasets, also available at   [data.opendatasoft.com](https://data.opendatasoft.com/page/home/) 
let datasetId = "datasetId_example"; // String | Dataset identifier.  Can be found in the \"information\" tab of the dataset page. 
let opts = {
  'select': "select_example", // String | A select expression can be used to add, remove or change fields to return. An expression can be:   - a wildcard ('*'): return all fields   - a field name: return only this field   - an include/exclude function. Include (resp exclude) all field matching include/exclude expression. This expression can contain wildcard. For example: include(spa*) will return all fields begining with 'spa'   - a complex expression: return the result of this expression. A label can be set for this expression, in that case, field will be named with this label. For instance: 'size * 2 as bigger_size' will return a new field named bigger_size and containing the double of size field value. 
  'where': ["null"], // [String] | An array of filters.  A filter is a text expression performing a simple full-text search that can also include logical operations (NOT, AND, OR...) as well as lots of other functions, thus performing more complex and more precise searches.  Read [the query language reference](https://docs.opendatasoft.com/api/explore/v2.html#where-clause) for more details. 
  'sort': ["null"], // [String] | **Deprecated, use `order_by` instead.**  A list of field names, each possibly prefixed with a minus (-).  Sorts results according to the specified fields' values. By default, the sort is ascending (from the smallest value to the biggest value). A minus sign (‘-‘) may be used to perform a descending sort. Sorting is only available on numeric fields (int, double, date and datetime) and on text fields which have the sortable annotation. 
  'orderBy': ["null"], // [String] | A comma-separated list of field names or aggregations to sort on, followed by an order (`asc` or `desc`).  Sorts results according to the specified fields' values in ascending order by default. To sort results in descending order, use the `desc` keyword.  Example: `sum(age) desc, name asc` 
  'limit': -1, // Number | Number of items to return in export.  Use -1 (default) to retrieve all records 
  'offset': 0, // Number | Index of the first item to return (starting at 0).  To use in conjonction with limit to implement pagination. 
  'search': ["null"], // [String] | An array of full text search.  A full text search performs a prefixed text search for each provided terms in all visible fields of a catalog/dataset. 
  'facet': ["null"], // [String] | A facet is a field used for simple filtering (through the parameters refine and exclude) or exploration (with the endpoint `/facets`).  Facets can be configured in the back-office or with this parameter.  Read [the facets documentation](https://help.opendatasoft.com/apis/ods-search-v2/#facets) for more details. 
  'refine': ["null"], // [String] | An array of facet filters. For example **city:Paris** or **modified:2019/12**. The request will only include the selected facet value.  Read [filtering with facets value](https://help.opendatasoft.com/apis/ods-search-v2/#filtering-with-facets-values) for more details.  *Not to be confused with a where filter. Refining with a facet is equivalent to selecting an entry in the left navigation panel.*  *refine is not available for monitoring sources* 
  'exclude': ["null"], // [String] | An array of facet filters. For example **city:Paris** or **modified:2019/12**. The request will exclude the defined facet value.  Read [filtering with facets value](https://help.opendatasoft.com/apis/ods-search-v2/#filtering-with-facets-values) for more details.  *Not to be confused with a where filter. Excluding a facet value is equivalent to removing an entry in the left navigation panel.*  *exclude is not available for monitoring sources* 
  'timezone': "'UTC'", // String | Set timezone for datetime fields
  'pretty': false // Boolean | Activate pretty print
};
apiInstance.exportRecordsGEOJSON_0(source, datasetId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source** | **String**| Each source represents a different catalog of datasets you&#39;ll be able to query.  There are 2 sources available:  * catalog: the catalog of datasets on your portal * opendatasoft: Opendatasoft&#39;s repository of public datasets, also available at   [data.opendatasoft.com](https://data.opendatasoft.com/page/home/)  | [default to &#39;catalog&#39;]
 **datasetId** | **String**| Dataset identifier.  Can be found in the \&quot;information\&quot; tab of the dataset page.  | 
 **select** | **String**| A select expression can be used to add, remove or change fields to return. An expression can be:   - a wildcard (&#39;*&#39;): return all fields   - a field name: return only this field   - an include/exclude function. Include (resp exclude) all field matching include/exclude expression. This expression can contain wildcard. For example: include(spa*) will return all fields begining with &#39;spa&#39;   - a complex expression: return the result of this expression. A label can be set for this expression, in that case, field will be named with this label. For instance: &#39;size * 2 as bigger_size&#39; will return a new field named bigger_size and containing the double of size field value.  | [optional] 
 **where** | [**[String]**](String.md)| An array of filters.  A filter is a text expression performing a simple full-text search that can also include logical operations (NOT, AND, OR...) as well as lots of other functions, thus performing more complex and more precise searches.  Read [the query language reference](https://docs.opendatasoft.com/api/explore/v2.html#where-clause) for more details.  | [optional] 
 **sort** | [**[String]**](String.md)| **Deprecated, use &#x60;order_by&#x60; instead.**  A list of field names, each possibly prefixed with a minus (-).  Sorts results according to the specified fields&#39; values. By default, the sort is ascending (from the smallest value to the biggest value). A minus sign (‘-‘) may be used to perform a descending sort. Sorting is only available on numeric fields (int, double, date and datetime) and on text fields which have the sortable annotation.  | [optional] 
 **orderBy** | [**[String]**](String.md)| A comma-separated list of field names or aggregations to sort on, followed by an order (&#x60;asc&#x60; or &#x60;desc&#x60;).  Sorts results according to the specified fields&#39; values in ascending order by default. To sort results in descending order, use the &#x60;desc&#x60; keyword.  Example: &#x60;sum(age) desc, name asc&#x60;  | [optional] 
 **limit** | **Number**| Number of items to return in export.  Use -1 (default) to retrieve all records  | [optional] [default to -1]
 **offset** | **Number**| Index of the first item to return (starting at 0).  To use in conjonction with limit to implement pagination.  | [optional] [default to 0]
 **search** | [**[String]**](String.md)| An array of full text search.  A full text search performs a prefixed text search for each provided terms in all visible fields of a catalog/dataset.  | [optional] 
 **facet** | [**[String]**](String.md)| A facet is a field used for simple filtering (through the parameters refine and exclude) or exploration (with the endpoint &#x60;/facets&#x60;).  Facets can be configured in the back-office or with this parameter.  Read [the facets documentation](https://help.opendatasoft.com/apis/ods-search-v2/#facets) for more details.  | [optional] 
 **refine** | [**[String]**](String.md)| An array of facet filters. For example **city:Paris** or **modified:2019/12**. The request will only include the selected facet value.  Read [filtering with facets value](https://help.opendatasoft.com/apis/ods-search-v2/#filtering-with-facets-values) for more details.  *Not to be confused with a where filter. Refining with a facet is equivalent to selecting an entry in the left navigation panel.*  *refine is not available for monitoring sources*  | [optional] 
 **exclude** | [**[String]**](String.md)| An array of facet filters. For example **city:Paris** or **modified:2019/12**. The request will exclude the defined facet value.  Read [filtering with facets value](https://help.opendatasoft.com/apis/ods-search-v2/#filtering-with-facets-values) for more details.  *Not to be confused with a where filter. Excluding a facet value is equivalent to removing an entry in the left navigation panel.*  *exclude is not available for monitoring sources*  | [optional] 
 **timezone** | **String**| Set timezone for datetime fields | [optional] [default to &#39;UTC&#39;]
 **pretty** | **Boolean**| Activate pretty print | [optional] [default to false]

### Return type

**File**

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## exportRecordsICAL_0

> File exportRecordsICAL_0(source, datasetId, opts)



Export dataset in ICAL format 

### Example

```javascript
import Opendatasoft from 'opendatasoft';
let defaultClient = Opendatasoft.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure HTTP basic authorization: basic
let basic = defaultClient.authentications['basic'];
basic.username = 'YOUR USERNAME';
basic.password = 'YOUR PASSWORD';

let apiInstance = new Opendatasoft.OdsApi();
let source = "'catalog'"; // String | Each source represents a different catalog of datasets you'll be able to query.  There are 2 sources available:  * catalog: the catalog of datasets on your portal * opendatasoft: Opendatasoft's repository of public datasets, also available at   [data.opendatasoft.com](https://data.opendatasoft.com/page/home/) 
let datasetId = "datasetId_example"; // String | Dataset identifier.  Can be found in the \"information\" tab of the dataset page. 
let opts = {
  'select': "select_example", // String | A select expression can be used to add, remove or change fields to return. An expression can be:   - a wildcard ('*'): return all fields   - a field name: return only this field   - an include/exclude function. Include (resp exclude) all field matching include/exclude expression. This expression can contain wildcard. For example: include(spa*) will return all fields begining with 'spa'   - a complex expression: return the result of this expression. A label can be set for this expression, in that case, field will be named with this label. For instance: 'size * 2 as bigger_size' will return a new field named bigger_size and containing the double of size field value. 
  'where': ["null"], // [String] | An array of filters.  A filter is a text expression performing a simple full-text search that can also include logical operations (NOT, AND, OR...) as well as lots of other functions, thus performing more complex and more precise searches.  Read [the query language reference](https://docs.opendatasoft.com/api/explore/v2.html#where-clause) for more details. 
  'sort': ["null"], // [String] | **Deprecated, use `order_by` instead.**  A list of field names, each possibly prefixed with a minus (-).  Sorts results according to the specified fields' values. By default, the sort is ascending (from the smallest value to the biggest value). A minus sign (‘-‘) may be used to perform a descending sort. Sorting is only available on numeric fields (int, double, date and datetime) and on text fields which have the sortable annotation. 
  'orderBy': ["null"], // [String] | A comma-separated list of field names or aggregations to sort on, followed by an order (`asc` or `desc`).  Sorts results according to the specified fields' values in ascending order by default. To sort results in descending order, use the `desc` keyword.  Example: `sum(age) desc, name asc` 
  'limit': -1, // Number | Number of items to return in export.  Use -1 (default) to retrieve all records 
  'offset': 0, // Number | Index of the first item to return (starting at 0).  To use in conjonction with limit to implement pagination. 
  'search': ["null"], // [String] | An array of full text search.  A full text search performs a prefixed text search for each provided terms in all visible fields of a catalog/dataset. 
  'facet': ["null"], // [String] | A facet is a field used for simple filtering (through the parameters refine and exclude) or exploration (with the endpoint `/facets`).  Facets can be configured in the back-office or with this parameter.  Read [the facets documentation](https://help.opendatasoft.com/apis/ods-search-v2/#facets) for more details. 
  'refine': ["null"], // [String] | An array of facet filters. For example **city:Paris** or **modified:2019/12**. The request will only include the selected facet value.  Read [filtering with facets value](https://help.opendatasoft.com/apis/ods-search-v2/#filtering-with-facets-values) for more details.  *Not to be confused with a where filter. Refining with a facet is equivalent to selecting an entry in the left navigation panel.*  *refine is not available for monitoring sources* 
  'exclude': ["null"], // [String] | An array of facet filters. For example **city:Paris** or **modified:2019/12**. The request will exclude the defined facet value.  Read [filtering with facets value](https://help.opendatasoft.com/apis/ods-search-v2/#filtering-with-facets-values) for more details.  *Not to be confused with a where filter. Excluding a facet value is equivalent to removing an entry in the left navigation panel.*  *exclude is not available for monitoring sources* 
  'timezone': "'UTC'" // String | Set timezone for datetime fields
};
apiInstance.exportRecordsICAL_0(source, datasetId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source** | **String**| Each source represents a different catalog of datasets you&#39;ll be able to query.  There are 2 sources available:  * catalog: the catalog of datasets on your portal * opendatasoft: Opendatasoft&#39;s repository of public datasets, also available at   [data.opendatasoft.com](https://data.opendatasoft.com/page/home/)  | [default to &#39;catalog&#39;]
 **datasetId** | **String**| Dataset identifier.  Can be found in the \&quot;information\&quot; tab of the dataset page.  | 
 **select** | **String**| A select expression can be used to add, remove or change fields to return. An expression can be:   - a wildcard (&#39;*&#39;): return all fields   - a field name: return only this field   - an include/exclude function. Include (resp exclude) all field matching include/exclude expression. This expression can contain wildcard. For example: include(spa*) will return all fields begining with &#39;spa&#39;   - a complex expression: return the result of this expression. A label can be set for this expression, in that case, field will be named with this label. For instance: &#39;size * 2 as bigger_size&#39; will return a new field named bigger_size and containing the double of size field value.  | [optional] 
 **where** | [**[String]**](String.md)| An array of filters.  A filter is a text expression performing a simple full-text search that can also include logical operations (NOT, AND, OR...) as well as lots of other functions, thus performing more complex and more precise searches.  Read [the query language reference](https://docs.opendatasoft.com/api/explore/v2.html#where-clause) for more details.  | [optional] 
 **sort** | [**[String]**](String.md)| **Deprecated, use &#x60;order_by&#x60; instead.**  A list of field names, each possibly prefixed with a minus (-).  Sorts results according to the specified fields&#39; values. By default, the sort is ascending (from the smallest value to the biggest value). A minus sign (‘-‘) may be used to perform a descending sort. Sorting is only available on numeric fields (int, double, date and datetime) and on text fields which have the sortable annotation.  | [optional] 
 **orderBy** | [**[String]**](String.md)| A comma-separated list of field names or aggregations to sort on, followed by an order (&#x60;asc&#x60; or &#x60;desc&#x60;).  Sorts results according to the specified fields&#39; values in ascending order by default. To sort results in descending order, use the &#x60;desc&#x60; keyword.  Example: &#x60;sum(age) desc, name asc&#x60;  | [optional] 
 **limit** | **Number**| Number of items to return in export.  Use -1 (default) to retrieve all records  | [optional] [default to -1]
 **offset** | **Number**| Index of the first item to return (starting at 0).  To use in conjonction with limit to implement pagination.  | [optional] [default to 0]
 **search** | [**[String]**](String.md)| An array of full text search.  A full text search performs a prefixed text search for each provided terms in all visible fields of a catalog/dataset.  | [optional] 
 **facet** | [**[String]**](String.md)| A facet is a field used for simple filtering (through the parameters refine and exclude) or exploration (with the endpoint &#x60;/facets&#x60;).  Facets can be configured in the back-office or with this parameter.  Read [the facets documentation](https://help.opendatasoft.com/apis/ods-search-v2/#facets) for more details.  | [optional] 
 **refine** | [**[String]**](String.md)| An array of facet filters. For example **city:Paris** or **modified:2019/12**. The request will only include the selected facet value.  Read [filtering with facets value](https://help.opendatasoft.com/apis/ods-search-v2/#filtering-with-facets-values) for more details.  *Not to be confused with a where filter. Refining with a facet is equivalent to selecting an entry in the left navigation panel.*  *refine is not available for monitoring sources*  | [optional] 
 **exclude** | [**[String]**](String.md)| An array of facet filters. For example **city:Paris** or **modified:2019/12**. The request will exclude the defined facet value.  Read [filtering with facets value](https://help.opendatasoft.com/apis/ods-search-v2/#filtering-with-facets-values) for more details.  *Not to be confused with a where filter. Excluding a facet value is equivalent to removing an entry in the left navigation panel.*  *exclude is not available for monitoring sources*  | [optional] 
 **timezone** | **String**| Set timezone for datetime fields | [optional] [default to &#39;UTC&#39;]

### Return type

**File**

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## exportRecordsJSON_0

> File exportRecordsJSON_0(source, datasetId, opts)



Export dataset in JSON format 

### Example

```javascript
import Opendatasoft from 'opendatasoft';
let defaultClient = Opendatasoft.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure HTTP basic authorization: basic
let basic = defaultClient.authentications['basic'];
basic.username = 'YOUR USERNAME';
basic.password = 'YOUR PASSWORD';

let apiInstance = new Opendatasoft.OdsApi();
let source = "'catalog'"; // String | Each source represents a different catalog of datasets you'll be able to query.  There are 2 sources available:  * catalog: the catalog of datasets on your portal * opendatasoft: Opendatasoft's repository of public datasets, also available at   [data.opendatasoft.com](https://data.opendatasoft.com/page/home/) 
let datasetId = "datasetId_example"; // String | Dataset identifier.  Can be found in the \"information\" tab of the dataset page. 
let opts = {
  'select': "select_example", // String | A select expression can be used to add, remove or change fields to return. An expression can be:   - a wildcard ('*'): return all fields   - a field name: return only this field   - an include/exclude function. Include (resp exclude) all field matching include/exclude expression. This expression can contain wildcard. For example: include(spa*) will return all fields begining with 'spa'   - a complex expression: return the result of this expression. A label can be set for this expression, in that case, field will be named with this label. For instance: 'size * 2 as bigger_size' will return a new field named bigger_size and containing the double of size field value. 
  'where': ["null"], // [String] | An array of filters.  A filter is a text expression performing a simple full-text search that can also include logical operations (NOT, AND, OR...) as well as lots of other functions, thus performing more complex and more precise searches.  Read [the query language reference](https://docs.opendatasoft.com/api/explore/v2.html#where-clause) for more details. 
  'sort': ["null"], // [String] | **Deprecated, use `order_by` instead.**  A list of field names, each possibly prefixed with a minus (-).  Sorts results according to the specified fields' values. By default, the sort is ascending (from the smallest value to the biggest value). A minus sign (‘-‘) may be used to perform a descending sort. Sorting is only available on numeric fields (int, double, date and datetime) and on text fields which have the sortable annotation. 
  'orderBy': ["null"], // [String] | A comma-separated list of field names or aggregations to sort on, followed by an order (`asc` or `desc`).  Sorts results according to the specified fields' values in ascending order by default. To sort results in descending order, use the `desc` keyword.  Example: `sum(age) desc, name asc` 
  'limit': -1, // Number | Number of items to return in export.  Use -1 (default) to retrieve all records 
  'offset': 0, // Number | Index of the first item to return (starting at 0).  To use in conjonction with limit to implement pagination. 
  'search': ["null"], // [String] | An array of full text search.  A full text search performs a prefixed text search for each provided terms in all visible fields of a catalog/dataset. 
  'facet': ["null"], // [String] | A facet is a field used for simple filtering (through the parameters refine and exclude) or exploration (with the endpoint `/facets`).  Facets can be configured in the back-office or with this parameter.  Read [the facets documentation](https://help.opendatasoft.com/apis/ods-search-v2/#facets) for more details. 
  'refine': ["null"], // [String] | An array of facet filters. For example **city:Paris** or **modified:2019/12**. The request will only include the selected facet value.  Read [filtering with facets value](https://help.opendatasoft.com/apis/ods-search-v2/#filtering-with-facets-values) for more details.  *Not to be confused with a where filter. Refining with a facet is equivalent to selecting an entry in the left navigation panel.*  *refine is not available for monitoring sources* 
  'exclude': ["null"], // [String] | An array of facet filters. For example **city:Paris** or **modified:2019/12**. The request will exclude the defined facet value.  Read [filtering with facets value](https://help.opendatasoft.com/apis/ods-search-v2/#filtering-with-facets-values) for more details.  *Not to be confused with a where filter. Excluding a facet value is equivalent to removing an entry in the left navigation panel.*  *exclude is not available for monitoring sources* 
  'pretty': false, // Boolean | Activate pretty print
  'timezone': "'UTC'" // String | Set timezone for datetime fields
};
apiInstance.exportRecordsJSON_0(source, datasetId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source** | **String**| Each source represents a different catalog of datasets you&#39;ll be able to query.  There are 2 sources available:  * catalog: the catalog of datasets on your portal * opendatasoft: Opendatasoft&#39;s repository of public datasets, also available at   [data.opendatasoft.com](https://data.opendatasoft.com/page/home/)  | [default to &#39;catalog&#39;]
 **datasetId** | **String**| Dataset identifier.  Can be found in the \&quot;information\&quot; tab of the dataset page.  | 
 **select** | **String**| A select expression can be used to add, remove or change fields to return. An expression can be:   - a wildcard (&#39;*&#39;): return all fields   - a field name: return only this field   - an include/exclude function. Include (resp exclude) all field matching include/exclude expression. This expression can contain wildcard. For example: include(spa*) will return all fields begining with &#39;spa&#39;   - a complex expression: return the result of this expression. A label can be set for this expression, in that case, field will be named with this label. For instance: &#39;size * 2 as bigger_size&#39; will return a new field named bigger_size and containing the double of size field value.  | [optional] 
 **where** | [**[String]**](String.md)| An array of filters.  A filter is a text expression performing a simple full-text search that can also include logical operations (NOT, AND, OR...) as well as lots of other functions, thus performing more complex and more precise searches.  Read [the query language reference](https://docs.opendatasoft.com/api/explore/v2.html#where-clause) for more details.  | [optional] 
 **sort** | [**[String]**](String.md)| **Deprecated, use &#x60;order_by&#x60; instead.**  A list of field names, each possibly prefixed with a minus (-).  Sorts results according to the specified fields&#39; values. By default, the sort is ascending (from the smallest value to the biggest value). A minus sign (‘-‘) may be used to perform a descending sort. Sorting is only available on numeric fields (int, double, date and datetime) and on text fields which have the sortable annotation.  | [optional] 
 **orderBy** | [**[String]**](String.md)| A comma-separated list of field names or aggregations to sort on, followed by an order (&#x60;asc&#x60; or &#x60;desc&#x60;).  Sorts results according to the specified fields&#39; values in ascending order by default. To sort results in descending order, use the &#x60;desc&#x60; keyword.  Example: &#x60;sum(age) desc, name asc&#x60;  | [optional] 
 **limit** | **Number**| Number of items to return in export.  Use -1 (default) to retrieve all records  | [optional] [default to -1]
 **offset** | **Number**| Index of the first item to return (starting at 0).  To use in conjonction with limit to implement pagination.  | [optional] [default to 0]
 **search** | [**[String]**](String.md)| An array of full text search.  A full text search performs a prefixed text search for each provided terms in all visible fields of a catalog/dataset.  | [optional] 
 **facet** | [**[String]**](String.md)| A facet is a field used for simple filtering (through the parameters refine and exclude) or exploration (with the endpoint &#x60;/facets&#x60;).  Facets can be configured in the back-office or with this parameter.  Read [the facets documentation](https://help.opendatasoft.com/apis/ods-search-v2/#facets) for more details.  | [optional] 
 **refine** | [**[String]**](String.md)| An array of facet filters. For example **city:Paris** or **modified:2019/12**. The request will only include the selected facet value.  Read [filtering with facets value](https://help.opendatasoft.com/apis/ods-search-v2/#filtering-with-facets-values) for more details.  *Not to be confused with a where filter. Refining with a facet is equivalent to selecting an entry in the left navigation panel.*  *refine is not available for monitoring sources*  | [optional] 
 **exclude** | [**[String]**](String.md)| An array of facet filters. For example **city:Paris** or **modified:2019/12**. The request will exclude the defined facet value.  Read [filtering with facets value](https://help.opendatasoft.com/apis/ods-search-v2/#filtering-with-facets-values) for more details.  *Not to be confused with a where filter. Excluding a facet value is equivalent to removing an entry in the left navigation panel.*  *exclude is not available for monitoring sources*  | [optional] 
 **pretty** | **Boolean**| Activate pretty print | [optional] [default to false]
 **timezone** | **String**| Set timezone for datetime fields | [optional] [default to &#39;UTC&#39;]

### Return type

**File**

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## exportRecordsOV2_0

> File exportRecordsOV2_0(source, datasetId, opts)



Export dataset in OV2 format 

### Example

```javascript
import Opendatasoft from 'opendatasoft';
let defaultClient = Opendatasoft.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure HTTP basic authorization: basic
let basic = defaultClient.authentications['basic'];
basic.username = 'YOUR USERNAME';
basic.password = 'YOUR PASSWORD';

let apiInstance = new Opendatasoft.OdsApi();
let source = "'catalog'"; // String | Each source represents a different catalog of datasets you'll be able to query.  There are 2 sources available:  * catalog: the catalog of datasets on your portal * opendatasoft: Opendatasoft's repository of public datasets, also available at   [data.opendatasoft.com](https://data.opendatasoft.com/page/home/) 
let datasetId = "datasetId_example"; // String | Dataset identifier.  Can be found in the \"information\" tab of the dataset page. 
let opts = {
  'select': "select_example", // String | A select expression can be used to add, remove or change fields to return. An expression can be:   - a wildcard ('*'): return all fields   - a field name: return only this field   - an include/exclude function. Include (resp exclude) all field matching include/exclude expression. This expression can contain wildcard. For example: include(spa*) will return all fields begining with 'spa'   - a complex expression: return the result of this expression. A label can be set for this expression, in that case, field will be named with this label. For instance: 'size * 2 as bigger_size' will return a new field named bigger_size and containing the double of size field value. 
  'where': ["null"], // [String] | An array of filters.  A filter is a text expression performing a simple full-text search that can also include logical operations (NOT, AND, OR...) as well as lots of other functions, thus performing more complex and more precise searches.  Read [the query language reference](https://docs.opendatasoft.com/api/explore/v2.html#where-clause) for more details. 
  'sort': ["null"], // [String] | **Deprecated, use `order_by` instead.**  A list of field names, each possibly prefixed with a minus (-).  Sorts results according to the specified fields' values. By default, the sort is ascending (from the smallest value to the biggest value). A minus sign (‘-‘) may be used to perform a descending sort. Sorting is only available on numeric fields (int, double, date and datetime) and on text fields which have the sortable annotation. 
  'orderBy': ["null"], // [String] | A comma-separated list of field names or aggregations to sort on, followed by an order (`asc` or `desc`).  Sorts results according to the specified fields' values in ascending order by default. To sort results in descending order, use the `desc` keyword.  Example: `sum(age) desc, name asc` 
  'limit': -1, // Number | Number of items to return in export.  Use -1 (default) to retrieve all records 
  'offset': 0, // Number | Index of the first item to return (starting at 0).  To use in conjonction with limit to implement pagination. 
  'search': ["null"], // [String] | An array of full text search.  A full text search performs a prefixed text search for each provided terms in all visible fields of a catalog/dataset. 
  'facet': ["null"], // [String] | A facet is a field used for simple filtering (through the parameters refine and exclude) or exploration (with the endpoint `/facets`).  Facets can be configured in the back-office or with this parameter.  Read [the facets documentation](https://help.opendatasoft.com/apis/ods-search-v2/#facets) for more details. 
  'refine': ["null"], // [String] | An array of facet filters. For example **city:Paris** or **modified:2019/12**. The request will only include the selected facet value.  Read [filtering with facets value](https://help.opendatasoft.com/apis/ods-search-v2/#filtering-with-facets-values) for more details.  *Not to be confused with a where filter. Refining with a facet is equivalent to selecting an entry in the left navigation panel.*  *refine is not available for monitoring sources* 
  'exclude': ["null"], // [String] | An array of facet filters. For example **city:Paris** or **modified:2019/12**. The request will exclude the defined facet value.  Read [filtering with facets value](https://help.opendatasoft.com/apis/ods-search-v2/#filtering-with-facets-values) for more details.  *Not to be confused with a where filter. Excluding a facet value is equivalent to removing an entry in the left navigation panel.*  *exclude is not available for monitoring sources* 
  'timezone': "'UTC'" // String | Set timezone for datetime fields
};
apiInstance.exportRecordsOV2_0(source, datasetId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source** | **String**| Each source represents a different catalog of datasets you&#39;ll be able to query.  There are 2 sources available:  * catalog: the catalog of datasets on your portal * opendatasoft: Opendatasoft&#39;s repository of public datasets, also available at   [data.opendatasoft.com](https://data.opendatasoft.com/page/home/)  | [default to &#39;catalog&#39;]
 **datasetId** | **String**| Dataset identifier.  Can be found in the \&quot;information\&quot; tab of the dataset page.  | 
 **select** | **String**| A select expression can be used to add, remove or change fields to return. An expression can be:   - a wildcard (&#39;*&#39;): return all fields   - a field name: return only this field   - an include/exclude function. Include (resp exclude) all field matching include/exclude expression. This expression can contain wildcard. For example: include(spa*) will return all fields begining with &#39;spa&#39;   - a complex expression: return the result of this expression. A label can be set for this expression, in that case, field will be named with this label. For instance: &#39;size * 2 as bigger_size&#39; will return a new field named bigger_size and containing the double of size field value.  | [optional] 
 **where** | [**[String]**](String.md)| An array of filters.  A filter is a text expression performing a simple full-text search that can also include logical operations (NOT, AND, OR...) as well as lots of other functions, thus performing more complex and more precise searches.  Read [the query language reference](https://docs.opendatasoft.com/api/explore/v2.html#where-clause) for more details.  | [optional] 
 **sort** | [**[String]**](String.md)| **Deprecated, use &#x60;order_by&#x60; instead.**  A list of field names, each possibly prefixed with a minus (-).  Sorts results according to the specified fields&#39; values. By default, the sort is ascending (from the smallest value to the biggest value). A minus sign (‘-‘) may be used to perform a descending sort. Sorting is only available on numeric fields (int, double, date and datetime) and on text fields which have the sortable annotation.  | [optional] 
 **orderBy** | [**[String]**](String.md)| A comma-separated list of field names or aggregations to sort on, followed by an order (&#x60;asc&#x60; or &#x60;desc&#x60;).  Sorts results according to the specified fields&#39; values in ascending order by default. To sort results in descending order, use the &#x60;desc&#x60; keyword.  Example: &#x60;sum(age) desc, name asc&#x60;  | [optional] 
 **limit** | **Number**| Number of items to return in export.  Use -1 (default) to retrieve all records  | [optional] [default to -1]
 **offset** | **Number**| Index of the first item to return (starting at 0).  To use in conjonction with limit to implement pagination.  | [optional] [default to 0]
 **search** | [**[String]**](String.md)| An array of full text search.  A full text search performs a prefixed text search for each provided terms in all visible fields of a catalog/dataset.  | [optional] 
 **facet** | [**[String]**](String.md)| A facet is a field used for simple filtering (through the parameters refine and exclude) or exploration (with the endpoint &#x60;/facets&#x60;).  Facets can be configured in the back-office or with this parameter.  Read [the facets documentation](https://help.opendatasoft.com/apis/ods-search-v2/#facets) for more details.  | [optional] 
 **refine** | [**[String]**](String.md)| An array of facet filters. For example **city:Paris** or **modified:2019/12**. The request will only include the selected facet value.  Read [filtering with facets value](https://help.opendatasoft.com/apis/ods-search-v2/#filtering-with-facets-values) for more details.  *Not to be confused with a where filter. Refining with a facet is equivalent to selecting an entry in the left navigation panel.*  *refine is not available for monitoring sources*  | [optional] 
 **exclude** | [**[String]**](String.md)| An array of facet filters. For example **city:Paris** or **modified:2019/12**. The request will exclude the defined facet value.  Read [filtering with facets value](https://help.opendatasoft.com/apis/ods-search-v2/#filtering-with-facets-values) for more details.  *Not to be confused with a where filter. Excluding a facet value is equivalent to removing an entry in the left navigation panel.*  *exclude is not available for monitoring sources*  | [optional] 
 **timezone** | **String**| Set timezone for datetime fields | [optional] [default to &#39;UTC&#39;]

### Return type

**File**

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/plain


## exportRecordsSHP_0

> File exportRecordsSHP_0(source, datasetId, opts)



Export dataset in Esri shapefile (shp) format 

### Example

```javascript
import Opendatasoft from 'opendatasoft';
let defaultClient = Opendatasoft.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure HTTP basic authorization: basic
let basic = defaultClient.authentications['basic'];
basic.username = 'YOUR USERNAME';
basic.password = 'YOUR PASSWORD';

let apiInstance = new Opendatasoft.OdsApi();
let source = "'catalog'"; // String | Each source represents a different catalog of datasets you'll be able to query.  There are 2 sources available:  * catalog: the catalog of datasets on your portal * opendatasoft: Opendatasoft's repository of public datasets, also available at   [data.opendatasoft.com](https://data.opendatasoft.com/page/home/) 
let datasetId = "datasetId_example"; // String | Dataset identifier.  Can be found in the \"information\" tab of the dataset page. 
let opts = {
  'select': "select_example", // String | A select expression can be used to add, remove or change fields to return. An expression can be:   - a wildcard ('*'): return all fields   - a field name: return only this field   - an include/exclude function. Include (resp exclude) all field matching include/exclude expression. This expression can contain wildcard. For example: include(spa*) will return all fields begining with 'spa'   - a complex expression: return the result of this expression. A label can be set for this expression, in that case, field will be named with this label. For instance: 'size * 2 as bigger_size' will return a new field named bigger_size and containing the double of size field value. 
  'where': ["null"], // [String] | An array of filters.  A filter is a text expression performing a simple full-text search that can also include logical operations (NOT, AND, OR...) as well as lots of other functions, thus performing more complex and more precise searches.  Read [the query language reference](https://docs.opendatasoft.com/api/explore/v2.html#where-clause) for more details. 
  'sort': ["null"], // [String] | **Deprecated, use `order_by` instead.**  A list of field names, each possibly prefixed with a minus (-).  Sorts results according to the specified fields' values. By default, the sort is ascending (from the smallest value to the biggest value). A minus sign (‘-‘) may be used to perform a descending sort. Sorting is only available on numeric fields (int, double, date and datetime) and on text fields which have the sortable annotation. 
  'orderBy': ["null"], // [String] | A comma-separated list of field names or aggregations to sort on, followed by an order (`asc` or `desc`).  Sorts results according to the specified fields' values in ascending order by default. To sort results in descending order, use the `desc` keyword.  Example: `sum(age) desc, name asc` 
  'limit': -1, // Number | Number of items to return in export.  Use -1 (default) to retrieve all records 
  'offset': 0, // Number | Index of the first item to return (starting at 0).  To use in conjonction with limit to implement pagination. 
  'search': ["null"], // [String] | An array of full text search.  A full text search performs a prefixed text search for each provided terms in all visible fields of a catalog/dataset. 
  'facet': ["null"], // [String] | A facet is a field used for simple filtering (through the parameters refine and exclude) or exploration (with the endpoint `/facets`).  Facets can be configured in the back-office or with this parameter.  Read [the facets documentation](https://help.opendatasoft.com/apis/ods-search-v2/#facets) for more details. 
  'refine': ["null"], // [String] | An array of facet filters. For example **city:Paris** or **modified:2019/12**. The request will only include the selected facet value.  Read [filtering with facets value](https://help.opendatasoft.com/apis/ods-search-v2/#filtering-with-facets-values) for more details.  *Not to be confused with a where filter. Refining with a facet is equivalent to selecting an entry in the left navigation panel.*  *refine is not available for monitoring sources* 
  'exclude': ["null"], // [String] | An array of facet filters. For example **city:Paris** or **modified:2019/12**. The request will exclude the defined facet value.  Read [filtering with facets value](https://help.opendatasoft.com/apis/ods-search-v2/#filtering-with-facets-values) for more details.  *Not to be confused with a where filter. Excluding a facet value is equivalent to removing an entry in the left navigation panel.*  *exclude is not available for monitoring sources* 
  'timezone': "'UTC'" // String | Set timezone for datetime fields
};
apiInstance.exportRecordsSHP_0(source, datasetId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source** | **String**| Each source represents a different catalog of datasets you&#39;ll be able to query.  There are 2 sources available:  * catalog: the catalog of datasets on your portal * opendatasoft: Opendatasoft&#39;s repository of public datasets, also available at   [data.opendatasoft.com](https://data.opendatasoft.com/page/home/)  | [default to &#39;catalog&#39;]
 **datasetId** | **String**| Dataset identifier.  Can be found in the \&quot;information\&quot; tab of the dataset page.  | 
 **select** | **String**| A select expression can be used to add, remove or change fields to return. An expression can be:   - a wildcard (&#39;*&#39;): return all fields   - a field name: return only this field   - an include/exclude function. Include (resp exclude) all field matching include/exclude expression. This expression can contain wildcard. For example: include(spa*) will return all fields begining with &#39;spa&#39;   - a complex expression: return the result of this expression. A label can be set for this expression, in that case, field will be named with this label. For instance: &#39;size * 2 as bigger_size&#39; will return a new field named bigger_size and containing the double of size field value.  | [optional] 
 **where** | [**[String]**](String.md)| An array of filters.  A filter is a text expression performing a simple full-text search that can also include logical operations (NOT, AND, OR...) as well as lots of other functions, thus performing more complex and more precise searches.  Read [the query language reference](https://docs.opendatasoft.com/api/explore/v2.html#where-clause) for more details.  | [optional] 
 **sort** | [**[String]**](String.md)| **Deprecated, use &#x60;order_by&#x60; instead.**  A list of field names, each possibly prefixed with a minus (-).  Sorts results according to the specified fields&#39; values. By default, the sort is ascending (from the smallest value to the biggest value). A minus sign (‘-‘) may be used to perform a descending sort. Sorting is only available on numeric fields (int, double, date and datetime) and on text fields which have the sortable annotation.  | [optional] 
 **orderBy** | [**[String]**](String.md)| A comma-separated list of field names or aggregations to sort on, followed by an order (&#x60;asc&#x60; or &#x60;desc&#x60;).  Sorts results according to the specified fields&#39; values in ascending order by default. To sort results in descending order, use the &#x60;desc&#x60; keyword.  Example: &#x60;sum(age) desc, name asc&#x60;  | [optional] 
 **limit** | **Number**| Number of items to return in export.  Use -1 (default) to retrieve all records  | [optional] [default to -1]
 **offset** | **Number**| Index of the first item to return (starting at 0).  To use in conjonction with limit to implement pagination.  | [optional] [default to 0]
 **search** | [**[String]**](String.md)| An array of full text search.  A full text search performs a prefixed text search for each provided terms in all visible fields of a catalog/dataset.  | [optional] 
 **facet** | [**[String]**](String.md)| A facet is a field used for simple filtering (through the parameters refine and exclude) or exploration (with the endpoint &#x60;/facets&#x60;).  Facets can be configured in the back-office or with this parameter.  Read [the facets documentation](https://help.opendatasoft.com/apis/ods-search-v2/#facets) for more details.  | [optional] 
 **refine** | [**[String]**](String.md)| An array of facet filters. For example **city:Paris** or **modified:2019/12**. The request will only include the selected facet value.  Read [filtering with facets value](https://help.opendatasoft.com/apis/ods-search-v2/#filtering-with-facets-values) for more details.  *Not to be confused with a where filter. Refining with a facet is equivalent to selecting an entry in the left navigation panel.*  *refine is not available for monitoring sources*  | [optional] 
 **exclude** | [**[String]**](String.md)| An array of facet filters. For example **city:Paris** or **modified:2019/12**. The request will exclude the defined facet value.  Read [filtering with facets value](https://help.opendatasoft.com/apis/ods-search-v2/#filtering-with-facets-values) for more details.  *Not to be confused with a where filter. Excluding a facet value is equivalent to removing an entry in the left navigation panel.*  *exclude is not available for monitoring sources*  | [optional] 
 **timezone** | **String**| Set timezone for datetime fields | [optional] [default to &#39;UTC&#39;]

### Return type

**File**

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/zip


## exportRecordsXLS_0

> File exportRecordsXLS_0(source, datasetId, opts)



Export dataset in XLS (Excel) format 

### Example

```javascript
import Opendatasoft from 'opendatasoft';
let defaultClient = Opendatasoft.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure HTTP basic authorization: basic
let basic = defaultClient.authentications['basic'];
basic.username = 'YOUR USERNAME';
basic.password = 'YOUR PASSWORD';

let apiInstance = new Opendatasoft.OdsApi();
let source = "'catalog'"; // String | Each source represents a different catalog of datasets you'll be able to query.  There are 2 sources available:  * catalog: the catalog of datasets on your portal * opendatasoft: Opendatasoft's repository of public datasets, also available at   [data.opendatasoft.com](https://data.opendatasoft.com/page/home/) 
let datasetId = "datasetId_example"; // String | Dataset identifier.  Can be found in the \"information\" tab of the dataset page. 
let opts = {
  'select': "select_example", // String | A select expression can be used to add, remove or change fields to return. An expression can be:   - a wildcard ('*'): return all fields   - a field name: return only this field   - an include/exclude function. Include (resp exclude) all field matching include/exclude expression. This expression can contain wildcard. For example: include(spa*) will return all fields begining with 'spa'   - a complex expression: return the result of this expression. A label can be set for this expression, in that case, field will be named with this label. For instance: 'size * 2 as bigger_size' will return a new field named bigger_size and containing the double of size field value. 
  'where': ["null"], // [String] | An array of filters.  A filter is a text expression performing a simple full-text search that can also include logical operations (NOT, AND, OR...) as well as lots of other functions, thus performing more complex and more precise searches.  Read [the query language reference](https://docs.opendatasoft.com/api/explore/v2.html#where-clause) for more details. 
  'sort': ["null"], // [String] | **Deprecated, use `order_by` instead.**  A list of field names, each possibly prefixed with a minus (-).  Sorts results according to the specified fields' values. By default, the sort is ascending (from the smallest value to the biggest value). A minus sign (‘-‘) may be used to perform a descending sort. Sorting is only available on numeric fields (int, double, date and datetime) and on text fields which have the sortable annotation. 
  'orderBy': ["null"], // [String] | A comma-separated list of field names or aggregations to sort on, followed by an order (`asc` or `desc`).  Sorts results according to the specified fields' values in ascending order by default. To sort results in descending order, use the `desc` keyword.  Example: `sum(age) desc, name asc` 
  'limit': -1, // Number | Number of items to return in export.  Use -1 (default) to retrieve all records 
  'offset': 0, // Number | Index of the first item to return (starting at 0).  To use in conjonction with limit to implement pagination. 
  'search': ["null"], // [String] | An array of full text search.  A full text search performs a prefixed text search for each provided terms in all visible fields of a catalog/dataset. 
  'facet': ["null"], // [String] | A facet is a field used for simple filtering (through the parameters refine and exclude) or exploration (with the endpoint `/facets`).  Facets can be configured in the back-office or with this parameter.  Read [the facets documentation](https://help.opendatasoft.com/apis/ods-search-v2/#facets) for more details. 
  'refine': ["null"], // [String] | An array of facet filters. For example **city:Paris** or **modified:2019/12**. The request will only include the selected facet value.  Read [filtering with facets value](https://help.opendatasoft.com/apis/ods-search-v2/#filtering-with-facets-values) for more details.  *Not to be confused with a where filter. Refining with a facet is equivalent to selecting an entry in the left navigation panel.*  *refine is not available for monitoring sources* 
  'exclude': ["null"], // [String] | An array of facet filters. For example **city:Paris** or **modified:2019/12**. The request will exclude the defined facet value.  Read [filtering with facets value](https://help.opendatasoft.com/apis/ods-search-v2/#filtering-with-facets-values) for more details.  *Not to be confused with a where filter. Excluding a facet value is equivalent to removing an entry in the left navigation panel.*  *exclude is not available for monitoring sources* 
  'timezone': "'UTC'" // String | Set timezone for datetime fields
};
apiInstance.exportRecordsXLS_0(source, datasetId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source** | **String**| Each source represents a different catalog of datasets you&#39;ll be able to query.  There are 2 sources available:  * catalog: the catalog of datasets on your portal * opendatasoft: Opendatasoft&#39;s repository of public datasets, also available at   [data.opendatasoft.com](https://data.opendatasoft.com/page/home/)  | [default to &#39;catalog&#39;]
 **datasetId** | **String**| Dataset identifier.  Can be found in the \&quot;information\&quot; tab of the dataset page.  | 
 **select** | **String**| A select expression can be used to add, remove or change fields to return. An expression can be:   - a wildcard (&#39;*&#39;): return all fields   - a field name: return only this field   - an include/exclude function. Include (resp exclude) all field matching include/exclude expression. This expression can contain wildcard. For example: include(spa*) will return all fields begining with &#39;spa&#39;   - a complex expression: return the result of this expression. A label can be set for this expression, in that case, field will be named with this label. For instance: &#39;size * 2 as bigger_size&#39; will return a new field named bigger_size and containing the double of size field value.  | [optional] 
 **where** | [**[String]**](String.md)| An array of filters.  A filter is a text expression performing a simple full-text search that can also include logical operations (NOT, AND, OR...) as well as lots of other functions, thus performing more complex and more precise searches.  Read [the query language reference](https://docs.opendatasoft.com/api/explore/v2.html#where-clause) for more details.  | [optional] 
 **sort** | [**[String]**](String.md)| **Deprecated, use &#x60;order_by&#x60; instead.**  A list of field names, each possibly prefixed with a minus (-).  Sorts results according to the specified fields&#39; values. By default, the sort is ascending (from the smallest value to the biggest value). A minus sign (‘-‘) may be used to perform a descending sort. Sorting is only available on numeric fields (int, double, date and datetime) and on text fields which have the sortable annotation.  | [optional] 
 **orderBy** | [**[String]**](String.md)| A comma-separated list of field names or aggregations to sort on, followed by an order (&#x60;asc&#x60; or &#x60;desc&#x60;).  Sorts results according to the specified fields&#39; values in ascending order by default. To sort results in descending order, use the &#x60;desc&#x60; keyword.  Example: &#x60;sum(age) desc, name asc&#x60;  | [optional] 
 **limit** | **Number**| Number of items to return in export.  Use -1 (default) to retrieve all records  | [optional] [default to -1]
 **offset** | **Number**| Index of the first item to return (starting at 0).  To use in conjonction with limit to implement pagination.  | [optional] [default to 0]
 **search** | [**[String]**](String.md)| An array of full text search.  A full text search performs a prefixed text search for each provided terms in all visible fields of a catalog/dataset.  | [optional] 
 **facet** | [**[String]**](String.md)| A facet is a field used for simple filtering (through the parameters refine and exclude) or exploration (with the endpoint &#x60;/facets&#x60;).  Facets can be configured in the back-office or with this parameter.  Read [the facets documentation](https://help.opendatasoft.com/apis/ods-search-v2/#facets) for more details.  | [optional] 
 **refine** | [**[String]**](String.md)| An array of facet filters. For example **city:Paris** or **modified:2019/12**. The request will only include the selected facet value.  Read [filtering with facets value](https://help.opendatasoft.com/apis/ods-search-v2/#filtering-with-facets-values) for more details.  *Not to be confused with a where filter. Refining with a facet is equivalent to selecting an entry in the left navigation panel.*  *refine is not available for monitoring sources*  | [optional] 
 **exclude** | [**[String]**](String.md)| An array of facet filters. For example **city:Paris** or **modified:2019/12**. The request will exclude the defined facet value.  Read [filtering with facets value](https://help.opendatasoft.com/apis/ods-search-v2/#filtering-with-facets-values) for more details.  *Not to be confused with a where filter. Excluding a facet value is equivalent to removing an entry in the left navigation panel.*  *exclude is not available for monitoring sources*  | [optional] 
 **timezone** | **String**| Set timezone for datetime fields | [optional] [default to &#39;UTC&#39;]

### Return type

**File**

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: xls


## getDatasetAttachements_0

> GetDatasetAttachements200Response getDatasetAttachements_0(source, datasetId)



Get list of all available attachments 

### Example

```javascript
import Opendatasoft from 'opendatasoft';
let defaultClient = Opendatasoft.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure HTTP basic authorization: basic
let basic = defaultClient.authentications['basic'];
basic.username = 'YOUR USERNAME';
basic.password = 'YOUR PASSWORD';

let apiInstance = new Opendatasoft.OdsApi();
let source = "'catalog'"; // String | Each source represents a different catalog of datasets you'll be able to query.  There are 2 sources available:  * catalog: the catalog of datasets on your portal * opendatasoft: Opendatasoft's repository of public datasets, also available at   [data.opendatasoft.com](https://data.opendatasoft.com/page/home/) 
let datasetId = "datasetId_example"; // String | Dataset identifier.  Can be found in the \"information\" tab of the dataset page. 
apiInstance.getDatasetAttachements_0(source, datasetId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source** | **String**| Each source represents a different catalog of datasets you&#39;ll be able to query.  There are 2 sources available:  * catalog: the catalog of datasets on your portal * opendatasoft: Opendatasoft&#39;s repository of public datasets, also available at   [data.opendatasoft.com](https://data.opendatasoft.com/page/home/)  | [default to &#39;catalog&#39;]
 **datasetId** | **String**| Dataset identifier.  Can be found in the \&quot;information\&quot; tab of the dataset page.  | 

### Return type

[**GetDatasetAttachements200Response**](GetDatasetAttachements200Response.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDatasetFile_0

> getDatasetFile_0(source, datasetId, fileId, opts)



Download file 

### Example

```javascript
import Opendatasoft from 'opendatasoft';
let defaultClient = Opendatasoft.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure HTTP basic authorization: basic
let basic = defaultClient.authentications['basic'];
basic.username = 'YOUR USERNAME';
basic.password = 'YOUR PASSWORD';

let apiInstance = new Opendatasoft.OdsApi();
let source = "'catalog'"; // String | Each source represents a different catalog of datasets you'll be able to query.  There are 2 sources available:  * catalog: the catalog of datasets on your portal * opendatasoft: Opendatasoft's repository of public datasets, also available at   [data.opendatasoft.com](https://data.opendatasoft.com/page/home/) 
let datasetId = "datasetId_example"; // String | Dataset identifier.  Can be found in the \"information\" tab of the dataset page. 
let fileId = "fileId_example"; // String | 
let opts = {
  'thumbnailSize': "thumbnailSize_example" // String | Set the size of the thumbnail representing the resource (attachment, image or file)
};
apiInstance.getDatasetFile_0(source, datasetId, fileId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source** | **String**| Each source represents a different catalog of datasets you&#39;ll be able to query.  There are 2 sources available:  * catalog: the catalog of datasets on your portal * opendatasoft: Opendatasoft&#39;s repository of public datasets, also available at   [data.opendatasoft.com](https://data.opendatasoft.com/page/home/)  | [default to &#39;catalog&#39;]
 **datasetId** | **String**| Dataset identifier.  Can be found in the \&quot;information\&quot; tab of the dataset page.  | 
 **fileId** | **String**|  | 
 **thumbnailSize** | **String**| Set the size of the thumbnail representing the resource (attachment, image or file) | [optional] 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getDatasetReuse_0

> GetDatasetReuse200Response getDatasetReuse_0(source, datasetId, reuseId, opts)



Retrieve a single reuse based on its ID. 

### Example

```javascript
import Opendatasoft from 'opendatasoft';
let defaultClient = Opendatasoft.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure HTTP basic authorization: basic
let basic = defaultClient.authentications['basic'];
basic.username = 'YOUR USERNAME';
basic.password = 'YOUR PASSWORD';

let apiInstance = new Opendatasoft.OdsApi();
let source = "'catalog'"; // String | Each source represents a different catalog of datasets you'll be able to query.  There are 2 sources available:  * catalog: the catalog of datasets on your portal * opendatasoft: Opendatasoft's repository of public datasets, also available at   [data.opendatasoft.com](https://data.opendatasoft.com/page/home/) 
let datasetId = "datasetId_example"; // String | Dataset identifier.  Can be found in the \"information\" tab of the dataset page. 
let reuseId = "reuseId_example"; // String | 
let opts = {
  'timezone': "'UTC'" // String | Set timezone for datetime fields
};
apiInstance.getDatasetReuse_0(source, datasetId, reuseId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source** | **String**| Each source represents a different catalog of datasets you&#39;ll be able to query.  There are 2 sources available:  * catalog: the catalog of datasets on your portal * opendatasoft: Opendatasoft&#39;s repository of public datasets, also available at   [data.opendatasoft.com](https://data.opendatasoft.com/page/home/)  | [default to &#39;catalog&#39;]
 **datasetId** | **String**| Dataset identifier.  Can be found in the \&quot;information\&quot; tab of the dataset page.  | 
 **reuseId** | **String**|  | 
 **timezone** | **String**| Set timezone for datetime fields | [optional] [default to &#39;UTC&#39;]

### Return type

[**GetDatasetReuse200Response**](GetDatasetReuse200Response.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDatasetReuses_0

> GetDatasetReuses200Response getDatasetReuses_0(source, datasetId, opts)



Get list of reuses 

### Example

```javascript
import Opendatasoft from 'opendatasoft';
let defaultClient = Opendatasoft.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure HTTP basic authorization: basic
let basic = defaultClient.authentications['basic'];
basic.username = 'YOUR USERNAME';
basic.password = 'YOUR PASSWORD';

let apiInstance = new Opendatasoft.OdsApi();
let source = "'catalog'"; // String | Each source represents a different catalog of datasets you'll be able to query.  There are 2 sources available:  * catalog: the catalog of datasets on your portal * opendatasoft: Opendatasoft's repository of public datasets, also available at   [data.opendatasoft.com](https://data.opendatasoft.com/page/home/) 
let datasetId = "datasetId_example"; // String | Dataset identifier.  Can be found in the \"information\" tab of the dataset page. 
let opts = {
  'limit': 10, // Number | Number of items to return.  To use in conjonction with offset to implement pagination.  Limit maximum value is 100. To retrive more data use export entry points. The default value is 10. 
  'offset': 0, // Number | Index of the first item to return (starting at 0).  To use in conjonction with limit to implement pagination. 
  'timezone': "'UTC'" // String | Set timezone for datetime fields
};
apiInstance.getDatasetReuses_0(source, datasetId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source** | **String**| Each source represents a different catalog of datasets you&#39;ll be able to query.  There are 2 sources available:  * catalog: the catalog of datasets on your portal * opendatasoft: Opendatasoft&#39;s repository of public datasets, also available at   [data.opendatasoft.com](https://data.opendatasoft.com/page/home/)  | [default to &#39;catalog&#39;]
 **datasetId** | **String**| Dataset identifier.  Can be found in the \&quot;information\&quot; tab of the dataset page.  | 
 **limit** | **Number**| Number of items to return.  To use in conjonction with offset to implement pagination.  Limit maximum value is 100. To retrive more data use export entry points. The default value is 10.  | [optional] [default to 10]
 **offset** | **Number**| Index of the first item to return (starting at 0).  To use in conjonction with limit to implement pagination.  | [optional] [default to 0]
 **timezone** | **String**| Set timezone for datetime fields | [optional] [default to &#39;UTC&#39;]

### Return type

[**GetDatasetReuses200Response**](GetDatasetReuses200Response.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDatasetSnapshots_0

> GetDatasetSnapshots200Response getDatasetSnapshots_0(source, datasetId, opts)



List of all snapshots for this dataset. 

### Example

```javascript
import Opendatasoft from 'opendatasoft';
let defaultClient = Opendatasoft.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure HTTP basic authorization: basic
let basic = defaultClient.authentications['basic'];
basic.username = 'YOUR USERNAME';
basic.password = 'YOUR PASSWORD';

let apiInstance = new Opendatasoft.OdsApi();
let source = "'catalog'"; // String | Each source represents a different catalog of datasets you'll be able to query.  There are 2 sources available:  * catalog: the catalog of datasets on your portal * opendatasoft: Opendatasoft's repository of public datasets, also available at   [data.opendatasoft.com](https://data.opendatasoft.com/page/home/) 
let datasetId = "datasetId_example"; // String | Dataset identifier.  Can be found in the \"information\" tab of the dataset page. 
let opts = {
  'timezone': "'UTC'" // String | Set timezone for datetime fields
};
apiInstance.getDatasetSnapshots_0(source, datasetId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source** | **String**| Each source represents a different catalog of datasets you&#39;ll be able to query.  There are 2 sources available:  * catalog: the catalog of datasets on your portal * opendatasoft: Opendatasoft&#39;s repository of public datasets, also available at   [data.opendatasoft.com](https://data.opendatasoft.com/page/home/)  | [default to &#39;catalog&#39;]
 **datasetId** | **String**| Dataset identifier.  Can be found in the \&quot;information\&quot; tab of the dataset page.  | 
 **timezone** | **String**| Set timezone for datetime fields | [optional] [default to &#39;UTC&#39;]

### Return type

[**GetDatasetSnapshots200Response**](GetDatasetSnapshots200Response.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDataset_0

> GetDatasets200ResponseDatasetsInner getDataset_0(source, datasetId, opts)



List of available endpoints for the specified dataset, with metadata and endpoints.  Will provide links for: * the attachments endpoint * the files endpoint * the records endpoint * the catalog endpoint 

### Example

```javascript
import Opendatasoft from 'opendatasoft';
let defaultClient = Opendatasoft.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure HTTP basic authorization: basic
let basic = defaultClient.authentications['basic'];
basic.username = 'YOUR USERNAME';
basic.password = 'YOUR PASSWORD';

let apiInstance = new Opendatasoft.OdsApi();
let source = "'catalog'"; // String | Each source represents a different catalog of datasets you'll be able to query.  There are 2 sources available:  * catalog: the catalog of datasets on your portal * opendatasoft: Opendatasoft's repository of public datasets, also available at   [data.opendatasoft.com](https://data.opendatasoft.com/page/home/) 
let datasetId = "datasetId_example"; // String | Dataset identifier.  Can be found in the \"information\" tab of the dataset page. 
let opts = {
  'select': "select_example", // String | A select expression can be used to add, remove or change fields to return. An expression can be:   - a wildcard ('*'): return all fields   - a field name: return only this field   - an include/exclude function. Include (resp exclude) all field matching include/exclude expression. This expression can contain wildcard. For example: include(spa*) will return all fields begining with 'spa'   - a complex expression: return the result of this expression. A label can be set for this expression, in that case, field will be named with this label. For instance: 'size * 2 as bigger_size' will return a new field named bigger_size and containing the double of size field value. 
  'pretty': false, // Boolean | Activate pretty print
  'timezone': "'UTC'", // String | Set timezone for datetime fields
  'includeAppMetas': false // Boolean | Explicitely request application metas for each datasets. 
};
apiInstance.getDataset_0(source, datasetId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source** | **String**| Each source represents a different catalog of datasets you&#39;ll be able to query.  There are 2 sources available:  * catalog: the catalog of datasets on your portal * opendatasoft: Opendatasoft&#39;s repository of public datasets, also available at   [data.opendatasoft.com](https://data.opendatasoft.com/page/home/)  | [default to &#39;catalog&#39;]
 **datasetId** | **String**| Dataset identifier.  Can be found in the \&quot;information\&quot; tab of the dataset page.  | 
 **select** | **String**| A select expression can be used to add, remove or change fields to return. An expression can be:   - a wildcard (&#39;*&#39;): return all fields   - a field name: return only this field   - an include/exclude function. Include (resp exclude) all field matching include/exclude expression. This expression can contain wildcard. For example: include(spa*) will return all fields begining with &#39;spa&#39;   - a complex expression: return the result of this expression. A label can be set for this expression, in that case, field will be named with this label. For instance: &#39;size * 2 as bigger_size&#39; will return a new field named bigger_size and containing the double of size field value.  | [optional] 
 **pretty** | **Boolean**| Activate pretty print | [optional] [default to false]
 **timezone** | **String**| Set timezone for datetime fields | [optional] [default to &#39;UTC&#39;]
 **includeAppMetas** | **Boolean**| Explicitely request application metas for each datasets.  | [optional] [default to false]

### Return type

[**GetDatasets200ResponseDatasetsInner**](GetDatasets200ResponseDatasetsInner.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDatasetsFacets_1

> GetRecordsFacets200Response getDatasetsFacets_1(source, opts)



Enumerate facets values for datasets and return a list of values for each facet. Can be used to implement guided navigation in large result sets.  Read [the facets documentation](https://help.opendatasoft.com/apis/ods-search-v2/#enumerating-facets-values) for more details. 

### Example

```javascript
import Opendatasoft from 'opendatasoft';
let defaultClient = Opendatasoft.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure HTTP basic authorization: basic
let basic = defaultClient.authentications['basic'];
basic.username = 'YOUR USERNAME';
basic.password = 'YOUR PASSWORD';

let apiInstance = new Opendatasoft.OdsApi();
let source = "'catalog'"; // String | Each source represents a different catalog of datasets you'll be able to query.  There are 2 sources available:  * catalog: the catalog of datasets on your portal * opendatasoft: Opendatasoft's repository of public datasets, also available at   [data.opendatasoft.com](https://data.opendatasoft.com/page/home/) 
let opts = {
  'facet': ["null"], // [String] | A facet is a field used for simple filtering (through the parameters refine and exclude) or exploration (with the endpoint `/facets`).  Facets can be configured in the back-office or with this parameter.  Read [the facets documentation](https://help.opendatasoft.com/apis/ods-search-v2/#facets) for more details. 
  'refine': ["null"], // [String] | An array of facet filters. For example **city:Paris** or **modified:2019/12**. The request will only include the selected facet value.  Read [filtering with facets value](https://help.opendatasoft.com/apis/ods-search-v2/#filtering-with-facets-values) for more details.  *Not to be confused with a where filter. Refining with a facet is equivalent to selecting an entry in the left navigation panel.*  *refine is not available for monitoring sources* 
  'exclude': ["null"], // [String] | An array of facet filters. For example **city:Paris** or **modified:2019/12**. The request will exclude the defined facet value.  Read [filtering with facets value](https://help.opendatasoft.com/apis/ods-search-v2/#filtering-with-facets-values) for more details.  *Not to be confused with a where filter. Excluding a facet value is equivalent to removing an entry in the left navigation panel.*  *exclude is not available for monitoring sources* 
  'where': ["null"], // [String] | An array of filters.  A filter is a text expression performing a simple full-text search that can also include logical operations (NOT, AND, OR...) as well as lots of other functions, thus performing more complex and more precise searches.  Read [the query language reference](https://docs.opendatasoft.com/api/explore/v2.html#where-clause) for more details. 
  'search': ["null"], // [String] | An array of full text search.  A full text search performs a prefixed text search for each provided terms in all visible fields of a catalog/dataset. 
  'timezone': "'UTC'" // String | Set timezone for datetime fields
};
apiInstance.getDatasetsFacets_1(source, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source** | **String**| Each source represents a different catalog of datasets you&#39;ll be able to query.  There are 2 sources available:  * catalog: the catalog of datasets on your portal * opendatasoft: Opendatasoft&#39;s repository of public datasets, also available at   [data.opendatasoft.com](https://data.opendatasoft.com/page/home/)  | [default to &#39;catalog&#39;]
 **facet** | [**[String]**](String.md)| A facet is a field used for simple filtering (through the parameters refine and exclude) or exploration (with the endpoint &#x60;/facets&#x60;).  Facets can be configured in the back-office or with this parameter.  Read [the facets documentation](https://help.opendatasoft.com/apis/ods-search-v2/#facets) for more details.  | [optional] 
 **refine** | [**[String]**](String.md)| An array of facet filters. For example **city:Paris** or **modified:2019/12**. The request will only include the selected facet value.  Read [filtering with facets value](https://help.opendatasoft.com/apis/ods-search-v2/#filtering-with-facets-values) for more details.  *Not to be confused with a where filter. Refining with a facet is equivalent to selecting an entry in the left navigation panel.*  *refine is not available for monitoring sources*  | [optional] 
 **exclude** | [**[String]**](String.md)| An array of facet filters. For example **city:Paris** or **modified:2019/12**. The request will exclude the defined facet value.  Read [filtering with facets value](https://help.opendatasoft.com/apis/ods-search-v2/#filtering-with-facets-values) for more details.  *Not to be confused with a where filter. Excluding a facet value is equivalent to removing an entry in the left navigation panel.*  *exclude is not available for monitoring sources*  | [optional] 
 **where** | [**[String]**](String.md)| An array of filters.  A filter is a text expression performing a simple full-text search that can also include logical operations (NOT, AND, OR...) as well as lots of other functions, thus performing more complex and more precise searches.  Read [the query language reference](https://docs.opendatasoft.com/api/explore/v2.html#where-clause) for more details.  | [optional] 
 **search** | [**[String]**](String.md)| An array of full text search.  A full text search performs a prefixed text search for each provided terms in all visible fields of a catalog/dataset.  | [optional] 
 **timezone** | **String**| Set timezone for datetime fields | [optional] [default to &#39;UTC&#39;]

### Return type

[**GetRecordsFacets200Response**](GetRecordsFacets200Response.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDatasets_0

> GetDatasets200Response getDatasets_0(source, opts)



List of available datasets, each with their endpoints, paginated.  Links provided: * previous page * next page * last page * first page 

### Example

```javascript
import Opendatasoft from 'opendatasoft';
let defaultClient = Opendatasoft.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure HTTP basic authorization: basic
let basic = defaultClient.authentications['basic'];
basic.username = 'YOUR USERNAME';
basic.password = 'YOUR PASSWORD';

let apiInstance = new Opendatasoft.OdsApi();
let source = "'catalog'"; // String | Each source represents a different catalog of datasets you'll be able to query.  There are 2 sources available:  * catalog: the catalog of datasets on your portal * opendatasoft: Opendatasoft's repository of public datasets, also available at   [data.opendatasoft.com](https://data.opendatasoft.com/page/home/) 
let opts = {
  'select': "select_example", // String | A select expression can be used to add, remove or change fields to return. An expression can be:   - a wildcard ('*'): return all fields   - a field name: return only this field   - an include/exclude function. Include (resp exclude) all field matching include/exclude expression. This expression can contain wildcard. For example: include(spa*) will return all fields begining with 'spa'   - a complex expression: return the result of this expression. A label can be set for this expression, in that case, field will be named with this label. For instance: 'size * 2 as bigger_size' will return a new field named bigger_size and containing the double of size field value. 
  'where': ["null"], // [String] | An array of filters.  A filter is a text expression performing a simple full-text search that can also include logical operations (NOT, AND, OR...) as well as lots of other functions, thus performing more complex and more precise searches.  Read [the query language reference](https://docs.opendatasoft.com/api/explore/v2.html#where-clause) for more details. 
  'groupBy': "groupBy_example", // String | A group by expression defines a grouping function for an aggregation. It can be:  - a field name: group result by each value of this field  - a range function: group result by range  - a date function: group result by date It is possible to specify a custom name with the 'as name' notation. For instance: group_by='city_field as city'. 
  'sort': ["null"], // [String] | **Deprecated, use `order_by` instead.**  A list of field names, each possibly prefixed with a minus (-).  Sorts results according to the specified fields' values. By default, the sort is ascending (from the smallest value to the biggest value). A minus sign (‘-‘) may be used to perform a descending sort. Sorting is only available on numeric fields (int, double, date and datetime) and on text fields which have the sortable annotation. 
  'orderBy': ["null"], // [String] | A comma-separated list of field names or aggregations to sort on, followed by an order (`asc` or `desc`).  Sorts results according to the specified fields' values in ascending order by default. To sort results in descending order, use the `desc` keyword.  Example: `sum(age) desc, name asc` 
  'limit': 10, // Number | Number of items to return.  To use in conjonction with offset to implement pagination.  Limit maximum value is 100. To retrive more data use export entry points. The default value is 10. 
  'offset': 0, // Number | Index of the first item to return (starting at 0).  To use in conjonction with limit to implement pagination. 
  'search': ["null"], // [String] | An array of full text search.  A full text search performs a prefixed text search for each provided terms in all visible fields of a catalog/dataset. 
  'facet': ["null"], // [String] | A facet is a field used for simple filtering (through the parameters refine and exclude) or exploration (with the endpoint `/facets`).  Facets can be configured in the back-office or with this parameter.  Read [the facets documentation](https://help.opendatasoft.com/apis/ods-search-v2/#facets) for more details. 
  'refine': ["null"], // [String] | An array of facet filters. For example **city:Paris** or **modified:2019/12**. The request will only include the selected facet value.  Read [filtering with facets value](https://help.opendatasoft.com/apis/ods-search-v2/#filtering-with-facets-values) for more details.  *Not to be confused with a where filter. Refining with a facet is equivalent to selecting an entry in the left navigation panel.*  *refine is not available for monitoring sources* 
  'exclude': ["null"], // [String] | An array of facet filters. For example **city:Paris** or **modified:2019/12**. The request will exclude the defined facet value.  Read [filtering with facets value](https://help.opendatasoft.com/apis/ods-search-v2/#filtering-with-facets-values) for more details.  *Not to be confused with a where filter. Excluding a facet value is equivalent to removing an entry in the left navigation panel.*  *exclude is not available for monitoring sources* 
  'pretty': false, // Boolean | Activate pretty print
  'timezone': "'UTC'", // String | Set timezone for datetime fields
  'includeAppMetas': false // Boolean | Explicitely request application metas for each datasets. 
};
apiInstance.getDatasets_0(source, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source** | **String**| Each source represents a different catalog of datasets you&#39;ll be able to query.  There are 2 sources available:  * catalog: the catalog of datasets on your portal * opendatasoft: Opendatasoft&#39;s repository of public datasets, also available at   [data.opendatasoft.com](https://data.opendatasoft.com/page/home/)  | [default to &#39;catalog&#39;]
 **select** | **String**| A select expression can be used to add, remove or change fields to return. An expression can be:   - a wildcard (&#39;*&#39;): return all fields   - a field name: return only this field   - an include/exclude function. Include (resp exclude) all field matching include/exclude expression. This expression can contain wildcard. For example: include(spa*) will return all fields begining with &#39;spa&#39;   - a complex expression: return the result of this expression. A label can be set for this expression, in that case, field will be named with this label. For instance: &#39;size * 2 as bigger_size&#39; will return a new field named bigger_size and containing the double of size field value.  | [optional] 
 **where** | [**[String]**](String.md)| An array of filters.  A filter is a text expression performing a simple full-text search that can also include logical operations (NOT, AND, OR...) as well as lots of other functions, thus performing more complex and more precise searches.  Read [the query language reference](https://docs.opendatasoft.com/api/explore/v2.html#where-clause) for more details.  | [optional] 
 **groupBy** | **String**| A group by expression defines a grouping function for an aggregation. It can be:  - a field name: group result by each value of this field  - a range function: group result by range  - a date function: group result by date It is possible to specify a custom name with the &#39;as name&#39; notation. For instance: group_by&#x3D;&#39;city_field as city&#39;.  | [optional] 
 **sort** | [**[String]**](String.md)| **Deprecated, use &#x60;order_by&#x60; instead.**  A list of field names, each possibly prefixed with a minus (-).  Sorts results according to the specified fields&#39; values. By default, the sort is ascending (from the smallest value to the biggest value). A minus sign (‘-‘) may be used to perform a descending sort. Sorting is only available on numeric fields (int, double, date and datetime) and on text fields which have the sortable annotation.  | [optional] 
 **orderBy** | [**[String]**](String.md)| A comma-separated list of field names or aggregations to sort on, followed by an order (&#x60;asc&#x60; or &#x60;desc&#x60;).  Sorts results according to the specified fields&#39; values in ascending order by default. To sort results in descending order, use the &#x60;desc&#x60; keyword.  Example: &#x60;sum(age) desc, name asc&#x60;  | [optional] 
 **limit** | **Number**| Number of items to return.  To use in conjonction with offset to implement pagination.  Limit maximum value is 100. To retrive more data use export entry points. The default value is 10.  | [optional] [default to 10]
 **offset** | **Number**| Index of the first item to return (starting at 0).  To use in conjonction with limit to implement pagination.  | [optional] [default to 0]
 **search** | [**[String]**](String.md)| An array of full text search.  A full text search performs a prefixed text search for each provided terms in all visible fields of a catalog/dataset.  | [optional] 
 **facet** | [**[String]**](String.md)| A facet is a field used for simple filtering (through the parameters refine and exclude) or exploration (with the endpoint &#x60;/facets&#x60;).  Facets can be configured in the back-office or with this parameter.  Read [the facets documentation](https://help.opendatasoft.com/apis/ods-search-v2/#facets) for more details.  | [optional] 
 **refine** | [**[String]**](String.md)| An array of facet filters. For example **city:Paris** or **modified:2019/12**. The request will only include the selected facet value.  Read [filtering with facets value](https://help.opendatasoft.com/apis/ods-search-v2/#filtering-with-facets-values) for more details.  *Not to be confused with a where filter. Refining with a facet is equivalent to selecting an entry in the left navigation panel.*  *refine is not available for monitoring sources*  | [optional] 
 **exclude** | [**[String]**](String.md)| An array of facet filters. For example **city:Paris** or **modified:2019/12**. The request will exclude the defined facet value.  Read [filtering with facets value](https://help.opendatasoft.com/apis/ods-search-v2/#filtering-with-facets-values) for more details.  *Not to be confused with a where filter. Excluding a facet value is equivalent to removing an entry in the left navigation panel.*  *exclude is not available for monitoring sources*  | [optional] 
 **pretty** | **Boolean**| Activate pretty print | [optional] [default to false]
 **timezone** | **String**| Set timezone for datetime fields | [optional] [default to &#39;UTC&#39;]
 **includeAppMetas** | **Boolean**| Explicitely request application metas for each datasets.  | [optional] [default to false]

### Return type

[**GetDatasets200Response**](GetDatasets200Response.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getMetadataTemplate_0

> GetMetadataTemplatesType200ResponseMetadataTemplatesInner getMetadataTemplate_0(source, metadataTemplateType, metadataTemplateName)



A single metadata_template 

### Example

```javascript
import Opendatasoft from 'opendatasoft';
let defaultClient = Opendatasoft.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure HTTP basic authorization: basic
let basic = defaultClient.authentications['basic'];
basic.username = 'YOUR USERNAME';
basic.password = 'YOUR PASSWORD';

let apiInstance = new Opendatasoft.OdsApi();
let source = "'catalog'"; // String | Each source represents a different catalog of datasets you'll be able to query.  There are 2 sources available:  * catalog: the catalog of datasets on your portal * opendatasoft: Opendatasoft's repository of public datasets, also available at   [data.opendatasoft.com](https://data.opendatasoft.com/page/home/) 
let metadataTemplateType = "'basic'"; // String | 
let metadataTemplateName = "metadataTemplateName_example"; // String | 
apiInstance.getMetadataTemplate_0(source, metadataTemplateType, metadataTemplateName, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source** | **String**| Each source represents a different catalog of datasets you&#39;ll be able to query.  There are 2 sources available:  * catalog: the catalog of datasets on your portal * opendatasoft: Opendatasoft&#39;s repository of public datasets, also available at   [data.opendatasoft.com](https://data.opendatasoft.com/page/home/)  | [default to &#39;catalog&#39;]
 **metadataTemplateType** | **String**|  | [default to &#39;basic&#39;]
 **metadataTemplateName** | **String**|  | 

### Return type

[**GetMetadataTemplatesType200ResponseMetadataTemplatesInner**](GetMetadataTemplatesType200ResponseMetadataTemplatesInner.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getMetadataTemplatesType_0

> GetMetadataTemplatesType200Response getMetadataTemplatesType_0(source, metadataTemplateType)



List of metadata templates available for this type. 

### Example

```javascript
import Opendatasoft from 'opendatasoft';
let defaultClient = Opendatasoft.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure HTTP basic authorization: basic
let basic = defaultClient.authentications['basic'];
basic.username = 'YOUR USERNAME';
basic.password = 'YOUR PASSWORD';

let apiInstance = new Opendatasoft.OdsApi();
let source = "'catalog'"; // String | Each source represents a different catalog of datasets you'll be able to query.  There are 2 sources available:  * catalog: the catalog of datasets on your portal * opendatasoft: Opendatasoft's repository of public datasets, also available at   [data.opendatasoft.com](https://data.opendatasoft.com/page/home/) 
let metadataTemplateType = "'basic'"; // String | 
apiInstance.getMetadataTemplatesType_0(source, metadataTemplateType, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source** | **String**| Each source represents a different catalog of datasets you&#39;ll be able to query.  There are 2 sources available:  * catalog: the catalog of datasets on your portal * opendatasoft: Opendatasoft&#39;s repository of public datasets, also available at   [data.opendatasoft.com](https://data.opendatasoft.com/page/home/)  | [default to &#39;catalog&#39;]
 **metadataTemplateType** | **String**|  | [default to &#39;basic&#39;]

### Return type

[**GetMetadataTemplatesType200Response**](GetMetadataTemplatesType200Response.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getMetadataTemplatesTypes_0

> GetRoot200Response getMetadataTemplatesTypes_0(source)



List of available metadata templates types, each with their endpoints. 

### Example

```javascript
import Opendatasoft from 'opendatasoft';
let defaultClient = Opendatasoft.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure HTTP basic authorization: basic
let basic = defaultClient.authentications['basic'];
basic.username = 'YOUR USERNAME';
basic.password = 'YOUR PASSWORD';

let apiInstance = new Opendatasoft.OdsApi();
let source = "'catalog'"; // String | Each source represents a different catalog of datasets you'll be able to query.  There are 2 sources available:  * catalog: the catalog of datasets on your portal * opendatasoft: Opendatasoft's repository of public datasets, also available at   [data.opendatasoft.com](https://data.opendatasoft.com/page/home/) 
apiInstance.getMetadataTemplatesTypes_0(source, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source** | **String**| Each source represents a different catalog of datasets you&#39;ll be able to query.  There are 2 sources available:  * catalog: the catalog of datasets on your portal * opendatasoft: Opendatasoft&#39;s repository of public datasets, also available at   [data.opendatasoft.com](https://data.opendatasoft.com/page/home/)  | [default to &#39;catalog&#39;]

### Return type

[**GetRoot200Response**](GetRoot200Response.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPage_0

> GetPages200ResponsePagesInner getPage_0(slug)



A single page&#39;s metadata from this portal 

### Example

```javascript
import Opendatasoft from 'opendatasoft';
let defaultClient = Opendatasoft.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure HTTP basic authorization: basic
let basic = defaultClient.authentications['basic'];
basic.username = 'YOUR USERNAME';
basic.password = 'YOUR PASSWORD';

let apiInstance = new Opendatasoft.OdsApi();
let slug = "slug_example"; // String | Page slug. 
apiInstance.getPage_0(slug, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **String**| Page slug.  | 

### Return type

[**GetPages200ResponsePagesInner**](GetPages200ResponsePagesInner.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPages_0

> GetPages200Response getPages_0()



List of all pages from this portal. 

### Example

```javascript
import Opendatasoft from 'opendatasoft';
let defaultClient = Opendatasoft.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure HTTP basic authorization: basic
let basic = defaultClient.authentications['basic'];
basic.username = 'YOUR USERNAME';
basic.password = 'YOUR PASSWORD';

let apiInstance = new Opendatasoft.OdsApi();
apiInstance.getPages_0((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**GetPages200Response**](GetPages200Response.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getRecord_0

> GetRecords200ResponseRecordsInner getRecord_0(source, datasetId, recordId, opts)



Retrieve a single record based on its ID. 

### Example

```javascript
import Opendatasoft from 'opendatasoft';
let defaultClient = Opendatasoft.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure HTTP basic authorization: basic
let basic = defaultClient.authentications['basic'];
basic.username = 'YOUR USERNAME';
basic.password = 'YOUR PASSWORD';

let apiInstance = new Opendatasoft.OdsApi();
let source = "'catalog'"; // String | Each source represents a different catalog of datasets you'll be able to query.  There are 2 sources available:  * catalog: the catalog of datasets on your portal * opendatasoft: Opendatasoft's repository of public datasets, also available at   [data.opendatasoft.com](https://data.opendatasoft.com/page/home/) 
let datasetId = "datasetId_example"; // String | Dataset identifier.  Can be found in the \"information\" tab of the dataset page. 
let recordId = "recordId_example"; // String | 
let opts = {
  'select': "select_example", // String | A select expression can be used to add, remove or change fields to return. An expression can be:   - a wildcard ('*'): return all fields   - a field name: return only this field   - an include/exclude function. Include (resp exclude) all field matching include/exclude expression. This expression can contain wildcard. For example: include(spa*) will return all fields begining with 'spa'   - a complex expression: return the result of this expression. A label can be set for this expression, in that case, field will be named with this label. For instance: 'size * 2 as bigger_size' will return a new field named bigger_size and containing the double of size field value. 
  'pretty': false, // Boolean | Activate pretty print
  'timezone': "'UTC'" // String | Set timezone for datetime fields
};
apiInstance.getRecord_0(source, datasetId, recordId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source** | **String**| Each source represents a different catalog of datasets you&#39;ll be able to query.  There are 2 sources available:  * catalog: the catalog of datasets on your portal * opendatasoft: Opendatasoft&#39;s repository of public datasets, also available at   [data.opendatasoft.com](https://data.opendatasoft.com/page/home/)  | [default to &#39;catalog&#39;]
 **datasetId** | **String**| Dataset identifier.  Can be found in the \&quot;information\&quot; tab of the dataset page.  | 
 **recordId** | **String**|  | 
 **select** | **String**| A select expression can be used to add, remove or change fields to return. An expression can be:   - a wildcard (&#39;*&#39;): return all fields   - a field name: return only this field   - an include/exclude function. Include (resp exclude) all field matching include/exclude expression. This expression can contain wildcard. For example: include(spa*) will return all fields begining with &#39;spa&#39;   - a complex expression: return the result of this expression. A label can be set for this expression, in that case, field will be named with this label. For instance: &#39;size * 2 as bigger_size&#39; will return a new field named bigger_size and containing the double of size field value.  | [optional] 
 **pretty** | **Boolean**| Activate pretty print | [optional] [default to false]
 **timezone** | **String**| Set timezone for datetime fields | [optional] [default to &#39;UTC&#39;]

### Return type

[**GetRecords200ResponseRecordsInner**](GetRecords200ResponseRecordsInner.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getRecordsFacets_1

> GetRecordsFacets200Response getRecordsFacets_1(source, datasetId, opts)



Enumerate facets values for records and return a list of values for each facet. Can be used to implement guided navigation in large result sets.  Read [the facets documentation](https://help.opendatasoft.com/apis/ods-search-v2/#enumerating-facets-values) for more details. 

### Example

```javascript
import Opendatasoft from 'opendatasoft';
let defaultClient = Opendatasoft.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure HTTP basic authorization: basic
let basic = defaultClient.authentications['basic'];
basic.username = 'YOUR USERNAME';
basic.password = 'YOUR PASSWORD';

let apiInstance = new Opendatasoft.OdsApi();
let source = "'catalog'"; // String | Each source represents a different catalog of datasets you'll be able to query.  There are 2 sources available:  * catalog: the catalog of datasets on your portal * opendatasoft: Opendatasoft's repository of public datasets, also available at   [data.opendatasoft.com](https://data.opendatasoft.com/page/home/) 
let datasetId = "datasetId_example"; // String | Dataset identifier.  Can be found in the \"information\" tab of the dataset page. 
let opts = {
  'where': ["null"], // [String] | An array of filters.  A filter is a text expression performing a simple full-text search that can also include logical operations (NOT, AND, OR...) as well as lots of other functions, thus performing more complex and more precise searches.  Read [the query language reference](https://docs.opendatasoft.com/api/explore/v2.html#where-clause) for more details. 
  'facet': ["null"], // [String] | A facet is a field used for simple filtering (through the parameters refine and exclude) or exploration (with the endpoint `/facets`).  Facets can be configured in the back-office or with this parameter.  Read [the facets documentation](https://help.opendatasoft.com/apis/ods-search-v2/#facets) for more details. 
  'refine': ["null"], // [String] | An array of facet filters. For example **city:Paris** or **modified:2019/12**. The request will only include the selected facet value.  Read [filtering with facets value](https://help.opendatasoft.com/apis/ods-search-v2/#filtering-with-facets-values) for more details.  *Not to be confused with a where filter. Refining with a facet is equivalent to selecting an entry in the left navigation panel.*  *refine is not available for monitoring sources* 
  'exclude': ["null"], // [String] | An array of facet filters. For example **city:Paris** or **modified:2019/12**. The request will exclude the defined facet value.  Read [filtering with facets value](https://help.opendatasoft.com/apis/ods-search-v2/#filtering-with-facets-values) for more details.  *Not to be confused with a where filter. Excluding a facet value is equivalent to removing an entry in the left navigation panel.*  *exclude is not available for monitoring sources* 
  'search': ["null"], // [String] | An array of full text search.  A full text search performs a prefixed text search for each provided terms in all visible fields of a catalog/dataset. 
  'timezone': "'UTC'" // String | Set timezone for datetime fields
};
apiInstance.getRecordsFacets_1(source, datasetId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source** | **String**| Each source represents a different catalog of datasets you&#39;ll be able to query.  There are 2 sources available:  * catalog: the catalog of datasets on your portal * opendatasoft: Opendatasoft&#39;s repository of public datasets, also available at   [data.opendatasoft.com](https://data.opendatasoft.com/page/home/)  | [default to &#39;catalog&#39;]
 **datasetId** | **String**| Dataset identifier.  Can be found in the \&quot;information\&quot; tab of the dataset page.  | 
 **where** | [**[String]**](String.md)| An array of filters.  A filter is a text expression performing a simple full-text search that can also include logical operations (NOT, AND, OR...) as well as lots of other functions, thus performing more complex and more precise searches.  Read [the query language reference](https://docs.opendatasoft.com/api/explore/v2.html#where-clause) for more details.  | [optional] 
 **facet** | [**[String]**](String.md)| A facet is a field used for simple filtering (through the parameters refine and exclude) or exploration (with the endpoint &#x60;/facets&#x60;).  Facets can be configured in the back-office or with this parameter.  Read [the facets documentation](https://help.opendatasoft.com/apis/ods-search-v2/#facets) for more details.  | [optional] 
 **refine** | [**[String]**](String.md)| An array of facet filters. For example **city:Paris** or **modified:2019/12**. The request will only include the selected facet value.  Read [filtering with facets value](https://help.opendatasoft.com/apis/ods-search-v2/#filtering-with-facets-values) for more details.  *Not to be confused with a where filter. Refining with a facet is equivalent to selecting an entry in the left navigation panel.*  *refine is not available for monitoring sources*  | [optional] 
 **exclude** | [**[String]**](String.md)| An array of facet filters. For example **city:Paris** or **modified:2019/12**. The request will exclude the defined facet value.  Read [filtering with facets value](https://help.opendatasoft.com/apis/ods-search-v2/#filtering-with-facets-values) for more details.  *Not to be confused with a where filter. Excluding a facet value is equivalent to removing an entry in the left navigation panel.*  *exclude is not available for monitoring sources*  | [optional] 
 **search** | [**[String]**](String.md)| An array of full text search.  A full text search performs a prefixed text search for each provided terms in all visible fields of a catalog/dataset.  | [optional] 
 **timezone** | **String**| Set timezone for datetime fields | [optional] [default to &#39;UTC&#39;]

### Return type

[**GetRecordsFacets200Response**](GetRecordsFacets200Response.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getRecords_0

> GetRecords200Response getRecords_0(source, datasetId, opts)



Search dataset&#39;s records. 

### Example

```javascript
import Opendatasoft from 'opendatasoft';
let defaultClient = Opendatasoft.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure HTTP basic authorization: basic
let basic = defaultClient.authentications['basic'];
basic.username = 'YOUR USERNAME';
basic.password = 'YOUR PASSWORD';

let apiInstance = new Opendatasoft.OdsApi();
let source = "'catalog'"; // String | Each source represents a different catalog of datasets you'll be able to query.  There are 2 sources available:  * catalog: the catalog of datasets on your portal * opendatasoft: Opendatasoft's repository of public datasets, also available at   [data.opendatasoft.com](https://data.opendatasoft.com/page/home/) 
let datasetId = "datasetId_example"; // String | Dataset identifier.  Can be found in the \"information\" tab of the dataset page. 
let opts = {
  'select': "select_example", // String | A select expression can be used to add, remove or change fields to return. An expression can be:   - a wildcard ('*'): return all fields   - a field name: return only this field   - an include/exclude function. Include (resp exclude) all field matching include/exclude expression. This expression can contain wildcard. For example: include(spa*) will return all fields begining with 'spa'   - a complex expression: return the result of this expression. A label can be set for this expression, in that case, field will be named with this label. For instance: 'size * 2 as bigger_size' will return a new field named bigger_size and containing the double of size field value. 
  'where': ["null"], // [String] | An array of filters.  A filter is a text expression performing a simple full-text search that can also include logical operations (NOT, AND, OR...) as well as lots of other functions, thus performing more complex and more precise searches.  Read [the query language reference](https://docs.opendatasoft.com/api/explore/v2.html#where-clause) for more details. 
  'groupBy': "groupBy_example", // String | A group by expression defines a grouping function for an aggregation. It can be:  - a field name: group result by each value of this field  - a range function: group result by range  - a date function: group result by date It is possible to specify a custom name with the 'as name' notation. For instance: group_by='city_field as city'. 
  'sort': ["null"], // [String] | **Deprecated, use `order_by` instead.**  A list of field names, each possibly prefixed with a minus (-).  Sorts results according to the specified fields' values. By default, the sort is ascending (from the smallest value to the biggest value). A minus sign (‘-‘) may be used to perform a descending sort. Sorting is only available on numeric fields (int, double, date and datetime) and on text fields which have the sortable annotation. 
  'orderBy': ["null"], // [String] | A comma-separated list of field names or aggregations to sort on, followed by an order (`asc` or `desc`).  Sorts results according to the specified fields' values in ascending order by default. To sort results in descending order, use the `desc` keyword.  Example: `sum(age) desc, name asc` 
  'limit': 10, // Number | Number of items to return.  To use in conjonction with offset to implement pagination.  Limit maximum value is 100. To retrive more data use export entry points. The default value is 10. 
  'offset': 0, // Number | Index of the first item to return (starting at 0).  To use in conjonction with limit to implement pagination. 
  'search': ["null"], // [String] | An array of full text search.  A full text search performs a prefixed text search for each provided terms in all visible fields of a catalog/dataset. 
  'facet': ["null"], // [String] | A facet is a field used for simple filtering (through the parameters refine and exclude) or exploration (with the endpoint `/facets`).  Facets can be configured in the back-office or with this parameter.  Read [the facets documentation](https://help.opendatasoft.com/apis/ods-search-v2/#facets) for more details. 
  'refine': ["null"], // [String] | An array of facet filters. For example **city:Paris** or **modified:2019/12**. The request will only include the selected facet value.  Read [filtering with facets value](https://help.opendatasoft.com/apis/ods-search-v2/#filtering-with-facets-values) for more details.  *Not to be confused with a where filter. Refining with a facet is equivalent to selecting an entry in the left navigation panel.*  *refine is not available for monitoring sources* 
  'exclude': ["null"], // [String] | An array of facet filters. For example **city:Paris** or **modified:2019/12**. The request will exclude the defined facet value.  Read [filtering with facets value](https://help.opendatasoft.com/apis/ods-search-v2/#filtering-with-facets-values) for more details.  *Not to be confused with a where filter. Excluding a facet value is equivalent to removing an entry in the left navigation panel.*  *exclude is not available for monitoring sources* 
  'pretty': false, // Boolean | Activate pretty print
  'timezone': "'UTC'" // String | Set timezone for datetime fields
};
apiInstance.getRecords_0(source, datasetId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source** | **String**| Each source represents a different catalog of datasets you&#39;ll be able to query.  There are 2 sources available:  * catalog: the catalog of datasets on your portal * opendatasoft: Opendatasoft&#39;s repository of public datasets, also available at   [data.opendatasoft.com](https://data.opendatasoft.com/page/home/)  | [default to &#39;catalog&#39;]
 **datasetId** | **String**| Dataset identifier.  Can be found in the \&quot;information\&quot; tab of the dataset page.  | 
 **select** | **String**| A select expression can be used to add, remove or change fields to return. An expression can be:   - a wildcard (&#39;*&#39;): return all fields   - a field name: return only this field   - an include/exclude function. Include (resp exclude) all field matching include/exclude expression. This expression can contain wildcard. For example: include(spa*) will return all fields begining with &#39;spa&#39;   - a complex expression: return the result of this expression. A label can be set for this expression, in that case, field will be named with this label. For instance: &#39;size * 2 as bigger_size&#39; will return a new field named bigger_size and containing the double of size field value.  | [optional] 
 **where** | [**[String]**](String.md)| An array of filters.  A filter is a text expression performing a simple full-text search that can also include logical operations (NOT, AND, OR...) as well as lots of other functions, thus performing more complex and more precise searches.  Read [the query language reference](https://docs.opendatasoft.com/api/explore/v2.html#where-clause) for more details.  | [optional] 
 **groupBy** | **String**| A group by expression defines a grouping function for an aggregation. It can be:  - a field name: group result by each value of this field  - a range function: group result by range  - a date function: group result by date It is possible to specify a custom name with the &#39;as name&#39; notation. For instance: group_by&#x3D;&#39;city_field as city&#39;.  | [optional] 
 **sort** | [**[String]**](String.md)| **Deprecated, use &#x60;order_by&#x60; instead.**  A list of field names, each possibly prefixed with a minus (-).  Sorts results according to the specified fields&#39; values. By default, the sort is ascending (from the smallest value to the biggest value). A minus sign (‘-‘) may be used to perform a descending sort. Sorting is only available on numeric fields (int, double, date and datetime) and on text fields which have the sortable annotation.  | [optional] 
 **orderBy** | [**[String]**](String.md)| A comma-separated list of field names or aggregations to sort on, followed by an order (&#x60;asc&#x60; or &#x60;desc&#x60;).  Sorts results according to the specified fields&#39; values in ascending order by default. To sort results in descending order, use the &#x60;desc&#x60; keyword.  Example: &#x60;sum(age) desc, name asc&#x60;  | [optional] 
 **limit** | **Number**| Number of items to return.  To use in conjonction with offset to implement pagination.  Limit maximum value is 100. To retrive more data use export entry points. The default value is 10.  | [optional] [default to 10]
 **offset** | **Number**| Index of the first item to return (starting at 0).  To use in conjonction with limit to implement pagination.  | [optional] [default to 0]
 **search** | [**[String]**](String.md)| An array of full text search.  A full text search performs a prefixed text search for each provided terms in all visible fields of a catalog/dataset.  | [optional] 
 **facet** | [**[String]**](String.md)| A facet is a field used for simple filtering (through the parameters refine and exclude) or exploration (with the endpoint &#x60;/facets&#x60;).  Facets can be configured in the back-office or with this parameter.  Read [the facets documentation](https://help.opendatasoft.com/apis/ods-search-v2/#facets) for more details.  | [optional] 
 **refine** | [**[String]**](String.md)| An array of facet filters. For example **city:Paris** or **modified:2019/12**. The request will only include the selected facet value.  Read [filtering with facets value](https://help.opendatasoft.com/apis/ods-search-v2/#filtering-with-facets-values) for more details.  *Not to be confused with a where filter. Refining with a facet is equivalent to selecting an entry in the left navigation panel.*  *refine is not available for monitoring sources*  | [optional] 
 **exclude** | [**[String]**](String.md)| An array of facet filters. For example **city:Paris** or **modified:2019/12**. The request will exclude the defined facet value.  Read [filtering with facets value](https://help.opendatasoft.com/apis/ods-search-v2/#filtering-with-facets-values) for more details.  *Not to be confused with a where filter. Excluding a facet value is equivalent to removing an entry in the left navigation panel.*  *exclude is not available for monitoring sources*  | [optional] 
 **pretty** | **Boolean**| Activate pretty print | [optional] [default to false]
 **timezone** | **String**| Set timezone for datetime fields | [optional] [default to &#39;UTC&#39;]

### Return type

[**GetRecords200Response**](GetRecords200Response.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getRoot_0

> GetRoot200Response getRoot_0()



API entry point  Provides links for: * catalog, your domain&#39;s list of datasets * opendatasoft, all datasets on the Opendatasoft network 

### Example

```javascript
import Opendatasoft from 'opendatasoft';
let defaultClient = Opendatasoft.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure HTTP basic authorization: basic
let basic = defaultClient.authentications['basic'];
basic.username = 'YOUR USERNAME';
basic.password = 'YOUR PASSWORD';

let apiInstance = new Opendatasoft.OdsApi();
apiInstance.getRoot_0((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**GetRoot200Response**](GetRoot200Response.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSource_0

> GetRoot200Response getSource_0(source)



Source entry points  Provides links for the source&#39;s datasets and metadata. 

### Example

```javascript
import Opendatasoft from 'opendatasoft';
let defaultClient = Opendatasoft.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure HTTP basic authorization: basic
let basic = defaultClient.authentications['basic'];
basic.username = 'YOUR USERNAME';
basic.password = 'YOUR PASSWORD';

let apiInstance = new Opendatasoft.OdsApi();
let source = "'catalog'"; // String | Each source represents a different catalog of datasets you'll be able to query.  There are 2 sources available:  * catalog: the catalog of datasets on your portal * opendatasoft: Opendatasoft's repository of public datasets, also available at   [data.opendatasoft.com](https://data.opendatasoft.com/page/home/) 
apiInstance.getSource_0(source, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source** | **String**| Each source represents a different catalog of datasets you&#39;ll be able to query.  There are 2 sources available:  * catalog: the catalog of datasets on your portal * opendatasoft: Opendatasoft&#39;s repository of public datasets, also available at   [data.opendatasoft.com](https://data.opendatasoft.com/page/home/)  | [default to &#39;catalog&#39;]

### Return type

[**GetRoot200Response**](GetRoot200Response.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## sendDatasetFeedback_0

> sendDatasetFeedback_0(source, datasetId, feedback)



Create new feedback entry. 

### Example

```javascript
import Opendatasoft from 'opendatasoft';
let defaultClient = Opendatasoft.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure HTTP basic authorization: basic
let basic = defaultClient.authentications['basic'];
basic.username = 'YOUR USERNAME';
basic.password = 'YOUR PASSWORD';

let apiInstance = new Opendatasoft.OdsApi();
let source = "'catalog'"; // String | Each source represents a different catalog of datasets you'll be able to query.  There are 2 sources available:  * catalog: the catalog of datasets on your portal * opendatasoft: Opendatasoft's repository of public datasets, also available at   [data.opendatasoft.com](https://data.opendatasoft.com/page/home/) 
let datasetId = "datasetId_example"; // String | Dataset identifier.  Can be found in the \"information\" tab of the dataset page. 
let feedback = new Opendatasoft.SendDatasetFeedbackRequest(); // SendDatasetFeedbackRequest | Feedback entry
apiInstance.sendDatasetFeedback_0(source, datasetId, feedback, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source** | **String**| Each source represents a different catalog of datasets you&#39;ll be able to query.  There are 2 sources available:  * catalog: the catalog of datasets on your portal * opendatasoft: Opendatasoft&#39;s repository of public datasets, also available at   [data.opendatasoft.com](https://data.opendatasoft.com/page/home/)  | [default to &#39;catalog&#39;]
 **datasetId** | **String**| Dataset identifier.  Can be found in the \&quot;information\&quot; tab of the dataset page.  | 
 **feedback** | [**SendDatasetFeedbackRequest**](SendDatasetFeedbackRequest.md)| Feedback entry | 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

