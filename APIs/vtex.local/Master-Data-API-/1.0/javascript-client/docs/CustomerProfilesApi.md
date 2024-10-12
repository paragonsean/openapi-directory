# MasterDataApiV2.CustomerProfilesApi

All URIs are relative to *https://vtex.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createNewCustomerProfilev2**](CustomerProfilesApi.md#createNewCustomerProfilev2) | **POST** /api/dataentities/Client/documents | Create new customer profile
[**deleteCustomerProfile**](CustomerProfilesApi.md#deleteCustomerProfile) | **DELETE** /api/dataentities/Client/documents/{id} | Delete customer profile
[**updateCustomerProfile**](CustomerProfilesApi.md#updateCustomerProfile) | **PATCH** /api/dataentities/Client/documents/{id} | Update customer profile



## createNewCustomerProfilev2

> DocumentResponse createNewCustomerProfilev2(contentType, accept, createUpdateProfileRequests, opts)

Create new customer profile

Creates new customer profile.    &gt; You can use this request to create customer profiles according to any &#x60;CL&#x60; schema. Because of this, you are not restricted to using the fields exemplified below in your requests. But you should be aware of the fields allowed or required for the schemas you are using. Learn more about how to use [Master Data v2 schemas](https://developers.vtex.com/vtex-rest-api/docs/master-data-schema-lifecycle).

### Example

```javascript
import MasterDataApiV2 from 'master_data_api_v2';
let defaultClient = MasterDataApiV2.ApiClient.instance;
// Configure API key authorization: appToken
let appToken = defaultClient.authentications['appToken'];
appToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appToken.apiKeyPrefix = 'Token';
// Configure API key authorization: appKey
let appKey = defaultClient.authentications['appKey'];
appKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appKey.apiKeyPrefix = 'Token';

let apiInstance = new MasterDataApiV2.CustomerProfilesApi();
let contentType = "application/json"; // String | Type of the content being sent.
let accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let createUpdateProfileRequests = new MasterDataApiV2.CreateUpdateProfileRequests(); // CreateUpdateProfileRequests | 
let opts = {
  'schema': "schema" // String | Name of the schema the document to be created needs to be compliant with.
};
apiInstance.createNewCustomerProfilev2(contentType, accept, createUpdateProfileRequests, opts, (error, data, response) => {
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
 **contentType** | **String**| Type of the content being sent. | 
 **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | 
 **createUpdateProfileRequests** | [**CreateUpdateProfileRequests**](CreateUpdateProfileRequests.md)|  | 
 **schema** | **String**| Name of the schema the document to be created needs to be compliant with. | [optional] 

### Return type

[**DocumentResponse**](DocumentResponse.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteCustomerProfile

> DocumentResponse deleteCustomerProfile(contentType, accept, id)

Delete customer profile

Deletes a customer profile.

### Example

```javascript
import MasterDataApiV2 from 'master_data_api_v2';
let defaultClient = MasterDataApiV2.ApiClient.instance;
// Configure API key authorization: appToken
let appToken = defaultClient.authentications['appToken'];
appToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appToken.apiKeyPrefix = 'Token';
// Configure API key authorization: appKey
let appKey = defaultClient.authentications['appKey'];
appKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appKey.apiKeyPrefix = 'Token';

let apiInstance = new MasterDataApiV2.CustomerProfilesApi();
let contentType = "application/json"; // String | Type of the content being sent.
let accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let id = "Client-b818cbda-e489-11e6-94f4-0ac138d2d42e"; // String | ID of the Document.
apiInstance.deleteCustomerProfile(contentType, accept, id, (error, data, response) => {
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
 **contentType** | **String**| Type of the content being sent. | 
 **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | 
 **id** | **String**| ID of the Document. | 

### Return type

[**DocumentResponse**](DocumentResponse.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateCustomerProfile

> DocumentResponse updateCustomerProfile(contentType, accept, id, createUpdateProfileRequests, opts)

Update customer profile

Partially updates a customer profile.    &gt; You can use this request to update customer profiles according to any &#x60;CL&#x60; schema. Because of this, you are not restricted to using the fields exemplified below in your requests. But you should be aware of the fields allowed or required for the schemas you are using. Learn more about how to use [Master Data v2 schemas](https://developers.vtex.com/vtex-rest-api/docs/master-data-schema-lifecycle).

### Example

```javascript
import MasterDataApiV2 from 'master_data_api_v2';
let defaultClient = MasterDataApiV2.ApiClient.instance;
// Configure API key authorization: appToken
let appToken = defaultClient.authentications['appToken'];
appToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appToken.apiKeyPrefix = 'Token';
// Configure API key authorization: appKey
let appKey = defaultClient.authentications['appKey'];
appKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appKey.apiKeyPrefix = 'Token';

let apiInstance = new MasterDataApiV2.CustomerProfilesApi();
let contentType = "application/json"; // String | Type of the content being sent.
let accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let id = "Client-b818cbda-e489-11e6-94f4-0ac138d2d42e"; // String | ID of the Document.
let createUpdateProfileRequests = new MasterDataApiV2.CreateUpdateProfileRequests(); // CreateUpdateProfileRequests | 
let opts = {
  'schema': "schema" // String | Name of the schema the document to be created needs to be compliant with.
};
apiInstance.updateCustomerProfile(contentType, accept, id, createUpdateProfileRequests, opts, (error, data, response) => {
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
 **contentType** | **String**| Type of the content being sent. | 
 **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | 
 **id** | **String**| ID of the Document. | 
 **createUpdateProfileRequests** | [**CreateUpdateProfileRequests**](CreateUpdateProfileRequests.md)|  | 
 **schema** | **String**| Name of the schema the document to be created needs to be compliant with. | [optional] 

### Return type

[**DocumentResponse**](DocumentResponse.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

