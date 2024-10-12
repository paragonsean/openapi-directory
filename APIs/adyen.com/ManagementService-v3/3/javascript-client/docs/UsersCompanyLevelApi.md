# ManagementApi.UsersCompanyLevelApi

All URIs are relative to *https://management-test.adyen.com/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getCompaniesCompanyIdUsers**](UsersCompanyLevelApi.md#getCompaniesCompanyIdUsers) | **GET** /companies/{companyId}/users | Get a list of users
[**getCompaniesCompanyIdUsersUserId**](UsersCompanyLevelApi.md#getCompaniesCompanyIdUsersUserId) | **GET** /companies/{companyId}/users/{userId} | Get user details
[**patchCompaniesCompanyIdUsersUserId**](UsersCompanyLevelApi.md#patchCompaniesCompanyIdUsersUserId) | **PATCH** /companies/{companyId}/users/{userId} | Update user details
[**postCompaniesCompanyIdUsers**](UsersCompanyLevelApi.md#postCompaniesCompanyIdUsers) | **POST** /companies/{companyId}/users | Create a new user



## getCompaniesCompanyIdUsers

> ListCompanyUsersResponse getCompaniesCompanyIdUsers(companyId, opts)

Get a list of users

Returns the list of users for the &#x60;companyId&#x60; identified in the path.  To make this request, your API credential must have the following [role](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Users read and write 

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

let apiInstance = new ManagementApi.UsersCompanyLevelApi();
let companyId = "companyId_example"; // String | The unique identifier of the company account.
let opts = {
  'pageNumber': 56, // Number | The number of the page to return.
  'pageSize': 56, // Number | The number of items to have on a page. Maximum value is **100**. The default is **10** items on a page.
  'username': "username_example" // String | The partial or complete username to select all users that match.
};
apiInstance.getCompaniesCompanyIdUsers(companyId, opts, (error, data, response) => {
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
 **companyId** | **String**| The unique identifier of the company account. | 
 **pageNumber** | **Number**| The number of the page to return. | [optional] 
 **pageSize** | **Number**| The number of items to have on a page. Maximum value is **100**. The default is **10** items on a page. | [optional] 
 **username** | **String**| The partial or complete username to select all users that match. | [optional] 

### Return type

[**ListCompanyUsersResponse**](ListCompanyUsersResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getCompaniesCompanyIdUsersUserId

> CompanyUser getCompaniesCompanyIdUsersUserId(companyId, userId)

Get user details

Returns user details for the &#x60;userId&#x60; and the &#x60;companyId&#x60; identified in the path.  To make this request, your API credential must have the following [role](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Users read and write 

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

let apiInstance = new ManagementApi.UsersCompanyLevelApi();
let companyId = "companyId_example"; // String | The unique identifier of the company account.
let userId = "userId_example"; // String | The unique identifier of the user.
apiInstance.getCompaniesCompanyIdUsersUserId(companyId, userId, (error, data, response) => {
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
 **companyId** | **String**| The unique identifier of the company account. | 
 **userId** | **String**| The unique identifier of the user. | 

### Return type

[**CompanyUser**](CompanyUser.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## patchCompaniesCompanyIdUsersUserId

> CompanyUser patchCompaniesCompanyIdUsersUserId(companyId, userId, opts)

Update user details

Updates user details for the &#x60;userId&#x60; and the &#x60;companyId&#x60; identified in the path.  To make this request, your API credential must have the following [role](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Users read and write 

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

let apiInstance = new ManagementApi.UsersCompanyLevelApi();
let companyId = "companyId_example"; // String | The unique identifier of the company account.
let userId = "userId_example"; // String | The unique identifier of the user.
let opts = {
  'updateCompanyUserRequest': new ManagementApi.UpdateCompanyUserRequest() // UpdateCompanyUserRequest | 
};
apiInstance.patchCompaniesCompanyIdUsersUserId(companyId, userId, opts, (error, data, response) => {
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
 **companyId** | **String**| The unique identifier of the company account. | 
 **userId** | **String**| The unique identifier of the user. | 
 **updateCompanyUserRequest** | [**UpdateCompanyUserRequest**](UpdateCompanyUserRequest.md)|  | [optional] 

### Return type

[**CompanyUser**](CompanyUser.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## postCompaniesCompanyIdUsers

> CreateCompanyUserResponse postCompaniesCompanyIdUsers(companyId, opts)

Create a new user

Creates the user for the &#x60;companyId&#x60; identified in the path.  To make this request, your API credential must have the following [role](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Users read and write 

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

let apiInstance = new ManagementApi.UsersCompanyLevelApi();
let companyId = "companyId_example"; // String | The unique identifier of the company account.
let opts = {
  'createCompanyUserRequest': new ManagementApi.CreateCompanyUserRequest() // CreateCompanyUserRequest | 
};
apiInstance.postCompaniesCompanyIdUsers(companyId, opts, (error, data, response) => {
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
 **companyId** | **String**| The unique identifier of the company account. | 
 **createCompanyUserRequest** | [**CreateCompanyUserRequest**](CreateCompanyUserRequest.md)|  | [optional] 

### Return type

[**CreateCompanyUserResponse**](CreateCompanyUserResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

