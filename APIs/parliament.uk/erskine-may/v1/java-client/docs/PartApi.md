# PartApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiPartGet**](PartApi.md#apiPartGet) | **GET** /api/Part | Returns a list of all parts. |
| [**apiPartPartNumberGet**](PartApi.md#apiPartPartNumberGet) | **GET** /api/Part/{partNumber} | Returns a part by part number. |


<a id="apiPartGet"></a>
# **apiPartGet**
> List&lt;ErskineMayPart&gt; apiPartGet()

Returns a list of all parts.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PartApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    PartApi apiInstance = new PartApi(defaultClient);
    try {
      List<ErskineMayPart> result = apiInstance.apiPartGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PartApi#apiPartGet");
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

[**List&lt;ErskineMayPart&gt;**](ErskineMayPart.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="apiPartPartNumberGet"></a>
# **apiPartPartNumberGet**
> ErskineMayPart apiPartPartNumberGet(partNumber)

Returns a part by part number.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PartApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    PartApi apiInstance = new PartApi(defaultClient);
    Integer partNumber = 56; // Integer | Part by part number
    try {
      ErskineMayPart result = apiInstance.apiPartPartNumberGet(partNumber);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PartApi#apiPartPartNumberGet");
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
| **partNumber** | **Integer**| Part by part number | |

### Return type

[**ErskineMayPart**](ErskineMayPart.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad Request |  -  |
| **404** | Not Found |  -  |

