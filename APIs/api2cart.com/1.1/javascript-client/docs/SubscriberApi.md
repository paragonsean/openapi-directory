# SwaggerApi2Cart.SubscriberApi

All URIs are relative to *https://api.api2cart.com/v1.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**subscriberList**](SubscriberApi.md#subscriberList) | **GET** /subscriber.list.json | 



## subscriberList

> SubscriberList200Response subscriberList(opts)



Get subscribers list

### Example

```javascript
import SwaggerApi2Cart from 'swagger_api2_cart';
let defaultClient = SwaggerApi2Cart.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: store_key
let store_key = defaultClient.authentications['store_key'];
store_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//store_key.apiKeyPrefix = 'Token';

let apiInstance = new SwaggerApi2Cart.SubscriberApi();
let opts = {
  'start': 0, // Number | This parameter sets the number from which you want to get entities
  'count': 10, // Number | This parameter sets the entity amount that has to be retrieved. Max allowed count=250
  'subscribed': true, // Boolean | Filter by subscription status
  'storeId': "storeId_example", // String | Store Id
  'email': "email_example", // String | Filter subscribers by email
  'params': "'force_all'", // String | Set this parameter in order to choose which entity fields you want to retrieve
  'exclude': "exclude_example", // String | Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter `params` equal force_all
  'createdFrom': "createdFrom_example", // String | Retrieve entities from their creation date
  'createdTo': "createdTo_example", // String | Retrieve entities to their creation date
  'modifiedFrom': "modifiedFrom_example", // String | Retrieve entities from their modification date
  'modifiedTo': "modifiedTo_example", // String | Retrieve entities to their modification date
  'pageCursor': "pageCursor_example", // String | Used to retrieve entities via cursor-based pagination (it can't be used with any other filtering parameter)
  'responseFields': "responseFields_example" // String | Set this parameter in order to choose which entity fields you want to retrieve
};
apiInstance.subscriberList(opts, (error, data, response) => {
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
 **start** | **Number**| This parameter sets the number from which you want to get entities | [optional] [default to 0]
 **count** | **Number**| This parameter sets the entity amount that has to be retrieved. Max allowed count&#x3D;250 | [optional] [default to 10]
 **subscribed** | **Boolean**| Filter by subscription status | [optional] 
 **storeId** | **String**| Store Id | [optional] 
 **email** | **String**| Filter subscribers by email | [optional] 
 **params** | **String**| Set this parameter in order to choose which entity fields you want to retrieve | [optional] [default to &#39;force_all&#39;]
 **exclude** | **String**| Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter &#x60;params&#x60; equal force_all | [optional] 
 **createdFrom** | **String**| Retrieve entities from their creation date | [optional] 
 **createdTo** | **String**| Retrieve entities to their creation date | [optional] 
 **modifiedFrom** | **String**| Retrieve entities from their modification date | [optional] 
 **modifiedTo** | **String**| Retrieve entities to their modification date | [optional] 
 **pageCursor** | **String**| Used to retrieve entities via cursor-based pagination (it can&#39;t be used with any other filtering parameter) | [optional] 
 **responseFields** | **String**| Set this parameter in order to choose which entity fields you want to retrieve | [optional] 

### Return type

[**SubscriberList200Response**](SubscriberList200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

