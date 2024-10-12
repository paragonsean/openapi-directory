# Opendatasoft.AggregationsApi

All URIs are relative to *https://public.opendatasoft.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**aggregateDatasets_0**](AggregationsApi.md#aggregateDatasets_0) | **GET** /{source}/aggregates | 
[**aggregateRecords_0**](AggregationsApi.md#aggregateRecords_0) | **GET** /{source}/datasets/{dataset_id}/aggregates | 



## aggregateDatasets_0

> AggregateDatasets200Response aggregateDatasets_0(source, opts)



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

let apiInstance = new Opendatasoft.AggregationsApi();
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
apiInstance.aggregateDatasets_0(source, opts, (error, data, response) => {
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


## aggregateRecords_0

> AggregateDatasets200Response aggregateRecords_0(source, datasetId, opts)



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

let apiInstance = new Opendatasoft.AggregationsApi();
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
apiInstance.aggregateRecords_0(source, datasetId, opts, (error, data, response) => {
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

