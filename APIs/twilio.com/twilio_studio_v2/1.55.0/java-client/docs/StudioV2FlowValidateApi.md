# StudioV2FlowValidateApi

All URIs are relative to *https://studio.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**updateFlowValidate**](StudioV2FlowValidateApi.md#updateFlowValidate) | **POST** /v2/Flows/Validate |  |


<a id="updateFlowValidate"></a>
# **updateFlowValidate**
> StudioV2FlowValidate updateFlowValidate(definition, friendlyName, status, commitMessage)



Validate flow JSON definition

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StudioV2FlowValidateApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://studio.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    StudioV2FlowValidateApi apiInstance = new StudioV2FlowValidateApi(defaultClient);
    Object definition = null; // Object | JSON representation of flow definition.
    String friendlyName = "friendlyName_example"; // String | The string that you assigned to describe the Flow.
    FlowValidateEnumStatus status = FlowValidateEnumStatus.fromValue("draft"); // FlowValidateEnumStatus | 
    String commitMessage = "commitMessage_example"; // String | Description of change made in the revision.
    try {
      StudioV2FlowValidate result = apiInstance.updateFlowValidate(definition, friendlyName, status, commitMessage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StudioV2FlowValidateApi#updateFlowValidate");
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
| **definition** | [**Object**](Object.md)| JSON representation of flow definition. | |
| **friendlyName** | **String**| The string that you assigned to describe the Flow. | |
| **status** | **FlowValidateEnumStatus**|  | [enum: draft, published] |
| **commitMessage** | **String**| Description of change made in the revision. | [optional] |

### Return type

[**StudioV2FlowValidate**](StudioV2FlowValidate.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

