# NeutrinoApi.WWWApi

All URIs are relative to *https://neutrinoapi.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**browserBot**](WWWApi.md#browserBot) | **POST** /browser-bot | Browser Bot
[**hTMLClean**](WWWApi.md#hTMLClean) | **POST** /html-clean | HTML Clean
[**uRLInfo**](WWWApi.md#uRLInfo) | **GET** /url-info | URL Info



## browserBot

> BrowserBotResponse browserBot(url, opts)

Browser Bot

Browser bot can extract content, interact with keyboard and mouse events, and execute JavaScript on a website

### Example

```javascript
import NeutrinoApi from 'neutrino_api';
let defaultClient = NeutrinoApi.ApiClient.instance;
// Configure API key authorization: api-key
let api-key = defaultClient.authentications['api-key'];
api-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api-key.apiKeyPrefix = 'Token';
// Configure API key authorization: user-id
let user-id = defaultClient.authentications['user-id'];
user-id.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//user-id.apiKeyPrefix = 'Token';

let apiInstance = new NeutrinoApi.WWWApi();
let url = "url_example"; // String | The URL to load
let opts = {
  'delay': 3, // Number | Delay in seconds to wait before capturing any page data, executing selectors or JavaScript
  'exec': ["null"], // [String] | Execute JavaScript on the website. This parameter accepts JavaScript as either a string containing JavaScript or for sending multiple separate statements a JSON array or POST array can also be used. If a statement returns any value it will be returned in the 'exec-results' response. You can also use the following specially defined user interaction functions: <br> <br> <div> sleep(seconds); Just wait/sleep for the specified number of seconds. <br>click('selector'); Click on the first element matching the given selector. <br>focus('selector'); Focus on the first element matching the given selector. <br>keys('characters'); Send the specified keyboard characters. Use click() or focus() first to send keys to a specific element. <br>enter(); Send the Enter key. <br>tab(); Send the Tab key. <br> </div>
  'ignoreCertificateErrors': false, // Boolean | Ignore any TLS/SSL certificate errors and load the page anyway
  'selector': "selector_example", // String | Extract content from the page DOM using this selector. Commonly known as a CSS selector, you can find a good reference <a href=\\\"https://www.w3schools.com/cssref/css_selectors.asp\\\">here</a>
  'timeout': 30, // Number | Timeout in seconds. Give up if still trying to load the page after this number of seconds
  'userAgent': "userAgent_example" // String | Override the browsers default user-agent string with this one
};
apiInstance.browserBot(url, opts, (error, data, response) => {
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
 **url** | **String**| The URL to load | 
 **delay** | **Number**| Delay in seconds to wait before capturing any page data, executing selectors or JavaScript | [optional] [default to 3]
 **exec** | [**[String]**](String.md)| Execute JavaScript on the website. This parameter accepts JavaScript as either a string containing JavaScript or for sending multiple separate statements a JSON array or POST array can also be used. If a statement returns any value it will be returned in the &#39;exec-results&#39; response. You can also use the following specially defined user interaction functions: &lt;br&gt; &lt;br&gt; &lt;div&gt; sleep(seconds); Just wait/sleep for the specified number of seconds. &lt;br&gt;click(&#39;selector&#39;); Click on the first element matching the given selector. &lt;br&gt;focus(&#39;selector&#39;); Focus on the first element matching the given selector. &lt;br&gt;keys(&#39;characters&#39;); Send the specified keyboard characters. Use click() or focus() first to send keys to a specific element. &lt;br&gt;enter(); Send the Enter key. &lt;br&gt;tab(); Send the Tab key. &lt;br&gt; &lt;/div&gt; | [optional] 
 **ignoreCertificateErrors** | **Boolean**| Ignore any TLS/SSL certificate errors and load the page anyway | [optional] [default to false]
 **selector** | **String**| Extract content from the page DOM using this selector. Commonly known as a CSS selector, you can find a good reference &lt;a href&#x3D;\\\&quot;https://www.w3schools.com/cssref/css_selectors.asp\\\&quot;&gt;here&lt;/a&gt; | [optional] 
 **timeout** | **Number**| Timeout in seconds. Give up if still trying to load the page after this number of seconds | [optional] [default to 30]
 **userAgent** | **String**| Override the browsers default user-agent string with this one | [optional] 

### Return type

[**BrowserBotResponse**](BrowserBotResponse.md)

### Authorization

[api-key](../README.md#api-key), [user-id](../README.md#user-id)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## hTMLClean

> File hTMLClean(content, outputType)

HTML Clean

Clean and sanitize untrusted HTML

### Example

```javascript
import NeutrinoApi from 'neutrino_api';
let defaultClient = NeutrinoApi.ApiClient.instance;
// Configure API key authorization: api-key
let api-key = defaultClient.authentications['api-key'];
api-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api-key.apiKeyPrefix = 'Token';
// Configure API key authorization: user-id
let user-id = defaultClient.authentications['user-id'];
user-id.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//user-id.apiKeyPrefix = 'Token';

let apiInstance = new NeutrinoApi.WWWApi();
let content = "content_example"; // String | The HTML content. This can be either a URL to load from, a file upload (multipart/form-data) or an HTML content string
let outputType = "outputType_example"; // String | The level of sanitization, possible values are: <br><b>plain-text</b>: reduce the content to plain text only (no HTML tags at all) <br><b>simple-text</b>: allow only very basic text formatting tags like b, em, i, strong, u <br><b>basic-html</b>: allow advanced text formatting and hyper links <br><b>basic-html-with-images</b>: same as basic html but also allows image tags <br><b>advanced-html</b>: same as basic html with images but also allows many more common HTML tags like table, ul, dl, pre <br>
apiInstance.hTMLClean(content, outputType, (error, data, response) => {
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
 **content** | **String**| The HTML content. This can be either a URL to load from, a file upload (multipart/form-data) or an HTML content string | 
 **outputType** | **String**| The level of sanitization, possible values are: &lt;br&gt;&lt;b&gt;plain-text&lt;/b&gt;: reduce the content to plain text only (no HTML tags at all) &lt;br&gt;&lt;b&gt;simple-text&lt;/b&gt;: allow only very basic text formatting tags like b, em, i, strong, u &lt;br&gt;&lt;b&gt;basic-html&lt;/b&gt;: allow advanced text formatting and hyper links &lt;br&gt;&lt;b&gt;basic-html-with-images&lt;/b&gt;: same as basic html but also allows image tags &lt;br&gt;&lt;b&gt;advanced-html&lt;/b&gt;: same as basic html with images but also allows many more common HTML tags like table, ul, dl, pre &lt;br&gt; | 

### Return type

**File**

### Authorization

[api-key](../README.md#api-key), [user-id](../README.md#user-id)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## uRLInfo

> URLInfoResponse uRLInfo(url, opts)

URL Info

Parse, analyze and retrieve content from the supplied URL

### Example

```javascript
import NeutrinoApi from 'neutrino_api';
let defaultClient = NeutrinoApi.ApiClient.instance;
// Configure API key authorization: api-key
let api-key = defaultClient.authentications['api-key'];
api-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api-key.apiKeyPrefix = 'Token';
// Configure API key authorization: user-id
let user-id = defaultClient.authentications['user-id'];
user-id.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//user-id.apiKeyPrefix = 'Token';

let apiInstance = new NeutrinoApi.WWWApi();
let url = "url_example"; // String | The URL to probe
let opts = {
  'fetchContent': false, // Boolean | If this URL responds with html, text, json or xml then return the response. This option is useful if you want to perform further processing on the URL content (e.g. with the HTML Extract or HTML Clean APIs)
  'ignoreCertificateErrors': false, // Boolean | Ignore any TLS/SSL certificate errors and load the URL anyway
  'timeout': 60, // Number | Timeout in seconds. Give up if still trying to load the URL after this number of seconds
  'retry': 0 // Number | If the request fails for any reason try again this many times
};
apiInstance.uRLInfo(url, opts, (error, data, response) => {
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
 **url** | **String**| The URL to probe | 
 **fetchContent** | **Boolean**| If this URL responds with html, text, json or xml then return the response. This option is useful if you want to perform further processing on the URL content (e.g. with the HTML Extract or HTML Clean APIs) | [optional] [default to false]
 **ignoreCertificateErrors** | **Boolean**| Ignore any TLS/SSL certificate errors and load the URL anyway | [optional] [default to false]
 **timeout** | **Number**| Timeout in seconds. Give up if still trying to load the URL after this number of seconds | [optional] [default to 60]
 **retry** | **Number**| If the request fails for any reason try again this many times | [optional] [default to 0]

### Return type

[**URLInfoResponse**](URLInfoResponse.md)

### Authorization

[api-key](../README.md#api-key), [user-id](../README.md#user-id)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

