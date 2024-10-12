# AzureAppConfiguration.RevisionsApi

All URIs are relative to *https://azure.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**checkRevisions**](RevisionsApi.md#checkRevisions) | **HEAD** /revisions | Requests the headers and status of the given resource.
[**getRevisions**](RevisionsApi.md#getRevisions) | **GET** /revisions | Gets a list of key-value revisions.



## checkRevisions

> checkRevisions(apiVersion, opts)

Requests the headers and status of the given resource.

### Example

```javascript
import AzureAppConfiguration from 'azure_app_configuration';

let apiInstance = new AzureAppConfiguration.RevisionsApi();
let apiVersion = "apiVersion_example"; // String | The API version to be used with the HTTP request.
let opts = {
  'key': "key_example", // String | A filter used to match keys.
  'label': "label_example", // String | A filter used to match labels
  'syncToken': "syncToken_example", // String | Used to guarantee real-time consistency between requests.
  'after': "after_example", // String | Instructs the server to return elements that appear after the element referred to by the specified token.
  'acceptDatetime': "acceptDatetime_example", // String | Requests the server to respond with the state of the resource at the specified time.
  'select': ["null"] // [String] | Used to select what fields are present in the returned resource(s).
};
apiInstance.checkRevisions(apiVersion, opts, (error, data, response) => {
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
 **apiVersion** | **String**| The API version to be used with the HTTP request. | 
 **key** | **String**| A filter used to match keys. | [optional] 
 **label** | **String**| A filter used to match labels | [optional] 
 **syncToken** | **String**| Used to guarantee real-time consistency between requests. | [optional] 
 **after** | **String**| Instructs the server to return elements that appear after the element referred to by the specified token. | [optional] 
 **acceptDatetime** | **String**| Requests the server to respond with the state of the resource at the specified time. | [optional] 
 **select** | [**[String]**](String.md)| Used to select what fields are present in the returned resource(s). | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getRevisions

> KeyValueListResult getRevisions(apiVersion, opts)

Gets a list of key-value revisions.

### Example

```javascript
import AzureAppConfiguration from 'azure_app_configuration';

let apiInstance = new AzureAppConfiguration.RevisionsApi();
let apiVersion = "apiVersion_example"; // String | The API version to be used with the HTTP request.
let opts = {
  'key': "key_example", // String | A filter used to match keys.
  'label': "label_example", // String | A filter used to match labels
  'syncToken': "syncToken_example", // String | Used to guarantee real-time consistency between requests.
  'after': "after_example", // String | Instructs the server to return elements that appear after the element referred to by the specified token.
  'acceptDatetime': "acceptDatetime_example", // String | Requests the server to respond with the state of the resource at the specified time.
  'select': ["null"] // [String] | Used to select what fields are present in the returned resource(s).
};
apiInstance.getRevisions(apiVersion, opts, (error, data, response) => {
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
 **apiVersion** | **String**| The API version to be used with the HTTP request. | 
 **key** | **String**| A filter used to match keys. | [optional] 
 **label** | **String**| A filter used to match labels | [optional] 
 **syncToken** | **String**| Used to guarantee real-time consistency between requests. | [optional] 
 **after** | **String**| Instructs the server to return elements that appear after the element referred to by the specified token. | [optional] 
 **acceptDatetime** | **String**| Requests the server to respond with the state of the resource at the specified time. | [optional] 
 **select** | [**[String]**](String.md)| Used to select what fields are present in the returned resource(s). | [optional] 

### Return type

[**KeyValueListResult**](KeyValueListResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.microsoft.appconfig.kvset+json, application/json, application/problem+json

