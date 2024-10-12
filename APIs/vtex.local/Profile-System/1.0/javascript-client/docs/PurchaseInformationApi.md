# ProfileSystem.PurchaseInformationApi

All URIs are relative to *https://vtex.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createPurchaseInformation**](PurchaseInformationApi.md#createPurchaseInformation) | **POST** /api/storage/profile-system/profiles/{profileId}/purchase-info | Create purchase information
[**deletePurchaseInformation**](PurchaseInformationApi.md#deletePurchaseInformation) | **DELETE** /api/storage/profile-system/profiles/{profileId}/purchase-info | Delete purchase information
[**getPurchaseInformation**](PurchaseInformationApi.md#getPurchaseInformation) | **GET** /api/storage/profile-system/profiles/{profileId}/purchase-info | Get purchase information
[**getUnmaskedPurchaseInformation**](PurchaseInformationApi.md#getUnmaskedPurchaseInformation) | **GET** /api/storage/profile-system/profiles/{profileId}/purchase-info/unmask | Get unmasked purchase information
[**updatePurchaseInformation**](PurchaseInformationApi.md#updatePurchaseInformation) | **PATCH** /api/storage/profile-system/profiles/{profileId}/purchase-info | Update purchase information



## createPurchaseInformation

> Object createPurchaseInformation(contentType, accept, profileId, opts)

Create purchase information

Creates purchase information for a given client profile.    &gt; Learn more about the [Profile System](https://developers.vtex.com/vtex-rest-api/docs/profile-system) and its other API endpoints.

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

let apiInstance = new ProfileSystem.PurchaseInformationApi();
let contentType = "application/json"; // String | Type of the content being sent.
let accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let profileId = "70caf394-8534-447e-a0ca-1803c669c771"; // String | ID of the client's profile as returned by the Create profile endpoint's response, in the `id` field. It can also be an `alternativeKey` according to your custom profile schema. In this case, this request should also send the `alternativeKey` parameter.
let opts = {
  'alternativeKey': "email", // String | The `profileId` path parameter may be substituted by other profile fields in this request. When making this request, send the `alternativeKey` parameter with a value equal to the key of the field you wish to use as `profileId`.    > Currently, there are two possible values for this parameter: `email` and `document`.
  'body': null // Object | 
};
apiInstance.createPurchaseInformation(contentType, accept, profileId, opts, (error, data, response) => {
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
 **profileId** | **String**| ID of the client&#39;s profile as returned by the Create profile endpoint&#39;s response, in the &#x60;id&#x60; field. It can also be an &#x60;alternativeKey&#x60; according to your custom profile schema. In this case, this request should also send the &#x60;alternativeKey&#x60; parameter. | 
 **alternativeKey** | **String**| The &#x60;profileId&#x60; path parameter may be substituted by other profile fields in this request. When making this request, send the &#x60;alternativeKey&#x60; parameter with a value equal to the key of the field you wish to use as &#x60;profileId&#x60;.    &gt; Currently, there are two possible values for this parameter: &#x60;email&#x60; and &#x60;document&#x60;. | [optional] 
 **body** | **Object**|  | [optional] 

### Return type

**Object**

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deletePurchaseInformation

> deletePurchaseInformation(contentType, accept, profileId, opts)

Delete purchase information

Deletes purchase informaiton by &#x60;profileId&#x60;.    &gt; Learn more about the [Profile System](https://developers.vtex.com/vtex-rest-api/docs/profile-system) and its other API endpoints.

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

let apiInstance = new ProfileSystem.PurchaseInformationApi();
let contentType = "application/json"; // String | Type of the content being sent.
let accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let profileId = "70caf394-8534-447e-a0ca-1803c669c771"; // String | ID of the client's profile as returned by the Create profile endpoint's response, in the `id` field. It can also be an `alternativeKey` according to your custom profile schema. In this case, this request should also send the `alternativeKey` parameter.
let opts = {
  'alternativeKey': "email" // String | The `profileId` path parameter may be substituted by other profile fields in this request. When making this request, send the `alternativeKey` parameter with a value equal to the key of the field you wish to use as `profileId`.    > Currently, there are two possible values for this parameter: `email` and `document`.
};
apiInstance.deletePurchaseInformation(contentType, accept, profileId, opts, (error, data, response) => {
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
 **profileId** | **String**| ID of the client&#39;s profile as returned by the Create profile endpoint&#39;s response, in the &#x60;id&#x60; field. It can also be an &#x60;alternativeKey&#x60; according to your custom profile schema. In this case, this request should also send the &#x60;alternativeKey&#x60; parameter. | 
 **alternativeKey** | **String**| The &#x60;profileId&#x60; path parameter may be substituted by other profile fields in this request. When making this request, send the &#x60;alternativeKey&#x60; parameter with a value equal to the key of the field you wish to use as &#x60;profileId&#x60;.    &gt; Currently, there are two possible values for this parameter: &#x60;email&#x60; and &#x60;document&#x60;. | [optional] 

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getPurchaseInformation

> [Object] getPurchaseInformation(contentType, accept, profileId, opts)

Get purchase information

Retrieves purchase information of a given client, by its &#x60;profileId&#x60;.    &gt; For security and privacy reasons, this request returns masked data. For unmasked information, see Get unmasked purchase information.    &gt; Learn more about the [Profile System](https://developers.vtex.com/vtex-rest-api/docs/profile-system) and its other API endpoints.

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

let apiInstance = new ProfileSystem.PurchaseInformationApi();
let contentType = "application/json"; // String | Type of the content being sent.
let accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let profileId = "70caf394-8534-447e-a0ca-1803c669c771"; // String | ID of the client's profile as returned by the Create profile endpoint's response, in the `id` field. It can also be an `alternativeKey` according to your custom profile schema. In this case, this request should also send the `alternativeKey` parameter.
let opts = {
  'alternativeKey': "email" // String | The `profileId` path parameter may be substituted by other profile fields in this request. When making this request, send the `alternativeKey` parameter with a value equal to the key of the field you wish to use as `profileId`.    > Currently, there are two possible values for this parameter: `email` and `document`.
};
apiInstance.getPurchaseInformation(contentType, accept, profileId, opts, (error, data, response) => {
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
 **profileId** | **String**| ID of the client&#39;s profile as returned by the Create profile endpoint&#39;s response, in the &#x60;id&#x60; field. It can also be an &#x60;alternativeKey&#x60; according to your custom profile schema. In this case, this request should also send the &#x60;alternativeKey&#x60; parameter. | 
 **alternativeKey** | **String**| The &#x60;profileId&#x60; path parameter may be substituted by other profile fields in this request. When making this request, send the &#x60;alternativeKey&#x60; parameter with a value equal to the key of the field you wish to use as &#x60;profileId&#x60;.    &gt; Currently, there are two possible values for this parameter: &#x60;email&#x60; and &#x60;document&#x60;. | [optional] 

### Return type

**[Object]**

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getUnmaskedPurchaseInformation

> [Object] getUnmaskedPurchaseInformation(contentType, accept, profileId)

Get unmasked purchase information

Retrieves unmasked purchase information of a given client, by its &#x60;profileId&#x60;.    &gt; Learn more about the [Profile System](https://developers.vtex.com/vtex-rest-api/docs/profile-system) and its other API endpoints.

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

let apiInstance = new ProfileSystem.PurchaseInformationApi();
let contentType = "application/json"; // String | Type of the content being sent.
let accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let profileId = "70caf394-8534-447e-a0ca-1803c669c771"; // String | ID of the client's profile as returned by the Create profile endpoint's response, in the `id` field. It can also be an `alternativeKey` according to your custom profile schema. In this case, this request should also send the `alternativeKey` parameter.
apiInstance.getUnmaskedPurchaseInformation(contentType, accept, profileId, (error, data, response) => {
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
 **profileId** | **String**| ID of the client&#39;s profile as returned by the Create profile endpoint&#39;s response, in the &#x60;id&#x60; field. It can also be an &#x60;alternativeKey&#x60; according to your custom profile schema. In this case, this request should also send the &#x60;alternativeKey&#x60; parameter. | 

### Return type

**[Object]**

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updatePurchaseInformation

> Object updatePurchaseInformation(contentType, accept, profileId, opts)

Update purchase information

Updates one or more fields of existing purchase information for a given client profile.    &gt; Learn more about the [Profile System](https://developers.vtex.com/vtex-rest-api/docs/profile-system) and its other API endpoints.

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

let apiInstance = new ProfileSystem.PurchaseInformationApi();
let contentType = "application/json"; // String | Type of the content being sent.
let accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let profileId = "70caf394-8534-447e-a0ca-1803c669c771"; // String | ID of the client's profile as returned by the Create profile endpoint's response, in the `id` field. It can also be an `alternativeKey` according to your custom profile schema. In this case, this request should also send the `alternativeKey` parameter.
let opts = {
  'alternativeKey': "email", // String | The `profileId` path parameter may be substituted by other profile fields in this request. When making this request, send the `alternativeKey` parameter with a value equal to the key of the field you wish to use as `profileId`.    > Currently, there are two possible values for this parameter: `email` and `document`.
  'body': null // Object | 
};
apiInstance.updatePurchaseInformation(contentType, accept, profileId, opts, (error, data, response) => {
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
 **profileId** | **String**| ID of the client&#39;s profile as returned by the Create profile endpoint&#39;s response, in the &#x60;id&#x60; field. It can also be an &#x60;alternativeKey&#x60; according to your custom profile schema. In this case, this request should also send the &#x60;alternativeKey&#x60; parameter. | 
 **alternativeKey** | **String**| The &#x60;profileId&#x60; path parameter may be substituted by other profile fields in this request. When making this request, send the &#x60;alternativeKey&#x60; parameter with a value equal to the key of the field you wish to use as &#x60;profileId&#x60;.    &gt; Currently, there are two possible values for this parameter: &#x60;email&#x60; and &#x60;document&#x60;. | [optional] 
 **body** | **Object**|  | [optional] 

### Return type

**Object**

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

