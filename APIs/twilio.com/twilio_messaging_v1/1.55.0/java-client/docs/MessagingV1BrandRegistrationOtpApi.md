# MessagingV1BrandRegistrationOtpApi

All URIs are relative to *https://messaging.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createBrandRegistrationOtp**](MessagingV1BrandRegistrationOtpApi.md#createBrandRegistrationOtp) | **POST** /v1/a2p/BrandRegistrations/{BrandRegistrationSid}/SmsOtp |  |


<a id="createBrandRegistrationOtp"></a>
# **createBrandRegistrationOtp**
> MessagingV1BrandRegistrationsBrandRegistrationOtp createBrandRegistrationOtp(brandRegistrationSid)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MessagingV1BrandRegistrationOtpApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://messaging.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    MessagingV1BrandRegistrationOtpApi apiInstance = new MessagingV1BrandRegistrationOtpApi(defaultClient);
    String brandRegistrationSid = "brandRegistrationSid_example"; // String | Brand Registration Sid of Sole Proprietor Brand.
    try {
      MessagingV1BrandRegistrationsBrandRegistrationOtp result = apiInstance.createBrandRegistrationOtp(brandRegistrationSid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MessagingV1BrandRegistrationOtpApi#createBrandRegistrationOtp");
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
| **brandRegistrationSid** | **String**| Brand Registration Sid of Sole Proprietor Brand. | |

### Return type

[**MessagingV1BrandRegistrationsBrandRegistrationOtp**](MessagingV1BrandRegistrationsBrandRegistrationOtp.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |

