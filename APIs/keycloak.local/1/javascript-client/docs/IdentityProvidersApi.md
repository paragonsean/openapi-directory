# KeycloakAdminRestApi.IdentityProvidersApi

All URIs are relative to *http://keycloak.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**realmIdentityProviderImportConfigPost**](IdentityProvidersApi.md#realmIdentityProviderImportConfigPost) | **POST** /{realm}/identity-provider/import-config | Import identity provider from uploaded JSON file
[**realmIdentityProviderInstancesAliasDelete**](IdentityProvidersApi.md#realmIdentityProviderInstancesAliasDelete) | **DELETE** /{realm}/identity-provider/instances/{alias} | Delete the identity provider
[**realmIdentityProviderInstancesAliasExportGet**](IdentityProvidersApi.md#realmIdentityProviderInstancesAliasExportGet) | **GET** /{realm}/identity-provider/instances/{alias}/export | Export public broker configuration for identity provider
[**realmIdentityProviderInstancesAliasGet**](IdentityProvidersApi.md#realmIdentityProviderInstancesAliasGet) | **GET** /{realm}/identity-provider/instances/{alias} | Get the identity provider
[**realmIdentityProviderInstancesAliasManagementPermissionsGet**](IdentityProvidersApi.md#realmIdentityProviderInstancesAliasManagementPermissionsGet) | **GET** /{realm}/identity-provider/instances/{alias}/management/permissions | Return object stating whether client Authorization permissions have been initialized or not and a reference
[**realmIdentityProviderInstancesAliasManagementPermissionsPut**](IdentityProvidersApi.md#realmIdentityProviderInstancesAliasManagementPermissionsPut) | **PUT** /{realm}/identity-provider/instances/{alias}/management/permissions | Return object stating whether client Authorization permissions have been initialized or not and a reference
[**realmIdentityProviderInstancesAliasMapperTypesGet**](IdentityProvidersApi.md#realmIdentityProviderInstancesAliasMapperTypesGet) | **GET** /{realm}/identity-provider/instances/{alias}/mapper-types | Get mapper types for identity provider
[**realmIdentityProviderInstancesAliasMappersGet**](IdentityProvidersApi.md#realmIdentityProviderInstancesAliasMappersGet) | **GET** /{realm}/identity-provider/instances/{alias}/mappers | Get mappers for identity provider
[**realmIdentityProviderInstancesAliasMappersIdDelete**](IdentityProvidersApi.md#realmIdentityProviderInstancesAliasMappersIdDelete) | **DELETE** /{realm}/identity-provider/instances/{alias}/mappers/{id} | Delete a mapper for the identity provider
[**realmIdentityProviderInstancesAliasMappersIdGet**](IdentityProvidersApi.md#realmIdentityProviderInstancesAliasMappersIdGet) | **GET** /{realm}/identity-provider/instances/{alias}/mappers/{id} | Get mapper by id for the identity provider
[**realmIdentityProviderInstancesAliasMappersIdPut**](IdentityProvidersApi.md#realmIdentityProviderInstancesAliasMappersIdPut) | **PUT** /{realm}/identity-provider/instances/{alias}/mappers/{id} | Update a mapper for the identity provider
[**realmIdentityProviderInstancesAliasMappersPost**](IdentityProvidersApi.md#realmIdentityProviderInstancesAliasMappersPost) | **POST** /{realm}/identity-provider/instances/{alias}/mappers | Add a mapper to identity provider
[**realmIdentityProviderInstancesAliasPut**](IdentityProvidersApi.md#realmIdentityProviderInstancesAliasPut) | **PUT** /{realm}/identity-provider/instances/{alias} | Update the identity provider
[**realmIdentityProviderInstancesGet**](IdentityProvidersApi.md#realmIdentityProviderInstancesGet) | **GET** /{realm}/identity-provider/instances | Get identity providers
[**realmIdentityProviderInstancesPost**](IdentityProvidersApi.md#realmIdentityProviderInstancesPost) | **POST** /{realm}/identity-provider/instances | Create a new identity provider
[**realmIdentityProviderProvidersProviderIdGet**](IdentityProvidersApi.md#realmIdentityProviderProvidersProviderIdGet) | **GET** /{realm}/identity-provider/providers/{provider_id} | Get identity providers



## realmIdentityProviderImportConfigPost

> {String: Object} realmIdentityProviderImportConfigPost(realm)

Import identity provider from uploaded JSON file

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.IdentityProvidersApi();
let realm = "realm_example"; // String | realm name (not id!)
apiInstance.realmIdentityProviderImportConfigPost(realm, (error, data, response) => {
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
 **realm** | **String**| realm name (not id!) | 

### Return type

**{String: Object}**

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## realmIdentityProviderInstancesAliasDelete

> realmIdentityProviderInstancesAliasDelete(realm, alias)

Delete the identity provider

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.IdentityProvidersApi();
let realm = "realm_example"; // String | realm name (not id!)
let alias = "alias_example"; // String | 
apiInstance.realmIdentityProviderInstancesAliasDelete(realm, alias, (error, data, response) => {
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
 **realm** | **String**| realm name (not id!) | 
 **alias** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## realmIdentityProviderInstancesAliasExportGet

> realmIdentityProviderInstancesAliasExportGet(realm, alias, opts)

Export public broker configuration for identity provider

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.IdentityProvidersApi();
let realm = "realm_example"; // String | realm name (not id!)
let alias = "alias_example"; // String | 
let opts = {
  'format': "format_example" // String | Format to use
};
apiInstance.realmIdentityProviderInstancesAliasExportGet(realm, alias, opts, (error, data, response) => {
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
 **realm** | **String**| realm name (not id!) | 
 **alias** | **String**|  | 
 **format** | **String**| Format to use | [optional] 

### Return type

null (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## realmIdentityProviderInstancesAliasGet

> IdentityProviderRepresentation realmIdentityProviderInstancesAliasGet(realm, alias)

Get the identity provider

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.IdentityProvidersApi();
let realm = "realm_example"; // String | realm name (not id!)
let alias = "alias_example"; // String | 
apiInstance.realmIdentityProviderInstancesAliasGet(realm, alias, (error, data, response) => {
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
 **realm** | **String**| realm name (not id!) | 
 **alias** | **String**|  | 

### Return type

[**IdentityProviderRepresentation**](IdentityProviderRepresentation.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## realmIdentityProviderInstancesAliasManagementPermissionsGet

> ManagementPermissionReference realmIdentityProviderInstancesAliasManagementPermissionsGet(realm, alias)

Return object stating whether client Authorization permissions have been initialized or not and a reference

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.IdentityProvidersApi();
let realm = "realm_example"; // String | realm name (not id!)
let alias = "alias_example"; // String | 
apiInstance.realmIdentityProviderInstancesAliasManagementPermissionsGet(realm, alias, (error, data, response) => {
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
 **realm** | **String**| realm name (not id!) | 
 **alias** | **String**|  | 

### Return type

[**ManagementPermissionReference**](ManagementPermissionReference.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## realmIdentityProviderInstancesAliasManagementPermissionsPut

> ManagementPermissionReference realmIdentityProviderInstancesAliasManagementPermissionsPut(realm, alias, managementPermissionReference)

Return object stating whether client Authorization permissions have been initialized or not and a reference

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.IdentityProvidersApi();
let realm = "realm_example"; // String | realm name (not id!)
let alias = "alias_example"; // String | 
let managementPermissionReference = new KeycloakAdminRestApi.ManagementPermissionReference(); // ManagementPermissionReference | 
apiInstance.realmIdentityProviderInstancesAliasManagementPermissionsPut(realm, alias, managementPermissionReference, (error, data, response) => {
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
 **realm** | **String**| realm name (not id!) | 
 **alias** | **String**|  | 
 **managementPermissionReference** | [**ManagementPermissionReference**](ManagementPermissionReference.md)|  | 

### Return type

[**ManagementPermissionReference**](ManagementPermissionReference.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## realmIdentityProviderInstancesAliasMapperTypesGet

> realmIdentityProviderInstancesAliasMapperTypesGet(realm, alias)

Get mapper types for identity provider

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.IdentityProvidersApi();
let realm = "realm_example"; // String | realm name (not id!)
let alias = "alias_example"; // String | 
apiInstance.realmIdentityProviderInstancesAliasMapperTypesGet(realm, alias, (error, data, response) => {
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
 **realm** | **String**| realm name (not id!) | 
 **alias** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## realmIdentityProviderInstancesAliasMappersGet

> [IdentityProviderMapperRepresentation] realmIdentityProviderInstancesAliasMappersGet(realm, alias)

Get mappers for identity provider

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.IdentityProvidersApi();
let realm = "realm_example"; // String | realm name (not id!)
let alias = "alias_example"; // String | 
apiInstance.realmIdentityProviderInstancesAliasMappersGet(realm, alias, (error, data, response) => {
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
 **realm** | **String**| realm name (not id!) | 
 **alias** | **String**|  | 

### Return type

[**[IdentityProviderMapperRepresentation]**](IdentityProviderMapperRepresentation.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## realmIdentityProviderInstancesAliasMappersIdDelete

> realmIdentityProviderInstancesAliasMappersIdDelete(realm, alias, id)

Delete a mapper for the identity provider

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.IdentityProvidersApi();
let realm = "realm_example"; // String | realm name (not id!)
let alias = "alias_example"; // String | 
let id = "id_example"; // String | Mapper id
apiInstance.realmIdentityProviderInstancesAliasMappersIdDelete(realm, alias, id, (error, data, response) => {
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
 **realm** | **String**| realm name (not id!) | 
 **alias** | **String**|  | 
 **id** | **String**| Mapper id | 

### Return type

null (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## realmIdentityProviderInstancesAliasMappersIdGet

> IdentityProviderMapperRepresentation realmIdentityProviderInstancesAliasMappersIdGet(realm, alias, id)

Get mapper by id for the identity provider

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.IdentityProvidersApi();
let realm = "realm_example"; // String | realm name (not id!)
let alias = "alias_example"; // String | 
let id = "id_example"; // String | Mapper id
apiInstance.realmIdentityProviderInstancesAliasMappersIdGet(realm, alias, id, (error, data, response) => {
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
 **realm** | **String**| realm name (not id!) | 
 **alias** | **String**|  | 
 **id** | **String**| Mapper id | 

### Return type

[**IdentityProviderMapperRepresentation**](IdentityProviderMapperRepresentation.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## realmIdentityProviderInstancesAliasMappersIdPut

> realmIdentityProviderInstancesAliasMappersIdPut(realm, alias, id, identityProviderMapperRepresentation)

Update a mapper for the identity provider

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.IdentityProvidersApi();
let realm = "realm_example"; // String | realm name (not id!)
let alias = "alias_example"; // String | 
let id = "id_example"; // String | Mapper id
let identityProviderMapperRepresentation = new KeycloakAdminRestApi.IdentityProviderMapperRepresentation(); // IdentityProviderMapperRepresentation | 
apiInstance.realmIdentityProviderInstancesAliasMappersIdPut(realm, alias, id, identityProviderMapperRepresentation, (error, data, response) => {
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
 **realm** | **String**| realm name (not id!) | 
 **alias** | **String**|  | 
 **id** | **String**| Mapper id | 
 **identityProviderMapperRepresentation** | [**IdentityProviderMapperRepresentation**](IdentityProviderMapperRepresentation.md)|  | 

### Return type

null (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## realmIdentityProviderInstancesAliasMappersPost

> realmIdentityProviderInstancesAliasMappersPost(realm, alias, identityProviderMapperRepresentation)

Add a mapper to identity provider

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.IdentityProvidersApi();
let realm = "realm_example"; // String | realm name (not id!)
let alias = "alias_example"; // String | 
let identityProviderMapperRepresentation = new KeycloakAdminRestApi.IdentityProviderMapperRepresentation(); // IdentityProviderMapperRepresentation | 
apiInstance.realmIdentityProviderInstancesAliasMappersPost(realm, alias, identityProviderMapperRepresentation, (error, data, response) => {
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
 **realm** | **String**| realm name (not id!) | 
 **alias** | **String**|  | 
 **identityProviderMapperRepresentation** | [**IdentityProviderMapperRepresentation**](IdentityProviderMapperRepresentation.md)|  | 

### Return type

null (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## realmIdentityProviderInstancesAliasPut

> realmIdentityProviderInstancesAliasPut(realm, alias, identityProviderRepresentation)

Update the identity provider

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.IdentityProvidersApi();
let realm = "realm_example"; // String | realm name (not id!)
let alias = "alias_example"; // String | 
let identityProviderRepresentation = new KeycloakAdminRestApi.IdentityProviderRepresentation(); // IdentityProviderRepresentation | 
apiInstance.realmIdentityProviderInstancesAliasPut(realm, alias, identityProviderRepresentation, (error, data, response) => {
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
 **realm** | **String**| realm name (not id!) | 
 **alias** | **String**|  | 
 **identityProviderRepresentation** | [**IdentityProviderRepresentation**](IdentityProviderRepresentation.md)|  | 

### Return type

null (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## realmIdentityProviderInstancesGet

> [IdentityProviderRepresentation] realmIdentityProviderInstancesGet(realm)

Get identity providers

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.IdentityProvidersApi();
let realm = "realm_example"; // String | realm name (not id!)
apiInstance.realmIdentityProviderInstancesGet(realm, (error, data, response) => {
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
 **realm** | **String**| realm name (not id!) | 

### Return type

[**[IdentityProviderRepresentation]**](IdentityProviderRepresentation.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## realmIdentityProviderInstancesPost

> realmIdentityProviderInstancesPost(realm, identityProviderRepresentation)

Create a new identity provider

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.IdentityProvidersApi();
let realm = "realm_example"; // String | realm name (not id!)
let identityProviderRepresentation = new KeycloakAdminRestApi.IdentityProviderRepresentation(); // IdentityProviderRepresentation | JSON body
apiInstance.realmIdentityProviderInstancesPost(realm, identityProviderRepresentation, (error, data, response) => {
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
 **realm** | **String**| realm name (not id!) | 
 **identityProviderRepresentation** | [**IdentityProviderRepresentation**](IdentityProviderRepresentation.md)| JSON body | 

### Return type

null (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## realmIdentityProviderProvidersProviderIdGet

> realmIdentityProviderProvidersProviderIdGet(realm, providerId)

Get identity providers

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.IdentityProvidersApi();
let realm = "realm_example"; // String | realm name (not id!)
let providerId = "providerId_example"; // String | Provider id
apiInstance.realmIdentityProviderProvidersProviderIdGet(realm, providerId, (error, data, response) => {
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
 **realm** | **String**| realm name (not id!) | 
 **providerId** | **String**| Provider id | 

### Return type

null (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

