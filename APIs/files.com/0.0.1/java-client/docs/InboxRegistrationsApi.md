# InboxRegistrationsApi

All URIs are relative to *http://app.files.com/api/rest/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getInboxRegistrations**](InboxRegistrationsApi.md#getInboxRegistrations) | **GET** /inbox_registrations | List Inbox Registrations |


<a id="getInboxRegistrations"></a>
# **getInboxRegistrations**
> List&lt;InboxRegistrationEntity&gt; getInboxRegistrations(cursor, perPage, folderBehaviorId)

List Inbox Registrations

List Inbox Registrations

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InboxRegistrationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://app.files.com/api/rest/v1");

    InboxRegistrationsApi apiInstance = new InboxRegistrationsApi(defaultClient);
    String cursor = "cursor_example"; // String | Used for pagination.  When a list request has more records available, cursors are provided in the response headers `X-Files-Cursor-Next` and `X-Files-Cursor-Prev`.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination.
    Integer perPage = 56; // Integer | Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended).
    Integer folderBehaviorId = 56; // Integer | ID of the associated Inbox.
    try {
      List<InboxRegistrationEntity> result = apiInstance.getInboxRegistrations(cursor, perPage, folderBehaviorId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InboxRegistrationsApi#getInboxRegistrations");
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
| **cursor** | **String**| Used for pagination.  When a list request has more records available, cursors are provided in the response headers &#x60;X-Files-Cursor-Next&#x60; and &#x60;X-Files-Cursor-Prev&#x60;.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination. | [optional] |
| **perPage** | **Integer**| Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended). | [optional] |
| **folderBehaviorId** | **Integer**| ID of the associated Inbox. | [optional] |

### Return type

[**List&lt;InboxRegistrationEntity&gt;**](InboxRegistrationEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of InboxRegistrations objects. |  -  |
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

