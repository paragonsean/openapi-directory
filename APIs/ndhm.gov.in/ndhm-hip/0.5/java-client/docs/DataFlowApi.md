# DataFlowApi

All URIs are relative to *https://dev.ndhm.gov.in/gateway*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**v05HealthInformationHipRequestPost**](DataFlowApi.md#v05HealthInformationHipRequestPost) | **POST** /v0.5/health-information/hip/request | Health information data request |


<a id="v05HealthInformationHipRequestPost"></a>
# **v05HealthInformationHipRequestPost**
> v05HealthInformationHipRequestPost(authorization, X_HIP_ID, hiPHealthInformationRequest)

Health information data request

API called by CM to request Health information from HIP against a validated consent artefact. The transactionId is the correlation id that HIP should use use when pushing data to the **dataPushUrl**.  

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DataFlowApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dev.ndhm.gov.in/gateway");

    DataFlowApi apiInstance = new DataFlowApi(defaultClient);
    String authorization = "authorization_example"; // String | Access token which was issued after successful login with gateway auth server, which will be sent by gateway to authenticate itself with API bridge.
    String X_HIP_ID = "X_HIP_ID_example"; // String | Identifier of the health information provider to which the request was intended.
    HIPHealthInformationRequest hiPHealthInformationRequest = new HIPHealthInformationRequest(); // HIPHealthInformationRequest | 
    try {
      apiInstance.v05HealthInformationHipRequestPost(authorization, X_HIP_ID, hiPHealthInformationRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling DataFlowApi#v05HealthInformationHipRequestPost");
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
| **hiPHealthInformationRequest** | [**HIPHealthInformationRequest**](HIPHealthInformationRequest.md)|  | |

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
| **202** | Request accepted. |  -  |
| **400** | **Causes:**   * Bad request  |  -  |
| **401** | **Causes:**   * Token is invalid or Link has expired  |  -  |
| **500** | **Causes:**   * Downstream system(s) is down.   * Unhandled exceptions.  |  -  |

