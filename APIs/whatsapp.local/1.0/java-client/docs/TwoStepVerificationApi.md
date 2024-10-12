# TwoStepVerificationApi

All URIs are relative to *http://whatsapp.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**disableTwoStep**](TwoStepVerificationApi.md#disableTwoStep) | **DELETE** /settings/account/two-step | Disable-Two-Step |
| [**enableTwoStep**](TwoStepVerificationApi.md#enableTwoStep) | **POST** /settings/account/two-step | Enable-Two-Step |


<a id="disableTwoStep"></a>
# **disableTwoStep**
> disableTwoStep()

Disable-Two-Step

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TwoStepVerificationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://whatsapp.local");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    TwoStepVerificationApi apiInstance = new TwoStepVerificationApi(defaultClient);
    try {
      apiInstance.disableTwoStep();
    } catch (ApiException e) {
      System.err.println("Exception when calling TwoStepVerificationApi#disableTwoStep");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="enableTwoStep"></a>
# **enableTwoStep**
> enableTwoStep(enableTwoStepRequestBody)

Enable-Two-Step

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TwoStepVerificationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://whatsapp.local");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    TwoStepVerificationApi apiInstance = new TwoStepVerificationApi(defaultClient);
    EnableTwoStepRequestBody enableTwoStepRequestBody = new EnableTwoStepRequestBody(); // EnableTwoStepRequestBody | 
    try {
      apiInstance.enableTwoStep(enableTwoStepRequestBody);
    } catch (ApiException e) {
      System.err.println("Exception when calling TwoStepVerificationApi#enableTwoStep");
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
| **enableTwoStepRequestBody** | [**EnableTwoStepRequestBody**](EnableTwoStepRequestBody.md)|  | |

### Return type

null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

