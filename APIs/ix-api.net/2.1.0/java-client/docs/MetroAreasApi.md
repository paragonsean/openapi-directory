# MetroAreasApi

All URIs are relative to */api/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**metroAreasList**](MetroAreasApi.md#metroAreasList) | **GET** /metro-areas |  |
| [**metroAreasRead**](MetroAreasApi.md#metroAreasRead) | **GET** /metro-areas/{id} |  |


<a id="metroAreasList"></a>
# **metroAreasList**
> List&lt;MetroArea&gt; metroAreasList(id)



List all MetroAreas

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MetroAreasApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");
    
    // Configure HTTP bearer authorization: Bearer
    HttpBearerAuth Bearer = (HttpBearerAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setBearerToken("BEARER TOKEN");

    MetroAreasApi apiInstance = new MetroAreasApi(defaultClient);
    List<String> id = Arrays.asList(); // List<String> | Filter by id
    try {
      List<MetroArea> result = apiInstance.metroAreasList(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MetroAreasApi#metroAreasList");
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
| **id** | [**List&lt;String&gt;**](String.md)| Filter by id | [optional] |

### Return type

[**List&lt;MetroArea&gt;**](MetroArea.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of: MetroArea |  -  |
| **400** | ValidationError |  -  |
| **401** | Authentication |  -  |
| **403** | PermissionDenied |  -  |

<a id="metroAreasRead"></a>
# **metroAreasRead**
> List&lt;MetroArea&gt; metroAreasRead(id)



Get a single MetroArea

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MetroAreasApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");
    
    // Configure HTTP bearer authorization: Bearer
    HttpBearerAuth Bearer = (HttpBearerAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setBearerToken("BEARER TOKEN");

    MetroAreasApi apiInstance = new MetroAreasApi(defaultClient);
    String id = "id_example"; // String | Get by id
    try {
      List<MetroArea> result = apiInstance.metroAreasRead(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MetroAreasApi#metroAreasRead");
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
| **id** | **String**| Get by id | |

### Return type

[**List&lt;MetroArea&gt;**](MetroArea.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of: MetroArea |  -  |
| **401** | Authentication |  -  |
| **403** | PermissionDenied |  -  |
| **404** | NotFound |  -  |

