# AppStoreConnectApi.AppPriceTiersApi

All URIs are relative to *https://api.appstoreconnect.apple.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**appPriceTiersGetCollection**](AppPriceTiersApi.md#appPriceTiersGetCollection) | **GET** /v1/appPriceTiers | 
[**appPriceTiersGetInstance**](AppPriceTiersApi.md#appPriceTiersGetInstance) | **GET** /v1/appPriceTiers/{id} | 
[**appPriceTiersPricePointsGetToManyRelated**](AppPriceTiersApi.md#appPriceTiersPricePointsGetToManyRelated) | **GET** /v1/appPriceTiers/{id}/pricePoints | 



## appPriceTiersGetCollection

> AppPriceTiersResponse appPriceTiersGetCollection(opts)



### Example

```javascript
import AppStoreConnectApi from 'app_store_connect_api';
let defaultClient = AppStoreConnectApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: itc-bearer-token
let itc-bearer-token = defaultClient.authentications['itc-bearer-token'];
itc-bearer-token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new AppStoreConnectApi.AppPriceTiersApi();
let opts = {
  'filterId': ["null"], // [String] | filter by id(s)
  'fieldsAppPriceTiers': ["null"], // [String] | the fields to include for returned resources of type appPriceTiers
  'limit': 56, // Number | maximum resources per page
  'include': ["null"], // [String] | comma-separated list of relationships to include
  'fieldsAppPricePoints': ["null"], // [String] | the fields to include for returned resources of type appPricePoints
  'limitPricePoints': 56 // Number | maximum number of related pricePoints returned (when they are included)
};
apiInstance.appPriceTiersGetCollection(opts, (error, data, response) => {
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
 **filterId** | [**[String]**](String.md)| filter by id(s) | [optional] 
 **fieldsAppPriceTiers** | [**[String]**](String.md)| the fields to include for returned resources of type appPriceTiers | [optional] 
 **limit** | **Number**| maximum resources per page | [optional] 
 **include** | [**[String]**](String.md)| comma-separated list of relationships to include | [optional] 
 **fieldsAppPricePoints** | [**[String]**](String.md)| the fields to include for returned resources of type appPricePoints | [optional] 
 **limitPricePoints** | **Number**| maximum number of related pricePoints returned (when they are included) | [optional] 

### Return type

[**AppPriceTiersResponse**](AppPriceTiersResponse.md)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## appPriceTiersGetInstance

> AppPriceTierResponse appPriceTiersGetInstance(id, opts)



### Example

```javascript
import AppStoreConnectApi from 'app_store_connect_api';
let defaultClient = AppStoreConnectApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: itc-bearer-token
let itc-bearer-token = defaultClient.authentications['itc-bearer-token'];
itc-bearer-token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new AppStoreConnectApi.AppPriceTiersApi();
let id = "id_example"; // String | the id of the requested resource
let opts = {
  'fieldsAppPriceTiers': ["null"], // [String] | the fields to include for returned resources of type appPriceTiers
  'include': ["null"], // [String] | comma-separated list of relationships to include
  'fieldsAppPricePoints': ["null"], // [String] | the fields to include for returned resources of type appPricePoints
  'limitPricePoints': 56 // Number | maximum number of related pricePoints returned (when they are included)
};
apiInstance.appPriceTiersGetInstance(id, opts, (error, data, response) => {
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
 **fieldsAppPriceTiers** | [**[String]**](String.md)| the fields to include for returned resources of type appPriceTiers | [optional] 
 **include** | [**[String]**](String.md)| comma-separated list of relationships to include | [optional] 
 **fieldsAppPricePoints** | [**[String]**](String.md)| the fields to include for returned resources of type appPricePoints | [optional] 
 **limitPricePoints** | **Number**| maximum number of related pricePoints returned (when they are included) | [optional] 

### Return type

[**AppPriceTierResponse**](AppPriceTierResponse.md)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## appPriceTiersPricePointsGetToManyRelated

> AppPricePointsResponse appPriceTiersPricePointsGetToManyRelated(id, opts)



### Example

```javascript
import AppStoreConnectApi from 'app_store_connect_api';
let defaultClient = AppStoreConnectApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: itc-bearer-token
let itc-bearer-token = defaultClient.authentications['itc-bearer-token'];
itc-bearer-token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new AppStoreConnectApi.AppPriceTiersApi();
let id = "id_example"; // String | the id of the requested resource
let opts = {
  'fieldsAppPricePoints': ["null"], // [String] | the fields to include for returned resources of type appPricePoints
  'limit': 56 // Number | maximum resources per page
};
apiInstance.appPriceTiersPricePointsGetToManyRelated(id, opts, (error, data, response) => {
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
 **fieldsAppPricePoints** | [**[String]**](String.md)| the fields to include for returned resources of type appPricePoints | [optional] 
 **limit** | **Number**| maximum resources per page | [optional] 

### Return type

[**AppPricePointsResponse**](AppPricePointsResponse.md)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

