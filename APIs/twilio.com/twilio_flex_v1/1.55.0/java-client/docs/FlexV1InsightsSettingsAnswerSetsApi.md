# FlexV1InsightsSettingsAnswerSetsApi

All URIs are relative to *https://flex-api.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**fetchInsightsSettingsAnswersets**](FlexV1InsightsSettingsAnswerSetsApi.md#fetchInsightsSettingsAnswersets) | **GET** /v1/Insights/QualityManagement/Settings/AnswerSets |  |


<a id="fetchInsightsSettingsAnswersets"></a>
# **fetchInsightsSettingsAnswersets**
> FlexV1InsightsSettingsAnswersets fetchInsightsSettingsAnswersets(authorization)



To get the Answer Set Settings for an Account

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FlexV1InsightsSettingsAnswerSetsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://flex-api.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    FlexV1InsightsSettingsAnswerSetsApi apiInstance = new FlexV1InsightsSettingsAnswerSetsApi(defaultClient);
    String authorization = "authorization_example"; // String | The Authorization HTTP request header
    try {
      FlexV1InsightsSettingsAnswersets result = apiInstance.fetchInsightsSettingsAnswersets(authorization);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FlexV1InsightsSettingsAnswerSetsApi#fetchInsightsSettingsAnswersets");
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
| **authorization** | **String**| The Authorization HTTP request header | [optional] |

### Return type

[**FlexV1InsightsSettingsAnswersets**](FlexV1InsightsSettingsAnswersets.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

