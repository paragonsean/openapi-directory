# AzureResourceGraph.ChangesApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**resourceChangeDetails**](ChangesApi.md#resourceChangeDetails) | **POST** /providers/Microsoft.ResourceGraph/resourceChangeDetails | 
[**resourceChanges**](ChangesApi.md#resourceChanges) | **POST** /providers/Microsoft.ResourceGraph/resourceChanges | 



## resourceChangeDetails

> ResourceChangeData resourceChangeDetails(apiVersion, parameters)



Get resource change details.

### Example

```javascript
import AzureResourceGraph from 'azure_resource_graph';
let defaultClient = AzureResourceGraph.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureResourceGraph.ChangesApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let parameters = new AzureResourceGraph.ResourceChangeDetailsRequestParameters(); // ResourceChangeDetailsRequestParameters | The parameters for this request for resource change details.
apiInstance.resourceChangeDetails(apiVersion, parameters, (error, data, response) => {
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
 **apiVersion** | **String**| Client Api Version. | 
 **parameters** | [**ResourceChangeDetailsRequestParameters**](ResourceChangeDetailsRequestParameters.md)| The parameters for this request for resource change details. | 

### Return type

[**ResourceChangeData**](ResourceChangeData.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## resourceChanges

> ResourceChangeList resourceChanges(apiVersion, parameters)



List changes to a resource for a given time interval.

### Example

```javascript
import AzureResourceGraph from 'azure_resource_graph';
let defaultClient = AzureResourceGraph.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureResourceGraph.ChangesApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let parameters = new AzureResourceGraph.ResourceChangesRequestParameters(); // ResourceChangesRequestParameters | the parameters for this request for changes.
apiInstance.resourceChanges(apiVersion, parameters, (error, data, response) => {
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
 **apiVersion** | **String**| Client Api Version. | 
 **parameters** | [**ResourceChangesRequestParameters**](ResourceChangesRequestParameters.md)| the parameters for this request for changes. | 

### Return type

[**ResourceChangeList**](ResourceChangeList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

