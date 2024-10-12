# Ip2WhoisDomainLookup.DefaultApi

All URIs are relative to *https://api.ip2whois.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rootGet**](DefaultApi.md#rootGet) | **GET** / | 



## rootGet

> String rootGet(domain, key, opts)



Lookup WHOIS information

### Example

```javascript
import Ip2WhoisDomainLookup from 'ip2_whois_domain_lookup';

let apiInstance = new Ip2WhoisDomainLookup.DefaultApi();
let domain = "domain_example"; // String | Domain name for lookup purpose.
let key = "key_example"; // String | API key.
let opts = {
  'format': "format_example" // String | Returns the API response in json (default) or xml format.
};
apiInstance.rootGet(domain, key, opts, (error, data, response) => {
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
 **domain** | **String**| Domain name for lookup purpose. | 
 **key** | **String**| API key. | 
 **format** | **String**| Returns the API response in json (default) or xml format. | [optional] 

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/html; charset=UTF-8

