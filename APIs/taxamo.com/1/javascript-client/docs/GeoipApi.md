# Taxamo.GeoipApi

All URIs are relative to *https://api.taxamo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**locateGivenIP**](GeoipApi.md#locateGivenIP) | **GET** /api/v1/geoip/{ip} | Locate provided IP
[**locateMyIP**](GeoipApi.md#locateMyIP) | **GET** /api/v1/geoip | Locate IP



## locateGivenIP

> LocateGivenIPOut locateGivenIP(ip)

Locate provided IP

### Example

```javascript
import Taxamo from 'taxamo';

let apiInstance = new Taxamo.GeoipApi();
let ip = "ip_example"; // String | IP address.
apiInstance.locateGivenIP(ip, (error, data, response) => {
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
 **ip** | **String**| IP address. | 

### Return type

[**LocateGivenIPOut**](LocateGivenIPOut.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## locateMyIP

> LocateMyIPOut locateMyIP()

Locate IP

### Example

```javascript
import Taxamo from 'taxamo';

let apiInstance = new Taxamo.GeoipApi();
apiInstance.locateMyIP((error, data, response) => {
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

[**LocateMyIPOut**](LocateMyIPOut.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

