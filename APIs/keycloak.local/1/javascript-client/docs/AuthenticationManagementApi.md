# KeycloakAdminRestApi.AuthenticationManagementApi

All URIs are relative to *http://keycloak.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**realmAuthenticationAuthenticatorProvidersGet**](AuthenticationManagementApi.md#realmAuthenticationAuthenticatorProvidersGet) | **GET** /{realm}/authentication/authenticator-providers | Get authenticator providers   Returns a list of authenticator providers.
[**realmAuthenticationClientAuthenticatorProvidersGet**](AuthenticationManagementApi.md#realmAuthenticationClientAuthenticatorProvidersGet) | **GET** /{realm}/authentication/client-authenticator-providers | Get client authenticator providers   Returns a list of client authenticator providers.
[**realmAuthenticationConfigDescriptionProviderIdGet**](AuthenticationManagementApi.md#realmAuthenticationConfigDescriptionProviderIdGet) | **GET** /{realm}/authentication/config-description/{providerId} | Get authenticator provider’s configuration description
[**realmAuthenticationConfigIdDelete**](AuthenticationManagementApi.md#realmAuthenticationConfigIdDelete) | **DELETE** /{realm}/authentication/config/{id} | Delete authenticator configuration
[**realmAuthenticationConfigIdGet**](AuthenticationManagementApi.md#realmAuthenticationConfigIdGet) | **GET** /{realm}/authentication/config/{id} | Get authenticator configuration
[**realmAuthenticationConfigIdPut**](AuthenticationManagementApi.md#realmAuthenticationConfigIdPut) | **PUT** /{realm}/authentication/config/{id} | Update authenticator configuration
[**realmAuthenticationExecutionsExecutionIdConfigPost**](AuthenticationManagementApi.md#realmAuthenticationExecutionsExecutionIdConfigPost) | **POST** /{realm}/authentication/executions/{executionId}/config | Update execution with new configuration
[**realmAuthenticationExecutionsExecutionIdDelete**](AuthenticationManagementApi.md#realmAuthenticationExecutionsExecutionIdDelete) | **DELETE** /{realm}/authentication/executions/{executionId} | Delete execution
[**realmAuthenticationExecutionsExecutionIdGet**](AuthenticationManagementApi.md#realmAuthenticationExecutionsExecutionIdGet) | **GET** /{realm}/authentication/executions/{executionId} | Get Single Execution
[**realmAuthenticationExecutionsExecutionIdLowerPriorityPost**](AuthenticationManagementApi.md#realmAuthenticationExecutionsExecutionIdLowerPriorityPost) | **POST** /{realm}/authentication/executions/{executionId}/lower-priority | Lower execution’s priority
[**realmAuthenticationExecutionsExecutionIdRaisePriorityPost**](AuthenticationManagementApi.md#realmAuthenticationExecutionsExecutionIdRaisePriorityPost) | **POST** /{realm}/authentication/executions/{executionId}/raise-priority | Raise execution’s priority
[**realmAuthenticationExecutionsPost**](AuthenticationManagementApi.md#realmAuthenticationExecutionsPost) | **POST** /{realm}/authentication/executions | Add new authentication execution
[**realmAuthenticationFlowsFlowAliasCopyPost**](AuthenticationManagementApi.md#realmAuthenticationFlowsFlowAliasCopyPost) | **POST** /{realm}/authentication/flows/{flowAlias}/copy | Copy existing authentication flow under a new name   The new name is given as &#39;newName&#39; attribute of the passed JSON object
[**realmAuthenticationFlowsFlowAliasExecutionsExecutionPost**](AuthenticationManagementApi.md#realmAuthenticationFlowsFlowAliasExecutionsExecutionPost) | **POST** /{realm}/authentication/flows/{flowAlias}/executions/execution | Add new authentication execution to a flow
[**realmAuthenticationFlowsFlowAliasExecutionsFlowPost**](AuthenticationManagementApi.md#realmAuthenticationFlowsFlowAliasExecutionsFlowPost) | **POST** /{realm}/authentication/flows/{flowAlias}/executions/flow | Add new flow with new execution to existing flow
[**realmAuthenticationFlowsFlowAliasExecutionsGet**](AuthenticationManagementApi.md#realmAuthenticationFlowsFlowAliasExecutionsGet) | **GET** /{realm}/authentication/flows/{flowAlias}/executions | Get authentication executions for a flow
[**realmAuthenticationFlowsFlowAliasExecutionsPut**](AuthenticationManagementApi.md#realmAuthenticationFlowsFlowAliasExecutionsPut) | **PUT** /{realm}/authentication/flows/{flowAlias}/executions | Update authentication executions of a flow
[**realmAuthenticationFlowsGet**](AuthenticationManagementApi.md#realmAuthenticationFlowsGet) | **GET** /{realm}/authentication/flows | Get authentication flows   Returns a list of authentication flows.
[**realmAuthenticationFlowsIdDelete**](AuthenticationManagementApi.md#realmAuthenticationFlowsIdDelete) | **DELETE** /{realm}/authentication/flows/{id} | Delete an authentication flow
[**realmAuthenticationFlowsIdGet**](AuthenticationManagementApi.md#realmAuthenticationFlowsIdGet) | **GET** /{realm}/authentication/flows/{id} | Get authentication flow for id
[**realmAuthenticationFlowsIdPut**](AuthenticationManagementApi.md#realmAuthenticationFlowsIdPut) | **PUT** /{realm}/authentication/flows/{id} | Update an authentication flow
[**realmAuthenticationFlowsPost**](AuthenticationManagementApi.md#realmAuthenticationFlowsPost) | **POST** /{realm}/authentication/flows | Create a new authentication flow
[**realmAuthenticationFormActionProvidersGet**](AuthenticationManagementApi.md#realmAuthenticationFormActionProvidersGet) | **GET** /{realm}/authentication/form-action-providers | Get form action providers   Returns a list of form action providers.
[**realmAuthenticationFormProvidersGet**](AuthenticationManagementApi.md#realmAuthenticationFormProvidersGet) | **GET** /{realm}/authentication/form-providers | Get form providers   Returns a list of form providers.
[**realmAuthenticationPerClientConfigDescriptionGet**](AuthenticationManagementApi.md#realmAuthenticationPerClientConfigDescriptionGet) | **GET** /{realm}/authentication/per-client-config-description | Get configuration descriptions for all clients
[**realmAuthenticationRegisterRequiredActionPost**](AuthenticationManagementApi.md#realmAuthenticationRegisterRequiredActionPost) | **POST** /{realm}/authentication/register-required-action | Register a new required actions
[**realmAuthenticationRequiredActionsAliasDelete**](AuthenticationManagementApi.md#realmAuthenticationRequiredActionsAliasDelete) | **DELETE** /{realm}/authentication/required-actions/{alias} | Delete required action
[**realmAuthenticationRequiredActionsAliasGet**](AuthenticationManagementApi.md#realmAuthenticationRequiredActionsAliasGet) | **GET** /{realm}/authentication/required-actions/{alias} | Get required action for alias
[**realmAuthenticationRequiredActionsAliasLowerPriorityPost**](AuthenticationManagementApi.md#realmAuthenticationRequiredActionsAliasLowerPriorityPost) | **POST** /{realm}/authentication/required-actions/{alias}/lower-priority | Lower required action’s priority
[**realmAuthenticationRequiredActionsAliasPut**](AuthenticationManagementApi.md#realmAuthenticationRequiredActionsAliasPut) | **PUT** /{realm}/authentication/required-actions/{alias} | Update required action
[**realmAuthenticationRequiredActionsAliasRaisePriorityPost**](AuthenticationManagementApi.md#realmAuthenticationRequiredActionsAliasRaisePriorityPost) | **POST** /{realm}/authentication/required-actions/{alias}/raise-priority | Raise required action’s priority
[**realmAuthenticationRequiredActionsGet**](AuthenticationManagementApi.md#realmAuthenticationRequiredActionsGet) | **GET** /{realm}/authentication/required-actions | Get required actions   Returns a list of required actions.
[**realmAuthenticationUnregisteredRequiredActionsGet**](AuthenticationManagementApi.md#realmAuthenticationUnregisteredRequiredActionsGet) | **GET** /{realm}/authentication/unregistered-required-actions | Get unregistered required actions   Returns a list of unregistered required actions.



## realmAuthenticationAuthenticatorProvidersGet

> [{String: Object}] realmAuthenticationAuthenticatorProvidersGet(realm)

Get authenticator providers   Returns a list of authenticator providers.

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.AuthenticationManagementApi();
let realm = "realm_example"; // String | realm name (not id!)
apiInstance.realmAuthenticationAuthenticatorProvidersGet(realm, (error, data, response) => {
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


## realmAuthenticationClientAuthenticatorProvidersGet

> [{String: Object}] realmAuthenticationClientAuthenticatorProvidersGet(realm)

Get client authenticator providers   Returns a list of client authenticator providers.

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.AuthenticationManagementApi();
let realm = "realm_example"; // String | realm name (not id!)
apiInstance.realmAuthenticationClientAuthenticatorProvidersGet(realm, (error, data, response) => {
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


## realmAuthenticationConfigDescriptionProviderIdGet

> AuthenticatorConfigInfoRepresentation realmAuthenticationConfigDescriptionProviderIdGet(realm, providerId)

Get authenticator provider’s configuration description

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.AuthenticationManagementApi();
let realm = "realm_example"; // String | realm name (not id!)
let providerId = "providerId_example"; // String | 
apiInstance.realmAuthenticationConfigDescriptionProviderIdGet(realm, providerId, (error, data, response) => {
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
 **providerId** | **String**|  | 

### Return type

[**AuthenticatorConfigInfoRepresentation**](AuthenticatorConfigInfoRepresentation.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## realmAuthenticationConfigIdDelete

> realmAuthenticationConfigIdDelete(realm, id)

Delete authenticator configuration

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.AuthenticationManagementApi();
let realm = "realm_example"; // String | realm name (not id!)
let id = "id_example"; // String | Configuration id
apiInstance.realmAuthenticationConfigIdDelete(realm, id, (error, data, response) => {
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
 **id** | **String**| Configuration id | 

### Return type

null (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## realmAuthenticationConfigIdGet

> AuthenticatorConfigRepresentation realmAuthenticationConfigIdGet(realm, id)

Get authenticator configuration

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.AuthenticationManagementApi();
let realm = "realm_example"; // String | realm name (not id!)
let id = "id_example"; // String | Configuration id
apiInstance.realmAuthenticationConfigIdGet(realm, id, (error, data, response) => {
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
 **id** | **String**| Configuration id | 

### Return type

[**AuthenticatorConfigRepresentation**](AuthenticatorConfigRepresentation.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## realmAuthenticationConfigIdPut

> realmAuthenticationConfigIdPut(realm, id, authenticatorConfigRepresentation)

Update authenticator configuration

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.AuthenticationManagementApi();
let realm = "realm_example"; // String | realm name (not id!)
let id = "id_example"; // String | Configuration id
let authenticatorConfigRepresentation = new KeycloakAdminRestApi.AuthenticatorConfigRepresentation(); // AuthenticatorConfigRepresentation | JSON describing new state of authenticator configuration
apiInstance.realmAuthenticationConfigIdPut(realm, id, authenticatorConfigRepresentation, (error, data, response) => {
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
 **id** | **String**| Configuration id | 
 **authenticatorConfigRepresentation** | [**AuthenticatorConfigRepresentation**](AuthenticatorConfigRepresentation.md)| JSON describing new state of authenticator configuration | 

### Return type

null (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## realmAuthenticationExecutionsExecutionIdConfigPost

> realmAuthenticationExecutionsExecutionIdConfigPost(realm, executionId, authenticatorConfigRepresentation)

Update execution with new configuration

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.AuthenticationManagementApi();
let realm = "realm_example"; // String | realm name (not id!)
let executionId = "executionId_example"; // String | Execution id
let authenticatorConfigRepresentation = new KeycloakAdminRestApi.AuthenticatorConfigRepresentation(); // AuthenticatorConfigRepresentation | JSON with new configuration
apiInstance.realmAuthenticationExecutionsExecutionIdConfigPost(realm, executionId, authenticatorConfigRepresentation, (error, data, response) => {
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
 **executionId** | **String**| Execution id | 
 **authenticatorConfigRepresentation** | [**AuthenticatorConfigRepresentation**](AuthenticatorConfigRepresentation.md)| JSON with new configuration | 

### Return type

null (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## realmAuthenticationExecutionsExecutionIdDelete

> realmAuthenticationExecutionsExecutionIdDelete(realm, executionId)

Delete execution

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.AuthenticationManagementApi();
let realm = "realm_example"; // String | realm name (not id!)
let executionId = "executionId_example"; // String | Execution id
apiInstance.realmAuthenticationExecutionsExecutionIdDelete(realm, executionId, (error, data, response) => {
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
 **executionId** | **String**| Execution id | 

### Return type

null (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## realmAuthenticationExecutionsExecutionIdGet

> realmAuthenticationExecutionsExecutionIdGet(realm, executionId)

Get Single Execution

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.AuthenticationManagementApi();
let realm = "realm_example"; // String | realm name (not id!)
let executionId = "executionId_example"; // String | Execution id
apiInstance.realmAuthenticationExecutionsExecutionIdGet(realm, executionId, (error, data, response) => {
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
 **executionId** | **String**| Execution id | 

### Return type

null (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## realmAuthenticationExecutionsExecutionIdLowerPriorityPost

> realmAuthenticationExecutionsExecutionIdLowerPriorityPost(realm, executionId)

Lower execution’s priority

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.AuthenticationManagementApi();
let realm = "realm_example"; // String | realm name (not id!)
let executionId = "executionId_example"; // String | Execution id
apiInstance.realmAuthenticationExecutionsExecutionIdLowerPriorityPost(realm, executionId, (error, data, response) => {
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
 **executionId** | **String**| Execution id | 

### Return type

null (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## realmAuthenticationExecutionsExecutionIdRaisePriorityPost

> realmAuthenticationExecutionsExecutionIdRaisePriorityPost(realm, executionId)

Raise execution’s priority

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.AuthenticationManagementApi();
let realm = "realm_example"; // String | realm name (not id!)
let executionId = "executionId_example"; // String | Execution id
apiInstance.realmAuthenticationExecutionsExecutionIdRaisePriorityPost(realm, executionId, (error, data, response) => {
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
 **executionId** | **String**| Execution id | 

### Return type

null (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## realmAuthenticationExecutionsPost

> realmAuthenticationExecutionsPost(realm, authenticationExecutionRepresentation)

Add new authentication execution

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.AuthenticationManagementApi();
let realm = "realm_example"; // String | realm name (not id!)
let authenticationExecutionRepresentation = new KeycloakAdminRestApi.AuthenticationExecutionRepresentation(); // AuthenticationExecutionRepresentation | JSON model describing authentication execution
apiInstance.realmAuthenticationExecutionsPost(realm, authenticationExecutionRepresentation, (error, data, response) => {
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
 **authenticationExecutionRepresentation** | [**AuthenticationExecutionRepresentation**](AuthenticationExecutionRepresentation.md)| JSON model describing authentication execution | 

### Return type

null (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## realmAuthenticationFlowsFlowAliasCopyPost

> realmAuthenticationFlowsFlowAliasCopyPost(realm, flowAlias, requestBody)

Copy existing authentication flow under a new name   The new name is given as &#39;newName&#39; attribute of the passed JSON object

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.AuthenticationManagementApi();
let realm = "realm_example"; // String | realm name (not id!)
let flowAlias = "flowAlias_example"; // String | Name of the existing authentication flow
let requestBody = {key: null}; // {String: Object} | JSON containing 'newName' attribute
apiInstance.realmAuthenticationFlowsFlowAliasCopyPost(realm, flowAlias, requestBody, (error, data, response) => {
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
 **flowAlias** | **String**| Name of the existing authentication flow | 
 **requestBody** | [**{String: Object}**](Object.md)| JSON containing &#39;newName&#39; attribute | 

### Return type

null (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## realmAuthenticationFlowsFlowAliasExecutionsExecutionPost

> realmAuthenticationFlowsFlowAliasExecutionsExecutionPost(realm, flowAlias, requestBody)

Add new authentication execution to a flow

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.AuthenticationManagementApi();
let realm = "realm_example"; // String | realm name (not id!)
let flowAlias = "flowAlias_example"; // String | Alias of parent flow
let requestBody = {key: null}; // {String: Object} | New execution JSON data containing 'provider' attribute
apiInstance.realmAuthenticationFlowsFlowAliasExecutionsExecutionPost(realm, flowAlias, requestBody, (error, data, response) => {
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
 **flowAlias** | **String**| Alias of parent flow | 
 **requestBody** | [**{String: Object}**](Object.md)| New execution JSON data containing &#39;provider&#39; attribute | 

### Return type

null (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## realmAuthenticationFlowsFlowAliasExecutionsFlowPost

> realmAuthenticationFlowsFlowAliasExecutionsFlowPost(realm, flowAlias, requestBody)

Add new flow with new execution to existing flow

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.AuthenticationManagementApi();
let realm = "realm_example"; // String | realm name (not id!)
let flowAlias = "flowAlias_example"; // String | Alias of parent authentication flow
let requestBody = {key: null}; // {String: Object} | New authentication flow / execution JSON data containing 'alias', 'type', 'provider', and 'description' attributes
apiInstance.realmAuthenticationFlowsFlowAliasExecutionsFlowPost(realm, flowAlias, requestBody, (error, data, response) => {
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
 **flowAlias** | **String**| Alias of parent authentication flow | 
 **requestBody** | [**{String: Object}**](Object.md)| New authentication flow / execution JSON data containing &#39;alias&#39;, &#39;type&#39;, &#39;provider&#39;, and &#39;description&#39; attributes | 

### Return type

null (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## realmAuthenticationFlowsFlowAliasExecutionsGet

> realmAuthenticationFlowsFlowAliasExecutionsGet(realm, flowAlias)

Get authentication executions for a flow

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.AuthenticationManagementApi();
let realm = "realm_example"; // String | realm name (not id!)
let flowAlias = "flowAlias_example"; // String | Flow alias
apiInstance.realmAuthenticationFlowsFlowAliasExecutionsGet(realm, flowAlias, (error, data, response) => {
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
 **flowAlias** | **String**| Flow alias | 

### Return type

null (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## realmAuthenticationFlowsFlowAliasExecutionsPut

> realmAuthenticationFlowsFlowAliasExecutionsPut(realm, flowAlias, authenticationExecutionInfoRepresentation)

Update authentication executions of a flow

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.AuthenticationManagementApi();
let realm = "realm_example"; // String | realm name (not id!)
let flowAlias = "flowAlias_example"; // String | Flow alias
let authenticationExecutionInfoRepresentation = new KeycloakAdminRestApi.AuthenticationExecutionInfoRepresentation(); // AuthenticationExecutionInfoRepresentation | 
apiInstance.realmAuthenticationFlowsFlowAliasExecutionsPut(realm, flowAlias, authenticationExecutionInfoRepresentation, (error, data, response) => {
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
 **flowAlias** | **String**| Flow alias | 
 **authenticationExecutionInfoRepresentation** | [**AuthenticationExecutionInfoRepresentation**](AuthenticationExecutionInfoRepresentation.md)|  | 

### Return type

null (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## realmAuthenticationFlowsGet

> [AuthenticationFlowRepresentation] realmAuthenticationFlowsGet(realm)

Get authentication flows   Returns a list of authentication flows.

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.AuthenticationManagementApi();
let realm = "realm_example"; // String | realm name (not id!)
apiInstance.realmAuthenticationFlowsGet(realm, (error, data, response) => {
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

[**[AuthenticationFlowRepresentation]**](AuthenticationFlowRepresentation.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## realmAuthenticationFlowsIdDelete

> realmAuthenticationFlowsIdDelete(realm, id)

Delete an authentication flow

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.AuthenticationManagementApi();
let realm = "realm_example"; // String | realm name (not id!)
let id = "id_example"; // String | Flow id
apiInstance.realmAuthenticationFlowsIdDelete(realm, id, (error, data, response) => {
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
 **id** | **String**| Flow id | 

### Return type

null (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## realmAuthenticationFlowsIdGet

> AuthenticationFlowRepresentation realmAuthenticationFlowsIdGet(realm, id)

Get authentication flow for id

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.AuthenticationManagementApi();
let realm = "realm_example"; // String | realm name (not id!)
let id = "id_example"; // String | Flow id
apiInstance.realmAuthenticationFlowsIdGet(realm, id, (error, data, response) => {
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
 **id** | **String**| Flow id | 

### Return type

[**AuthenticationFlowRepresentation**](AuthenticationFlowRepresentation.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## realmAuthenticationFlowsIdPut

> realmAuthenticationFlowsIdPut(realm, id, authenticationFlowRepresentation)

Update an authentication flow

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.AuthenticationManagementApi();
let realm = "realm_example"; // String | realm name (not id!)
let id = "id_example"; // String | Flow id
let authenticationFlowRepresentation = new KeycloakAdminRestApi.AuthenticationFlowRepresentation(); // AuthenticationFlowRepresentation | Authentication flow representation
apiInstance.realmAuthenticationFlowsIdPut(realm, id, authenticationFlowRepresentation, (error, data, response) => {
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
 **id** | **String**| Flow id | 
 **authenticationFlowRepresentation** | [**AuthenticationFlowRepresentation**](AuthenticationFlowRepresentation.md)| Authentication flow representation | 

### Return type

null (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## realmAuthenticationFlowsPost

> realmAuthenticationFlowsPost(realm, authenticationFlowRepresentation)

Create a new authentication flow

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.AuthenticationManagementApi();
let realm = "realm_example"; // String | realm name (not id!)
let authenticationFlowRepresentation = new KeycloakAdminRestApi.AuthenticationFlowRepresentation(); // AuthenticationFlowRepresentation | Authentication flow representation
apiInstance.realmAuthenticationFlowsPost(realm, authenticationFlowRepresentation, (error, data, response) => {
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
 **authenticationFlowRepresentation** | [**AuthenticationFlowRepresentation**](AuthenticationFlowRepresentation.md)| Authentication flow representation | 

### Return type

null (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## realmAuthenticationFormActionProvidersGet

> [{String: Object}] realmAuthenticationFormActionProvidersGet(realm)

Get form action providers   Returns a list of form action providers.

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.AuthenticationManagementApi();
let realm = "realm_example"; // String | realm name (not id!)
apiInstance.realmAuthenticationFormActionProvidersGet(realm, (error, data, response) => {
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


## realmAuthenticationFormProvidersGet

> [{String: Object}] realmAuthenticationFormProvidersGet(realm)

Get form providers   Returns a list of form providers.

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.AuthenticationManagementApi();
let realm = "realm_example"; // String | realm name (not id!)
apiInstance.realmAuthenticationFormProvidersGet(realm, (error, data, response) => {
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


## realmAuthenticationPerClientConfigDescriptionGet

> {String: Object} realmAuthenticationPerClientConfigDescriptionGet(realm)

Get configuration descriptions for all clients

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.AuthenticationManagementApi();
let realm = "realm_example"; // String | realm name (not id!)
apiInstance.realmAuthenticationPerClientConfigDescriptionGet(realm, (error, data, response) => {
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


## realmAuthenticationRegisterRequiredActionPost

> realmAuthenticationRegisterRequiredActionPost(realm, requestBody)

Register a new required actions

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.AuthenticationManagementApi();
let realm = "realm_example"; // String | realm name (not id!)
let requestBody = {key: null}; // {String: Object} | JSON containing 'providerId', and 'name' attributes.
apiInstance.realmAuthenticationRegisterRequiredActionPost(realm, requestBody, (error, data, response) => {
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
 **requestBody** | [**{String: Object}**](Object.md)| JSON containing &#39;providerId&#39;, and &#39;name&#39; attributes. | 

### Return type

null (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## realmAuthenticationRequiredActionsAliasDelete

> realmAuthenticationRequiredActionsAliasDelete(realm, alias)

Delete required action

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.AuthenticationManagementApi();
let realm = "realm_example"; // String | realm name (not id!)
let alias = "alias_example"; // String | Alias of required action
apiInstance.realmAuthenticationRequiredActionsAliasDelete(realm, alias, (error, data, response) => {
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
 **alias** | **String**| Alias of required action | 

### Return type

null (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## realmAuthenticationRequiredActionsAliasGet

> RequiredActionProviderRepresentation realmAuthenticationRequiredActionsAliasGet(realm, alias)

Get required action for alias

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.AuthenticationManagementApi();
let realm = "realm_example"; // String | realm name (not id!)
let alias = "alias_example"; // String | Alias of required action
apiInstance.realmAuthenticationRequiredActionsAliasGet(realm, alias, (error, data, response) => {
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
 **alias** | **String**| Alias of required action | 

### Return type

[**RequiredActionProviderRepresentation**](RequiredActionProviderRepresentation.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## realmAuthenticationRequiredActionsAliasLowerPriorityPost

> realmAuthenticationRequiredActionsAliasLowerPriorityPost(realm, alias)

Lower required action’s priority

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.AuthenticationManagementApi();
let realm = "realm_example"; // String | realm name (not id!)
let alias = "alias_example"; // String | Alias of required action
apiInstance.realmAuthenticationRequiredActionsAliasLowerPriorityPost(realm, alias, (error, data, response) => {
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
 **alias** | **String**| Alias of required action | 

### Return type

null (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## realmAuthenticationRequiredActionsAliasPut

> realmAuthenticationRequiredActionsAliasPut(realm, alias, requiredActionProviderRepresentation)

Update required action

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.AuthenticationManagementApi();
let realm = "realm_example"; // String | realm name (not id!)
let alias = "alias_example"; // String | Alias of required action
let requiredActionProviderRepresentation = new KeycloakAdminRestApi.RequiredActionProviderRepresentation(); // RequiredActionProviderRepresentation | JSON describing new state of required action
apiInstance.realmAuthenticationRequiredActionsAliasPut(realm, alias, requiredActionProviderRepresentation, (error, data, response) => {
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
 **alias** | **String**| Alias of required action | 
 **requiredActionProviderRepresentation** | [**RequiredActionProviderRepresentation**](RequiredActionProviderRepresentation.md)| JSON describing new state of required action | 

### Return type

null (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## realmAuthenticationRequiredActionsAliasRaisePriorityPost

> realmAuthenticationRequiredActionsAliasRaisePriorityPost(realm, alias)

Raise required action’s priority

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.AuthenticationManagementApi();
let realm = "realm_example"; // String | realm name (not id!)
let alias = "alias_example"; // String | Alias of required action
apiInstance.realmAuthenticationRequiredActionsAliasRaisePriorityPost(realm, alias, (error, data, response) => {
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
 **alias** | **String**| Alias of required action | 

### Return type

null (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## realmAuthenticationRequiredActionsGet

> [RequiredActionProviderRepresentation] realmAuthenticationRequiredActionsGet(realm)

Get required actions   Returns a list of required actions.

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.AuthenticationManagementApi();
let realm = "realm_example"; // String | realm name (not id!)
apiInstance.realmAuthenticationRequiredActionsGet(realm, (error, data, response) => {
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

[**[RequiredActionProviderRepresentation]**](RequiredActionProviderRepresentation.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## realmAuthenticationUnregisteredRequiredActionsGet

> [{String: Object}] realmAuthenticationUnregisteredRequiredActionsGet(realm)

Get unregistered required actions   Returns a list of unregistered required actions.

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.AuthenticationManagementApi();
let realm = "realm_example"; // String | realm name (not id!)
apiInstance.realmAuthenticationUnregisteredRequiredActionsGet(realm, (error, data, response) => {
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

