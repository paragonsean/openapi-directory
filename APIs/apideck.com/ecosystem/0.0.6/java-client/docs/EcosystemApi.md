# EcosystemApi

All URIs are relative to *https://api.apideck.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**ecosystemsOne**](EcosystemApi.md#ecosystemsOne) | **GET** /ecosystems/{ecosystem_id} | Get ecosystem |


<a id="ecosystemsOne"></a>
# **ecosystemsOne**
> GetEcosystemResponse ecosystemsOne(ecosystemId)

Get ecosystem

Get ecosystem

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EcosystemApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.apideck.com");

    EcosystemApi apiInstance = new EcosystemApi(defaultClient);
    String ecosystemId = "ecosystemId_example"; // String | 
    try {
      GetEcosystemResponse result = apiInstance.ecosystemsOne(ecosystemId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EcosystemApi#ecosystemsOne");
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
| **ecosystemId** | **String**|  | |

### Return type

[**GetEcosystemResponse**](GetEcosystemResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Ecosystems |  -  |

