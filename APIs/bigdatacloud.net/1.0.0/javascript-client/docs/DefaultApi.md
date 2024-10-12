# IpGeolocationApi.DefaultApi

All URIs are relative to *https://api.bigdatacloud.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ipGeolocationWithConfidenceAreaAndHazardReportApi**](DefaultApi.md#ipGeolocationWithConfidenceAreaAndHazardReportApi) | **GET** /data/ip-geolocation-full | IP Geolocation with Confidence Area and Hazard Report API
[**ipGeolocationWithConfidenceAreaApi**](DefaultApi.md#ipGeolocationWithConfidenceAreaApi) | **GET** /data/ip-geolocation-with-confidence | IP Geolocation with Confidence Area API



## ipGeolocationWithConfidenceAreaAndHazardReportApi

> ipGeolocationWithConfidenceAreaAndHazardReportApi(opts)

IP Geolocation with Confidence Area and Hazard Report API

This API returns additional security hazard report in addition to confidence area and locality information.

### Example

```javascript
import IpGeolocationApi from 'ip_geolocation_api';

let apiInstance = new IpGeolocationApi.DefaultApi();
let opts = {
  'ip': "193.114.112.122", // String | IPv4 IP address in a string or numeric format. If omitted, the caller’s IP address is assumed 
  'localityLanguage': "en", // String | Preferred language for locality names in ISO 639-1 format, such as 'en' for English, 'es' for Spanish etc. Please note: 147 common world languages are supported, full list here, but not all languages are available for every location. If requested language is not available for a requested location it will default to English, if no English is available, the native, local names will be provided 
  'key': "{{API KEY}}" // String | Your API key 
};
apiInstance.ipGeolocationWithConfidenceAreaAndHazardReportApi(opts, (error, data, response) => {
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
 **ip** | **String**| IPv4 IP address in a string or numeric format. If omitted, the caller’s IP address is assumed  | [optional] 
 **localityLanguage** | **String**| Preferred language for locality names in ISO 639-1 format, such as &#39;en&#39; for English, &#39;es&#39; for Spanish etc. Please note: 147 common world languages are supported, full list here, but not all languages are available for every location. If requested language is not available for a requested location it will default to English, if no English is available, the native, local names will be provided  | [optional] 
 **key** | **String**| Your API key  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## ipGeolocationWithConfidenceAreaApi

> ipGeolocationWithConfidenceAreaApi(opts)

IP Geolocation with Confidence Area API

Returns list of geocoordinates which represents estimated geolocation confidence area.

### Example

```javascript
import IpGeolocationApi from 'ip_geolocation_api';

let apiInstance = new IpGeolocationApi.DefaultApi();
let opts = {
  'ip': "193.114.112.122", // String | IPv4 IP address in a string or numeric format. If omitted, the caller’s IP address is assumed 
  'localityLanguage': "en", // String | Preferred language for locality names in ISO 639-1 format, such as 'en' for English, 'es' for Spanish etc. Please note: 147 common world languages are supported, full list here, but not all languages are available for every location. If requested language is not available for a requested location it will default to English, if no English is available, the native, local names will be provided 
  'key': "{{API KEY}}" // String | Your API key 
};
apiInstance.ipGeolocationWithConfidenceAreaApi(opts, (error, data, response) => {
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
 **ip** | **String**| IPv4 IP address in a string or numeric format. If omitted, the caller’s IP address is assumed  | [optional] 
 **localityLanguage** | **String**| Preferred language for locality names in ISO 639-1 format, such as &#39;en&#39; for English, &#39;es&#39; for Spanish etc. Please note: 147 common world languages are supported, full list here, but not all languages are available for every location. If requested language is not available for a requested location it will default to English, if no English is available, the native, local names will be provided  | [optional] 
 **key** | **String**| Your API key  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

