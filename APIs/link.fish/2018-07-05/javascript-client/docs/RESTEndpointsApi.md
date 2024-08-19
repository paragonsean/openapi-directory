# LinkFishApi.RESTEndpointsApi

All URIs are relative to *https://api.link.fish*

Method | HTTP request | Description
------------- | ------------- | -------------
[**urlsAppsGet**](RESTEndpointsApi.md#urlsAppsGet) | **GET** /Urls/apps | Get mobile apps
[**urlsBrowserDataGet**](RESTEndpointsApi.md#urlsBrowserDataGet) | **GET** /Urls/browser-data | Extract data (browser)
[**urlsBrowserScreenshotGet**](RESTEndpointsApi.md#urlsBrowserScreenshotGet) | **GET** /Urls/browser-screenshot | Generate screenshot (browser)
[**urlsDataGet**](RESTEndpointsApi.md#urlsDataGet) | **GET** /Urls/data | Extract data
[**urlsDataRawGet**](RESTEndpointsApi.md#urlsDataRawGet) | **GET** /Urls/data-raw | Return data of JSON/XML
[**urlsDataTabularGet**](RESTEndpointsApi.md#urlsDataTabularGet) | **GET** /Urls/data-tabular | Return tabular data
[**urlsGeoCoordinatesGet**](RESTEndpointsApi.md#urlsGeoCoordinatesGet) | **GET** /Urls/geo-coordinates | Get geo coordinates
[**urlsSocialMediaGet**](RESTEndpointsApi.md#urlsSocialMediaGet) | **GET** /Urls/social-media | Get social media accounts



## urlsAppsGet

> Apps urlsAppsGet(url, opts)

Get mobile apps

Visits the URL and checks if there are mobile apps on them and returns the found ones.  Will by default return the app identifiers and not the full URL to the apps. To return URLs instead set the parameter \&quot;return_urls\&quot; to true.  The URLs can also be created manually like this:  | Property | URL                                                | | -------- | -------------------------------------------------- | | android  | https://play.google.com/store/apps/details?id&#x3D;{ID} | | ios      | https://itunes.apple.com/us/app/app-name/id{ID}    |  Properties only get set when a value for it has been found. That means that if no app has been found only the property \&quot;url\&quot; will be set. 

### Example

```javascript
import LinkFishApi from 'link_fish_api';
let defaultClient = LinkFishApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new LinkFishApi.RESTEndpointsApi();
let url = "url_example"; // String | The URL of the website to query
let opts = {
  'returnUrls': false, // Boolean | Returns app URLs instead of the identifiers
  'browserRender': false // Boolean | If the page should be fully rendered with a browser to extract data. The request will then cost 5 credits instead of 1!
};
apiInstance.urlsAppsGet(url, opts, (error, data, response) => {
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
 **url** | **String**| The URL of the website to query | 
 **returnUrls** | **Boolean**| Returns app URLs instead of the identifiers | [optional] [default to false]
 **browserRender** | **Boolean**| If the page should be fully rendered with a browser to extract data. The request will then cost 5 credits instead of 1! | [optional] [default to false]

### Return type

[**Apps**](Apps.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## urlsBrowserDataGet

> UrlBrowser urlsBrowserDataGet(url, opts)

Extract data (browser)

Visits the URL with a full browser and extracts the data. This request costs 5 credits.

### Example

```javascript
import LinkFishApi from 'link_fish_api';
let defaultClient = LinkFishApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new LinkFishApi.RESTEndpointsApi();
let url = "url_example"; // String | The URL of the website to query
let opts = {
  'itemFormat': "'normal'", // String | If the items should be return \"normal\" with multiple levels or \"flat\" with just one level and linked instead.
  'simplifySpecialTypes': false, // Boolean | Some types like \"PropertyValue\" do save key and value in separate properties which makes the data harder to process. If this option gets set it converts them automatically into the regular key -> value format.
  'includeRawHtml': false, // Boolean | Returns additionally also the raw HTML as property \"rawHtml\".
  'screenshot': "'none'", // String | If and what kind of screenshot should be returned. Do only request screenshot generation when really needed because it will increase the response time significantly.
  'screenshotWidth': 640, // Number | The widh of the screenshot in pixel.
  'screenshotFileFormat': "'png'" // String | The file format of the screenshot
};
apiInstance.urlsBrowserDataGet(url, opts, (error, data, response) => {
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
 **url** | **String**| The URL of the website to query | 
 **itemFormat** | **String**| If the items should be return \&quot;normal\&quot; with multiple levels or \&quot;flat\&quot; with just one level and linked instead. | [optional] [default to &#39;normal&#39;]
 **simplifySpecialTypes** | **Boolean**| Some types like \&quot;PropertyValue\&quot; do save key and value in separate properties which makes the data harder to process. If this option gets set it converts them automatically into the regular key -&gt; value format. | [optional] [default to false]
 **includeRawHtml** | **Boolean**| Returns additionally also the raw HTML as property \&quot;rawHtml\&quot;. | [optional] [default to false]
 **screenshot** | **String**| If and what kind of screenshot should be returned. Do only request screenshot generation when really needed because it will increase the response time significantly. | [optional] [default to &#39;none&#39;]
 **screenshotWidth** | **Number**| The widh of the screenshot in pixel. | [optional] [default to 640]
 **screenshotFileFormat** | **String**| The file format of the screenshot | [optional] [default to &#39;png&#39;]

### Return type

[**UrlBrowser**](UrlBrowser.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## urlsBrowserScreenshotGet

> urlsBrowserScreenshotGet(url, opts)

Generate screenshot (browser)

Visits the URL with full browser and creates a screenshot. This request costs 5 credits.

### Example

```javascript
import LinkFishApi from 'link_fish_api';
let defaultClient = LinkFishApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new LinkFishApi.RESTEndpointsApi();
let url = "url_example"; // String | The URL of the website to create screenshot of
let opts = {
  'type': "'normal'", // String | What kind of screenshot should be returned. If it should be a regular 16:9 screenshot or one with the full page height
  'fileFormat': "'png'", // String | The file format of the screenshot
  'width': 640 // Number | The widh of the screenshot in pixel.
};
apiInstance.urlsBrowserScreenshotGet(url, opts, (error, data, response) => {
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
 **url** | **String**| The URL of the website to create screenshot of | 
 **type** | **String**| What kind of screenshot should be returned. If it should be a regular 16:9 screenshot or one with the full page height | [optional] [default to &#39;normal&#39;]
 **fileFormat** | **String**| The file format of the screenshot | [optional] [default to &#39;png&#39;]
 **width** | **Number**| The widh of the screenshot in pixel. | [optional] [default to 640]

### Return type

null (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: image/png, image/jpeg


## urlsDataGet

> Url urlsDataGet(url, opts)

Extract data

Visits the URL and extracts the data.

### Example

```javascript
import LinkFishApi from 'link_fish_api';
let defaultClient = LinkFishApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new LinkFishApi.RESTEndpointsApi();
let url = "url_example"; // String | The URL of the website to query
let opts = {
  'itemFormat': "'normal'", // String | If the items should be return \"normal\" with multiple levels or \"flat\" with just one level and linked instead.
  'simplifySpecialTypes': false, // Boolean | Some types like \"PropertyValue\" do save key and value in separate properties which makes the data harder to process. If this option gets set it converts them automatically into the regular key -> value format.
  'includeRawHtml': false, // Boolean | Returns additionally also the raw HTML as property \"rawHtml\".
  'browserRender': false // Boolean | If the page should be fully rendered with a browser to extract data. The request will then cost 5 credits instead of 1!
};
apiInstance.urlsDataGet(url, opts, (error, data, response) => {
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
 **url** | **String**| The URL of the website to query | 
 **itemFormat** | **String**| If the items should be return \&quot;normal\&quot; with multiple levels or \&quot;flat\&quot; with just one level and linked instead. | [optional] [default to &#39;normal&#39;]
 **simplifySpecialTypes** | **Boolean**| Some types like \&quot;PropertyValue\&quot; do save key and value in separate properties which makes the data harder to process. If this option gets set it converts them automatically into the regular key -&gt; value format. | [optional] [default to false]
 **includeRawHtml** | **Boolean**| Returns additionally also the raw HTML as property \&quot;rawHtml\&quot;. | [optional] [default to false]
 **browserRender** | **Boolean**| If the page should be fully rendered with a browser to extract data. The request will then cost 5 credits instead of 1! | [optional] [default to false]

### Return type

[**Url**](Url.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## urlsDataRawGet

> DataRaw urlsDataRawGet(url)

Return data of JSON/XML

Visits the URL and extracts the data.

### Example

```javascript
import LinkFishApi from 'link_fish_api';
let defaultClient = LinkFishApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new LinkFishApi.RESTEndpointsApi();
let url = "url_example"; // String | The URL to get the data of
apiInstance.urlsDataRawGet(url, (error, data, response) => {
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
 **url** | **String**| The URL to get the data of | 

### Return type

[**DataRaw**](DataRaw.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## urlsDataTabularGet

> DataTabular urlsDataTabularGet(url, opts)

Return tabular data

Visits the URL and extracts tabular data.

### Example

```javascript
import LinkFishApi from 'link_fish_api';
let defaultClient = LinkFishApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new LinkFishApi.RESTEndpointsApi();
let url = "url_example"; // String | The URL to get the data of
let opts = {
  'selector': "selector_example", // String | CSS selector to define tabular data which should get returned
  'browserRender': false // Boolean | If the page should be fully rendered with a browser to extract data. The request will then cost 5 credits instead of 1!
};
apiInstance.urlsDataTabularGet(url, opts, (error, data, response) => {
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
 **url** | **String**| The URL to get the data of | 
 **selector** | **String**| CSS selector to define tabular data which should get returned | [optional] 
 **browserRender** | **Boolean**| If the page should be fully rendered with a browser to extract data. The request will then cost 5 credits instead of 1! | [optional] [default to false]

### Return type

[**DataTabular**](DataTabular.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## urlsGeoCoordinatesGet

> GeoCoordinates urlsGeoCoordinatesGet(url, opts)

Get geo coordinates

Visits the URL and checks if there are Geo Coordinates on them and returns the found ones.  Properties only get set when a value for both latitude and longitude have been found. That means that if no geo coordinates have been found only the property \&quot;url\&quot; will be set.

### Example

```javascript
import LinkFishApi from 'link_fish_api';
let defaultClient = LinkFishApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new LinkFishApi.RESTEndpointsApi();
let url = "url_example"; // String | The URL of the website to query
let opts = {
  'browserRender': false // Boolean | If the page should be fully rendered with a browser to extract data. The request will then cost 5 credits instead of 1!
};
apiInstance.urlsGeoCoordinatesGet(url, opts, (error, data, response) => {
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
 **url** | **String**| The URL of the website to query | 
 **browserRender** | **Boolean**| If the page should be fully rendered with a browser to extract data. The request will then cost 5 credits instead of 1! | [optional] [default to false]

### Return type

[**GeoCoordinates**](GeoCoordinates.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## urlsSocialMediaGet

> SocialMedia urlsSocialMediaGet(url, opts)

Get social media accounts

Visits the URL and checks if there are any social media accounts and returns the found ones.  Will by default return the account identifiers and not the full URL to the profiles. To return URLs instead set the parameter \&quot;return_urls\&quot; to true.  The URLs can also be created manually like this:  | Property        | URL                                    | | --------------- | -------------------------------------- | | facebookPage    | https://facebook.com/{ID}              | | githubUser      | https://github.com/{ID}                | | googlePlus      | https://plus.google.com/+{ID}          | | instagram       | https://instagram.com/{ID}             | | linkedInCompany | https://linkedin.com/company/{ID}      | | pinterest       | https://pinterest.com/{ID}             | | twitter         | https://twitter.com/{ID}               | | youTubeUser     | https://youtube.com/user/{ID}          |  Properties only get set when a value for it has been found. That means that if no social media account has been found only the property \&quot;url\&quot; will be set. 

### Example

```javascript
import LinkFishApi from 'link_fish_api';
let defaultClient = LinkFishApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new LinkFishApi.RESTEndpointsApi();
let url = "url_example"; // String | The URL of the website to query
let opts = {
  'returnUrls': false, // Boolean | Returns profile URLs instead of the profile names/ids
  'browserRender': false // Boolean | If the page should be fully rendered with a browser to extract data. The request will then cost 5 credits instead of 1!
};
apiInstance.urlsSocialMediaGet(url, opts, (error, data, response) => {
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
 **url** | **String**| The URL of the website to query | 
 **returnUrls** | **Boolean**| Returns profile URLs instead of the profile names/ids | [optional] [default to false]
 **browserRender** | **Boolean**| If the page should be fully rendered with a browser to extract data. The request will then cost 5 credits instead of 1! | [optional] [default to false]

### Return type

[**SocialMedia**](SocialMedia.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml

