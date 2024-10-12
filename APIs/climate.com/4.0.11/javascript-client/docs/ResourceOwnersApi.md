# ClimateFieldViewPlatformApis.ResourceOwnersApi

All URIs are relative to *https://platform.climate.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getResourceOwner**](ResourceOwnersApi.md#getResourceOwner) | **GET** /v4/resourceOwners/{resourceOwnerId} | Retrieve a resource owner by ID



## getResourceOwner

> ResourceOwner getResourceOwner(resourceOwnerId)

Retrieve a resource owner by ID

Retrieve a resource owner for the given &#x60;resourceOwnerId&#x60;.

### Example

```javascript
import ClimateFieldViewPlatformApis from 'climate_field_view_platform_apis';
let defaultClient = ClimateFieldViewPlatformApis.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: oauth2_authorization_code
let oauth2_authorization_code = defaultClient.authentications['oauth2_authorization_code'];
oauth2_authorization_code.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ClimateFieldViewPlatformApis.ResourceOwnersApi();
let resourceOwnerId = "resourceOwnerId_example"; // String | Unique identifier of the resource owner.
apiInstance.getResourceOwner(resourceOwnerId, (error, data, response) => {
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
 **resourceOwnerId** | **String**| Unique identifier of the resource owner. | 

### Return type

[**ResourceOwner**](ResourceOwner.md)

### Authorization

[api_key](../README.md#api_key), [oauth2_authorization_code](../README.md#oauth2_authorization_code)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

