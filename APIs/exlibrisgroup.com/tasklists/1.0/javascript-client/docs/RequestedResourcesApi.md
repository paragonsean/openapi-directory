# ExLibrisApis.RequestedResourcesApi

All URIs are relative to *https://api-eu.hosted.exlibrisgroup.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getAlmawsV1TaskListsRequestedResources**](RequestedResourcesApi.md#getAlmawsV1TaskListsRequestedResources) | **GET** /almaws/v1/task-lists/requested-resources | Get Requested Resources
[**postAlmawsV1TaskListsRequestedResources**](RequestedResourcesApi.md#postAlmawsV1TaskListsRequestedResources) | **POST** /almaws/v1/task-lists/requested-resources | Act on Requested Resources



## getAlmawsV1TaskListsRequestedResources

> GetAlmawsV1TaskListsRequestedResources200Response getAlmawsV1TaskListsRequestedResources(library, circDesk, opts)

Get Requested Resources

This API returns a list of requested resources to be picked from the shelf in Alma

### Example

```javascript
import ExLibrisApis from 'ex_libris_apis';
let defaultClient = ExLibrisApis.ApiClient.instance;
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new ExLibrisApis.RequestedResourcesApi();
let library = "library_example"; // String | The library of the given circulation desk or department where the resources are located. Mandatory.
let circDesk = "circDesk_example"; // String | The circulation desk where the action is being performed. Mandatory.
let opts = {
  'location': "''", // String | The location code. Optional.
  'orderBy': "'call_number'", // String | The order in which to retrieve the results: location/call_number (default).
  'direction': "'asc'", // String | The order direction in which to retrieve the results. Optional.
  'pickupInst': "''", // String | The pickup institution. Optional.
  'reported': "''", // String | Show reported results: Y/N. Optional.
  'printed': "''", // String | Show printed results: Y/N. Optional.
  'limit': 56, // Number | Limits the number of results. Optional. Valid values are 0-100. Default value: 10.
  'offset': 56 // Number | Offset of the results returned. Optional. Default value: 0, which means that the first results will be returned.
};
apiInstance.getAlmawsV1TaskListsRequestedResources(library, circDesk, opts, (error, data, response) => {
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
 **library** | **String**| The library of the given circulation desk or department where the resources are located. Mandatory. | 
 **circDesk** | **String**| The circulation desk where the action is being performed. Mandatory. | 
 **location** | **String**| The location code. Optional. | [optional] [default to &#39;&#39;]
 **orderBy** | **String**| The order in which to retrieve the results: location/call_number (default). | [optional] [default to &#39;call_number&#39;]
 **direction** | **String**| The order direction in which to retrieve the results. Optional. | [optional] [default to &#39;asc&#39;]
 **pickupInst** | **String**| The pickup institution. Optional. | [optional] [default to &#39;&#39;]
 **reported** | **String**| Show reported results: Y/N. Optional. | [optional] [default to &#39;&#39;]
 **printed** | **String**| Show printed results: Y/N. Optional. | [optional] [default to &#39;&#39;]
 **limit** | **Number**| Limits the number of results. Optional. Valid values are 0-100. Default value: 10. | [optional] 
 **offset** | **Number**| Offset of the results returned. Optional. Default value: 0, which means that the first results will be returned. | [optional] 

### Return type

[**GetAlmawsV1TaskListsRequestedResources200Response**](GetAlmawsV1TaskListsRequestedResources200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## postAlmawsV1TaskListsRequestedResources

> Object postAlmawsV1TaskListsRequestedResources(opts)

Act on Requested Resources

This API performs an action on requested resources that are on the shelf in Alma

### Example

```javascript
import ExLibrisApis from 'ex_libris_apis';
let defaultClient = ExLibrisApis.ApiClient.instance;
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new ExLibrisApis.RequestedResourcesApi();
let opts = {
  'library': "''", // String | The library of the given circulation desk or department where the resources are located. Mandatory.
  'circDesk': "''", // String | The circulation desk where the action is being performed. Mandatory.
  'op': "''", // String | Operation to be preformed on the list of given requests. Currently the only supported action is 'mark_reported'. Mandatory.
  'location': "''", // String | The location code. Optional.
  'pickupInst': "''", // String | The pickup institution. Optional.
  'reported': "''", // String | Show reported results: Y/N. Optional.
  'printed': "''" // String | Show printed results: Y/N. Optional.
};
apiInstance.postAlmawsV1TaskListsRequestedResources(opts, (error, data, response) => {
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
 **library** | **String**| The library of the given circulation desk or department where the resources are located. Mandatory. | [optional] [default to &#39;&#39;]
 **circDesk** | **String**| The circulation desk where the action is being performed. Mandatory. | [optional] [default to &#39;&#39;]
 **op** | **String**| Operation to be preformed on the list of given requests. Currently the only supported action is &#39;mark_reported&#39;. Mandatory. | [optional] [default to &#39;&#39;]
 **location** | **String**| The location code. Optional. | [optional] [default to &#39;&#39;]
 **pickupInst** | **String**| The pickup institution. Optional. | [optional] [default to &#39;&#39;]
 **reported** | **String**| Show reported results: Y/N. Optional. | [optional] [default to &#39;&#39;]
 **printed** | **String**| Show printed results: Y/N. Optional. | [optional] [default to &#39;&#39;]

### Return type

**Object**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml

