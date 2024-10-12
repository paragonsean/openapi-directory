# Conjur.PublicKeysApi

All URIs are relative to *http://conjur.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**showPublicKeys**](PublicKeysApi.md#showPublicKeys) | **GET** /public_keys/{account}/{kind}/{identifier} | Shows all public keys for a resource.



## showPublicKeys

> String showPublicKeys(account, kind, identifier, opts)

Shows all public keys for a resource.

Shows all public keys for a resource as newline delimited string for compatibility with the authorized_keys SSH format. Returns an empty string if the resource does not exist, to prevent attackers from determining whether a resource exists. 

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

let apiInstance = new Conjur.PublicKeysApi();
let account = "account_example"; // String | Organization account name
let kind = "user"; // String | Type of resource
let identifier = "admin"; // String | ID of the resource for which to get the information about
let opts = {
  'xRequestId': "test-id" // String | Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one. 
};
apiInstance.showPublicKeys(account, kind, identifier, opts, (error, data, response) => {
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
 **kind** | **String**| Type of resource | 
 **identifier** | **String**| ID of the resource for which to get the information about | 
 **xRequestId** | **String**| Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one.  | [optional] 

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth), [conjurKubernetesMutualTls](../README.md#conjurKubernetesMutualTls), [conjurAuth](../README.md#conjurAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/plain

