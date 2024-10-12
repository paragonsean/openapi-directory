# DataflowKitWebScraper.UrlToPdfApi

All URIs are relative to *https://api.dataflowkit.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**urlToPdf**](UrlToPdfApi.md#urlToPdf) | **POST** /convert/url/pdf | Save web page as PDF



## urlToPdf

> File urlToPdf(url2pdfrequest)

Save web page as PDF

Automate URL to PDF Conversion right in your application.  Specify request parameters like URL, Proxy, and actions to render web pages to PDF using Headless Chrome.  Get resulted PDF even from websites blocked in your area for some reason utilizing our worldwide pool of proxies.  Simulate real-world human interaction with the page. For example, before saving a web page to PDF, you may need to scroll it.  Generate ready-to-run code for your favorite language at [https://dataflowkit.com/url-to-pdf](https://dataflowkit.com/url-to-pdf)

### Example

```javascript
import DataflowKitWebScraper from 'dataflow_kit_web_scraper';
let defaultClient = DataflowKitWebScraper.ApiClient.instance;
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new DataflowKitWebScraper.UrlToPdfApi();
let url2pdfrequest = new DataflowKitWebScraper.Url2pdfrequest(); // Url2pdfrequest | 
apiInstance.urlToPdf(url2pdfrequest, (error, data, response) => {
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
 **url2pdfrequest** | [**Url2pdfrequest**](Url2pdfrequest.md)|  | 

### Return type

**File**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/pdf, text/plain; charset=utf-8

