# AppStoreConnectApi.AppStoreVersionSubmissionsApi

All URIs are relative to *https://api.appstoreconnect.apple.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**appStoreVersionSubmissionsCreateInstance**](AppStoreVersionSubmissionsApi.md#appStoreVersionSubmissionsCreateInstance) | **POST** /v1/appStoreVersionSubmissions | 
[**appStoreVersionSubmissionsDeleteInstance**](AppStoreVersionSubmissionsApi.md#appStoreVersionSubmissionsDeleteInstance) | **DELETE** /v1/appStoreVersionSubmissions/{id} | 



## appStoreVersionSubmissionsCreateInstance

> AppStoreVersionSubmissionResponse appStoreVersionSubmissionsCreateInstance(appStoreVersionSubmissionCreateRequest)



### Example

```javascript
import AppStoreConnectApi from 'app_store_connect_api';
let defaultClient = AppStoreConnectApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: itc-bearer-token
let itc-bearer-token = defaultClient.authentications['itc-bearer-token'];
itc-bearer-token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new AppStoreConnectApi.AppStoreVersionSubmissionsApi();
let appStoreVersionSubmissionCreateRequest = new AppStoreConnectApi.AppStoreVersionSubmissionCreateRequest(); // AppStoreVersionSubmissionCreateRequest | AppStoreVersionSubmission representation
apiInstance.appStoreVersionSubmissionsCreateInstance(appStoreVersionSubmissionCreateRequest, (error, data, response) => {
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
 **appStoreVersionSubmissionCreateRequest** | [**AppStoreVersionSubmissionCreateRequest**](AppStoreVersionSubmissionCreateRequest.md)| AppStoreVersionSubmission representation | 

### Return type

[**AppStoreVersionSubmissionResponse**](AppStoreVersionSubmissionResponse.md)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## appStoreVersionSubmissionsDeleteInstance

> appStoreVersionSubmissionsDeleteInstance(id)



### Example

```javascript
import AppStoreConnectApi from 'app_store_connect_api';
let defaultClient = AppStoreConnectApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: itc-bearer-token
let itc-bearer-token = defaultClient.authentications['itc-bearer-token'];
itc-bearer-token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new AppStoreConnectApi.AppStoreVersionSubmissionsApi();
let id = "id_example"; // String | the id of the requested resource
apiInstance.appStoreVersionSubmissionsDeleteInstance(id, (error, data, response) => {
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
 **id** | **String**| the id of the requested resource | 

### Return type

null (empty response body)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

