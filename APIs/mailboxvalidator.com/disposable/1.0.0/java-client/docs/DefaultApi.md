# DefaultApi

All URIs are relative to *https://virtserver.swaggerhub.com/mailboxvalidator/MailboxValidator-Disposable-Email-Checker/1.0.0*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**v1EmailDisposableGet**](DefaultApi.md#v1EmailDisposableGet) | **GET** /v1/email/disposable |  |


<a id="v1EmailDisposableGet"></a>
# **v1EmailDisposableGet**
> String v1EmailDisposableGet(email, key, format)



The Disposable Email Checker API does checking on a single email address and returns if it is from a disposable email provider in either JSON or XML format.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://virtserver.swaggerhub.com/mailboxvalidator/MailboxValidator-Disposable-Email-Checker/1.0.0");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String email = "email_example"; // String | The email address to check if is from a disposable email provider.
    String key = "key_example"; // String | API key.
    String format = "json"; // String | Return the result in json (default) or xml format.
    try {
      String result = apiInstance.v1EmailDisposableGet(email, key, format);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#v1EmailDisposableGet");
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
| **email** | **String**| The email address to check if is from a disposable email provider. | |
| **key** | **String**| API key. | |
| **format** | **String**| Return the result in json (default) or xml format. | [optional] [enum: json, xml] |

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | disposable email checker response |  -  |

