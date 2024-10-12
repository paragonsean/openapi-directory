# PicoLoadmanagementGroupApi

All URIs are relative to *https://smart-me.com:443*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiPicoLoadmanagementgroupGet**](PicoLoadmanagementGroupApi.md#apiPicoLoadmanagementgroupGet) | **GET** /api/pico/loadmanagementgroup | GET: api/pico/loadmanagementgroup                            Returns all available load management groups |
| [**picoLoadmanagementGroupGet**](PicoLoadmanagementGroupApi.md#picoLoadmanagementGroupGet) | **GET** /api/pico/loadmanagementgroup/{id} | GET: api/pico/loadmanagementgroup                            Returns a pico load management group by it&#39;s id |


<a id="apiPicoLoadmanagementgroupGet"></a>
# **apiPicoLoadmanagementgroupGet**
> List&lt;PicoLoadmanagementGroupDto&gt; apiPicoLoadmanagementgroupGet()

GET: api/pico/loadmanagementgroup                            Returns all available load management groups

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PicoLoadmanagementGroupApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://smart-me.com:443");

    PicoLoadmanagementGroupApi apiInstance = new PicoLoadmanagementGroupApi(defaultClient);
    try {
      List<PicoLoadmanagementGroupDto> result = apiInstance.apiPicoLoadmanagementgroupGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PicoLoadmanagementGroupApi#apiPicoLoadmanagementgroupGet");
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

[**List&lt;PicoLoadmanagementGroupDto&gt;**](PicoLoadmanagementGroupDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="picoLoadmanagementGroupGet"></a>
# **picoLoadmanagementGroupGet**
> PicoLoadmanagementGroupDto picoLoadmanagementGroupGet(id)

GET: api/pico/loadmanagementgroup                            Returns a pico load management group by it&#39;s id

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PicoLoadmanagementGroupApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://smart-me.com:443");

    PicoLoadmanagementGroupApi apiInstance = new PicoLoadmanagementGroupApi(defaultClient);
    String id = "id_example"; // String | 
    try {
      PicoLoadmanagementGroupDto result = apiInstance.picoLoadmanagementGroupGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PicoLoadmanagementGroupApi#picoLoadmanagementGroupGet");
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
| **id** | **String**|  | |

### Return type

[**PicoLoadmanagementGroupDto**](PicoLoadmanagementGroupDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

