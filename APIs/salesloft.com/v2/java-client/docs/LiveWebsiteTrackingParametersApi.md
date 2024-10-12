# LiveWebsiteTrackingParametersApi

All URIs are relative to *https://api.salesloft.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**v2LiveWebsiteTrackingParametersJsonPost**](LiveWebsiteTrackingParametersApi.md#v2LiveWebsiteTrackingParametersJsonPost) | **POST** /v2/live_website_tracking_parameters.json | Create an Live Website Tracking Parameter |


<a id="v2LiveWebsiteTrackingParametersJsonPost"></a>
# **v2LiveWebsiteTrackingParametersJsonPost**
> LiveWebsiteTrackingParameter v2LiveWebsiteTrackingParametersJsonPost(personId)

Create an Live Website Tracking Parameter

Creates a Live Website Tracking parameter to identify a person 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LiveWebsiteTrackingParametersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.salesloft.com");

    LiveWebsiteTrackingParametersApi apiInstance = new LiveWebsiteTrackingParametersApi(defaultClient);
    Integer personId = 56; // Integer | The person to create the LiveWebsiteTrackingParameter for
    try {
      LiveWebsiteTrackingParameter result = apiInstance.v2LiveWebsiteTrackingParametersJsonPost(personId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LiveWebsiteTrackingParametersApi#v2LiveWebsiteTrackingParametersJsonPost");
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
| **personId** | **Integer**| The person to create the LiveWebsiteTrackingParameter for | |

### Return type

[**LiveWebsiteTrackingParameter**](LiveWebsiteTrackingParameter.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

