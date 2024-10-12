# ActionNotificationExportsApi

All URIs are relative to *http://app.files.com/api/rest/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getActionNotificationExportsId**](ActionNotificationExportsApi.md#getActionNotificationExportsId) | **GET** /action_notification_exports/{id} | Show Action Notification Export |
| [**postActionNotificationExports**](ActionNotificationExportsApi.md#postActionNotificationExports) | **POST** /action_notification_exports | Create Action Notification Export |


<a id="getActionNotificationExportsId"></a>
# **getActionNotificationExportsId**
> ActionNotificationExportEntity getActionNotificationExportsId(id)

Show Action Notification Export

Show Action Notification Export

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActionNotificationExportsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://app.files.com/api/rest/v1");

    ActionNotificationExportsApi apiInstance = new ActionNotificationExportsApi(defaultClient);
    Integer id = 56; // Integer | Action Notification Export ID.
    try {
      ActionNotificationExportEntity result = apiInstance.getActionNotificationExportsId(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActionNotificationExportsApi#getActionNotificationExportsId");
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
| **id** | **Integer**| Action Notification Export ID. | |

### Return type

[**ActionNotificationExportEntity**](ActionNotificationExportEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The ActionNotificationExports object. |  -  |
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

<a id="postActionNotificationExports"></a>
# **postActionNotificationExports**
> ActionNotificationExportEntity postActionNotificationExports(endAt, queryFolder, queryMessage, queryPath, queryRequestMethod, queryRequestUrl, queryStatus, querySuccess, startAt, userId)

Create Action Notification Export

Create Action Notification Export

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActionNotificationExportsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://app.files.com/api/rest/v1");

    ActionNotificationExportsApi apiInstance = new ActionNotificationExportsApi(defaultClient);
    OffsetDateTime endAt = OffsetDateTime.now(); // OffsetDateTime | End date/time of export range.
    String queryFolder = "queryFolder_example"; // String | Return notifications that were triggered by actions in this folder.
    String queryMessage = "queryMessage_example"; // String | Error message associated with the request, if any.
    String queryPath = "queryPath_example"; // String | Return notifications that were triggered by actions on this specific path.
    String queryRequestMethod = "queryRequestMethod_example"; // String | The HTTP request method used by the webhook.
    String queryRequestUrl = "queryRequestUrl_example"; // String | The target webhook URL.
    String queryStatus = "queryStatus_example"; // String | The HTTP status returned from the server in response to the webhook request.
    Boolean querySuccess = true; // Boolean | true if the webhook request succeeded (i.e. returned a 200 or 204 response status). false otherwise.
    OffsetDateTime startAt = OffsetDateTime.now(); // OffsetDateTime | Start date/time of export range.
    Integer userId = 56; // Integer | User ID.  Provide a value of `0` to operate the current session's user.
    try {
      ActionNotificationExportEntity result = apiInstance.postActionNotificationExports(endAt, queryFolder, queryMessage, queryPath, queryRequestMethod, queryRequestUrl, queryStatus, querySuccess, startAt, userId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActionNotificationExportsApi#postActionNotificationExports");
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
| **endAt** | **OffsetDateTime**| End date/time of export range. | [optional] |
| **queryFolder** | **String**| Return notifications that were triggered by actions in this folder. | [optional] |
| **queryMessage** | **String**| Error message associated with the request, if any. | [optional] |
| **queryPath** | **String**| Return notifications that were triggered by actions on this specific path. | [optional] |
| **queryRequestMethod** | **String**| The HTTP request method used by the webhook. | [optional] |
| **queryRequestUrl** | **String**| The target webhook URL. | [optional] |
| **queryStatus** | **String**| The HTTP status returned from the server in response to the webhook request. | [optional] |
| **querySuccess** | **Boolean**| true if the webhook request succeeded (i.e. returned a 200 or 204 response status). false otherwise. | [optional] |
| **startAt** | **OffsetDateTime**| Start date/time of export range. | [optional] |
| **userId** | **Integer**| User ID.  Provide a value of &#x60;0&#x60; to operate the current session&#39;s user. | [optional] |

### Return type

[**ActionNotificationExportEntity**](ActionNotificationExportEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The ActionNotificationExports object. |  -  |
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

