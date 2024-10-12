# WhoHostsThisApi.HostingApi

All URIs are relative to *https://www.who-hosts-this.com/APIEndpoint*

Method | HTTP request | Description
------------- | ------------- | -------------
[**detectGet**](HostingApi.md#detectGet) | **GET** /Detect | Discover the hosting provider for a web site



## detectGet

> detectGet(url)

Discover the hosting provider for a web site

### Example

```javascript
import WhoHostsThisApi from 'who_hosts_this_api';
let defaultClient = WhoHostsThisApi.ApiClient.instance;
// Configure API key authorization: QueryKey
let QueryKey = defaultClient.authentications['QueryKey'];
QueryKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//QueryKey.apiKeyPrefix = 'Token';

let apiInstance = new WhoHostsThisApi.HostingApi();
let url = "url_example"; // String | The url of the page to check
apiInstance.detectGet(url, (error, data, response) => {
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
 **url** | **String**| The url of the page to check | 

### Return type

null (empty response body)

### Authorization

[QueryKey](../README.md#QueryKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

