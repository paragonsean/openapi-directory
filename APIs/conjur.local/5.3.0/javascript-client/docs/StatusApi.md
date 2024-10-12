# Conjur.StatusApi

All URIs are relative to *http://conjur.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getAuthenticators**](StatusApi.md#getAuthenticators) | **GET** /authenticators | Details about which authenticators are on the Conjur Server
[**getGCPAuthenticatorStatus**](StatusApi.md#getGCPAuthenticatorStatus) | **GET** /authn-gcp/{account}/status | Details whether an authentication service has been configured properly
[**getServiceAuthenticatorStatus**](StatusApi.md#getServiceAuthenticatorStatus) | **GET** /{authenticator}/{service_id}/{account}/status | Details whether an authentication service has been configured properly
[**health**](StatusApi.md#health) | **GET** /health | Health info about conjur
[**info**](StatusApi.md#info) | **GET** /info | Basic information about the Conjur Enterprise server
[**remoteHealth**](StatusApi.md#remoteHealth) | **GET** /remote_health/{remote} | Health info about a given Conjur Enterprise server
[**whoAmI**](StatusApi.md#whoAmI) | **GET** /whoami | Provides information about the client making an API request.



## getAuthenticators

> GetAuthenticators200Response getAuthenticators(opts)

Details about which authenticators are on the Conjur Server

Response contains three members: installed, configured, and enabled.  installed: The authenticator is implemented in Conjur and is available for configuration configured: The authenticator has a webservice in the DB that was loaded by policy enabled: The authenticator is enabled (in the DB or in the ENV) and is ready for authentication 

### Example

```javascript
import Conjur from 'conjur';
let defaultClient = Conjur.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: conjurAuth
let conjurAuth = defaultClient.authentications['conjurAuth'];
conjurAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//conjurAuth.apiKeyPrefix = 'Token';

let apiInstance = new Conjur.StatusApi();
let opts = {
  'xRequestId': "test-id" // String | Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one. 
};
apiInstance.getAuthenticators(opts, (error, data, response) => {
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
 **xRequestId** | **String**| Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one.  | [optional] 

### Return type

[**GetAuthenticators200Response**](GetAuthenticators200Response.md)

### Authorization

[basicAuth](../README.md#basicAuth), [conjurKubernetesMutualTls](../README.md#conjurKubernetesMutualTls), [conjurAuth](../README.md#conjurAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getGCPAuthenticatorStatus

> getGCPAuthenticatorStatus(account, opts)

Details whether an authentication service has been configured properly

Once the status webservice has been properly configured and the relevant user groups have been given permissions to access the status webservice, the users in those groups can check the status of the authenticator.  This operation only supports the GCP authenticator  See [Conjur Documentation](https://docs.conjur.org/Latest/en/Content/Integrations/Authn-status.htm) for details on setting up the authenticator status webservice. 

### Example

```javascript
import Conjur from 'conjur';
let defaultClient = Conjur.ApiClient.instance;
// Configure API key authorization: conjurAuth
let conjurAuth = defaultClient.authentications['conjurAuth'];
conjurAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//conjurAuth.apiKeyPrefix = 'Token';

let apiInstance = new Conjur.StatusApi();
let account = "dev"; // String | The organization account name
let opts = {
  'xRequestId': "test-id" // String | Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one. 
};
apiInstance.getGCPAuthenticatorStatus(account, opts, (error, data, response) => {
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
 **account** | **String**| The organization account name | 
 **xRequestId** | **String**| Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one.  | [optional] 

### Return type

null (empty response body)

### Authorization

[conjurAuth](../README.md#conjurAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getServiceAuthenticatorStatus

> GetServiceAuthenticatorStatus200Response getServiceAuthenticatorStatus(authenticator, serviceId, account, opts)

Details whether an authentication service has been configured properly

Once the status webservice has been properly configured and the relevant user groups have been given permissions to access the status webservice, the users in those groups can check the status of the authenticator.  Supported Authenticators:   - Azure   - OIDC  Not Supported:   - AWS IAM   - Kubernetes   - LDAP  See [Conjur Documentation](https://docs.conjur.org/Latest/en/Content/Integrations/Authn-status.htm) for details on setting up the authenticator status webservice. 

### Example

```javascript
import Conjur from 'conjur';
let defaultClient = Conjur.ApiClient.instance;
// Configure API key authorization: conjurAuth
let conjurAuth = defaultClient.authentications['conjurAuth'];
conjurAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//conjurAuth.apiKeyPrefix = 'Token';

let apiInstance = new Conjur.StatusApi();
let authenticator = "authn-oidc"; // String | The type of authenticator
let serviceId = "prod%2fgke"; // String | URL-Encoded authenticator service ID
let account = "dev"; // String | The organization account name
let opts = {
  'xRequestId': "test-id" // String | Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one. 
};
apiInstance.getServiceAuthenticatorStatus(authenticator, serviceId, account, opts, (error, data, response) => {
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
 **authenticator** | **String**| The type of authenticator | 
 **serviceId** | **String**| URL-Encoded authenticator service ID | 
 **account** | **String**| The organization account name | 
 **xRequestId** | **String**| Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one.  | [optional] 

### Return type

[**GetServiceAuthenticatorStatus200Response**](GetServiceAuthenticatorStatus200Response.md)

### Authorization

[conjurAuth](../README.md#conjurAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## health

> Object health()

Health info about conjur

You can request health checks against any cluster node using the Conjur API. These routes do not require authentication.  The health check attempts an internal HTTP or TCP connection to each Conjur Enterprise service. It also attempts a simple transaction against all internal databases. 

### Example

```javascript
import Conjur from 'conjur';
let defaultClient = Conjur.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: conjurAuth
let conjurAuth = defaultClient.authentications['conjurAuth'];
conjurAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//conjurAuth.apiKeyPrefix = 'Token';

let apiInstance = new Conjur.StatusApi();
apiInstance.health((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

**Object**

### Authorization

[basicAuth](../README.md#basicAuth), [conjurKubernetesMutualTls](../README.md#conjurKubernetesMutualTls), [conjurAuth](../README.md#conjurAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## info

> Info200Response info()

Basic information about the Conjur Enterprise server

Information about the Conjur Enterprise node which was queried against.  Includes authenticator info, release/version info, configuration details, internal services, and role information. 

### Example

```javascript
import Conjur from 'conjur';
let defaultClient = Conjur.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: conjurAuth
let conjurAuth = defaultClient.authentications['conjurAuth'];
conjurAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//conjurAuth.apiKeyPrefix = 'Token';

let apiInstance = new Conjur.StatusApi();
apiInstance.info((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**Info200Response**](Info200Response.md)

### Authorization

[basicAuth](../README.md#basicAuth), [conjurKubernetesMutualTls](../README.md#conjurKubernetesMutualTls), [conjurAuth](../README.md#conjurAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## remoteHealth

> Object remoteHealth(remote)

Health info about a given Conjur Enterprise server

Use the remote_health route to check the health of any Conjur Enterprise Server from any other Conjur Enterprise Server. With this route, you can check master health relative to a follower, or follower health relative to a standby, and so on. 

### Example

```javascript
import Conjur from 'conjur';
let defaultClient = Conjur.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: conjurAuth
let conjurAuth = defaultClient.authentications['conjurAuth'];
conjurAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//conjurAuth.apiKeyPrefix = 'Token';

let apiInstance = new Conjur.StatusApi();
let remote = "conjur.myorg.com"; // String | The hostname of the remote to check
apiInstance.remoteHealth(remote, (error, data, response) => {
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
 **remote** | **String**| The hostname of the remote to check | 

### Return type

**Object**

### Authorization

[basicAuth](../README.md#basicAuth), [conjurKubernetesMutualTls](../README.md#conjurKubernetesMutualTls), [conjurAuth](../README.md#conjurAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## whoAmI

> WhoAmI200Response whoAmI(opts)

Provides information about the client making an API request.

WhoAmI provides information about the client making an API request. It can be used to help troubleshoot configuration by verifying authentication and the client IP address for audit and network access restrictions. For more information, see Host Attributes. 

### Example

```javascript
import Conjur from 'conjur';
let defaultClient = Conjur.ApiClient.instance;
// Configure API key authorization: conjurAuth
let conjurAuth = defaultClient.authentications['conjurAuth'];
conjurAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//conjurAuth.apiKeyPrefix = 'Token';

let apiInstance = new Conjur.StatusApi();
let opts = {
  'xRequestId': "test-id" // String | Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one. 
};
apiInstance.whoAmI(opts, (error, data, response) => {
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
 **xRequestId** | **String**| Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one.  | [optional] 

### Return type

[**WhoAmI200Response**](WhoAmI200Response.md)

### Authorization

[conjurAuth](../README.md#conjurAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

