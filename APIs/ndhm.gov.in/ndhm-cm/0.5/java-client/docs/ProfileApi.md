# ProfileApi

All URIs are relative to *https://dev.ndhm.gov.in/cm*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**v05PatientsProfileOnSharePost**](ProfileApi.md#v05PatientsProfileOnSharePost) | **POST** /v0.5/patients/profile/on-share | Response to patient&#39;s share profile request |


<a id="v05PatientsProfileOnSharePost"></a>
# **v05PatientsProfileOnSharePost**
> v05PatientsProfileOnSharePost(authorization, shareProfileResult)

Response to patient&#39;s share profile request

Result of patient share profile request at HIP end. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProfileApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dev.ndhm.gov.in/cm");

    ProfileApi apiInstance = new ProfileApi(defaultClient);
    String authorization = "authorization_example"; // String | Access token which was issued after successful login with gateway auth server.
    ShareProfileResult shareProfileResult = new ShareProfileResult(); // ShareProfileResult | 
    try {
      apiInstance.v05PatientsProfileOnSharePost(authorization, shareProfileResult);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProfileApi#v05PatientsProfileOnSharePost");
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
| **authorization** | **String**| Access token which was issued after successful login with gateway auth server. | |
| **shareProfileResult** | [**ShareProfileResult**](ShareProfileResult.md)|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Request accepted |  -  |
| **400** | **Causes:**   * Format mismatch of any of attributes.  |  -  |
| **401** | **Causes:**   * Unauthorized request  |  -  |
| **500** | **Causes:**   * Downstream system(s) is down.   * Unhandled exceptions.  |  -  |

