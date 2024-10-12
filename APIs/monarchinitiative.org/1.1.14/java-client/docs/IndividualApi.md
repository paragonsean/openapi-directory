# IndividualApi

All URIs are relative to */api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getIndividual**](IndividualApi.md#getIndividual) | **GET** /individual/{id} | Returns list of matches |
| [**getPedigree**](IndividualApi.md#getPedigree) | **GET** /individual/pedigree/{id} | Returns list of matches |


<a id="getIndividual"></a>
# **getIndividual**
> List&lt;Association&gt; getIndividual(id)

Returns list of matches

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IndividualApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    IndividualApi apiInstance = new IndividualApi(defaultClient);
    String id = "id_example"; // String | 
    try {
      List<Association> result = apiInstance.getIndividual(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IndividualApi#getIndividual");
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

[**List&lt;Association&gt;**](Association.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="getPedigree"></a>
# **getPedigree**
> List&lt;Association&gt; getPedigree(id)

Returns list of matches

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IndividualApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    IndividualApi apiInstance = new IndividualApi(defaultClient);
    String id = "id_example"; // String | 
    try {
      List<Association> result = apiInstance.getPedigree(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IndividualApi#getPedigree");
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

[**List&lt;Association&gt;**](Association.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

