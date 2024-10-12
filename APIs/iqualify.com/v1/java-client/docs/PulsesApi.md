# PulsesApi

All URIs are relative to *https://api.iqualify.com/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**offeringsOfferingIdAnalyticsPulsesGet**](PulsesApi.md#offeringsOfferingIdAnalyticsPulsesGet) | **GET** /offerings/{offeringId}/analytics/pulses | Find all pulse IDs in the specified offering |
| [**offeringsOfferingIdAnalyticsPulsesPulseIdResponsesGet**](PulsesApi.md#offeringsOfferingIdAnalyticsPulsesPulseIdResponsesGet) | **GET** /offerings/{offeringId}/analytics/pulses/{pulseId}/responses | Find pulses by offeringId and pulseId |
| [**offeringsOfferingIdAnalyticsPulsesResponsesGet**](PulsesApi.md#offeringsOfferingIdAnalyticsPulsesResponsesGet) | **GET** /offerings/{offeringId}/analytics/pulses/responses | Find pulses by offeringId |


<a id="offeringsOfferingIdAnalyticsPulsesGet"></a>
# **offeringsOfferingIdAnalyticsPulsesGet**
> List&lt;String&gt; offeringsOfferingIdAnalyticsPulsesGet(offeringId)

Find all pulse IDs in the specified offering

Responds with the IDs of all pulses that learners have responded to in a specified offering.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PulsesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.iqualify.com/v1");
    
    // Configure API key authorization: Authorization
    ApiKeyAuth Authorization = (ApiKeyAuth) defaultClient.getAuthentication("Authorization");
    Authorization.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Authorization.setApiKeyPrefix("Token");

    PulsesApi apiInstance = new PulsesApi(defaultClient);
    String offeringId = "offeringId_example"; // String | offering's id
    try {
      List<String> result = apiInstance.offeringsOfferingIdAnalyticsPulsesGet(offeringId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PulsesApi#offeringsOfferingIdAnalyticsPulsesGet");
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
| **offeringId** | **String**| offering&#39;s id | |

### Return type

**List&lt;String&gt;**

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Pulses&#39; ids |  -  |
| **401** | No authorization token was found. |  -  |
| **403** | You are not allowed to access this resource. |  -  |
| **404** | Not Found |  -  |

<a id="offeringsOfferingIdAnalyticsPulsesPulseIdResponsesGet"></a>
# **offeringsOfferingIdAnalyticsPulsesPulseIdResponsesGet**
> List&lt;PulseResponse&gt; offeringsOfferingIdAnalyticsPulsesPulseIdResponsesGet(offeringId, pulseId)

Find pulses by offeringId and pulseId

Responds with pulse&#39;s responses, matching the pulseId, in an offering matching the offeringId.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PulsesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.iqualify.com/v1");
    
    // Configure API key authorization: Authorization
    ApiKeyAuth Authorization = (ApiKeyAuth) defaultClient.getAuthentication("Authorization");
    Authorization.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Authorization.setApiKeyPrefix("Token");

    PulsesApi apiInstance = new PulsesApi(defaultClient);
    String offeringId = "offeringId_example"; // String | offering's id
    String pulseId = "pulseId_example"; // String | pulse's base id
    try {
      List<PulseResponse> result = apiInstance.offeringsOfferingIdAnalyticsPulsesPulseIdResponsesGet(offeringId, pulseId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PulsesApi#offeringsOfferingIdAnalyticsPulsesPulseIdResponsesGet");
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
| **offeringId** | **String**| offering&#39;s id | |
| **pulseId** | **String**| pulse&#39;s base id | |

### Return type

[**List&lt;PulseResponse&gt;**](PulseResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Pulse data matching pulseId |  -  |
| **401** | No authorization token was found. |  -  |
| **403** | You are not allowed to access this resource. |  -  |
| **404** | Not Found |  -  |

<a id="offeringsOfferingIdAnalyticsPulsesResponsesGet"></a>
# **offeringsOfferingIdAnalyticsPulsesResponsesGet**
> List&lt;PulseResponse&gt; offeringsOfferingIdAnalyticsPulsesResponsesGet(offeringId, pulseType, responseTime)

Find pulses by offeringId

Responds with pulse&#39;s responses in an offering matching the offeringId.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PulsesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.iqualify.com/v1");
    
    // Configure API key authorization: Authorization
    ApiKeyAuth Authorization = (ApiKeyAuth) defaultClient.getAuthentication("Authorization");
    Authorization.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Authorization.setApiKeyPrefix("Token");

    PulsesApi apiInstance = new PulsesApi(defaultClient);
    String offeringId = "offeringId_example"; // String | offering's id
    String pulseType = "submit_text"; // String | Filter pulse responses by type.
    OfferingsOfferingIdAnalyticsPulsesResponsesGetResponseTimeParameter responseTime = new OfferingsOfferingIdAnalyticsPulsesResponsesGetResponseTimeParameter(); // OfferingsOfferingIdAnalyticsPulsesResponsesGetResponseTimeParameter | Filter pulse responses by responseTime. Lower then (`lt`), lower then or equal (`lte`), greater then (`gt`) and greater then or equal (`gte`) operators are available. Example of filtering by time range __gte__2017-03-14T07:30:00Z__
    try {
      List<PulseResponse> result = apiInstance.offeringsOfferingIdAnalyticsPulsesResponsesGet(offeringId, pulseType, responseTime);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PulsesApi#offeringsOfferingIdAnalyticsPulsesResponsesGet");
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
| **offeringId** | **String**| offering&#39;s id | |
| **pulseType** | **String**| Filter pulse responses by type. | [optional] [enum: submit_text, MCQ, spatial_triangular, spatial_planar, spatial_linear] |
| **responseTime** | [**OfferingsOfferingIdAnalyticsPulsesResponsesGetResponseTimeParameter**](.md)| Filter pulse responses by responseTime. Lower then (&#x60;lt&#x60;), lower then or equal (&#x60;lte&#x60;), greater then (&#x60;gt&#x60;) and greater then or equal (&#x60;gte&#x60;) operators are available. Example of filtering by time range __gte__2017-03-14T07:30:00Z__ | [optional] |

### Return type

[**List&lt;PulseResponse&gt;**](PulseResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | All pulses&#39; responses |  -  |
| **401** | No authorization token was found. |  -  |
| **403** | You are not allowed to access this resource. |  -  |
| **404** | Not Found |  -  |

