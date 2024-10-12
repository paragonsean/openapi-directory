# ClimateFieldViewPlatformApis.FieldsApi

All URIs are relative to *https://platform.climate.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetchAllFields**](FieldsApi.md#fetchAllFields) | **GET** /v4/fields/all | Retrieve list of all Fields the user has access to.
[**fetchFieldById**](FieldsApi.md#fetchFieldById) | **GET** /v4/fields/{fieldId} | Retrieve a specific Field by ID
[**fetchFields**](FieldsApi.md#fetchFields) | **GET** /v4/fields | Retrieve list of Fields



## fetchAllFields

> Fields fetchAllFields(opts)

Retrieve list of all Fields the user has access to.

Retrieve all fields the authenticated user has access to, including fields shared with the authenticated user from other resource owners. Filter the results by field name if the &#x60;fieldName&#x60; query parameter is specified. A 409 will be returned if the X-Next-Token has expired. When receiving a 409, the client should discard the X-Next-Token, discard all currently persisted fields for the user, and re-fetch fields from /fields/all.

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

let apiInstance = new ClimateFieldViewPlatformApis.FieldsApi();
let opts = {
  'xNextToken': "xNextToken_example", // String | Opaque string which allows for fetching the next batch of results.  Can be used to poll for changes.
  'xLimit': 56, // Number | Max number of results to return per batch.  Must be between 1 and 100 inclusive.  Defaults to 100.
  'fieldName': "fieldName_example" // String | Optional prefix filter for field name. Must be at least 3 characters.
};
apiInstance.fetchAllFields(opts, (error, data, response) => {
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
 **xNextToken** | **String**| Opaque string which allows for fetching the next batch of results.  Can be used to poll for changes. | [optional] 
 **xLimit** | **Number**| Max number of results to return per batch.  Must be between 1 and 100 inclusive.  Defaults to 100. | [optional] 
 **fieldName** | **String**| Optional prefix filter for field name. Must be at least 3 characters. | [optional] 

### Return type

[**Fields**](Fields.md)

### Authorization

[api_key](../README.md#api_key), [oauth2_authorization_code](../README.md#oauth2_authorization_code)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## fetchFieldById

> Field fetchFieldById(fieldId)

Retrieve a specific Field by ID

Retrieve a given **Field** by ID.

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

let apiInstance = new ClimateFieldViewPlatformApis.FieldsApi();
let fieldId = "fieldId_example"; // String | Unique identifier of the Field.
apiInstance.fetchFieldById(fieldId, (error, data, response) => {
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
 **fieldId** | **String**| Unique identifier of the Field. | 

### Return type

[**Field**](Field.md)

### Authorization

[api_key](../README.md#api_key), [oauth2_authorization_code](../README.md#oauth2_authorization_code)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## fetchFields

> Fields fetchFields(opts)

Retrieve list of Fields

Retrieve list of **Fields**. Filter the results by field name if the &#x60;fieldName&#x60; query parameter is specified.

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

let apiInstance = new ClimateFieldViewPlatformApis.FieldsApi();
let opts = {
  'xNextToken': "xNextToken_example", // String | Opaque string which allows for fetching the next batch of results.  Can be used to poll for changes.
  'xLimit': 56, // Number | Max number of results to return per batch.  Must be between 1 and 100 inclusive.  Defaults to 100.
  'fieldName': "fieldName_example" // String | Optional prefix filter for field name. Must be at least 3 characters.
};
apiInstance.fetchFields(opts, (error, data, response) => {
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
 **xNextToken** | **String**| Opaque string which allows for fetching the next batch of results.  Can be used to poll for changes. | [optional] 
 **xLimit** | **Number**| Max number of results to return per batch.  Must be between 1 and 100 inclusive.  Defaults to 100. | [optional] 
 **fieldName** | **String**| Optional prefix filter for field name. Must be at least 3 characters. | [optional] 

### Return type

[**Fields**](Fields.md)

### Authorization

[api_key](../README.md#api_key), [oauth2_authorization_code](../README.md#oauth2_authorization_code)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

