# DefaultApi

All URIs are relative to *https://api-rv.herokuapp.com/rv/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**resourcesGet**](DefaultApi.md#resourcesGet) | **GET** /resources | Fetch all verses sung for a specific category of god, person, or object |


<a id="resourcesGet"></a>
# **resourcesGet**
> resourcesGet(sungforcategory)

Fetch all verses sung for a specific category of god, person, or object

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api-rv.herokuapp.com/rv/v1");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String sungforcategory = "abstract"; // String | Click to select one of these available values.
    try {
      apiInstance.resourcesGet(sungforcategory);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#resourcesGet");
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
| **sungforcategory** | **String**| Click to select one of these available values. | [enum: abstract, animal, demon male, divine female, divine human, divine male, human couple, human female, human male, human unborn, object, plant] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Verses fetched. |  -  |
| **404** | No verses found. |  -  |

