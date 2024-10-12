# Ip2LocationIoIpGeolocationApi.DefaultApi

All URIs are relative to *https://api.ip2location.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rootGet**](DefaultApi.md#rootGet) | **GET** / | 



## rootGet

> rootGet(key, ip, opts)



Geolocate user&#39;s location information via IP address

### Example

```javascript
import Ip2LocationIoIpGeolocationApi from 'ip2_location_io_ip_geolocation_api';

let apiInstance = new Ip2LocationIoIpGeolocationApi.DefaultApi();
let key = "key_example"; // String | API key.
let ip = "8.8.8.8"; // String | IP address (IPv4 or IPv6) for reverse IP location lookup purposes. If not present, the server IP address will be used for the location lookup.
let opts = {
  'format': "format_example", // String | Format of the response message.
  'lang': "lang_example" // String | Translation information. The translation only applicable for continent, country, region and city name. This parameter is only available for Plus and Security plan only.
};
apiInstance.rootGet(key, ip, opts, (error, data, response) => {
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
 **key** | **String**| API key. | 
 **ip** | **String**| IP address (IPv4 or IPv6) for reverse IP location lookup purposes. If not present, the server IP address will be used for the location lookup. | 
 **format** | **String**| Format of the response message. | [optional] 
 **lang** | **String**| Translation information. The translation only applicable for continent, country, region and city name. This parameter is only available for Plus and Security plan only. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

