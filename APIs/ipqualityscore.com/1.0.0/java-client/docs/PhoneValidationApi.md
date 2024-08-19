# PhoneValidationApi

All URIs are relative to *https://ipqualityscore.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**phoneValidation**](PhoneValidationApi.md#phoneValidation) | **GET** /json/phone/{YOUR_API_KEY_HERE}/{USER_PHONE_HERE} | Phone Validation |


<a id="phoneValidation"></a>
# **phoneValidation**
> PhoneValidation200Response phoneValidation(YOUR_API_KEY_HERE, USER_PHONE_HERE, country)

Phone Validation

Phone Validation

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PhoneValidationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ipqualityscore.com/api");

    PhoneValidationApi apiInstance = new PhoneValidationApi(defaultClient);
    String YOUR_API_KEY_HERE = "asd24#sdfs322#"; // String | (Required) YOUR_API_KEY_HERE
    String USER_PHONE_HERE = "18007132618"; // String | (Required) USER_PHONE_HERE
    String country = "UK"; // String | country
    try {
      PhoneValidation200Response result = apiInstance.phoneValidation(YOUR_API_KEY_HERE, USER_PHONE_HERE, country);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PhoneValidationApi#phoneValidation");
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
| **YOUR_API_KEY_HERE** | **String**| (Required) YOUR_API_KEY_HERE | |
| **USER_PHONE_HERE** | **String**| (Required) USER_PHONE_HERE | |
| **country** | **String**| country | [optional] |

### Return type

[**PhoneValidation200Response**](PhoneValidation200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |
| **400** | Bad Request |  -  |
| **500** | Unexpected error |  -  |

