# ClickwrapsApi

All URIs are relative to *http://app.files.com/api/rest/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**deleteClickwrapsId**](ClickwrapsApi.md#deleteClickwrapsId) | **DELETE** /clickwraps/{id} | Delete Clickwrap |
| [**getClickwraps**](ClickwrapsApi.md#getClickwraps) | **GET** /clickwraps | List Clickwraps |
| [**getClickwrapsId**](ClickwrapsApi.md#getClickwrapsId) | **GET** /clickwraps/{id} | Show Clickwrap |
| [**patchClickwrapsId**](ClickwrapsApi.md#patchClickwrapsId) | **PATCH** /clickwraps/{id} | Update Clickwrap |
| [**postClickwraps**](ClickwrapsApi.md#postClickwraps) | **POST** /clickwraps | Create Clickwrap |


<a id="deleteClickwrapsId"></a>
# **deleteClickwrapsId**
> deleteClickwrapsId(id)

Delete Clickwrap

Delete Clickwrap

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClickwrapsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://app.files.com/api/rest/v1");

    ClickwrapsApi apiInstance = new ClickwrapsApi(defaultClient);
    Integer id = 56; // Integer | Clickwrap ID.
    try {
      apiInstance.deleteClickwrapsId(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClickwrapsApi#deleteClickwrapsId");
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
| **id** | **Integer**| Clickwrap ID. | |

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

<a id="getClickwraps"></a>
# **getClickwraps**
> List&lt;ClickwrapEntity&gt; getClickwraps(cursor, perPage)

List Clickwraps

List Clickwraps

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClickwrapsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://app.files.com/api/rest/v1");

    ClickwrapsApi apiInstance = new ClickwrapsApi(defaultClient);
    String cursor = "cursor_example"; // String | Used for pagination.  When a list request has more records available, cursors are provided in the response headers `X-Files-Cursor-Next` and `X-Files-Cursor-Prev`.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination.
    Integer perPage = 56; // Integer | Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended).
    try {
      List<ClickwrapEntity> result = apiInstance.getClickwraps(cursor, perPage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClickwrapsApi#getClickwraps");
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

### Return type

[**List&lt;ClickwrapEntity&gt;**](ClickwrapEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of Clickwraps objects. |  -  |
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

<a id="getClickwrapsId"></a>
# **getClickwrapsId**
> ClickwrapEntity getClickwrapsId(id)

Show Clickwrap

Show Clickwrap

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClickwrapsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://app.files.com/api/rest/v1");

    ClickwrapsApi apiInstance = new ClickwrapsApi(defaultClient);
    Integer id = 56; // Integer | Clickwrap ID.
    try {
      ClickwrapEntity result = apiInstance.getClickwrapsId(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClickwrapsApi#getClickwrapsId");
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
| **id** | **Integer**| Clickwrap ID. | |

### Return type

[**ClickwrapEntity**](ClickwrapEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The Clickwraps object. |  -  |
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

<a id="patchClickwrapsId"></a>
# **patchClickwrapsId**
> ClickwrapEntity patchClickwrapsId(id, body, name, useWithBundles, useWithInboxes, useWithUsers)

Update Clickwrap

Update Clickwrap

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClickwrapsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://app.files.com/api/rest/v1");

    ClickwrapsApi apiInstance = new ClickwrapsApi(defaultClient);
    Integer id = 56; // Integer | Clickwrap ID.
    String body = "body_example"; // String | Body text of Clickwrap (supports Markdown formatting).
    String name = "name_example"; // String | Name of the Clickwrap agreement (used when selecting from multiple Clickwrap agreements.)
    String useWithBundles = "none"; // String | Use this Clickwrap for Bundles?
    String useWithInboxes = "none"; // String | Use this Clickwrap for Inboxes?
    String useWithUsers = "none"; // String | Use this Clickwrap for User Registrations?  Note: This only applies to User Registrations where the User is invited to your Files.com site using an E-Mail invitation process where they then set their own password.
    try {
      ClickwrapEntity result = apiInstance.patchClickwrapsId(id, body, name, useWithBundles, useWithInboxes, useWithUsers);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClickwrapsApi#patchClickwrapsId");
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
| **id** | **Integer**| Clickwrap ID. | |
| **body** | **String**| Body text of Clickwrap (supports Markdown formatting). | [optional] |
| **name** | **String**| Name of the Clickwrap agreement (used when selecting from multiple Clickwrap agreements.) | [optional] |
| **useWithBundles** | **String**| Use this Clickwrap for Bundles? | [optional] [enum: none, available, require] |
| **useWithInboxes** | **String**| Use this Clickwrap for Inboxes? | [optional] [enum: none, available, require] |
| **useWithUsers** | **String**| Use this Clickwrap for User Registrations?  Note: This only applies to User Registrations where the User is invited to your Files.com site using an E-Mail invitation process where they then set their own password. | [optional] [enum: none, require] |

### Return type

[**ClickwrapEntity**](ClickwrapEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The Clickwraps object. |  -  |
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

<a id="postClickwraps"></a>
# **postClickwraps**
> ClickwrapEntity postClickwraps(body, name, useWithBundles, useWithInboxes, useWithUsers)

Create Clickwrap

Create Clickwrap

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClickwrapsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://app.files.com/api/rest/v1");

    ClickwrapsApi apiInstance = new ClickwrapsApi(defaultClient);
    String body = "body_example"; // String | Body text of Clickwrap (supports Markdown formatting).
    String name = "name_example"; // String | Name of the Clickwrap agreement (used when selecting from multiple Clickwrap agreements.)
    String useWithBundles = "none"; // String | Use this Clickwrap for Bundles?
    String useWithInboxes = "none"; // String | Use this Clickwrap for Inboxes?
    String useWithUsers = "none"; // String | Use this Clickwrap for User Registrations?  Note: This only applies to User Registrations where the User is invited to your Files.com site using an E-Mail invitation process where they then set their own password.
    try {
      ClickwrapEntity result = apiInstance.postClickwraps(body, name, useWithBundles, useWithInboxes, useWithUsers);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClickwrapsApi#postClickwraps");
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
| **body** | **String**| Body text of Clickwrap (supports Markdown formatting). | [optional] |
| **name** | **String**| Name of the Clickwrap agreement (used when selecting from multiple Clickwrap agreements.) | [optional] |
| **useWithBundles** | **String**| Use this Clickwrap for Bundles? | [optional] [enum: none, available, require] |
| **useWithInboxes** | **String**| Use this Clickwrap for Inboxes? | [optional] [enum: none, available, require] |
| **useWithUsers** | **String**| Use this Clickwrap for User Registrations?  Note: This only applies to User Registrations where the User is invited to your Files.com site using an E-Mail invitation process where they then set their own password. | [optional] [enum: none, require] |

### Return type

[**ClickwrapEntity**](ClickwrapEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The Clickwraps object. |  -  |
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

