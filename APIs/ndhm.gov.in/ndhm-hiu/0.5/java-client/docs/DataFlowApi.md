# DataFlowApi

All URIs are relative to *https://dev.ndhm.gov.in/gateway*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**v05HealthInformationHiuOnRequestPost**](DataFlowApi.md#v05HealthInformationHiuOnRequestPost) | **POST** /v0.5/health-information/hiu/on-request | Health information data request |
| [**v05HealthInformationTransferPost**](DataFlowApi.md#v05HealthInformationTransferPost) | **POST** /v0.5/health-information/transfer | health information transfer API |


<a id="v05HealthInformationHiuOnRequestPost"></a>
# **v05HealthInformationHiuOnRequestPost**
> v05HealthInformationHiuOnRequestPost(authorization, X_HIU_ID, hiUHealthInformationRequestResponse)

Health information data request

Callback API for acknowledgement of Health information request made by HIU. Gateway calls this API when request has validated for the specified  consent id. Either the **hiRequest** or **error** would be specified. If the health info request was valid, then the ***hiRequest.transactionId*** specifies the transaction context against which HIP would send over the data.  Possible cases of errors are   1. **Invalid consent artefact id**   2. **Consent has expired**   3. **Date ranges are invalid** 

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
    String X_HIU_ID = "X_HIU_ID_example"; // String | Identifier of the health information user to which the request was intended.
    HIUHealthInformationRequestResponse hiUHealthInformationRequestResponse = new HIUHealthInformationRequestResponse(); // HIUHealthInformationRequestResponse | 
    try {
      apiInstance.v05HealthInformationHiuOnRequestPost(authorization, X_HIU_ID, hiUHealthInformationRequestResponse);
    } catch (ApiException e) {
      System.err.println("Exception when calling DataFlowApi#v05HealthInformationHiuOnRequestPost");
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
| **X_HIU_ID** | **String**| Identifier of the health information user to which the request was intended. | |
| **hiUHealthInformationRequestResponse** | [**HIUHealthInformationRequestResponse**](HIUHealthInformationRequestResponse.md)|  | |

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
| **202** | Request Accepted |  -  |
| **400** | **Causes:**   * Bad request  |  -  |
| **401** | **Causes:**   * Token is invalid or Link has expired  |  -  |
| **500** | **Causes:**   * Downstream system(s) is down.   * Unhandled exceptions.  |  -  |

<a id="v05HealthInformationTransferPost"></a>
# **v05HealthInformationTransferPost**
> v05HealthInformationTransferPost(authorization, dataNotification)

health information transfer API

**NOTE**: This API is actually the callback URL that is passed as **dataPushUrl** in the data request API - /v0.5/health-information/hip/request. This API is directly called by HIP Data Bridge and is not mediated via CM, and hence not routed through the Gateway.    1. This API should be implemented at HIU side. It maybe implemented by the Data Bridge representing the HIU.    2. Entry elements maybe ***content*** or ***link***, although for version 1, entry ***content*** is preferred.    3. Entry ***content*** (or even link reference content) must be encrypted by means of Elliptic-curve Diffie–Hellman Key Exchange, utilizing the HIU keymaterials that are passed through the data request API - /v0.5/health-information/hip/request.    4. Media contains the mimetype of content, and for v1, it is \&quot;application/fhir+json\&quot;   5. checksum is Md5 checksum of the data conent, before encryption   6. Please refer to the NDHM Sandbox documentation for the format of FHIR bundle that is passed through content  

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
    DataNotification dataNotification = new DataNotification(); // DataNotification | 
    try {
      apiInstance.v05HealthInformationTransferPost(authorization, dataNotification);
    } catch (ApiException e) {
      System.err.println("Exception when calling DataFlowApi#v05HealthInformationTransferPost");
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
| **dataNotification** | [**DataNotification**](DataNotification.md)|  | |

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
| **202** | Data accepted. |  -  |
| **401** | **Causes:**   * Invalid/Expired/Empty token.  |  -  |
| **500** | **Causes:**   * Downstream services are down  |  -  |

