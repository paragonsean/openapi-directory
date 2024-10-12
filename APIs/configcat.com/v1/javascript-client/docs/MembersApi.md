# ConfigCatPublicManagementApi.MembersApi

All URIs are relative to *https://api.configcat.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addMemberToGroup**](MembersApi.md#addMemberToGroup) | **POST** /v1/organizations/{organizationId}/members/{userId} | Update Member Permissions
[**deleteOrganizationMember**](MembersApi.md#deleteOrganizationMember) | **DELETE** /v1/organizations/{organizationId}/members/{userId} | Delete Member from Organization
[**deleteProductMember**](MembersApi.md#deleteProductMember) | **DELETE** /v1/products/{productId}/members/{userId} | Delete Member from Product
[**getOrganizationMembers**](MembersApi.md#getOrganizationMembers) | **GET** /v1/organizations/{organizationId}/members | List Organization Members
[**getProductMembers**](MembersApi.md#getProductMembers) | **GET** /v1/products/{productId}/members | List Product Members
[**inviteMember**](MembersApi.md#inviteMember) | **POST** /v1/products/{productId}/members/invite | Invite Member



## addMemberToGroup

> addMemberToGroup(organizationId, userId, addUserToGroupRequest)

Update Member Permissions

This endpoint adds a Member identified by the &#x60;userId&#x60; to one or more Permission Groups.  This endpoint can also be used to move a Member between Permission Groups within a Product. Only a single Permission Group can be set per Product.

### Example

```javascript
import ConfigCatPublicManagementApi from 'config_cat_public_management_api';
let defaultClient = ConfigCatPublicManagementApi.ApiClient.instance;
// Configure HTTP basic authorization: Basic
let Basic = defaultClient.authentications['Basic'];
Basic.username = 'YOUR USERNAME';
Basic.password = 'YOUR PASSWORD';

let apiInstance = new ConfigCatPublicManagementApi.MembersApi();
let organizationId = "organizationId_example"; // String | The identifier of the Organization.
let userId = "userId_example"; // String | The identifier of the Member.
let addUserToGroupRequest = new ConfigCatPublicManagementApi.AddUserToGroupRequest(); // AddUserToGroupRequest | 
apiInstance.addMemberToGroup(organizationId, userId, addUserToGroupRequest, (error, data, response) => {
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
 **organizationId** | **String**| The identifier of the Organization. | 
 **userId** | **String**| The identifier of the Member. | 
 **addUserToGroupRequest** | [**AddUserToGroupRequest**](AddUserToGroupRequest.md)|  | 

### Return type

null (empty response body)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

- **Content-Type**: application/*+json, application/json, text/json
- **Accept**: Not defined


## deleteOrganizationMember

> deleteOrganizationMember(organizationId, userId)

Delete Member from Organization

This endpoint removes a Member identified by the &#x60;userId&#x60; from the  given Organization identified by the &#x60;organizationId&#x60; parameter.

### Example

```javascript
import ConfigCatPublicManagementApi from 'config_cat_public_management_api';
let defaultClient = ConfigCatPublicManagementApi.ApiClient.instance;
// Configure HTTP basic authorization: Basic
let Basic = defaultClient.authentications['Basic'];
Basic.username = 'YOUR USERNAME';
Basic.password = 'YOUR PASSWORD';

let apiInstance = new ConfigCatPublicManagementApi.MembersApi();
let organizationId = "organizationId_example"; // String | The identifier of the Organization.
let userId = "userId_example"; // String | The identifier of the Member.
apiInstance.deleteOrganizationMember(organizationId, userId, (error, data, response) => {
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
 **organizationId** | **String**| The identifier of the Organization. | 
 **userId** | **String**| The identifier of the Member. | 

### Return type

null (empty response body)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteProductMember

> deleteProductMember(productId, userId)

Delete Member from Product

This endpoint removes a Member identified by the &#x60;userId&#x60; from the  given Product identified by the &#x60;productId&#x60; parameter.

### Example

```javascript
import ConfigCatPublicManagementApi from 'config_cat_public_management_api';
let defaultClient = ConfigCatPublicManagementApi.ApiClient.instance;
// Configure HTTP basic authorization: Basic
let Basic = defaultClient.authentications['Basic'];
Basic.username = 'YOUR USERNAME';
Basic.password = 'YOUR PASSWORD';

let apiInstance = new ConfigCatPublicManagementApi.MembersApi();
let productId = "productId_example"; // String | The identifier of the Product.
let userId = "userId_example"; // String | The identifier of the Member.
apiInstance.deleteProductMember(productId, userId, (error, data, response) => {
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
 **productId** | **String**| The identifier of the Product. | 
 **userId** | **String**| The identifier of the Member. | 

### Return type

null (empty response body)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getOrganizationMembers

> [UserModel] getOrganizationMembers(organizationId)

List Organization Members

This endpoint returns the list of Members that belongs  to the given Organization, identified by the &#x60;organizationId&#x60; parameter.

### Example

```javascript
import ConfigCatPublicManagementApi from 'config_cat_public_management_api';
let defaultClient = ConfigCatPublicManagementApi.ApiClient.instance;
// Configure HTTP basic authorization: Basic
let Basic = defaultClient.authentications['Basic'];
Basic.username = 'YOUR USERNAME';
Basic.password = 'YOUR PASSWORD';

let apiInstance = new ConfigCatPublicManagementApi.MembersApi();
let organizationId = "organizationId_example"; // String | The identifier of the Organization.
apiInstance.getOrganizationMembers(organizationId, (error, data, response) => {
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
 **organizationId** | **String**| The identifier of the Organization. | 

### Return type

[**[UserModel]**](UserModel.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/hal+json, application/json


## getProductMembers

> [MemberModel] getProductMembers(productId)

List Product Members

This endpoint returns the list of Members that belongs  to the given Product, identified by the &#x60;productId&#x60; parameter.

### Example

```javascript
import ConfigCatPublicManagementApi from 'config_cat_public_management_api';
let defaultClient = ConfigCatPublicManagementApi.ApiClient.instance;
// Configure HTTP basic authorization: Basic
let Basic = defaultClient.authentications['Basic'];
Basic.username = 'YOUR USERNAME';
Basic.password = 'YOUR PASSWORD';

let apiInstance = new ConfigCatPublicManagementApi.MembersApi();
let productId = "productId_example"; // String | The identifier of the Product.
apiInstance.getProductMembers(productId, (error, data, response) => {
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
 **productId** | **String**| The identifier of the Product. | 

### Return type

[**[MemberModel]**](MemberModel.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/hal+json, application/json


## inviteMember

> inviteMember(productId, inviteMembersRequest)

Invite Member

This endpoint invites a Member into the given Product identified by the &#x60;productId&#x60; parameter.

### Example

```javascript
import ConfigCatPublicManagementApi from 'config_cat_public_management_api';
let defaultClient = ConfigCatPublicManagementApi.ApiClient.instance;
// Configure HTTP basic authorization: Basic
let Basic = defaultClient.authentications['Basic'];
Basic.username = 'YOUR USERNAME';
Basic.password = 'YOUR PASSWORD';

let apiInstance = new ConfigCatPublicManagementApi.MembersApi();
let productId = "productId_example"; // String | The identifier of the Product.
let inviteMembersRequest = new ConfigCatPublicManagementApi.InviteMembersRequest(); // InviteMembersRequest | 
apiInstance.inviteMember(productId, inviteMembersRequest, (error, data, response) => {
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
 **productId** | **String**| The identifier of the Product. | 
 **inviteMembersRequest** | [**InviteMembersRequest**](InviteMembersRequest.md)|  | 

### Return type

null (empty response body)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

- **Content-Type**: application/*+json, application/json, text/json
- **Accept**: Not defined

