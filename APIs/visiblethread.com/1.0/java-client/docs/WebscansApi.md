# WebscansApi

All URIs are relative to *https://api.visiblethread.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getScanById**](WebscansApi.md#getScanById) | **GET** /webscans/{scanId} | Get data from a previously run scan |
| [**getScanUrlById**](WebscansApi.md#getScanUrlById) | **GET** /webscans/{scanId}/webUrls/{urlId} | Gets data for a particular scan/webUrl |
| [**runScan**](WebscansApi.md#runScan) | **POST** /webscans | Run a new scan |
| [**webscansGet**](WebscansApi.md#webscansGet) | **GET** /webscans | Get your list of scans |


<a id="getScanById"></a>
# **getScanById**
> ScanResponseDetailed getScanById(scanId)

Get data from a previously run scan

Get data from a previously run scan, identified by **scanId**

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WebscansApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.visiblethread.com/api/v1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    WebscansApi apiInstance = new WebscansApi(defaultClient);
    Long scanId = 56L; // Long | Id of scan to fetch
    try {
      ScanResponseDetailed result = apiInstance.getScanById(scanId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WebscansApi#getScanById");
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
| **scanId** | **Long**| Id of scan to fetch | |

### Return type

[**ScanResponseDetailed**](ScanResponseDetailed.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | scan response |  -  |
| **404** | webscan not found |  -  |
| **503** | the web analysis has not yet completed, try again later |  -  |

<a id="getScanUrlById"></a>
# **getScanUrlById**
> WebUrlDetail getScanUrlById(scanId, urlId)

Gets data for a particular scan/webUrl

Get detailed results for a scan/url (readability, long sentence and passive language instances), identified by **scanId** &amp; **urlId**

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WebscansApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.visiblethread.com/api/v1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    WebscansApi apiInstance = new WebscansApi(defaultClient);
    Long scanId = 56L; // Long | Id of scan
    Long urlId = 56L; // Long | Id of url to fetch
    try {
      WebUrlDetail result = apiInstance.getScanUrlById(scanId, urlId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WebscansApi#getScanUrlById");
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
| **scanId** | **Long**| Id of scan | |
| **urlId** | **Long**| Id of url to fetch | |

### Return type

[**WebUrlDetail**](WebUrlDetail.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | scan response |  -  |
| **404** | scan url not found |  -  |

<a id="runScan"></a>
# **runScan**
> NewScanResponse runScan(body)

Run a new scan

The scan runs in the background but returns immediately with a JSON response containing an \&quot;id\&quot; that represents your scan.         You can use this id in other requests to retrieve your scan result.   Also, an \&quot;id\&quot; is returned for each url which can be used to retrieve detailed results for individual scan urls. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WebscansApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.visiblethread.com/api/v1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    WebscansApi apiInstance = new WebscansApi(defaultClient);
    NewScan body = new NewScan(); // NewScan | Scan title and webUrls to analyze
    try {
      NewScanResponse result = apiInstance.runScan(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WebscansApi#runScan");
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
| **body** | [**NewScan**](NewScan.md)| Scan title and webUrls to analyze | |

### Return type

[**NewScanResponse**](NewScanResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |
| **405** | Invalid input |  -  |

<a id="webscansGet"></a>
# **webscansGet**
> List&lt;ScanResponseSummary&gt; webscansGet()

Get your list of scans

Get your list of scans

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WebscansApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.visiblethread.com/api/v1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    WebscansApi apiInstance = new WebscansApi(defaultClient);
    try {
      List<ScanResponseSummary> result = apiInstance.webscansGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WebscansApi#webscansGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**List&lt;ScanResponseSummary&gt;**](ScanResponseSummary.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

