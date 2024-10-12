# SftpHostKeysApi

All URIs are relative to *http://app.files.com/api/rest/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**deleteSftpHostKeysId**](SftpHostKeysApi.md#deleteSftpHostKeysId) | **DELETE** /sftp_host_keys/{id} | Delete Sftp Host Key |
| [**getSftpHostKeys**](SftpHostKeysApi.md#getSftpHostKeys) | **GET** /sftp_host_keys | List Sftp Host Keys |
| [**getSftpHostKeysId**](SftpHostKeysApi.md#getSftpHostKeysId) | **GET** /sftp_host_keys/{id} | Show Sftp Host Key |
| [**patchSftpHostKeysId**](SftpHostKeysApi.md#patchSftpHostKeysId) | **PATCH** /sftp_host_keys/{id} | Update Sftp Host Key |
| [**postSftpHostKeys**](SftpHostKeysApi.md#postSftpHostKeys) | **POST** /sftp_host_keys | Create Sftp Host Key |


<a id="deleteSftpHostKeysId"></a>
# **deleteSftpHostKeysId**
> deleteSftpHostKeysId(id)

Delete Sftp Host Key

Delete Sftp Host Key

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SftpHostKeysApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://app.files.com/api/rest/v1");

    SftpHostKeysApi apiInstance = new SftpHostKeysApi(defaultClient);
    Integer id = 56; // Integer | Sftp Host Key ID.
    try {
      apiInstance.deleteSftpHostKeysId(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling SftpHostKeysApi#deleteSftpHostKeysId");
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
| **id** | **Integer**| Sftp Host Key ID. | |

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

<a id="getSftpHostKeys"></a>
# **getSftpHostKeys**
> List&lt;SftpHostKeyEntity&gt; getSftpHostKeys(cursor, perPage)

List Sftp Host Keys

List Sftp Host Keys

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SftpHostKeysApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://app.files.com/api/rest/v1");

    SftpHostKeysApi apiInstance = new SftpHostKeysApi(defaultClient);
    String cursor = "cursor_example"; // String | Used for pagination.  When a list request has more records available, cursors are provided in the response headers `X-Files-Cursor-Next` and `X-Files-Cursor-Prev`.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination.
    Integer perPage = 56; // Integer | Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended).
    try {
      List<SftpHostKeyEntity> result = apiInstance.getSftpHostKeys(cursor, perPage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SftpHostKeysApi#getSftpHostKeys");
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

[**List&lt;SftpHostKeyEntity&gt;**](SftpHostKeyEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of SftpHostKeys objects. |  -  |
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

<a id="getSftpHostKeysId"></a>
# **getSftpHostKeysId**
> SftpHostKeyEntity getSftpHostKeysId(id)

Show Sftp Host Key

Show Sftp Host Key

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SftpHostKeysApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://app.files.com/api/rest/v1");

    SftpHostKeysApi apiInstance = new SftpHostKeysApi(defaultClient);
    Integer id = 56; // Integer | Sftp Host Key ID.
    try {
      SftpHostKeyEntity result = apiInstance.getSftpHostKeysId(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SftpHostKeysApi#getSftpHostKeysId");
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
| **id** | **Integer**| Sftp Host Key ID. | |

### Return type

[**SftpHostKeyEntity**](SftpHostKeyEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The SftpHostKeys object. |  -  |
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

<a id="patchSftpHostKeysId"></a>
# **patchSftpHostKeysId**
> SftpHostKeyEntity patchSftpHostKeysId(id, name, privateKey)

Update Sftp Host Key

Update Sftp Host Key

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SftpHostKeysApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://app.files.com/api/rest/v1");

    SftpHostKeysApi apiInstance = new SftpHostKeysApi(defaultClient);
    Integer id = 56; // Integer | Sftp Host Key ID.
    String name = "name_example"; // String | The friendly name of this SFTP Host Key.
    String privateKey = "privateKey_example"; // String | The private key data.
    try {
      SftpHostKeyEntity result = apiInstance.patchSftpHostKeysId(id, name, privateKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SftpHostKeysApi#patchSftpHostKeysId");
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
| **id** | **Integer**| Sftp Host Key ID. | |
| **name** | **String**| The friendly name of this SFTP Host Key. | [optional] |
| **privateKey** | **String**| The private key data. | [optional] |

### Return type

[**SftpHostKeyEntity**](SftpHostKeyEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The SftpHostKeys object. |  -  |
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

<a id="postSftpHostKeys"></a>
# **postSftpHostKeys**
> SftpHostKeyEntity postSftpHostKeys(name, privateKey)

Create Sftp Host Key

Create Sftp Host Key

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SftpHostKeysApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://app.files.com/api/rest/v1");

    SftpHostKeysApi apiInstance = new SftpHostKeysApi(defaultClient);
    String name = "name_example"; // String | The friendly name of this SFTP Host Key.
    String privateKey = "privateKey_example"; // String | The private key data.
    try {
      SftpHostKeyEntity result = apiInstance.postSftpHostKeys(name, privateKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SftpHostKeysApi#postSftpHostKeys");
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
| **name** | **String**| The friendly name of this SFTP Host Key. | [optional] |
| **privateKey** | **String**| The private key data. | [optional] |

### Return type

[**SftpHostKeyEntity**](SftpHostKeyEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The SftpHostKeys object. |  -  |
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

