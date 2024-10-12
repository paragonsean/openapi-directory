# ScreenshotApi

All URIs are relative to *https://api.browshot.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createMultipleScreenshots**](ScreenshotApi.md#createMultipleScreenshots) | **GET** /screenshot/multiple | Request multiple screenshots |
| [**createScreenshot**](ScreenshotApi.md#createScreenshot) | **GET** /screenshot/create | Request a screenshot |
| [**deleteScreenshot**](ScreenshotApi.md#deleteScreenshot) | **GET** /screenshot/delete | Delete screenshot data |
| [**getHTML**](ScreenshotApi.md#getHTML) | **GET** /screenshot/html | Get the HTML code |
| [**getMultipleScreenshotsInfo**](ScreenshotApi.md#getMultipleScreenshotsInfo) | **GET** /screenshot/list | Get information about screenshots |
| [**getScreenshotInfo**](ScreenshotApi.md#getScreenshotInfo) | **GET** /screenshot/info | Query screenshot status |
| [**getThumbnail**](ScreenshotApi.md#getThumbnail) | **GET** /screenshot/thumbnail | Retrieve a thumbnail image |
| [**hostScreenshot**](ScreenshotApi.md#hostScreenshot) | **GET** /screenshot/host | Host thumbnails on your own S3 account or on Browshot. |
| [**searchScreenshot**](ScreenshotApi.md#searchScreenshot) | **GET** /screenshot/search | Search for screenshots |
| [**shareScreenshot**](ScreenshotApi.md#shareScreenshot) | **GET** /screenshot/share | Share a screenshot |


<a id="createMultipleScreenshots"></a>
# **createMultipleScreenshots**
> ScreenshotList createMultipleScreenshots(url, instanceId, size, cache, delay, flashDelay, screenWidth, screenHeight, priority, referer, postData, cookie, script, details, html, maxWait, headers, hosting, hostingHeight, hostingWidth, hostingScale, hostingBucket, hostingFile, hostingHeaders)

Request multiple screenshots

Request multiple screenshots in one API call. The API call accepts all the parameters supported by screenshot/create. You can specify up to 10 URLs and 10 instances for a total of 100 screenshots in one API call. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ScreenshotApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.browshot.com/api/v1");
    
    // Configure API key authorization: apiKeyQuery
    ApiKeyAuth apiKeyQuery = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyQuery");
    apiKeyQuery.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyQuery.setApiKeyPrefix("Token");

    ScreenshotApi apiInstance = new ScreenshotApi(defaultClient);
    String url = "url_example"; // String | URL of the page to get a screenshot for. You can specify multiple url parameters (up to 10).
    Integer instanceId = 56; // Integer | instance ID to use. You can specify multiple instance_id parameters (up to 10).
    String size = "screen"; // String | screenshot size - \"screen\" (default) or \"page\"
    Integer cache = 86400; // Integer | use a previous screenshot (same URL, same instance) if it was done within <cache_value> seconds. The default value is 24hours. Specify cache=0 if you want a new screenshot.
    Integer delay = 5; // Integer | number of seconds to wait after the page has loaded. This is used to let JavaScript run longer before taking the screenshot. Use delay=0 to take screenshots faster.
    Integer flashDelay = 10; // Integer | number of seconds to wait after the page has loaded if Flash elements are present. Use flash_delay=0 to take screenshots faster.
    Integer screenWidth = 1024; // Integer | width of the browser window. For desktop browsers only.
    Integer screenHeight = 768; // Integer | height of the browser window. For desktop browsers only. (Note: full-page screenshots can have a height of up to 15,000px)
    Integer priority = 56; // Integer | assign priority to the screenshot (for private instances only)
    String referer = "referer_example"; // String | use a custom referrer header - paid screenshots only
    String postData = "postData_example"; // String | send a POST requests with post_data, useful for filling out forms - paid screenshots only
    String cookie = "cookie_example"; // String | set a cookie for the URL requested (see Custom POST Data, Referer and Cookie) Cookies should be separated by a ; - paid screenshots only
    String script = "script_example"; // String | URL of javascript file to execute after the page load event
    Integer details = 2; // Integer | level of information available with screenshot/info
    Integer html = 0; // Integer | saves the HTML of the rendered page which can be retrieved by the API call screenshot/html. This feature costs *1 credit* per screenshot.
    Integer maxWait = 0; // Integer | maximum number of seconds to wait before triggering the PageLoad event. Note that delay will still be used. (default: 0 = disabled)
    String headers = "headers_example"; // String | any custom HTTP headers. (Not supported with Internet Explorer)
    String hosting = "s3"; // String | hosting option - s3 or browshot
    Integer hostingHeight = 56; // Integer | maximum height of the thumbnail to host
    Integer hostingWidth = 56; // Integer | maximum height of the thumbnail to host
    Float hostingScale = 1.0F; // Float | scale of the thumbnail to host
    String hostingBucket = "hostingBucket_example"; // String | S3 bucket to upload the screenshot or thumbnail (required for S3)
    String hostingFile = "hostingFile_example"; // String | file name to use (for S3 only)
    String hostingHeaders = "hostingHeaders_example"; // String | list of headers to add to the S3 object (for S3 only)
    try {
      ScreenshotList result = apiInstance.createMultipleScreenshots(url, instanceId, size, cache, delay, flashDelay, screenWidth, screenHeight, priority, referer, postData, cookie, script, details, html, maxWait, headers, hosting, hostingHeight, hostingWidth, hostingScale, hostingBucket, hostingFile, hostingHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ScreenshotApi#createMultipleScreenshots");
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
| **url** | **String**| URL of the page to get a screenshot for. You can specify multiple url parameters (up to 10). | |
| **instanceId** | **Integer**| instance ID to use. You can specify multiple instance_id parameters (up to 10). | |
| **size** | **String**| screenshot size - \&quot;screen\&quot; (default) or \&quot;page\&quot; | [optional] [default to screen] [enum: screen, page] |
| **cache** | **Integer**| use a previous screenshot (same URL, same instance) if it was done within &lt;cache_value&gt; seconds. The default value is 24hours. Specify cache&#x3D;0 if you want a new screenshot. | [optional] [default to 86400] |
| **delay** | **Integer**| number of seconds to wait after the page has loaded. This is used to let JavaScript run longer before taking the screenshot. Use delay&#x3D;0 to take screenshots faster. | [optional] [default to 5] |
| **flashDelay** | **Integer**| number of seconds to wait after the page has loaded if Flash elements are present. Use flash_delay&#x3D;0 to take screenshots faster. | [optional] [default to 10] |
| **screenWidth** | **Integer**| width of the browser window. For desktop browsers only. | [optional] [default to 1024] |
| **screenHeight** | **Integer**| height of the browser window. For desktop browsers only. (Note: full-page screenshots can have a height of up to 15,000px) | [optional] [default to 768] |
| **priority** | **Integer**| assign priority to the screenshot (for private instances only) | [optional] |
| **referer** | **String**| use a custom referrer header - paid screenshots only | [optional] |
| **postData** | **String**| send a POST requests with post_data, useful for filling out forms - paid screenshots only | [optional] |
| **cookie** | **String**| set a cookie for the URL requested (see Custom POST Data, Referer and Cookie) Cookies should be separated by a ; - paid screenshots only | [optional] |
| **script** | **String**| URL of javascript file to execute after the page load event | [optional] |
| **details** | **Integer**| level of information available with screenshot/info | [optional] [default to 2] |
| **html** | **Integer**| saves the HTML of the rendered page which can be retrieved by the API call screenshot/html. This feature costs *1 credit* per screenshot. | [optional] [default to 0] |
| **maxWait** | **Integer**| maximum number of seconds to wait before triggering the PageLoad event. Note that delay will still be used. (default: 0 &#x3D; disabled) | [optional] [default to 0] |
| **headers** | **String**| any custom HTTP headers. (Not supported with Internet Explorer) | [optional] |
| **hosting** | **String**| hosting option - s3 or browshot | [optional] [enum: s3, browshot] |
| **hostingHeight** | **Integer**| maximum height of the thumbnail to host | [optional] |
| **hostingWidth** | **Integer**| maximum height of the thumbnail to host | [optional] |
| **hostingScale** | **Float**| scale of the thumbnail to host | [optional] [default to 1.0] |
| **hostingBucket** | **String**| S3 bucket to upload the screenshot or thumbnail (required for S3) | [optional] |
| **hostingFile** | **String**| file name to use (for S3 only) | [optional] |
| **hostingHeaders** | **String**| list of headers to add to the S3 object (for S3 only) | [optional] |

### Return type

[**ScreenshotList**](ScreenshotList.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Request accepted |  -  |
| **403** | Error |  -  |

<a id="createScreenshot"></a>
# **createScreenshot**
> Screenshot createScreenshot(url, instanceId, size, cache, delay, flashDelay, screenWidth, screenHeight, priority, referer, postData, cookie, script, details, html, maxWait, headers, shots, shotInterval, hosting, hostingHeight, hostingWidth, hostingScale, hostingBucket, hostingFile, hostingHeaders)

Request a screenshot

Screenshots requests to private and shared instances require a positive balance.  *IMPORTANT*: Remember that you can only do 100 free screenshots per month. To used a premium instance, use instance_id&#x3D;65 for example. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ScreenshotApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.browshot.com/api/v1");
    
    // Configure API key authorization: apiKeyQuery
    ApiKeyAuth apiKeyQuery = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyQuery");
    apiKeyQuery.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyQuery.setApiKeyPrefix("Token");

    ScreenshotApi apiInstance = new ScreenshotApi(defaultClient);
    String url = "url_example"; // String | URL of the page to get a screenshot for
    Integer instanceId = 56; // Integer | instance ID to use
    String size = "screen"; // String | screenshot size - \"screen\" (default) or \"page\"
    Integer cache = 86400; // Integer | use a previous screenshot (same URL, same instance) if it was done within <cache_value> seconds. The default value is 24hours. Specify cache=0 if you want a new screenshot.
    Integer delay = 5; // Integer | number of seconds to wait after the page has loaded. This is used to let JavaScript run longer before taking the screenshot. Use delay=0 to take screenshots faster.
    Integer flashDelay = 10; // Integer | number of seconds to wait after the page has loaded if Flash elements are present. Use flash_delay=0 to take screenshots faster.
    Integer screenWidth = 1024; // Integer | width of the browser window. For desktop browsers only.
    Integer screenHeight = 768; // Integer | height of the browser window. For desktop browsers only. (Note: full-page screenshots can have a height of up to 15,000px)
    Integer priority = 56; // Integer | assign priority to the screenshot (for private instances only)
    String referer = "referer_example"; // String | use a custom referrer header - paid screenshots only
    String postData = "postData_example"; // String | send a POST requests with post_data, useful for filling out forms - paid screenshots only
    String cookie = "cookie_example"; // String | set a cookie for the URL requested (see Custom POST Data, Referer and Cookie) Cookies should be separated by a ; - paid screenshots only
    String script = "script_example"; // String | URL of javascript file to execute after the page load event
    Integer details = 2; // Integer | level of information available with screenshot/info
    Integer html = 0; // Integer | saves the HTML of the rendered page which can be retrieved by the API call screenshot/html. This feature costs *1 credit* per screenshot.
    Integer maxWait = 0; // Integer | maximum number of seconds to wait before triggering the PageLoad event. Note that delay will still be used. (default: 0 = disabled)
    String headers = "headers_example"; // String | any custom HTTP headers. (Not supported with Internet Explorer)
    Integer shots = 1; // Integer | take multiple screenshots of the same page. This costs 1 additional credit for every 2 additional screenshots.
    Integer shotInterval = 5; // Integer | number of seconds between 2 screenshots
    String hosting = "s3"; // String | hosting option - s3 or browshot
    Integer hostingHeight = 56; // Integer | maximum height of the thumbnail to host
    Integer hostingWidth = 56; // Integer | maximum height of the thumbnail to host
    Float hostingScale = 1.0F; // Float | scale of the thumbnail to host
    String hostingBucket = "hostingBucket_example"; // String | S3 bucket to upload the screenshot or thumbnail (required for S3)
    String hostingFile = "hostingFile_example"; // String | file name to use (for S3 only)
    String hostingHeaders = "hostingHeaders_example"; // String | list of headers to add to the S3 object (for S3 only)
    try {
      Screenshot result = apiInstance.createScreenshot(url, instanceId, size, cache, delay, flashDelay, screenWidth, screenHeight, priority, referer, postData, cookie, script, details, html, maxWait, headers, shots, shotInterval, hosting, hostingHeight, hostingWidth, hostingScale, hostingBucket, hostingFile, hostingHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ScreenshotApi#createScreenshot");
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
| **url** | **String**| URL of the page to get a screenshot for | |
| **instanceId** | **Integer**| instance ID to use | |
| **size** | **String**| screenshot size - \&quot;screen\&quot; (default) or \&quot;page\&quot; | [optional] [default to screen] [enum: screen, page] |
| **cache** | **Integer**| use a previous screenshot (same URL, same instance) if it was done within &lt;cache_value&gt; seconds. The default value is 24hours. Specify cache&#x3D;0 if you want a new screenshot. | [optional] [default to 86400] |
| **delay** | **Integer**| number of seconds to wait after the page has loaded. This is used to let JavaScript run longer before taking the screenshot. Use delay&#x3D;0 to take screenshots faster. | [optional] [default to 5] |
| **flashDelay** | **Integer**| number of seconds to wait after the page has loaded if Flash elements are present. Use flash_delay&#x3D;0 to take screenshots faster. | [optional] [default to 10] |
| **screenWidth** | **Integer**| width of the browser window. For desktop browsers only. | [optional] [default to 1024] |
| **screenHeight** | **Integer**| height of the browser window. For desktop browsers only. (Note: full-page screenshots can have a height of up to 15,000px) | [optional] [default to 768] |
| **priority** | **Integer**| assign priority to the screenshot (for private instances only) | [optional] |
| **referer** | **String**| use a custom referrer header - paid screenshots only | [optional] |
| **postData** | **String**| send a POST requests with post_data, useful for filling out forms - paid screenshots only | [optional] |
| **cookie** | **String**| set a cookie for the URL requested (see Custom POST Data, Referer and Cookie) Cookies should be separated by a ; - paid screenshots only | [optional] |
| **script** | **String**| URL of javascript file to execute after the page load event | [optional] |
| **details** | **Integer**| level of information available with screenshot/info | [optional] [default to 2] |
| **html** | **Integer**| saves the HTML of the rendered page which can be retrieved by the API call screenshot/html. This feature costs *1 credit* per screenshot. | [optional] [default to 0] |
| **maxWait** | **Integer**| maximum number of seconds to wait before triggering the PageLoad event. Note that delay will still be used. (default: 0 &#x3D; disabled) | [optional] [default to 0] |
| **headers** | **String**| any custom HTTP headers. (Not supported with Internet Explorer) | [optional] |
| **shots** | **Integer**| take multiple screenshots of the same page. This costs 1 additional credit for every 2 additional screenshots. | [optional] [default to 1] |
| **shotInterval** | **Integer**| number of seconds between 2 screenshots | [optional] [default to 5] |
| **hosting** | **String**| hosting option - s3 or browshot | [optional] [enum: s3, browshot] |
| **hostingHeight** | **Integer**| maximum height of the thumbnail to host | [optional] |
| **hostingWidth** | **Integer**| maximum height of the thumbnail to host | [optional] |
| **hostingScale** | **Float**| scale of the thumbnail to host | [optional] [default to 1.0] |
| **hostingBucket** | **String**| S3 bucket to upload the screenshot or thumbnail (required for S3) | [optional] |
| **hostingFile** | **String**| file name to use (for S3 only) | [optional] |
| **hostingHeaders** | **String**| list of headers to add to the S3 object (for S3 only) | [optional] |

### Return type

[**Screenshot**](Screenshot.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Request accepted |  -  |
| **403** | Error |  -  |

<a id="deleteScreenshot"></a>
# **deleteScreenshot**
> List&lt;ScreenshotShort&gt; deleteScreenshot(id, data)

Delete screenshot data

You can delete details of your screenshots to remove any confidential information. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ScreenshotApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.browshot.com/api/v1");
    
    // Configure API key authorization: apiKeyQuery
    ApiKeyAuth apiKeyQuery = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyQuery");
    apiKeyQuery.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyQuery.setApiKeyPrefix("Token");

    ScreenshotApi apiInstance = new ScreenshotApi(defaultClient);
    Integer id = 56; // Integer | screenshot ID
    String data = "image"; // String | data to remove. You can specify multiple of them (separated by a ,): *image* (image files), *url* (url requested), *metadata* (time added, time finished, post data, cookie and referer used for the screenshot), *all* (all data and files) 
    try {
      List<ScreenshotShort> result = apiInstance.deleteScreenshot(id, data);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ScreenshotApi#deleteScreenshot");
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
| **id** | **Integer**| screenshot ID | |
| **data** | **String**| data to remove. You can specify multiple of them (separated by a ,): *image* (image files), *url* (url requested), *metadata* (time added, time finished, post data, cookie and referer used for the screenshot), *all* (all data and files)  | [optional] [default to image] |

### Return type

[**List&lt;ScreenshotShort&gt;**](ScreenshotShort.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | list of screenshot information |  -  |
| **0** | Screenshot not found |  -  |

<a id="getHTML"></a>
# **getHTML**
> getHTML(id)

Get the HTML code

Retrieve the HTML code of the rendered page. This API call should be used when html&#x3D;1 was specified in the screenshot request. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ScreenshotApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.browshot.com/api/v1");
    
    // Configure API key authorization: apiKeyQuery
    ApiKeyAuth apiKeyQuery = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyQuery");
    apiKeyQuery.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyQuery.setApiKeyPrefix("Token");

    ScreenshotApi apiInstance = new ScreenshotApi(defaultClient);
    Integer id = 56; // Integer | screenshot ID
    try {
      apiInstance.getHTML(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling ScreenshotApi#getHTML");
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
| **id** | **Integer**| screenshot ID | |

### Return type

null (empty response body)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | HTML code |  -  |

<a id="getMultipleScreenshotsInfo"></a>
# **getMultipleScreenshotsInfo**
> List&lt;ScreenshotList&gt; getMultipleScreenshotsInfo(limit, status)

Get information about screenshots

Get information about the last 100 screenshots requested.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ScreenshotApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.browshot.com/api/v1");
    
    // Configure API key authorization: apiKeyQuery
    ApiKeyAuth apiKeyQuery = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyQuery");
    apiKeyQuery.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyQuery.setApiKeyPrefix("Token");

    ScreenshotApi apiInstance = new ScreenshotApi(defaultClient);
    Integer limit = 100; // Integer | maximum number of screenshots' information to return
    String status = "error"; // String | get list of screenshot in a given status (error, finished, in_process)
    try {
      List<ScreenshotList> result = apiInstance.getMultipleScreenshotsInfo(limit, status);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ScreenshotApi#getMultipleScreenshotsInfo");
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
| **limit** | **Integer**| maximum number of screenshots&#39; information to return | [optional] [default to 100] |
| **status** | **String**| get list of screenshot in a given status (error, finished, in_process) | [optional] [enum: error, finished, in_process] |

### Return type

[**List&lt;ScreenshotList&gt;**](ScreenshotList.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | list of screenshot information |  -  |
| **0** | Screenshot not found |  -  |

<a id="getScreenshotInfo"></a>
# **getScreenshotInfo**
> List&lt;Screenshot&gt; getScreenshotInfo(id, details)

Query screenshot status

Once a screenshot has been requested, its status must be checked until it is either \&quot;error\&quot; or \&quot;finished\&quot;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ScreenshotApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.browshot.com/api/v1");
    
    // Configure API key authorization: apiKeyQuery
    ApiKeyAuth apiKeyQuery = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyQuery");
    apiKeyQuery.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyQuery.setApiKeyPrefix("Token");

    ScreenshotApi apiInstance = new ScreenshotApi(defaultClient);
    Integer id = 56; // Integer | screenshot ID received from /api/v1/screenshot/create
    Integer details = 2; // Integer | level of details about the screenshot and the page
    try {
      List<Screenshot> result = apiInstance.getScreenshotInfo(id, details);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ScreenshotApi#getScreenshotInfo");
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
| **id** | **Integer**| screenshot ID received from /api/v1/screenshot/create | |
| **details** | **Integer**| level of details about the screenshot and the page | [optional] [default to 2] |

### Return type

[**List&lt;Screenshot&gt;**](Screenshot.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Screenshot found |  -  |
| **0** | Screenshot not found |  -  |

<a id="getThumbnail"></a>
# **getThumbnail**
> getThumbnail(id, width, height, scale, zoom, ratio, left, right, top, bottom, format, shot, quality)

Retrieve a thumbnail image

Unlike the other API calls, this API sends back the thumbnail as a PNG file, not JSON. The HTTP response code indicates whether the screenshot was successful (200), or incomplete (404) or failed (404). If the screenshot failed or is not finished, a default image \&quot;Not found\&quot; is sent.  You can crop your screenshots. The crop is done first, then the thumbnail. You can take a 1024x768 screenshot, crop it to 768x768, and get it scaled down to 300x300. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ScreenshotApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.browshot.com/api/v1");
    
    // Configure API key authorization: apiKeyQuery
    ApiKeyAuth apiKeyQuery = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyQuery");
    apiKeyQuery.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyQuery.setApiKeyPrefix("Token");

    ScreenshotApi apiInstance = new ScreenshotApi(defaultClient);
    Integer id = 56; // Integer | screenshot ID
    Integer width = 56; // Integer | width of the thumbnail
    Integer height = 56; // Integer | height of the thumbnail
    Double scale = 1.0D; // Double | scale of the thumbnail
    Integer zoom = 100; // Integer | zoom 1 to 100 percent
    String ratio = "fit"; // String | Use fit to keep the original page ration, and fill to get a thumbnail for the exact width and height.  specified. If you provide both width and height, you need to specify the ratio: fit to keep the original width/height ratio (the thumbnail might be smaller than the specified width and height), or fill to crop the image if necessary.
    Integer left = 0; // Integer | left edge of the area to be cropped
    Integer right = 0; // Integer | right edge of the area to be cropped
    Integer top = 0; // Integer | top edge of the area to be cropped
    Integer bottom = 56; // Integer | bottom edge of the area to be cropped
    String format = "png"; // String | image as PNG or JPEG
    Integer shot = 1; // Integer | get the second or third screenshot if multiple screenshots were requested
    Integer quality = 100; // Integer | JPEG quality factor (for JPEG thumbnails only)
    try {
      apiInstance.getThumbnail(id, width, height, scale, zoom, ratio, left, right, top, bottom, format, shot, quality);
    } catch (ApiException e) {
      System.err.println("Exception when calling ScreenshotApi#getThumbnail");
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
| **id** | **Integer**| screenshot ID | |
| **width** | **Integer**| width of the thumbnail | [optional] |
| **height** | **Integer**| height of the thumbnail | [optional] |
| **scale** | **Double**| scale of the thumbnail | [optional] [default to 1.0] |
| **zoom** | **Integer**| zoom 1 to 100 percent | [optional] [default to 100] |
| **ratio** | **String**| Use fit to keep the original page ration, and fill to get a thumbnail for the exact width and height.  specified. If you provide both width and height, you need to specify the ratio: fit to keep the original width/height ratio (the thumbnail might be smaller than the specified width and height), or fill to crop the image if necessary. | [optional] [default to fit] [enum: fit, fill] |
| **left** | **Integer**| left edge of the area to be cropped | [optional] [default to 0] |
| **right** | **Integer**| right edge of the area to be cropped | [optional] [default to 0] |
| **top** | **Integer**| top edge of the area to be cropped | [optional] [default to 0] |
| **bottom** | **Integer**| bottom edge of the area to be cropped | [optional] |
| **format** | **String**| image as PNG or JPEG | [optional] [default to png] [enum: png, jpeg] |
| **shot** | **Integer**| get the second or third screenshot if multiple screenshots were requested | [optional] [default to 1] |
| **quality** | **Integer**| JPEG quality factor (for JPEG thumbnails only) | [optional] [default to 100] |

### Return type

null (empty response body)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | thumbnail |  -  |
| **404** | Screenshot not found |  -  |

<a id="hostScreenshot"></a>
# **hostScreenshot**
> List&lt;ScreenshotHost&gt; hostScreenshot(id, hosting, width, height, scale, bucket, _file, headers)

Host thumbnails on your own S3 account or on Browshot.

You can host screenshots and thumbnails on your own S3 account or on Browshot.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ScreenshotApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.browshot.com/api/v1");
    
    // Configure API key authorization: apiKeyQuery
    ApiKeyAuth apiKeyQuery = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyQuery");
    apiKeyQuery.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyQuery.setApiKeyPrefix("Token");

    ScreenshotApi apiInstance = new ScreenshotApi(defaultClient);
    Integer id = 56; // Integer | screenshot ID
    String hosting = "s3"; // String | hosting option: s3 or browshot
    Integer width = 56; // Integer | width of the thumbnail
    Integer height = 56; // Integer | height of the thumbnail
    Double scale = 1.0D; // Double | scale of the thumbnail
    String bucket = "bucket_example"; // String | S3 bucket to upload the screenshot or thumbnail - required with hosting=s3
    String _file = "_file_example"; // String | file name to use - optional, used with hosting=s3
    String headers = "headers_example"; // String | HTTP headers to add to your S3 object - optional, used with hosting=s3
    try {
      List<ScreenshotHost> result = apiInstance.hostScreenshot(id, hosting, width, height, scale, bucket, _file, headers);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ScreenshotApi#hostScreenshot");
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
| **id** | **Integer**| screenshot ID | |
| **hosting** | **String**| hosting option: s3 or browshot | [enum: s3, browshot] |
| **width** | **Integer**| width of the thumbnail | [optional] |
| **height** | **Integer**| height of the thumbnail | [optional] |
| **scale** | **Double**| scale of the thumbnail | [optional] [default to 1.0] |
| **bucket** | **String**| S3 bucket to upload the screenshot or thumbnail - required with hosting&#x3D;s3 | [optional] |
| **_file** | **String**| file name to use - optional, used with hosting&#x3D;s3 | [optional] |
| **headers** | **String**| HTTP headers to add to your S3 object - optional, used with hosting&#x3D;s3 | [optional] |

### Return type

[**List&lt;ScreenshotHost&gt;**](ScreenshotHost.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | list of screenshot information |  -  |
| **0** | Screenshot not found |  -  |

<a id="searchScreenshot"></a>
# **searchScreenshot**
> List&lt;ScreenshotList&gt; searchScreenshot(url, limit, status)

Search for screenshots

Search for screenshots of a specific URL.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ScreenshotApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.browshot.com/api/v1");
    
    // Configure API key authorization: apiKeyQuery
    ApiKeyAuth apiKeyQuery = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyQuery");
    apiKeyQuery.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyQuery.setApiKeyPrefix("Token");

    ScreenshotApi apiInstance = new ScreenshotApi(defaultClient);
    String url = "url_example"; // String | look for a string matching the URL requested
    Integer limit = 50; // Integer | maximum number of screenshots' information to return
    String status = "error"; // String | get list of screenshot in a given status (error, finished, in_process)
    try {
      List<ScreenshotList> result = apiInstance.searchScreenshot(url, limit, status);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ScreenshotApi#searchScreenshot");
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
| **url** | **String**| look for a string matching the URL requested | |
| **limit** | **Integer**| maximum number of screenshots&#39; information to return | [optional] [default to 50] |
| **status** | **String**| get list of screenshot in a given status (error, finished, in_process) | [optional] [enum: error, finished, in_process] |

### Return type

[**List&lt;ScreenshotList&gt;**](ScreenshotList.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | list of screenshot information |  -  |
| **0** | Screenshot not found |  -  |

<a id="shareScreenshot"></a>
# **shareScreenshot**
> List&lt;ScreenshotHost&gt; shareScreenshot(id, note)

Share a screenshot

You can make your screenshots public, add notes, and share it with your friends and colleagues. Only screenshots which are successfully completed can be shared.n the thumbnail. You can take a 1024x768 screenshot, crop it to 768x768, and get it scaled down to 300x300. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ScreenshotApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.browshot.com/api/v1");
    
    // Configure API key authorization: apiKeyQuery
    ApiKeyAuth apiKeyQuery = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyQuery");
    apiKeyQuery.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyQuery.setApiKeyPrefix("Token");

    ScreenshotApi apiInstance = new ScreenshotApi(defaultClient);
    Integer id = 56; // Integer | screenshot ID
    String note = "note_example"; // String | note to add on the sharing page
    try {
      List<ScreenshotHost> result = apiInstance.shareScreenshot(id, note);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ScreenshotApi#shareScreenshot");
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
| **id** | **Integer**| screenshot ID | |
| **note** | **String**| note to add on the sharing page | [optional] |

### Return type

[**List&lt;ScreenshotHost&gt;**](ScreenshotHost.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | list of screenshot information |  -  |
| **0** | Screenshot not found |  -  |

