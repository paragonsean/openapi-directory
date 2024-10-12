# Opendatasoft.DatasetApi

All URIs are relative to *https://public.opendatasoft.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**aggregateRecords**](DatasetApi.md#aggregateRecords) | **GET** /{source}/datasets/{dataset_id}/aggregates | 
[**downloadDatasetAttachement**](DatasetApi.md#downloadDatasetAttachement) | **GET** /{source}/datasets/{dataset_id}/attachments/{attachment_id} | 
[**downloadDatasetSnapshot**](DatasetApi.md#downloadDatasetSnapshot) | **GET** /{source}/datasets/{dataset_id}/snapshots/{snapshot_id} | 
[**getDataset**](DatasetApi.md#getDataset) | **GET** /{source}/datasets/{dataset_id} | 
[**getDatasetAttachements**](DatasetApi.md#getDatasetAttachements) | **GET** /{source}/datasets/{dataset_id}/attachments | 
[**getDatasetFile**](DatasetApi.md#getDatasetFile) | **GET** /{source}/datasets/{dataset_id}/files/{file_id} | 
[**getDatasetReuse**](DatasetApi.md#getDatasetReuse) | **GET** /{source}/datasets/{dataset_id}/reuses/{reuse_id} | 
[**getDatasetReuses**](DatasetApi.md#getDatasetReuses) | **GET** /{source}/datasets/{dataset_id}/reuses | 
[**getDatasetSnapshots**](DatasetApi.md#getDatasetSnapshots) | **GET** /{source}/datasets/{dataset_id}/snapshots | 
[**getRecord**](DatasetApi.md#getRecord) | **GET** /{source}/datasets/{dataset_id}/records/{record_id} | 
[**getRecords**](DatasetApi.md#getRecords) | **GET** /{source}/datasets/{dataset_id}/records | 
[**getRecordsFacets**](DatasetApi.md#getRecordsFacets) | **GET** /{source}/datasets/{dataset_id}/facets | 
[**sendDatasetFeedback**](DatasetApi.md#sendDatasetFeedback) | **PUT** /{source}/datasets/{dataset_id}/feedback | 



## aggregateRecords

> AggregateDatasets200Response aggregateRecords(source, datasetId, opts)



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

let apiInstance = new Opendatasoft.DatasetApi();
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
apiInstance.aggregateRecords(source, datasetId, opts, (error, data, response) => {
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


## downloadDatasetAttachement

> downloadDatasetAttachement(source, datasetId, attachmentId)



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

let apiInstance = new Opendatasoft.DatasetApi();
let source = "'catalog'"; // String | Each source represents a different catalog of datasets you'll be able to query.  There are 2 sources available:  * catalog: the catalog of datasets on your portal * opendatasoft: Opendatasoft's repository of public datasets, also available at   [data.opendatasoft.com](https://data.opendatasoft.com/page/home/) 
let datasetId = "datasetId_example"; // String | Dataset identifier.  Can be found in the \"information\" tab of the dataset page. 
let attachmentId = "attachmentId_example"; // String | 
apiInstance.downloadDatasetAttachement(source, datasetId, attachmentId, (error, data, response) => {
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


## downloadDatasetSnapshot

> downloadDatasetSnapshot(source, datasetId, snapshotId, opts)



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

let apiInstance = new Opendatasoft.DatasetApi();
let source = "'catalog'"; // String | Each source represents a different catalog of datasets you'll be able to query.  There are 2 sources available:  * catalog: the catalog of datasets on your portal * opendatasoft: Opendatasoft's repository of public datasets, also available at   [data.opendatasoft.com](https://data.opendatasoft.com/page/home/) 
let datasetId = "datasetId_example"; // String | Dataset identifier.  Can be found in the \"information\" tab of the dataset page. 
let snapshotId = "snapshotId_example"; // String | 
let opts = {
  'timezone': "'UTC'" // String | Set timezone for datetime fields
};
apiInstance.downloadDatasetSnapshot(source, datasetId, snapshotId, opts, (error, data, response) => {
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


## getDataset

> GetDatasets200ResponseDatasetsInner getDataset(source, datasetId, opts)



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

let apiInstance = new Opendatasoft.DatasetApi();
let source = "'catalog'"; // String | Each source represents a different catalog of datasets you'll be able to query.  There are 2 sources available:  * catalog: the catalog of datasets on your portal * opendatasoft: Opendatasoft's repository of public datasets, also available at   [data.opendatasoft.com](https://data.opendatasoft.com/page/home/) 
let datasetId = "datasetId_example"; // String | Dataset identifier.  Can be found in the \"information\" tab of the dataset page. 
let opts = {
  'select': "select_example", // String | A select expression can be used to add, remove or change fields to return. An expression can be:   - a wildcard ('*'): return all fields   - a field name: return only this field   - an include/exclude function. Include (resp exclude) all field matching include/exclude expression. This expression can contain wildcard. For example: include(spa*) will return all fields begining with 'spa'   - a complex expression: return the result of this expression. A label can be set for this expression, in that case, field will be named with this label. For instance: 'size * 2 as bigger_size' will return a new field named bigger_size and containing the double of size field value. 
  'pretty': false, // Boolean | Activate pretty print
  'timezone': "'UTC'", // String | Set timezone for datetime fields
  'includeAppMetas': false // Boolean | Explicitely request application metas for each datasets. 
};
apiInstance.getDataset(source, datasetId, opts, (error, data, response) => {
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


## getDatasetAttachements

> GetDatasetAttachements200Response getDatasetAttachements(source, datasetId)



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

let apiInstance = new Opendatasoft.DatasetApi();
let source = "'catalog'"; // String | Each source represents a different catalog of datasets you'll be able to query.  There are 2 sources available:  * catalog: the catalog of datasets on your portal * opendatasoft: Opendatasoft's repository of public datasets, also available at   [data.opendatasoft.com](https://data.opendatasoft.com/page/home/) 
let datasetId = "datasetId_example"; // String | Dataset identifier.  Can be found in the \"information\" tab of the dataset page. 
apiInstance.getDatasetAttachements(source, datasetId, (error, data, response) => {
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


## getDatasetFile

> getDatasetFile(source, datasetId, fileId, opts)



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

let apiInstance = new Opendatasoft.DatasetApi();
let source = "'catalog'"; // String | Each source represents a different catalog of datasets you'll be able to query.  There are 2 sources available:  * catalog: the catalog of datasets on your portal * opendatasoft: Opendatasoft's repository of public datasets, also available at   [data.opendatasoft.com](https://data.opendatasoft.com/page/home/) 
let datasetId = "datasetId_example"; // String | Dataset identifier.  Can be found in the \"information\" tab of the dataset page. 
let fileId = "fileId_example"; // String | 
let opts = {
  'thumbnailSize': "thumbnailSize_example" // String | Set the size of the thumbnail representing the resource (attachment, image or file)
};
apiInstance.getDatasetFile(source, datasetId, fileId, opts, (error, data, response) => {
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


## getDatasetReuse

> GetDatasetReuse200Response getDatasetReuse(source, datasetId, reuseId, opts)



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

let apiInstance = new Opendatasoft.DatasetApi();
let source = "'catalog'"; // String | Each source represents a different catalog of datasets you'll be able to query.  There are 2 sources available:  * catalog: the catalog of datasets on your portal * opendatasoft: Opendatasoft's repository of public datasets, also available at   [data.opendatasoft.com](https://data.opendatasoft.com/page/home/) 
let datasetId = "datasetId_example"; // String | Dataset identifier.  Can be found in the \"information\" tab of the dataset page. 
let reuseId = "reuseId_example"; // String | 
let opts = {
  'timezone': "'UTC'" // String | Set timezone for datetime fields
};
apiInstance.getDatasetReuse(source, datasetId, reuseId, opts, (error, data, response) => {
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


## getDatasetReuses

> GetDatasetReuses200Response getDatasetReuses(source, datasetId, opts)



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

let apiInstance = new Opendatasoft.DatasetApi();
let source = "'catalog'"; // String | Each source represents a different catalog of datasets you'll be able to query.  There are 2 sources available:  * catalog: the catalog of datasets on your portal * opendatasoft: Opendatasoft's repository of public datasets, also available at   [data.opendatasoft.com](https://data.opendatasoft.com/page/home/) 
let datasetId = "datasetId_example"; // String | Dataset identifier.  Can be found in the \"information\" tab of the dataset page. 
let opts = {
  'limit': 10, // Number | Number of items to return.  To use in conjonction with offset to implement pagination.  Limit maximum value is 100. To retrive more data use export entry points. The default value is 10. 
  'offset': 0, // Number | Index of the first item to return (starting at 0).  To use in conjonction with limit to implement pagination. 
  'timezone': "'UTC'" // String | Set timezone for datetime fields
};
apiInstance.getDatasetReuses(source, datasetId, opts, (error, data, response) => {
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


## getDatasetSnapshots

> GetDatasetSnapshots200Response getDatasetSnapshots(source, datasetId, opts)



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

let apiInstance = new Opendatasoft.DatasetApi();
let source = "'catalog'"; // String | Each source represents a different catalog of datasets you'll be able to query.  There are 2 sources available:  * catalog: the catalog of datasets on your portal * opendatasoft: Opendatasoft's repository of public datasets, also available at   [data.opendatasoft.com](https://data.opendatasoft.com/page/home/) 
let datasetId = "datasetId_example"; // String | Dataset identifier.  Can be found in the \"information\" tab of the dataset page. 
let opts = {
  'timezone': "'UTC'" // String | Set timezone for datetime fields
};
apiInstance.getDatasetSnapshots(source, datasetId, opts, (error, data, response) => {
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


## getRecord

> GetRecords200ResponseRecordsInner getRecord(source, datasetId, recordId, opts)



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

let apiInstance = new Opendatasoft.DatasetApi();
let source = "'catalog'"; // String | Each source represents a different catalog of datasets you'll be able to query.  There are 2 sources available:  * catalog: the catalog of datasets on your portal * opendatasoft: Opendatasoft's repository of public datasets, also available at   [data.opendatasoft.com](https://data.opendatasoft.com/page/home/) 
let datasetId = "datasetId_example"; // String | Dataset identifier.  Can be found in the \"information\" tab of the dataset page. 
let recordId = "recordId_example"; // String | 
let opts = {
  'select': "select_example", // String | A select expression can be used to add, remove or change fields to return. An expression can be:   - a wildcard ('*'): return all fields   - a field name: return only this field   - an include/exclude function. Include (resp exclude) all field matching include/exclude expression. This expression can contain wildcard. For example: include(spa*) will return all fields begining with 'spa'   - a complex expression: return the result of this expression. A label can be set for this expression, in that case, field will be named with this label. For instance: 'size * 2 as bigger_size' will return a new field named bigger_size and containing the double of size field value. 
  'pretty': false, // Boolean | Activate pretty print
  'timezone': "'UTC'" // String | Set timezone for datetime fields
};
apiInstance.getRecord(source, datasetId, recordId, opts, (error, data, response) => {
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


## getRecords

> GetRecords200Response getRecords(source, datasetId, opts)



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

let apiInstance = new Opendatasoft.DatasetApi();
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
apiInstance.getRecords(source, datasetId, opts, (error, data, response) => {
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


## getRecordsFacets

> GetRecordsFacets200Response getRecordsFacets(source, datasetId, opts)



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

let apiInstance = new Opendatasoft.DatasetApi();
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
apiInstance.getRecordsFacets(source, datasetId, opts, (error, data, response) => {
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


## sendDatasetFeedback

> sendDatasetFeedback(source, datasetId, feedback)



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

let apiInstance = new Opendatasoft.DatasetApi();
let source = "'catalog'"; // String | Each source represents a different catalog of datasets you'll be able to query.  There are 2 sources available:  * catalog: the catalog of datasets on your portal * opendatasoft: Opendatasoft's repository of public datasets, also available at   [data.opendatasoft.com](https://data.opendatasoft.com/page/home/) 
let datasetId = "datasetId_example"; // String | Dataset identifier.  Can be found in the \"information\" tab of the dataset page. 
let feedback = new Opendatasoft.SendDatasetFeedbackRequest(); // SendDatasetFeedbackRequest | Feedback entry
apiInstance.sendDatasetFeedback(source, datasetId, feedback, (error, data, response) => {
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

