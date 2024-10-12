# ProfileApi

All URIs are relative to *https://dev.ndhm.gov.in/gateway*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**v05PatientsProfileOnSharePost**](ProfileApi.md#v05PatientsProfileOnSharePost) | **POST** /v0.5/patients/profile/on-share | Response to patient&#39;s share profile request |
| [**v05PatientsProfileSharePost**](ProfileApi.md#v05PatientsProfileSharePost) | **POST** /v0.5/patients/profile/share | Share patient profile details |


<a id="v05PatientsProfileOnSharePost"></a>
# **v05PatientsProfileOnSharePost**
> v05PatientsProfileOnSharePost(authorization, X_CM_ID, shareProfileResult)

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
    defaultClient.setBasePath("https://dev.ndhm.gov.in/gateway");

    ProfileApi apiInstance = new ProfileApi(defaultClient);
    String authorization = "authorization_example"; // String | Access token which was issued after successful login with gateway auth server.
    String X_CM_ID = "X_CM_ID_example"; // String | Suffix of the consent manager to which the request was intended.
    ShareProfileResult shareProfileResult = new ShareProfileResult(); // ShareProfileResult | 
    try {
      apiInstance.v05PatientsProfileOnSharePost(authorization, X_CM_ID, shareProfileResult);
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
| **X_CM_ID** | **String**| Suffix of the consent manager to which the request was intended. | |
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
    String authorization = "authorization_example"; // String | Access token which was issued after successful login with gateway auth server.
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
| **authorization** | **String**| Access token which was issued after successful login with gateway auth server. | |
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

