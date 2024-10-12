# InterzoidGlobalPageLoadPerformanceApi.PageLoadPerformanceTimeApi

All URIs are relative to *https://api.interzoid.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**globalpageload**](PageLoadPerformanceTimeApi.md#globalpageload) | **GET** /globalpageload | Gets page load (or an API call) performance from a specified global geography such as Paris, Tokyo, Virginia, Mumbai, Frankfurt, London, Seoul, California, Sao Paolo, and many more.



## globalpageload

> Globalpageload200Response globalpageload(license, origin, url)

Gets page load (or an API call) performance from a specified global geography such as Paris, Tokyo, Virginia, Mumbai, Frankfurt, London, Seoul, California, Sao Paolo, and many more.

Gets page load performance from a specified geography 

### Example

```javascript
import InterzoidGlobalPageLoadPerformanceApi from 'interzoid_global_page_load_performance_api';

let apiInstance = new InterzoidGlobalPageLoadPerformanceApi.PageLoadPerformanceTimeApi();
let license = "license_example"; // String | Your Interzoid license API key. Register at www.interzoid.com/register
let origin = "origin_example"; // String | Geographic location to perform the measurement from (Paris, Hong Kong, Seoul, Mumbai, Sao Paolo, London, etc. see API home page for full list)
let url = "url_example"; // String | specific URL to perform load test time
apiInstance.globalpageload(license, origin, url, (error, data, response) => {
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
 **license** | **String**| Your Interzoid license API key. Register at www.interzoid.com/register | 
 **origin** | **String**| Geographic location to perform the measurement from (Paris, Hong Kong, Seoul, Mumbai, Sao Paolo, London, etc. see API home page for full list) | 
 **url** | **String**| specific URL to perform load test time | 

### Return type

[**Globalpageload200Response**](Globalpageload200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

