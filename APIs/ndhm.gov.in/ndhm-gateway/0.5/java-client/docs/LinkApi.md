# LinkApi

All URIs are relative to *https://dev.ndhm.gov.in/gateway*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**v05LinksLinkAddContextsPost**](LinkApi.md#v05LinksLinkAddContextsPost) | **POST** /v0.5/links/link/add-contexts | API for HIP initiated care-context linking for patient |
| [**v05LinksLinkConfirmPost**](LinkApi.md#v05LinksLinkConfirmPost) | **POST** /v0.5/links/link/confirm | Token submission by Consent Manager for link confirmation |
| [**v05LinksLinkInitPost**](LinkApi.md#v05LinksLinkInitPost) | **POST** /v0.5/links/link/init | Link patient&#39;s care contexts |
| [**v05LinksLinkOnAddContextsPost**](LinkApi.md#v05LinksLinkOnAddContextsPost) | **POST** /v0.5/links/link/on-add-contexts | callback API for HIP initiated patient linking /link/add-context |
| [**v05LinksLinkOnConfirmPost**](LinkApi.md#v05LinksLinkOnConfirmPost) | **POST** /v0.5/links/link/on-confirm | Token authenticated by HIP, indicating completion of linkage of care-contexts |
| [**v05LinksLinkOnInitPost**](LinkApi.md#v05LinksLinkOnInitPost) | **POST** /v0.5/links/link/on-init | Response to patient&#39;s care context link request |


<a id="v05LinksLinkAddContextsPost"></a>
# **v05LinksLinkAddContextsPost**
> v05LinksLinkAddContextsPost(authorization, X_CM_ID, patientCareContextLinkRequest)

API for HIP initiated care-context linking for patient

API to submit care-context to CM for HIP initiated linking. The API must accompany the \&quot;accessToken\&quot; fetched in the users/auth process.     1. subsequent usage for accessToken may be invalid if it was meant for one-time usage or if it expired 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LinkApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dev.ndhm.gov.in/gateway");

    LinkApi apiInstance = new LinkApi(defaultClient);
    String authorization = "authorization_example"; // String | Access token which was issued after successful login with gateway auth server.
    String X_CM_ID = "X_CM_ID_example"; // String | Suffix of the consent manager to which the request was intended.
    PatientCareContextLinkRequest patientCareContextLinkRequest = new PatientCareContextLinkRequest(); // PatientCareContextLinkRequest | 
    try {
      apiInstance.v05LinksLinkAddContextsPost(authorization, X_CM_ID, patientCareContextLinkRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling LinkApi#v05LinksLinkAddContextsPost");
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
| **patientCareContextLinkRequest** | [**PatientCareContextLinkRequest**](PatientCareContextLinkRequest.md)|  | |

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
| **202** | accepted |  -  |
| **400** | **Causes:**   * required information not provided  |  -  |
| **401** | **Causes:**   * Unauthorized request  |  -  |
| **500** | **Causes:**   * Downstream system(s) is down.   * Unhandled exceptions.  |  -  |

<a id="v05LinksLinkConfirmPost"></a>
# **v05LinksLinkConfirmPost**
> v05LinksLinkConfirmPost(authorization, X_HIP_ID, linkConfirmationRequest)

Token submission by Consent Manager for link confirmation

API to submit the token that was sent by HIP during the link request.  

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LinkApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dev.ndhm.gov.in/gateway");

    LinkApi apiInstance = new LinkApi(defaultClient);
    String authorization = "authorization_example"; // String | Access token which was issued after successful login with gateway auth server.
    String X_HIP_ID = "X_HIP_ID_example"; // String | Identifier of the health information provider to which the request was intended.
    LinkConfirmationRequest linkConfirmationRequest = new LinkConfirmationRequest(); // LinkConfirmationRequest | 
    try {
      apiInstance.v05LinksLinkConfirmPost(authorization, X_HIP_ID, linkConfirmationRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling LinkApi#v05LinksLinkConfirmPost");
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
| **linkConfirmationRequest** | [**LinkConfirmationRequest**](LinkConfirmationRequest.md)|  | |

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
| **202** | accepted |  -  |
| **400** | **Causes:**   * Token is not provided  |  -  |
| **401** | **Causes:**   * Unauthorized request  |  -  |
| **500** | **Causes:**   * Downstream system(s) is down.   * Unhandled exceptions.  |  -  |

<a id="v05LinksLinkInitPost"></a>
# **v05LinksLinkInitPost**
> v05LinksLinkInitPost(authorization, X_HIP_ID, patientLinkReferenceRequest)

Link patient&#39;s care contexts

Request from CM to links care contexts associated with only one patient   1. **Validate account reference number and care context reference number**   2. **Validate transactionId in the request with discovery request entry to check whether there was a discovery       and were these care contexts discovered or not for a given patient**   3. **Before eventual link confirmation, HIP needs to authenticate the request with the patient(eg: OTP verification)**   4. **HIP should communicate the mode of authentication of a successful request to Consent Manager** 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LinkApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dev.ndhm.gov.in/gateway");

    LinkApi apiInstance = new LinkApi(defaultClient);
    String authorization = "authorization_example"; // String | Access token which was issued after successful login with gateway auth server.
    String X_HIP_ID = "X_HIP_ID_example"; // String | Identifier of the health information provider to which the request was intended.
    PatientLinkReferenceRequest patientLinkReferenceRequest = new PatientLinkReferenceRequest(); // PatientLinkReferenceRequest | 
    try {
      apiInstance.v05LinksLinkInitPost(authorization, X_HIP_ID, patientLinkReferenceRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling LinkApi#v05LinksLinkInitPost");
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
| **patientLinkReferenceRequest** | [**PatientLinkReferenceRequest**](PatientLinkReferenceRequest.md)|  | |

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
| **400** | **Causes:**   * Consent manager user id is not provided   * Patient reference number is not provided   * Care context references are not provided  |  -  |
| **401** | **Causes:**   * Unauthorized request  |  -  |
| **500** | **Causes:**   * Downstream system(s) is down.   * Unhandled exceptions.  |  -  |

<a id="v05LinksLinkOnAddContextsPost"></a>
# **v05LinksLinkOnAddContextsPost**
> v05LinksLinkOnAddContextsPost(authorization, X_HIP_ID, patientCareContextLinkResponse)

callback API for HIP initiated patient linking /link/add-context

If the accessToken is valid for purpose of linking, and specified details provided, CM will send \&quot;acknoweldgement.status\&quot; as SUCCESS. If any error occcurred, for example invalid token, or other required patient or care-context information not provided, then \&quot;error\&quot; attribute conveys so.    1. **accessToken must be valid and must be for the purpose of linking** 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LinkApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dev.ndhm.gov.in/gateway");

    LinkApi apiInstance = new LinkApi(defaultClient);
    String authorization = "authorization_example"; // String | Access token which was issued after successful login with gateway auth server.
    String X_HIP_ID = "X_HIP_ID_example"; // String | Identifier of the health information provider to which the request was intended.
    PatientCareContextLinkResponse patientCareContextLinkResponse = new PatientCareContextLinkResponse(); // PatientCareContextLinkResponse | 
    try {
      apiInstance.v05LinksLinkOnAddContextsPost(authorization, X_HIP_ID, patientCareContextLinkResponse);
    } catch (ApiException e) {
      System.err.println("Exception when calling LinkApi#v05LinksLinkOnAddContextsPost");
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
| **patientCareContextLinkResponse** | [**PatientCareContextLinkResponse**](PatientCareContextLinkResponse.md)|  | |

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
| **202** | accepted |  -  |
| **400** | **Causes:**   * resp not specified   * atleast acknowledgement or error should be specified  |  -  |
| **401** | **Causes:**   * Unauthorized request  |  -  |
| **500** | **Causes:**   * Downstream system(s) is down.   * Unhandled exceptions.  |  -  |

<a id="v05LinksLinkOnConfirmPost"></a>
# **v05LinksLinkOnConfirmPost**
> v05LinksLinkOnConfirmPost(authorization, X_CM_ID, patientLinkResult)

Token authenticated by HIP, indicating completion of linkage of care-contexts

Returns a list of linked care contexts with patient reference number.   1. **Validated and linked account reference number**   2. **Validated that the token sent from Consent Manager is same as the one generated by HIP**   3. **Verified that same Consent Manager which made the link request is sending the token**   4. **Results of unmasked linked care contexts with patient reference number** 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LinkApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dev.ndhm.gov.in/gateway");

    LinkApi apiInstance = new LinkApi(defaultClient);
    String authorization = "authorization_example"; // String | Access token which was issued after successful login with gateway auth server.
    String X_CM_ID = "X_CM_ID_example"; // String | Suffix of the consent manager to which the request was intended.
    PatientLinkResult patientLinkResult = new PatientLinkResult(); // PatientLinkResult | 
    try {
      apiInstance.v05LinksLinkOnConfirmPost(authorization, X_CM_ID, patientLinkResult);
    } catch (ApiException e) {
      System.err.println("Exception when calling LinkApi#v05LinksLinkOnConfirmPost");
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
| **patientLinkResult** | [**PatientLinkResult**](PatientLinkResult.md)|  | |

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
| **202** | accepted |  -  |
| **400** | **Causes:**   * resp not specified   * atleast patient or error should be specified  |  -  |
| **401** | **Causes:**   * Unauthorized request  |  -  |
| **500** | **Causes:**   * Downstream system(s) is down.   * Unhandled exceptions.  |  -  |

<a id="v05LinksLinkOnInitPost"></a>
# **v05LinksLinkOnInitPost**
> v05LinksLinkOnInitPost(authorization, X_CM_ID, patientLinkReferenceResult)

Response to patient&#39;s care context link request

Result of patient care-context link request from HIP end. This happens in context of previous discovery of patient found at HIP end, therefore the link requests ought to be in reference to the patient reference and care-context references previously returned by the HIP. The correlation of discovery and link request is maintained through the transactionId. HIP should have   1. **Validated transactionId in the request to check whether there was a discovery done previously, and the link request corresponds to returned patient care care context references**   2. **Before returning the response, HIP should have sent an authentication request to the patient(eg: OTP verification)**   3. **HIP should communicate the mode of authentication of a successful request**   4. **HIP subsequently should expect the token passed via /link/confirm against the link.referenceNumber passed in this call**                        The error section in the body, represents the potential errors that may have occurred. Possible reasons:   1. **Patient reference number is invalid**   2. **Care context reference numbers are invalid** 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LinkApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dev.ndhm.gov.in/gateway");

    LinkApi apiInstance = new LinkApi(defaultClient);
    String authorization = "authorization_example"; // String | Access token which was issued after successful login with gateway auth server.
    String X_CM_ID = "X_CM_ID_example"; // String | Suffix of the consent manager to which the request was intended.
    PatientLinkReferenceResult patientLinkReferenceResult = new PatientLinkReferenceResult(); // PatientLinkReferenceResult | 
    try {
      apiInstance.v05LinksLinkOnInitPost(authorization, X_CM_ID, patientLinkReferenceResult);
    } catch (ApiException e) {
      System.err.println("Exception when calling LinkApi#v05LinksLinkOnInitPost");
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
| **patientLinkReferenceResult** | [**PatientLinkReferenceResult**](PatientLinkReferenceResult.md)|  | |

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

