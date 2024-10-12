# SetupApi

All URIs are relative to */api/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getSetup**](SetupApi.md#getSetup) | **GET** /setup | Check if database has default user, org, bucket |
| [**postSetup**](SetupApi.md#postSetup) | **POST** /setup | Set up initial user, org and bucket |


<a id="getSetup"></a>
# **getSetup**
> IsOnboarding getSetup(zapTraceSpan)

Check if database has default user, org, bucket

Returns &#x60;true&#x60; if no default user, organization, or bucket has been created.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SetupApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");

    SetupApi apiInstance = new SetupApi(defaultClient);
    String zapTraceSpan = "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}"; // String | OpenTracing span context
    try {
      IsOnboarding result = apiInstance.getSetup(zapTraceSpan);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SetupApi#getSetup");
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
| **zapTraceSpan** | **String**| OpenTracing span context | [optional] |

### Return type

[**IsOnboarding**](IsOnboarding.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | allowed true or false |  -  |

<a id="postSetup"></a>
# **postSetup**
> OnboardingResponse postSetup(onboardingRequest, zapTraceSpan)

Set up initial user, org and bucket

Post an onboarding request to set up initial user, org and bucket.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SetupApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");

    SetupApi apiInstance = new SetupApi(defaultClient);
    OnboardingRequest onboardingRequest = new OnboardingRequest(); // OnboardingRequest | Source to create
    String zapTraceSpan = "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}"; // String | OpenTracing span context
    try {
      OnboardingResponse result = apiInstance.postSetup(onboardingRequest, zapTraceSpan);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SetupApi#postSetup");
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
| **onboardingRequest** | [**OnboardingRequest**](OnboardingRequest.md)| Source to create | |
| **zapTraceSpan** | **String**| OpenTracing span context | [optional] |

### Return type

[**OnboardingResponse**](OnboardingResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created default user, bucket, org |  -  |
| **0** | Non 2XX error response from server. |  -  |

