# SourceMapsApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**sourceMapsCreateOrUpdate**](SourceMapsApi.md#sourceMapsCreateOrUpdate) | **POST** /v3/sourcemaps/{logId} | Create or update a translation between a minified JavaScript path to the minified JavaScript and source map files. |


<a id="sourceMapsCreateOrUpdate"></a>
# **sourceMapsCreateOrUpdate**
> sourceMapsCreateOrUpdate(logId, minifiedJavaScript, path, sourceMap)

Create or update a translation between a minified JavaScript path to the minified JavaScript and source map files.

Required permission: &#x60;sourcemaps_write&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SourceMapsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    SourceMapsApi apiInstance = new SourceMapsApi(defaultClient);
    String logId = "logId_example"; // String | The ID of the log which should contain the minified JavaScript and source map.
    File minifiedJavaScript = new File("/path/to/file"); // File | The minified JavaScript file. Only files with an extension of .js and content type of text/javascript will be accepted.
    URI path = new URI(); // URI | An URL to the online minified JavaScript file. The URL can be absolute or relative but will always be converted to a relative path (no protocol, domain, and query parameters).  elmah.io uses this path to lookup any lines in a JS stack trace that will need de-minification.
    File sourceMap = new File("/path/to/file"); // File | The source map file. Only files with an extension of .map and content type of application/json will be accepted.
    try {
      apiInstance.sourceMapsCreateOrUpdate(logId, minifiedJavaScript, path, sourceMap);
    } catch (ApiException e) {
      System.err.println("Exception when calling SourceMapsApi#sourceMapsCreateOrUpdate");
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
| **logId** | **String**| The ID of the log which should contain the minified JavaScript and source map. | |
| **minifiedJavaScript** | **File**| The minified JavaScript file. Only files with an extension of .js and content type of text/javascript will be accepted. | |
| **path** | **URI**| An URL to the online minified JavaScript file. The URL can be absolute or relative but will always be converted to a relative path (no protocol, domain, and query parameters).  elmah.io uses this path to lookup any lines in a JS stack trace that will need de-minification. | |
| **sourceMap** | **File**| The source map file. Only files with an extension of .map and content type of application/json will be accepted. | |

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Source map was successfully created. |  -  |
| **400** | Something wrong with the query parameters or form. |  -  |
| **401** | API key not valid or no access to resource. |  -  |
| **402** | Tried to call the logs API but the trial expired. |  -  |
| **404** | Log not found. |  -  |
| **429** | A maximum of 500 requests per minute and 3600 requests per hour are permitted |  -  |

