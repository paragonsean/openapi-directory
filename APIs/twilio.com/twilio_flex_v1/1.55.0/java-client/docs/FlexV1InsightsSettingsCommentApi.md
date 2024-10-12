# FlexV1InsightsSettingsCommentApi

All URIs are relative to *https://flex-api.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**fetchInsightsSettingsComment**](FlexV1InsightsSettingsCommentApi.md#fetchInsightsSettingsComment) | **GET** /v1/Insights/QualityManagement/Settings/CommentTags |  |


<a id="fetchInsightsSettingsComment"></a>
# **fetchInsightsSettingsComment**
> FlexV1InsightsSettingsComment fetchInsightsSettingsComment(authorization)



To get the Comment Settings for an Account

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FlexV1InsightsSettingsCommentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://flex-api.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    FlexV1InsightsSettingsCommentApi apiInstance = new FlexV1InsightsSettingsCommentApi(defaultClient);
    String authorization = "authorization_example"; // String | The Authorization HTTP request header
    try {
      FlexV1InsightsSettingsComment result = apiInstance.fetchInsightsSettingsComment(authorization);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FlexV1InsightsSettingsCommentApi#fetchInsightsSettingsComment");
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

[**FlexV1InsightsSettingsComment**](FlexV1InsightsSettingsComment.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

