# AppStoreConnectApi.AppPricePointsApi

All URIs are relative to *https://api.appstoreconnect.apple.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**appPricePointsGetCollection**](AppPricePointsApi.md#appPricePointsGetCollection) | **GET** /v1/appPricePoints | 
[**appPricePointsGetInstance**](AppPricePointsApi.md#appPricePointsGetInstance) | **GET** /v1/appPricePoints/{id} | 
[**appPricePointsTerritoryGetToOneRelated**](AppPricePointsApi.md#appPricePointsTerritoryGetToOneRelated) | **GET** /v1/appPricePoints/{id}/territory | 



## appPricePointsGetCollection

> AppPricePointsResponse appPricePointsGetCollection(opts)



### Example

```javascript
import AppStoreConnectApi from 'app_store_connect_api';
let defaultClient = AppStoreConnectApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: itc-bearer-token
let itc-bearer-token = defaultClient.authentications['itc-bearer-token'];
itc-bearer-token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new AppStoreConnectApi.AppPricePointsApi();
let opts = {
  'filterPriceTier': ["null"], // [String] | filter by id(s) of related 'priceTier'
  'filterTerritory': ["null"], // [String] | filter by id(s) of related 'territory'
  'fieldsAppPricePoints': ["null"], // [String] | the fields to include for returned resources of type appPricePoints
  'limit': 56, // Number | maximum resources per page
  'include': ["null"], // [String] | comma-separated list of relationships to include
  'fieldsTerritories': ["null"] // [String] | the fields to include for returned resources of type territories
};
apiInstance.appPricePointsGetCollection(opts, (error, data, response) => {
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
 **filterPriceTier** | [**[String]**](String.md)| filter by id(s) of related &#39;priceTier&#39; | [optional] 
 **filterTerritory** | [**[String]**](String.md)| filter by id(s) of related &#39;territory&#39; | [optional] 
 **fieldsAppPricePoints** | [**[String]**](String.md)| the fields to include for returned resources of type appPricePoints | [optional] 
 **limit** | **Number**| maximum resources per page | [optional] 
 **include** | [**[String]**](String.md)| comma-separated list of relationships to include | [optional] 
 **fieldsTerritories** | [**[String]**](String.md)| the fields to include for returned resources of type territories | [optional] 

### Return type

[**AppPricePointsResponse**](AppPricePointsResponse.md)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## appPricePointsGetInstance

> AppPricePointResponse appPricePointsGetInstance(id, opts)



### Example

```javascript
import AppStoreConnectApi from 'app_store_connect_api';
let defaultClient = AppStoreConnectApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: itc-bearer-token
let itc-bearer-token = defaultClient.authentications['itc-bearer-token'];
itc-bearer-token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new AppStoreConnectApi.AppPricePointsApi();
let id = "id_example"; // String | the id of the requested resource
let opts = {
  'fieldsAppPricePoints': ["null"], // [String] | the fields to include for returned resources of type appPricePoints
  'include': ["null"], // [String] | comma-separated list of relationships to include
  'fieldsTerritories': ["null"] // [String] | the fields to include for returned resources of type territories
};
apiInstance.appPricePointsGetInstance(id, opts, (error, data, response) => {
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
 **include** | [**[String]**](String.md)| comma-separated list of relationships to include | [optional] 
 **fieldsTerritories** | [**[String]**](String.md)| the fields to include for returned resources of type territories | [optional] 

### Return type

[**AppPricePointResponse**](AppPricePointResponse.md)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## appPricePointsTerritoryGetToOneRelated

> TerritoryResponse appPricePointsTerritoryGetToOneRelated(id, opts)



### Example

```javascript
import AppStoreConnectApi from 'app_store_connect_api';
let defaultClient = AppStoreConnectApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: itc-bearer-token
let itc-bearer-token = defaultClient.authentications['itc-bearer-token'];
itc-bearer-token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new AppStoreConnectApi.AppPricePointsApi();
let id = "id_example"; // String | the id of the requested resource
let opts = {
  'fieldsTerritories': ["null"] // [String] | the fields to include for returned resources of type territories
};
apiInstance.appPricePointsTerritoryGetToOneRelated(id, opts, (error, data, response) => {
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
 **fieldsTerritories** | [**[String]**](String.md)| the fields to include for returned resources of type territories | [optional] 

### Return type

[**TerritoryResponse**](TerritoryResponse.md)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

