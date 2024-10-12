# SendingApiApi

All URIs are relative to *http://api.postmarkapp.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**sendEmail**](SendingApiApi.md#sendEmail) | **POST** /email | Send a single email |
| [**sendEmailBatch**](SendingApiApi.md#sendEmailBatch) | **POST** /email/batch | Send a batch of emails |
| [**sendEmailBatchWithTemplates**](SendingApiApi.md#sendEmailBatchWithTemplates) | **POST** /email/batchWithTemplates | Send a batch of email using templates. |
| [**sendEmailWithTemplate**](SendingApiApi.md#sendEmailWithTemplate) | **POST** /email/withTemplate | Send an email using a Template |


<a id="sendEmail"></a>
# **sendEmail**
> SendEmailResponse sendEmail(xPostmarkServerToken, body)

Send a single email

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SendingApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.postmarkapp.com");

    SendingApiApi apiInstance = new SendingApiApi(defaultClient);
    String xPostmarkServerToken = "xPostmarkServerToken_example"; // String | The token associated with the Server on which this request will operate.
    SendEmailRequest body = new SendEmailRequest(); // SendEmailRequest | 
    try {
      SendEmailResponse result = apiInstance.sendEmail(xPostmarkServerToken, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SendingApiApi#sendEmail");
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
| **xPostmarkServerToken** | **String**| The token associated with the Server on which this request will operate. | |
| **body** | [**SendEmailRequest**](SendEmailRequest.md)|  | [optional] |

### Return type

[**SendEmailResponse**](SendEmailResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **422** | An error was generated due to incorrect use of the API. See the Message associated with this response for more information. |  -  |
| **500** | Indicates an internal server error occurred. |  -  |

<a id="sendEmailBatch"></a>
# **sendEmailBatch**
> List&lt;SendEmailResponse&gt; sendEmailBatch(xPostmarkServerToken, body)

Send a batch of emails

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SendingApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.postmarkapp.com");

    SendingApiApi apiInstance = new SendingApiApi(defaultClient);
    String xPostmarkServerToken = "xPostmarkServerToken_example"; // String | The token associated with the Server on which this request will operate.
    List<SendEmailRequest> body = Arrays.asList(); // List<SendEmailRequest> | 
    try {
      List<SendEmailResponse> result = apiInstance.sendEmailBatch(xPostmarkServerToken, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SendingApiApi#sendEmailBatch");
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
| **xPostmarkServerToken** | **String**| The token associated with the Server on which this request will operate. | |
| **body** | [**List&lt;SendEmailRequest&gt;**](SendEmailRequest.md)|  | [optional] |

### Return type

[**List&lt;SendEmailResponse&gt;**](SendEmailResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **422** | An error was generated due to incorrect use of the API. See the Message associated with this response for more information. |  -  |
| **500** | Indicates an internal server error occurred. |  -  |

<a id="sendEmailBatchWithTemplates"></a>
# **sendEmailBatchWithTemplates**
> List&lt;SendEmailResponse&gt; sendEmailBatchWithTemplates(xPostmarkServerToken, body)

Send a batch of email using templates.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SendingApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.postmarkapp.com");

    SendingApiApi apiInstance = new SendingApiApi(defaultClient);
    String xPostmarkServerToken = "xPostmarkServerToken_example"; // String | The token associated with the Server on which this request will operate.
    SendEmailTemplatedBatchRequest body = new SendEmailTemplatedBatchRequest(); // SendEmailTemplatedBatchRequest | 
    try {
      List<SendEmailResponse> result = apiInstance.sendEmailBatchWithTemplates(xPostmarkServerToken, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SendingApiApi#sendEmailBatchWithTemplates");
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
| **xPostmarkServerToken** | **String**| The token associated with the Server on which this request will operate. | |
| **body** | [**SendEmailTemplatedBatchRequest**](SendEmailTemplatedBatchRequest.md)|  | |

### Return type

[**List&lt;SendEmailResponse&gt;**](SendEmailResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **422** | An error was generated due to incorrect use of the API. See the Message associated with this response for more information. |  -  |
| **500** | Indicates an internal server error occurred. |  -  |

<a id="sendEmailWithTemplate"></a>
# **sendEmailWithTemplate**
> SendEmailResponse sendEmailWithTemplate(xPostmarkServerToken, body)

Send an email using a Template

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SendingApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.postmarkapp.com");

    SendingApiApi apiInstance = new SendingApiApi(defaultClient);
    String xPostmarkServerToken = "xPostmarkServerToken_example"; // String | The token associated with the Server on which this request will operate.
    EmailWithTemplateRequest body = new EmailWithTemplateRequest(); // EmailWithTemplateRequest | 
    try {
      SendEmailResponse result = apiInstance.sendEmailWithTemplate(xPostmarkServerToken, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SendingApiApi#sendEmailWithTemplate");
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
| **xPostmarkServerToken** | **String**| The token associated with the Server on which this request will operate. | |
| **body** | [**EmailWithTemplateRequest**](EmailWithTemplateRequest.md)|  | |

### Return type

[**SendEmailResponse**](SendEmailResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **422** | An error was generated due to incorrect use of the API. See the Message associated with this response for more information. |  -  |
| **500** | Indicates an internal server error occurred. |  -  |

