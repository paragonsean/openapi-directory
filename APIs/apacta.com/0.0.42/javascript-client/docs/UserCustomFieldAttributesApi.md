# Apacta.UserCustomFieldAttributesApi

All URIs are relative to *https://app.apacta.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**userCustomFieldAttributesGet**](UserCustomFieldAttributesApi.md#userCustomFieldAttributesGet) | **GET** /user_custom_field_attributes | Get a list of user custom field attributes
[**userCustomFieldAttributesUserCustomFieldAttributeIdGet**](UserCustomFieldAttributesApi.md#userCustomFieldAttributesUserCustomFieldAttributeIdGet) | **GET** /user_custom_field_attributes/{user_custom_field_attribute_id} | Details of 1 user custom field attribute



## userCustomFieldAttributesGet

> UserCustomFieldAttributesGet200Response userCustomFieldAttributesGet()

Get a list of user custom field attributes

### Example

```javascript
import Apacta from 'apacta';
let defaultClient = Apacta.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: X-Auth-Token
let X-Auth-Token = defaultClient.authentications['X-Auth-Token'];
X-Auth-Token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Auth-Token.apiKeyPrefix = 'Token';

let apiInstance = new Apacta.UserCustomFieldAttributesApi();
apiInstance.userCustomFieldAttributesGet((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**UserCustomFieldAttributesGet200Response**](UserCustomFieldAttributesGet200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## userCustomFieldAttributesUserCustomFieldAttributeIdGet

> UserCustomFieldAttributesUserCustomFieldAttributeIdGet200Response userCustomFieldAttributesUserCustomFieldAttributeIdGet(userCustomFieldAttributeId)

Details of 1 user custom field attribute

### Example

```javascript
import Apacta from 'apacta';
let defaultClient = Apacta.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: X-Auth-Token
let X-Auth-Token = defaultClient.authentications['X-Auth-Token'];
X-Auth-Token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Auth-Token.apiKeyPrefix = 'Token';

let apiInstance = new Apacta.UserCustomFieldAttributesApi();
let userCustomFieldAttributeId = "userCustomFieldAttributeId_example"; // String | 
apiInstance.userCustomFieldAttributesUserCustomFieldAttributeIdGet(userCustomFieldAttributeId, (error, data, response) => {
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
 **userCustomFieldAttributeId** | **String**|  | 

### Return type

[**UserCustomFieldAttributesUserCustomFieldAttributeIdGet200Response**](UserCustomFieldAttributesUserCustomFieldAttributeIdGet200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

