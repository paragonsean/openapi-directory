# DataflowKitWebScraper.UrlToScreenshotApi

All URIs are relative to *https://api.dataflowkit.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**urlToScreenshot**](UrlToScreenshotApi.md#urlToScreenshot) | **POST** /convert/url/screenshot | Capture web page Screenshots.



## urlToScreenshot

> File urlToScreenshot(url2screenshotrequest)

Capture web page Screenshots.

Automate URL to Screenshot Conversion right in your application.  Specify request parameters like URL, Proxy, and actions to convert web pages to screenshots using Headless Chrome.  Get resulted pictures in JPG or PNG formats even from websites blocked in your area for some reason utilizing our worldwide pool of proxies.  Simulate real-world human interaction with the page. For example, before capturing a web page, you may need to scroll it.  Generate ready-to-run code for your favorite language at [https://dataflowkit.com/url-to-screenshot](https://dataflowkit.com/url-to-screenshot)

### Example

```javascript
import DataflowKitWebScraper from 'dataflow_kit_web_scraper';
let defaultClient = DataflowKitWebScraper.ApiClient.instance;
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new DataflowKitWebScraper.UrlToScreenshotApi();
let url2screenshotrequest = new DataflowKitWebScraper.Url2screenshotrequest(); // Url2screenshotrequest | 
apiInstance.urlToScreenshot(url2screenshotrequest, (error, data, response) => {
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
 **url2screenshotrequest** | [**Url2screenshotrequest**](Url2screenshotrequest.md)|  | 

### Return type

**File**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: image/jpeg, image/png, text/plain; charset=utf-8

