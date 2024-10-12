# WindowsHostingsApi

All URIs are relative to */v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getWindowsHosting**](WindowsHostingsApi.md#getWindowsHosting) | **GET** /windowshostings/{domainName} | Windows hosting detail |
| [**getWindowsHostings**](WindowsHostingsApi.md#getWindowsHostings) | **GET** /windowshostings | Overview of windows hostings |


<a id="getWindowsHosting"></a>
# **getWindowsHosting**
> WindowsHostingDetail getWindowsHosting(domainName, domainName2)

Windows hosting detail

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WindowsHostingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/v2");

    WindowsHostingsApi apiInstance = new WindowsHostingsApi(defaultClient);
    String domainName = "domainName_example"; // String | The Windows hosting domain name.
    String domainName2 = "domainName_example"; // String | Automatically added
    try {
      WindowsHostingDetail result = apiInstance.getWindowsHosting(domainName, domainName2);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WindowsHostingsApi#getWindowsHosting");
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
| **domainName** | **String**| The Windows hosting domain name. | |
| **domainName2** | **String**| Automatically added | |

### Return type

[**WindowsHostingDetail**](WindowsHostingDetail.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="getWindowsHostings"></a>
# **getWindowsHostings**
> List&lt;WindowsHosting&gt; getWindowsHostings(skip, take)

Overview of windows hostings

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WindowsHostingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/v2");

    WindowsHostingsApi apiInstance = new WindowsHostingsApi(defaultClient);
    Integer skip = 56; // Integer | The number of items to skip in the resultset.
    Integer take = 56; // Integer | The number of items to return in the resultset. The returned count can be equal or less than this number.
    try {
      List<WindowsHosting> result = apiInstance.getWindowsHostings(skip, take);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WindowsHostingsApi#getWindowsHostings");
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
| **skip** | **Integer**| The number of items to skip in the resultset. | [optional] |
| **take** | **Integer**| The number of items to return in the resultset. The returned count can be equal or less than this number. | [optional] |

### Return type

[**List&lt;WindowsHosting&gt;**](WindowsHosting.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  * X-Paging-Skipped - The number of results that have been skipped. <br>  * X-Paging-Take - The number of items in the current take. The number might differ from the requested take. It represents the actual number of items returned in the response. <br>  * X-Paging-TotalResults - The total number of results regardless of paging. <br>  |

