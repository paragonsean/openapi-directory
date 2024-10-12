# NetlifysApiDocumentation.MemberApi

All URIs are relative to *https://api.netlify.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addMemberToAccount**](MemberApi.md#addMemberToAccount) | **POST** /{account_slug}/members | 
[**getAccountMember**](MemberApi.md#getAccountMember) | **GET** /{account_slug}/members/{member_id} | 
[**listMembersForAccount**](MemberApi.md#listMembersForAccount) | **GET** /{account_slug}/members | 
[**removeAccountMember**](MemberApi.md#removeAccountMember) | **DELETE** /{account_slug}/members/{member_id} | 
[**updateAccountMember**](MemberApi.md#updateAccountMember) | **PUT** /{account_slug}/members/{member_id} | 



## addMemberToAccount

> [Member] addMemberToAccount(accountSlug, accountAddMemberSetup)



### Example

```javascript
import NetlifysApiDocumentation from 'netlifys_api_documentation';
let defaultClient = NetlifysApiDocumentation.ApiClient.instance;
// Configure OAuth2 access token for authorization: netlifyAuth
let netlifyAuth = defaultClient.authentications['netlifyAuth'];
netlifyAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetlifysApiDocumentation.MemberApi();
let accountSlug = "accountSlug_example"; // String | 
let accountAddMemberSetup = new NetlifysApiDocumentation.AccountAddMemberSetup(); // AccountAddMemberSetup | 
apiInstance.addMemberToAccount(accountSlug, accountAddMemberSetup, (error, data, response) => {
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
 **accountSlug** | **String**|  | 
 **accountAddMemberSetup** | [**AccountAddMemberSetup**](AccountAddMemberSetup.md)|  | 

### Return type

[**[Member]**](Member.md)

### Authorization

[netlifyAuth](../README.md#netlifyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getAccountMember

> Member getAccountMember(accountSlug, memberId)



### Example

```javascript
import NetlifysApiDocumentation from 'netlifys_api_documentation';
let defaultClient = NetlifysApiDocumentation.ApiClient.instance;
// Configure OAuth2 access token for authorization: netlifyAuth
let netlifyAuth = defaultClient.authentications['netlifyAuth'];
netlifyAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetlifysApiDocumentation.MemberApi();
let accountSlug = "accountSlug_example"; // String | 
let memberId = "memberId_example"; // String | 
apiInstance.getAccountMember(accountSlug, memberId, (error, data, response) => {
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
 **accountSlug** | **String**|  | 
 **memberId** | **String**|  | 

### Return type

[**Member**](Member.md)

### Authorization

[netlifyAuth](../README.md#netlifyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listMembersForAccount

> [Member] listMembersForAccount(accountSlug)



### Example

```javascript
import NetlifysApiDocumentation from 'netlifys_api_documentation';
let defaultClient = NetlifysApiDocumentation.ApiClient.instance;
// Configure OAuth2 access token for authorization: netlifyAuth
let netlifyAuth = defaultClient.authentications['netlifyAuth'];
netlifyAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetlifysApiDocumentation.MemberApi();
let accountSlug = "accountSlug_example"; // String | 
apiInstance.listMembersForAccount(accountSlug, (error, data, response) => {
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
 **accountSlug** | **String**|  | 

### Return type

[**[Member]**](Member.md)

### Authorization

[netlifyAuth](../README.md#netlifyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## removeAccountMember

> removeAccountMember(accountSlug, memberId)



### Example

```javascript
import NetlifysApiDocumentation from 'netlifys_api_documentation';
let defaultClient = NetlifysApiDocumentation.ApiClient.instance;
// Configure OAuth2 access token for authorization: netlifyAuth
let netlifyAuth = defaultClient.authentications['netlifyAuth'];
netlifyAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetlifysApiDocumentation.MemberApi();
let accountSlug = "accountSlug_example"; // String | 
let memberId = "memberId_example"; // String | 
apiInstance.removeAccountMember(accountSlug, memberId, (error, data, response) => {
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
 **accountSlug** | **String**|  | 
 **memberId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[netlifyAuth](../README.md#netlifyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateAccountMember

> Member updateAccountMember(accountSlug, memberId, accountUpdateMemberSetup)



### Example

```javascript
import NetlifysApiDocumentation from 'netlifys_api_documentation';
let defaultClient = NetlifysApiDocumentation.ApiClient.instance;
// Configure OAuth2 access token for authorization: netlifyAuth
let netlifyAuth = defaultClient.authentications['netlifyAuth'];
netlifyAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetlifysApiDocumentation.MemberApi();
let accountSlug = "accountSlug_example"; // String | 
let memberId = "memberId_example"; // String | 
let accountUpdateMemberSetup = new NetlifysApiDocumentation.AccountUpdateMemberSetup(); // AccountUpdateMemberSetup | 
apiInstance.updateAccountMember(accountSlug, memberId, accountUpdateMemberSetup, (error, data, response) => {
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
 **accountSlug** | **String**|  | 
 **memberId** | **String**|  | 
 **accountUpdateMemberSetup** | [**AccountUpdateMemberSetup**](AccountUpdateMemberSetup.md)|  | 

### Return type

[**Member**](Member.md)

### Authorization

[netlifyAuth](../README.md#netlifyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

