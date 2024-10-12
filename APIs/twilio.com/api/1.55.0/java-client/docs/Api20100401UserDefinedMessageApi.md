# Api20100401UserDefinedMessageApi

All URIs are relative to *https://api.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createUserDefinedMessage**](Api20100401UserDefinedMessageApi.md#createUserDefinedMessage) | **POST** /2010-04-01/Accounts/{AccountSid}/Calls/{CallSid}/UserDefinedMessages.json |  |


<a id="createUserDefinedMessage"></a>
# **createUserDefinedMessage**
> ApiV2010AccountCallUserDefinedMessage createUserDefinedMessage(accountSid, callSid, content, idempotencyKey)



Create a new User Defined Message for the given Call SID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Api20100401UserDefinedMessageApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    Api20100401UserDefinedMessageApi apiInstance = new Api20100401UserDefinedMessageApi(defaultClient);
    String accountSid = "accountSid_example"; // String | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created User Defined Message.
    String callSid = "callSid_example"; // String | The SID of the [Call](https://www.twilio.com/docs/voice/api/call-resource) the User Defined Message is associated with.
    String content = "content_example"; // String | The User Defined Message in the form of URL-encoded JSON string.
    String idempotencyKey = "idempotencyKey_example"; // String | A unique string value to identify API call. This should be a unique string value per API call and can be a randomly generated.
    try {
      ApiV2010AccountCallUserDefinedMessage result = apiInstance.createUserDefinedMessage(accountSid, callSid, content, idempotencyKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Api20100401UserDefinedMessageApi#createUserDefinedMessage");
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
| **accountSid** | **String**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created User Defined Message. | |
| **callSid** | **String**| The SID of the [Call](https://www.twilio.com/docs/voice/api/call-resource) the User Defined Message is associated with. | |
| **content** | **String**| The User Defined Message in the form of URL-encoded JSON string. | |
| **idempotencyKey** | **String**| A unique string value to identify API call. This should be a unique string value per API call and can be a randomly generated. | [optional] |

### Return type

[**ApiV2010AccountCallUserDefinedMessage**](ApiV2010AccountCallUserDefinedMessage.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |

