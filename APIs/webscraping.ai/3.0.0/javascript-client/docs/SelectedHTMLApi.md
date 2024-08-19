# WebScrapingAi.SelectedHTMLApi

All URIs are relative to *https://api.webscraping.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getSelected**](SelectedHTMLApi.md#getSelected) | **GET** /selected | HTML of a selected page area by URL and CSS selector
[**getSelectedMultiple**](SelectedHTMLApi.md#getSelectedMultiple) | **GET** /selected-multiple | HTML of multiple page areas by URL and CSS selectors



## getSelected

> String getSelected(url, opts)

HTML of a selected page area by URL and CSS selector

Returns just HTML on success, JSON on error

### Example

```javascript
import WebScrapingAi from 'web_scraping_ai';
let defaultClient = WebScrapingAi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new WebScrapingAi.SelectedHTMLApi();
let url = "https://example.com"; // String | URL of the target page
let opts = {
  'selector': "h1", // String | CSS selector (null by default, returns whole page HTML)
  'headers': {key: null}, // {String: String} | HTTP headers to pass to the target page. Can be specified either via a nested query parameter (...&headers[One]=value1&headers=[Another]=value2) or as a JSON encoded object (...&headers={\"One\": \"value1\", \"Another\": \"value2\"})
  'timeout': 10000, // Number | Maximum processing time in ms. Increase it in case of timeout errors (10000 by default, maximum is 30000)
  'js': true, // Boolean | Execute on-page JavaScript using a headless browser (true by default)
  'jsTimeout': 2000, // Number | Maximum JavaScript rendering time in ms. Increase it in case if you see a loading indicator instead of data on the target page.
  'proxy': "datacenter", // String | Type of proxy, use residential proxies if your site restricts traffic from datacenters (datacenter by default). Note that residential proxy requests are more expensive than datacenter, see the pricing page for details.
  'country': "us", // String | Country of the proxy to use (US by default). Only available on Startup and Custom plans.
  'device': "desktop", // String | Type of device emulation.
  'errorOn404': false, // Boolean | Return error on 404 HTTP status on the target page (false by default).
  'errorOnRedirect': false // Boolean | Return error on redirect on the target page (false by default).
};
apiInstance.getSelected(url, opts, (error, data, response) => {
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
 **url** | **String**| URL of the target page | 
 **selector** | **String**| CSS selector (null by default, returns whole page HTML) | [optional] 
 **headers** | [**{String: String}**](String.md)| HTTP headers to pass to the target page. Can be specified either via a nested query parameter (...&amp;headers[One]&#x3D;value1&amp;headers&#x3D;[Another]&#x3D;value2) or as a JSON encoded object (...&amp;headers&#x3D;{\&quot;One\&quot;: \&quot;value1\&quot;, \&quot;Another\&quot;: \&quot;value2\&quot;}) | [optional] 
 **timeout** | **Number**| Maximum processing time in ms. Increase it in case of timeout errors (10000 by default, maximum is 30000) | [optional] [default to 10000]
 **js** | **Boolean**| Execute on-page JavaScript using a headless browser (true by default) | [optional] [default to true]
 **jsTimeout** | **Number**| Maximum JavaScript rendering time in ms. Increase it in case if you see a loading indicator instead of data on the target page. | [optional] [default to 2000]
 **proxy** | **String**| Type of proxy, use residential proxies if your site restricts traffic from datacenters (datacenter by default). Note that residential proxy requests are more expensive than datacenter, see the pricing page for details. | [optional] [default to &#39;datacenter&#39;]
 **country** | **String**| Country of the proxy to use (US by default). Only available on Startup and Custom plans. | [optional] [default to &#39;us&#39;]
 **device** | **String**| Type of device emulation. | [optional] [default to &#39;desktop&#39;]
 **errorOn404** | **Boolean**| Return error on 404 HTTP status on the target page (false by default). | [optional] [default to false]
 **errorOnRedirect** | **Boolean**| Return error on redirect on the target page (false by default). | [optional] [default to false]

### Return type

**String**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/html, application/json


## getSelectedMultiple

> [String] getSelectedMultiple(url, opts)

HTML of multiple page areas by URL and CSS selectors

Always returns JSON

### Example

```javascript
import WebScrapingAi from 'web_scraping_ai';
let defaultClient = WebScrapingAi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new WebScrapingAi.SelectedHTMLApi();
let url = "https://example.com"; // String | URL of the target page
let opts = {
  'selectors': ["null"], // [String] | Multiple CSS selectors (null by default, returns whole page HTML)
  'headers': {key: null}, // {String: String} | HTTP headers to pass to the target page. Can be specified either via a nested query parameter (...&headers[One]=value1&headers=[Another]=value2) or as a JSON encoded object (...&headers={\"One\": \"value1\", \"Another\": \"value2\"})
  'timeout': 10000, // Number | Maximum processing time in ms. Increase it in case of timeout errors (10000 by default, maximum is 30000)
  'js': true, // Boolean | Execute on-page JavaScript using a headless browser (true by default)
  'jsTimeout': 2000, // Number | Maximum JavaScript rendering time in ms. Increase it in case if you see a loading indicator instead of data on the target page.
  'proxy': "datacenter", // String | Type of proxy, use residential proxies if your site restricts traffic from datacenters (datacenter by default). Note that residential proxy requests are more expensive than datacenter, see the pricing page for details.
  'country': "us", // String | Country of the proxy to use (US by default). Only available on Startup and Custom plans.
  'device': "desktop", // String | Type of device emulation.
  'errorOn404': false, // Boolean | Return error on 404 HTTP status on the target page (false by default).
  'errorOnRedirect': false // Boolean | Return error on redirect on the target page (false by default).
};
apiInstance.getSelectedMultiple(url, opts, (error, data, response) => {
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
 **url** | **String**| URL of the target page | 
 **selectors** | [**[String]**](String.md)| Multiple CSS selectors (null by default, returns whole page HTML) | [optional] 
 **headers** | [**{String: String}**](String.md)| HTTP headers to pass to the target page. Can be specified either via a nested query parameter (...&amp;headers[One]&#x3D;value1&amp;headers&#x3D;[Another]&#x3D;value2) or as a JSON encoded object (...&amp;headers&#x3D;{\&quot;One\&quot;: \&quot;value1\&quot;, \&quot;Another\&quot;: \&quot;value2\&quot;}) | [optional] 
 **timeout** | **Number**| Maximum processing time in ms. Increase it in case of timeout errors (10000 by default, maximum is 30000) | [optional] [default to 10000]
 **js** | **Boolean**| Execute on-page JavaScript using a headless browser (true by default) | [optional] [default to true]
 **jsTimeout** | **Number**| Maximum JavaScript rendering time in ms. Increase it in case if you see a loading indicator instead of data on the target page. | [optional] [default to 2000]
 **proxy** | **String**| Type of proxy, use residential proxies if your site restricts traffic from datacenters (datacenter by default). Note that residential proxy requests are more expensive than datacenter, see the pricing page for details. | [optional] [default to &#39;datacenter&#39;]
 **country** | **String**| Country of the proxy to use (US by default). Only available on Startup and Custom plans. | [optional] [default to &#39;us&#39;]
 **device** | **String**| Type of device emulation. | [optional] [default to &#39;desktop&#39;]
 **errorOn404** | **Boolean**| Return error on 404 HTTP status on the target page (false by default). | [optional] [default to false]
 **errorOnRedirect** | **Boolean**| Return error on redirect on the target page (false by default). | [optional] [default to false]

### Return type

**[String]**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

