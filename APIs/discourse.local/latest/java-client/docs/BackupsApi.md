# BackupsApi

All URIs are relative to *http://discourse.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createBackup**](BackupsApi.md#createBackup) | **POST** /admin/backups.json | Create backup |
| [**downloadBackup**](BackupsApi.md#downloadBackup) | **GET** /admin/backups/{filename} | Download backup |
| [**getBackups**](BackupsApi.md#getBackups) | **GET** /admin/backups.json | List backups |
| [**sendDownloadBackupEmail**](BackupsApi.md#sendDownloadBackupEmail) | **PUT** /admin/backups/{filename} | Send download backup email |


<a id="createBackup"></a>
# **createBackup**
> CreateBackup200Response createBackup(createBackupRequest)

Create backup

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BackupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://discourse.local");

    BackupsApi apiInstance = new BackupsApi(defaultClient);
    CreateBackupRequest createBackupRequest = new CreateBackupRequest(); // CreateBackupRequest | 
    try {
      CreateBackup200Response result = apiInstance.createBackup(createBackupRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BackupsApi#createBackup");
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
| **createBackupRequest** | [**CreateBackupRequest**](CreateBackupRequest.md)|  | [optional] |

### Return type

[**CreateBackup200Response**](CreateBackup200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | success response |  -  |

<a id="downloadBackup"></a>
# **downloadBackup**
> downloadBackup(filename, token)

Download backup

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BackupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://discourse.local");

    BackupsApi apiInstance = new BackupsApi(defaultClient);
    String filename = "filename_example"; // String | 
    String token = "token_example"; // String | 
    try {
      apiInstance.downloadBackup(filename, token);
    } catch (ApiException e) {
      System.err.println("Exception when calling BackupsApi#downloadBackup");
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
| **filename** | **String**|  | |
| **token** | **String**|  | |

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
| **200** | success response |  -  |

<a id="getBackups"></a>
# **getBackups**
> Set&lt;GetBackups200ResponseInner&gt; getBackups()

List backups

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BackupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://discourse.local");

    BackupsApi apiInstance = new BackupsApi(defaultClient);
    try {
      Set<GetBackups200ResponseInner> result = apiInstance.getBackups();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BackupsApi#getBackups");
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

[**Set&lt;GetBackups200ResponseInner&gt;**](GetBackups200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | success response |  -  |

<a id="sendDownloadBackupEmail"></a>
# **sendDownloadBackupEmail**
> sendDownloadBackupEmail(filename)

Send download backup email

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BackupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://discourse.local");

    BackupsApi apiInstance = new BackupsApi(defaultClient);
    String filename = "filename_example"; // String | 
    try {
      apiInstance.sendDownloadBackupEmail(filename);
    } catch (ApiException e) {
      System.err.println("Exception when calling BackupsApi#sendDownloadBackupEmail");
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
| **filename** | **String**|  | |

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
| **200** | success response |  -  |

