# Apacta.ContactCustomFieldAttributesApi

All URIs are relative to *https://app.apacta.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**contactCustomFieldAttributesContactCustomFieldAttributeIdGet**](ContactCustomFieldAttributesApi.md#contactCustomFieldAttributesContactCustomFieldAttributeIdGet) | **GET** /contact_custom_field_attributes/{contact_custom_field_attribute_id} | Details of 1 contact custom field attribute
[**contactCustomFieldAttributesGet**](ContactCustomFieldAttributesApi.md#contactCustomFieldAttributesGet) | **GET** /contact_custom_field_attributes | Get a list of contact custom field attributes



## contactCustomFieldAttributesContactCustomFieldAttributeIdGet

> ContactCustomFieldAttributesContactCustomFieldAttributeIdGet200Response contactCustomFieldAttributesContactCustomFieldAttributeIdGet(contactCustomFieldAttributeId)

Details of 1 contact custom field attribute

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

let apiInstance = new Apacta.ContactCustomFieldAttributesApi();
let contactCustomFieldAttributeId = "contactCustomFieldAttributeId_example"; // String | 
apiInstance.contactCustomFieldAttributesContactCustomFieldAttributeIdGet(contactCustomFieldAttributeId, (error, data, response) => {
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
 **contactCustomFieldAttributeId** | **String**|  | 

### Return type

[**ContactCustomFieldAttributesContactCustomFieldAttributeIdGet200Response**](ContactCustomFieldAttributesContactCustomFieldAttributeIdGet200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## contactCustomFieldAttributesGet

> ContactCustomFieldAttributesGet200Response contactCustomFieldAttributesGet()

Get a list of contact custom field attributes

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

let apiInstance = new Apacta.ContactCustomFieldAttributesApi();
apiInstance.contactCustomFieldAttributesGet((error, data, response) => {
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

[**ContactCustomFieldAttributesGet200Response**](ContactCustomFieldAttributesGet200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

