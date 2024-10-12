# BypassActivationLockAttemptsApi

All URIs are relative to *https://api.meraki.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createNetworkSmBypassActivationLockAttempt_1**](BypassActivationLockAttemptsApi.md#createNetworkSmBypassActivationLockAttempt_1) | **POST** /networks/{networkId}/sm/bypassActivationLockAttempts | Bypass activation lock attempt |
| [**getNetworkSmBypassActivationLockAttempt_1**](BypassActivationLockAttemptsApi.md#getNetworkSmBypassActivationLockAttempt_1) | **GET** /networks/{networkId}/sm/bypassActivationLockAttempts/{attemptId} | Bypass activation lock attempt status |


<a id="createNetworkSmBypassActivationLockAttempt_1"></a>
# **createNetworkSmBypassActivationLockAttempt_1**
> Object createNetworkSmBypassActivationLockAttempt_1(networkId, createNetworkSmBypassActivationLockAttemptRequest)

Bypass activation lock attempt

Bypass activation lock attempt

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BypassActivationLockAttemptsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    BypassActivationLockAttemptsApi apiInstance = new BypassActivationLockAttemptsApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    CreateNetworkSmBypassActivationLockAttemptRequest createNetworkSmBypassActivationLockAttemptRequest = new CreateNetworkSmBypassActivationLockAttemptRequest(); // CreateNetworkSmBypassActivationLockAttemptRequest | 
    try {
      Object result = apiInstance.createNetworkSmBypassActivationLockAttempt_1(networkId, createNetworkSmBypassActivationLockAttemptRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BypassActivationLockAttemptsApi#createNetworkSmBypassActivationLockAttempt_1");
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
| **networkId** | **String**|  | |
| **createNetworkSmBypassActivationLockAttemptRequest** | [**CreateNetworkSmBypassActivationLockAttemptRequest**](CreateNetworkSmBypassActivationLockAttemptRequest.md)|  | |

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Successful operation |  -  |

<a id="getNetworkSmBypassActivationLockAttempt_1"></a>
# **getNetworkSmBypassActivationLockAttempt_1**
> Object getNetworkSmBypassActivationLockAttempt_1(networkId, attemptId)

Bypass activation lock attempt status

Bypass activation lock attempt status

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BypassActivationLockAttemptsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    BypassActivationLockAttemptsApi apiInstance = new BypassActivationLockAttemptsApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String attemptId = "attemptId_example"; // String | 
    try {
      Object result = apiInstance.getNetworkSmBypassActivationLockAttempt_1(networkId, attemptId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BypassActivationLockAttemptsApi#getNetworkSmBypassActivationLockAttempt_1");
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
| **networkId** | **String**|  | |
| **attemptId** | **String**|  | |

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

