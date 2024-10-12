# DiscoveryApi

All URIs are relative to *https://dev.ndhm.gov.in/cm*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**v05CareContextsOnDiscoverPost**](DiscoveryApi.md#v05CareContextsOnDiscoverPost) | **POST** /v0.5/care-contexts/on-discover | Response to patient&#39;s account discovery request |


<a id="v05CareContextsOnDiscoverPost"></a>
# **v05CareContextsOnDiscoverPost**
> v05CareContextsOnDiscoverPost(authorization, patientDiscoveryResult)

Response to patient&#39;s account discovery request

Result of patient care-context discovery request at HIP end. If a matching patient found with zero or more care contexts associated, it is specified as result attribute. If the prior discovery request, resulted in errors then it is specified in the error attribute. Reasons of errors can be    1. **more than one definitive match for the given request**    2. **no verified identifer was specified** 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DiscoveryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dev.ndhm.gov.in/cm");

    DiscoveryApi apiInstance = new DiscoveryApi(defaultClient);
    String authorization = "authorization_example"; // String | Access token which was issued after successful login with gateway auth server.
    PatientDiscoveryResult patientDiscoveryResult = new PatientDiscoveryResult(); // PatientDiscoveryResult | 
    try {
      apiInstance.v05CareContextsOnDiscoverPost(authorization, patientDiscoveryResult);
    } catch (ApiException e) {
      System.err.println("Exception when calling DiscoveryApi#v05CareContextsOnDiscoverPost");
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
| **patientDiscoveryResult** | [**PatientDiscoveryResult**](PatientDiscoveryResult.md)|  | |

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

