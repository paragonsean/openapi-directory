# EmailValidationApi

All URIs are relative to *https://ipqualityscore.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**emailValidation**](EmailValidationApi.md#emailValidation) | **GET** /json/email/{YOUR_API_KEY_HERE}/{USER_EMAIL_HERE} | Email Validation |


<a id="emailValidation"></a>
# **emailValidation**
> EmailValidation200Response emailValidation(YOUR_API_KEY_HERE, USER_EMAIL_HERE)

Email Validation

Email Validation

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EmailValidationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ipqualityscore.com/api");

    EmailValidationApi apiInstance = new EmailValidationApi(defaultClient);
    String YOUR_API_KEY_HERE = "asd24#sdfs322#"; // String | (Required) YOUR_API_KEY_HERE
    String USER_EMAIL_HERE = "example@example.com"; // String | (Required) USER_EMAIL_HERE
    try {
      EmailValidation200Response result = apiInstance.emailValidation(YOUR_API_KEY_HERE, USER_EMAIL_HERE);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EmailValidationApi#emailValidation");
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
| **USER_EMAIL_HERE** | **String**| (Required) USER_EMAIL_HERE | |

### Return type

[**EmailValidation200Response**](EmailValidation200Response.md)

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

