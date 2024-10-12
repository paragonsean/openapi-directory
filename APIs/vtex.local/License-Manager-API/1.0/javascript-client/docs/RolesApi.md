# LicenseManagerApi.RolesApi

All URIs are relative to *https://vtex.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getListRoles**](RolesApi.md#getListRoles) | **GET** /api/license-manager/site/pvt/roles/list/paged | Get List of Roles
[**getRolesbyUser**](RolesApi.md#getRolesbyUser) | **GET** /api/license-manager/users/{userId}/roles | Get Roles by User/appKey
[**putRolesinUser**](RolesApi.md#putRolesinUser) | **PUT** /api/license-manager/users/{userId}/roles | Put Roles in User/appKey
[**removeRolefromUser**](RolesApi.md#removeRolefromUser) | **DELETE** /api/license-manager/users/{userId}/roles/{roleId} | Remove Role from User/appKey



## getListRoles

> ListRolesResponse getListRoles(contentType, opts)

Get List of Roles

Returns a list of available roles. The response is divided in pages. The query parameter &#x60;numItems&#x60; defines the number of items in each page, and consequently the amount of pages for the whole list.

### Example

```javascript
import LicenseManagerApi from 'license_manager_api';
let defaultClient = LicenseManagerApi.ApiClient.instance;
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

let apiInstance = new LicenseManagerApi.RolesApi();
let contentType = "'application/json'"; // String | The media type of the body of the request. Default value for license manager protocol is application/json
let opts = {
  'numItems': 10, // Number | Number of items in the returned page
  'pageNumber': 1, // Number | Which page from the whole list will be returned
  'sort': "'id'", // String | Chooses the field that the list will be sorted by
  'sortType': "'ASC'" // String | Defines the sorting order. ASC is used for ascendant order. DSC is used for descendant order
};
apiInstance.getListRoles(contentType, opts, (error, data, response) => {
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
 **contentType** | **String**| The media type of the body of the request. Default value for license manager protocol is application/json | [default to &#39;application/json&#39;]
 **numItems** | **Number**| Number of items in the returned page | [optional] [default to 10]
 **pageNumber** | **Number**| Which page from the whole list will be returned | [optional] [default to 1]
 **sort** | **String**| Chooses the field that the list will be sorted by | [optional] [default to &#39;id&#39;]
 **sortType** | **String**| Defines the sorting order. ASC is used for ascendant order. DSC is used for descendant order | [optional] [default to &#39;ASC&#39;]

### Return type

[**ListRolesResponse**](ListRolesResponse.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getRolesbyUser

> [GetRolesbyUser200ResponseInner] getRolesbyUser(contentType, userId)

Get Roles by User/appKey

Gets roles of a particular user or application key.

### Example

```javascript
import LicenseManagerApi from 'license_manager_api';
let defaultClient = LicenseManagerApi.ApiClient.instance;
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

let apiInstance = new LicenseManagerApi.RolesApi();
let contentType = "application/json"; // String | The media type of the body of the request. Default value for license manager protocol is application/json
let userId = "userId_example"; // String | ID corresponding to the user
apiInstance.getRolesbyUser(contentType, userId, (error, data, response) => {
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
 **contentType** | **String**| The media type of the body of the request. Default value for license manager protocol is application/json | 
 **userId** | **String**| ID corresponding to the user | 

### Return type

[**[GetRolesbyUser200ResponseInner]**](GetRolesbyUser200ResponseInner.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## putRolesinUser

> putRolesinUser(userId, requestBody)

Put Roles in User/appKey

Allows you to add roles to a particular user or application key by specifying the list of roles&#39; IDs on the request&#39;s body.

### Example

```javascript
import LicenseManagerApi from 'license_manager_api';
let defaultClient = LicenseManagerApi.ApiClient.instance;
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

let apiInstance = new LicenseManagerApi.RolesApi();
let userId = "userId_example"; // String | ID corresponding to the user
let requestBody = [9000,9111,9333,9444]; // [Number] | List of roles' IDs to add to the user or application key.
apiInstance.putRolesinUser(userId, requestBody, (error, data, response) => {
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
 **userId** | **String**| ID corresponding to the user | 
 **requestBody** | [**[Number]**](Number.md)| List of roles&#39; IDs to add to the user or application key. | 

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## removeRolefromUser

> removeRolefromUser(contentType, userId, roleId)

Remove Role from User/appKey

Allows you to remove a role from a specific user or application key. This method only allows the removal of one role per request. The role&#39;s ID must be specified on the request path, not on the request body.    &gt; Note that a successful response returns a &#x60;204&#x60; response with an empty body. A deletion on a role or user that does not exist will also return a &#x60;204&#x60;. Thus, this method should not be used to verify the existence of a specific user or role.

### Example

```javascript
import LicenseManagerApi from 'license_manager_api';
let defaultClient = LicenseManagerApi.ApiClient.instance;
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

let apiInstance = new LicenseManagerApi.RolesApi();
let contentType = "application/json"; // String | The media type of the body of the request. Default value for license manager protocol is application/json
let userId = "userId_example"; // String | ID corresponding to the user
let roleId = "roleId_example"; // String | ID of the role which will be removed from the user
apiInstance.removeRolefromUser(contentType, userId, roleId, (error, data, response) => {
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
 **contentType** | **String**| The media type of the body of the request. Default value for license manager protocol is application/json | 
 **userId** | **String**| ID corresponding to the user | 
 **roleId** | **String**| ID of the role which will be removed from the user | 

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

