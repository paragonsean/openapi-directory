# RubrikRestApi.ExclusionPatternApi

All URIs are relative to */api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bulkCreateExclusionPattern**](ExclusionPatternApi.md#bulkCreateExclusionPattern) | **POST** /exclusion_pattern/bulk | Bulk create exclusion patterns
[**bulkDeleteExclusionPattern**](ExclusionPatternApi.md#bulkDeleteExclusionPattern) | **DELETE** /exclusion_pattern/bulk | Bulk delete the provided mutable exclusion patterns
[**createExclusionPattern**](ExclusionPatternApi.md#createExclusionPattern) | **POST** /exclusion_pattern | Create an exclusion pattern
[**deleteExclusionPattern**](ExclusionPatternApi.md#deleteExclusionPattern) | **DELETE** /exclusion_pattern/{id} | Delete a mutable exclusion pattern
[**getExclusionPattern**](ExclusionPatternApi.md#getExclusionPattern) | **GET** /exclusion_pattern/{id} | Get details of a exclusion pattern
[**queryExclusionPattern**](ExclusionPatternApi.md#queryExclusionPattern) | **GET** /exclusion_pattern | Get a summary of all exclusion patterns
[**updateExclusionPattern**](ExclusionPatternApi.md#updateExclusionPattern) | **POST** /exclusion_pattern/{id} | Update a mutable exclusion pattern



## bulkCreateExclusionPattern

> ExclusionPatternDetailList bulkCreateExclusionPattern(exclusionPatternCreateConfig)

Bulk create exclusion patterns

Bulk create exclusion patterns.

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.ExclusionPatternApi();
let exclusionPatternCreateConfig = [new RubrikRestApi.ExclusionPatternCreateConfig()]; // [ExclusionPatternCreateConfig] | Create configuration parameters for a exclusion pattern.
apiInstance.bulkCreateExclusionPattern(exclusionPatternCreateConfig, (error, data, response) => {
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
 **exclusionPatternCreateConfig** | [**[ExclusionPatternCreateConfig]**](ExclusionPatternCreateConfig.md)| Create configuration parameters for a exclusion pattern. | 

### Return type

[**ExclusionPatternDetailList**](ExclusionPatternDetailList.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## bulkDeleteExclusionPattern

> bulkDeleteExclusionPattern(ids)

Bulk delete the provided mutable exclusion patterns

Bulk deletes the mutable patterns in a specified set of exclusion patterns.

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.ExclusionPatternApi();
let ids = ["null"]; // [String] | The ID of each exclusion pattern to delete.
apiInstance.bulkDeleteExclusionPattern(ids, (error, data, response) => {
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
 **ids** | [**[String]**](String.md)| The ID of each exclusion pattern to delete. | 

### Return type

null (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## createExclusionPattern

> ExclusionPatternDetail createExclusionPattern(exclusionPatternCreateConfig)

Create an exclusion pattern

Create a exclusion pattern.

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.ExclusionPatternApi();
let exclusionPatternCreateConfig = new RubrikRestApi.ExclusionPatternCreateConfig(); // ExclusionPatternCreateConfig | Create configuration parameters for a exclusion pattern.
apiInstance.createExclusionPattern(exclusionPatternCreateConfig, (error, data, response) => {
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
 **exclusionPatternCreateConfig** | [**ExclusionPatternCreateConfig**](ExclusionPatternCreateConfig.md)| Create configuration parameters for a exclusion pattern. | 

### Return type

[**ExclusionPatternDetail**](ExclusionPatternDetail.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteExclusionPattern

> deleteExclusionPattern(id)

Delete a mutable exclusion pattern

Deletes an exclusion pattern if that pattern is mutable.

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.ExclusionPatternApi();
let id = "id_example"; // String | ID of the exclusion pattern.
apiInstance.deleteExclusionPattern(id, (error, data, response) => {
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
 **id** | **String**| ID of the exclusion pattern. | 

### Return type

null (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getExclusionPattern

> ExclusionPatternDetail getExclusionPattern(id)

Get details of a exclusion pattern

Get details of a exclusion pattern.

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.ExclusionPatternApi();
let id = "id_example"; // String | ID of the exclusion pattern.
apiInstance.getExclusionPattern(id, (error, data, response) => {
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
 **id** | **String**| ID of the exclusion pattern. | 

### Return type

[**ExclusionPatternDetail**](ExclusionPatternDetail.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## queryExclusionPattern

> ExclusionPatternDetailListResponse queryExclusionPattern(opts)

Get a summary of all exclusion patterns

Get a summary of all exclusion patterns.

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.ExclusionPatternApi();
let opts = {
  'pattern': "pattern_example", // String | Filter a response by making an infix comparison of the exclusion patttern in the response with the specified value.
  'isMutable': true, // Boolean | Filter a response based on the mutability of the pattern.
  'sourceId': "sourceId_example", // String | Filter a response based on the protectable object to which the exclusion pattern applies.
  'primaryClusterId': "primaryClusterId_example", // String | Limit a response to the results that have the specified primary cluster value.
  'limit': 56, // Number | Limit the summary information to a specified maximum number of matches. Optionally, use with offset to start the count at a specified point. Optionally, use with sort_by to perform sort on given attributes. Include sort_order to determine the ascending or descending direction of the sort.
  'offset': 56, // Number | Starting position in the list of matches. The response includes the specified numbered entry and all higher numbered entries. Use with limit to retrieve the response as smaller groups of entries, for example for paging of results.
  'sortBy': "sortBy_example", // String | Specifies a comma-separated list of attributes to use in sorting the matches. Performs an ASCII sort of the values in the response using each specified attribute, in the order specified.
  'sortOrder': "'asc'" // String | Sort order, either ascending or descending.
};
apiInstance.queryExclusionPattern(opts, (error, data, response) => {
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
 **pattern** | **String**| Filter a response by making an infix comparison of the exclusion patttern in the response with the specified value. | [optional] 
 **isMutable** | **Boolean**| Filter a response based on the mutability of the pattern. | [optional] 
 **sourceId** | **String**| Filter a response based on the protectable object to which the exclusion pattern applies. | [optional] 
 **primaryClusterId** | **String**| Limit a response to the results that have the specified primary cluster value. | [optional] 
 **limit** | **Number**| Limit the summary information to a specified maximum number of matches. Optionally, use with offset to start the count at a specified point. Optionally, use with sort_by to perform sort on given attributes. Include sort_order to determine the ascending or descending direction of the sort. | [optional] 
 **offset** | **Number**| Starting position in the list of matches. The response includes the specified numbered entry and all higher numbered entries. Use with limit to retrieve the response as smaller groups of entries, for example for paging of results. | [optional] 
 **sortBy** | **String**| Specifies a comma-separated list of attributes to use in sorting the matches. Performs an ASCII sort of the values in the response using each specified attribute, in the order specified. | [optional] 
 **sortOrder** | **String**| Sort order, either ascending or descending. | [optional] [default to &#39;asc&#39;]

### Return type

[**ExclusionPatternDetailListResponse**](ExclusionPatternDetailListResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateExclusionPattern

> ExclusionPatternDetail updateExclusionPattern(id, exclusionPatternUpdateConfig)

Update a mutable exclusion pattern

Update mutable exclusion pattern with specified properties. The exclusion pattern which is mutable can be modified.

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.ExclusionPatternApi();
let id = "id_example"; // String | ID of exclusion pattern.
let exclusionPatternUpdateConfig = new RubrikRestApi.ExclusionPatternUpdateConfig(); // ExclusionPatternUpdateConfig | Properties to update.
apiInstance.updateExclusionPattern(id, exclusionPatternUpdateConfig, (error, data, response) => {
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
 **id** | **String**| ID of exclusion pattern. | 
 **exclusionPatternUpdateConfig** | [**ExclusionPatternUpdateConfig**](ExclusionPatternUpdateConfig.md)| Properties to update. | 

### Return type

[**ExclusionPatternDetail**](ExclusionPatternDetail.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

