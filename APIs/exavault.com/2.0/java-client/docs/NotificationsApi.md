# NotificationsApi

All URIs are relative to *https://accountname.exavault.com/api/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addNotification**](NotificationsApi.md#addNotification) | **POST** /notifications | Create a new notification |
| [**deleteNotificationById**](NotificationsApi.md#deleteNotificationById) | **DELETE** /notifications/{id} | Delete a notification |
| [**getNotificationById**](NotificationsApi.md#getNotificationById) | **GET** /notifications/{id} | Get notification details |
| [**listNotifications**](NotificationsApi.md#listNotifications) | **GET** /notifications | Get a list of notifications |
| [**updateNotificationById**](NotificationsApi.md#updateNotificationById) | **PATCH** /notifications/{id} | Update a notification |


<a id="addNotification"></a>
# **addNotification**
> NotificationResponse addNotification(evApiKey, evAccessToken, addNotificationRequestBody)

Create a new notification

Create a new notification for a [resource](#section/Identifying-Resources) in your account. Notifications can be sent via email or webhook;  - To enable email, pass an array of email addresses to the &#x60;recipients&#x60; parameter of this call.  - To enable webhooks, setup the webhook callback URL in your account settings via [PATCH /account](#operation/updateAccount).   **Notes:**   - Authenticated user should have [notifications permission](/docs/account/04-users/00-introduction#managing-user-roles-and-permissions) 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NotificationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://accountname.exavault.com/api/v2");

    NotificationsApi apiInstance = new NotificationsApi(defaultClient);
    String evApiKey = "evApiKey_example"; // String | API Key required to make API call. 
    String evAccessToken = "5dc97cc607985eb8da033220e7447647e7915fbf73808"; // String | Access token required to make the API call.
    AddNotificationRequestBody addNotificationRequestBody = new AddNotificationRequestBody(); // AddNotificationRequestBody | 
    try {
      NotificationResponse result = apiInstance.addNotification(evApiKey, evAccessToken, addNotificationRequestBody);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NotificationsApi#addNotification");
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
| **evApiKey** | **String**| API Key required to make API call.  | |
| **evAccessToken** | **String**| Access token required to make the API call. | |
| **addNotificationRequestBody** | [**AddNotificationRequestBody**](AddNotificationRequestBody.md)|  | [optional] |

### Return type

[**NotificationResponse**](NotificationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Successful Operation |  -  |

<a id="deleteNotificationById"></a>
# **deleteNotificationById**
> EmptyResponse deleteNotificationById(evApiKey, evAccessToken, id)

Delete a notification

Deletes a notification. Note that deleting a notification _only_ deletes the notification &amp;ndash; it does not delete any underlying files or folders.  **Notes:**  - You need to have the [notifications permission](/docs/account/04-users/00-introduction#managing-user-roles-and-permissions) to update a notification. - You can only delete notifications owned by your user account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NotificationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://accountname.exavault.com/api/v2");

    NotificationsApi apiInstance = new NotificationsApi(defaultClient);
    String evApiKey = "evApiKey_example"; // String | API Key required to make the API call.
    String evAccessToken = "5dc97cc607985eb8da033220e7447647e7915fbf73808"; // String | Access token required to make the API call.
    Integer id = 3; // Integer | ID of the notification. Use [GET /notifications](#operation/listNotifications) if you need to lookup an ID.
    try {
      EmptyResponse result = apiInstance.deleteNotificationById(evApiKey, evAccessToken, id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NotificationsApi#deleteNotificationById");
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
| **evApiKey** | **String**| API Key required to make the API call. | |
| **evAccessToken** | **String**| Access token required to make the API call. | |
| **id** | **Integer**| ID of the notification. Use [GET /notifications](#operation/listNotifications) if you need to lookup an ID. | |

### Return type

[**EmptyResponse**](EmptyResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Operation |  -  |

<a id="getNotificationById"></a>
# **getNotificationById**
> NotificationResponse getNotificationById(evApiKey, evAccessToken, id, include)

Get notification details

Get the details for a notification with a specific ID number. You&#39;ll be able to review its path, triggers and who&#39;s getting the notification.   **Notes**  - You need to have the [notifications permission](/docs/account/04-users/00-introduction#managing-user-roles-and-permissions) to view the detail for a notification. - You can only retrieve notifications owned by your user account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NotificationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://accountname.exavault.com/api/v2");

    NotificationsApi apiInstance = new NotificationsApi(defaultClient);
    String evApiKey = "evApiKey_example"; // String | API Key required to make the API call.
    String evAccessToken = "5dc97cc607985eb8da033220e7447647e7915fbf73808"; // String | Access token required to make the API call.
    Integer id = 3; // Integer | ID of the notification. Use [GET /notifications](#operation/listNotifications) if you need to lookup an ID.
    String include = "resource,share"; // String | Related record types to include in the response. You can include multiple types by separating them with commas. Valid options are **ownerUser**, **resource**, and **share**.
    try {
      NotificationResponse result = apiInstance.getNotificationById(evApiKey, evAccessToken, id, include);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NotificationsApi#getNotificationById");
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
| **evApiKey** | **String**| API Key required to make the API call. | |
| **evAccessToken** | **String**| Access token required to make the API call. | |
| **id** | **Integer**| ID of the notification. Use [GET /notifications](#operation/listNotifications) if you need to lookup an ID. | |
| **include** | **String**| Related record types to include in the response. You can include multiple types by separating them with commas. Valid options are **ownerUser**, **resource**, and **share**. | [optional] |

### Return type

[**NotificationResponse**](NotificationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Operation |  -  |

<a id="listNotifications"></a>
# **listNotifications**
> NotificationCollectionResponse listNotifications(evApiKey, evAccessToken, type, offset, sort, limit, include, action)

Get a list of notifications

Get a list of all the [notifications](/docs/account/06-notifications) you have access to. You can use sorting and filtering to limit the returned list.  **Notes:**   - Authenticated user should have [notifications permission](/docs/account/04-users/00-introduction#managing-user-roles-and-permissions)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NotificationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://accountname.exavault.com/api/v2");

    NotificationsApi apiInstance = new NotificationsApi(defaultClient);
    String evApiKey = "evApiKey_example"; // String | API Key required to make the API call. 
    String evAccessToken = "5dc97cc607985eb8da033220e7447647e7915fbf73808"; // String | Access token required to make the API call.
    String type = "file"; // String | Type of notification include in the list. Valid options are **file**, **folder**, **send_receipt**, **share_receipt**, **file_drop**  If this parameter is not used, only **file** and **folder** type notifications are included in the list.
    Integer offset = 0; // Integer | Starting notification record in the result set. Can be used for pagination.
    String sort = "date"; // String | What order the list of matches should be in. Valid sort fields are **resourcename**, **date**, **action** and **type**. The sort order for each sort field is ascending unless it is prefixed with a minus (“-“), in which case it will be descending.  You can chose multiple options for the sort by separating them with commmas, such as \"type,-date\" to sort by type, then most recent.
    Integer limit = 25; // Integer | Number of notification records to return. Can be used for pagination.
    String include = "resource"; // String | Related records to include in the response. Valid options are **ownerUser**, **resource**, **share**
    String action = "connect"; // String | The kind of action which triggers the notification. Valid choices are **connect** (only for delivery receipts), **download**, **upload**, **delete**, or **all**   **Note** The **all** action matches notifications set to \"all\", not all notifications. For example, notifications set to trigger only on delete are not included if you filter for action=all
    try {
      NotificationCollectionResponse result = apiInstance.listNotifications(evApiKey, evAccessToken, type, offset, sort, limit, include, action);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NotificationsApi#listNotifications");
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
| **evApiKey** | **String**| API Key required to make the API call.  | |
| **evAccessToken** | **String**| Access token required to make the API call. | |
| **type** | **String**| Type of notification include in the list. Valid options are **file**, **folder**, **send_receipt**, **share_receipt**, **file_drop**  If this parameter is not used, only **file** and **folder** type notifications are included in the list. | [optional] [enum: file, folder, shared_folder, send_receipt, share_receipt, file_drop] |
| **offset** | **Integer**| Starting notification record in the result set. Can be used for pagination. | [optional] [default to 0] |
| **sort** | **String**| What order the list of matches should be in. Valid sort fields are **resourcename**, **date**, **action** and **type**. The sort order for each sort field is ascending unless it is prefixed with a minus (“-“), in which case it will be descending.  You can chose multiple options for the sort by separating them with commmas, such as \&quot;type,-date\&quot; to sort by type, then most recent. | [optional] |
| **limit** | **Integer**| Number of notification records to return. Can be used for pagination. | [optional] [default to 25] |
| **include** | **String**| Related records to include in the response. Valid options are **ownerUser**, **resource**, **share** | [optional] [enum: resource, share, user] |
| **action** | **String**| The kind of action which triggers the notification. Valid choices are **connect** (only for delivery receipts), **download**, **upload**, **delete**, or **all**   **Note** The **all** action matches notifications set to \&quot;all\&quot;, not all notifications. For example, notifications set to trigger only on delete are not included if you filter for action&#x3D;all | [optional] [enum: connect, download, upload, delete, all] |

### Return type

[**NotificationCollectionResponse**](NotificationCollectionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Operation |  -  |

<a id="updateNotificationById"></a>
# **updateNotificationById**
> NotificationResponse updateNotificationById(evApiKey, evAccessToken, id, updateNotificationByIdRequestBody)

Update a notification

Update an existing notification. You can add additional emails or change the action or users that cause a notification to trigger.   When updating recipient emails, make sure your &#x60;recipients&#x60; parameter contains the full list of people who should be included on the notification. If you resend the list without an existing recipient, they will be deleted from the notification emails.   **Notes:**  - You need to have the [notifications permission](/docs/account/04-users/00-introduction#managing-user-roles-and-permissions) to update a notification. - You can only change notifications owned by your user account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NotificationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://accountname.exavault.com/api/v2");

    NotificationsApi apiInstance = new NotificationsApi(defaultClient);
    String evApiKey = "evApiKey_example"; // String | API Key required to make the API call.
    String evAccessToken = "5dc97cc607985eb8da033220e7447647e7915fbf73808"; // String | Access token required to make the API call.
    Integer id = 3; // Integer | ID of the notification. Use [GET /notifications](#operation/listNotifications) if you need to lookup an ID.
    UpdateNotificationByIdRequestBody updateNotificationByIdRequestBody = new UpdateNotificationByIdRequestBody(); // UpdateNotificationByIdRequestBody | 
    try {
      NotificationResponse result = apiInstance.updateNotificationById(evApiKey, evAccessToken, id, updateNotificationByIdRequestBody);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NotificationsApi#updateNotificationById");
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
| **evApiKey** | **String**| API Key required to make the API call. | |
| **evAccessToken** | **String**| Access token required to make the API call. | |
| **id** | **Integer**| ID of the notification. Use [GET /notifications](#operation/listNotifications) if you need to lookup an ID. | |
| **updateNotificationByIdRequestBody** | [**UpdateNotificationByIdRequestBody**](UpdateNotificationByIdRequestBody.md)|  | [optional] |

### Return type

[**NotificationResponse**](NotificationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Operation |  -  |

