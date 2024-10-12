# InterventionsApi

All URIs are relative to *http://opentrials.local/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getIntervention**](InterventionsApi.md#getIntervention) | **GET** /interventions/{id} |  |


<a id="getIntervention"></a>
# **getIntervention**
> Intervention getIntervention(id)



Returns intervention details

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InterventionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://opentrials.local/v1");

    InterventionsApi apiInstance = new InterventionsApi(defaultClient);
    String id = "id_example"; // String | ID of the intervention
    try {
      Intervention result = apiInstance.getIntervention(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InterventionsApi#getIntervention");
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
| **id** | **String**| ID of the intervention | |

### Return type

[**Intervention**](Intervention.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **404** | Intervention not found |  -  |
| **0** | Error |  -  |

