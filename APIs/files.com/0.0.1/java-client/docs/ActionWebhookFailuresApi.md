# ActionWebhookFailuresApi

All URIs are relative to *http://app.files.com/api/rest/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**postActionWebhookFailuresIdRetry**](ActionWebhookFailuresApi.md#postActionWebhookFailuresIdRetry) | **POST** /action_webhook_failures/{id}/retry | retry Action Webhook Failure |


<a id="postActionWebhookFailuresIdRetry"></a>
# **postActionWebhookFailuresIdRetry**
> postActionWebhookFailuresIdRetry(id)

retry Action Webhook Failure

retry Action Webhook Failure

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActionWebhookFailuresApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://app.files.com/api/rest/v1");

    ActionWebhookFailuresApi apiInstance = new ActionWebhookFailuresApi(defaultClient);
    Integer id = 56; // Integer | Action Webhook Failure ID.
    try {
      apiInstance.postActionWebhookFailuresIdRetry(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActionWebhookFailuresApi#postActionWebhookFailuresIdRetry");
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
| **id** | **Integer**| Action Webhook Failure ID. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The ActionWebhookFailures object. |  -  |
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

