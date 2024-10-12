# BusinessRegistries.IndividualsRolesApi

All URIs are relative to *http://api.abr.ato.gov.au*

Method | HTTP request | Description
------------- | ------------- | -------------
[**individualsPartyIdRolesGet**](IndividualsRolesApi.md#individualsPartyIdRolesGet) | **GET** /individuals/{partyId}/roles | Retrieve a list of roles
[**individualsPartyIdRolesPost**](IndividualsRolesApi.md#individualsPartyIdRolesPost) | **POST** /individuals/{partyId}/roles | Create a role
[**individualsPartyIdRolesRoleIdDelete**](IndividualsRolesApi.md#individualsPartyIdRolesRoleIdDelete) | **DELETE** /individuals/{partyId}/roles/{roleId} | Delete a role
[**individualsPartyIdRolesRoleIdGet**](IndividualsRolesApi.md#individualsPartyIdRolesRoleIdGet) | **GET** /individuals/{partyId}/roles/{roleId} | Retrieve a role
[**individualsPartyIdRolesRoleIdPut**](IndividualsRolesApi.md#individualsPartyIdRolesRoleIdPut) | **PUT** /individuals/{partyId}/roles/{roleId} | Update a role



## individualsPartyIdRolesGet

> [PartyRole] individualsPartyIdRolesGet(apiKey, partyId)

Retrieve a list of roles

### Example

```javascript
import BusinessRegistries from 'business_registries';

let apiInstance = new BusinessRegistries.IndividualsRolesApi();
let apiKey = "apiKey_example"; // String | The API key.
let partyId = "partyId_example"; // String | The party identifier.
apiInstance.individualsPartyIdRolesGet(apiKey, partyId, (error, data, response) => {
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


## individualsPartyIdRolesPost

> PartyRole individualsPartyIdRolesPost(apiKey, partyId, partyRole)

Create a role

Create a role 

### Example

```javascript
import BusinessRegistries from 'business_registries';

let apiInstance = new BusinessRegistries.IndividualsRolesApi();
let apiKey = "apiKey_example"; // String | The API key.
let partyId = "partyId_example"; // String | The party identifier.
let partyRole = new BusinessRegistries.PartyRole(); // PartyRole | Role resource
apiInstance.individualsPartyIdRolesPost(apiKey, partyId, partyRole, (error, data, response) => {
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


## individualsPartyIdRolesRoleIdDelete

> individualsPartyIdRolesRoleIdDelete(apiKey, partyId, roleId)

Delete a role

Delete a role 

### Example

```javascript
import BusinessRegistries from 'business_registries';

let apiInstance = new BusinessRegistries.IndividualsRolesApi();
let apiKey = "apiKey_example"; // String | The API key.
let partyId = "partyId_example"; // String | The party identifier.
let roleId = "roleId_example"; // String | The role identifier.
apiInstance.individualsPartyIdRolesRoleIdDelete(apiKey, partyId, roleId, (error, data, response) => {
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


## individualsPartyIdRolesRoleIdGet

> PartyRole individualsPartyIdRolesRoleIdGet(apiKey, partyId, roleId)

Retrieve a role

Retrieve a role 

### Example

```javascript
import BusinessRegistries from 'business_registries';

let apiInstance = new BusinessRegistries.IndividualsRolesApi();
let apiKey = "apiKey_example"; // String | The API key.
let partyId = "partyId_example"; // String | The party identifier.
let roleId = "roleId_example"; // String | The role identifier.
apiInstance.individualsPartyIdRolesRoleIdGet(apiKey, partyId, roleId, (error, data, response) => {
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


## individualsPartyIdRolesRoleIdPut

> PartyRole individualsPartyIdRolesRoleIdPut(apiKey, partyId, roleId, partyRole)

Update a role

Update a role 

### Example

```javascript
import BusinessRegistries from 'business_registries';

let apiInstance = new BusinessRegistries.IndividualsRolesApi();
let apiKey = "apiKey_example"; // String | The API key.
let partyId = "partyId_example"; // String | The party identifier.
let roleId = "roleId_example"; // String | The role identifier.
let partyRole = new BusinessRegistries.PartyRole(); // PartyRole | Role resource
apiInstance.individualsPartyIdRolesRoleIdPut(apiKey, partyId, roleId, partyRole, (error, data, response) => {
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

