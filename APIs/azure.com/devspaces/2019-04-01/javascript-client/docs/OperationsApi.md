# DevSpacesManagement.OperationsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**operationsList**](OperationsApi.md#operationsList) | **GET** /providers/Microsoft.DevSpaces/operations | Lists operations for the resource provider.



## operationsList

> ResourceProviderOperationList operationsList(apiVersion)

Lists operations for the resource provider.

Lists all the supported operations by the Microsoft.DevSpaces resource provider along with their description.

### Example

```javascript
import DevSpacesManagement from 'dev_spaces_management';

let apiInstance = new DevSpacesManagement.OperationsApi();
let apiVersion = "apiVersion_example"; // String | Client API version.
apiInstance.operationsList(apiVersion, (error, data, response) => {
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
 **apiVersion** | **String**| Client API version. | 

### Return type

[**ResourceProviderOperationList**](ResourceProviderOperationList.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

