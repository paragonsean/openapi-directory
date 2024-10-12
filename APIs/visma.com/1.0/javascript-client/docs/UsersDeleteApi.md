# SeveraPublicRestApiDocumentation.UsersDeleteApi

All URIs are relative to *https://api.severa.visma.com/rest-api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**keywordsDeleteUserKeyword**](UsersDeleteApi.md#keywordsDeleteUserKeyword) | **DELETE** /v1/users/{userGuid}/keywords/{guid} | Delete a keyword from the user
[**userCustomValuesDeleteUserCustomValue**](UsersDeleteApi.md#userCustomValuesDeleteUserCustomValue) | **DELETE** /v1/users/customvalues/{guid} | Deletes a user custom value.
[**usersDeleteUser**](UsersDeleteApi.md#usersDeleteUser) | **DELETE** /v1/users/{guid} | Delete an user.
[**workContractsDeleteWorkContract_0**](UsersDeleteApi.md#workContractsDeleteWorkContract_0) | **DELETE** /v1/workcontracts/{guid} | Delete a work contract.



## keywordsDeleteUserKeyword

> keywordsDeleteUserKeyword(userGuid, guid)

Delete a keyword from the user

Returns: No Content (204) if succeeded. Not found (404) if the keyword or the link can&#39;t be found.

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.UsersDeleteApi();
let userGuid = "userGuid_example"; // String | 
let guid = "guid_example"; // String | 
apiInstance.keywordsDeleteUserKeyword(userGuid, guid, (error, data, response) => {
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
 **userGuid** | **String**|  | 
 **guid** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## userCustomValuesDeleteUserCustomValue

> userCustomValuesDeleteUserCustomValue(guid)

Deletes a user custom value.

Returns: No Content (204) if succeeded.

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.UsersDeleteApi();
let guid = "guid_example"; // String | GUID used to delete the user custom value.
apiInstance.userCustomValuesDeleteUserCustomValue(guid, (error, data, response) => {
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
 **guid** | **String**| GUID used to delete the user custom value. | 

### Return type

null (empty response body)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## usersDeleteUser

> usersDeleteUser(guid)

Delete an user.

No Content (204) if succeeded. Bad Request (400) if user can&#39;t be deleted. Not Found (404) if the user can&#39;t be found.

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.UsersDeleteApi();
let guid = "guid_example"; // String | ID of the user.
apiInstance.usersDeleteUser(guid, (error, data, response) => {
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
 **guid** | **String**| ID of the user. | 

### Return type

null (empty response body)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## workContractsDeleteWorkContract_0

> workContractsDeleteWorkContract_0(guid)

Delete a work contract.

Returns: No Content (204) if succeeded. Not found (404) if work contract can&#39;t be found.

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.UsersDeleteApi();
let guid = "guid_example"; // String | ID for the work contract to delete.
apiInstance.workContractsDeleteWorkContract_0(guid, (error, data, response) => {
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
 **guid** | **String**| ID for the work contract to delete. | 

### Return type

null (empty response body)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

