# KeycloakAdminRestApi.RealmsAdminApi

All URIs are relative to *http://keycloak.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**realmAdminEventsDelete**](RealmsAdminApi.md#realmAdminEventsDelete) | **DELETE** /{realm}/admin-events | Delete all admin events
[**realmAdminEventsGet**](RealmsAdminApi.md#realmAdminEventsGet) | **GET** /{realm}/admin-events | Get admin events   Returns all admin events, or filters events based on URL query parameters listed here
[**realmClearKeysCachePost**](RealmsAdminApi.md#realmClearKeysCachePost) | **POST** /{realm}/clear-keys-cache | Clear cache of external public keys (Public keys of clients or Identity providers)
[**realmClearRealmCachePost**](RealmsAdminApi.md#realmClearRealmCachePost) | **POST** /{realm}/clear-realm-cache | Clear realm cache
[**realmClearUserCachePost**](RealmsAdminApi.md#realmClearUserCachePost) | **POST** /{realm}/clear-user-cache | Clear user cache
[**realmClientDescriptionConverterPost**](RealmsAdminApi.md#realmClientDescriptionConverterPost) | **POST** /{realm}/client-description-converter | Base path for importing clients under this realm.
[**realmClientSessionStatsGet**](RealmsAdminApi.md#realmClientSessionStatsGet) | **GET** /{realm}/client-session-stats | Get client session stats   Returns a JSON map.
[**realmCredentialRegistratorsGet**](RealmsAdminApi.md#realmCredentialRegistratorsGet) | **GET** /{realm}/credential-registrators | 
[**realmDefaultDefaultClientScopesClientScopeIdDelete**](RealmsAdminApi.md#realmDefaultDefaultClientScopesClientScopeIdDelete) | **DELETE** /{realm}/default-default-client-scopes/{clientScopeId} | 
[**realmDefaultDefaultClientScopesClientScopeIdPut**](RealmsAdminApi.md#realmDefaultDefaultClientScopesClientScopeIdPut) | **PUT** /{realm}/default-default-client-scopes/{clientScopeId} | 
[**realmDefaultDefaultClientScopesGet**](RealmsAdminApi.md#realmDefaultDefaultClientScopesGet) | **GET** /{realm}/default-default-client-scopes | Get realm default client scopes.
[**realmDefaultGroupsGet**](RealmsAdminApi.md#realmDefaultGroupsGet) | **GET** /{realm}/default-groups | Get group hierarchy.
[**realmDefaultGroupsGroupIdDelete**](RealmsAdminApi.md#realmDefaultGroupsGroupIdDelete) | **DELETE** /{realm}/default-groups/{groupId} | 
[**realmDefaultGroupsGroupIdPut**](RealmsAdminApi.md#realmDefaultGroupsGroupIdPut) | **PUT** /{realm}/default-groups/{groupId} | 
[**realmDefaultOptionalClientScopesClientScopeIdDelete**](RealmsAdminApi.md#realmDefaultOptionalClientScopesClientScopeIdDelete) | **DELETE** /{realm}/default-optional-client-scopes/{clientScopeId} | 
[**realmDefaultOptionalClientScopesClientScopeIdPut**](RealmsAdminApi.md#realmDefaultOptionalClientScopesClientScopeIdPut) | **PUT** /{realm}/default-optional-client-scopes/{clientScopeId} | 
[**realmDefaultOptionalClientScopesGet**](RealmsAdminApi.md#realmDefaultOptionalClientScopesGet) | **GET** /{realm}/default-optional-client-scopes | Get realm optional client scopes.
[**realmDelete**](RealmsAdminApi.md#realmDelete) | **DELETE** /{realm} | Delete the realm
[**realmEventsConfigGet**](RealmsAdminApi.md#realmEventsConfigGet) | **GET** /{realm}/events/config | Get the events provider configuration   Returns JSON object with events provider configuration
[**realmEventsConfigPut**](RealmsAdminApi.md#realmEventsConfigPut) | **PUT** /{realm}/events/config | Update the events provider   Change the events provider and/or its configuration
[**realmEventsDelete**](RealmsAdminApi.md#realmEventsDelete) | **DELETE** /{realm}/events | Delete all events
[**realmEventsGet**](RealmsAdminApi.md#realmEventsGet) | **GET** /{realm}/events | Get events   Returns all events, or filters them based on URL query parameters listed here
[**realmGet**](RealmsAdminApi.md#realmGet) | **GET** /{realm} | Get the top-level representation of the realm   It will not include nested information like User and Client representations.
[**realmGroupByPathPathGet**](RealmsAdminApi.md#realmGroupByPathPathGet) | **GET** /{realm}/group-by-path/{path} | 
[**realmLogoutAllPost**](RealmsAdminApi.md#realmLogoutAllPost) | **POST** /{realm}/logout-all | Removes all user sessions.
[**realmPartialExportPost**](RealmsAdminApi.md#realmPartialExportPost) | **POST** /{realm}/partial-export | Partial export of existing realm into a JSON file.
[**realmPartialImportPost**](RealmsAdminApi.md#realmPartialImportPost) | **POST** /{realm}/partialImport | Partial import from a JSON file to an existing realm.
[**realmPushRevocationPost**](RealmsAdminApi.md#realmPushRevocationPost) | **POST** /{realm}/push-revocation | Push the realm’s revocation policy to any client that has an admin url associated with it.
[**realmPut**](RealmsAdminApi.md#realmPut) | **PUT** /{realm} | Update the top-level information of the realm   Any user, roles or client information in the representation  will be ignored.
[**realmSessionsSessionDelete**](RealmsAdminApi.md#realmSessionsSessionDelete) | **DELETE** /{realm}/sessions/{session} | Remove a specific user session.
[**realmTestLDAPConnectionPost**](RealmsAdminApi.md#realmTestLDAPConnectionPost) | **POST** /{realm}/testLDAPConnection | Test LDAP connection
[**realmTestSMTPConnectionPost**](RealmsAdminApi.md#realmTestSMTPConnectionPost) | **POST** /{realm}/testSMTPConnection | 
[**realmUsersManagementPermissionsGet**](RealmsAdminApi.md#realmUsersManagementPermissionsGet) | **GET** /{realm}/users-management-permissions | 
[**realmUsersManagementPermissionsPut**](RealmsAdminApi.md#realmUsersManagementPermissionsPut) | **PUT** /{realm}/users-management-permissions | 
[**rootPost**](RealmsAdminApi.md#rootPost) | **POST** / | Import a realm   Imports a realm from a full representation of that realm.



## realmAdminEventsDelete

> realmAdminEventsDelete(realm)

Delete all admin events

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.RealmsAdminApi();
let realm = "realm_example"; // String | realm name (not id!)
apiInstance.realmAdminEventsDelete(realm, (error, data, response) => {
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

### Return type

null (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## realmAdminEventsGet

> [AdminEventRepresentation] realmAdminEventsGet(realm, opts)

Get admin events   Returns all admin events, or filters events based on URL query parameters listed here

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.RealmsAdminApi();
let realm = "realm_example"; // String | realm name (not id!)
let opts = {
  'authClient': "authClient_example", // String | 
  'authIpAddress': "authIpAddress_example", // String | 
  'authRealm': "authRealm_example", // String | 
  'authUser': "authUser_example", // String | user id
  'dateFrom': "dateFrom_example", // String | 
  'dateTo': "dateTo_example", // String | 
  'first': 56, // Number | 
  'max': 56, // Number | Maximum results size (defaults to 100)
  'operationTypes': ["null"], // [String] | 
  'resourcePath': "resourcePath_example", // String | 
  'resourceTypes': ["null"] // [String] | 
};
apiInstance.realmAdminEventsGet(realm, opts, (error, data, response) => {
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
 **authClient** | **String**|  | [optional] 
 **authIpAddress** | **String**|  | [optional] 
 **authRealm** | **String**|  | [optional] 
 **authUser** | **String**| user id | [optional] 
 **dateFrom** | **String**|  | [optional] 
 **dateTo** | **String**|  | [optional] 
 **first** | **Number**|  | [optional] 
 **max** | **Number**| Maximum results size (defaults to 100) | [optional] 
 **operationTypes** | [**[String]**](String.md)|  | [optional] 
 **resourcePath** | **String**|  | [optional] 
 **resourceTypes** | [**[String]**](String.md)|  | [optional] 

### Return type

[**[AdminEventRepresentation]**](AdminEventRepresentation.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## realmClearKeysCachePost

> realmClearKeysCachePost(realm)

Clear cache of external public keys (Public keys of clients or Identity providers)

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.RealmsAdminApi();
let realm = "realm_example"; // String | realm name (not id!)
apiInstance.realmClearKeysCachePost(realm, (error, data, response) => {
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

### Return type

null (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## realmClearRealmCachePost

> realmClearRealmCachePost(realm)

Clear realm cache

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.RealmsAdminApi();
let realm = "realm_example"; // String | realm name (not id!)
apiInstance.realmClearRealmCachePost(realm, (error, data, response) => {
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

### Return type

null (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## realmClearUserCachePost

> realmClearUserCachePost(realm)

Clear user cache

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.RealmsAdminApi();
let realm = "realm_example"; // String | realm name (not id!)
apiInstance.realmClearUserCachePost(realm, (error, data, response) => {
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

### Return type

null (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## realmClientDescriptionConverterPost

> ClientRepresentation realmClientDescriptionConverterPost(realm, body)

Base path for importing clients under this realm.

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.RealmsAdminApi();
let realm = "realm_example"; // String | realm name (not id!)
let body = "body_example"; // String | 
apiInstance.realmClientDescriptionConverterPost(realm, body, (error, data, response) => {
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
 **body** | **String**|  | 

### Return type

[**ClientRepresentation**](ClientRepresentation.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: text/plain
- **Accept**: application/json


## realmClientSessionStatsGet

> [{String: Object}] realmClientSessionStatsGet(realm)

Get client session stats   Returns a JSON map.

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.RealmsAdminApi();
let realm = "realm_example"; // String | realm name (not id!)
apiInstance.realmClientSessionStatsGet(realm, (error, data, response) => {
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

**[{String: Object}]**

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## realmCredentialRegistratorsGet

> [String] realmCredentialRegistratorsGet(realm)



### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.RealmsAdminApi();
let realm = "realm_example"; // String | realm name (not id!)
apiInstance.realmCredentialRegistratorsGet(realm, (error, data, response) => {
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

**[String]**

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## realmDefaultDefaultClientScopesClientScopeIdDelete

> realmDefaultDefaultClientScopesClientScopeIdDelete(realm, clientScopeId)



### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.RealmsAdminApi();
let realm = "realm_example"; // String | realm name (not id!)
let clientScopeId = "clientScopeId_example"; // String | 
apiInstance.realmDefaultDefaultClientScopesClientScopeIdDelete(realm, clientScopeId, (error, data, response) => {
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
 **clientScopeId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## realmDefaultDefaultClientScopesClientScopeIdPut

> realmDefaultDefaultClientScopesClientScopeIdPut(realm, clientScopeId)



### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.RealmsAdminApi();
let realm = "realm_example"; // String | realm name (not id!)
let clientScopeId = "clientScopeId_example"; // String | 
apiInstance.realmDefaultDefaultClientScopesClientScopeIdPut(realm, clientScopeId, (error, data, response) => {
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
 **clientScopeId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## realmDefaultDefaultClientScopesGet

> [ClientScopeRepresentation] realmDefaultDefaultClientScopesGet(realm)

Get realm default client scopes.

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.RealmsAdminApi();
let realm = "realm_example"; // String | realm name (not id!)
apiInstance.realmDefaultDefaultClientScopesGet(realm, (error, data, response) => {
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

[**[ClientScopeRepresentation]**](ClientScopeRepresentation.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## realmDefaultGroupsGet

> [GroupRepresentation] realmDefaultGroupsGet(realm)

Get group hierarchy.

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.RealmsAdminApi();
let realm = "realm_example"; // String | realm name (not id!)
apiInstance.realmDefaultGroupsGet(realm, (error, data, response) => {
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

[**[GroupRepresentation]**](GroupRepresentation.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## realmDefaultGroupsGroupIdDelete

> realmDefaultGroupsGroupIdDelete(realm, groupId)



### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.RealmsAdminApi();
let realm = "realm_example"; // String | realm name (not id!)
let groupId = "groupId_example"; // String | 
apiInstance.realmDefaultGroupsGroupIdDelete(realm, groupId, (error, data, response) => {
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
 **groupId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## realmDefaultGroupsGroupIdPut

> realmDefaultGroupsGroupIdPut(realm, groupId)



### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.RealmsAdminApi();
let realm = "realm_example"; // String | realm name (not id!)
let groupId = "groupId_example"; // String | 
apiInstance.realmDefaultGroupsGroupIdPut(realm, groupId, (error, data, response) => {
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
 **groupId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## realmDefaultOptionalClientScopesClientScopeIdDelete

> realmDefaultOptionalClientScopesClientScopeIdDelete(realm, clientScopeId)



### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.RealmsAdminApi();
let realm = "realm_example"; // String | realm name (not id!)
let clientScopeId = "clientScopeId_example"; // String | 
apiInstance.realmDefaultOptionalClientScopesClientScopeIdDelete(realm, clientScopeId, (error, data, response) => {
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
 **clientScopeId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## realmDefaultOptionalClientScopesClientScopeIdPut

> realmDefaultOptionalClientScopesClientScopeIdPut(realm, clientScopeId)



### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.RealmsAdminApi();
let realm = "realm_example"; // String | realm name (not id!)
let clientScopeId = "clientScopeId_example"; // String | 
apiInstance.realmDefaultOptionalClientScopesClientScopeIdPut(realm, clientScopeId, (error, data, response) => {
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
 **clientScopeId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## realmDefaultOptionalClientScopesGet

> [ClientScopeRepresentation] realmDefaultOptionalClientScopesGet(realm)

Get realm optional client scopes.

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.RealmsAdminApi();
let realm = "realm_example"; // String | realm name (not id!)
apiInstance.realmDefaultOptionalClientScopesGet(realm, (error, data, response) => {
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

[**[ClientScopeRepresentation]**](ClientScopeRepresentation.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## realmDelete

> realmDelete(realm)

Delete the realm

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.RealmsAdminApi();
let realm = "realm_example"; // String | realm name (not id!)
apiInstance.realmDelete(realm, (error, data, response) => {
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

### Return type

null (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## realmEventsConfigGet

> RealmEventsConfigRepresentation realmEventsConfigGet(realm)

Get the events provider configuration   Returns JSON object with events provider configuration

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.RealmsAdminApi();
let realm = "realm_example"; // String | realm name (not id!)
apiInstance.realmEventsConfigGet(realm, (error, data, response) => {
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

[**RealmEventsConfigRepresentation**](RealmEventsConfigRepresentation.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## realmEventsConfigPut

> realmEventsConfigPut(realm, realmEventsConfigRepresentation)

Update the events provider   Change the events provider and/or its configuration

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.RealmsAdminApi();
let realm = "realm_example"; // String | realm name (not id!)
let realmEventsConfigRepresentation = new KeycloakAdminRestApi.RealmEventsConfigRepresentation(); // RealmEventsConfigRepresentation | 
apiInstance.realmEventsConfigPut(realm, realmEventsConfigRepresentation, (error, data, response) => {
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
 **realmEventsConfigRepresentation** | [**RealmEventsConfigRepresentation**](RealmEventsConfigRepresentation.md)|  | 

### Return type

null (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## realmEventsDelete

> realmEventsDelete(realm)

Delete all events

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.RealmsAdminApi();
let realm = "realm_example"; // String | realm name (not id!)
apiInstance.realmEventsDelete(realm, (error, data, response) => {
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

### Return type

null (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## realmEventsGet

> [EventRepresentation] realmEventsGet(realm, opts)

Get events   Returns all events, or filters them based on URL query parameters listed here

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.RealmsAdminApi();
let realm = "realm_example"; // String | realm name (not id!)
let opts = {
  'client': "client_example", // String | App or oauth client name
  'dateFrom': "dateFrom_example", // String | From date
  'dateTo': "dateTo_example", // String | To date
  'first': 56, // Number | Paging offset
  'ipAddress': "ipAddress_example", // String | IP address
  'max': 56, // Number | Maximum results size (defaults to 100)
  'type': ["null"], // [String] | The types of events to return
  'user': "user_example" // String | User id
};
apiInstance.realmEventsGet(realm, opts, (error, data, response) => {
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
 **client** | **String**| App or oauth client name | [optional] 
 **dateFrom** | **String**| From date | [optional] 
 **dateTo** | **String**| To date | [optional] 
 **first** | **Number**| Paging offset | [optional] 
 **ipAddress** | **String**| IP address | [optional] 
 **max** | **Number**| Maximum results size (defaults to 100) | [optional] 
 **type** | [**[String]**](String.md)| The types of events to return | [optional] 
 **user** | **String**| User id | [optional] 

### Return type

[**[EventRepresentation]**](EventRepresentation.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## realmGet

> RealmRepresentation realmGet(realm)

Get the top-level representation of the realm   It will not include nested information like User and Client representations.

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.RealmsAdminApi();
let realm = "realm_example"; // String | realm name (not id!)
apiInstance.realmGet(realm, (error, data, response) => {
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

[**RealmRepresentation**](RealmRepresentation.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## realmGroupByPathPathGet

> GroupRepresentation realmGroupByPathPathGet(realm, path)



### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.RealmsAdminApi();
let realm = "realm_example"; // String | realm name (not id!)
let path = "path_example"; // String | 
apiInstance.realmGroupByPathPathGet(realm, path, (error, data, response) => {
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
 **path** | **String**|  | 

### Return type

[**GroupRepresentation**](GroupRepresentation.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## realmLogoutAllPost

> realmLogoutAllPost(realm)

Removes all user sessions.

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.RealmsAdminApi();
let realm = "realm_example"; // String | realm name (not id!)
apiInstance.realmLogoutAllPost(realm, (error, data, response) => {
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

### Return type

null (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## realmPartialExportPost

> RealmRepresentation realmPartialExportPost(realm, opts)

Partial export of existing realm into a JSON file.

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.RealmsAdminApi();
let realm = "realm_example"; // String | realm name (not id!)
let opts = {
  'exportClients': true, // Boolean | 
  'exportGroupsAndRoles': true // Boolean | 
};
apiInstance.realmPartialExportPost(realm, opts, (error, data, response) => {
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
 **exportClients** | **Boolean**|  | [optional] 
 **exportGroupsAndRoles** | **Boolean**|  | [optional] 

### Return type

[**RealmRepresentation**](RealmRepresentation.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## realmPartialImportPost

> realmPartialImportPost(realm, partialImportRepresentation)

Partial import from a JSON file to an existing realm.

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.RealmsAdminApi();
let realm = "realm_example"; // String | realm name (not id!)
let partialImportRepresentation = new KeycloakAdminRestApi.PartialImportRepresentation(); // PartialImportRepresentation | 
apiInstance.realmPartialImportPost(realm, partialImportRepresentation, (error, data, response) => {
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
 **partialImportRepresentation** | [**PartialImportRepresentation**](PartialImportRepresentation.md)|  | 

### Return type

null (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## realmPushRevocationPost

> realmPushRevocationPost(realm)

Push the realm’s revocation policy to any client that has an admin url associated with it.

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.RealmsAdminApi();
let realm = "realm_example"; // String | realm name (not id!)
apiInstance.realmPushRevocationPost(realm, (error, data, response) => {
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

### Return type

null (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## realmPut

> realmPut(realm, realmRepresentation)

Update the top-level information of the realm   Any user, roles or client information in the representation  will be ignored.

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.RealmsAdminApi();
let realm = "realm_example"; // String | realm name (not id!)
let realmRepresentation = new KeycloakAdminRestApi.RealmRepresentation(); // RealmRepresentation | 
apiInstance.realmPut(realm, realmRepresentation, (error, data, response) => {
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
 **realmRepresentation** | [**RealmRepresentation**](RealmRepresentation.md)|  | 

### Return type

null (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## realmSessionsSessionDelete

> realmSessionsSessionDelete(realm, session)

Remove a specific user session.

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.RealmsAdminApi();
let realm = "realm_example"; // String | realm name (not id!)
let session = "session_example"; // String | 
apiInstance.realmSessionsSessionDelete(realm, session, (error, data, response) => {
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
 **session** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## realmTestLDAPConnectionPost

> realmTestLDAPConnectionPost(realm, testLdapConnectionRepresentation)

Test LDAP connection

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.RealmsAdminApi();
let realm = "realm_example"; // String | realm name (not id!)
let testLdapConnectionRepresentation = new KeycloakAdminRestApi.TestLdapConnectionRepresentation(); // TestLdapConnectionRepresentation | 
apiInstance.realmTestLDAPConnectionPost(realm, testLdapConnectionRepresentation, (error, data, response) => {
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
 **testLdapConnectionRepresentation** | [**TestLdapConnectionRepresentation**](TestLdapConnectionRepresentation.md)|  | 

### Return type

null (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## realmTestSMTPConnectionPost

> realmTestSMTPConnectionPost(realm, requestBody)



### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.RealmsAdminApi();
let realm = "realm_example"; // String | realm name (not id!)
let requestBody = {key: null}; // {String: Object} | 
apiInstance.realmTestSMTPConnectionPost(realm, requestBody, (error, data, response) => {
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
 **requestBody** | [**{String: Object}**](Object.md)|  | 

### Return type

null (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## realmUsersManagementPermissionsGet

> ManagementPermissionReference realmUsersManagementPermissionsGet(realm)



### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.RealmsAdminApi();
let realm = "realm_example"; // String | realm name (not id!)
apiInstance.realmUsersManagementPermissionsGet(realm, (error, data, response) => {
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

[**ManagementPermissionReference**](ManagementPermissionReference.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## realmUsersManagementPermissionsPut

> ManagementPermissionReference realmUsersManagementPermissionsPut(realm, managementPermissionReference)



### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.RealmsAdminApi();
let realm = "realm_example"; // String | realm name (not id!)
let managementPermissionReference = new KeycloakAdminRestApi.ManagementPermissionReference(); // ManagementPermissionReference | 
apiInstance.realmUsersManagementPermissionsPut(realm, managementPermissionReference, (error, data, response) => {
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
 **managementPermissionReference** | [**ManagementPermissionReference**](ManagementPermissionReference.md)|  | 

### Return type

[**ManagementPermissionReference**](ManagementPermissionReference.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## rootPost

> rootPost(realmRepresentation)

Import a realm   Imports a realm from a full representation of that realm.

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.RealmsAdminApi();
let realmRepresentation = new KeycloakAdminRestApi.RealmRepresentation(); // RealmRepresentation | JSON representation of the realm
apiInstance.rootPost(realmRepresentation, (error, data, response) => {
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
 **realmRepresentation** | [**RealmRepresentation**](RealmRepresentation.md)| JSON representation of the realm | 

### Return type

null (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

