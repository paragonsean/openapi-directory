# DownloadsApi

All URIs are relative to */api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**downloadAvatar**](DownloadsApi.md#downloadAvatar) | **GET** /v4/downloads/avatar/{user_id}/{uuid} | Download avatar |
| [**downloadFileViaToken**](DownloadsApi.md#downloadFileViaToken) | **GET** /v4/downloads/{token} | Download file |
| [**downloadFileViaToken1**](DownloadsApi.md#downloadFileViaToken1) | **HEAD** /v4/downloads/{token} | Download file |
| [**downloadZipArchiveViaToken**](DownloadsApi.md#downloadZipArchiveViaToken) | **GET** /v4/downloads/zip/{token} | Download ZIP archive |


<a id="downloadAvatar"></a>
# **downloadAvatar**
> String downloadAvatar(userId, uuid)

Download avatar

&lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.11.0&lt;/h3&gt;  ### Description: Download avatar for given user ID and UUID.  ### Precondition: Valid UUID.  ### Postcondition: Stream is returned.  ### Further Information: None.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DownloadsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    DownloadsApi apiInstance = new DownloadsApi(defaultClient);
    Long userId = 56L; // Long | User ID
    String uuid = "uuid_example"; // String | UUID of the avatar
    try {
      String result = apiInstance.downloadAvatar(userId, uuid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DownloadsApi#downloadAvatar");
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
| **userId** | **Long**| User ID | |
| **uuid** | **String**| UUID of the avatar | |

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **404** | Not Found |  -  |
| **406** | Not Acceptable |  -  |

<a id="downloadFileViaToken"></a>
# **downloadFileViaToken**
> downloadFileViaToken(token, range, genericMimetype, inline)

Download file

### Description: Download a file.  ### Precondition: Valid download token.  ### Postcondition: Stream is returned.  ### Further Information: Range requests are supported.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DownloadsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    DownloadsApi apiInstance = new DownloadsApi(defaultClient);
    String token = "token_example"; // String | Download token
    String range = "range_example"; // String | Range   e.g. `bytes=0-999`
    Boolean genericMimetype = true; // Boolean | Always return `application/octet-stream` instead of specific mimetype
    Boolean inline = true; // Boolean | Use Content-Disposition: `inline` instead of `attachment`
    try {
      apiInstance.downloadFileViaToken(token, range, genericMimetype, inline);
    } catch (ApiException e) {
      System.err.println("Exception when calling DownloadsApi#downloadFileViaToken");
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
| **token** | **String**| Download token | |
| **range** | **String**| Range   e.g. &#x60;bytes&#x3D;0-999&#x60; | [optional] |
| **genericMimetype** | **Boolean**| Always return &#x60;application/octet-stream&#x60; instead of specific mimetype | [optional] |
| **inline** | **Boolean**| Use Content-Disposition: &#x60;inline&#x60; instead of &#x60;attachment&#x60; | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **206** | Partial Content |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **406** | Not Acceptable |  -  |
| **416** | Range Not Satisfiable |  -  |

<a id="downloadFileViaToken1"></a>
# **downloadFileViaToken1**
> downloadFileViaToken1(token, range, genericMimetype, inline)

Download file

### Description: Download a file.  ### Precondition: Valid download token.  ### Postcondition: Stream is returned.  ### Further Information: Range requests are supported.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DownloadsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    DownloadsApi apiInstance = new DownloadsApi(defaultClient);
    String token = "token_example"; // String | Download token
    String range = "range_example"; // String | Range   e.g. `bytes=0-999`
    Boolean genericMimetype = true; // Boolean | Always return `application/octet-stream` instead of specific mimetype
    Boolean inline = true; // Boolean | Use Content-Disposition: `inline` instead of `attachment`
    try {
      apiInstance.downloadFileViaToken1(token, range, genericMimetype, inline);
    } catch (ApiException e) {
      System.err.println("Exception when calling DownloadsApi#downloadFileViaToken1");
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
| **token** | **String**| Download token | |
| **range** | **String**| Range   e.g. &#x60;bytes&#x3D;0-999&#x60; | [optional] |
| **genericMimetype** | **Boolean**| Always return &#x60;application/octet-stream&#x60; instead of specific mimetype | [optional] |
| **inline** | **Boolean**| Use Content-Disposition: &#x60;inline&#x60; instead of &#x60;attachment&#x60; | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **206** | Partial Content |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **406** | Not Acceptable |  -  |
| **416** | Range Not Satisfiable |  -  |

<a id="downloadZipArchiveViaToken"></a>
# **downloadZipArchiveViaToken**
> downloadZipArchiveViaToken(token)

Download ZIP archive

### Description: Download multiple files in a ZIP archive.  ### Precondition: Valid download token.  ### Postcondition: Stream is returned.  ### Further Information: Create a download token with &#x60;POST /nodes/zip&#x60; API.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DownloadsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    DownloadsApi apiInstance = new DownloadsApi(defaultClient);
    String token = "token_example"; // String | Download token
    try {
      apiInstance.downloadZipArchiveViaToken(token);
    } catch (ApiException e) {
      System.err.println("Exception when calling DownloadsApi#downloadZipArchiveViaToken");
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
| **token** | **String**| Download token | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **406** | Not Acceptable |  -  |

