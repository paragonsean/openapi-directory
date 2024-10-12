# NumbersV1PortingPortabilityApi

All URIs are relative to *https://numbers.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**fetchPortingPortability**](NumbersV1PortingPortabilityApi.md#fetchPortingPortability) | **GET** /v1/Porting/Portability/PhoneNumber/{PhoneNumber} |  |


<a id="fetchPortingPortability"></a>
# **fetchPortingPortability**
> NumbersV1PortingPortability fetchPortingPortability(phoneNumber, targetAccountSid)



Allows to check if a single phone number can be ported to Twilio or not.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NumbersV1PortingPortabilityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://numbers.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    NumbersV1PortingPortabilityApi apiInstance = new NumbersV1PortingPortabilityApi(defaultClient);
    String phoneNumber = "phoneNumber_example"; // String | The phone number which portability is to be checked. Phone numbers are in E.164 format (e.g. +16175551212).
    String targetAccountSid = "targetAccountSid_example"; // String | The SID of the account where the phone number(s) will be ported.
    try {
      NumbersV1PortingPortability result = apiInstance.fetchPortingPortability(phoneNumber, targetAccountSid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NumbersV1PortingPortabilityApi#fetchPortingPortability");
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
| **phoneNumber** | **String**| The phone number which portability is to be checked. Phone numbers are in E.164 format (e.g. +16175551212). | |
| **targetAccountSid** | **String**| The SID of the account where the phone number(s) will be ported. | [optional] |

### Return type

[**NumbersV1PortingPortability**](NumbersV1PortingPortability.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

