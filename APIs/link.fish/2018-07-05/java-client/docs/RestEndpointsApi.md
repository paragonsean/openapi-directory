# RestEndpointsApi

All URIs are relative to *https://api.link.fish*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**urlsAppsGet**](RestEndpointsApi.md#urlsAppsGet) | **GET** /Urls/apps | Get mobile apps |
| [**urlsBrowserDataGet**](RestEndpointsApi.md#urlsBrowserDataGet) | **GET** /Urls/browser-data | Extract data (browser) |
| [**urlsBrowserScreenshotGet**](RestEndpointsApi.md#urlsBrowserScreenshotGet) | **GET** /Urls/browser-screenshot | Generate screenshot (browser) |
| [**urlsDataGet**](RestEndpointsApi.md#urlsDataGet) | **GET** /Urls/data | Extract data |
| [**urlsDataRawGet**](RestEndpointsApi.md#urlsDataRawGet) | **GET** /Urls/data-raw | Return data of JSON/XML |
| [**urlsDataTabularGet**](RestEndpointsApi.md#urlsDataTabularGet) | **GET** /Urls/data-tabular | Return tabular data |
| [**urlsGeoCoordinatesGet**](RestEndpointsApi.md#urlsGeoCoordinatesGet) | **GET** /Urls/geo-coordinates | Get geo coordinates |
| [**urlsSocialMediaGet**](RestEndpointsApi.md#urlsSocialMediaGet) | **GET** /Urls/social-media | Get social media accounts |


<a id="urlsAppsGet"></a>
# **urlsAppsGet**
> Apps urlsAppsGet(url, returnUrls, browserRender)

Get mobile apps

Visits the URL and checks if there are mobile apps on them and returns the found ones.  Will by default return the app identifiers and not the full URL to the apps. To return URLs instead set the parameter \&quot;return_urls\&quot; to true.  The URLs can also be created manually like this:  | Property | URL                                                | | -------- | -------------------------------------------------- | | android  | https://play.google.com/store/apps/details?id&#x3D;{ID} | | ios      | https://itunes.apple.com/us/app/app-name/id{ID}    |  Properties only get set when a value for it has been found. That means that if no app has been found only the property \&quot;url\&quot; will be set. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RestEndpointsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.link.fish");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    RestEndpointsApi apiInstance = new RestEndpointsApi(defaultClient);
    String url = "url_example"; // String | The URL of the website to query
    Boolean returnUrls = false; // Boolean | Returns app URLs instead of the identifiers
    Boolean browserRender = false; // Boolean | If the page should be fully rendered with a browser to extract data. The request will then cost 5 credits instead of 1!
    try {
      Apps result = apiInstance.urlsAppsGet(url, returnUrls, browserRender);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RestEndpointsApi#urlsAppsGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **url** | **String**| The URL of the website to query | |
| **returnUrls** | **Boolean**| Returns app URLs instead of the identifiers | [optional] [default to false] |
| **browserRender** | **Boolean**| If the page should be fully rendered with a browser to extract data. The request will then cost 5 credits instead of 1! | [optional] [default to false] |

### Return type

[**Apps**](Apps.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - Successful Request |  -  |
| **400** | Bad Request - Request was unacceptable. Normally because of missing required parameters or invalid data. |  -  |
| **401** | Unauthorized - Authentication missing or failed. |  -  |
| **402** | Request failed - All parameters were correct but the request failed. |  -  |
| **404** | Not Found - The requested resource does not exist. |  -  |
| **500** | Internal Server Error - Something went wrong on our side. |  -  |

<a id="urlsBrowserDataGet"></a>
# **urlsBrowserDataGet**
> UrlBrowser urlsBrowserDataGet(url, itemFormat, simplifySpecialTypes, includeRawHtml, screenshot, screenshotWidth, screenshotFileFormat)

Extract data (browser)

Visits the URL with a full browser and extracts the data. This request costs 5 credits.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RestEndpointsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.link.fish");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    RestEndpointsApi apiInstance = new RestEndpointsApi(defaultClient);
    String url = "url_example"; // String | The URL of the website to query
    String itemFormat = "normal"; // String | If the items should be return \"normal\" with multiple levels or \"flat\" with just one level and linked instead.
    Boolean simplifySpecialTypes = false; // Boolean | Some types like \"PropertyValue\" do save key and value in separate properties which makes the data harder to process. If this option gets set it converts them automatically into the regular key -> value format.
    Boolean includeRawHtml = false; // Boolean | Returns additionally also the raw HTML as property \"rawHtml\".
    String screenshot = "none"; // String | If and what kind of screenshot should be returned. Do only request screenshot generation when really needed because it will increase the response time significantly.
    Integer screenshotWidth = 640; // Integer | The widh of the screenshot in pixel.
    String screenshotFileFormat = "png"; // String | The file format of the screenshot
    try {
      UrlBrowser result = apiInstance.urlsBrowserDataGet(url, itemFormat, simplifySpecialTypes, includeRawHtml, screenshot, screenshotWidth, screenshotFileFormat);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RestEndpointsApi#urlsBrowserDataGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **url** | **String**| The URL of the website to query | |
| **itemFormat** | **String**| If the items should be return \&quot;normal\&quot; with multiple levels or \&quot;flat\&quot; with just one level and linked instead. | [optional] [default to normal] [enum: normal, flat] |
| **simplifySpecialTypes** | **Boolean**| Some types like \&quot;PropertyValue\&quot; do save key and value in separate properties which makes the data harder to process. If this option gets set it converts them automatically into the regular key -&gt; value format. | [optional] [default to false] |
| **includeRawHtml** | **Boolean**| Returns additionally also the raw HTML as property \&quot;rawHtml\&quot;. | [optional] [default to false] |
| **screenshot** | **String**| If and what kind of screenshot should be returned. Do only request screenshot generation when really needed because it will increase the response time significantly. | [optional] [default to none] [enum: none, normal, full] |
| **screenshotWidth** | **Integer**| The widh of the screenshot in pixel. | [optional] [default to 640] |
| **screenshotFileFormat** | **String**| The file format of the screenshot | [optional] [default to png] [enum: png, jpg] |

### Return type

[**UrlBrowser**](UrlBrowser.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - Successful Request |  -  |
| **400** | Bad Request - Request was unacceptable. Normally because of missing required parameters or invalid data. |  -  |
| **401** | Unauthorized - Authentication missing or failed. |  -  |
| **402** | Request failed - All parameters were correct but the request failed. |  -  |
| **404** | Not Found - The requested resource does not exist. |  -  |
| **500** | Internal Server Error - Something went wrong on our side. |  -  |

<a id="urlsBrowserScreenshotGet"></a>
# **urlsBrowserScreenshotGet**
> urlsBrowserScreenshotGet(url, type, fileFormat, width)

Generate screenshot (browser)

Visits the URL with full browser and creates a screenshot. This request costs 5 credits.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RestEndpointsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.link.fish");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    RestEndpointsApi apiInstance = new RestEndpointsApi(defaultClient);
    String url = "url_example"; // String | The URL of the website to create screenshot of
    String type = "normal"; // String | What kind of screenshot should be returned. If it should be a regular 16:9 screenshot or one with the full page height
    String fileFormat = "png"; // String | The file format of the screenshot
    Integer width = 640; // Integer | The widh of the screenshot in pixel.
    try {
      apiInstance.urlsBrowserScreenshotGet(url, type, fileFormat, width);
    } catch (ApiException e) {
      System.err.println("Exception when calling RestEndpointsApi#urlsBrowserScreenshotGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **url** | **String**| The URL of the website to create screenshot of | |
| **type** | **String**| What kind of screenshot should be returned. If it should be a regular 16:9 screenshot or one with the full page height | [optional] [default to normal] [enum: normal, full] |
| **fileFormat** | **String**| The file format of the screenshot | [optional] [default to png] [enum: png, jpg] |
| **width** | **Integer**| The widh of the screenshot in pixel. | [optional] [default to 640] |

### Return type

null (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: image/png, image/jpeg

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - Successful Request |  -  |
| **400** | Bad Request - Request was unacceptable. Normally because of missing required parameters or invalid data. |  -  |
| **401** | Unauthorized - Authentication missing or failed. |  -  |
| **402** | Request failed - All parameters were correct but the request failed. |  -  |
| **404** | Not Found - The requested resource does not exist. |  -  |
| **500** | Internal Server Error - Something went wrong on our side. |  -  |

<a id="urlsDataGet"></a>
# **urlsDataGet**
> Url urlsDataGet(url, itemFormat, simplifySpecialTypes, includeRawHtml, browserRender)

Extract data

Visits the URL and extracts the data.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RestEndpointsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.link.fish");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    RestEndpointsApi apiInstance = new RestEndpointsApi(defaultClient);
    String url = "url_example"; // String | The URL of the website to query
    String itemFormat = "normal"; // String | If the items should be return \"normal\" with multiple levels or \"flat\" with just one level and linked instead.
    Boolean simplifySpecialTypes = false; // Boolean | Some types like \"PropertyValue\" do save key and value in separate properties which makes the data harder to process. If this option gets set it converts them automatically into the regular key -> value format.
    Boolean includeRawHtml = false; // Boolean | Returns additionally also the raw HTML as property \"rawHtml\".
    Boolean browserRender = false; // Boolean | If the page should be fully rendered with a browser to extract data. The request will then cost 5 credits instead of 1!
    try {
      Url result = apiInstance.urlsDataGet(url, itemFormat, simplifySpecialTypes, includeRawHtml, browserRender);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RestEndpointsApi#urlsDataGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **url** | **String**| The URL of the website to query | |
| **itemFormat** | **String**| If the items should be return \&quot;normal\&quot; with multiple levels or \&quot;flat\&quot; with just one level and linked instead. | [optional] [default to normal] [enum: normal, flat] |
| **simplifySpecialTypes** | **Boolean**| Some types like \&quot;PropertyValue\&quot; do save key and value in separate properties which makes the data harder to process. If this option gets set it converts them automatically into the regular key -&gt; value format. | [optional] [default to false] |
| **includeRawHtml** | **Boolean**| Returns additionally also the raw HTML as property \&quot;rawHtml\&quot;. | [optional] [default to false] |
| **browserRender** | **Boolean**| If the page should be fully rendered with a browser to extract data. The request will then cost 5 credits instead of 1! | [optional] [default to false] |

### Return type

[**Url**](Url.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - Successful Request |  -  |
| **400** | Bad Request - Request was unacceptable. Normally because of missing required parameters or invalid data. |  -  |
| **401** | Unauthorized - Authentication missing or failed. |  -  |
| **402** | Request failed - All parameters were correct but the request failed. |  -  |
| **404** | Not Found - The requested resource does not exist. |  -  |
| **500** | Internal Server Error - Something went wrong on our side. |  -  |

<a id="urlsDataRawGet"></a>
# **urlsDataRawGet**
> DataRaw urlsDataRawGet(url)

Return data of JSON/XML

Visits the URL and extracts the data.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RestEndpointsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.link.fish");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    RestEndpointsApi apiInstance = new RestEndpointsApi(defaultClient);
    String url = "url_example"; // String | The URL to get the data of
    try {
      DataRaw result = apiInstance.urlsDataRawGet(url);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RestEndpointsApi#urlsDataRawGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **url** | **String**| The URL to get the data of | |

### Return type

[**DataRaw**](DataRaw.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - Successful Request |  -  |
| **400** | Bad Request - Request was unacceptable. Normally because of missing required parameters or invalid data. |  -  |
| **401** | Unauthorized - Authentication missing or failed. |  -  |
| **402** | Request failed - All parameters were correct but the request failed. |  -  |
| **404** | Not Found - The requested resource does not exist. |  -  |
| **500** | Internal Server Error - Something went wrong on our side. |  -  |

<a id="urlsDataTabularGet"></a>
# **urlsDataTabularGet**
> DataTabular urlsDataTabularGet(url, selector, browserRender)

Return tabular data

Visits the URL and extracts tabular data.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RestEndpointsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.link.fish");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    RestEndpointsApi apiInstance = new RestEndpointsApi(defaultClient);
    String url = "url_example"; // String | The URL to get the data of
    String selector = "selector_example"; // String | CSS selector to define tabular data which should get returned
    Boolean browserRender = false; // Boolean | If the page should be fully rendered with a browser to extract data. The request will then cost 5 credits instead of 1!
    try {
      DataTabular result = apiInstance.urlsDataTabularGet(url, selector, browserRender);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RestEndpointsApi#urlsDataTabularGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **url** | **String**| The URL to get the data of | |
| **selector** | **String**| CSS selector to define tabular data which should get returned | [optional] |
| **browserRender** | **Boolean**| If the page should be fully rendered with a browser to extract data. The request will then cost 5 credits instead of 1! | [optional] [default to false] |

### Return type

[**DataTabular**](DataTabular.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - Successful Request |  -  |
| **400** | Bad Request - Request was unacceptable. Normally because of missing required parameters or invalid data. |  -  |
| **401** | Unauthorized - Authentication missing or failed. |  -  |
| **402** | Request failed - All parameters were correct but the request failed. |  -  |
| **404** | Not Found - The requested resource does not exist. |  -  |
| **500** | Internal Server Error - Something went wrong on our side. |  -  |

<a id="urlsGeoCoordinatesGet"></a>
# **urlsGeoCoordinatesGet**
> GeoCoordinates urlsGeoCoordinatesGet(url, browserRender)

Get geo coordinates

Visits the URL and checks if there are Geo Coordinates on them and returns the found ones.  Properties only get set when a value for both latitude and longitude have been found. That means that if no geo coordinates have been found only the property \&quot;url\&quot; will be set.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RestEndpointsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.link.fish");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    RestEndpointsApi apiInstance = new RestEndpointsApi(defaultClient);
    String url = "url_example"; // String | The URL of the website to query
    Boolean browserRender = false; // Boolean | If the page should be fully rendered with a browser to extract data. The request will then cost 5 credits instead of 1!
    try {
      GeoCoordinates result = apiInstance.urlsGeoCoordinatesGet(url, browserRender);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RestEndpointsApi#urlsGeoCoordinatesGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **url** | **String**| The URL of the website to query | |
| **browserRender** | **Boolean**| If the page should be fully rendered with a browser to extract data. The request will then cost 5 credits instead of 1! | [optional] [default to false] |

### Return type

[**GeoCoordinates**](GeoCoordinates.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - Successful Request |  -  |
| **400** | Bad Request - Request was unacceptable. Normally because of missing required parameters or invalid data. |  -  |
| **401** | Unauthorized - Authentication missing or failed. |  -  |
| **402** | Request failed - All parameters were correct but the request failed. |  -  |
| **404** | Not Found - The requested resource does not exist. |  -  |
| **500** | Internal Server Error - Something went wrong on our side. |  -  |

<a id="urlsSocialMediaGet"></a>
# **urlsSocialMediaGet**
> SocialMedia urlsSocialMediaGet(url, returnUrls, browserRender)

Get social media accounts

Visits the URL and checks if there are any social media accounts and returns the found ones.  Will by default return the account identifiers and not the full URL to the profiles. To return URLs instead set the parameter \&quot;return_urls\&quot; to true.  The URLs can also be created manually like this:  | Property        | URL                                    | | --------------- | -------------------------------------- | | facebookPage    | https://facebook.com/{ID}              | | githubUser      | https://github.com/{ID}                | | googlePlus      | https://plus.google.com/+{ID}          | | instagram       | https://instagram.com/{ID}             | | linkedInCompany | https://linkedin.com/company/{ID}      | | pinterest       | https://pinterest.com/{ID}             | | twitter         | https://twitter.com/{ID}               | | youTubeUser     | https://youtube.com/user/{ID}          |  Properties only get set when a value for it has been found. That means that if no social media account has been found only the property \&quot;url\&quot; will be set. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RestEndpointsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.link.fish");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    RestEndpointsApi apiInstance = new RestEndpointsApi(defaultClient);
    String url = "url_example"; // String | The URL of the website to query
    Boolean returnUrls = false; // Boolean | Returns profile URLs instead of the profile names/ids
    Boolean browserRender = false; // Boolean | If the page should be fully rendered with a browser to extract data. The request will then cost 5 credits instead of 1!
    try {
      SocialMedia result = apiInstance.urlsSocialMediaGet(url, returnUrls, browserRender);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RestEndpointsApi#urlsSocialMediaGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **url** | **String**| The URL of the website to query | |
| **returnUrls** | **Boolean**| Returns profile URLs instead of the profile names/ids | [optional] [default to false] |
| **browserRender** | **Boolean**| If the page should be fully rendered with a browser to extract data. The request will then cost 5 credits instead of 1! | [optional] [default to false] |

### Return type

[**SocialMedia**](SocialMedia.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - Successful Request |  -  |
| **400** | Bad Request - Request was unacceptable. Normally because of missing required parameters or invalid data. |  -  |
| **401** | Unauthorized - Authentication missing or failed. |  -  |
| **402** | Request failed - All parameters were correct but the request failed. |  -  |
| **404** | Not Found - The requested resource does not exist. |  -  |
| **500** | Internal Server Error - Something went wrong on our side. |  -  |

