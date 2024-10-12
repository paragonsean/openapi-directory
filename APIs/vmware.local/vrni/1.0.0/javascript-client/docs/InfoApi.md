# VRealizeNetworkInsightApiReference.InfoApi

All URIs are relative to *http://vmware.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getVersion**](InfoApi.md#getVersion) | **GET** /info/version | Show version info



## getVersion

> VersionResponse getVersion()

Show version info

Show version info

### Example

```javascript
import VRealizeNetworkInsightApiReference from 'v_realize_network_insight_api_reference';
let defaultClient = VRealizeNetworkInsightApiReference.ApiClient.instance;
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new VRealizeNetworkInsightApiReference.InfoApi();
apiInstance.getVersion((error, data, response) => {
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

[**VersionResponse**](VersionResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

