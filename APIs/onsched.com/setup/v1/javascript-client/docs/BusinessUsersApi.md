# OnSchedSetupApi.BusinessUsersApi

All URIs are relative to *https://sandbox-api.onsched.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**setupV1BusinessusersEmailCompaniesGet**](BusinessUsersApi.md#setupV1BusinessusersEmailCompaniesGet) | **GET** /setup/v1/businessusers/{email}/companies | List User Companies
[**setupV1BusinessusersGet**](BusinessUsersApi.md#setupV1BusinessusersGet) | **GET** /setup/v1/businessusers | List Users
[**setupV1BusinessusersIdDelete**](BusinessUsersApi.md#setupV1BusinessusersIdDelete) | **DELETE** /setup/v1/businessusers/{id} | Delete User
[**setupV1BusinessusersIdGet**](BusinessUsersApi.md#setupV1BusinessusersIdGet) | **GET** /setup/v1/businessusers/{id} | Get User
[**setupV1BusinessusersIdPut**](BusinessUsersApi.md#setupV1BusinessusersIdPut) | **PUT** /setup/v1/businessusers/{id} | Update User
[**setupV1BusinessusersPermissionsGet**](BusinessUsersApi.md#setupV1BusinessusersPermissionsGet) | **GET** /setup/v1/businessusers/permissions | List User Permissions
[**setupV1BusinessusersPost**](BusinessUsersApi.md#setupV1BusinessusersPost) | **POST** /setup/v1/businessusers | Create User



## setupV1BusinessusersEmailCompaniesGet

> AuthorizedCompanyListViewModel setupV1BusinessusersEmailCompaniesGet(email, opts)

List User Companies

&lt;p&gt;Use this endpoint to return a &lt;b&gt;List of Companies&lt;/b&gt; associated with the business users email requested. A business user &lt;b&gt;email&lt;/b&gt; address is required. Use the offset and limit parameters to control the page start and number of results. Default offset is 0, limit is 20, max is 100. Use the query parameters to filter the results further.&lt;/p&gt;

### Example

```javascript
import OnSchedSetupApi from 'on_sched_setup_api';
let defaultClient = OnSchedSetupApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new OnSchedSetupApi.BusinessUsersApi();
let email = "email_example"; // String | Email of business user
let opts = {
  'searchText': "searchText_example", // String | All or partial company name
  'offset': 56, // Number | Starting row of page, default 0
  'limit': 56 // Number | Page limit default 20, max 100
};
apiInstance.setupV1BusinessusersEmailCompaniesGet(email, opts, (error, data, response) => {
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
 **email** | **String**| Email of business user | 
 **searchText** | **String**| All or partial company name | [optional] 
 **offset** | **Number**| Starting row of page, default 0 | [optional] 
 **limit** | **Number**| Page limit default 20, max 100 | [optional] 

### Return type

[**AuthorizedCompanyListViewModel**](AuthorizedCompanyListViewModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## setupV1BusinessusersGet

> BusinessUserListViewModel setupV1BusinessusersGet(opts)

List Users

&lt;p&gt;Use this endpoint to return a &lt;b&gt;List of Business Users and their Roles&lt;/b&gt;. The results are returned in pages. Use the offset and limit parameters to control the page start and number of results. Default offset is 0, limit is 20, max is 100. Use the query parameters to filter the results further.&lt;/p&gt;

### Example

```javascript
import OnSchedSetupApi from 'on_sched_setup_api';
let defaultClient = OnSchedSetupApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new OnSchedSetupApi.BusinessUsersApi();
let opts = {
  'locationId': "locationId_example", // String | id of business location, defaults to primary business location
  'email': "email_example", // String | Filter by email address
  'role': "role_example", // String | Filter user role
  'offset': 56, // Number | Starting row of page, default 0
  'limit': 56 // Number | Page limit default 20, max 100
};
apiInstance.setupV1BusinessusersGet(opts, (error, data, response) => {
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
 **locationId** | **String**| id of business location, defaults to primary business location | [optional] 
 **email** | **String**| Filter by email address | [optional] 
 **role** | **String**| Filter user role | [optional] 
 **offset** | **Number**| Starting row of page, default 0 | [optional] 
 **limit** | **Number**| Page limit default 20, max 100 | [optional] 

### Return type

[**BusinessUserListViewModel**](BusinessUserListViewModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## setupV1BusinessusersIdDelete

> setupV1BusinessusersIdDelete(id)

Delete User

&lt;p&gt;Use this endpoint to permanently &lt;b&gt;Delete&lt;/b&gt; a Business User. A valid &lt;b&gt;businessUser id&lt;/b&gt; is required.&lt;/p&gt;

### Example

```javascript
import OnSchedSetupApi from 'on_sched_setup_api';
let defaultClient = OnSchedSetupApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new OnSchedSetupApi.BusinessUsersApi();
let id = "id_example"; // String | 
apiInstance.setupV1BusinessusersIdDelete(id, (error, data, response) => {
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
 **id** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## setupV1BusinessusersIdGet

> BusinessUserViewModel setupV1BusinessusersIdGet(id)

Get User

&lt;p&gt;Use this endpoint to return a &lt;b&gt;Business User&lt;/b&gt; object. A valid &lt;b&gt;businessUser id&lt;/b&gt; is required. Find businessUser id&#39;s using the &lt;i&gt;GET /setup/v1/businessusers&lt;/i&gt; endpoint.&lt;/p&gt;

### Example

```javascript
import OnSchedSetupApi from 'on_sched_setup_api';
let defaultClient = OnSchedSetupApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new OnSchedSetupApi.BusinessUsersApi();
let id = "id_example"; // String | id of businessUser object
apiInstance.setupV1BusinessusersIdGet(id, (error, data, response) => {
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
 **id** | **String**| id of businessUser object | 

### Return type

[**BusinessUserViewModel**](BusinessUserViewModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## setupV1BusinessusersIdPut

> BusinessUserViewModel setupV1BusinessusersIdPut(id, opts)

Update User

&lt;p&gt;Use this endpoint to &lt;b&gt;Update&lt;/b&gt; a Business User. A valid &lt;b&gt;businessUser id&lt;/b&gt; is required.&lt;/p&gt;  &lt;p&gt;    &lt;b&gt;Business Roles Include: bizowner&lt;/b&gt; (Business Owner), &lt;b&gt;bizadmin&lt;/b&gt; (Business Administrator), &lt;b&gt;bizresource&lt;/b&gt; (Business User - Bookable Resource).&lt;/p&gt;

### Example

```javascript
import OnSchedSetupApi from 'on_sched_setup_api';
let defaultClient = OnSchedSetupApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new OnSchedSetupApi.BusinessUsersApi();
let id = "id_example"; // String | 
let opts = {
  'businessUserUpdateModel': new OnSchedSetupApi.BusinessUserUpdateModel() // BusinessUserUpdateModel | 
};
apiInstance.setupV1BusinessusersIdPut(id, opts, (error, data, response) => {
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
 **id** | **String**|  | 
 **businessUserUpdateModel** | [**BusinessUserUpdateModel**](BusinessUserUpdateModel.md)|  | [optional] 

### Return type

[**BusinessUserViewModel**](BusinessUserViewModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/*+json, application/json, application/json-patch+json, text/json
- **Accept**: application/json


## setupV1BusinessusersPermissionsGet

> BusinessPermissionListViewModel setupV1BusinessusersPermissionsGet(opts)

List User Permissions

&lt;p&gt;Use this endpoint to return a &lt;b&gt;List of Business User Permissions by Role&lt;/b&gt;. Results are returned in pages. Use the offset and limit parameters to control the page start and number of results. Default offset is 0, limit is 20, max is 100. Use the query parameters to filter the results further.&lt;/p&gt;

### Example

```javascript
import OnSchedSetupApi from 'on_sched_setup_api';
let defaultClient = OnSchedSetupApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new OnSchedSetupApi.BusinessUsersApi();
let opts = {
  'role': "role_example", // String | Filter permissions by role
  'offset': 56, // Number | Starting row of page, default 0
  'limit': 56 // Number | Page limit default 20, max 100
};
apiInstance.setupV1BusinessusersPermissionsGet(opts, (error, data, response) => {
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
 **role** | **String**| Filter permissions by role | [optional] 
 **offset** | **Number**| Starting row of page, default 0 | [optional] 
 **limit** | **Number**| Page limit default 20, max 100 | [optional] 

### Return type

[**BusinessPermissionListViewModel**](BusinessPermissionListViewModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## setupV1BusinessusersPost

> BusinessUserViewModel setupV1BusinessusersPost(opts)

Create User

&lt;p&gt;Use this endpoint to &lt;b&gt;Create&lt;/b&gt; a Business User. If not specified, the business location defaults to the primary business location. &lt;/p&gt;  &lt;p&gt;Required fields: &lt;b&gt;Name&lt;/b&gt;, &lt;b&gt;Email&lt;/b&gt; and &lt;b&gt;Role&lt;/b&gt;&lt;b&gt;Note:&lt;/b&gt; If the businessUser is a bookable resource (bizresource) then a resourceId is required.&lt;/p&gt;  &lt;p&gt;For role, use one of the values listed. &lt;b&gt;Business Roles Include: bizowner&lt;/b&gt; (Business Owner), &lt;b&gt;bizadmin&lt;/b&gt; (Business Administrator), &lt;b&gt;bizresource&lt;/b&gt; (Business User - Bookable Resource).&lt;/p&gt;  &lt;p&gt;The &lt;b&gt;sendRegistrationInvite&lt;/b&gt; parameter is available to API consumers for their own use. It provides no added functionality in OnSched.&lt;/p&gt;

### Example

```javascript
import OnSchedSetupApi from 'on_sched_setup_api';
let defaultClient = OnSchedSetupApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new OnSchedSetupApi.BusinessUsersApi();
let opts = {
  'businessUserInputModel': new OnSchedSetupApi.BusinessUserInputModel() // BusinessUserInputModel | 
};
apiInstance.setupV1BusinessusersPost(opts, (error, data, response) => {
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
 **businessUserInputModel** | [**BusinessUserInputModel**](BusinessUserInputModel.md)|  | [optional] 

### Return type

[**BusinessUserViewModel**](BusinessUserViewModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/*+json, application/json, application/json-patch+json, text/json
- **Accept**: application/json

