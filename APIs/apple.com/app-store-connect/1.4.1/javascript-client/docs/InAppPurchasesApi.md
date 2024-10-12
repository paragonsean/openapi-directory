# AppStoreConnectApi.InAppPurchasesApi

All URIs are relative to *https://api.appstoreconnect.apple.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**inAppPurchasesGetInstance**](InAppPurchasesApi.md#inAppPurchasesGetInstance) | **GET** /v1/inAppPurchases/{id} | 



## inAppPurchasesGetInstance

> InAppPurchaseResponse inAppPurchasesGetInstance(id, opts)



### Example

```javascript
import AppStoreConnectApi from 'app_store_connect_api';
let defaultClient = AppStoreConnectApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: itc-bearer-token
let itc-bearer-token = defaultClient.authentications['itc-bearer-token'];
itc-bearer-token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new AppStoreConnectApi.InAppPurchasesApi();
let id = "id_example"; // String | the id of the requested resource
let opts = {
  'fieldsInAppPurchases': ["null"], // [String] | the fields to include for returned resources of type inAppPurchases
  'include': ["null"], // [String] | comma-separated list of relationships to include
  'limitApps': 56 // Number | maximum number of related apps returned (when they are included)
};
apiInstance.inAppPurchasesGetInstance(id, opts, (error, data, response) => {
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
 **id** | **String**| the id of the requested resource | 
 **fieldsInAppPurchases** | [**[String]**](String.md)| the fields to include for returned resources of type inAppPurchases | [optional] 
 **include** | [**[String]**](String.md)| comma-separated list of relationships to include | [optional] 
 **limitApps** | **Number**| maximum number of related apps returned (when they are included) | [optional] 

### Return type

[**InAppPurchaseResponse**](InAppPurchaseResponse.md)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

