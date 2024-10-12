# ProxyKingdomApi.ProxyApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**proxyGet**](ProxyApi.md#proxyGet) | **GET** /proxy | Gets a random proxy for chosen parameters.



## proxyGet

> Proxy proxyGet(correlationId, opts)

Gets a random proxy for chosen parameters.

### Example

```javascript
import ProxyKingdomApi from 'proxy_kingdom_api';

let apiInstance = new ProxyKingdomApi.ProxyApi();
let correlationId = "'049d3e5c-f02a-4568-a1f4-7bd182668b1b'"; // String | Correlation Id header field
let opts = {
  'token': "token_example", // String | 
  'address': "address_example", // String | 
  'port': "port_example", // String | 
  'protocol': "protocol_example", // String | 
  'accessType': "accessType_example", // String | 
  'responseTime': "responseTime_example", // String | 
  'isSsl': "isSsl_example", // String | 
  'uptime': "uptime_example", // String | 
  'country': "country_example", // String | 
  'continent': "continent_example", // String | 
  'timezone': "timezone_example", // String | 
  'lastTested': "lastTested_example" // String | 
};
apiInstance.proxyGet(correlationId, opts, (error, data, response) => {
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
 **correlationId** | **String**| Correlation Id header field | [default to &#39;049d3e5c-f02a-4568-a1f4-7bd182668b1b&#39;]
 **token** | **String**|  | [optional] 
 **address** | **String**|  | [optional] 
 **port** | **String**|  | [optional] 
 **protocol** | **String**|  | [optional] 
 **accessType** | **String**|  | [optional] 
 **responseTime** | **String**|  | [optional] 
 **isSsl** | **String**|  | [optional] 
 **uptime** | **String**|  | [optional] 
 **country** | **String**|  | [optional] 
 **continent** | **String**|  | [optional] 
 **timezone** | **String**|  | [optional] 
 **lastTested** | **String**|  | [optional] 

### Return type

[**Proxy**](Proxy.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain

