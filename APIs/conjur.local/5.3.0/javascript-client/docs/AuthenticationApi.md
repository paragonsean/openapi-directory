# Conjur.AuthenticationApi

All URIs are relative to *http://conjur.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**changePassword**](AuthenticationApi.md#changePassword) | **PUT** /authn/{account}/password | Changes a user’s password.
[**enableAuthenticator**](AuthenticationApi.md#enableAuthenticator) | **PATCH** /{authenticator}/{account} | Enables or disables authenticator defined without service_id.
[**enableAuthenticatorInstance**](AuthenticationApi.md#enableAuthenticatorInstance) | **PATCH** /{authenticator}/{service_id}/{account} | Enables or disables authenticator service instances.
[**getAPIKey**](AuthenticationApi.md#getAPIKey) | **GET** /authn/{account}/login | Gets the API key of a user given the username and password via HTTP Basic Authentication. 
[**getAPIKeyViaLDAP**](AuthenticationApi.md#getAPIKeyViaLDAP) | **GET** /authn-ldap/{service_id}/{account}/login | Gets the Conjur API key of a user given the LDAP username and password via HTTP Basic Authentication. 
[**getAccessToken**](AuthenticationApi.md#getAccessToken) | **POST** /authn/{account}/{login}/authenticate | Gets a short-lived access token, which is required in the header of most subsequent API requests. 
[**getAccessTokenViaAWS**](AuthenticationApi.md#getAccessTokenViaAWS) | **POST** /authn-iam/{service_id}/{account}/{login}/authenticate | Get a short-lived access token for applications running in AWS.
[**getAccessTokenViaAzure**](AuthenticationApi.md#getAccessTokenViaAzure) | **POST** /authn-azure/{service_id}/{account}/{login}/authenticate | Gets a short-lived access token for applications running in Azure.
[**getAccessTokenViaGCP**](AuthenticationApi.md#getAccessTokenViaGCP) | **POST** /authn-gcp/{account}/authenticate | Gets a short-lived access token for applications running in Google Cloud Platform. 
[**getAccessTokenViaJWT**](AuthenticationApi.md#getAccessTokenViaJWT) | **POST** /authn-jwt/{service_id}/{account}/authenticate | Gets a short-lived access token for applications using JSON Web Token (JWT) to access the Conjur API. 
[**getAccessTokenViaJWTWithId**](AuthenticationApi.md#getAccessTokenViaJWTWithId) | **POST** /authn-jwt/{service_id}/{account}/{id}/authenticate | Gets a short-lived access token for applications using JSON Web Token (JWT) to access the Conjur API. Covers the case of use of optional URL parameter \&quot;ID\&quot; 
[**getAccessTokenViaKubernetes**](AuthenticationApi.md#getAccessTokenViaKubernetes) | **POST** /authn-k8s/{service_id}/{account}/{login}/authenticate | Gets a short-lived access token for applications running in Kubernetes.
[**getAccessTokenViaLDAP**](AuthenticationApi.md#getAccessTokenViaLDAP) | **POST** /authn-ldap/{service_id}/{account}/{login}/authenticate | Gets a short-lived access token for users and hosts using their LDAP identity to access the Conjur API. 
[**getAccessTokenViaOIDC**](AuthenticationApi.md#getAccessTokenViaOIDC) | **POST** /authn-oidc/{service_id}/{account}/authenticate | Gets a short-lived access token for applications using OpenID Connect (OIDC) to access the Conjur API. 
[**k8sInjectClientCert**](AuthenticationApi.md#k8sInjectClientCert) | **POST** /authn-k8s/{service_id}/inject_client_cert | For applications running in Kubernetes; sends Conjur a certificate signing request (CSR) and requests a client certificate injected into the application&#39;s Kubernetes pod. 
[**rotateApiKey**](AuthenticationApi.md#rotateApiKey) | **PUT** /authn/{account}/api_key | Rotates a role&#39;s API key.



## changePassword

> changePassword(account, body, opts)

Changes a user’s password.

You must provide the login name and current password or API key of the user whose password is to be updated in an HTTP Basic Authentication header. Also replaces the user’s API key with a new securely generated random value. You can fetch the new API key using the Login method.  The Basic authentication-compliant header is formed by: 1. Concatenating the role&#39;s name, a literal colon character &#39;:&#39;,    and the password or API key to create the authentication string. 2. Base64-encoding the authentication string. 3. Prefixing the authentication string with the scheme: &#x60;Basic &#x60;    (note the required space). 4. Providing the result as the value of the &#x60;Authorization&#x60; HTTP header:    &#x60;Authorization: Basic &lt;authentication string&gt;&#x60;.  Your HTTP/REST client probably provides HTTP basic authentication support. For example, &#x60;curl&#x60; and all of the Conjur client libraries provide this.  Note that machine roles (Hosts) do not have passwords. They authenticate using their API keys, while passwords are only used by human users. 

### Example

```javascript
import Conjur from 'conjur';
let defaultClient = Conjur.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new Conjur.AuthenticationApi();
let account = "account_example"; // String | Organization account name
let body = "body_example"; // String | New password
let opts = {
  'xRequestId': "test-id" // String | Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one. 
};
apiInstance.changePassword(account, body, opts, (error, data, response) => {
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
 **account** | **String**| Organization account name | 
 **body** | **String**| New password | 
 **xRequestId** | **String**| Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one.  | [optional] 

### Return type

null (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: text/plain
- **Accept**: Not defined


## enableAuthenticator

> enableAuthenticator(authenticator, account, opts)

Enables or disables authenticator defined without service_id.

Allows you to either enable or disable a given authenticator that does not have service_id (For example: authn-gcp).  When you enable or disable an authenticator via this endpoint, the status of the authenticator is stored in the Conjur database. The enablement status of the authenticator service may be overridden by setting the &#x60;CONJUR_AUTHENTICATORS&#x60; environment variable on the Conjur server; in the case where this environment variable is set, the database record of whether the authenticator service is enabled will be ignored.  **This endpoint is part of an early implementation of support for enabling Conjur authenticators via the API, and is currently available at the Community (or early alpha) level. This endpoint is still subject to breaking changes in the future.** 

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

let apiInstance = new Conjur.AuthenticationApi();
let authenticator = "authn-gcp"; // String | The authenticator to update
let account = "dev"; // String | Organization account name
let opts = {
  'xRequestId': "test-id", // String | Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one. 
  'enabled': true // Boolean | 
};
apiInstance.enableAuthenticator(authenticator, account, opts, (error, data, response) => {
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
 **authenticator** | **String**| The authenticator to update | 
 **account** | **String**| Organization account name | 
 **xRequestId** | **String**| Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one.  | [optional] 
 **enabled** | **Boolean**|  | [optional] 

### Return type

null (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth), [conjurKubernetesMutualTls](../README.md#conjurKubernetesMutualTls), [conjurAuth](../README.md#conjurAuth)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: Not defined


## enableAuthenticatorInstance

> enableAuthenticatorInstance(authenticator, serviceId, account, opts)

Enables or disables authenticator service instances.

Allows you to either enable or disable a given authenticator service instance.  When you enable or disable an authenticator service instance via this endpoint, the status of the authenticator service instance is stored in the Conjur database. The enablement status of the authenticator service instance may be overridden by setting the &#x60;CONJUR_AUTHENTICATORS&#x60; environment variable on the Conjur server; in the case where this environment variable is set, the database record of whether the authenticator service instance is enabled will be ignored.  **This endpoint is part of an early implementation of support for enabling Conjur authenticators via the API, and is currently available at the Community (or early alpha) level. This endpoint is still subject to breaking changes in the future.** 

### Example

```javascript
import Conjur from 'conjur';
let defaultClient = Conjur.ApiClient.instance;
// Configure API key authorization: conjurAuth
let conjurAuth = defaultClient.authentications['conjurAuth'];
conjurAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//conjurAuth.apiKeyPrefix = 'Token';

let apiInstance = new Conjur.AuthenticationApi();
let authenticator = new Conjur.ERRORUNKNOWN(); // ERRORUNKNOWN | The authenticator to update
let serviceId = "prod%2fgke"; // String | URL-Encoded authenticator service ID
let account = "dev"; // String | Organization account name
let opts = {
  'xRequestId': "test-id" // String | Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one. 
};
apiInstance.enableAuthenticatorInstance(authenticator, serviceId, account, opts, (error, data, response) => {
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
 **authenticator** | [**ERRORUNKNOWN**](.md)| The authenticator to update | 
 **serviceId** | **String**| URL-Encoded authenticator service ID | 
 **account** | **String**| Organization account name | 
 **xRequestId** | **String**| Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one.  | [optional] 

### Return type

null (empty response body)

### Authorization

[conjurAuth](../README.md#conjurAuth)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: Not defined


## getAPIKey

> String getAPIKey(account, opts)

Gets the API key of a user given the username and password via HTTP Basic Authentication. 

Passwords are stored in the Conjur database using &#x60;bcrypt&#x60; with a work factor of 12. Therefore, login is a fairly expensive operation. However, once the API key is obtained, it may be used to inexpensively obtain access tokens by calling the Authenticate method. An access token is required to use most other parts of the Conjur API.  The Basic authentication-compliant header is formed by: 1. Concatenating the role&#39;s name, a literal colon character &#39;:&#39;,    and the password or API key to create the authentication string. 2. Base64-encoding the authentication string. 3. Prefixing the authentication string with the scheme: &#x60;Basic &#x60;    (note the required space). 4. Providing the result as the value of the &#x60;Authorization&#x60; HTTP header:    &#x60;Authorization: Basic &lt;authentication string&gt;&#x60;.  Your HTTP/REST client probably provides HTTP basic authentication support. For example, &#x60;curl&#x60; and all of the Conjur client libraries provide this.  Note that machine roles (Hosts) do not have passwords and do not need to use this endpoint. 

### Example

```javascript
import Conjur from 'conjur';
let defaultClient = Conjur.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new Conjur.AuthenticationApi();
let account = "account_example"; // String | Organization account name
let opts = {
  'xRequestId': "test-id" // String | Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one. 
};
apiInstance.getAPIKey(account, opts, (error, data, response) => {
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
 **account** | **String**| Organization account name | 
 **xRequestId** | **String**| Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one.  | [optional] 

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/plain


## getAPIKeyViaLDAP

> getAPIKeyViaLDAP(serviceId, account, opts)

Gets the Conjur API key of a user given the LDAP username and password via HTTP Basic Authentication. 

Exchange your LDAP credentials for a Conjur API key. Once the API key is obtained, it may be used to inexpensively obtain access tokens by calling the Authenticate method. An access token is required to use most other parts of the Conjur API.  The Basic authentication-compliant header is formed by: 1. Concatenating the LDAP username, a literal colon character &#39;:&#39;,    and the password to create the authentication string. 2. Base64-encoding the authentication string. 3. Prefixing the authentication string with the scheme: &#x60;Basic &#x60;    (note the required space). 4. Providing the result as the value of the &#x60;Authorization&#x60; HTTP header:    &#x60;Authorization: Basic &lt;authentication string&gt;&#x60;.  Your HTTP/REST client probably provides HTTP basic authentication support. 

### Example

```javascript
import Conjur from 'conjur';
let defaultClient = Conjur.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new Conjur.AuthenticationApi();
let serviceId = "prod%2fgke"; // String | URL-Encoded authenticator service ID
let account = "account_example"; // String | Organization account name
let opts = {
  'xRequestId': "test-id" // String | Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one. 
};
apiInstance.getAPIKeyViaLDAP(serviceId, account, opts, (error, data, response) => {
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
 **serviceId** | **String**| URL-Encoded authenticator service ID | 
 **account** | **String**| Organization account name | 
 **xRequestId** | **String**| Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one.  | [optional] 

### Return type

null (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getAccessToken

> String getAccessToken(account, login, body, opts)

Gets a short-lived access token, which is required in the header of most subsequent API requests. 

A client can obtain an access token by presenting a valid login name and API key.  The access token is used to communicate to the REST API that the bearer of the token has been authorized to access the API and perform specific actions specified by the scope that was granted during authorization.  The &#x60;login&#x60; must be URL encoded. For example, &#x60;alice@devops&#x60; must be encoded as &#x60;alice%40devops&#x60;.  The &#x60;service_id&#x60;, if given, must be URL encoded. For example, &#x60;prod/gke&#x60; must be encoded as &#x60;prod%2Fgke&#x60;.  For host authentication, the &#x60;login&#x60; is the host ID with the prefix &#x60;host/&#x60;. For example, the host webserver would login as &#x60;host/webserver&#x60;, and would be encoded as &#x60;host%2Fwebserver&#x60;.  For API usage, the base64-encoded access token is ordinarily passed as an HTTP Authorization header as &#x60;Authorization: Token token&#x3D;&lt;base64-encoded token&gt;&#x60;.  This is the default authentication endpoint only. See other endpoints for details on authenticating to Conjur using another method, e.g. for applications running in Azure or Kubernetes. 

### Example

```javascript
import Conjur from 'conjur';

let apiInstance = new Conjur.AuthenticationApi();
let account = "account_example"; // String | Organization account name
let login = "admin"; // String | URL-encoded login name. For users, it’s the user ID. For hosts, the login name is `host/<host-id>`
let body = null; // Object | API Key
let opts = {
  'xRequestId': "test-id", // String | Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one. 
  'acceptEncoding': "'application/json'" // String | Setting the Accept-Encoding header to base64 will return a pre-encoded access token
};
apiInstance.getAccessToken(account, login, body, opts, (error, data, response) => {
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
 **account** | **String**| Organization account name | 
 **login** | **String**| URL-encoded login name. For users, it’s the user ID. For hosts, the login name is &#x60;host/&lt;host-id&gt;&#x60; | 
 **body** | **Object**| API Key | 
 **xRequestId** | **String**| Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one.  | [optional] 
 **acceptEncoding** | **String**| Setting the Accept-Encoding header to base64 will return a pre-encoded access token | [optional] [default to &#39;application/json&#39;]

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: text/plain
- **Accept**: text/plain


## getAccessTokenViaAWS

> getAccessTokenViaAWS(serviceId, account, login, body, opts)

Get a short-lived access token for applications running in AWS.

The access token is used to communicate to the REST API that the bearer of the token has been authorized to access the API and perform specific actions specified by the scope that was granted during authorization.  For API usage, the base64-encoded access token is ordinarily passed as an HTTP Authorization header as &#x60;Authorization: Token token&#x3D;&lt;base64-encoded token&gt;&#x60;.  The &#x60;login&#x60; must be URL encoded and the host ID must have the prefix &#x60;host/&#x60;. For example, the host webserver would login as &#x60;host/webserver&#x60;, and would be encoded as &#x60;host%2Fwebserver&#x60;.  The &#x60;service_id&#x60;, if given, must be URL encoded. For example, &#x60;prod/gke&#x60; must be encoded as &#x60;prod%2Fgke&#x60;.  For detailed instructions on authenticating to Conjur using this endpoint, reference the documentation: [AWS IAM Authenticator](https://docs.conjur.org/Latest/en/Content/Operations/Services/AWS_IAM_Authenticator.htm) (&#x60;authn-iam&#x60;). 

### Example

```javascript
import Conjur from 'conjur';

let apiInstance = new Conjur.AuthenticationApi();
let serviceId = "prod%2fgke"; // String | URL-Encoded authenticator service ID
let account = "account_example"; // String | Organization account name
let login = new Conjur.ERRORUNKNOWN(); // ERRORUNKNOWN | URL-encoded login name. For hosts, the login name is `host/<host-id>`
let body = "body_example"; // String | AWS Signature header
let opts = {
  'xRequestId': "test-id", // String | Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one. 
  'acceptEncoding': "'application/json'" // String | Setting the Accept-Encoding header to base64 will return a pre-encoded access token
};
apiInstance.getAccessTokenViaAWS(serviceId, account, login, body, opts, (error, data, response) => {
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
 **serviceId** | **String**| URL-Encoded authenticator service ID | 
 **account** | **String**| Organization account name | 
 **login** | [**ERRORUNKNOWN**](.md)| URL-encoded login name. For hosts, the login name is &#x60;host/&lt;host-id&gt;&#x60; | 
 **body** | **String**| AWS Signature header | 
 **xRequestId** | **String**| Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one.  | [optional] 
 **acceptEncoding** | **String**| Setting the Accept-Encoding header to base64 will return a pre-encoded access token | [optional] [default to &#39;application/json&#39;]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: text/plain
- **Accept**: Not defined


## getAccessTokenViaAzure

> getAccessTokenViaAzure(serviceId, account, login, opts)

Gets a short-lived access token for applications running in Azure.

The access token is used to communicate to the REST API that the bearer of the token has been authorized to access the API and perform specific actions specified by the scope that was granted during authorization.  For API usage, the base64-encoded access token is ordinarily passed as an HTTP Authorization header as &#x60;Authorization: Token token&#x3D;&lt;base64-encoded token&gt;&#x60;.  The &#x60;login&#x60; must be URL encoded and the host ID must have the prefix &#x60;host/&#x60;. For example, the host webserver would login as &#x60;host/webserver&#x60;, and would be encoded as &#x60;host%2Fwebserver&#x60;.  The &#x60;service_id&#x60;, if given, must be URL encoded. For example, &#x60;prod/gke&#x60; must be encoded as &#x60;prod%2Fgke&#x60;.  To authenticate to Conjur using this endpoint, reference the detailed documentation: [Azure Authenticator](https://docs.conjur.org/Latest/en/Content/Operations/Services/azure_authn.htm) (&#x60;authn-azure&#x60;). 

### Example

```javascript
import Conjur from 'conjur';

let apiInstance = new Conjur.AuthenticationApi();
let serviceId = "prod%2fgke"; // String | URL-Encoded authenticator service ID
let account = "account_example"; // String | Organization account name
let login = new Conjur.ERRORUNKNOWN(); // ERRORUNKNOWN | URL-encoded login name. For users, it’s the user ID. For hosts, the login name is `host/<host-id>`
let opts = {
  'xRequestId': "test-id", // String | Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one. 
  'acceptEncoding': "'application/json'", // String | Setting the Accept-Encoding header to base64 will return a pre-encoded access token
  'jwt': "jwt_example" // String | 
};
apiInstance.getAccessTokenViaAzure(serviceId, account, login, opts, (error, data, response) => {
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
 **serviceId** | **String**| URL-Encoded authenticator service ID | 
 **account** | **String**| Organization account name | 
 **login** | [**ERRORUNKNOWN**](.md)| URL-encoded login name. For users, it’s the user ID. For hosts, the login name is &#x60;host/&lt;host-id&gt;&#x60; | 
 **xRequestId** | **String**| Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one.  | [optional] 
 **acceptEncoding** | **String**| Setting the Accept-Encoding header to base64 will return a pre-encoded access token | [optional] [default to &#39;application/json&#39;]
 **jwt** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: Not defined


## getAccessTokenViaGCP

> getAccessTokenViaGCP(account, opts)

Gets a short-lived access token for applications running in Google Cloud Platform. 

Use the GCP Authenticator API to send an authentication request from a Google Cloud service to Conjur.  For more information, see [the documentation](https://docs.conjur.org/Latest/en/Content/Operations/Services/cjr-gcp-authn.htm). 

### Example

```javascript
import Conjur from 'conjur';

let apiInstance = new Conjur.AuthenticationApi();
let account = "dev"; // String | Organization account name
let opts = {
  'xRequestId': "test-id", // String | Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one. 
  'acceptEncoding': "acceptEncoding_example", // String | Setting the Accept-Encoding header to base64 will return a pre-encoded access token
  'jwt': "jwt_example" // String | 
};
apiInstance.getAccessTokenViaGCP(account, opts, (error, data, response) => {
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
 **account** | **String**| Organization account name | 
 **xRequestId** | **String**| Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one.  | [optional] 
 **acceptEncoding** | **String**| Setting the Accept-Encoding header to base64 will return a pre-encoded access token | [optional] 
 **jwt** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: Not defined


## getAccessTokenViaJWT

> getAccessTokenViaJWT(account, serviceId, opts)

Gets a short-lived access token for applications using JSON Web Token (JWT) to access the Conjur API. 

Use the JWT Authenticator to leverage the identity layer provided by JWT to authenticate with Conjur. 

### Example

```javascript
import Conjur from 'conjur';

let apiInstance = new Conjur.AuthenticationApi();
let account = "account_example"; // String | Organization account name
let serviceId = "prod%2fgke"; // String | URL-Encoded authenticator service ID
let opts = {
  'xRequestId': "test-id", // String | Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one. 
  'jwt': "jwt_example" // String | 
};
apiInstance.getAccessTokenViaJWT(account, serviceId, opts, (error, data, response) => {
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
 **account** | **String**| Organization account name | 
 **serviceId** | **String**| URL-Encoded authenticator service ID | 
 **xRequestId** | **String**| Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one.  | [optional] 
 **jwt** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: Not defined


## getAccessTokenViaJWTWithId

> getAccessTokenViaJWTWithId(account, id, serviceId, opts)

Gets a short-lived access token for applications using JSON Web Token (JWT) to access the Conjur API. Covers the case of use of optional URL parameter \&quot;ID\&quot; 

Use the JWT Authenticator to leverage the identity layer provided by JWT to authenticate with Conjur. 

### Example

```javascript
import Conjur from 'conjur';

let apiInstance = new Conjur.AuthenticationApi();
let account = "account_example"; // String | Organization account name
let id = "SomeUserID"; // String | Organization user id
let serviceId = "prod%2fgke"; // String | URL-Encoded authenticator service ID
let opts = {
  'xRequestId': "test-id" // String | Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one. 
};
apiInstance.getAccessTokenViaJWTWithId(account, id, serviceId, opts, (error, data, response) => {
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
 **account** | **String**| Organization account name | 
 **id** | **String**| Organization user id | 
 **serviceId** | **String**| URL-Encoded authenticator service ID | 
 **xRequestId** | **String**| Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one.  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: Not defined


## getAccessTokenViaKubernetes

> getAccessTokenViaKubernetes(serviceId, account, login, opts)

Gets a short-lived access token for applications running in Kubernetes.

The access token is used to communicate to the REST API that the bearer of the token has been authorized to access the API and perform specific actions specified by the scope that was granted during authorization.  For API usage, the base64-encoded access token is ordinarily passed as an HTTP Authorization header as &#x60;Authorization: Token token&#x3D;&lt;base64-encoded token&gt;&#x60;.  The &#x60;login&#x60; must be URL encoded and the host ID must have the prefix &#x60;host/&#x60;. For example, the host webserver would login as &#x60;host/webserver&#x60;, and would be encoded as &#x60;host%2Fwebserver&#x60;.  The &#x60;service_id&#x60;, if given, must be URL encoded. For example, &#x60;prod/gke&#x60; must be encoded as &#x60;prod%2Fgke&#x60;.  To authenticate to Conjur using this endpoint, reference the detailed documentation: [Kubernetes Authenticator](https://docs.conjur.org/Latest/en/Content/Operations/Services/k8s_auth.htm) (&#x60;authn-k8s&#x60;). 

### Example

```javascript
import Conjur from 'conjur';
let defaultClient = Conjur.ApiClient.instance;

let apiInstance = new Conjur.AuthenticationApi();
let serviceId = "prod%2fgke"; // String | URL-Encoded authenticator service ID
let account = "account_example"; // String | Organization account name
let login = new Conjur.ERRORUNKNOWN(); // ERRORUNKNOWN | URL-encoded login name. For users, it’s the user ID. For hosts, the login name is `host/<host-id>`
let opts = {
  'xRequestId': "test-id", // String | Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one. 
  'acceptEncoding': "'application/json'" // String | Setting the Accept-Encoding header to base64 will return a pre-encoded access token
};
apiInstance.getAccessTokenViaKubernetes(serviceId, account, login, opts, (error, data, response) => {
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
 **serviceId** | **String**| URL-Encoded authenticator service ID | 
 **account** | **String**| Organization account name | 
 **login** | [**ERRORUNKNOWN**](.md)| URL-encoded login name. For users, it’s the user ID. For hosts, the login name is &#x60;host/&lt;host-id&gt;&#x60; | 
 **xRequestId** | **String**| Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one.  | [optional] 
 **acceptEncoding** | **String**| Setting the Accept-Encoding header to base64 will return a pre-encoded access token | [optional] [default to &#39;application/json&#39;]

### Return type

null (empty response body)

### Authorization

[conjurKubernetesMutualTls](../README.md#conjurKubernetesMutualTls)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getAccessTokenViaLDAP

> getAccessTokenViaLDAP(serviceId, account, login, opts)

Gets a short-lived access token for users and hosts using their LDAP identity to access the Conjur API. 

The access token is used to communicate to the REST API that the bearer of the token has been authorized to access the API and perform specific actions specified by the scope that was granted during authorization.  For API usage, the base64-encoded access token is ordinarily passed as an HTTP Authorization header as &#x60;Authorization: Token token&#x3D;&lt;base64-encoded token&gt;&#x60;.  The &#x60;login&#x60; must be URL encoded. For example, &#x60;alice@devops&#x60; must be encoded as &#x60;alice%40devops&#x60;.  The &#x60;service_id&#x60;, if given, must be URL encoded. For example, &#x60;prod/gke&#x60; must be encoded as &#x60;prod%2Fgke&#x60;.  For host authentication, the &#x60;login&#x60; is the host ID with the prefix &#x60;host/&#x60;. For example, the host webserver would login as &#x60;host/webserver&#x60;, and would be encoded as &#x60;host%2Fwebserver&#x60;.  To authenticate to Conjur using a LDAP, reference the detailed documentation: [LDAP Authenticator](https://docs.conjur.org/Latest/en/Content/Integrations/ldap/ldap_authenticator.html) (&#x60;authn-ldap&#x60;). 

### Example

```javascript
import Conjur from 'conjur';

let apiInstance = new Conjur.AuthenticationApi();
let serviceId = "prod%2fgke"; // String | URL-Encoded authenticator service ID
let account = "account_example"; // String | Organization account name
let login = new Conjur.ERRORUNKNOWN(); // ERRORUNKNOWN | URL-encoded login name. For users, it’s the user ID. For hosts, the login name is `host/<host-id>`
let opts = {
  'xRequestId': "test-id", // String | Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one. 
  'acceptEncoding': "'application/json'", // String | Setting the Accept-Encoding header to base64 will return a pre-encoded access token
  'body': null // Object | API key
};
apiInstance.getAccessTokenViaLDAP(serviceId, account, login, opts, (error, data, response) => {
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
 **serviceId** | **String**| URL-Encoded authenticator service ID | 
 **account** | **String**| Organization account name | 
 **login** | [**ERRORUNKNOWN**](.md)| URL-encoded login name. For users, it’s the user ID. For hosts, the login name is &#x60;host/&lt;host-id&gt;&#x60; | 
 **xRequestId** | **String**| Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one.  | [optional] 
 **acceptEncoding** | **String**| Setting the Accept-Encoding header to base64 will return a pre-encoded access token | [optional] [default to &#39;application/json&#39;]
 **body** | **Object**| API key | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: text/plain
- **Accept**: Not defined


## getAccessTokenViaOIDC

> getAccessTokenViaOIDC(serviceId, account, opts)

Gets a short-lived access token for applications using OpenID Connect (OIDC) to access the Conjur API. 

Use the OIDC Authenticator to leverage the identity layer provided by OIDC to authenticate with Conjur.  For more information see [the documentation](https://docs.conjur.org/Latest/en/Content/OIDC/OIDC.htm). 

### Example

```javascript
import Conjur from 'conjur';

let apiInstance = new Conjur.AuthenticationApi();
let serviceId = "prod%2fgke"; // String | URL-Encoded authenticator service ID
let account = "account_example"; // String | Organization account name
let opts = {
  'xRequestId': "test-id", // String | Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one. 
  'idToken': "idToken_example" // String | 
};
apiInstance.getAccessTokenViaOIDC(serviceId, account, opts, (error, data, response) => {
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
 **serviceId** | **String**| URL-Encoded authenticator service ID | 
 **account** | **String**| Organization account name | 
 **xRequestId** | **String**| Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one.  | [optional] 
 **idToken** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: Not defined


## k8sInjectClientCert

> k8sInjectClientCert(serviceId, body, opts)

For applications running in Kubernetes; sends Conjur a certificate signing request (CSR) and requests a client certificate injected into the application&#39;s Kubernetes pod. 

This request sends a Certificate Signing Request to Conjur, which uses the Kubernetes API to inject a client certificate into the application pod.  This endpoint requires a properly configured Conjur Certificate Authority service alongside a properly configured and enabled Kubernetes authenticator. For detailed instructions, see [the documentation](https://docs.conjur.org/Latest/en/Content/Integrations/kubernetes.htm). 

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

let apiInstance = new Conjur.AuthenticationApi();
let serviceId = "prod%2fgke"; // String | URL-Encoded authenticator service ID
let body = "body_example"; // String | Valid certificate signing request that includes the host identity suffix as the CSR common name 
let opts = {
  'xRequestId': "test-id", // String | Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one. 
  'hostIdPrefix': "host/conjur/authn-k8s/my-authenticator-id/apps" // String | Dot-separated policy tree, prefixed by `host.`, where the application identity is defined
};
apiInstance.k8sInjectClientCert(serviceId, body, opts, (error, data, response) => {
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
 **serviceId** | **String**| URL-Encoded authenticator service ID | 
 **body** | **String**| Valid certificate signing request that includes the host identity suffix as the CSR common name  | 
 **xRequestId** | **String**| Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one.  | [optional] 
 **hostIdPrefix** | **String**| Dot-separated policy tree, prefixed by &#x60;host.&#x60;, where the application identity is defined | [optional] 

### Return type

null (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth), [conjurKubernetesMutualTls](../README.md#conjurKubernetesMutualTls), [conjurAuth](../README.md#conjurAuth)

### HTTP request headers

- **Content-Type**: text/plain
- **Accept**: Not defined


## rotateApiKey

> rotateApiKey(account, opts)

Rotates a role&#39;s API key.

Any role can rotate its own API key. The name and password (for users) or current API key (for hosts and users) of the role must be provided via HTTP Basic Authorization.  To rotate another role&#39;s API key, you may provide your name and password (for users) or current API key (for hosts and users) via HTTP Basic Authorization with the request. Alternatively, you may provide your Conjur access token via the standard Conjur &#x60;Authorization&#x60; header.  The Basic authentication-compliant header is formed by: 1. Concatenating the role&#39;s name, a literal colon character &#39;:&#39;,    and the password or API key to create the authentication string. 2. Base64-encoding the authentication string. 3. Prefixing the authentication string with the scheme: &#x60;Basic &#x60;    (note the required space). 4. Providing the result as the value of the &#x60;Authorization&#x60; HTTP header:    &#x60;Authorization: Basic &lt;authentication string&gt;&#x60;.  Your HTTP/REST client probably provides HTTP basic authentication support. For example, &#x60;curl&#x60; and all of the Conjur client libraries provide this.  If using the Conjur &#x60;Authorization&#x60; header, its value should be set to &#x60;Token token&#x3D;&lt;base64-encoded access token&gt;&#x60;.  Note that the body of the request must be the empty string. 

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

let apiInstance = new Conjur.AuthenticationApi();
let account = "account_example"; // String | Organization account name
let opts = {
  'xRequestId': "test-id", // String | Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one. 
  'role': "role_example" // String | (**Optional**) role specifier in `{kind}:{identifier}` format  ##### Permissions required  `update` privilege on the role whose API key is being rotated. 
};
apiInstance.rotateApiKey(account, opts, (error, data, response) => {
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
 **account** | **String**| Organization account name | 
 **xRequestId** | **String**| Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one.  | [optional] 
 **role** | **String**| (**Optional**) role specifier in &#x60;{kind}:{identifier}&#x60; format  ##### Permissions required  &#x60;update&#x60; privilege on the role whose API key is being rotated.  | [optional] 

### Return type

null (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth), [conjurAuth](../README.md#conjurAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

