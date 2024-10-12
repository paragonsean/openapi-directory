# ScrapeWebsiteEmailApi.PingApi

All URIs are relative to *http://scrapewebsite.email*

Method | HTTP request | Description
------------- | ------------- | -------------
[**gETV1PingFormat**](PingApi.md#gETV1PingFormat) | **GET** /v1/ping.json | Returns whether the system is up.



## gETV1PingFormat

> gETV1PingFormat()

Returns whether the system is up.

&lt;p&gt;Returns ‘pong’ if the site is up&lt;/p&gt; 

### Example

```javascript
import ScrapeWebsiteEmailApi from 'scrape_website_email_api';

let apiInstance = new ScrapeWebsiteEmailApi.PingApi();
apiInstance.gETV1PingFormat((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

