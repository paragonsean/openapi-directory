# MessagingV1DomainConfigMessagingServiceApi

All URIs are relative to *https://messaging.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**fetchDomainConfigMessagingService**](MessagingV1DomainConfigMessagingServiceApi.md#fetchDomainConfigMessagingService) | **GET** /v1/LinkShortening/MessagingService/{MessagingServiceSid}/DomainConfig |  |


<a id="fetchDomainConfigMessagingService"></a>
# **fetchDomainConfigMessagingService**
> MessagingV1DomainConfigMessagingService fetchDomainConfigMessagingService(messagingServiceSid)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MessagingV1DomainConfigMessagingServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://messaging.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    MessagingV1DomainConfigMessagingServiceApi apiInstance = new MessagingV1DomainConfigMessagingServiceApi(defaultClient);
    String messagingServiceSid = "messagingServiceSid_example"; // String | Unique string used to identify the Messaging service that this domain should be associated with.
    try {
      MessagingV1DomainConfigMessagingService result = apiInstance.fetchDomainConfigMessagingService(messagingServiceSid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MessagingV1DomainConfigMessagingServiceApi#fetchDomainConfigMessagingService");
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
| **messagingServiceSid** | **String**| Unique string used to identify the Messaging service that this domain should be associated with. | |

### Return type

[**MessagingV1DomainConfigMessagingService**](MessagingV1DomainConfigMessagingService.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

