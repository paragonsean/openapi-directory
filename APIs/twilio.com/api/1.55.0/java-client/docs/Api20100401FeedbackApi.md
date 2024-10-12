# Api20100401FeedbackApi

All URIs are relative to *https://api.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createMessageFeedback**](Api20100401FeedbackApi.md#createMessageFeedback) | **POST** /2010-04-01/Accounts/{AccountSid}/Messages/{MessageSid}/Feedback.json |  |


<a id="createMessageFeedback"></a>
# **createMessageFeedback**
> ApiV2010AccountMessageMessageFeedback createMessageFeedback(accountSid, messageSid, outcome)



Create Message Feedback to confirm a tracked user action was performed by the recipient of the associated Message

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Api20100401FeedbackApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    Api20100401FeedbackApi apiInstance = new Api20100401FeedbackApi(defaultClient);
    String accountSid = "accountSid_example"; // String | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) associated with the Message resource for which to create MessageFeedback.
    String messageSid = "messageSid_example"; // String | The SID of the Message resource for which to create MessageFeedback.
    MessageFeedbackEnumOutcome outcome = MessageFeedbackEnumOutcome.fromValue("confirmed"); // MessageFeedbackEnumOutcome | 
    try {
      ApiV2010AccountMessageMessageFeedback result = apiInstance.createMessageFeedback(accountSid, messageSid, outcome);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Api20100401FeedbackApi#createMessageFeedback");
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
| **accountSid** | **String**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) associated with the Message resource for which to create MessageFeedback. | |
| **messageSid** | **String**| The SID of the Message resource for which to create MessageFeedback. | |
| **outcome** | **MessageFeedbackEnumOutcome**|  | [optional] [enum: confirmed, unconfirmed] |

### Return type

[**ApiV2010AccountMessageMessageFeedback**](ApiV2010AccountMessageMessageFeedback.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |

