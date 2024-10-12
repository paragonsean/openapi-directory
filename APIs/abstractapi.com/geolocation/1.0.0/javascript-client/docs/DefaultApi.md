# IpGeolocationApi.DefaultApi

All URIs are relative to *https://ipgeolocation.abstractapi.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1Get**](DefaultApi.md#v1Get) | **GET** /v1/ | 



## v1Get

> InlineResponse200 v1Get(apiKey, opts)



Retrieve the location of an IP address

### Example

```javascript
import IpGeolocationApi from 'ip_geolocation_api';

let apiInstance = new IpGeolocationApi.DefaultApi();
let apiKey = "apiKey_example"; // String | 
let opts = {
  'ipAddress': "195.154.25.40", // String | 
  'fields': "country,city,timezone" // String | 
};
apiInstance.v1Get(apiKey, opts, (error, data, response) => {
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
 **apiKey** | **String**|  | 
 **ipAddress** | **String**|  | [optional] 
 **fields** | **String**|  | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

