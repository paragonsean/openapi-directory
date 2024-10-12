# BackupRestoreApi

All URIs are relative to *http://whatsapp.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**backupSettings**](BackupRestoreApi.md#backupSettings) | **POST** /settings/backup | Backup-Settings |
| [**restoreSettings**](BackupRestoreApi.md#restoreSettings) | **POST** /settings/restore | Restore-Settings |


<a id="backupSettings"></a>
# **backupSettings**
> BackupSettingsResponse backupSettings(backupSettingsRequestBody)

Backup-Settings

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BackupRestoreApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://whatsapp.local");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    BackupRestoreApi apiInstance = new BackupRestoreApi(defaultClient);
    BackupSettingsRequestBody backupSettingsRequestBody = new BackupSettingsRequestBody(); // BackupSettingsRequestBody | 
    try {
      BackupSettingsResponse result = apiInstance.backupSettings(backupSettingsRequestBody);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BackupRestoreApi#backupSettings");
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
| **backupSettingsRequestBody** | [**BackupSettingsRequestBody**](BackupSettingsRequestBody.md)|  | |

### Return type

[**BackupSettingsResponse**](BackupSettingsResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="restoreSettings"></a>
# **restoreSettings**
> restoreSettings(restoreSettingsRequestBody)

Restore-Settings

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BackupRestoreApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://whatsapp.local");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    BackupRestoreApi apiInstance = new BackupRestoreApi(defaultClient);
    RestoreSettingsRequestBody restoreSettingsRequestBody = new RestoreSettingsRequestBody(); // RestoreSettingsRequestBody | 
    try {
      apiInstance.restoreSettings(restoreSettingsRequestBody);
    } catch (ApiException e) {
      System.err.println("Exception when calling BackupRestoreApi#restoreSettings");
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
| **restoreSettingsRequestBody** | [**RestoreSettingsRequestBody**](RestoreSettingsRequestBody.md)|  | |

### Return type

null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

