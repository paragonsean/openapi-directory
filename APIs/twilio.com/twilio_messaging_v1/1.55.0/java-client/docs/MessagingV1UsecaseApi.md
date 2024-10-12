# MessagingV1UsecaseApi

All URIs are relative to *https://messaging.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**fetchUsecase**](MessagingV1UsecaseApi.md#fetchUsecase) | **GET** /v1/Services/Usecases |  |


<a id="fetchUsecase"></a>
# **fetchUsecase**
> MessagingV1Usecase fetchUsecase()





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MessagingV1UsecaseApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://messaging.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    MessagingV1UsecaseApi apiInstance = new MessagingV1UsecaseApi(defaultClient);
    try {
      MessagingV1Usecase result = apiInstance.fetchUsecase();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MessagingV1UsecaseApi#fetchUsecase");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**MessagingV1Usecase**](MessagingV1Usecase.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

