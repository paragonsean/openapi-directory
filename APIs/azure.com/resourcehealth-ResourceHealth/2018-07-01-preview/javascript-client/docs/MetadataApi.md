# MicrosoftResourceHealth.MetadataApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**metadataGet**](MetadataApi.md#metadataGet) | **GET** /providers/Microsoft.ResourceHealth/metadata/{name} | Gets the metadata entity.
[**metadataList**](MetadataApi.md#metadataList) | **GET** /providers/Microsoft.ResourceHealth/metadata | Gets the list of metadata entities.



## metadataGet

> MetadataEntity metadataGet(name, apiVersion)

Gets the metadata entity.

### Example

```javascript
import MicrosoftResourceHealth from 'microsoft_resource_health';
let defaultClient = MicrosoftResourceHealth.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MicrosoftResourceHealth.MetadataApi();
let name = "name_example"; // String | Name of metadata entity.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
apiInstance.metadataGet(name, apiVersion, (error, data, response) => {
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
 **name** | **String**| Name of metadata entity. | 
 **apiVersion** | **String**| Client Api Version. | 

### Return type

[**MetadataEntity**](MetadataEntity.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## metadataList

> MetadataEntityListResult metadataList(apiVersion)

Gets the list of metadata entities.

### Example

```javascript
import MicrosoftResourceHealth from 'microsoft_resource_health';
let defaultClient = MicrosoftResourceHealth.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MicrosoftResourceHealth.MetadataApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
apiInstance.metadataList(apiVersion, (error, data, response) => {
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

### Return type

[**MetadataEntityListResult**](MetadataEntityListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

