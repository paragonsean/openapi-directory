# NetlifysApiDocumentation.EnvironmentVariablesApi

All URIs are relative to *https://api.netlify.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createEnvVars**](EnvironmentVariablesApi.md#createEnvVars) | **POST** /accounts/{account_id}/env | 
[**deleteEnvVar**](EnvironmentVariablesApi.md#deleteEnvVar) | **DELETE** /accounts/{account_id}/env/{key} | 
[**deleteEnvVarValue**](EnvironmentVariablesApi.md#deleteEnvVarValue) | **DELETE** /accounts/{account_id}/env/{key}/value/{id} | 
[**getEnvVar**](EnvironmentVariablesApi.md#getEnvVar) | **GET** /accounts/{account_id}/env/{key} | 
[**getEnvVars**](EnvironmentVariablesApi.md#getEnvVars) | **GET** /accounts/{account_id}/env | 
[**setEnvVarValue**](EnvironmentVariablesApi.md#setEnvVarValue) | **PATCH** /accounts/{account_id}/env/{key} | 
[**updateEnvVar**](EnvironmentVariablesApi.md#updateEnvVar) | **PUT** /accounts/{account_id}/env/{key} | 



## createEnvVars

> [EnvVar] createEnvVars(accountId, opts)



Creates new environment variables. Granular scopes are available on Pro plans and above.  To use this endpoint, your site must no longer be using the &lt;a href&#x3D;\&quot;https://docs.netlify.com/environment-variables/classic-experience/\&quot;&gt;classic environment variables experience&lt;/a&gt;.  Migrate now with the Netlify UI.

### Example

```javascript
import NetlifysApiDocumentation from 'netlifys_api_documentation';
let defaultClient = NetlifysApiDocumentation.ApiClient.instance;
// Configure OAuth2 access token for authorization: netlifyAuth
let netlifyAuth = defaultClient.authentications['netlifyAuth'];
netlifyAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetlifysApiDocumentation.EnvironmentVariablesApi();
let accountId = "accountId_example"; // String | Scope response to account_id
let opts = {
  'siteId': "siteId_example", // String | If provided, create an environment variable on the site level, not the account level
  'envVars': [new NetlifysApiDocumentation.CreateEnvVarsRequestInner()] // [CreateEnvVarsRequestInner] | 
};
apiInstance.createEnvVars(accountId, opts, (error, data, response) => {
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
 **accountId** | **String**| Scope response to account_id | 
 **siteId** | **String**| If provided, create an environment variable on the site level, not the account level | [optional] 
 **envVars** | [**[CreateEnvVarsRequestInner]**](CreateEnvVarsRequestInner.md)|  | [optional] 

### Return type

[**[EnvVar]**](EnvVar.md)

### Authorization

[netlifyAuth](../README.md#netlifyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteEnvVar

> deleteEnvVar(accountId, key, opts)



Deletes an environment variable. To use this endpoint, your site must no longer be using the &lt;a href&#x3D;\&quot;https://docs.netlify.com/environment-variables/classic-experience/\&quot;&gt;classic environment variables experience&lt;/a&gt;.  Migrate now with the Netlify UI.

### Example

```javascript
import NetlifysApiDocumentation from 'netlifys_api_documentation';
let defaultClient = NetlifysApiDocumentation.ApiClient.instance;
// Configure OAuth2 access token for authorization: netlifyAuth
let netlifyAuth = defaultClient.authentications['netlifyAuth'];
netlifyAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetlifysApiDocumentation.EnvironmentVariablesApi();
let accountId = "accountId_example"; // String | Scope response to account_id
let key = "key_example"; // String | The environment variable key (case-sensitive)
let opts = {
  'siteId': "siteId_example" // String | If provided, delete the environment variable from this site
};
apiInstance.deleteEnvVar(accountId, key, opts, (error, data, response) => {
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
 **accountId** | **String**| Scope response to account_id | 
 **key** | **String**| The environment variable key (case-sensitive) | 
 **siteId** | **String**| If provided, delete the environment variable from this site | [optional] 

### Return type

null (empty response body)

### Authorization

[netlifyAuth](../README.md#netlifyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteEnvVarValue

> deleteEnvVarValue(accountId, id, key, opts)



Deletes a specific environment variable value. To use this endpoint, your site must no longer be using the &lt;a href&#x3D;\&quot;https://docs.netlify.com/environment-variables/classic-experience/\&quot;&gt;classic environment variables experience&lt;/a&gt;.  Migrate now with the Netlify UI.

### Example

```javascript
import NetlifysApiDocumentation from 'netlifys_api_documentation';
let defaultClient = NetlifysApiDocumentation.ApiClient.instance;
// Configure OAuth2 access token for authorization: netlifyAuth
let netlifyAuth = defaultClient.authentications['netlifyAuth'];
netlifyAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetlifysApiDocumentation.EnvironmentVariablesApi();
let accountId = "accountId_example"; // String | Scope response to account_id
let id = "id_example"; // String | The environment variable value's ID
let key = "key_example"; // String | The environment variable key name (case-sensitive)
let opts = {
  'siteId': "siteId_example" // String | If provided, delete the value from an environment variable on this site
};
apiInstance.deleteEnvVarValue(accountId, id, key, opts, (error, data, response) => {
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
 **accountId** | **String**| Scope response to account_id | 
 **id** | **String**| The environment variable value&#39;s ID | 
 **key** | **String**| The environment variable key name (case-sensitive) | 
 **siteId** | **String**| If provided, delete the value from an environment variable on this site | [optional] 

### Return type

null (empty response body)

### Authorization

[netlifyAuth](../README.md#netlifyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getEnvVar

> EnvVar getEnvVar(accountId, key, opts)



Returns an individual environment variable. To use this endpoint, your site must no longer be using the &lt;a href&#x3D;\&quot;https://docs.netlify.com/environment-variables/classic-experience/\&quot;&gt;classic environment variables experience&lt;/a&gt;.  Migrate now with the Netlify UI.

### Example

```javascript
import NetlifysApiDocumentation from 'netlifys_api_documentation';
let defaultClient = NetlifysApiDocumentation.ApiClient.instance;
// Configure OAuth2 access token for authorization: netlifyAuth
let netlifyAuth = defaultClient.authentications['netlifyAuth'];
netlifyAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetlifysApiDocumentation.EnvironmentVariablesApi();
let accountId = "accountId_example"; // String | Scope response to account_id
let key = "key_example"; // String | The environment variable key (case-sensitive)
let opts = {
  'siteId': "siteId_example" // String | If provided, return the environment variable for a specific site (no merging is performed)
};
apiInstance.getEnvVar(accountId, key, opts, (error, data, response) => {
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
 **accountId** | **String**| Scope response to account_id | 
 **key** | **String**| The environment variable key (case-sensitive) | 
 **siteId** | **String**| If provided, return the environment variable for a specific site (no merging is performed) | [optional] 

### Return type

[**EnvVar**](EnvVar.md)

### Authorization

[netlifyAuth](../README.md#netlifyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getEnvVars

> [EnvVar] getEnvVars(accountId, opts)



Returns all environment variables for an account or site. An account corresponds to a team in the Netlify UI. To use this endpoint, your site must no longer be using the &lt;a href&#x3D;\&quot;https://docs.netlify.com/environment-variables/classic-experience/\&quot;&gt;classic environment variables experience&lt;/a&gt;.  Migrate now with the Netlify UI.

### Example

```javascript
import NetlifysApiDocumentation from 'netlifys_api_documentation';
let defaultClient = NetlifysApiDocumentation.ApiClient.instance;
// Configure OAuth2 access token for authorization: netlifyAuth
let netlifyAuth = defaultClient.authentications['netlifyAuth'];
netlifyAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetlifysApiDocumentation.EnvironmentVariablesApi();
let accountId = "accountId_example"; // String | Scope response to account_id
let opts = {
  'contextName': "contextName_example", // String | Filter by deploy context
  'scope': "scope_example", // String | Filter by scope
  'siteId': "siteId_example" // String | If specified, only return environment variables set on this site
};
apiInstance.getEnvVars(accountId, opts, (error, data, response) => {
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
 **accountId** | **String**| Scope response to account_id | 
 **contextName** | **String**| Filter by deploy context | [optional] 
 **scope** | **String**| Filter by scope | [optional] 
 **siteId** | **String**| If specified, only return environment variables set on this site | [optional] 

### Return type

[**[EnvVar]**](EnvVar.md)

### Authorization

[netlifyAuth](../README.md#netlifyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## setEnvVarValue

> EnvVar setEnvVarValue(accountId, key, opts)



Updates or creates a new value for an existing environment variable. To use this endpoint, your site must no longer be using the &lt;a href&#x3D;\&quot;https://docs.netlify.com/environment-variables/classic-experience/\&quot;&gt;classic environment variables experience&lt;/a&gt;.  Migrate now with the Netlify UI.

### Example

```javascript
import NetlifysApiDocumentation from 'netlifys_api_documentation';
let defaultClient = NetlifysApiDocumentation.ApiClient.instance;
// Configure OAuth2 access token for authorization: netlifyAuth
let netlifyAuth = defaultClient.authentications['netlifyAuth'];
netlifyAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetlifysApiDocumentation.EnvironmentVariablesApi();
let accountId = "accountId_example"; // String | Scope response to account_id
let key = "key_example"; // String | The existing environment variable key name (case-sensitive)
let opts = {
  'siteId': "siteId_example", // String | If provided, update an environment variable set on this site
  'envVar': new NetlifysApiDocumentation.SetEnvVarValueRequest() // SetEnvVarValueRequest | 
};
apiInstance.setEnvVarValue(accountId, key, opts, (error, data, response) => {
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
 **accountId** | **String**| Scope response to account_id | 
 **key** | **String**| The existing environment variable key name (case-sensitive) | 
 **siteId** | **String**| If provided, update an environment variable set on this site | [optional] 
 **envVar** | [**SetEnvVarValueRequest**](SetEnvVarValueRequest.md)|  | [optional] 

### Return type

[**EnvVar**](EnvVar.md)

### Authorization

[netlifyAuth](../README.md#netlifyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateEnvVar

> EnvVar updateEnvVar(accountId, key, opts)



Updates an existing environment variable and all of its values. Existing values will be replaced by values provided. To use this endpoint, your site must no longer be using the &lt;a href&#x3D;\&quot;https://docs.netlify.com/environment-variables/classic-experience/\&quot;&gt;classic environment variables experience&lt;/a&gt;.  Migrate now with the Netlify UI.

### Example

```javascript
import NetlifysApiDocumentation from 'netlifys_api_documentation';
let defaultClient = NetlifysApiDocumentation.ApiClient.instance;
// Configure OAuth2 access token for authorization: netlifyAuth
let netlifyAuth = defaultClient.authentications['netlifyAuth'];
netlifyAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetlifysApiDocumentation.EnvironmentVariablesApi();
let accountId = "accountId_example"; // String | Scope response to account_id
let key = "key_example"; // String | The existing environment variable key name (case-sensitive)
let opts = {
  'siteId': "siteId_example", // String | If provided, update an environment variable set on this site
  'envVar': new NetlifysApiDocumentation.CreateEnvVarsRequestInner() // CreateEnvVarsRequestInner | 
};
apiInstance.updateEnvVar(accountId, key, opts, (error, data, response) => {
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
 **accountId** | **String**| Scope response to account_id | 
 **key** | **String**| The existing environment variable key name (case-sensitive) | 
 **siteId** | **String**| If provided, update an environment variable set on this site | [optional] 
 **envVar** | [**CreateEnvVarsRequestInner**](CreateEnvVarsRequestInner.md)|  | [optional] 

### Return type

[**EnvVar**](EnvVar.md)

### Authorization

[netlifyAuth](../README.md#netlifyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

