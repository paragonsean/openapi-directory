# BundleNotificationsApi

All URIs are relative to *http://app.files.com/api/rest/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**deleteBundleNotificationsId**](BundleNotificationsApi.md#deleteBundleNotificationsId) | **DELETE** /bundle_notifications/{id} | Delete Bundle Notification |
| [**getBundleNotifications**](BundleNotificationsApi.md#getBundleNotifications) | **GET** /bundle_notifications | List Bundle Notifications |
| [**getBundleNotificationsId**](BundleNotificationsApi.md#getBundleNotificationsId) | **GET** /bundle_notifications/{id} | Show Bundle Notification |
| [**patchBundleNotificationsId**](BundleNotificationsApi.md#patchBundleNotificationsId) | **PATCH** /bundle_notifications/{id} | Update Bundle Notification |
| [**postBundleNotifications**](BundleNotificationsApi.md#postBundleNotifications) | **POST** /bundle_notifications | Create Bundle Notification |


<a id="deleteBundleNotificationsId"></a>
# **deleteBundleNotificationsId**
> deleteBundleNotificationsId(id)

Delete Bundle Notification

Delete Bundle Notification

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BundleNotificationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://app.files.com/api/rest/v1");

    BundleNotificationsApi apiInstance = new BundleNotificationsApi(defaultClient);
    Integer id = 56; // Integer | Bundle Notification ID.
    try {
      apiInstance.deleteBundleNotificationsId(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling BundleNotificationsApi#deleteBundleNotificationsId");
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
| **id** | **Integer**| Bundle Notification ID. | |

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
| **204** | No body. |  -  |
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

<a id="getBundleNotifications"></a>
# **getBundleNotifications**
> List&lt;BundleNotificationEntity&gt; getBundleNotifications(userId, cursor, perPage, sortBy, bundleId, filter)

List Bundle Notifications

List Bundle Notifications

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BundleNotificationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://app.files.com/api/rest/v1");

    BundleNotificationsApi apiInstance = new BundleNotificationsApi(defaultClient);
    Integer userId = 56; // Integer | User ID.  Provide a value of `0` to operate the current session's user.
    String cursor = "cursor_example"; // String | Used for pagination.  When a list request has more records available, cursors are provided in the response headers `X-Files-Cursor-Next` and `X-Files-Cursor-Prev`.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination.
    Integer perPage = 56; // Integer | Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended).
    Object sortBy = null; // Object | If set, sort records by the specified field in either `asc` or `desc` direction (e.g. `sort_by[bundle_id]=desc`). Valid fields are `bundle_id`.
    String bundleId = "bundleId_example"; // String | If set, return records where the specified field is equal to the supplied value.
    Object filter = null; // Object | If set, return records where the specified field is equal to the supplied value. Valid fields are `bundle_id`.
    try {
      List<BundleNotificationEntity> result = apiInstance.getBundleNotifications(userId, cursor, perPage, sortBy, bundleId, filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BundleNotificationsApi#getBundleNotifications");
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
| **userId** | **Integer**| User ID.  Provide a value of &#x60;0&#x60; to operate the current session&#39;s user. | [optional] |
| **cursor** | **String**| Used for pagination.  When a list request has more records available, cursors are provided in the response headers &#x60;X-Files-Cursor-Next&#x60; and &#x60;X-Files-Cursor-Prev&#x60;.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination. | [optional] |
| **perPage** | **Integer**| Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended). | [optional] |
| **sortBy** | [**Object**](.md)| If set, sort records by the specified field in either &#x60;asc&#x60; or &#x60;desc&#x60; direction (e.g. &#x60;sort_by[bundle_id]&#x3D;desc&#x60;). Valid fields are &#x60;bundle_id&#x60;. | [optional] |
| **bundleId** | **String**| If set, return records where the specified field is equal to the supplied value. | [optional] |
| **filter** | [**Object**](.md)| If set, return records where the specified field is equal to the supplied value. Valid fields are &#x60;bundle_id&#x60;. | [optional] |

### Return type

[**List&lt;BundleNotificationEntity&gt;**](BundleNotificationEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of BundleNotifications objects. |  -  |
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

<a id="getBundleNotificationsId"></a>
# **getBundleNotificationsId**
> BundleNotificationEntity getBundleNotificationsId(id)

Show Bundle Notification

Show Bundle Notification

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BundleNotificationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://app.files.com/api/rest/v1");

    BundleNotificationsApi apiInstance = new BundleNotificationsApi(defaultClient);
    Integer id = 56; // Integer | Bundle Notification ID.
    try {
      BundleNotificationEntity result = apiInstance.getBundleNotificationsId(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BundleNotificationsApi#getBundleNotificationsId");
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
| **id** | **Integer**| Bundle Notification ID. | |

### Return type

[**BundleNotificationEntity**](BundleNotificationEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The BundleNotifications object. |  -  |
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

<a id="patchBundleNotificationsId"></a>
# **patchBundleNotificationsId**
> BundleNotificationEntity patchBundleNotificationsId(id, notifyOnRegistration, notifyOnUpload)

Update Bundle Notification

Update Bundle Notification

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BundleNotificationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://app.files.com/api/rest/v1");

    BundleNotificationsApi apiInstance = new BundleNotificationsApi(defaultClient);
    Integer id = 56; // Integer | Bundle Notification ID.
    Boolean notifyOnRegistration = true; // Boolean | Triggers bundle notification when a registration action occurs for it.
    Boolean notifyOnUpload = true; // Boolean | Triggers bundle notification when a upload action occurs for it.
    try {
      BundleNotificationEntity result = apiInstance.patchBundleNotificationsId(id, notifyOnRegistration, notifyOnUpload);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BundleNotificationsApi#patchBundleNotificationsId");
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
| **id** | **Integer**| Bundle Notification ID. | |
| **notifyOnRegistration** | **Boolean**| Triggers bundle notification when a registration action occurs for it. | [optional] |
| **notifyOnUpload** | **Boolean**| Triggers bundle notification when a upload action occurs for it. | [optional] |

### Return type

[**BundleNotificationEntity**](BundleNotificationEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The BundleNotifications object. |  -  |
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

<a id="postBundleNotifications"></a>
# **postBundleNotifications**
> BundleNotificationEntity postBundleNotifications(bundleId, notifyOnRegistration, notifyOnUpload, userId)

Create Bundle Notification

Create Bundle Notification

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BundleNotificationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://app.files.com/api/rest/v1");

    BundleNotificationsApi apiInstance = new BundleNotificationsApi(defaultClient);
    Integer bundleId = 56; // Integer | Bundle ID to notify on
    Boolean notifyOnRegistration = true; // Boolean | Triggers bundle notification when a registration action occurs for it.
    Boolean notifyOnUpload = true; // Boolean | Triggers bundle notification when a upload action occurs for it.
    Integer userId = 56; // Integer | The id of the user to notify.
    try {
      BundleNotificationEntity result = apiInstance.postBundleNotifications(bundleId, notifyOnRegistration, notifyOnUpload, userId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BundleNotificationsApi#postBundleNotifications");
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
| **bundleId** | **Integer**| Bundle ID to notify on | |
| **notifyOnRegistration** | **Boolean**| Triggers bundle notification when a registration action occurs for it. | [optional] |
| **notifyOnUpload** | **Boolean**| Triggers bundle notification when a upload action occurs for it. | [optional] |
| **userId** | **Integer**| The id of the user to notify. | [optional] |

### Return type

[**BundleNotificationEntity**](BundleNotificationEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The BundleNotifications object. |  -  |
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

