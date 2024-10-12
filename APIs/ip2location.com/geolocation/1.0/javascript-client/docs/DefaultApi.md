# Ip2LocationIpGeolocation.DefaultApi

All URIs are relative to *https://api.ip2location.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rootGet**](DefaultApi.md#rootGet) | **GET** / | 



## rootGet

> String rootGet(ip, key, opts)



Get geolocation information via IP address

### Example

```javascript
import Ip2LocationIpGeolocation from 'ip2_location_ip_geolocation';

let apiInstance = new Ip2LocationIpGeolocation.DefaultApi();
let ip = "8.8.8.8"; // String | IP address (IPv4 or IPv6) for reverse IP location lookup purpose. If not present, the server IP address will be used for the location lookup.
let key = "key_example"; // String | API Key. Please sign up free trial license key at ip2location.com
let opts = {
  '_package': "_package_example", // String | Web service package of different granularity of return information.
  'addon': ["null"], // [String] | Extra information in addition to the above selected package.
  'format': "format_example", // String | Format of the response message.
  'lang': "lang_example" // String | Translation information. The translation only applicable for continent, country, region and city name for the addon package.
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
 **ip** | **String**| IP address (IPv4 or IPv6) for reverse IP location lookup purpose. If not present, the server IP address will be used for the location lookup. | 
 **key** | **String**| API Key. Please sign up free trial license key at ip2location.com | 
 **_package** | **String**| Web service package of different granularity of return information. | [optional] 
 **addon** | [**[String]**](String.md)| Extra information in addition to the above selected package. | [optional] 
 **format** | **String**| Format of the response message. | [optional] 
 **lang** | **String**| Translation information. The translation only applicable for continent, country, region and city name for the addon package. | [optional] 

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json; charset=utf-8

