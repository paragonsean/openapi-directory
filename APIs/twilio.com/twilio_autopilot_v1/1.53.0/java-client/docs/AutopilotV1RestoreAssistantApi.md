# AutopilotV1RestoreAssistantApi

All URIs are relative to *https://autopilot.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**updateRestoreAssistant**](AutopilotV1RestoreAssistantApi.md#updateRestoreAssistant) | **POST** /v1/Assistants/Restore |  |


<a id="updateRestoreAssistant"></a>
# **updateRestoreAssistant**
> AutopilotV1RestoreAssistant updateRestoreAssistant(assistant)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AutopilotV1RestoreAssistantApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://autopilot.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    AutopilotV1RestoreAssistantApi apiInstance = new AutopilotV1RestoreAssistantApi(defaultClient);
    String assistant = "assistant_example"; // String | The Twilio-provided string that uniquely identifies the Assistant resource to restore.
    try {
      AutopilotV1RestoreAssistant result = apiInstance.updateRestoreAssistant(assistant);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AutopilotV1RestoreAssistantApi#updateRestoreAssistant");
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
| **assistant** | **String**| The Twilio-provided string that uniquely identifies the Assistant resource to restore. | |

### Return type

[**AutopilotV1RestoreAssistant**](AutopilotV1RestoreAssistant.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

