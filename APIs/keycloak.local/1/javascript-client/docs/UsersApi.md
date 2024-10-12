# KeycloakAdminRestApi.UsersApi

All URIs are relative to *http://keycloak.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**realmUsersCountGet**](UsersApi.md#realmUsersCountGet) | **GET** /{realm}/users/count | Returns the number of users that match the given criteria.
[**realmUsersGet**](UsersApi.md#realmUsersGet) | **GET** /{realm}/users | Get users   Returns a list of users, filtered according to query parameters
[**realmUsersIdConfiguredUserStorageCredentialTypesGet**](UsersApi.md#realmUsersIdConfiguredUserStorageCredentialTypesGet) | **GET** /{realm}/users/{id}/configured-user-storage-credential-types | Return credential types, which are provided by the user storage where user is stored.
[**realmUsersIdConsentsClientDelete**](UsersApi.md#realmUsersIdConsentsClientDelete) | **DELETE** /{realm}/users/{id}/consents/{client} | Revoke consent and offline tokens for particular client from user
[**realmUsersIdConsentsGet**](UsersApi.md#realmUsersIdConsentsGet) | **GET** /{realm}/users/{id}/consents | Get consents granted by the user
[**realmUsersIdCredentialsCredentialIdDelete**](UsersApi.md#realmUsersIdCredentialsCredentialIdDelete) | **DELETE** /{realm}/users/{id}/credentials/{credentialId} | Remove a credential for a user
[**realmUsersIdCredentialsCredentialIdMoveAfterNewPreviousCredentialIdPost**](UsersApi.md#realmUsersIdCredentialsCredentialIdMoveAfterNewPreviousCredentialIdPost) | **POST** /{realm}/users/{id}/credentials/{credentialId}/moveAfter/{newPreviousCredentialId} | Move a credential to a position behind another credential
[**realmUsersIdCredentialsCredentialIdMoveToFirstPost**](UsersApi.md#realmUsersIdCredentialsCredentialIdMoveToFirstPost) | **POST** /{realm}/users/{id}/credentials/{credentialId}/moveToFirst | Move a credential to a first position in the credentials list of the user
[**realmUsersIdCredentialsCredentialIdUserLabelPut**](UsersApi.md#realmUsersIdCredentialsCredentialIdUserLabelPut) | **PUT** /{realm}/users/{id}/credentials/{credentialId}/userLabel | Update a credential label for a user
[**realmUsersIdCredentialsGet**](UsersApi.md#realmUsersIdCredentialsGet) | **GET** /{realm}/users/{id}/credentials | 
[**realmUsersIdDelete**](UsersApi.md#realmUsersIdDelete) | **DELETE** /{realm}/users/{id} | Delete the user
[**realmUsersIdDisableCredentialTypesPut**](UsersApi.md#realmUsersIdDisableCredentialTypesPut) | **PUT** /{realm}/users/{id}/disable-credential-types | Disable all credentials for a user of a specific type
[**realmUsersIdExecuteActionsEmailPut**](UsersApi.md#realmUsersIdExecuteActionsEmailPut) | **PUT** /{realm}/users/{id}/execute-actions-email | Send a update account email to the user   An email contains a link the user can click to perform a set of required actions.
[**realmUsersIdFederatedIdentityGet**](UsersApi.md#realmUsersIdFederatedIdentityGet) | **GET** /{realm}/users/{id}/federated-identity | Get social logins associated with the user
[**realmUsersIdFederatedIdentityProviderDelete**](UsersApi.md#realmUsersIdFederatedIdentityProviderDelete) | **DELETE** /{realm}/users/{id}/federated-identity/{provider} | Remove a social login provider from user
[**realmUsersIdFederatedIdentityProviderPost**](UsersApi.md#realmUsersIdFederatedIdentityProviderPost) | **POST** /{realm}/users/{id}/federated-identity/{provider} | Add a social login provider to the user
[**realmUsersIdGet**](UsersApi.md#realmUsersIdGet) | **GET** /{realm}/users/{id} | Get representation of the user
[**realmUsersIdGroupsCountGet**](UsersApi.md#realmUsersIdGroupsCountGet) | **GET** /{realm}/users/{id}/groups/count | 
[**realmUsersIdGroupsGet**](UsersApi.md#realmUsersIdGroupsGet) | **GET** /{realm}/users/{id}/groups | 
[**realmUsersIdGroupsGroupIdDelete**](UsersApi.md#realmUsersIdGroupsGroupIdDelete) | **DELETE** /{realm}/users/{id}/groups/{groupId} | 
[**realmUsersIdGroupsGroupIdPut**](UsersApi.md#realmUsersIdGroupsGroupIdPut) | **PUT** /{realm}/users/{id}/groups/{groupId} | 
[**realmUsersIdImpersonationPost**](UsersApi.md#realmUsersIdImpersonationPost) | **POST** /{realm}/users/{id}/impersonation | Impersonate the user
[**realmUsersIdLogoutPost**](UsersApi.md#realmUsersIdLogoutPost) | **POST** /{realm}/users/{id}/logout | Remove all user sessions associated with the user   Also send notification to all clients that have an admin URL to invalidate the sessions for the particular user.
[**realmUsersIdOfflineSessionsClientIdGet**](UsersApi.md#realmUsersIdOfflineSessionsClientIdGet) | **GET** /{realm}/users/{id}/offline-sessions/{clientId} | Get offline sessions associated with the user and client
[**realmUsersIdPut**](UsersApi.md#realmUsersIdPut) | **PUT** /{realm}/users/{id} | Update the user
[**realmUsersIdResetPasswordPut**](UsersApi.md#realmUsersIdResetPasswordPut) | **PUT** /{realm}/users/{id}/reset-password | Set up a new password for the user.
[**realmUsersIdSendVerifyEmailPut**](UsersApi.md#realmUsersIdSendVerifyEmailPut) | **PUT** /{realm}/users/{id}/send-verify-email | Send an email-verification email to the user   An email contains a link the user can click to verify their email address.
[**realmUsersIdSessionsGet**](UsersApi.md#realmUsersIdSessionsGet) | **GET** /{realm}/users/{id}/sessions | Get sessions associated with the user
[**realmUsersPost**](UsersApi.md#realmUsersPost) | **POST** /{realm}/users | Create a new user   Username must be unique.



## realmUsersCountGet

> Number realmUsersCountGet(realm, opts)

Returns the number of users that match the given criteria.

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.UsersApi();
let realm = "realm_example"; // String | realm name (not id!)
let opts = {
  'email': "email_example", // String | email filter
  'firstName': "firstName_example", // String | first name filter
  'lastName': "lastName_example", // String | last name filter
  'search': "search_example", // String | arbitrary search string for all the fields below
  'username': "username_example" // String | username filter
};
apiInstance.realmUsersCountGet(realm, opts, (error, data, response) => {
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
 **email** | **String**| email filter | [optional] 
 **firstName** | **String**| first name filter | [optional] 
 **lastName** | **String**| last name filter | [optional] 
 **search** | **String**| arbitrary search string for all the fields below | [optional] 
 **username** | **String**| username filter | [optional] 

### Return type

**Number**

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## realmUsersGet

> [UserRepresentation] realmUsersGet(realm, opts)

Get users   Returns a list of users, filtered according to query parameters

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.UsersApi();
let realm = "realm_example"; // String | realm name (not id!)
let opts = {
  'briefRepresentation': true, // Boolean | 
  'email': "email_example", // String | 
  'first': 56, // Number | 
  'firstName': "firstName_example", // String | 
  'lastName': "lastName_example", // String | 
  'max': 56, // Number | Maximum results size (defaults to 100)
  'search': "search_example", // String | A String contained in username, first or last name, or email
  'username': "username_example" // String | 
};
apiInstance.realmUsersGet(realm, opts, (error, data, response) => {
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
 **briefRepresentation** | **Boolean**|  | [optional] 
 **email** | **String**|  | [optional] 
 **first** | **Number**|  | [optional] 
 **firstName** | **String**|  | [optional] 
 **lastName** | **String**|  | [optional] 
 **max** | **Number**| Maximum results size (defaults to 100) | [optional] 
 **search** | **String**| A String contained in username, first or last name, or email | [optional] 
 **username** | **String**|  | [optional] 

### Return type

[**[UserRepresentation]**](UserRepresentation.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## realmUsersIdConfiguredUserStorageCredentialTypesGet

> [String] realmUsersIdConfiguredUserStorageCredentialTypesGet(realm, id)

Return credential types, which are provided by the user storage where user is stored.

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.UsersApi();
let realm = "realm_example"; // String | realm name (not id!)
let id = "id_example"; // String | User id
apiInstance.realmUsersIdConfiguredUserStorageCredentialTypesGet(realm, id, (error, data, response) => {
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
 **id** | **String**| User id | 

### Return type

**[String]**

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## realmUsersIdConsentsClientDelete

> realmUsersIdConsentsClientDelete(realm, id, client)

Revoke consent and offline tokens for particular client from user

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.UsersApi();
let realm = "realm_example"; // String | realm name (not id!)
let id = "id_example"; // String | User id
let client = "client_example"; // String | Client id
apiInstance.realmUsersIdConsentsClientDelete(realm, id, client, (error, data, response) => {
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
 **id** | **String**| User id | 
 **client** | **String**| Client id | 

### Return type

null (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## realmUsersIdConsentsGet

> [{String: Object}] realmUsersIdConsentsGet(realm, id)

Get consents granted by the user

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.UsersApi();
let realm = "realm_example"; // String | realm name (not id!)
let id = "id_example"; // String | User id
apiInstance.realmUsersIdConsentsGet(realm, id, (error, data, response) => {
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
 **id** | **String**| User id | 

### Return type

**[{String: Object}]**

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## realmUsersIdCredentialsCredentialIdDelete

> realmUsersIdCredentialsCredentialIdDelete(realm, id, credentialId)

Remove a credential for a user

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.UsersApi();
let realm = "realm_example"; // String | realm name (not id!)
let id = "id_example"; // String | User id
let credentialId = "credentialId_example"; // String | 
apiInstance.realmUsersIdCredentialsCredentialIdDelete(realm, id, credentialId, (error, data, response) => {
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
 **id** | **String**| User id | 
 **credentialId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## realmUsersIdCredentialsCredentialIdMoveAfterNewPreviousCredentialIdPost

> realmUsersIdCredentialsCredentialIdMoveAfterNewPreviousCredentialIdPost(realm, id, credentialId, newPreviousCredentialId)

Move a credential to a position behind another credential

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.UsersApi();
let realm = "realm_example"; // String | realm name (not id!)
let id = "id_example"; // String | User id
let credentialId = "credentialId_example"; // String | The credential to move
let newPreviousCredentialId = "newPreviousCredentialId_example"; // String | The credential that will be the previous element in the list. If set to null, the moved credential will be the first element in the list.
apiInstance.realmUsersIdCredentialsCredentialIdMoveAfterNewPreviousCredentialIdPost(realm, id, credentialId, newPreviousCredentialId, (error, data, response) => {
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
 **id** | **String**| User id | 
 **credentialId** | **String**| The credential to move | 
 **newPreviousCredentialId** | **String**| The credential that will be the previous element in the list. If set to null, the moved credential will be the first element in the list. | 

### Return type

null (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## realmUsersIdCredentialsCredentialIdMoveToFirstPost

> realmUsersIdCredentialsCredentialIdMoveToFirstPost(realm, id, credentialId)

Move a credential to a first position in the credentials list of the user

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.UsersApi();
let realm = "realm_example"; // String | realm name (not id!)
let id = "id_example"; // String | User id
let credentialId = "credentialId_example"; // String | The credential to move
apiInstance.realmUsersIdCredentialsCredentialIdMoveToFirstPost(realm, id, credentialId, (error, data, response) => {
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
 **id** | **String**| User id | 
 **credentialId** | **String**| The credential to move | 

### Return type

null (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## realmUsersIdCredentialsCredentialIdUserLabelPut

> realmUsersIdCredentialsCredentialIdUserLabelPut(realm, id, credentialId, body)

Update a credential label for a user

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.UsersApi();
let realm = "realm_example"; // String | realm name (not id!)
let id = "id_example"; // String | User id
let credentialId = "credentialId_example"; // String | 
let body = "body_example"; // String | 
apiInstance.realmUsersIdCredentialsCredentialIdUserLabelPut(realm, id, credentialId, body, (error, data, response) => {
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
 **id** | **String**| User id | 
 **credentialId** | **String**|  | 
 **body** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: text/plain
- **Accept**: Not defined


## realmUsersIdCredentialsGet

> [CredentialRepresentation] realmUsersIdCredentialsGet(realm, id)



### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.UsersApi();
let realm = "realm_example"; // String | realm name (not id!)
let id = "id_example"; // String | User id
apiInstance.realmUsersIdCredentialsGet(realm, id, (error, data, response) => {
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
 **id** | **String**| User id | 

### Return type

[**[CredentialRepresentation]**](CredentialRepresentation.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## realmUsersIdDelete

> realmUsersIdDelete(realm, id)

Delete the user

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.UsersApi();
let realm = "realm_example"; // String | realm name (not id!)
let id = "id_example"; // String | User id
apiInstance.realmUsersIdDelete(realm, id, (error, data, response) => {
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
 **id** | **String**| User id | 

### Return type

null (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## realmUsersIdDisableCredentialTypesPut

> realmUsersIdDisableCredentialTypesPut(realm, id, requestBody)

Disable all credentials for a user of a specific type

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.UsersApi();
let realm = "realm_example"; // String | realm name (not id!)
let id = "id_example"; // String | User id
let requestBody = ["null"]; // [String] | 
apiInstance.realmUsersIdDisableCredentialTypesPut(realm, id, requestBody, (error, data, response) => {
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
 **id** | **String**| User id | 
 **requestBody** | [**[String]**](String.md)|  | 

### Return type

null (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## realmUsersIdExecuteActionsEmailPut

> realmUsersIdExecuteActionsEmailPut(realm, id, requestBody, opts)

Send a update account email to the user   An email contains a link the user can click to perform a set of required actions.

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.UsersApi();
let realm = "realm_example"; // String | realm name (not id!)
let id = "id_example"; // String | User id
let requestBody = ["null"]; // [String] | required actions the user needs to complete
let opts = {
  'clientId': "clientId_example", // String | Client id
  'lifespan': 56, // Number | Number of seconds after which the generated token expires
  'redirectUri': "redirectUri_example" // String | Redirect uri
};
apiInstance.realmUsersIdExecuteActionsEmailPut(realm, id, requestBody, opts, (error, data, response) => {
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
 **id** | **String**| User id | 
 **requestBody** | [**[String]**](String.md)| required actions the user needs to complete | 
 **clientId** | **String**| Client id | [optional] 
 **lifespan** | **Number**| Number of seconds after which the generated token expires | [optional] 
 **redirectUri** | **String**| Redirect uri | [optional] 

### Return type

null (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## realmUsersIdFederatedIdentityGet

> [FederatedIdentityRepresentation] realmUsersIdFederatedIdentityGet(realm, id)

Get social logins associated with the user

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.UsersApi();
let realm = "realm_example"; // String | realm name (not id!)
let id = "id_example"; // String | User id
apiInstance.realmUsersIdFederatedIdentityGet(realm, id, (error, data, response) => {
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
 **id** | **String**| User id | 

### Return type

[**[FederatedIdentityRepresentation]**](FederatedIdentityRepresentation.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## realmUsersIdFederatedIdentityProviderDelete

> realmUsersIdFederatedIdentityProviderDelete(realm, id, provider)

Remove a social login provider from user

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.UsersApi();
let realm = "realm_example"; // String | realm name (not id!)
let id = "id_example"; // String | User id
let provider = "provider_example"; // String | Social login provider id
apiInstance.realmUsersIdFederatedIdentityProviderDelete(realm, id, provider, (error, data, response) => {
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
 **id** | **String**| User id | 
 **provider** | **String**| Social login provider id | 

### Return type

null (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## realmUsersIdFederatedIdentityProviderPost

> realmUsersIdFederatedIdentityProviderPost(realm, id, provider, federatedIdentityRepresentation)

Add a social login provider to the user

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.UsersApi();
let realm = "realm_example"; // String | realm name (not id!)
let id = "id_example"; // String | User id
let provider = "provider_example"; // String | Social login provider id
let federatedIdentityRepresentation = new KeycloakAdminRestApi.FederatedIdentityRepresentation(); // FederatedIdentityRepresentation | 
apiInstance.realmUsersIdFederatedIdentityProviderPost(realm, id, provider, federatedIdentityRepresentation, (error, data, response) => {
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
 **id** | **String**| User id | 
 **provider** | **String**| Social login provider id | 
 **federatedIdentityRepresentation** | [**FederatedIdentityRepresentation**](FederatedIdentityRepresentation.md)|  | 

### Return type

null (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## realmUsersIdGet

> UserRepresentation realmUsersIdGet(realm, id)

Get representation of the user

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.UsersApi();
let realm = "realm_example"; // String | realm name (not id!)
let id = "id_example"; // String | User id
apiInstance.realmUsersIdGet(realm, id, (error, data, response) => {
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
 **id** | **String**| User id | 

### Return type

[**UserRepresentation**](UserRepresentation.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## realmUsersIdGroupsCountGet

> {String: Object} realmUsersIdGroupsCountGet(realm, id, opts)



### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.UsersApi();
let realm = "realm_example"; // String | realm name (not id!)
let id = "id_example"; // String | User id
let opts = {
  'search': "search_example" // String | 
};
apiInstance.realmUsersIdGroupsCountGet(realm, id, opts, (error, data, response) => {
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
 **id** | **String**| User id | 
 **search** | **String**|  | [optional] 

### Return type

**{String: Object}**

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## realmUsersIdGroupsGet

> [GroupRepresentation] realmUsersIdGroupsGet(realm, id, opts)



### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.UsersApi();
let realm = "realm_example"; // String | realm name (not id!)
let id = "id_example"; // String | User id
let opts = {
  'briefRepresentation': true, // Boolean | 
  'first': 56, // Number | 
  'max': 56, // Number | 
  'search': "search_example" // String | 
};
apiInstance.realmUsersIdGroupsGet(realm, id, opts, (error, data, response) => {
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
 **id** | **String**| User id | 
 **briefRepresentation** | **Boolean**|  | [optional] 
 **first** | **Number**|  | [optional] 
 **max** | **Number**|  | [optional] 
 **search** | **String**|  | [optional] 

### Return type

[**[GroupRepresentation]**](GroupRepresentation.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## realmUsersIdGroupsGroupIdDelete

> realmUsersIdGroupsGroupIdDelete(realm, id, groupId)



### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.UsersApi();
let realm = "realm_example"; // String | realm name (not id!)
let id = "id_example"; // String | User id
let groupId = "groupId_example"; // String | 
apiInstance.realmUsersIdGroupsGroupIdDelete(realm, id, groupId, (error, data, response) => {
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
 **id** | **String**| User id | 
 **groupId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## realmUsersIdGroupsGroupIdPut

> realmUsersIdGroupsGroupIdPut(realm, id, groupId)



### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.UsersApi();
let realm = "realm_example"; // String | realm name (not id!)
let id = "id_example"; // String | User id
let groupId = "groupId_example"; // String | 
apiInstance.realmUsersIdGroupsGroupIdPut(realm, id, groupId, (error, data, response) => {
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
 **id** | **String**| User id | 
 **groupId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## realmUsersIdImpersonationPost

> {String: Object} realmUsersIdImpersonationPost(realm, id)

Impersonate the user

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.UsersApi();
let realm = "realm_example"; // String | realm name (not id!)
let id = "id_example"; // String | User id
apiInstance.realmUsersIdImpersonationPost(realm, id, (error, data, response) => {
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
 **id** | **String**| User id | 

### Return type

**{String: Object}**

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## realmUsersIdLogoutPost

> realmUsersIdLogoutPost(realm, id)

Remove all user sessions associated with the user   Also send notification to all clients that have an admin URL to invalidate the sessions for the particular user.

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.UsersApi();
let realm = "realm_example"; // String | realm name (not id!)
let id = "id_example"; // String | User id
apiInstance.realmUsersIdLogoutPost(realm, id, (error, data, response) => {
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
 **id** | **String**| User id | 

### Return type

null (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## realmUsersIdOfflineSessionsClientIdGet

> [UserSessionRepresentation] realmUsersIdOfflineSessionsClientIdGet(realm, id, clientId)

Get offline sessions associated with the user and client

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.UsersApi();
let realm = "realm_example"; // String | realm name (not id!)
let id = "id_example"; // String | User id
let clientId = "clientId_example"; // String | 
apiInstance.realmUsersIdOfflineSessionsClientIdGet(realm, id, clientId, (error, data, response) => {
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
 **id** | **String**| User id | 
 **clientId** | **String**|  | 

### Return type

[**[UserSessionRepresentation]**](UserSessionRepresentation.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## realmUsersIdPut

> realmUsersIdPut(realm, id, userRepresentation)

Update the user

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.UsersApi();
let realm = "realm_example"; // String | realm name (not id!)
let id = "id_example"; // String | User id
let userRepresentation = new KeycloakAdminRestApi.UserRepresentation(); // UserRepresentation | 
apiInstance.realmUsersIdPut(realm, id, userRepresentation, (error, data, response) => {
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
 **id** | **String**| User id | 
 **userRepresentation** | [**UserRepresentation**](UserRepresentation.md)|  | 

### Return type

null (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## realmUsersIdResetPasswordPut

> realmUsersIdResetPasswordPut(realm, id, credentialRepresentation)

Set up a new password for the user.

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.UsersApi();
let realm = "realm_example"; // String | realm name (not id!)
let id = "id_example"; // String | User id
let credentialRepresentation = new KeycloakAdminRestApi.CredentialRepresentation(); // CredentialRepresentation | The representation must contain a rawPassword with the plain-text password
apiInstance.realmUsersIdResetPasswordPut(realm, id, credentialRepresentation, (error, data, response) => {
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
 **id** | **String**| User id | 
 **credentialRepresentation** | [**CredentialRepresentation**](CredentialRepresentation.md)| The representation must contain a rawPassword with the plain-text password | 

### Return type

null (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## realmUsersIdSendVerifyEmailPut

> realmUsersIdSendVerifyEmailPut(realm, id, opts)

Send an email-verification email to the user   An email contains a link the user can click to verify their email address.

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.UsersApi();
let realm = "realm_example"; // String | realm name (not id!)
let id = "id_example"; // String | User id
let opts = {
  'clientId': "clientId_example", // String | Client id
  'redirectUri': "redirectUri_example" // String | Redirect uri
};
apiInstance.realmUsersIdSendVerifyEmailPut(realm, id, opts, (error, data, response) => {
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
 **id** | **String**| User id | 
 **clientId** | **String**| Client id | [optional] 
 **redirectUri** | **String**| Redirect uri | [optional] 

### Return type

null (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## realmUsersIdSessionsGet

> [UserSessionRepresentation] realmUsersIdSessionsGet(realm, id)

Get sessions associated with the user

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.UsersApi();
let realm = "realm_example"; // String | realm name (not id!)
let id = "id_example"; // String | User id
apiInstance.realmUsersIdSessionsGet(realm, id, (error, data, response) => {
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
 **id** | **String**| User id | 

### Return type

[**[UserSessionRepresentation]**](UserSessionRepresentation.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## realmUsersPost

> realmUsersPost(realm, userRepresentation)

Create a new user   Username must be unique.

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.UsersApi();
let realm = "realm_example"; // String | realm name (not id!)
let userRepresentation = new KeycloakAdminRestApi.UserRepresentation(); // UserRepresentation | 
apiInstance.realmUsersPost(realm, userRepresentation, (error, data, response) => {
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
 **userRepresentation** | [**UserRepresentation**](UserRepresentation.md)|  | 

### Return type

null (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

