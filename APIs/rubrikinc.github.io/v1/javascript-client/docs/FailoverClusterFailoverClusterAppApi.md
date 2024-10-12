# RubrikRestApi.FailoverClusterFailoverClusterAppApi

All URIs are relative to */api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bulkDeleteFailoverClusterApp**](FailoverClusterFailoverClusterAppApi.md#bulkDeleteFailoverClusterApp) | **DELETE** /failover_cluster/failover_cluster_app/bulk | Delete failover cluster applications
[**createFailoverClusterApp**](FailoverClusterFailoverClusterAppApi.md#createFailoverClusterApp) | **POST** /failover_cluster/failover_cluster_app | Create a failover cluster app
[**deleteFailoverClusterApp**](FailoverClusterFailoverClusterAppApi.md#deleteFailoverClusterApp) | **DELETE** /failover_cluster/failover_cluster_app/{id} | Delete a failover cluster app
[**getFailoverClusterApp**](FailoverClusterFailoverClusterAppApi.md#getFailoverClusterApp) | **GET** /failover_cluster/failover_cluster_app/{id} | Get details of a failover cluster app
[**queryFailoverClusterApp**](FailoverClusterFailoverClusterAppApi.md#queryFailoverClusterApp) | **GET** /failover_cluster/failover_cluster_app | Get a summary of all failover cluster apps
[**updateFailoverClusterApp**](FailoverClusterFailoverClusterAppApi.md#updateFailoverClusterApp) | **PATCH** /failover_cluster/failover_cluster_app/{id} | Update a failover cluster app



## bulkDeleteFailoverClusterApp

> bulkDeleteFailoverClusterApp(ids, opts)

Delete failover cluster applications

Delete failover cluster applications from Rubrik cluster.

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

let apiInstance = new RubrikRestApi.FailoverClusterFailoverClusterAppApi();
let ids = ["null"]; // [String] | The ID of each failover cluster application to delete.
let opts = {
  'preserveSnapshots': true // Boolean | Specifies whether to preserve the snapshots of the fileset that belongs to a failover cluster application. When this value is 'true,' the snapshots are preserved. The default value is 'true'.
};
apiInstance.bulkDeleteFailoverClusterApp(ids, opts, (error, data, response) => {
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
 **ids** | [**[String]**](String.md)| The ID of each failover cluster application to delete. | 
 **preserveSnapshots** | **Boolean**| Specifies whether to preserve the snapshots of the fileset that belongs to a failover cluster application. When this value is &#39;true,&#39; the snapshots are preserved. The default value is &#39;true&#39;. | [optional] 

### Return type

null (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## createFailoverClusterApp

> FailoverClusterAppSummary createFailoverClusterApp(failoverClusterAppConfig)

Create a failover cluster app

Create a failover cluster app.

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

let apiInstance = new RubrikRestApi.FailoverClusterFailoverClusterAppApi();
let failoverClusterAppConfig = new RubrikRestApi.FailoverClusterAppConfig(); // FailoverClusterAppConfig | Create configuration parameters for a failover cluster app.
apiInstance.createFailoverClusterApp(failoverClusterAppConfig, (error, data, response) => {
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
 **failoverClusterAppConfig** | [**FailoverClusterAppConfig**](FailoverClusterAppConfig.md)| Create configuration parameters for a failover cluster app. | 

### Return type

[**FailoverClusterAppSummary**](FailoverClusterAppSummary.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteFailoverClusterApp

> deleteFailoverClusterApp(id, opts)

Delete a failover cluster app

Delete a failover cluster app.

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

let apiInstance = new RubrikRestApi.FailoverClusterFailoverClusterAppApi();
let id = "id_example"; // String | ID of the failover cluster app.
let opts = {
  'preserveSnapshots': true // Boolean | A Boolean that specifies whether to preserve the snapshots of the fileset which belong to a failover cluster application. When this value is 'true,' the snapshots are preserved. The default value is 'true'.
};
apiInstance.deleteFailoverClusterApp(id, opts, (error, data, response) => {
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
 **id** | **String**| ID of the failover cluster app. | 
 **preserveSnapshots** | **Boolean**| A Boolean that specifies whether to preserve the snapshots of the fileset which belong to a failover cluster application. When this value is &#39;true,&#39; the snapshots are preserved. The default value is &#39;true&#39;. | [optional] 

### Return type

null (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getFailoverClusterApp

> FailoverClusterAppDetail getFailoverClusterApp(id)

Get details of a failover cluster app

Get details of a failover cluster app.

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

let apiInstance = new RubrikRestApi.FailoverClusterFailoverClusterAppApi();
let id = "id_example"; // String | ID of the failover cluster app.
apiInstance.getFailoverClusterApp(id, (error, data, response) => {
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
 **id** | **String**| ID of the failover cluster app. | 

### Return type

[**FailoverClusterAppDetail**](FailoverClusterAppDetail.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## queryFailoverClusterApp

> FailoverClusterAppSummaryListResponse queryFailoverClusterApp(opts)

Get a summary of all failover cluster apps

Get a summary of all failover cluster apps.

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

let apiInstance = new RubrikRestApi.FailoverClusterFailoverClusterAppApi();
let opts = {
  'name': "name_example", // String | Filter the response by comparing the failover cluster app name with the specified value.
  'slaAssignment': "slaAssignment_example", // String | Limit a response to the results that have the specified SLA Domain assignment type.
  'primaryClusterId': "primaryClusterId_example", // String | Limit a response to the results that have the specified primary cluster value.
  'operatingSystemType': "operatingSystemType_example", // String | Filter a response based on the failover cluster operating system type.
  'limit': 56, // Number | Limit the summary information to a specified maximum number of matches. Optionally, use with offset to start the count at a specified point. Optionally, use with sort_by to perform sort on given attributes. Include sort_order to determine the ascending or descending direction of the sort.
  'offset': 56, // Number | Starting position in the list of matches. The response includes the specified numbered entry and all higher numbered entries. Use with limit to retrieve the response as smaller groups of entries, for example for paging of results.
  'sortBy': "sortBy_example", // String | Specifies a comma-separated list of attributes to use in sorting the matches. Performs an ASCII sort of the values in the response using each specified attribute, in the order specified.
  'sortOrder': "'asc'" // String | Sort order, either ascending or descending.
};
apiInstance.queryFailoverClusterApp(opts, (error, data, response) => {
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
 **name** | **String**| Filter the response by comparing the failover cluster app name with the specified value. | [optional] 
 **slaAssignment** | **String**| Limit a response to the results that have the specified SLA Domain assignment type. | [optional] 
 **primaryClusterId** | **String**| Limit a response to the results that have the specified primary cluster value. | [optional] 
 **operatingSystemType** | **String**| Filter a response based on the failover cluster operating system type. | [optional] 
 **limit** | **Number**| Limit the summary information to a specified maximum number of matches. Optionally, use with offset to start the count at a specified point. Optionally, use with sort_by to perform sort on given attributes. Include sort_order to determine the ascending or descending direction of the sort. | [optional] 
 **offset** | **Number**| Starting position in the list of matches. The response includes the specified numbered entry and all higher numbered entries. Use with limit to retrieve the response as smaller groups of entries, for example for paging of results. | [optional] 
 **sortBy** | **String**| Specifies a comma-separated list of attributes to use in sorting the matches. Performs an ASCII sort of the values in the response using each specified attribute, in the order specified. | [optional] 
 **sortOrder** | **String**| Sort order, either ascending or descending. | [optional] [default to &#39;asc&#39;]

### Return type

[**FailoverClusterAppSummaryListResponse**](FailoverClusterAppSummaryListResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateFailoverClusterApp

> FailoverClusterAppSummary updateFailoverClusterApp(id, failoverClusterAppConfig)

Update a failover cluster app

Update the failover cluster app with specified properties.

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

let apiInstance = new RubrikRestApi.FailoverClusterFailoverClusterAppApi();
let id = "id_example"; // String | ID of failover cluster app.
let failoverClusterAppConfig = new RubrikRestApi.FailoverClusterAppConfig(); // FailoverClusterAppConfig | Properties to update.
apiInstance.updateFailoverClusterApp(id, failoverClusterAppConfig, (error, data, response) => {
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
 **id** | **String**| ID of failover cluster app. | 
 **failoverClusterAppConfig** | [**FailoverClusterAppConfig**](FailoverClusterAppConfig.md)| Properties to update. | 

### Return type

[**FailoverClusterAppSummary**](FailoverClusterAppSummary.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

