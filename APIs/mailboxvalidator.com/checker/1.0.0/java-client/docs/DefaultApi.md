# DefaultApi

All URIs are relative to *https://api.mailboxvalidator.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**v1EmailFreeGet**](DefaultApi.md#v1EmailFreeGet) | **GET** /v1/email/free |  |


<a id="v1EmailFreeGet"></a>
# **v1EmailFreeGet**
> String v1EmailFreeGet(email, key, format)



The Free Email Checker API does validation on a single email address and returns if it is from a free email provider in either JSON or XML format.

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
    defaultClient.setBasePath("https://api.mailboxvalidator.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String email = "email_example"; // String | The email address to check if is from a free email provider.
    String key = "key_example"; // String | API key.
    String format = "json"; // String | Return the result in json (default) or xml format.
    try {
      String result = apiInstance.v1EmailFreeGet(email, key, format);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#v1EmailFreeGet");
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
| **email** | **String**| The email address to check if is from a free email provider. | |
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
| **200** | free email checker response |  -  |

