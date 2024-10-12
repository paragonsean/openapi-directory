# GatewayRestApi.DefaultApi

All URIs are relative to *http://tyk.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**tykApisApiIDDelete**](DefaultApi.md#tykApisApiIDDelete) | **DELETE** /tyk/apis/{apiID} | 
[**tykApisApiIDGet**](DefaultApi.md#tykApisApiIDGet) | **GET** /tyk/apis/{apiID} | 
[**tykApisApiIDPut**](DefaultApi.md#tykApisApiIDPut) | **PUT** /tyk/apis/{apiID} | 
[**tykApisGet**](DefaultApi.md#tykApisGet) | **GET** /tyk/apis/ | 
[**tykApisPost**](DefaultApi.md#tykApisPost) | **POST** /tyk/apis/ | 
[**tykHealthGet**](DefaultApi.md#tykHealthGet) | **GET** /tyk/health/ | 
[**tykKeysCreatePost**](DefaultApi.md#tykKeysCreatePost) | **POST** /tyk/keys/create | 
[**tykKeysGet**](DefaultApi.md#tykKeysGet) | **GET** /tyk/keys/ | 
[**tykKeysKeyIdDelete**](DefaultApi.md#tykKeysKeyIdDelete) | **DELETE** /tyk/keys/{keyId} | 
[**tykKeysKeyIdPost**](DefaultApi.md#tykKeysKeyIdPost) | **POST** /tyk/keys/{keyId} | 
[**tykKeysKeyIdPut**](DefaultApi.md#tykKeysKeyIdPut) | **PUT** /tyk/keys/{keyId} | 
[**tykOauthAuthorizeClientPost**](DefaultApi.md#tykOauthAuthorizeClientPost) | **POST** /tyk/oauth/authorize-client/ | 
[**tykOauthClientsApiIdClientIdDelete**](DefaultApi.md#tykOauthClientsApiIdClientIdDelete) | **DELETE** /tyk/oauth/clients/{apiId}/{clientId} | 
[**tykOauthClientsApiIdGet**](DefaultApi.md#tykOauthClientsApiIdGet) | **GET** /tyk/oauth/clients/{apiId} | 
[**tykOauthClientsCreatePost**](DefaultApi.md#tykOauthClientsCreatePost) | **POST** /tyk/oauth/clients/create | 
[**tykOauthRefreshKeyIdDelete**](DefaultApi.md#tykOauthRefreshKeyIdDelete) | **DELETE** /tyk/oauth/refresh/{keyId} | 
[**tykReloadGet**](DefaultApi.md#tykReloadGet) | **GET** /tyk/reload/ | 
[**tykReloadGroupGet**](DefaultApi.md#tykReloadGroupGet) | **GET** /tyk/reload/group | 



## tykApisApiIDDelete

> TykApisApiIDDelete200Response tykApisApiIDDelete(xTykAuthorization, apiID)



Deletes an *API Definition* object, if it exists 

### Example

```javascript
import GatewayRestApi from 'gateway_rest_api';

let apiInstance = new GatewayRestApi.DefaultApi();
let xTykAuthorization = "xTykAuthorization_example"; // String | tyk gateway shared secret
let apiID = "apiID_example"; // String | API ID
apiInstance.tykApisApiIDDelete(xTykAuthorization, apiID, (error, data, response) => {
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
 **xTykAuthorization** | **String**| tyk gateway shared secret | 
 **apiID** | **String**| API ID | 

### Return type

[**TykApisApiIDDelete200Response**](TykApisApiIDDelete200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## tykApisApiIDGet

> APIDefinition tykApisApiIDGet(xTykAuthorization, apiID)



Gets an *API Definition* object, if it exists 

### Example

```javascript
import GatewayRestApi from 'gateway_rest_api';

let apiInstance = new GatewayRestApi.DefaultApi();
let xTykAuthorization = "xTykAuthorization_example"; // String | tyk gateway shared secret
let apiID = "apiID_example"; // String | API ID
apiInstance.tykApisApiIDGet(xTykAuthorization, apiID, (error, data, response) => {
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
 **xTykAuthorization** | **String**| tyk gateway shared secret | 
 **apiID** | **String**| API ID | 

### Return type

[**APIDefinition**](APIDefinition.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## tykApisApiIDPut

> TykApisPost200Response tykApisApiIDPut(xTykAuthorization, apiID, opts)



Updates an *API Definition* object, if it exists 

### Example

```javascript
import GatewayRestApi from 'gateway_rest_api';

let apiInstance = new GatewayRestApi.DefaultApi();
let xTykAuthorization = "xTykAuthorization_example"; // String | tyk gateway shared secret
let apiID = "apiID_example"; // String | API ID
let opts = {
  'apiDefinition': new GatewayRestApi.APIDefinition() // APIDefinition | 
};
apiInstance.tykApisApiIDPut(xTykAuthorization, apiID, opts, (error, data, response) => {
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
 **xTykAuthorization** | **String**| tyk gateway shared secret | 
 **apiID** | **String**| API ID | 
 **apiDefinition** | [**APIDefinition**](APIDefinition.md)|  | [optional] 

### Return type

[**TykApisPost200Response**](TykApisPost200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## tykApisGet

> [APIDefinition] tykApisGet(xTykAuthorization)



Gets a list of *API Definition* objects that are currently live on the gateway  

### Example

```javascript
import GatewayRestApi from 'gateway_rest_api';

let apiInstance = new GatewayRestApi.DefaultApi();
let xTykAuthorization = "xTykAuthorization_example"; // String | tyk gateway shared secret
apiInstance.tykApisGet(xTykAuthorization, (error, data, response) => {
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
 **xTykAuthorization** | **String**| tyk gateway shared secret | 

### Return type

[**[APIDefinition]**](APIDefinition.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## tykApisPost

> TykApisPost200Response tykApisPost(opts)



Create an *API Definition* object 

### Example

```javascript
import GatewayRestApi from 'gateway_rest_api';

let apiInstance = new GatewayRestApi.DefaultApi();
let opts = {
  'apiDefinition': new GatewayRestApi.APIDefinition() // APIDefinition | 
};
apiInstance.tykApisPost(opts, (error, data, response) => {
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
 **apiDefinition** | [**APIDefinition**](APIDefinition.md)|  | [optional] 

### Return type

[**TykApisPost200Response**](TykApisPost200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## tykHealthGet

> TykHealthGet200Response tykHealthGet(xTykAuthorization, apiId)



Gets the health check values for an API if it is being recorded 

### Example

```javascript
import GatewayRestApi from 'gateway_rest_api';

let apiInstance = new GatewayRestApi.DefaultApi();
let xTykAuthorization = "xTykAuthorization_example"; // String | tyk gateway shared secret
let apiId = "apiId_example"; // String | API ID to query
apiInstance.tykHealthGet(xTykAuthorization, apiId, (error, data, response) => {
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
 **xTykAuthorization** | **String**| tyk gateway shared secret | 
 **apiId** | **String**| API ID to query | 

### Return type

[**TykHealthGet200Response**](TykHealthGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## tykKeysCreatePost

> TykKeysCreatePost200Response tykKeysCreatePost(xTykAuthorization, opts)



Create a new *API token* with the *session object* defined in the body 

### Example

```javascript
import GatewayRestApi from 'gateway_rest_api';

let apiInstance = new GatewayRestApi.DefaultApi();
let xTykAuthorization = "xTykAuthorization_example"; // String | tyk gateway shared secret
let opts = {
  'suppressReset': 3.4, // Number | Adding the `suppress_reset` parameter and setting it to `1`, will cause Tyk to not reset the quota limit that is in the current live quota manager. By default Tyk will reset the quota in the live quota manager (initialising it) when ADDing a key. Adding the `suppress_reset` flag to the URL parameters will avoid this behaviour.
  'sessionObject': new GatewayRestApi.SessionObject() // SessionObject | 
};
apiInstance.tykKeysCreatePost(xTykAuthorization, opts, (error, data, response) => {
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
 **xTykAuthorization** | **String**| tyk gateway shared secret | 
 **suppressReset** | **Number**| Adding the &#x60;suppress_reset&#x60; parameter and setting it to &#x60;1&#x60;, will cause Tyk to not reset the quota limit that is in the current live quota manager. By default Tyk will reset the quota in the live quota manager (initialising it) when ADDing a key. Adding the &#x60;suppress_reset&#x60; flag to the URL parameters will avoid this behaviour. | [optional] 
 **sessionObject** | [**SessionObject**](SessionObject.md)|  | [optional] 

### Return type

[**TykKeysCreatePost200Response**](TykKeysCreatePost200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## tykKeysGet

> TykKeysGet200Response tykKeysGet(apiId, xTykAuthorization)



Gets a list of *key* IDs (will only work with non-hashed installations) 

### Example

```javascript
import GatewayRestApi from 'gateway_rest_api';

let apiInstance = new GatewayRestApi.DefaultApi();
let apiId = "apiId_example"; // String | Back-end to target
let xTykAuthorization = "xTykAuthorization_example"; // String | tyk gateway shared secret
apiInstance.tykKeysGet(apiId, xTykAuthorization, (error, data, response) => {
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
 **apiId** | **String**| Back-end to target | 
 **xTykAuthorization** | **String**| tyk gateway shared secret | 

### Return type

[**TykKeysGet200Response**](TykKeysGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## tykKeysKeyIdDelete

> TykApisApiIDDelete200Response tykKeysKeyIdDelete(xTykAuthorization, keyId, apiId)



Remove this *API token* from the gateway, this will completely destroy the token and metadata associated with the token and instantly stop access from being granted 

### Example

```javascript
import GatewayRestApi from 'gateway_rest_api';

let apiInstance = new GatewayRestApi.DefaultApi();
let xTykAuthorization = "xTykAuthorization_example"; // String | tyk gateway shared secret
let keyId = "keyId_example"; // String | Access Token
let apiId = "apiId_example"; // String | Back-end to target
apiInstance.tykKeysKeyIdDelete(xTykAuthorization, keyId, apiId, (error, data, response) => {
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
 **xTykAuthorization** | **String**| tyk gateway shared secret | 
 **keyId** | **String**| Access Token | 
 **apiId** | **String**| Back-end to target | 

### Return type

[**TykApisApiIDDelete200Response**](TykApisApiIDDelete200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## tykKeysKeyIdPost

> TykKeysKeyIdPost200Response tykKeysKeyIdPost(xTykAuthorization, keyId, opts)



Add a pre-specified *API token* with the *session object* defined in the body, this operatin creates a custom token that dsoes not use the gateway naming convention for tokens 

### Example

```javascript
import GatewayRestApi from 'gateway_rest_api';

let apiInstance = new GatewayRestApi.DefaultApi();
let xTykAuthorization = "xTykAuthorization_example"; // String | tyk gateway shared secret
let keyId = "keyId_example"; // String | Access Token
let opts = {
  'sessionObject': new GatewayRestApi.SessionObject() // SessionObject | 
};
apiInstance.tykKeysKeyIdPost(xTykAuthorization, keyId, opts, (error, data, response) => {
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
 **xTykAuthorization** | **String**| tyk gateway shared secret | 
 **keyId** | **String**| Access Token | 
 **sessionObject** | [**SessionObject**](SessionObject.md)|  | [optional] 

### Return type

[**TykKeysKeyIdPost200Response**](TykKeysKeyIdPost200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## tykKeysKeyIdPut

> TykKeysKeyIdPut200Response tykKeysKeyIdPut(xTykAuthorization, keyId, apiId, opts)



Update an *API token* with the *session object* defined in the body, this operatin overwrites the existing object 

### Example

```javascript
import GatewayRestApi from 'gateway_rest_api';

let apiInstance = new GatewayRestApi.DefaultApi();
let xTykAuthorization = "xTykAuthorization_example"; // String | tyk gateway shared secret
let keyId = "keyId_example"; // String | Access Token
let apiId = "apiId_example"; // String | Back-end to target
let opts = {
  'suppressReset': 3.4, // Number | Adding the `suppress_reset` parameter and setting it to `1`, will cause Tyk to not reset the quota limit that is in the current live quota manager. By default Tyk will reset the quota in the live quota manager (initialising it) when ADDing a key. Adding the `suppress_reset` flag to the URL parameters will avoid this behaviour.
  'sessionObject': new GatewayRestApi.SessionObject() // SessionObject | 
};
apiInstance.tykKeysKeyIdPut(xTykAuthorization, keyId, apiId, opts, (error, data, response) => {
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
 **xTykAuthorization** | **String**| tyk gateway shared secret | 
 **keyId** | **String**| Access Token | 
 **apiId** | **String**| Back-end to target | 
 **suppressReset** | **Number**| Adding the &#x60;suppress_reset&#x60; parameter and setting it to &#x60;1&#x60;, will cause Tyk to not reset the quota limit that is in the current live quota manager. By default Tyk will reset the quota in the live quota manager (initialising it) when ADDing a key. Adding the &#x60;suppress_reset&#x60; flag to the URL parameters will avoid this behaviour. | [optional] 
 **sessionObject** | [**SessionObject**](SessionObject.md)|  | [optional] 

### Return type

[**TykKeysKeyIdPut200Response**](TykKeysKeyIdPut200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## tykOauthAuthorizeClientPost

> TykOauthAuthorizeClientPost200Response tykOauthAuthorizeClientPost(xTykAuthorization, responseType, clientId, redirectUri, keyRules)



The final request from an authorising party for a redirect URI during the Tyk OAuth flow 

### Example

```javascript
import GatewayRestApi from 'gateway_rest_api';

let apiInstance = new GatewayRestApi.DefaultApi();
let xTykAuthorization = "xTykAuthorization_example"; // String | tyk gateway shared secret
let responseType = "responseType_example"; // String | Should be provided by requesting client as part of authorisation request, this should be either `code` or `token` depending on the methods you have specified for the API
let clientId = "clientId_example"; // String | Should be provided by requesting client as part of authorisation request. The Client ID that is making the request
let redirectUri = "redirectUri_example"; // String | Should be provided by requesting client as part of authorisation request. Must match with the record stored with Tyk
let keyRules = "keyRules_example"; // String | A string representation of a *Session Object (form-encoded)*. This should be provided by your application in order to apply any quotas or rules to the key
apiInstance.tykOauthAuthorizeClientPost(xTykAuthorization, responseType, clientId, redirectUri, keyRules, (error, data, response) => {
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
 **xTykAuthorization** | **String**| tyk gateway shared secret | 
 **responseType** | **String**| Should be provided by requesting client as part of authorisation request, this should be either &#x60;code&#x60; or &#x60;token&#x60; depending on the methods you have specified for the API | 
 **clientId** | **String**| Should be provided by requesting client as part of authorisation request. The Client ID that is making the request | 
 **redirectUri** | **String**| Should be provided by requesting client as part of authorisation request. Must match with the record stored with Tyk | 
 **keyRules** | **String**| A string representation of a *Session Object (form-encoded)*. This should be provided by your application in order to apply any quotas or rules to the key | 

### Return type

[**TykOauthAuthorizeClientPost200Response**](TykOauthAuthorizeClientPost200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: */*


## tykOauthClientsApiIdClientIdDelete

> TykApisApiIDDelete200Response tykOauthClientsApiIdClientIdDelete(xTykAuthorization, apiId, clientId)



Delete the OAuth client 

### Example

```javascript
import GatewayRestApi from 'gateway_rest_api';

let apiInstance = new GatewayRestApi.DefaultApi();
let xTykAuthorization = "xTykAuthorization_example"; // String | tyk gateway shared secret
let apiId = "apiId_example"; // String | API ID that owns this client (back end)
let clientId = "clientId_example"; // String | OAuth Client ID to delete
apiInstance.tykOauthClientsApiIdClientIdDelete(xTykAuthorization, apiId, clientId, (error, data, response) => {
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
 **xTykAuthorization** | **String**| tyk gateway shared secret | 
 **apiId** | **String**| API ID that owns this client (back end) | 
 **clientId** | **String**| OAuth Client ID to delete | 

### Return type

[**TykApisApiIDDelete200Response**](TykApisApiIDDelete200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## tykOauthClientsApiIdGet

> [OAuthClient] tykOauthClientsApiIdGet(xTykAuthorization, apiId)



Get a list of OAuth clients bound to this back end  

### Example

```javascript
import GatewayRestApi from 'gateway_rest_api';

let apiInstance = new GatewayRestApi.DefaultApi();
let xTykAuthorization = "xTykAuthorization_example"; // String | tyk gateway shared secret
let apiId = "apiId_example"; // String | API ID that owns this client (back end)
apiInstance.tykOauthClientsApiIdGet(xTykAuthorization, apiId, (error, data, response) => {
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
 **xTykAuthorization** | **String**| tyk gateway shared secret | 
 **apiId** | **String**| API ID that owns this client (back end) | 

### Return type

[**[OAuthClient]**](OAuthClient.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## tykOauthClientsCreatePost

> OAuthClient tykOauthClientsCreatePost(xTykAuthorization, opts)



Create a new OAuth client 

### Example

```javascript
import GatewayRestApi from 'gateway_rest_api';

let apiInstance = new GatewayRestApi.DefaultApi();
let xTykAuthorization = "xTykAuthorization_example"; // String | tyk gateway shared secret
let opts = {
  'oauthClient': new GatewayRestApi.TykOauthClientsCreatePostRequest() // TykOauthClientsCreatePostRequest | 
};
apiInstance.tykOauthClientsCreatePost(xTykAuthorization, opts, (error, data, response) => {
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
 **xTykAuthorization** | **String**| tyk gateway shared secret | 
 **oauthClient** | [**TykOauthClientsCreatePostRequest**](TykOauthClientsCreatePostRequest.md)|  | [optional] 

### Return type

[**OAuthClient**](OAuthClient.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## tykOauthRefreshKeyIdDelete

> TykApisApiIDDelete200Response tykOauthRefreshKeyIdDelete(xTykAuthorization, keyId, apiID)



Invalidate a refresh token 

### Example

```javascript
import GatewayRestApi from 'gateway_rest_api';

let apiInstance = new GatewayRestApi.DefaultApi();
let xTykAuthorization = "xTykAuthorization_example"; // String | tyk gateway shared secret
let keyId = "keyId_example"; // String | Access Token
let apiID = "apiID_example"; // String | API ID
apiInstance.tykOauthRefreshKeyIdDelete(xTykAuthorization, keyId, apiID, (error, data, response) => {
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
 **xTykAuthorization** | **String**| tyk gateway shared secret | 
 **keyId** | **String**| Access Token | 
 **apiID** | **String**| API ID | 

### Return type

[**TykApisApiIDDelete200Response**](TykApisApiIDDelete200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## tykReloadGet

> TykReloadGet200Response tykReloadGet(xTykAuthorization)



Will reload the targetted gateway 

### Example

```javascript
import GatewayRestApi from 'gateway_rest_api';

let apiInstance = new GatewayRestApi.DefaultApi();
let xTykAuthorization = "xTykAuthorization_example"; // String | tyk gateway shared secret
apiInstance.tykReloadGet(xTykAuthorization, (error, data, response) => {
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
 **xTykAuthorization** | **String**| tyk gateway shared secret | 

### Return type

[**TykReloadGet200Response**](TykReloadGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## tykReloadGroupGet

> TykReloadGet200Response tykReloadGroupGet(xTykAuthorization)



Will reload the cluster via the targeted gateway 

### Example

```javascript
import GatewayRestApi from 'gateway_rest_api';

let apiInstance = new GatewayRestApi.DefaultApi();
let xTykAuthorization = "xTykAuthorization_example"; // String | tyk gateway shared secret
apiInstance.tykReloadGroupGet(xTykAuthorization, (error, data, response) => {
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
 **xTykAuthorization** | **String**| tyk gateway shared secret | 

### Return type

[**TykReloadGet200Response**](TykReloadGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

