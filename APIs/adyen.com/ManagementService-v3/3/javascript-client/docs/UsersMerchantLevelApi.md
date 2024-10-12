# ManagementApi.UsersMerchantLevelApi

All URIs are relative to *https://management-test.adyen.com/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getMerchantsMerchantIdUsers**](UsersMerchantLevelApi.md#getMerchantsMerchantIdUsers) | **GET** /merchants/{merchantId}/users | Get a list of users
[**getMerchantsMerchantIdUsersUserId**](UsersMerchantLevelApi.md#getMerchantsMerchantIdUsersUserId) | **GET** /merchants/{merchantId}/users/{userId} | Get user details
[**patchMerchantsMerchantIdUsersUserId**](UsersMerchantLevelApi.md#patchMerchantsMerchantIdUsersUserId) | **PATCH** /merchants/{merchantId}/users/{userId} | Update a user
[**postMerchantsMerchantIdUsers**](UsersMerchantLevelApi.md#postMerchantsMerchantIdUsers) | **POST** /merchants/{merchantId}/users | Create a new user



## getMerchantsMerchantIdUsers

> ListMerchantUsersResponse getMerchantsMerchantIdUsers(merchantId, opts)

Get a list of users

Returns a list of users associated with the &#x60;merchantId&#x60; specified in the path.  To make this request, your API credential must have the following [role](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Users read and write 

### Example

```javascript
import ManagementApi from 'management_api';
let defaultClient = ManagementApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new ManagementApi.UsersMerchantLevelApi();
let merchantId = "merchantId_example"; // String | Unique identifier of the merchant.
let opts = {
  'pageNumber': 56, // Number | The number of the page to fetch.
  'pageSize': 56, // Number | The number of items to have on a page. Maximum value is **100**. The default is **10** items on a page.
  'username': "username_example" // String | The partial or complete username to select all users that match.
};
apiInstance.getMerchantsMerchantIdUsers(merchantId, opts, (error, data, response) => {
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
 **merchantId** | **String**| Unique identifier of the merchant. | 
 **pageNumber** | **Number**| The number of the page to fetch. | [optional] 
 **pageSize** | **Number**| The number of items to have on a page. Maximum value is **100**. The default is **10** items on a page. | [optional] 
 **username** | **String**| The partial or complete username to select all users that match. | [optional] 

### Return type

[**ListMerchantUsersResponse**](ListMerchantUsersResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getMerchantsMerchantIdUsersUserId

> User getMerchantsMerchantIdUsersUserId(merchantId, userId)

Get user details

Returns user details for the &#x60;userId&#x60; and the &#x60;merchantId&#x60; specified in the path.  To make this request, your API credential must have the following [role](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Users read and write 

### Example

```javascript
import ManagementApi from 'management_api';
let defaultClient = ManagementApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new ManagementApi.UsersMerchantLevelApi();
let merchantId = "merchantId_example"; // String | Unique identifier of the merchant.
let userId = "userId_example"; // String | Unique identifier of the user.
apiInstance.getMerchantsMerchantIdUsersUserId(merchantId, userId, (error, data, response) => {
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
 **merchantId** | **String**| Unique identifier of the merchant. | 
 **userId** | **String**| Unique identifier of the user. | 

### Return type

[**User**](User.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## patchMerchantsMerchantIdUsersUserId

> User patchMerchantsMerchantIdUsersUserId(merchantId, userId, opts)

Update a user

Updates user details for the &#x60;userId&#x60; and the &#x60;merchantId&#x60; specified in the path.  To make this request, your API credential must have the following [role](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Users read and write 

### Example

```javascript
import ManagementApi from 'management_api';
let defaultClient = ManagementApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new ManagementApi.UsersMerchantLevelApi();
let merchantId = "merchantId_example"; // String | Unique identifier of the merchant.
let userId = "userId_example"; // String | Unique identifier of the user.
let opts = {
  'updateMerchantUserRequest': new ManagementApi.UpdateMerchantUserRequest() // UpdateMerchantUserRequest | 
};
apiInstance.patchMerchantsMerchantIdUsersUserId(merchantId, userId, opts, (error, data, response) => {
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
 **merchantId** | **String**| Unique identifier of the merchant. | 
 **userId** | **String**| Unique identifier of the user. | 
 **updateMerchantUserRequest** | [**UpdateMerchantUserRequest**](UpdateMerchantUserRequest.md)|  | [optional] 

### Return type

[**User**](User.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## postMerchantsMerchantIdUsers

> CreateUserResponse postMerchantsMerchantIdUsers(merchantId, opts)

Create a new user

Creates a user for the &#x60;merchantId&#x60; specified in the path.  To make this request, your API credential must have the following [role](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Users read and write 

### Example

```javascript
import ManagementApi from 'management_api';
let defaultClient = ManagementApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new ManagementApi.UsersMerchantLevelApi();
let merchantId = "merchantId_example"; // String | Unique identifier of the merchant.
let opts = {
  'createMerchantUserRequest': new ManagementApi.CreateMerchantUserRequest() // CreateMerchantUserRequest | 
};
apiInstance.postMerchantsMerchantIdUsers(merchantId, opts, (error, data, response) => {
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
 **merchantId** | **String**| Unique identifier of the merchant. | 
 **createMerchantUserRequest** | [**CreateMerchantUserRequest**](CreateMerchantUserRequest.md)|  | [optional] 

### Return type

[**CreateUserResponse**](CreateUserResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

