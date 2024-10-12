# RubrikRestApi.SessionApi

All URIs are relative to */api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createSession**](SessionApi.md#createSession) | **POST** /session | Create user session
[**deleteSession**](SessionApi.md#deleteSession) | **DELETE** /session/{id} | Delete user session



## createSession

> SessionSummary createSession(opts)

Create user session

Open a user session.

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.SessionApi();
let opts = {
  'organizationId': "organizationId_example", // String | Bind the new session to the specified organization. When this parameter is not specified, the session will be bound to an organization chosen according to the user's preferences and authorizations.
  'realm': "realm_example" // String | Bind the new session to the specified directory. When this parameter is unspecified, the session will be bound to local domain.
};
apiInstance.createSession(opts, (error, data, response) => {
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
 **organizationId** | **String**| Bind the new session to the specified organization. When this parameter is not specified, the session will be bound to an organization chosen according to the user&#39;s preferences and authorizations. | [optional] 
 **realm** | **String**| Bind the new session to the specified directory. When this parameter is unspecified, the session will be bound to local domain. | [optional] 

### Return type

[**SessionSummary**](SessionSummary.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteSession

> deleteSession(id)

Delete user session

Close a user session and invalidate the session token.

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.SessionApi();
let id = "'me'"; // String | Session ID or  *me* for session of bearer token.
apiInstance.deleteSession(id, (error, data, response) => {
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
 **id** | **String**| Session ID or  *me* for session of bearer token. | [default to &#39;me&#39;]

### Return type

null (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

