# KeycloakAdminRestApi.ClientsApi

All URIs are relative to *http://keycloak.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**realmClientsGet**](ClientsApi.md#realmClientsGet) | **GET** /{realm}/clients | Get clients belonging to the realm   Returns a list of clients belonging to the realm
[**realmClientsIdClientSecretGet**](ClientsApi.md#realmClientsIdClientSecretGet) | **GET** /{realm}/clients/{id}/client-secret | Get the client secret
[**realmClientsIdClientSecretPost**](ClientsApi.md#realmClientsIdClientSecretPost) | **POST** /{realm}/clients/{id}/client-secret | Generate a new secret for the client
[**realmClientsIdDefaultClientScopesClientScopeIdDelete**](ClientsApi.md#realmClientsIdDefaultClientScopesClientScopeIdDelete) | **DELETE** /{realm}/clients/{id}/default-client-scopes/{clientScopeId} | 
[**realmClientsIdDefaultClientScopesClientScopeIdPut**](ClientsApi.md#realmClientsIdDefaultClientScopesClientScopeIdPut) | **PUT** /{realm}/clients/{id}/default-client-scopes/{clientScopeId} | 
[**realmClientsIdDefaultClientScopesGet**](ClientsApi.md#realmClientsIdDefaultClientScopesGet) | **GET** /{realm}/clients/{id}/default-client-scopes | Get default client scopes.
[**realmClientsIdDelete**](ClientsApi.md#realmClientsIdDelete) | **DELETE** /{realm}/clients/{id} | Delete the client
[**realmClientsIdEvaluateScopesGenerateExampleAccessTokenGet**](ClientsApi.md#realmClientsIdEvaluateScopesGenerateExampleAccessTokenGet) | **GET** /{realm}/clients/{id}/evaluate-scopes/generate-example-access-token | Create JSON with payload of example access token
[**realmClientsIdEvaluateScopesProtocolMappersGet**](ClientsApi.md#realmClientsIdEvaluateScopesProtocolMappersGet) | **GET** /{realm}/clients/{id}/evaluate-scopes/protocol-mappers | Return list of all protocol mappers, which will be used when generating tokens issued for particular client.
[**realmClientsIdEvaluateScopesScopeMappingsRoleContainerIdGrantedGet**](ClientsApi.md#realmClientsIdEvaluateScopesScopeMappingsRoleContainerIdGrantedGet) | **GET** /{realm}/clients/{id}/evaluate-scopes/scope-mappings/{roleContainerId}/granted | Get effective scope mapping of all roles of particular role container, which this client is defacto allowed to have in the accessToken issued for him.
[**realmClientsIdEvaluateScopesScopeMappingsRoleContainerIdNotGrantedGet**](ClientsApi.md#realmClientsIdEvaluateScopesScopeMappingsRoleContainerIdNotGrantedGet) | **GET** /{realm}/clients/{id}/evaluate-scopes/scope-mappings/{roleContainerId}/not-granted | Get roles, which this client doesn’t have scope for and can’t have them in the accessToken issued for him.
[**realmClientsIdGet**](ClientsApi.md#realmClientsIdGet) | **GET** /{realm}/clients/{id} | Get representation of the client
[**realmClientsIdInstallationProvidersProviderIdGet**](ClientsApi.md#realmClientsIdInstallationProvidersProviderIdGet) | **GET** /{realm}/clients/{id}/installation/providers/{providerId} | 
[**realmClientsIdManagementPermissionsGet**](ClientsApi.md#realmClientsIdManagementPermissionsGet) | **GET** /{realm}/clients/{id}/management/permissions | Return object stating whether client Authorization permissions have been initialized or not and a reference
[**realmClientsIdManagementPermissionsPut**](ClientsApi.md#realmClientsIdManagementPermissionsPut) | **PUT** /{realm}/clients/{id}/management/permissions | Return object stating whether client Authorization permissions have been initialized or not and a reference
[**realmClientsIdNodesNodeDelete**](ClientsApi.md#realmClientsIdNodesNodeDelete) | **DELETE** /{realm}/clients/{id}/nodes/{node} | Unregister a cluster node from the client
[**realmClientsIdNodesPost**](ClientsApi.md#realmClientsIdNodesPost) | **POST** /{realm}/clients/{id}/nodes | Register a cluster node with the client   Manually register cluster node to this client - usually it’s not needed to call this directly as adapter should handle  by sending registration request to Keycloak
[**realmClientsIdOfflineSessionCountGet**](ClientsApi.md#realmClientsIdOfflineSessionCountGet) | **GET** /{realm}/clients/{id}/offline-session-count | Get application offline session count   Returns a number of offline user sessions associated with this client   {      \&quot;count\&quot;: number  }
[**realmClientsIdOfflineSessionsGet**](ClientsApi.md#realmClientsIdOfflineSessionsGet) | **GET** /{realm}/clients/{id}/offline-sessions | Get offline sessions for client   Returns a list of offline user sessions associated with this client
[**realmClientsIdOptionalClientScopesClientScopeIdDelete**](ClientsApi.md#realmClientsIdOptionalClientScopesClientScopeIdDelete) | **DELETE** /{realm}/clients/{id}/optional-client-scopes/{clientScopeId} | 
[**realmClientsIdOptionalClientScopesClientScopeIdPut**](ClientsApi.md#realmClientsIdOptionalClientScopesClientScopeIdPut) | **PUT** /{realm}/clients/{id}/optional-client-scopes/{clientScopeId} | 
[**realmClientsIdOptionalClientScopesGet**](ClientsApi.md#realmClientsIdOptionalClientScopesGet) | **GET** /{realm}/clients/{id}/optional-client-scopes | Get optional client scopes.
[**realmClientsIdPushRevocationPost**](ClientsApi.md#realmClientsIdPushRevocationPost) | **POST** /{realm}/clients/{id}/push-revocation | Push the client’s revocation policy to its admin URL   If the client has an admin URL, push revocation policy to it.
[**realmClientsIdPut**](ClientsApi.md#realmClientsIdPut) | **PUT** /{realm}/clients/{id} | Update the client
[**realmClientsIdRegistrationAccessTokenPost**](ClientsApi.md#realmClientsIdRegistrationAccessTokenPost) | **POST** /{realm}/clients/{id}/registration-access-token | Generate a new registration access token for the client
[**realmClientsIdServiceAccountUserGet**](ClientsApi.md#realmClientsIdServiceAccountUserGet) | **GET** /{realm}/clients/{id}/service-account-user | Get a user dedicated to the service account
[**realmClientsIdSessionCountGet**](ClientsApi.md#realmClientsIdSessionCountGet) | **GET** /{realm}/clients/{id}/session-count | Get application session count   Returns a number of user sessions associated with this client   {      \&quot;count\&quot;: number  }
[**realmClientsIdTestNodesAvailableGet**](ClientsApi.md#realmClientsIdTestNodesAvailableGet) | **GET** /{realm}/clients/{id}/test-nodes-available | Test if registered cluster nodes are available   Tests availability by sending &#39;ping&#39; request to all cluster nodes.
[**realmClientsIdUserSessionsGet**](ClientsApi.md#realmClientsIdUserSessionsGet) | **GET** /{realm}/clients/{id}/user-sessions | Get user sessions for client   Returns a list of user sessions associated with this client
[**realmClientsPost**](ClientsApi.md#realmClientsPost) | **POST** /{realm}/clients | Create a new client   Client’s client_id must be unique!



## realmClientsGet

> [ClientRepresentation] realmClientsGet(realm, opts)

Get clients belonging to the realm   Returns a list of clients belonging to the realm

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.ClientsApi();
let realm = "realm_example"; // String | realm name (not id!)
let opts = {
  'clientId': "clientId_example", // String | filter by clientId
  'first': 56, // Number | the first result
  'max': 56, // Number | the max results to return
  'search': true, // Boolean | whether this is a search query or a getClientById query
  'viewableOnly': true // Boolean | filter clients that cannot be viewed in full by admin
};
apiInstance.realmClientsGet(realm, opts, (error, data, response) => {
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
 **clientId** | **String**| filter by clientId | [optional] 
 **first** | **Number**| the first result | [optional] 
 **max** | **Number**| the max results to return | [optional] 
 **search** | **Boolean**| whether this is a search query or a getClientById query | [optional] 
 **viewableOnly** | **Boolean**| filter clients that cannot be viewed in full by admin | [optional] 

### Return type

[**[ClientRepresentation]**](ClientRepresentation.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## realmClientsIdClientSecretGet

> CredentialRepresentation realmClientsIdClientSecretGet(realm, id)

Get the client secret

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.ClientsApi();
let realm = "realm_example"; // String | realm name (not id!)
let id = "id_example"; // String | id of client (not client-id)
apiInstance.realmClientsIdClientSecretGet(realm, id, (error, data, response) => {
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
 **id** | **String**| id of client (not client-id) | 

### Return type

[**CredentialRepresentation**](CredentialRepresentation.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## realmClientsIdClientSecretPost

> CredentialRepresentation realmClientsIdClientSecretPost(realm, id)

Generate a new secret for the client

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.ClientsApi();
let realm = "realm_example"; // String | realm name (not id!)
let id = "id_example"; // String | id of client (not client-id)
apiInstance.realmClientsIdClientSecretPost(realm, id, (error, data, response) => {
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
 **id** | **String**| id of client (not client-id) | 

### Return type

[**CredentialRepresentation**](CredentialRepresentation.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## realmClientsIdDefaultClientScopesClientScopeIdDelete

> realmClientsIdDefaultClientScopesClientScopeIdDelete(realm, id, clientScopeId)



### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.ClientsApi();
let realm = "realm_example"; // String | realm name (not id!)
let id = "id_example"; // String | id of client (not client-id)
let clientScopeId = "clientScopeId_example"; // String | 
apiInstance.realmClientsIdDefaultClientScopesClientScopeIdDelete(realm, id, clientScopeId, (error, data, response) => {
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
 **id** | **String**| id of client (not client-id) | 
 **clientScopeId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## realmClientsIdDefaultClientScopesClientScopeIdPut

> realmClientsIdDefaultClientScopesClientScopeIdPut(realm, id, clientScopeId)



### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.ClientsApi();
let realm = "realm_example"; // String | realm name (not id!)
let id = "id_example"; // String | id of client (not client-id)
let clientScopeId = "clientScopeId_example"; // String | 
apiInstance.realmClientsIdDefaultClientScopesClientScopeIdPut(realm, id, clientScopeId, (error, data, response) => {
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
 **id** | **String**| id of client (not client-id) | 
 **clientScopeId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## realmClientsIdDefaultClientScopesGet

> [ClientScopeRepresentation] realmClientsIdDefaultClientScopesGet(realm, id)

Get default client scopes.

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.ClientsApi();
let realm = "realm_example"; // String | realm name (not id!)
let id = "id_example"; // String | id of client (not client-id)
apiInstance.realmClientsIdDefaultClientScopesGet(realm, id, (error, data, response) => {
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
 **id** | **String**| id of client (not client-id) | 

### Return type

[**[ClientScopeRepresentation]**](ClientScopeRepresentation.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## realmClientsIdDelete

> realmClientsIdDelete(realm, id)

Delete the client

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.ClientsApi();
let realm = "realm_example"; // String | realm name (not id!)
let id = "id_example"; // String | id of client (not client-id)
apiInstance.realmClientsIdDelete(realm, id, (error, data, response) => {
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
 **id** | **String**| id of client (not client-id) | 

### Return type

null (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## realmClientsIdEvaluateScopesGenerateExampleAccessTokenGet

> AccessToken realmClientsIdEvaluateScopesGenerateExampleAccessTokenGet(realm, id, opts)

Create JSON with payload of example access token

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.ClientsApi();
let realm = "realm_example"; // String | realm name (not id!)
let id = "id_example"; // String | id of client (not client-id)
let opts = {
  'scope': "scope_example", // String | 
  'userId': "userId_example" // String | 
};
apiInstance.realmClientsIdEvaluateScopesGenerateExampleAccessTokenGet(realm, id, opts, (error, data, response) => {
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
 **id** | **String**| id of client (not client-id) | 
 **scope** | **String**|  | [optional] 
 **userId** | **String**|  | [optional] 

### Return type

[**AccessToken**](AccessToken.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## realmClientsIdEvaluateScopesProtocolMappersGet

> [ClientScopeEvaluateResourceProtocolMapperEvaluationRepresentation] realmClientsIdEvaluateScopesProtocolMappersGet(realm, id, opts)

Return list of all protocol mappers, which will be used when generating tokens issued for particular client.

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.ClientsApi();
let realm = "realm_example"; // String | realm name (not id!)
let id = "id_example"; // String | id of client (not client-id)
let opts = {
  'scope': "scope_example" // String | 
};
apiInstance.realmClientsIdEvaluateScopesProtocolMappersGet(realm, id, opts, (error, data, response) => {
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
 **id** | **String**| id of client (not client-id) | 
 **scope** | **String**|  | [optional] 

### Return type

[**[ClientScopeEvaluateResourceProtocolMapperEvaluationRepresentation]**](ClientScopeEvaluateResourceProtocolMapperEvaluationRepresentation.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## realmClientsIdEvaluateScopesScopeMappingsRoleContainerIdGrantedGet

> [RoleRepresentation] realmClientsIdEvaluateScopesScopeMappingsRoleContainerIdGrantedGet(realm, id, roleContainerId, opts)

Get effective scope mapping of all roles of particular role container, which this client is defacto allowed to have in the accessToken issued for him.

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.ClientsApi();
let realm = "realm_example"; // String | realm name (not id!)
let id = "id_example"; // String | id of client (not client-id)
let roleContainerId = "roleContainerId_example"; // String | either realm name OR client UUID
let opts = {
  'scope': "scope_example" // String | 
};
apiInstance.realmClientsIdEvaluateScopesScopeMappingsRoleContainerIdGrantedGet(realm, id, roleContainerId, opts, (error, data, response) => {
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
 **id** | **String**| id of client (not client-id) | 
 **roleContainerId** | **String**| either realm name OR client UUID | 
 **scope** | **String**|  | [optional] 

### Return type

[**[RoleRepresentation]**](RoleRepresentation.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## realmClientsIdEvaluateScopesScopeMappingsRoleContainerIdNotGrantedGet

> [RoleRepresentation] realmClientsIdEvaluateScopesScopeMappingsRoleContainerIdNotGrantedGet(realm, id, roleContainerId, opts)

Get roles, which this client doesn’t have scope for and can’t have them in the accessToken issued for him.

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.ClientsApi();
let realm = "realm_example"; // String | realm name (not id!)
let id = "id_example"; // String | id of client (not client-id)
let roleContainerId = "roleContainerId_example"; // String | either realm name OR client UUID
let opts = {
  'scope': "scope_example" // String | 
};
apiInstance.realmClientsIdEvaluateScopesScopeMappingsRoleContainerIdNotGrantedGet(realm, id, roleContainerId, opts, (error, data, response) => {
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
 **id** | **String**| id of client (not client-id) | 
 **roleContainerId** | **String**| either realm name OR client UUID | 
 **scope** | **String**|  | [optional] 

### Return type

[**[RoleRepresentation]**](RoleRepresentation.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## realmClientsIdGet

> ClientRepresentation realmClientsIdGet(realm, id)

Get representation of the client

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.ClientsApi();
let realm = "realm_example"; // String | realm name (not id!)
let id = "id_example"; // String | id of client (not client-id)
apiInstance.realmClientsIdGet(realm, id, (error, data, response) => {
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
 **id** | **String**| id of client (not client-id) | 

### Return type

[**ClientRepresentation**](ClientRepresentation.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## realmClientsIdInstallationProvidersProviderIdGet

> realmClientsIdInstallationProvidersProviderIdGet(realm, id, providerId)



### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.ClientsApi();
let realm = "realm_example"; // String | realm name (not id!)
let id = "id_example"; // String | id of client (not client-id)
let providerId = "providerId_example"; // String | 
apiInstance.realmClientsIdInstallationProvidersProviderIdGet(realm, id, providerId, (error, data, response) => {
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
 **id** | **String**| id of client (not client-id) | 
 **providerId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## realmClientsIdManagementPermissionsGet

> ManagementPermissionReference realmClientsIdManagementPermissionsGet(realm, id)

Return object stating whether client Authorization permissions have been initialized or not and a reference

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.ClientsApi();
let realm = "realm_example"; // String | realm name (not id!)
let id = "id_example"; // String | id of client (not client-id)
apiInstance.realmClientsIdManagementPermissionsGet(realm, id, (error, data, response) => {
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
 **id** | **String**| id of client (not client-id) | 

### Return type

[**ManagementPermissionReference**](ManagementPermissionReference.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## realmClientsIdManagementPermissionsPut

> ManagementPermissionReference realmClientsIdManagementPermissionsPut(realm, id, managementPermissionReference)

Return object stating whether client Authorization permissions have been initialized or not and a reference

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.ClientsApi();
let realm = "realm_example"; // String | realm name (not id!)
let id = "id_example"; // String | id of client (not client-id)
let managementPermissionReference = new KeycloakAdminRestApi.ManagementPermissionReference(); // ManagementPermissionReference | 
apiInstance.realmClientsIdManagementPermissionsPut(realm, id, managementPermissionReference, (error, data, response) => {
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
 **id** | **String**| id of client (not client-id) | 
 **managementPermissionReference** | [**ManagementPermissionReference**](ManagementPermissionReference.md)|  | 

### Return type

[**ManagementPermissionReference**](ManagementPermissionReference.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## realmClientsIdNodesNodeDelete

> realmClientsIdNodesNodeDelete(realm, id, node)

Unregister a cluster node from the client

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.ClientsApi();
let realm = "realm_example"; // String | realm name (not id!)
let id = "id_example"; // String | id of client (not client-id)
let node = "node_example"; // String | 
apiInstance.realmClientsIdNodesNodeDelete(realm, id, node, (error, data, response) => {
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
 **id** | **String**| id of client (not client-id) | 
 **node** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## realmClientsIdNodesPost

> realmClientsIdNodesPost(realm, id, requestBody)

Register a cluster node with the client   Manually register cluster node to this client - usually it’s not needed to call this directly as adapter should handle  by sending registration request to Keycloak

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.ClientsApi();
let realm = "realm_example"; // String | realm name (not id!)
let id = "id_example"; // String | id of client (not client-id)
let requestBody = {key: null}; // {String: Object} | 
apiInstance.realmClientsIdNodesPost(realm, id, requestBody, (error, data, response) => {
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
 **id** | **String**| id of client (not client-id) | 
 **requestBody** | [**{String: Object}**](Object.md)|  | 

### Return type

null (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## realmClientsIdOfflineSessionCountGet

> {String: Object} realmClientsIdOfflineSessionCountGet(realm, id)

Get application offline session count   Returns a number of offline user sessions associated with this client   {      \&quot;count\&quot;: number  }

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.ClientsApi();
let realm = "realm_example"; // String | realm name (not id!)
let id = "id_example"; // String | id of client (not client-id)
apiInstance.realmClientsIdOfflineSessionCountGet(realm, id, (error, data, response) => {
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
 **id** | **String**| id of client (not client-id) | 

### Return type

**{String: Object}**

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## realmClientsIdOfflineSessionsGet

> [UserSessionRepresentation] realmClientsIdOfflineSessionsGet(realm, id, opts)

Get offline sessions for client   Returns a list of offline user sessions associated with this client

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.ClientsApi();
let realm = "realm_example"; // String | realm name (not id!)
let id = "id_example"; // String | id of client (not client-id)
let opts = {
  'first': 56, // Number | Paging offset
  'max': 56 // Number | Maximum results size (defaults to 100)
};
apiInstance.realmClientsIdOfflineSessionsGet(realm, id, opts, (error, data, response) => {
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
 **id** | **String**| id of client (not client-id) | 
 **first** | **Number**| Paging offset | [optional] 
 **max** | **Number**| Maximum results size (defaults to 100) | [optional] 

### Return type

[**[UserSessionRepresentation]**](UserSessionRepresentation.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## realmClientsIdOptionalClientScopesClientScopeIdDelete

> realmClientsIdOptionalClientScopesClientScopeIdDelete(realm, id, clientScopeId)



### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.ClientsApi();
let realm = "realm_example"; // String | realm name (not id!)
let id = "id_example"; // String | id of client (not client-id)
let clientScopeId = "clientScopeId_example"; // String | 
apiInstance.realmClientsIdOptionalClientScopesClientScopeIdDelete(realm, id, clientScopeId, (error, data, response) => {
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
 **id** | **String**| id of client (not client-id) | 
 **clientScopeId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## realmClientsIdOptionalClientScopesClientScopeIdPut

> realmClientsIdOptionalClientScopesClientScopeIdPut(realm, id, clientScopeId)



### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.ClientsApi();
let realm = "realm_example"; // String | realm name (not id!)
let id = "id_example"; // String | id of client (not client-id)
let clientScopeId = "clientScopeId_example"; // String | 
apiInstance.realmClientsIdOptionalClientScopesClientScopeIdPut(realm, id, clientScopeId, (error, data, response) => {
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
 **id** | **String**| id of client (not client-id) | 
 **clientScopeId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## realmClientsIdOptionalClientScopesGet

> [ClientScopeRepresentation] realmClientsIdOptionalClientScopesGet(realm, id)

Get optional client scopes.

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.ClientsApi();
let realm = "realm_example"; // String | realm name (not id!)
let id = "id_example"; // String | id of client (not client-id)
apiInstance.realmClientsIdOptionalClientScopesGet(realm, id, (error, data, response) => {
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
 **id** | **String**| id of client (not client-id) | 

### Return type

[**[ClientScopeRepresentation]**](ClientScopeRepresentation.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## realmClientsIdPushRevocationPost

> GlobalRequestResult realmClientsIdPushRevocationPost(realm, id)

Push the client’s revocation policy to its admin URL   If the client has an admin URL, push revocation policy to it.

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.ClientsApi();
let realm = "realm_example"; // String | realm name (not id!)
let id = "id_example"; // String | id of client (not client-id)
apiInstance.realmClientsIdPushRevocationPost(realm, id, (error, data, response) => {
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
 **id** | **String**| id of client (not client-id) | 

### Return type

[**GlobalRequestResult**](GlobalRequestResult.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## realmClientsIdPut

> realmClientsIdPut(realm, id, clientRepresentation)

Update the client

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.ClientsApi();
let realm = "realm_example"; // String | realm name (not id!)
let id = "id_example"; // String | id of client (not client-id)
let clientRepresentation = new KeycloakAdminRestApi.ClientRepresentation(); // ClientRepresentation | 
apiInstance.realmClientsIdPut(realm, id, clientRepresentation, (error, data, response) => {
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
 **id** | **String**| id of client (not client-id) | 
 **clientRepresentation** | [**ClientRepresentation**](ClientRepresentation.md)|  | 

### Return type

null (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## realmClientsIdRegistrationAccessTokenPost

> ClientRepresentation realmClientsIdRegistrationAccessTokenPost(realm, id)

Generate a new registration access token for the client

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.ClientsApi();
let realm = "realm_example"; // String | realm name (not id!)
let id = "id_example"; // String | id of client (not client-id)
apiInstance.realmClientsIdRegistrationAccessTokenPost(realm, id, (error, data, response) => {
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
 **id** | **String**| id of client (not client-id) | 

### Return type

[**ClientRepresentation**](ClientRepresentation.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## realmClientsIdServiceAccountUserGet

> UserRepresentation realmClientsIdServiceAccountUserGet(realm, id)

Get a user dedicated to the service account

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.ClientsApi();
let realm = "realm_example"; // String | realm name (not id!)
let id = "id_example"; // String | id of client (not client-id)
apiInstance.realmClientsIdServiceAccountUserGet(realm, id, (error, data, response) => {
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
 **id** | **String**| id of client (not client-id) | 

### Return type

[**UserRepresentation**](UserRepresentation.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## realmClientsIdSessionCountGet

> {String: Object} realmClientsIdSessionCountGet(realm, id)

Get application session count   Returns a number of user sessions associated with this client   {      \&quot;count\&quot;: number  }

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.ClientsApi();
let realm = "realm_example"; // String | realm name (not id!)
let id = "id_example"; // String | id of client (not client-id)
apiInstance.realmClientsIdSessionCountGet(realm, id, (error, data, response) => {
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
 **id** | **String**| id of client (not client-id) | 

### Return type

**{String: Object}**

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## realmClientsIdTestNodesAvailableGet

> GlobalRequestResult realmClientsIdTestNodesAvailableGet(realm, id)

Test if registered cluster nodes are available   Tests availability by sending &#39;ping&#39; request to all cluster nodes.

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.ClientsApi();
let realm = "realm_example"; // String | realm name (not id!)
let id = "id_example"; // String | id of client (not client-id)
apiInstance.realmClientsIdTestNodesAvailableGet(realm, id, (error, data, response) => {
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
 **id** | **String**| id of client (not client-id) | 

### Return type

[**GlobalRequestResult**](GlobalRequestResult.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## realmClientsIdUserSessionsGet

> [UserSessionRepresentation] realmClientsIdUserSessionsGet(realm, id, opts)

Get user sessions for client   Returns a list of user sessions associated with this client

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.ClientsApi();
let realm = "realm_example"; // String | realm name (not id!)
let id = "id_example"; // String | id of client (not client-id)
let opts = {
  'first': 56, // Number | Paging offset
  'max': 56 // Number | Maximum results size (defaults to 100)
};
apiInstance.realmClientsIdUserSessionsGet(realm, id, opts, (error, data, response) => {
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
 **id** | **String**| id of client (not client-id) | 
 **first** | **Number**| Paging offset | [optional] 
 **max** | **Number**| Maximum results size (defaults to 100) | [optional] 

### Return type

[**[UserSessionRepresentation]**](UserSessionRepresentation.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## realmClientsPost

> realmClientsPost(realm, clientRepresentation)

Create a new client   Client’s client_id must be unique!

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.ClientsApi();
let realm = "realm_example"; // String | realm name (not id!)
let clientRepresentation = new KeycloakAdminRestApi.ClientRepresentation(); // ClientRepresentation | 
apiInstance.realmClientsPost(realm, clientRepresentation, (error, data, response) => {
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
 **clientRepresentation** | [**ClientRepresentation**](ClientRepresentation.md)|  | 

### Return type

null (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

