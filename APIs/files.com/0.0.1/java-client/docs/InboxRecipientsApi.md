# InboxRecipientsApi

All URIs are relative to *http://app.files.com/api/rest/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getInboxRecipients**](InboxRecipientsApi.md#getInboxRecipients) | **GET** /inbox_recipients | List Inbox Recipients |
| [**postInboxRecipients**](InboxRecipientsApi.md#postInboxRecipients) | **POST** /inbox_recipients | Create Inbox Recipient |


<a id="getInboxRecipients"></a>
# **getInboxRecipients**
> List&lt;InboxRecipientEntity&gt; getInboxRecipients(inboxId, cursor, perPage, sortBy, filter)

List Inbox Recipients

List Inbox Recipients

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InboxRecipientsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://app.files.com/api/rest/v1");

    InboxRecipientsApi apiInstance = new InboxRecipientsApi(defaultClient);
    Integer inboxId = 56; // Integer | List recipients for the inbox with this ID.
    String cursor = "cursor_example"; // String | Used for pagination.  When a list request has more records available, cursors are provided in the response headers `X-Files-Cursor-Next` and `X-Files-Cursor-Prev`.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination.
    Integer perPage = 56; // Integer | Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended).
    Object sortBy = null; // Object | If set, sort records by the specified field in either `asc` or `desc` direction (e.g. `sort_by[has_registrations]=desc`). Valid fields are `has_registrations`.
    Object filter = null; // Object | If set, return records where the specified field is equal to the supplied value. Valid fields are `has_registrations`.
    try {
      List<InboxRecipientEntity> result = apiInstance.getInboxRecipients(inboxId, cursor, perPage, sortBy, filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InboxRecipientsApi#getInboxRecipients");
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
| **inboxId** | **Integer**| List recipients for the inbox with this ID. | |
| **cursor** | **String**| Used for pagination.  When a list request has more records available, cursors are provided in the response headers &#x60;X-Files-Cursor-Next&#x60; and &#x60;X-Files-Cursor-Prev&#x60;.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination. | [optional] |
| **perPage** | **Integer**| Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended). | [optional] |
| **sortBy** | [**Object**](.md)| If set, sort records by the specified field in either &#x60;asc&#x60; or &#x60;desc&#x60; direction (e.g. &#x60;sort_by[has_registrations]&#x3D;desc&#x60;). Valid fields are &#x60;has_registrations&#x60;. | [optional] |
| **filter** | [**Object**](.md)| If set, return records where the specified field is equal to the supplied value. Valid fields are &#x60;has_registrations&#x60;. | [optional] |

### Return type

[**List&lt;InboxRecipientEntity&gt;**](InboxRecipientEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of InboxRecipients objects. |  -  |
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

<a id="postInboxRecipients"></a>
# **postInboxRecipients**
> InboxRecipientEntity postInboxRecipients(inboxId, recipient, company, name, note, shareAfterCreate)

Create Inbox Recipient

Create Inbox Recipient

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InboxRecipientsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://app.files.com/api/rest/v1");

    InboxRecipientsApi apiInstance = new InboxRecipientsApi(defaultClient);
    Integer inboxId = 56; // Integer | Inbox to share.
    String recipient = "recipient_example"; // String | Email address to share this inbox with.
    String company = "company_example"; // String | Company of recipient.
    String name = "name_example"; // String | Name of recipient.
    String note = "note_example"; // String | Note to include in email.
    Boolean shareAfterCreate = true; // Boolean | Set to true to share the link with the recipient upon creation.
    try {
      InboxRecipientEntity result = apiInstance.postInboxRecipients(inboxId, recipient, company, name, note, shareAfterCreate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InboxRecipientsApi#postInboxRecipients");
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
| **inboxId** | **Integer**| Inbox to share. | |
| **recipient** | **String**| Email address to share this inbox with. | |
| **company** | **String**| Company of recipient. | [optional] |
| **name** | **String**| Name of recipient. | [optional] |
| **note** | **String**| Note to include in email. | [optional] |
| **shareAfterCreate** | **Boolean**| Set to true to share the link with the recipient upon creation. | [optional] |

### Return type

[**InboxRecipientEntity**](InboxRecipientEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The InboxRecipients object. |  -  |
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

