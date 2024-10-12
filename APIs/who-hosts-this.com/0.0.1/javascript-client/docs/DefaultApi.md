# WhoHostsThisApi.DefaultApi

All URIs are relative to *https://www.who-hosts-this.com/APIEndpoint*

Method | HTTP request | Description
------------- | ------------- | -------------
[**statusGet**](DefaultApi.md#statusGet) | **GET** /Status | View usage details for the current billing period



## statusGet

> statusGet()

View usage details for the current billing period

### Example

```javascript
import WhoHostsThisApi from 'who_hosts_this_api';
let defaultClient = WhoHostsThisApi.ApiClient.instance;
// Configure API key authorization: QueryKey
let QueryKey = defaultClient.authentications['QueryKey'];
QueryKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//QueryKey.apiKeyPrefix = 'Token';

let apiInstance = new WhoHostsThisApi.DefaultApi();
apiInstance.statusGet((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

[QueryKey](../README.md#QueryKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

