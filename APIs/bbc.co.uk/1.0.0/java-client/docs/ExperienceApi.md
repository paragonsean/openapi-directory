# ExperienceApi

All URIs are relative to *https://rms.api.bbc.co.uk*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getExperienceHomepage**](ExperienceApi.md#getExperienceHomepage) | **GET** /experience/homepage | Homepage Experience |


<a id="getExperienceHomepage"></a>
# **getExperienceHomepage**
> ExperienceResponse getExperienceHomepage(xAPIKey)

Homepage Experience

Homepage Experience 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExperienceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rms.api.bbc.co.uk");

    ExperienceApi apiInstance = new ExperienceApi(defaultClient);
    String xAPIKey = "xAPIKey_example"; // String | API_KEY
    try {
      ExperienceResponse result = apiInstance.getExperienceHomepage(xAPIKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExperienceApi#getExperienceHomepage");
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
| **xAPIKey** | **String**| API_KEY | |

### Return type

[**ExperienceResponse**](ExperienceResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Unexpected error |  -  |

