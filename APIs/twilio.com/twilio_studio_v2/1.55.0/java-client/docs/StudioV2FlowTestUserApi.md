# StudioV2FlowTestUserApi

All URIs are relative to *https://studio.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**fetchTestUser**](StudioV2FlowTestUserApi.md#fetchTestUser) | **GET** /v2/Flows/{Sid}/TestUsers |  |
| [**updateTestUser**](StudioV2FlowTestUserApi.md#updateTestUser) | **POST** /v2/Flows/{Sid}/TestUsers |  |


<a id="fetchTestUser"></a>
# **fetchTestUser**
> StudioV2FlowTestUser fetchTestUser(sid)



Fetch flow test users

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StudioV2FlowTestUserApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://studio.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    StudioV2FlowTestUserApi apiInstance = new StudioV2FlowTestUserApi(defaultClient);
    String sid = "sid_example"; // String | Unique identifier of the flow.
    try {
      StudioV2FlowTestUser result = apiInstance.fetchTestUser(sid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StudioV2FlowTestUserApi#fetchTestUser");
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
| **sid** | **String**| Unique identifier of the flow. | |

### Return type

[**StudioV2FlowTestUser**](StudioV2FlowTestUser.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="updateTestUser"></a>
# **updateTestUser**
> StudioV2FlowTestUser updateTestUser(sid, testUsers)



Update flow test users

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StudioV2FlowTestUserApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://studio.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    StudioV2FlowTestUserApi apiInstance = new StudioV2FlowTestUserApi(defaultClient);
    String sid = "sid_example"; // String | Unique identifier of the flow.
    List<String> testUsers = Arrays.asList(); // List<String> | List of test user identities that can test draft versions of the flow.
    try {
      StudioV2FlowTestUser result = apiInstance.updateTestUser(sid, testUsers);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StudioV2FlowTestUserApi#updateTestUser");
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
| **sid** | **String**| Unique identifier of the flow. | |
| **testUsers** | [**List&lt;String&gt;**](String.md)| List of test user identities that can test draft versions of the flow. | |

### Return type

[**StudioV2FlowTestUser**](StudioV2FlowTestUser.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

