# InfoApi

All URIs are relative to *http://optimade.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getEntryInfoInfoEntryGet**](InfoApi.md#getEntryInfoInfoEntryGet) | **GET** /info/{entry} | Get Entry Info |
| [**getInfoInfoGet**](InfoApi.md#getInfoInfoGet) | **GET** /info | Get Info |


<a id="getEntryInfoInfoEntryGet"></a>
# **getEntryInfoInfoEntryGet**
> EntryInfoResponse getEntryInfoInfoEntryGet(entry)

Get Entry Info

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InfoApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://optimade.local");

    InfoApi apiInstance = new InfoApi(defaultClient);
    String entry = "entry_example"; // String | 
    try {
      EntryInfoResponse result = apiInstance.getEntryInfoInfoEntryGet(entry);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InfoApi#getEntryInfoInfoEntryGet");
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
| **entry** | **String**|  | |

### Return type

[**EntryInfoResponse**](EntryInfoResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **400** | Bad Request |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **422** | Unprocessable Entity |  -  |
| **500** | Internal Server Error |  -  |
| **501** | Not Implemented |  -  |
| **553** | Version Not Supported |  -  |

<a id="getInfoInfoGet"></a>
# **getInfoInfoGet**
> InfoResponse getInfoInfoGet()

Get Info

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InfoApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://optimade.local");

    InfoApi apiInstance = new InfoApi(defaultClient);
    try {
      InfoResponse result = apiInstance.getInfoInfoGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InfoApi#getInfoInfoGet");
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

[**InfoResponse**](InfoResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **400** | Bad Request |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **422** | Unprocessable Entity |  -  |
| **500** | Internal Server Error |  -  |
| **501** | Not Implemented |  -  |
| **553** | Version Not Supported |  -  |

