# ClimateFieldViewPlatformApis.OperationsApi

All URIs are relative to *https://platform.climate.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetchOperations**](OperationsApi.md#fetchOperations) | **GET** /v4/operations/all | Retrieve the operations accessible to a a given user.



## fetchOperations

> Operations fetchOperations(opts)

Retrieve the operations accessible to a a given user.

Retrieve the **operations** accessible to the authenticated user. Filter the results by resource owner if the &#x60;resourceOwnerId&#x60; query parameter is specified.

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

let apiInstance = new ClimateFieldViewPlatformApis.OperationsApi();
let opts = {
  'resourceOwnerId': "resourceOwnerId_example" // String | Optional comma-separated list of resource owner unique identifiers by which to filter results.
};
apiInstance.fetchOperations(opts, (error, data, response) => {
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
 **resourceOwnerId** | **String**| Optional comma-separated list of resource owner unique identifiers by which to filter results. | [optional] 

### Return type

[**Operations**](Operations.md)

### Authorization

[api_key](../README.md#api_key), [oauth2_authorization_code](../README.md#oauth2_authorization_code)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

