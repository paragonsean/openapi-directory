# TemplatesApiApi

All URIs are relative to *http://api.postmarkapp.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**pushTemplates**](TemplatesApiApi.md#pushTemplates) | **PUT** /templates/push | Push templates from one server to another |


<a id="pushTemplates"></a>
# **pushTemplates**
> TemplatesPushResponse pushTemplates(xPostmarkAccountToken, body)

Push templates from one server to another

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TemplatesApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.postmarkapp.com");

    TemplatesApiApi apiInstance = new TemplatesApiApi(defaultClient);
    String xPostmarkAccountToken = "xPostmarkAccountToken_example"; // String | The token associated with the Account on which this request will operate.
    TemplatesPushModel body = new TemplatesPushModel(); // TemplatesPushModel | 
    try {
      TemplatesPushResponse result = apiInstance.pushTemplates(xPostmarkAccountToken, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TemplatesApiApi#pushTemplates");
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
| **xPostmarkAccountToken** | **String**| The token associated with the Account on which this request will operate. | |
| **body** | [**TemplatesPushModel**](TemplatesPushModel.md)|  | |

### Return type

[**TemplatesPushResponse**](TemplatesPushResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | ok |  -  |
| **422** | An error was generated due to incorrect use of the API. See the Message associated with this response for more information. |  -  |
| **500** | Indicates an internal server error occurred. |  -  |

