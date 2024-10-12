# AccountsV1AuthTokenPromotionApi

All URIs are relative to *https://accounts.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**updateAuthTokenPromotion**](AccountsV1AuthTokenPromotionApi.md#updateAuthTokenPromotion) | **POST** /v1/AuthTokens/Promote |  |


<a id="updateAuthTokenPromotion"></a>
# **updateAuthTokenPromotion**
> AccountsV1AuthTokenPromotion updateAuthTokenPromotion()



Promote the secondary Auth Token to primary. After promoting the new token, all requests to Twilio using your old primary Auth Token will result in an error.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountsV1AuthTokenPromotionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://accounts.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    AccountsV1AuthTokenPromotionApi apiInstance = new AccountsV1AuthTokenPromotionApi(defaultClient);
    try {
      AccountsV1AuthTokenPromotion result = apiInstance.updateAuthTokenPromotion();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountsV1AuthTokenPromotionApi#updateAuthTokenPromotion");
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

[**AccountsV1AuthTokenPromotion**](AccountsV1AuthTokenPromotion.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

