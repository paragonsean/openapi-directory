# BusinessRegistries.OrganisationsRolesApi

All URIs are relative to *http://api.abr.ato.gov.au*

Method | HTTP request | Description
------------- | ------------- | -------------
[**organisationsPartyIdRolesGet**](OrganisationsRolesApi.md#organisationsPartyIdRolesGet) | **GET** /organisations/{partyId}/roles | Retrieve a list of roles
[**organisationsPartyIdRolesPost**](OrganisationsRolesApi.md#organisationsPartyIdRolesPost) | **POST** /organisations/{partyId}/roles | Create a role
[**organisationsPartyIdRolesRoleIdDelete**](OrganisationsRolesApi.md#organisationsPartyIdRolesRoleIdDelete) | **DELETE** /organisations/{partyId}/roles/{roleId} | Delete a role
[**organisationsPartyIdRolesRoleIdGet**](OrganisationsRolesApi.md#organisationsPartyIdRolesRoleIdGet) | **GET** /organisations/{partyId}/roles/{roleId} | Retrieve a role
[**organisationsPartyIdRolesRoleIdPut**](OrganisationsRolesApi.md#organisationsPartyIdRolesRoleIdPut) | **PUT** /organisations/{partyId}/roles/{roleId} | Update a role



## organisationsPartyIdRolesGet

> [PartyRole] organisationsPartyIdRolesGet(apiKey, partyId)

Retrieve a list of roles

### Example

```javascript
import BusinessRegistries from 'business_registries';

let apiInstance = new BusinessRegistries.OrganisationsRolesApi();
let apiKey = "apiKey_example"; // String | The API key.
let partyId = "partyId_example"; // String | The party identifier.
apiInstance.organisationsPartyIdRolesGet(apiKey, partyId, (error, data, response) => {
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
 **apiKey** | **String**| The API key. | 
 **partyId** | **String**| The party identifier. | 

### Return type

[**[PartyRole]**](PartyRole.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## organisationsPartyIdRolesPost

> PartyRole organisationsPartyIdRolesPost(apiKey, partyId, partyRole)

Create a role

Create a role 

### Example

```javascript
import BusinessRegistries from 'business_registries';

let apiInstance = new BusinessRegistries.OrganisationsRolesApi();
let apiKey = "apiKey_example"; // String | The API key.
let partyId = "partyId_example"; // String | The party identifier.
let partyRole = new BusinessRegistries.PartyRole(); // PartyRole | Role resource
apiInstance.organisationsPartyIdRolesPost(apiKey, partyId, partyRole, (error, data, response) => {
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
 **apiKey** | **String**| The API key. | 
 **partyId** | **String**| The party identifier. | 
 **partyRole** | [**PartyRole**](PartyRole.md)| Role resource | 

### Return type

[**PartyRole**](PartyRole.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## organisationsPartyIdRolesRoleIdDelete

> organisationsPartyIdRolesRoleIdDelete(apiKey, partyId, roleId)

Delete a role

Delete a role 

### Example

```javascript
import BusinessRegistries from 'business_registries';

let apiInstance = new BusinessRegistries.OrganisationsRolesApi();
let apiKey = "apiKey_example"; // String | The API key.
let partyId = "partyId_example"; // String | The party identifier.
let roleId = "roleId_example"; // String | The role identifier.
apiInstance.organisationsPartyIdRolesRoleIdDelete(apiKey, partyId, roleId, (error, data, response) => {
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
 **apiKey** | **String**| The API key. | 
 **partyId** | **String**| The party identifier. | 
 **roleId** | **String**| The role identifier. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## organisationsPartyIdRolesRoleIdGet

> PartyRole organisationsPartyIdRolesRoleIdGet(apiKey, partyId, roleId)

Retrieve a role

Retrieve a role 

### Example

```javascript
import BusinessRegistries from 'business_registries';

let apiInstance = new BusinessRegistries.OrganisationsRolesApi();
let apiKey = "apiKey_example"; // String | The API key.
let partyId = "partyId_example"; // String | The party identifier.
let roleId = "roleId_example"; // String | The role identifier.
apiInstance.organisationsPartyIdRolesRoleIdGet(apiKey, partyId, roleId, (error, data, response) => {
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
 **apiKey** | **String**| The API key. | 
 **partyId** | **String**| The party identifier. | 
 **roleId** | **String**| The role identifier. | 

### Return type

[**PartyRole**](PartyRole.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## organisationsPartyIdRolesRoleIdPut

> PartyRole organisationsPartyIdRolesRoleIdPut(apiKey, partyId, roleId, partyRole)

Update a role

Update a role 

### Example

```javascript
import BusinessRegistries from 'business_registries';

let apiInstance = new BusinessRegistries.OrganisationsRolesApi();
let apiKey = "apiKey_example"; // String | The API key.
let partyId = "partyId_example"; // String | The party identifier.
let roleId = "roleId_example"; // String | The role identifier.
let partyRole = new BusinessRegistries.PartyRole(); // PartyRole | Role resource
apiInstance.organisationsPartyIdRolesRoleIdPut(apiKey, partyId, roleId, partyRole, (error, data, response) => {
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
 **apiKey** | **String**| The API key. | 
 **partyId** | **String**| The party identifier. | 
 **roleId** | **String**| The role identifier. | 
 **partyRole** | [**PartyRole**](PartyRole.md)| Role resource | 

### Return type

[**PartyRole**](PartyRole.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

