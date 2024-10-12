# AuthentiqConnectApi.SessionManagementApi

All URIs are relative to *https://connect.authentiq.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**authorizeIframe**](SessionManagementApi.md#authorizeIframe) | **GET** /{client_id}/iframe | Include a session iframe



## authorizeIframe

> authorizeIframe(clientId)

Include a session iframe

An OpenID Connect Session Management iframe to facilitate e.g. single sign-on or remote logouts.  The iframe implements the OIDC postMessage-based [change notification protocol](http://openid.net/specs/openid-connect-session-1_0.html#ChangeNotification) via which a client can receive notifications about session state changes. 

### Example

```javascript
import AuthentiqConnectApi from 'authentiq_connect_api';

let apiInstance = new AuthentiqConnectApi.SessionManagementApi();
let clientId = "clientId_example"; // String | Client identifier
apiInstance.authorizeIframe(clientId, (error, data, response) => {
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
 **clientId** | **String**| Client identifier | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

