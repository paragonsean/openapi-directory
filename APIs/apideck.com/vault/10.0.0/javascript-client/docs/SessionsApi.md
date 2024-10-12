# VaultApi.SessionsApi

All URIs are relative to *https://unify.apideck.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sessionsCreate**](SessionsApi.md#sessionsCreate) | **POST** /vault/sessions | Create Session



## sessionsCreate

> CreateSessionResponse sessionsCreate(xApideckConsumerId, xApideckAppId, opts)

Create Session

Making a POST request to this endpoint will initiate a Hosted Vault session. Redirect the consumer to the returned URL to allow temporary access to manage their integrations and settings.  Note: This is a short lived token that will expire after 1 hour (TTL: 3600). 

### Example

```javascript
import VaultApi from 'vault_api';
let defaultClient = VaultApi.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new VaultApi.SessionsApi();
let xApideckConsumerId = "xApideckConsumerId_example"; // String | ID of the consumer which you want to get or push data from
let xApideckAppId = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX"; // String | The ID of your Unify application
let opts = {
  'session': new VaultApi.Session() // Session | Additional redirect uri and/or consumer metadata
};
apiInstance.sessionsCreate(xApideckConsumerId, xApideckAppId, opts, (error, data, response) => {
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
 **xApideckConsumerId** | **String**| ID of the consumer which you want to get or push data from | 
 **xApideckAppId** | **String**| The ID of your Unify application | 
 **session** | [**Session**](Session.md)| Additional redirect uri and/or consumer metadata | [optional] 

### Return type

[**CreateSessionResponse**](CreateSessionResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

