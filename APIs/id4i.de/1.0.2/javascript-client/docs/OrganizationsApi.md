# Id4iApi.OrganizationsApi

All URIs are relative to *http://backend.id4i.de*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addPartnerOrganization**](OrganizationsApi.md#addPartnerOrganization) | **PUT** /api/v1/organizations/{organizationId}/partner | Add partner
[**addUserRoles_0**](OrganizationsApi.md#addUserRoles_0) | **POST** /api/v1/organizations/{organizationId}/users/{username}/roles | Add role(s) to user
[**createOrganization**](OrganizationsApi.md#createOrganization) | **POST** /api/v1/organizations | Create organization
[**deleteOrganization**](OrganizationsApi.md#deleteOrganization) | **DELETE** /api/v1/organizations/{organizationId} | Delete organization
[**deleteOrganizationBillingAddress**](OrganizationsApi.md#deleteOrganizationBillingAddress) | **DELETE** /api/v1/organizations/{organizationId}/addresses/billing | Remove billing address
[**deleteOrganizationLogo**](OrganizationsApi.md#deleteOrganizationLogo) | **DELETE** /api/v1/organizations/{organizationId}/logo | Delete organization logo
[**findOrganization**](OrganizationsApi.md#findOrganization) | **GET** /api/v1/organizations/{organizationId} | Find organization by id/namespace
[**findOrganizationAddress**](OrganizationsApi.md#findOrganizationAddress) | **GET** /api/v1/organizations/{organizationId}/addresses/default | Retrieve address
[**findOrganizationBillingAddress**](OrganizationsApi.md#findOrganizationBillingAddress) | **GET** /api/v1/organizations/{organizationId}/addresses/billing | Retrieve billing address
[**getAllCollectionsOfOrganization_0**](OrganizationsApi.md#getAllCollectionsOfOrganization_0) | **GET** /api/v1/organizations/{organizationId}/collections | Get collections of organization
[**getAllOrganizationRoles_0**](OrganizationsApi.md#getAllOrganizationRoles_0) | **GET** /api/v1/organizations/{organizationId}/roles | List users and their roles
[**getOrganizationPrivileges**](OrganizationsApi.md#getOrganizationPrivileges) | **GET** /api/v1/organizations/{organizationId}/privileges | List my privileges
[**getOrganizationsOfUser_0**](OrganizationsApi.md#getOrganizationsOfUser_0) | **GET** /api/v1/user/organizations | Retrieve organizations of user
[**getPartnerOrganizations**](OrganizationsApi.md#getPartnerOrganizations) | **GET** /api/v1/organizations/{organizationId}/partner | Get partners of an organization
[**getUserRoles_0**](OrganizationsApi.md#getUserRoles_0) | **GET** /api/v1/organizations/{organizationId}/users/{username}/roles | Get user roles by username
[**getUsersOfOrganization_0**](OrganizationsApi.md#getUsersOfOrganization_0) | **GET** /api/v1/organizations/{organizationId}/users | Find users in organization
[**inviteUsers_0**](OrganizationsApi.md#inviteUsers_0) | **POST** /api/v1/organizations/{organizationId}/users/invite | Invite Users
[**listCountries**](OrganizationsApi.md#listCountries) | **GET** /api/v1/countries | List countries
[**removePartnerOrganization**](OrganizationsApi.md#removePartnerOrganization) | **DELETE** /api/v1/organizations/{organizationId}/partner | Remove partner
[**removeUserRoles_0**](OrganizationsApi.md#removeUserRoles_0) | **DELETE** /api/v1/organizations/{organizationId}/users/{username}/roles | Remove role(s) from user
[**setOrganizationLogo**](OrganizationsApi.md#setOrganizationLogo) | **POST** /api/v1/organizations/{organizationId}/logo | Update organization logo
[**updateOrganization**](OrganizationsApi.md#updateOrganization) | **PUT** /api/v1/organizations/{organizationId} | Update organization
[**updateOrganizationAddress**](OrganizationsApi.md#updateOrganizationAddress) | **PUT** /api/v1/organizations/{organizationId}/addresses/default | Store address
[**updateOrganizationBillingAddress**](OrganizationsApi.md#updateOrganizationBillingAddress) | **PUT** /api/v1/organizations/{organizationId}/addresses/billing | Store billing address



## addPartnerOrganization

> addPartnerOrganization(organizationId, addPartnerRequest)

Add partner

Adding a partner organization. If the given organization is already a partner the result will be state 200 too.

### Example

```javascript
import Id4iApi from 'id4i_api';
let defaultClient = Id4iApi.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new Id4iApi.OrganizationsApi();
let organizationId = "organizationId_example"; // String | The namespace of the organization
let addPartnerRequest = new Id4iApi.AddPartnerRequest(); // AddPartnerRequest | request
apiInstance.addPartnerOrganization(organizationId, addPartnerRequest, (error, data, response) => {
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
 **organizationId** | **String**| The namespace of the organization | 
 **addPartnerRequest** | [**AddPartnerRequest**](AddPartnerRequest.md)| request | 

### Return type

null (empty response body)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml


## addUserRoles_0

> addUserRoles_0(organizationId, username, changeRoleRequest)

Add role(s) to user

### Example

```javascript
import Id4iApi from 'id4i_api';
let defaultClient = Id4iApi.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new Id4iApi.OrganizationsApi();
let organizationId = "organizationId_example"; // String | The namespace of the organization
let username = "username_example"; // String | username
let changeRoleRequest = new Id4iApi.ChangeRoleRequest(); // ChangeRoleRequest | changeRoleRequest
apiInstance.addUserRoles_0(organizationId, username, changeRoleRequest, (error, data, response) => {
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
 **organizationId** | **String**| The namespace of the organization | 
 **username** | **String**| username | 
 **changeRoleRequest** | [**ChangeRoleRequest**](ChangeRoleRequest.md)| changeRoleRequest | 

### Return type

null (empty response body)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml


## createOrganization

> Organization createOrganization(organization)

Create organization

Creating a new organization.

### Example

```javascript
import Id4iApi from 'id4i_api';
let defaultClient = Id4iApi.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new Id4iApi.OrganizationsApi();
let organization = new Id4iApi.Organization(); // Organization | Organization to be created
apiInstance.createOrganization(organization, (error, data, response) => {
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
 **organization** | [**Organization**](Organization.md)| Organization to be created | 

### Return type

[**Organization**](Organization.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml


## deleteOrganization

> deleteOrganization(organizationId)

Delete organization

### Example

```javascript
import Id4iApi from 'id4i_api';
let defaultClient = Id4iApi.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new Id4iApi.OrganizationsApi();
let organizationId = "organizationId_example"; // String | The namespace of the organization to be deleted.
apiInstance.deleteOrganization(organizationId, (error, data, response) => {
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
 **organizationId** | **String**| The namespace of the organization to be deleted. | 

### Return type

null (empty response body)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## deleteOrganizationBillingAddress

> deleteOrganizationBillingAddress(organizationId)

Remove billing address

### Example

```javascript
import Id4iApi from 'id4i_api';
let defaultClient = Id4iApi.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new Id4iApi.OrganizationsApi();
let organizationId = "organizationId_example"; // String | organizationId
apiInstance.deleteOrganizationBillingAddress(organizationId, (error, data, response) => {
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
 **organizationId** | **String**| organizationId | 

### Return type

null (empty response body)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## deleteOrganizationLogo

> deleteOrganizationLogo(organizationId)

Delete organization logo

### Example

```javascript
import Id4iApi from 'id4i_api';
let defaultClient = Id4iApi.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new Id4iApi.OrganizationsApi();
let organizationId = "organizationId_example"; // String | The namespace of the organization where the logo should be deleted.
apiInstance.deleteOrganizationLogo(organizationId, (error, data, response) => {
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
 **organizationId** | **String**| The namespace of the organization where the logo should be deleted. | 

### Return type

null (empty response body)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## findOrganization

> Organization findOrganization(organizationId)

Find organization by id/namespace

Returns a single organization.

### Example

```javascript
import Id4iApi from 'id4i_api';
let defaultClient = Id4iApi.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new Id4iApi.OrganizationsApi();
let organizationId = "organizationId_example"; // String | The namespace of the organization to be retrieved.
apiInstance.findOrganization(organizationId, (error, data, response) => {
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
 **organizationId** | **String**| The namespace of the organization to be retrieved. | 

### Return type

[**Organization**](Organization.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## findOrganizationAddress

> OrganizationAddress findOrganizationAddress(organizationId)

Retrieve address

### Example

```javascript
import Id4iApi from 'id4i_api';
let defaultClient = Id4iApi.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new Id4iApi.OrganizationsApi();
let organizationId = "organizationId_example"; // String | organizationId
apiInstance.findOrganizationAddress(organizationId, (error, data, response) => {
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
 **organizationId** | **String**| organizationId | 

### Return type

[**OrganizationAddress**](OrganizationAddress.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## findOrganizationBillingAddress

> OrganizationAddress findOrganizationBillingAddress(organizationId)

Retrieve billing address

### Example

```javascript
import Id4iApi from 'id4i_api';
let defaultClient = Id4iApi.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new Id4iApi.OrganizationsApi();
let organizationId = "organizationId_example"; // String | organizationId
apiInstance.findOrganizationBillingAddress(organizationId, (error, data, response) => {
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
 **organizationId** | **String**| organizationId | 

### Return type

[**OrganizationAddress**](OrganizationAddress.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## getAllCollectionsOfOrganization_0

> PaginatedResponseOfGuidCollection getAllCollectionsOfOrganization_0(organizationId, opts)

Get collections of organization

Retrieving all collections of an organization in a paginated manner. You may filter the results by specifying id4n properties with filter operations (eq, in, ne) in the query parameters. e.g. &#x60;com.yourcompany.orderId.eq&#x3D;1234&#x60;  

### Example

```javascript
import Id4iApi from 'id4i_api';
let defaultClient = Id4iApi.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new Id4iApi.OrganizationsApi();
let organizationId = "organizationId_example"; // String | The namespace of the organization
let opts = {
  'offset': 56, // Number | Start with the n-th element
  'limit': 56, // Number | The maximum count of returned elements
  'type': "type_example", // String | Filter by this type
  'label': "label_example", // String | Filter by this label
  'labelPrefix': "labelPrefix_example", // String | Filter by this label prefix
  'property': ["null"] // [String] | List of i4dn property filter. e.g. \"com.myorga.state:IN:waiting|processing\" or \"com.myorga.orderId:EQ:SAP001\"
};
apiInstance.getAllCollectionsOfOrganization_0(organizationId, opts, (error, data, response) => {
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
 **organizationId** | **String**| The namespace of the organization | 
 **offset** | **Number**| Start with the n-th element | [optional] 
 **limit** | **Number**| The maximum count of returned elements | [optional] 
 **type** | **String**| Filter by this type | [optional] 
 **label** | **String**| Filter by this label | [optional] 
 **labelPrefix** | **String**| Filter by this label prefix | [optional] 
 **property** | [**[String]**](String.md)| List of i4dn property filter. e.g. \&quot;com.myorga.state:IN:waiting|processing\&quot; or \&quot;com.myorga.orderId:EQ:SAP001\&quot; | [optional] 

### Return type

[**PaginatedResponseOfGuidCollection**](PaginatedResponseOfGuidCollection.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## getAllOrganizationRoles_0

> PaginatedResponseOfUserRoles getAllOrganizationRoles_0(organizationId, opts)

List users and their roles

Listing users and their roles in a paginated manner.

### Example

```javascript
import Id4iApi from 'id4i_api';
let defaultClient = Id4iApi.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new Id4iApi.OrganizationsApi();
let organizationId = "organizationId_example"; // String | organizationId
let opts = {
  'offset': 56, // Number | Start with the n-th element
  'limit': 56 // Number | The maximum count of returned elements
};
apiInstance.getAllOrganizationRoles_0(organizationId, opts, (error, data, response) => {
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
 **organizationId** | **String**| organizationId | 
 **offset** | **Number**| Start with the n-th element | [optional] 
 **limit** | **Number**| The maximum count of returned elements | [optional] 

### Return type

[**PaginatedResponseOfUserRoles**](PaginatedResponseOfUserRoles.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## getOrganizationPrivileges

> [String] getOrganizationPrivileges(organizationId)

List my privileges

Listing all privileges of the current user/APIKey of the specified organization.

### Example

```javascript
import Id4iApi from 'id4i_api';
let defaultClient = Id4iApi.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new Id4iApi.OrganizationsApi();
let organizationId = "organizationId_example"; // String | The namespace of the organization
apiInstance.getOrganizationPrivileges(organizationId, (error, data, response) => {
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
 **organizationId** | **String**| The namespace of the organization | 

### Return type

**[String]**

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## getOrganizationsOfUser_0

> PaginatedResponseOfOrganization getOrganizationsOfUser_0(opts)

Retrieve organizations of user

### Example

```javascript
import Id4iApi from 'id4i_api';
let defaultClient = Id4iApi.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new Id4iApi.OrganizationsApi();
let opts = {
  'role': "role_example", // String | role
  'offset': 56, // Number | Start with the n-th element
  'limit': 56 // Number | The maximum count of returned elements
};
apiInstance.getOrganizationsOfUser_0(opts, (error, data, response) => {
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
 **role** | **String**| role | [optional] 
 **offset** | **Number**| Start with the n-th element | [optional] 
 **limit** | **Number**| The maximum count of returned elements | [optional] 

### Return type

[**PaginatedResponseOfOrganization**](PaginatedResponseOfOrganization.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## getPartnerOrganizations

> PaginatedResponseOfPartnerOrganization getPartnerOrganizations(organizationId, opts)

Get partners of an organization

Listing partners in a paginated manner.

### Example

```javascript
import Id4iApi from 'id4i_api';
let defaultClient = Id4iApi.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new Id4iApi.OrganizationsApi();
let organizationId = "organizationId_example"; // String | The namespace of the organization to query partner organizations
let opts = {
  'offset': 56, // Number | Start with the n-th element
  'limit': 56 // Number | The maximum count of returned elements
};
apiInstance.getPartnerOrganizations(organizationId, opts, (error, data, response) => {
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
 **organizationId** | **String**| The namespace of the organization to query partner organizations | 
 **offset** | **Number**| Start with the n-th element | [optional] 
 **limit** | **Number**| The maximum count of returned elements | [optional] 

### Return type

[**PaginatedResponseOfPartnerOrganization**](PaginatedResponseOfPartnerOrganization.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## getUserRoles_0

> PaginatedResponseOfstring getUserRoles_0(organizationId, username, opts)

Get user roles by username

### Example

```javascript
import Id4iApi from 'id4i_api';
let defaultClient = Id4iApi.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new Id4iApi.OrganizationsApi();
let organizationId = "organizationId_example"; // String | The namespace of the organization
let username = "username_example"; // String | username
let opts = {
  'offset': 56, // Number | Start with the n-th element
  'limit': 56 // Number | The maximum count of returned elements
};
apiInstance.getUserRoles_0(organizationId, username, opts, (error, data, response) => {
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
 **organizationId** | **String**| The namespace of the organization | 
 **username** | **String**| username | 
 **offset** | **Number**| Start with the n-th element | [optional] 
 **limit** | **Number**| The maximum count of returned elements | [optional] 

### Return type

[**PaginatedResponseOfstring**](PaginatedResponseOfstring.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## getUsersOfOrganization_0

> PaginatedResponseOfUserPresentation getUsersOfOrganization_0(organizationId, opts)

Find users in organization

Finding users in the specified organization in a paginated manner.

### Example

```javascript
import Id4iApi from 'id4i_api';
let defaultClient = Id4iApi.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new Id4iApi.OrganizationsApi();
let organizationId = "organizationId_example"; // String | organizationId
let opts = {
  'offset': 56, // Number | Start with the n-th element
  'limit': 56 // Number | The maximum count of returned elements
};
apiInstance.getUsersOfOrganization_0(organizationId, opts, (error, data, response) => {
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
 **organizationId** | **String**| organizationId | 
 **offset** | **Number**| Start with the n-th element | [optional] 
 **limit** | **Number**| The maximum count of returned elements | [optional] 

### Return type

[**PaginatedResponseOfUserPresentation**](PaginatedResponseOfUserPresentation.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## inviteUsers_0

> inviteUsers_0(organizationId, organizationUserInvitationListRequest)

Invite Users

### Example

```javascript
import Id4iApi from 'id4i_api';
let defaultClient = Id4iApi.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new Id4iApi.OrganizationsApi();
let organizationId = "organizationId_example"; // String | The namespace of the organization where users should be invited
let organizationUserInvitationListRequest = new Id4iApi.OrganizationUserInvitationListRequest(); // OrganizationUserInvitationListRequest | invitationList
apiInstance.inviteUsers_0(organizationId, organizationUserInvitationListRequest, (error, data, response) => {
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
 **organizationId** | **String**| The namespace of the organization where users should be invited | 
 **organizationUserInvitationListRequest** | [**OrganizationUserInvitationListRequest**](OrganizationUserInvitationListRequest.md)| invitationList | 

### Return type

null (empty response body)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml


## listCountries

> PaginatedResponseOfCountry listCountries(opts)

List countries

### Example

```javascript
import Id4iApi from 'id4i_api';
let defaultClient = Id4iApi.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new Id4iApi.OrganizationsApi();
let opts = {
  'offset': 56, // Number | Start with the n-th element
  'limit': 56 // Number | The maximum count of returned elements
};
apiInstance.listCountries(opts, (error, data, response) => {
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
 **offset** | **Number**| Start with the n-th element | [optional] 
 **limit** | **Number**| The maximum count of returned elements | [optional] 

### Return type

[**PaginatedResponseOfCountry**](PaginatedResponseOfCountry.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## removePartnerOrganization

> removePartnerOrganization(organizationId, removePartnerRequest)

Remove partner

Removing a partner organization

### Example

```javascript
import Id4iApi from 'id4i_api';
let defaultClient = Id4iApi.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new Id4iApi.OrganizationsApi();
let organizationId = "organizationId_example"; // String | The namespace of the organization
let removePartnerRequest = new Id4iApi.RemovePartnerRequest(); // RemovePartnerRequest | request
apiInstance.removePartnerOrganization(organizationId, removePartnerRequest, (error, data, response) => {
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
 **organizationId** | **String**| The namespace of the organization | 
 **removePartnerRequest** | [**RemovePartnerRequest**](RemovePartnerRequest.md)| request | 

### Return type

null (empty response body)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml


## removeUserRoles_0

> removeUserRoles_0(organizationId, username, changeRoleRequest)

Remove role(s) from user

### Example

```javascript
import Id4iApi from 'id4i_api';
let defaultClient = Id4iApi.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new Id4iApi.OrganizationsApi();
let organizationId = "organizationId_example"; // String | The namespace of the organization
let username = "username_example"; // String | username
let changeRoleRequest = new Id4iApi.ChangeRoleRequest(); // ChangeRoleRequest | changeRoleRequest
apiInstance.removeUserRoles_0(organizationId, username, changeRoleRequest, (error, data, response) => {
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
 **organizationId** | **String**| The namespace of the organization | 
 **username** | **String**| username | 
 **changeRoleRequest** | [**ChangeRoleRequest**](ChangeRoleRequest.md)| changeRoleRequest | 

### Return type

null (empty response body)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml


## setOrganizationLogo

> PublicImagePresentation setOrganizationLogo(organizationId, file)

Update organization logo

Updating an organization logo using a multipart file upload.

### Example

```javascript
import Id4iApi from 'id4i_api';
let defaultClient = Id4iApi.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new Id4iApi.OrganizationsApi();
let organizationId = "organizationId_example"; // String | The namespace of the organization where the logo should be updated.
let file = "/path/to/file"; // File | An image containing the new logo.
apiInstance.setOrganizationLogo(organizationId, file, (error, data, response) => {
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
 **organizationId** | **String**| The namespace of the organization where the logo should be updated. | 
 **file** | **File**| An image containing the new logo. | 

### Return type

[**PublicImagePresentation**](PublicImagePresentation.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json, application/xml


## updateOrganization

> Organization updateOrganization(organizationId, organizationUpdate)

Update organization

### Example

```javascript
import Id4iApi from 'id4i_api';
let defaultClient = Id4iApi.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new Id4iApi.OrganizationsApi();
let organizationId = "organizationId_example"; // String | The namespace of the organization to be updated.
let organizationUpdate = new Id4iApi.OrganizationUpdate(); // OrganizationUpdate | Updated organization object
apiInstance.updateOrganization(organizationId, organizationUpdate, (error, data, response) => {
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
 **organizationId** | **String**| The namespace of the organization to be updated. | 
 **organizationUpdate** | [**OrganizationUpdate**](OrganizationUpdate.md)| Updated organization object | 

### Return type

[**Organization**](Organization.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml


## updateOrganizationAddress

> OrganizationAddress updateOrganizationAddress(organizationId, organizationAddress)

Store address

### Example

```javascript
import Id4iApi from 'id4i_api';
let defaultClient = Id4iApi.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new Id4iApi.OrganizationsApi();
let organizationId = "organizationId_example"; // String | organizationId
let organizationAddress = new Id4iApi.OrganizationAddress(); // OrganizationAddress | addressResource
apiInstance.updateOrganizationAddress(organizationId, organizationAddress, (error, data, response) => {
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
 **organizationId** | **String**| organizationId | 
 **organizationAddress** | [**OrganizationAddress**](OrganizationAddress.md)| addressResource | 

### Return type

[**OrganizationAddress**](OrganizationAddress.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml


## updateOrganizationBillingAddress

> OrganizationAddress updateOrganizationBillingAddress(organizationId, organizationAddress)

Store billing address

### Example

```javascript
import Id4iApi from 'id4i_api';
let defaultClient = Id4iApi.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new Id4iApi.OrganizationsApi();
let organizationId = "organizationId_example"; // String | organizationId
let organizationAddress = new Id4iApi.OrganizationAddress(); // OrganizationAddress | addressResource
apiInstance.updateOrganizationBillingAddress(organizationId, organizationAddress, (error, data, response) => {
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
 **organizationId** | **String**| organizationId | 
 **organizationAddress** | [**OrganizationAddress**](OrganizationAddress.md)| addressResource | 

### Return type

[**OrganizationAddress**](OrganizationAddress.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml

