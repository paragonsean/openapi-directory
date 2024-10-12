# Conjur.PoliciesApi

All URIs are relative to *http://conjur.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**loadPolicy**](PoliciesApi.md#loadPolicy) | **POST** /policies/{account}/policy/{identifier} | Adds data to the existing Conjur policy.
[**replacePolicy**](PoliciesApi.md#replacePolicy) | **PUT** /policies/{account}/policy/{identifier} | Loads or replaces a Conjur policy document.
[**updatePolicy**](PoliciesApi.md#updatePolicy) | **PATCH** /policies/{account}/policy/{identifier} | Modifies an existing Conjur policy.



## loadPolicy

> loadPolicy(account, identifier, body, opts)

Adds data to the existing Conjur policy.

Adds data to the existing Conjur policy. Deletions are not allowed. Any policy objects that exist on the server but are omitted from the policy file will not be deleted and any explicit deletions in the policy file will result in an error.  ##### Permissions required  &#x60;create&#x60; privilege on the policy.\&quot; 

### Example

```javascript
import Conjur from 'conjur';
let defaultClient = Conjur.ApiClient.instance;
// Configure API key authorization: conjurAuth
let conjurAuth = defaultClient.authentications['conjurAuth'];
conjurAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//conjurAuth.apiKeyPrefix = 'Token';

let apiInstance = new Conjur.PoliciesApi();
let account = "account_example"; // String | Organization account name
let identifier = "root"; // String | ID of the policy to update
let body = null; // Object | Policy
let opts = {
  'xRequestId': "test-id" // String | Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one. 
};
apiInstance.loadPolicy(account, identifier, body, opts, (error, data, response) => {
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
 **identifier** | **String**| ID of the policy to update | 
 **body** | **Object**| Policy | 
 **xRequestId** | **String**| Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one.  | [optional] 

### Return type

null (empty response body)

### Authorization

[conjurAuth](../README.md#conjurAuth)

### HTTP request headers

- **Content-Type**: application/x-yaml, text/plain, text/x-yaml, text/yaml
- **Accept**: Not defined


## replacePolicy

> ReplacePolicy201Response replacePolicy(account, identifier, body, opts)

Loads or replaces a Conjur policy document.

Loads or replaces a Conjur policy document.  **Any policy data which already exists on the server but is not explicitly specified in the new policy file will be deleted!**. 

### Example

```javascript
import Conjur from 'conjur';
let defaultClient = Conjur.ApiClient.instance;
// Configure API key authorization: conjurAuth
let conjurAuth = defaultClient.authentications['conjurAuth'];
conjurAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//conjurAuth.apiKeyPrefix = 'Token';

let apiInstance = new Conjur.PoliciesApi();
let account = "account_example"; // String | Organization account name
let identifier = "root"; // String | ID of the policy to load (root if no root policy has been loaded yet)
let body = null; // Object | Policy
let opts = {
  'xRequestId': "test-id" // String | Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one. 
};
apiInstance.replacePolicy(account, identifier, body, opts, (error, data, response) => {
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
 **identifier** | **String**| ID of the policy to load (root if no root policy has been loaded yet) | 
 **body** | **Object**| Policy | 
 **xRequestId** | **String**| Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one.  | [optional] 

### Return type

[**ReplacePolicy201Response**](ReplacePolicy201Response.md)

### Authorization

[conjurAuth](../README.md#conjurAuth)

### HTTP request headers

- **Content-Type**: application/x-yaml, text/plain, text/x-yaml, text/yaml
- **Accept**: application/json


## updatePolicy

> updatePolicy(account, identifier, body, opts)

Modifies an existing Conjur policy.

Modifies an existing Conjur policy. Data may be explicitly deleted using the &#x60;!delete&#x60;, &#x60;!revoke&#x60;, and &#x60;!deny&#x60; statements. Unlike &#x60;replace&#x60; mode, no data is ever implicitly deleted.  ##### Permissions required 

### Example

```javascript
import Conjur from 'conjur';
let defaultClient = Conjur.ApiClient.instance;
// Configure API key authorization: conjurAuth
let conjurAuth = defaultClient.authentications['conjurAuth'];
conjurAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//conjurAuth.apiKeyPrefix = 'Token';

let apiInstance = new Conjur.PoliciesApi();
let account = "account_example"; // String | Organization account name
let identifier = "root"; // String | ID of the policy to update
let body = null; // Object | Policy
let opts = {
  'xRequestId': "test-id" // String | Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one. 
};
apiInstance.updatePolicy(account, identifier, body, opts, (error, data, response) => {
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
 **identifier** | **String**| ID of the policy to update | 
 **body** | **Object**| Policy | 
 **xRequestId** | **String**| Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one.  | [optional] 

### Return type

null (empty response body)

### Authorization

[conjurAuth](../README.md#conjurAuth)

### HTTP request headers

- **Content-Type**: application/x-yaml, text/plain, text/x-yaml, text/yaml
- **Accept**: Not defined

