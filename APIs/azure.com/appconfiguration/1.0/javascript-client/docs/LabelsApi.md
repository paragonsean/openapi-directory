# AzureAppConfiguration.LabelsApi

All URIs are relative to *https://azure.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**checkLabels**](LabelsApi.md#checkLabels) | **HEAD** /labels | Requests the headers and status of the given resource.
[**getLabels**](LabelsApi.md#getLabels) | **GET** /labels | Gets a list of labels.



## checkLabels

> checkLabels(apiVersion, opts)

Requests the headers and status of the given resource.

### Example

```javascript
import AzureAppConfiguration from 'azure_app_configuration';

let apiInstance = new AzureAppConfiguration.LabelsApi();
let apiVersion = "apiVersion_example"; // String | The API version to be used with the HTTP request.
let opts = {
  'name': "name_example", // String | A filter for the name of the returned labels.
  'syncToken': "syncToken_example", // String | Used to guarantee real-time consistency between requests.
  'after': "after_example", // String | Instructs the server to return elements that appear after the element referred to by the specified token.
  'acceptDatetime': "acceptDatetime_example", // String | Requests the server to respond with the state of the resource at the specified time.
  'select': ["null"] // [String] | Used to select what fields are present in the returned resource(s).
};
apiInstance.checkLabels(apiVersion, opts, (error, data, response) => {
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
 **name** | **String**| A filter for the name of the returned labels. | [optional] 
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


## getLabels

> LabelListResult getLabels(apiVersion, opts)

Gets a list of labels.

### Example

```javascript
import AzureAppConfiguration from 'azure_app_configuration';

let apiInstance = new AzureAppConfiguration.LabelsApi();
let apiVersion = "apiVersion_example"; // String | The API version to be used with the HTTP request.
let opts = {
  'name': "name_example", // String | A filter for the name of the returned labels.
  'syncToken': "syncToken_example", // String | Used to guarantee real-time consistency between requests.
  'after': "after_example", // String | Instructs the server to return elements that appear after the element referred to by the specified token.
  'acceptDatetime': "acceptDatetime_example", // String | Requests the server to respond with the state of the resource at the specified time.
  'select': ["null"] // [String] | Used to select what fields are present in the returned resource(s).
};
apiInstance.getLabels(apiVersion, opts, (error, data, response) => {
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
 **name** | **String**| A filter for the name of the returned labels. | [optional] 
 **syncToken** | **String**| Used to guarantee real-time consistency between requests. | [optional] 
 **after** | **String**| Instructs the server to return elements that appear after the element referred to by the specified token. | [optional] 
 **acceptDatetime** | **String**| Requests the server to respond with the state of the resource at the specified time. | [optional] 
 **select** | [**[String]**](String.md)| Used to select what fields are present in the returned resource(s). | [optional] 

### Return type

[**LabelListResult**](LabelListResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.microsoft.appconfig.labelset+json, application/json, application/problem+json

