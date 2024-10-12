# FitbitPlusApi.OauthApi

All URIs are relative to *https://api.twinehealth.com/pub*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createToken**](OauthApi.md#createToken) | **POST** /oauth/token | Create an oauth token
[**fetchTokenGroups**](OauthApi.md#fetchTokenGroups) | **GET** /oauth/token/{id}/groups | Get the groups for a token
[**fetchTokenOrganization**](OauthApi.md#fetchTokenOrganization) | **GET** /oauth/token/{id}/organization | Get the organization for a token



## createToken

> CreateTokenResponse createToken(createTokenRequest, opts)

Create an oauth token

Create an OAuth 2.0 Bearer token. A valid bearer token is required for all other API requests.  Be sure to set the header &#x60;Content-Type: \&quot;application/vnd.api+json\&quot;&#x60;. Otherwise, you will get an error 403 Forbidden. Using &#x60;Content-Type: \&quot;application/json\&quot;&#x60; is permitted (to support older oauth clients) but when using &#x60;application/json&#x60; the body should have a body in the following format instead of nesting under &#x60;data.attributes&#x60;: &#x60;&#x60;&#x60; {   \&quot;grant_type\&quot;: \&quot;client_credentials\&quot;,   \&quot;client_id\&quot;: \&quot;95c78ab2-167f-40b8-8bec-8398d4b87454\&quot;,   \&quot;client_secret\&quot;: \&quot;35d18dc9-a3dd-4948-b787-063a490b9354\&quot; } &#x60;&#x60;&#x60; 

### Example

```javascript
import FitbitPlusApi from 'fitbit_plus_api';
let defaultClient = FitbitPlusApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new FitbitPlusApi.OauthApi();
let createTokenRequest = new FitbitPlusApi.CreateTokenRequest(); // CreateTokenRequest | 
let opts = {
  'include': "include_example" // String | List of related resources to include in the response
};
apiInstance.createToken(createTokenRequest, opts, (error, data, response) => {
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
 **createTokenRequest** | [**CreateTokenRequest**](CreateTokenRequest.md)|  | 
 **include** | **String**| List of related resources to include in the response | [optional] 

### Return type

[**CreateTokenResponse**](CreateTokenResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json, application/vnd.api+json
- **Accept**: application/vnd.api+json


## fetchTokenGroups

> FetchGroupsResponse fetchTokenGroups(id)

Get the groups for a token

Get the list of groups a token can be used to access.

### Example

```javascript
import FitbitPlusApi from 'fitbit_plus_api';
let defaultClient = FitbitPlusApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new FitbitPlusApi.OauthApi();
let id = "id_example"; // String | Token identifier
apiInstance.fetchTokenGroups(id, (error, data, response) => {
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
 **id** | **String**| Token identifier | 

### Return type

[**FetchGroupsResponse**](FetchGroupsResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.api+json


## fetchTokenOrganization

> FetchOrganizationResponse fetchTokenOrganization(id)

Get the organization for a token

Get the organization a token can be used to access.

### Example

```javascript
import FitbitPlusApi from 'fitbit_plus_api';

let apiInstance = new FitbitPlusApi.OauthApi();
let id = "id_example"; // String | Token identifier
apiInstance.fetchTokenOrganization(id, (error, data, response) => {
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
 **id** | **String**| Token identifier | 

### Return type

[**FetchOrganizationResponse**](FetchOrganizationResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.api+json

