# ApiKeyApi

All URIs are relative to *http://app.files.com/api/rest/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiKeyDeleteCurrent**](ApiKeyApi.md#apiKeyDeleteCurrent) | **DELETE** /api_key | Delete current API key.  (Requires current API connection to be using an API key.) |
| [**apiKeyFindCurrent**](ApiKeyApi.md#apiKeyFindCurrent) | **GET** /api_key | Show information about current API key.  (Requires current API connection to be using an API key.) |
| [**apiKeyUpdateCurrent**](ApiKeyApi.md#apiKeyUpdateCurrent) | **PATCH** /api_key | Update current API key.  (Requires current API connection to be using an API key.) |


<a id="apiKeyDeleteCurrent"></a>
# **apiKeyDeleteCurrent**
> apiKeyDeleteCurrent()

Delete current API key.  (Requires current API connection to be using an API key.)

Delete current API key.  (Requires current API connection to be using an API key.)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApiKeyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://app.files.com/api/rest/v1");

    ApiKeyApi apiInstance = new ApiKeyApi(defaultClient);
    try {
      apiInstance.apiKeyDeleteCurrent();
    } catch (ApiException e) {
      System.err.println("Exception when calling ApiKeyApi#apiKeyDeleteCurrent");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

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

<a id="apiKeyFindCurrent"></a>
# **apiKeyFindCurrent**
> ApiKeyEntity apiKeyFindCurrent()

Show information about current API key.  (Requires current API connection to be using an API key.)

Show information about current API key.  (Requires current API connection to be using an API key.)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApiKeyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://app.files.com/api/rest/v1");

    ApiKeyApi apiInstance = new ApiKeyApi(defaultClient);
    try {
      ApiKeyEntity result = apiInstance.apiKeyFindCurrent();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApiKeyApi#apiKeyFindCurrent");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ApiKeyEntity**](ApiKeyEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The ApiKey object. |  -  |
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

<a id="apiKeyUpdateCurrent"></a>
# **apiKeyUpdateCurrent**
> ApiKeyEntity apiKeyUpdateCurrent(expiresAt, name, permissionSet)

Update current API key.  (Requires current API connection to be using an API key.)

Update current API key.  (Requires current API connection to be using an API key.)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApiKeyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://app.files.com/api/rest/v1");

    ApiKeyApi apiInstance = new ApiKeyApi(defaultClient);
    OffsetDateTime expiresAt = OffsetDateTime.now(); // OffsetDateTime | API Key expiration date
    String name = "name_example"; // String | Internal name for the API Key.  For your use.
    String permissionSet = "none"; // String | Permissions for this API Key.  Keys with the `desktop_app` permission set only have the ability to do the functions provided in our Desktop App (File and Share Link operations).  Additional permission sets may become available in the future, such as for a Site Admin to give a key with no administrator privileges.  If you have ideas for permission sets, please let us know.
    try {
      ApiKeyEntity result = apiInstance.apiKeyUpdateCurrent(expiresAt, name, permissionSet);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApiKeyApi#apiKeyUpdateCurrent");
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
| **expiresAt** | **OffsetDateTime**| API Key expiration date | [optional] |
| **name** | **String**| Internal name for the API Key.  For your use. | [optional] |
| **permissionSet** | **String**| Permissions for this API Key.  Keys with the &#x60;desktop_app&#x60; permission set only have the ability to do the functions provided in our Desktop App (File and Share Link operations).  Additional permission sets may become available in the future, such as for a Site Admin to give a key with no administrator privileges.  If you have ideas for permission sets, please let us know. | [optional] [enum: none, full, desktop_app, sync_app, office_integration, mobile_app] |

### Return type

[**ApiKeyEntity**](ApiKeyEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The ApiKey object. |  -  |
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

