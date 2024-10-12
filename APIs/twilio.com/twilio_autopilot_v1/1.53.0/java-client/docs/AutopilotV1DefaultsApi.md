# AutopilotV1DefaultsApi

All URIs are relative to *https://autopilot.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**fetchDefaults**](AutopilotV1DefaultsApi.md#fetchDefaults) | **GET** /v1/Assistants/{AssistantSid}/Defaults |  |
| [**updateDefaults**](AutopilotV1DefaultsApi.md#updateDefaults) | **POST** /v1/Assistants/{AssistantSid}/Defaults |  |


<a id="fetchDefaults"></a>
# **fetchDefaults**
> AutopilotV1AssistantDefaults fetchDefaults(assistantSid)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AutopilotV1DefaultsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://autopilot.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    AutopilotV1DefaultsApi apiInstance = new AutopilotV1DefaultsApi(defaultClient);
    String assistantSid = "assistantSid_example"; // String | The SID of the [Assistant](https://www.twilio.com/docs/autopilot/api/assistant) that is the parent of the resource to fetch.
    try {
      AutopilotV1AssistantDefaults result = apiInstance.fetchDefaults(assistantSid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AutopilotV1DefaultsApi#fetchDefaults");
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
| **assistantSid** | **String**| The SID of the [Assistant](https://www.twilio.com/docs/autopilot/api/assistant) that is the parent of the resource to fetch. | |

### Return type

[**AutopilotV1AssistantDefaults**](AutopilotV1AssistantDefaults.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="updateDefaults"></a>
# **updateDefaults**
> AutopilotV1AssistantDefaults updateDefaults(assistantSid, defaults)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AutopilotV1DefaultsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://autopilot.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    AutopilotV1DefaultsApi apiInstance = new AutopilotV1DefaultsApi(defaultClient);
    String assistantSid = "assistantSid_example"; // String | The SID of the [Assistant](https://www.twilio.com/docs/autopilot/api/assistant) that is the parent of the resource to update.
    Object defaults = null; // Object | A JSON string that describes the default task links for the `assistant_initiation`, `collect`, and `fallback` situations.
    try {
      AutopilotV1AssistantDefaults result = apiInstance.updateDefaults(assistantSid, defaults);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AutopilotV1DefaultsApi#updateDefaults");
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
| **assistantSid** | **String**| The SID of the [Assistant](https://www.twilio.com/docs/autopilot/api/assistant) that is the parent of the resource to update. | |
| **defaults** | [**Object**](Object.md)| A JSON string that describes the default task links for the &#x60;assistant_initiation&#x60;, &#x60;collect&#x60;, and &#x60;fallback&#x60; situations. | [optional] |

### Return type

[**AutopilotV1AssistantDefaults**](AutopilotV1AssistantDefaults.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

