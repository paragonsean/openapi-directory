# ProfileApi

All URIs are relative to *https://dev.ndhm.gov.in/gateway*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**v05PatientsProfileSharePost**](ProfileApi.md#v05PatientsProfileSharePost) | **POST** /v0.5/patients/profile/share | Share patient profile details |


<a id="v05PatientsProfileSharePost"></a>
# **v05PatientsProfileSharePost**
> v05PatientsProfileSharePost(authorization, X_HIP_ID, shareProfileRequest)

Share patient profile details

Request for sharing patient&#39;s profile details to HIP 

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
    defaultClient.setBasePath("https://dev.ndhm.gov.in/gateway");

    ProfileApi apiInstance = new ProfileApi(defaultClient);
    String authorization = "authorization_example"; // String | Access token which was issued after successful login with gateway auth server, which will be sent by gateway to authenticate itself with API bridge.
    String X_HIP_ID = "X_HIP_ID_example"; // String | Identifier of the health information provider to which the request was intended.
    ShareProfileRequest shareProfileRequest = new ShareProfileRequest(); // ShareProfileRequest | 
    try {
      apiInstance.v05PatientsProfileSharePost(authorization, X_HIP_ID, shareProfileRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProfileApi#v05PatientsProfileSharePost");
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
| **authorization** | **String**| Access token which was issued after successful login with gateway auth server, which will be sent by gateway to authenticate itself with API bridge. | |
| **X_HIP_ID** | **String**| Identifier of the health information provider to which the request was intended. | |
| **shareProfileRequest** | [**ShareProfileRequest**](ShareProfileRequest.md)|  | |

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
| **400** | **Causes:**   * Invalid Request  |  -  |
| **401** | **Causes:**   * Unauthorized request  |  -  |
| **500** | **Causes:**   * Downstream system(s) is down.   * Unhandled exceptions.  |  -  |

