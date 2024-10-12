# IdentifierMapperApi

All URIs are relative to */api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getIdentifierMapper**](IdentifierMapperApi.md#getIdentifierMapper) | **GET** /identifier/mapper/{source}/{target}/ | TODO maps a list of identifiers from a source to a target |


<a id="getIdentifierMapper"></a>
# **getIdentifierMapper**
> List&lt;Association&gt; getIdentifierMapper(source, target)

TODO maps a list of identifiers from a source to a target

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IdentifierMapperApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    IdentifierMapperApi apiInstance = new IdentifierMapperApi(defaultClient);
    String source = "source_example"; // String | 
    String target = "target_example"; // String | 
    try {
      List<Association> result = apiInstance.getIdentifierMapper(source, target);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IdentifierMapperApi#getIdentifierMapper");
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
| **source** | **String**|  | |
| **target** | **String**|  | |

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

