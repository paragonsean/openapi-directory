# QuicksoldRestApi.WGS84ToOSGB36Api

All URIs are relative to *http://quicksold.co.uk*

Method | HTTP request | Description
------------- | ------------- | -------------
[**wgs84ToOsgb36UsingGET**](WGS84ToOSGB36Api.md#wgs84ToOsgb36UsingGET) | **GET** /v1/wgs84ToOsgb36/{latitude}/{longitude} | wgs84ToOsgb36



## wgs84ToOsgb36UsingGET

> ApiResponse wgs84ToOsgb36UsingGET(latitude, longitude)

wgs84ToOsgb36

### Example

```javascript
import QuicksoldRestApi from 'quicksold_rest_api';

let apiInstance = new QuicksoldRestApi.WGS84ToOSGB36Api();
let latitude = "latitude_example"; // String | latitude
let longitude = "longitude_example"; // String | longitude
apiInstance.wgs84ToOsgb36UsingGET(latitude, longitude, (error, data, response) => {
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
 **latitude** | **String**| latitude | 
 **longitude** | **String**| longitude | 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

