# ProfileSystem.ProfilesApi

All URIs are relative to *https://vtex.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createClientProfile**](ProfilesApi.md#createClientProfile) | **POST** /api/storage/profile-system/profiles | Create client profile
[**deleteClientProfile**](ProfilesApi.md#deleteClientProfile) | **DELETE** /api/storage/profile-system/profiles/{profileId} | Delete client profile
[**getProfile**](ProfilesApi.md#getProfile) | **GET** /api/storage/profile-system/profiles/{profileId} | Get profile
[**getProfileByVersion**](ProfilesApi.md#getProfileByVersion) | **GET** /api/storage/profile-system/profiles/{profileId}/versions/{profileVersionId} | Get profile by version
[**getUnmaskedProfile**](ProfilesApi.md#getUnmaskedProfile) | **GET** /api/storage/profile-system/profiles/{profileId}/unmask | Get unmasked profile
[**getUnmaskedProfileByVersion**](ProfilesApi.md#getUnmaskedProfileByVersion) | **GET** /api/storage/profile-system/profiles/{profileId}/versions/{profileVersionId}/unmask | Get unmasked profile by version
[**updateClientProfile**](ProfilesApi.md#updateClientProfile) | **PATCH** /api/storage/profile-system/profiles/{profileId} | Updates client profile



## createClientProfile

> Object createClientProfile(contentType, accept, opts)

Create client profile

Creates new client profile.    &gt; Since your store&#39;s profile schema is customizable, the schema and examples presented below may differ from yours. Your integration must be adapted accordingly.    &gt; The &#x60;id&#x60; field returned by this request is the &#x60;profileId&#x60; used to retrieve information on a specific profile later.    &gt; Learn more about the [Profile System](https://developers.vtex.com/vtex-rest-api/docs/profile-system) and its other API endpoints.

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

let apiInstance = new ProfileSystem.ProfilesApi();
let contentType = "application/json"; // String | Type of the content being sent.
let accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let opts = {
  'ttl': 365, // Number | This parameter sets the the Time To Live (TTL), in days, of the specific document being created or updated with this request. After this period of time from the moment of the request, the document is deleted. By sending this parameter you override the TTL set for the schema.    > Currently, the available default document schemas have no TTL. This means that documents are stored indefinitely, unless a TTL is sent when creating or updating.
  'profile': new ProfileSystem.Profile() // Profile | 
};
apiInstance.createClientProfile(contentType, accept, opts, (error, data, response) => {
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
 **ttl** | **Number**| This parameter sets the the Time To Live (TTL), in days, of the specific document being created or updated with this request. After this period of time from the moment of the request, the document is deleted. By sending this parameter you override the TTL set for the schema.    &gt; Currently, the available default document schemas have no TTL. This means that documents are stored indefinitely, unless a TTL is sent when creating or updating. | [optional] 
 **profile** | [**Profile**](Profile.md)|  | [optional] 

### Return type

**Object**

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteClientProfile

> deleteClientProfile(contentType, accept, profileId)

Delete client profile

Deletes a client profile by &#x60;profileId&#x60;.    &gt; Learn more about the [Profile System](https://developers.vtex.com/vtex-rest-api/docs/profile-system) and its other API endpoints.

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

let apiInstance = new ProfileSystem.ProfilesApi();
let contentType = "application/json"; // String | Type of the content being sent.
let accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let profileId = "70caf394-8534-447e-a0ca-1803c669c771"; // String | ID of the client's profile as returned by the Create profile endpoint's response, in the `id` field. It can also be an `alternativeKey` according to your custom profile schema. In this case, this request should also send the `alternativeKey` parameter.
apiInstance.deleteClientProfile(contentType, accept, profileId, (error, data, response) => {
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

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getProfile

> [Object] getProfile(contentType, accept, profileId, opts)

Get profile

Retrieves the information of a specific client, by its &#x60;profileId&#x60;.    &gt; Since your store&#39;s profile schema is customizable, the schema and examples presented below may differ from yours. Your integration must be adapted accordingly.    &gt; For security and privacy reasons, this request returns masked profile data. For unmasked information, see Get unmasked profile.    &gt; Learn more about the [Profile System](https://developers.vtex.com/vtex-rest-api/docs/profile-system) and its other API endpoints.

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

let apiInstance = new ProfileSystem.ProfilesApi();
let contentType = "application/json"; // String | Type of the content being sent.
let accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let profileId = "70caf394-8534-447e-a0ca-1803c669c771"; // String | ID of the client's profile as returned by the Create profile endpoint's response, in the `id` field. It can also be an `alternativeKey` according to your custom profile schema. In this case, this request should also send the `alternativeKey` parameter.
let opts = {
  'alternativeKey': "email" // String | The `profileId` path parameter may be substituted by other profile fields in this request. When making this request, send the `alternativeKey` parameter with a value equal to the key of the field you wish to use as `profileId`.    > Currently, there are two possible values for this parameter: `email` and `document`.
};
apiInstance.getProfile(contentType, accept, profileId, opts, (error, data, response) => {
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


## getProfileByVersion

> [Object] getProfileByVersion(contentType, accept, profileId, profileVersionId)

Get profile by version

Retrieves the information of a specific version of a client profile.    &gt; Since your store&#39;s profile schema is customizable, the schema and examples presented below may differ from yours. Your integration must be adapted accordingly.    &gt; For security and privacy reasons, this request returns masked profile data. For unmasked information, see Get unmasked profile by version.    &gt; Learn more about the [Profile System](https://developers.vtex.com/vtex-rest-api/docs/profile-system) and its other API endpoints.

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

let apiInstance = new ProfileSystem.ProfilesApi();
let contentType = "application/json"; // String | Type of the content being sent.
let accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let profileId = "70caf394-8534-447e-a0ca-1803c669c771"; // String | ID of the client's profile as returned by the Create profile endpoint's response, in the `id` field. It can also be an `alternativeKey` according to your custom profile schema. In this case, this request should also send the `alternativeKey` parameter.
let profileVersionId = "70caf394-8534-447e-a0ca-1803c669c771"; // String | ID of the version of the client's profile as returned by endpoints that create or update profile information in the `version` field.
apiInstance.getProfileByVersion(contentType, accept, profileId, profileVersionId, (error, data, response) => {
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
 **profileVersionId** | **String**| ID of the version of the client&#39;s profile as returned by endpoints that create or update profile information in the &#x60;version&#x60; field. | 

### Return type

**[Object]**

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getUnmaskedProfile

> [Object] getUnmaskedProfile(contentType, accept, profileId, reason, opts)

Get unmasked profile

Retrieves unmasked information of a specific client, by its &#x60;profileId&#x60;.    &gt; Since your store&#39;s profile schema is customizable, the schema and examples presented below may differ from yours. Your integration must be adapted accordingly.    &gt; Learn more about the [Profile System](https://developers.vtex.com/vtex-rest-api/docs/profile-system) and its other API endpoints.

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

let apiInstance = new ProfileSystem.ProfilesApi();
let contentType = "application/json"; // String | Type of the content being sent.
let accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let profileId = "70caf394-8534-447e-a0ca-1803c669c771"; // String | ID of the client's profile as returned by the Create profile endpoint's response, in the `id` field. It can also be an `alternativeKey` according to your custom profile schema. In this case, this request should also send the `alternativeKey` parameter.
let reason = "data-validation"; // String | Reason for requesting unmasked data.
let opts = {
  'alternativeKey': "email" // String | The `profileId` path parameter may be substituted by other profile fields in this request. When making this request, send the `alternativeKey` parameter with a value equal to the key of the field you wish to use as `profileId`.    > Currently, there are two possible values for this parameter: `email` and `document`.
};
apiInstance.getUnmaskedProfile(contentType, accept, profileId, reason, opts, (error, data, response) => {
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
 **reason** | **String**| Reason for requesting unmasked data. | 
 **alternativeKey** | **String**| The &#x60;profileId&#x60; path parameter may be substituted by other profile fields in this request. When making this request, send the &#x60;alternativeKey&#x60; parameter with a value equal to the key of the field you wish to use as &#x60;profileId&#x60;.    &gt; Currently, there are two possible values for this parameter: &#x60;email&#x60; and &#x60;document&#x60;. | [optional] 

### Return type

**[Object]**

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getUnmaskedProfileByVersion

> [Object] getUnmaskedProfileByVersion(contentType, accept, profileId, profileVersionId, reason)

Get unmasked profile by version

Retrieves unmasked information of a specific version of a client profile.    &gt; Since your store&#39;s profile schema is customizable, the schema and examples presented below may differ from yours. Your integration must be adapted accordingly.    &gt; Learn more about the [Profile System](https://developers.vtex.com/vtex-rest-api/docs/profile-system) and its other API endpoints.

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

let apiInstance = new ProfileSystem.ProfilesApi();
let contentType = "application/json"; // String | Type of the content being sent.
let accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let profileId = "70caf394-8534-447e-a0ca-1803c669c771"; // String | ID of the client's profile as returned by the Create profile endpoint's response, in the `id` field. It can also be an `alternativeKey` according to your custom profile schema. In this case, this request should also send the `alternativeKey` parameter.
let profileVersionId = "70caf394-8534-447e-a0ca-1803c669c771"; // String | ID of the version of the client's profile as returned by endpoints that create or update profile information in the `version` field.
let reason = "data-validation"; // String | Reason for requesting unmasked data.
apiInstance.getUnmaskedProfileByVersion(contentType, accept, profileId, profileVersionId, reason, (error, data, response) => {
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
 **profileVersionId** | **String**| ID of the version of the client&#39;s profile as returned by endpoints that create or update profile information in the &#x60;version&#x60; field. | 
 **reason** | **String**| Reason for requesting unmasked data. | 

### Return type

**[Object]**

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateClientProfile

> Object updateClientProfile(contentType, accept, profileId, opts)

Updates client profile

Updates one or more fields of an existing client profile.    &gt; Since your store&#39;s profile schema is customizable, the schema and examples presented below may differ from yours. Your integration must be adapted accordingly.    &gt; Learn more about the [Profile System](https://developers.vtex.com/vtex-rest-api/docs/profile-system) and its other API endpoints.

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

let apiInstance = new ProfileSystem.ProfilesApi();
let contentType = "application/json"; // String | Type of the content being sent.
let accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let profileId = "70caf394-8534-447e-a0ca-1803c669c771"; // String | ID of the client's profile as returned by the Create profile endpoint's response, in the `id` field. It can also be an `alternativeKey` according to your custom profile schema. In this case, this request should also send the `alternativeKey` parameter.
let opts = {
  'alternativeKey': "email", // String | The `profileId` path parameter may be substituted by other profile fields in this request. When making this request, send the `alternativeKey` parameter with a value equal to the key of the field you wish to use as `profileId`.    > Currently, there are two possible values for this parameter: `email` and `document`.
  'ttl': 365, // Number | This parameter sets the the Time To Live (TTL), in days, of the specific document being created or updated with this request. After this period of time from the moment of the request, the document is deleted. By sending this parameter you override the TTL set for the schema.    > Currently, the available default document schemas have no TTL. This means that documents are stored indefinitely, unless a TTL is sent when creating or updating.
  'updateClientProfileRequest': new ProfileSystem.UpdateClientProfileRequest() // UpdateClientProfileRequest | 
};
apiInstance.updateClientProfile(contentType, accept, profileId, opts, (error, data, response) => {
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
 **ttl** | **Number**| This parameter sets the the Time To Live (TTL), in days, of the specific document being created or updated with this request. After this period of time from the moment of the request, the document is deleted. By sending this parameter you override the TTL set for the schema.    &gt; Currently, the available default document schemas have no TTL. This means that documents are stored indefinitely, unless a TTL is sent when creating or updating. | [optional] 
 **updateClientProfileRequest** | [**UpdateClientProfileRequest**](UpdateClientProfileRequest.md)|  | [optional] 

### Return type

**Object**

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

