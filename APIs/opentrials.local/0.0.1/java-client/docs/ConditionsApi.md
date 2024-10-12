# ConditionsApi

All URIs are relative to *http://opentrials.local/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getCondition**](ConditionsApi.md#getCondition) | **GET** /conditions/{id} |  |


<a id="getCondition"></a>
# **getCondition**
> Condition getCondition(id)



Returns condition details

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConditionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://opentrials.local/v1");

    ConditionsApi apiInstance = new ConditionsApi(defaultClient);
    String id = "id_example"; // String | ID of the condition
    try {
      Condition result = apiInstance.getCondition(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConditionsApi#getCondition");
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
| **id** | **String**| ID of the condition | |

### Return type

[**Condition**](Condition.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **404** | Condition not found |  -  |
| **0** | Error |  -  |

