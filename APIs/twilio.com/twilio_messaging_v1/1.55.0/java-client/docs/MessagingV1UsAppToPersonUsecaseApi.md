# MessagingV1UsAppToPersonUsecaseApi

All URIs are relative to *https://messaging.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**fetchUsAppToPersonUsecase**](MessagingV1UsAppToPersonUsecaseApi.md#fetchUsAppToPersonUsecase) | **GET** /v1/Services/{MessagingServiceSid}/Compliance/Usa2p/Usecases |  |


<a id="fetchUsAppToPersonUsecase"></a>
# **fetchUsAppToPersonUsecase**
> MessagingV1ServiceUsAppToPersonUsecase fetchUsAppToPersonUsecase(messagingServiceSid, brandRegistrationSid)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MessagingV1UsAppToPersonUsecaseApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://messaging.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    MessagingV1UsAppToPersonUsecaseApi apiInstance = new MessagingV1UsAppToPersonUsecaseApi(defaultClient);
    String messagingServiceSid = "messagingServiceSid_example"; // String | The SID of the [Messaging Service](https://www.twilio.com/docs/messaging/api/service-resource) to fetch the resource from.
    String brandRegistrationSid = "brandRegistrationSid_example"; // String | The unique string to identify the A2P brand.
    try {
      MessagingV1ServiceUsAppToPersonUsecase result = apiInstance.fetchUsAppToPersonUsecase(messagingServiceSid, brandRegistrationSid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MessagingV1UsAppToPersonUsecaseApi#fetchUsAppToPersonUsecase");
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
| **messagingServiceSid** | **String**| The SID of the [Messaging Service](https://www.twilio.com/docs/messaging/api/service-resource) to fetch the resource from. | |
| **brandRegistrationSid** | **String**| The unique string to identify the A2P brand. | [optional] |

### Return type

[**MessagingV1ServiceUsAppToPersonUsecase**](MessagingV1ServiceUsAppToPersonUsecase.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

