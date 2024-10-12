# Ip2ProxyProxyDetection.DefaultApi

All URIs are relative to *https://api.ip2proxy.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rootGet**](DefaultApi.md#rootGet) | **GET** / | 



## rootGet

> String rootGet(ip, key, opts)



Check if an IP address is proxy

### Example

```javascript
import Ip2ProxyProxyDetection from 'ip2_proxy_proxy_detection';

let apiInstance = new Ip2ProxyProxyDetection.DefaultApi();
let ip = "ip_example"; // String | IP address (IPv4) for lookup purpose. If not present, the server IP address will be used for the lookup.
let key = "key_example"; // String | API key. Please sign up free trial license key at ip2location.com
let opts = {
  '_package': "_package_example", // String | Package name from PX1 to PX11. If not present, the web service will assume the PX1 package query.
  'format': "format_example" // String | If not present, json format will be returned as the search result.
};
apiInstance.rootGet(ip, key, opts, (error, data, response) => {
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
 **ip** | **String**| IP address (IPv4) for lookup purpose. If not present, the server IP address will be used for the lookup. | 
 **key** | **String**| API key. Please sign up free trial license key at ip2location.com | 
 **_package** | **String**| Package name from PX1 to PX11. If not present, the web service will assume the PX1 package query. | [optional] 
 **format** | **String**| If not present, json format will be returned as the search result. | [optional] 

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/html; charset=UTF-8

