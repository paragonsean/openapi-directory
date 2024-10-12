# ProfileSystem.SchemasApi

All URIs are relative to *https://vtex.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createOrUpdateProfileSchema**](SchemasApi.md#createOrUpdateProfileSchema) | **PUT** /api/storage/profile-system/profiles/schema | Create or update profile schema



## createOrUpdateProfileSchema

> Object createOrUpdateProfileSchema(contentType, accept, opts)

Create or update profile schema

Creates or updates profile schema.    &gt; Each account has one profile schema. Updating it with this request will substitute the previous version.    &gt; Learn more about the [Profile System](https://developers.vtex.com/vtex-rest-api/docs/profile-system) and its other API endpoints.

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

let apiInstance = new ProfileSystem.SchemasApi();
let contentType = "application/json"; // String | Type of the content being sent.
let accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let opts = {
  'schema': new ProfileSystem.Schema() // Schema | 
};
apiInstance.createOrUpdateProfileSchema(contentType, accept, opts, (error, data, response) => {
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
 **schema** | [**Schema**](Schema.md)|  | [optional] 

### Return type

**Object**

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

