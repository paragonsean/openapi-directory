# WebhookTestsApi

All URIs are relative to *http://app.files.com/api/rest/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**postWebhookTests**](WebhookTestsApi.md#postWebhookTests) | **POST** /webhook_tests | Create Webhook Test |


<a id="postWebhookTests"></a>
# **postWebhookTests**
> WebhookTestEntity postWebhookTests(url, action, body, encoding, fileAsBody, fileFormField, headers, method, rawBody)

Create Webhook Test

Create Webhook Test

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WebhookTestsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://app.files.com/api/rest/v1");

    WebhookTestsApi apiInstance = new WebhookTestsApi(defaultClient);
    String url = "url_example"; // String | URL for testing the webhook.
    String action = "action_example"; // String | action for test body
    Object body = null; // Object | Additional body parameters.
    String encoding = "encoding_example"; // String | HTTP encoding method.  Can be JSON, XML, or RAW (form data).
    Boolean fileAsBody = true; // Boolean | Send the file data as the request body?
    String fileFormField = "fileFormField_example"; // String | Send the file data as a named parameter in the request POST body
    Object headers = null; // Object | Additional request headers.
    String method = "method_example"; // String | HTTP method(GET or POST).
    String rawBody = "rawBody_example"; // String | raw body text
    try {
      WebhookTestEntity result = apiInstance.postWebhookTests(url, action, body, encoding, fileAsBody, fileFormField, headers, method, rawBody);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WebhookTestsApi#postWebhookTests");
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
| **url** | **String**| URL for testing the webhook. | |
| **action** | **String**| action for test body | [optional] |
| **body** | [**Object**](Object.md)| Additional body parameters. | [optional] |
| **encoding** | **String**| HTTP encoding method.  Can be JSON, XML, or RAW (form data). | [optional] |
| **fileAsBody** | **Boolean**| Send the file data as the request body? | [optional] |
| **fileFormField** | **String**| Send the file data as a named parameter in the request POST body | [optional] |
| **headers** | [**Object**](Object.md)| Additional request headers. | [optional] |
| **method** | **String**| HTTP method(GET or POST). | [optional] |
| **rawBody** | **String**| raw body text | [optional] |

### Return type

[**WebhookTestEntity**](WebhookTestEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The WebhookTests object. |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **405** | Method Not Allowed |  -  |
| **409** | Conflict |  -  |
| **412** | Precondition Failed |  -  |
| **422** | Unprocessable Entity |  -  |
| **423** | Locked |  -  |
| **429** | Too Many Requests |  -  |

