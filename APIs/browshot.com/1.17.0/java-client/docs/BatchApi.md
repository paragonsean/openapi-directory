# BatchApi

All URIs are relative to *https://api.browshot.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createBatch**](BatchApi.md#createBatch) | **POST** /batch/ceate | Requests thousands of screenshtos at once |
| [**getBatchInfo**](BatchApi.md#getBatchInfo) | **GET** /batch/info | Get the batch status |


<a id="createBatch"></a>
# **createBatch**
> List&lt;Batch&gt; createBatch(instanceId, hosting, hostingHeight, hostingWidth, hostingScale, hostingBucket, hostingFile, hostingHeaders, _file, size, name, width, height, delay, flashDelay, screenWidth, screenHeight, priority, referer, postData, cookie, script, details, html, maxWait, headers, format)

Requests thousands of screenshtos at once

Get hundreds or thousands of screenshots from a text file. You can use this API call or the dashboard. Unlike the other API calls, you must issue a POST request with the Content-Type \&quot;multipart/form-data\&quot; in order to upload the text file. The text file must contain the list of URLs to request, 1 URL per line. Failed screenshots will be tried up to 3 times before giving up. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BatchApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.browshot.com/api/v1");
    
    // Configure API key authorization: apiKeyQuery
    ApiKeyAuth apiKeyQuery = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyQuery");
    apiKeyQuery.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyQuery.setApiKeyPrefix("Token");

    BatchApi apiInstance = new BatchApi(defaultClient);
    Integer instanceId = 56; // Integer | instance ID to use
    String hosting = "s3"; // String | hosting option - s3 or browshot
    Integer hostingHeight = 56; // Integer | maximum height of the thumbnail to host
    Integer hostingWidth = 56; // Integer | maximum height of the thumbnail to host
    Float hostingScale = 1.0F; // Float | scale of the thumbnail to host
    String hostingBucket = "hostingBucket_example"; // String | S3 bucket to upload the screenshot or thumbnail (required for S3)
    String hostingFile = "hostingFile_example"; // String | file name to use (for S3 only)
    String hostingHeaders = "hostingHeaders_example"; // String | list of headers to add to the S3 object (for S3 only)
    File _file = new File("/path/to/file"); // File | text file to use
    String size = "screen"; // String | screenshots size - \\\"screen\\\" (default) or \\\"page\\\"
    String name = "name_example"; // String | name of the batch
    Integer width = 1024; // Integer | thumbnail width.
    Integer height = 56; // Integer | thumbnail height
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
    String format = "png"; // String | image as PNG or JPEG
    try {
      List<Batch> result = apiInstance.createBatch(instanceId, hosting, hostingHeight, hostingWidth, hostingScale, hostingBucket, hostingFile, hostingHeaders, _file, size, name, width, height, delay, flashDelay, screenWidth, screenHeight, priority, referer, postData, cookie, script, details, html, maxWait, headers, format);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BatchApi#createBatch");
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
| **instanceId** | **Integer**| instance ID to use | |
| **hosting** | **String**| hosting option - s3 or browshot | [optional] [enum: s3] |
| **hostingHeight** | **Integer**| maximum height of the thumbnail to host | [optional] |
| **hostingWidth** | **Integer**| maximum height of the thumbnail to host | [optional] |
| **hostingScale** | **Float**| scale of the thumbnail to host | [optional] [default to 1.0] |
| **hostingBucket** | **String**| S3 bucket to upload the screenshot or thumbnail (required for S3) | [optional] |
| **hostingFile** | **String**| file name to use (for S3 only) | [optional] |
| **hostingHeaders** | **String**| list of headers to add to the S3 object (for S3 only) | [optional] |
| **_file** | **File**| text file to use | [optional] |
| **size** | **String**| screenshots size - \\\&quot;screen\\\&quot; (default) or \\\&quot;page\\\&quot; | [optional] [default to screen] [enum: screen, page] |
| **name** | **String**| name of the batch | [optional] |
| **width** | **Integer**| thumbnail width. | [optional] [default to 1024] |
| **height** | **Integer**| thumbnail height | [optional] |
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
| **format** | **String**| image as PNG or JPEG | [optional] [default to png] [enum: png, jpeg] |

### Return type

[**List&lt;Batch&gt;**](Batch.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | batch information |  -  |
| **0** | Batch not created |  -  |

<a id="getBatchInfo"></a>
# **getBatchInfo**
> Batch getBatchInfo(id)

Get the batch status

Get the status of a batch requested through the API or through the dashboard. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BatchApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.browshot.com/api/v1");
    
    // Configure API key authorization: apiKeyQuery
    ApiKeyAuth apiKeyQuery = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyQuery");
    apiKeyQuery.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyQuery.setApiKeyPrefix("Token");

    BatchApi apiInstance = new BatchApi(defaultClient);
    Integer id = 56; // Integer | batch ID
    try {
      Batch result = apiInstance.getBatchInfo(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BatchApi#getBatchInfo");
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
| **id** | **Integer**| batch ID | |

### Return type

[**Batch**](Batch.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | batch information |  -  |
| **0** | Batch not found |  -  |

