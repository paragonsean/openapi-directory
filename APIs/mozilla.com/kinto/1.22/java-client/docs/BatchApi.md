# BatchApi

All URIs are relative to *https://firefox.settings.services.mozilla.com/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**batch**](BatchApi.md#batch) | **POST** /batch |  |


<a id="batch"></a>
# **batch**
> BatchResponseBodySchema batch(batchPayloadSchema)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BatchApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://firefox.settings.services.mozilla.com/v1");

    BatchApi apiInstance = new BatchApi(defaultClient);
    BatchPayloadSchema batchPayloadSchema = new BatchPayloadSchema(); // BatchPayloadSchema | 
    try {
      BatchResponseBodySchema result = apiInstance.batch(batchPayloadSchema);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BatchApi#batch");
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
| **batchPayloadSchema** | [**BatchPayloadSchema**](BatchPayloadSchema.md)|  | |

### Return type

[**BatchResponseBodySchema**](BatchResponseBodySchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Return a list of operation responses. |  -  |
| **400** | The request was badly formatted. |  -  |
| **0** | an unknown error occurred. |  -  |

