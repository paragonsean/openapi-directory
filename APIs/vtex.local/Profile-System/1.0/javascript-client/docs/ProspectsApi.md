# ProfileSystem.ProspectsApi

All URIs are relative to *https://vtex.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createProspect**](ProspectsApi.md#createProspect) | **POST** /api/storage/profile-system/prospects | Create prospect
[**deleteProspect**](ProspectsApi.md#deleteProspect) | **DELETE** /api/storage/profile-system/prospects/{prospectId} | Delete prospect
[**getProspect**](ProspectsApi.md#getProspect) | **GET** /api/storage/profile-system/prospects/{prospectId} | Get prospect
[**getUnmaskedProspect**](ProspectsApi.md#getUnmaskedProspect) | **GET** /api/storage/profile-system/prospects/{prospectId}/unmask | Get unmasked prospect
[**updateProspect**](ProspectsApi.md#updateProspect) | **PATCH** /api/storage/profile-system/prospects/{prospectId} | Update prospect



## createProspect

> Object createProspect(contentType, accept, opts)

Create prospect

Creates new prospect.    &gt; The &#x60;id&#x60; field returned by this request is the &#x60;prospectId&#x60; used to retrieve information on a specific prospect later.    &gt; Learn more about the [Profile System](https://developers.vtex.com/vtex-rest-api/docs/profile-system) and its other API endpoints.

### Example

```javascript
import ProfileSystem from 'profile_system';
let defaultClient = ProfileSystem.ApiClient.instance;
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

let apiInstance = new ProfileSystem.ProspectsApi();
let contentType = "application/json"; // String | Type of the content being sent.
let accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let opts = {
  'body': null // Object | 
};
apiInstance.createProspect(contentType, accept, opts, (error, data, response) => {
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
 **body** | **Object**|  | [optional] 

### Return type

**Object**

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteProspect

> deleteProspect(contentType, accept, prospectId)

Delete prospect

Deletes a prospect by &#x60;prospectId&#x60;.    &gt; Learn more about the [Profile System](https://developers.vtex.com/vtex-rest-api/docs/profile-system) and its other API endpoints.

### Example

```javascript
import ProfileSystem from 'profile_system';
let defaultClient = ProfileSystem.ApiClient.instance;
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

let apiInstance = new ProfileSystem.ProspectsApi();
let contentType = "application/json"; // String | Type of the content being sent.
let accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let prospectId = "51clk394-8534-447e-a0ca-1803p669c987"; // String | ID of the prospect as returned by the Create prospect endpoint's response, in the `id` field.
apiInstance.deleteProspect(contentType, accept, prospectId, (error, data, response) => {
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
 **contentType** | **String**| Type of the content being sent. | 
 **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | 
 **prospectId** | **String**| ID of the prospect as returned by the Create prospect endpoint&#39;s response, in the &#x60;id&#x60; field. | 

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getProspect

> [Object] getProspect(contentType, accept, prospectId)

Get prospect

Retrieves the information of a specific prospect, by its &#x60;prospectId&#x60;.    &gt; For security and privacy reasons, this request returns masked prospect data. For unmasked information, see Get unmasked prospect.    &gt; Learn more about the [Profile System](https://developers.vtex.com/vtex-rest-api/docs/profile-system) and its other API endpoints.

### Example

```javascript
import ProfileSystem from 'profile_system';
let defaultClient = ProfileSystem.ApiClient.instance;
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

let apiInstance = new ProfileSystem.ProspectsApi();
let contentType = "application/json"; // String | Type of the content being sent.
let accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let prospectId = "51clk394-8534-447e-a0ca-1803p669c987"; // String | ID of the prospect as returned by the Create prospect endpoint's response, in the `id` field.
apiInstance.getProspect(contentType, accept, prospectId, (error, data, response) => {
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
 **prospectId** | **String**| ID of the prospect as returned by the Create prospect endpoint&#39;s response, in the &#x60;id&#x60; field. | 

### Return type

**[Object]**

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getUnmaskedProspect

> [Object] getUnmaskedProspect(contentType, accept, prospectId, reason)

Get unmasked prospect

Retrieves unmasked information of a specific prospect, by its &#x60;prospectId&#x60;.    &gt; Learn more about the [Profile System](https://developers.vtex.com/vtex-rest-api/docs/profile-system) and its other API endpoints.

### Example

```javascript
import ProfileSystem from 'profile_system';
let defaultClient = ProfileSystem.ApiClient.instance;
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

let apiInstance = new ProfileSystem.ProspectsApi();
let contentType = "application/json"; // String | Type of the content being sent.
let accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let prospectId = "51clk394-8534-447e-a0ca-1803p669c987"; // String | ID of the prospect as returned by the Create prospect endpoint's response, in the `id` field.
let reason = "data-validation"; // String | Reason for requesting unmasked data.
apiInstance.getUnmaskedProspect(contentType, accept, prospectId, reason, (error, data, response) => {
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
 **prospectId** | **String**| ID of the prospect as returned by the Create prospect endpoint&#39;s response, in the &#x60;id&#x60; field. | 
 **reason** | **String**| Reason for requesting unmasked data. | 

### Return type

**[Object]**

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateProspect

> Object updateProspect(contentType, accept, prospectId, opts)

Update prospect

Updates one or more fields of an existing prospect.    &gt; Learn more about the [Profile System](https://developers.vtex.com/vtex-rest-api/docs/profile-system) and its other API endpoints.

### Example

```javascript
import ProfileSystem from 'profile_system';
let defaultClient = ProfileSystem.ApiClient.instance;
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

let apiInstance = new ProfileSystem.ProspectsApi();
let contentType = "application/json"; // String | Type of the content being sent.
let accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let prospectId = "51clk394-8534-447e-a0ca-1803p669c987"; // String | ID of the prospect as returned by the Create prospect endpoint's response, in the `id` field.
let opts = {
  'body': null // Object | 
};
apiInstance.updateProspect(contentType, accept, prospectId, opts, (error, data, response) => {
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
 **prospectId** | **String**| ID of the prospect as returned by the Create prospect endpoint&#39;s response, in the &#x60;id&#x60; field. | 
 **body** | **Object**|  | [optional] 

### Return type

**Object**

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

