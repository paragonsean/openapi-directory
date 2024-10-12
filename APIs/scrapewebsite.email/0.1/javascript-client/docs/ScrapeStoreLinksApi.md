# ScrapeWebsiteEmailApi.ScrapeStoreLinksApi

All URIs are relative to *http://scrapewebsite.email*

Method | HTTP request | Description
------------- | ------------- | -------------
[**gETV1ScrapeStoreLinksFormat**](ScrapeStoreLinksApi.md#gETV1ScrapeStoreLinksFormat) | **GET** /v1/scrape_store_links.json | Attempts to grab the google store url or the ios store url for a site, after searching through the site.



## gETV1ScrapeStoreLinksFormat

> gETV1ScrapeStoreLinksFormat(website)

Attempts to grab the google store url or the ios store url for a site, after searching through the site.

### Example

```javascript
import ScrapeWebsiteEmailApi from 'scrape_website_email_api';

let apiInstance = new ScrapeWebsiteEmailApi.ScrapeStoreLinksApi();
let website = "website_example"; // String | <p>The website (ie. www.soundflair.com)</p> 
apiInstance.gETV1ScrapeStoreLinksFormat(website, (error, data, response) => {
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
 **website** | **String**| &lt;p&gt;The website (ie. www.soundflair.com)&lt;/p&gt;  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

