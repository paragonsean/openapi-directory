# FolderSettingsApi

All URIs are relative to *https://smart-me.com:443*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**folderSettingsDelete**](FolderSettingsApi.md#folderSettingsDelete) | **DELETE** /api/folder/settings/{id} | Deletes a folder |
| [**folderSettingsGet**](FolderSettingsApi.md#folderSettingsGet) | **GET** /api/folder/settings/{id} | Gets the settings of a folder or meter |
| [**folderSettingsPost**](FolderSettingsApi.md#folderSettingsPost) | **POST** /api/folder/settings/{id} | Add or edit a folder or a meter. To add a new folder use and empty ID |


<a id="folderSettingsDelete"></a>
# **folderSettingsDelete**
> folderSettingsDelete(id)

Deletes a folder

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FolderSettingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://smart-me.com:443");

    FolderSettingsApi apiInstance = new FolderSettingsApi(defaultClient);
    String id = "id_example"; // String | The ID of the folder
    try {
      apiInstance.folderSettingsDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling FolderSettingsApi#folderSettingsDelete");
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
| **id** | **String**| The ID of the folder | |

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
| **204** | No Content |  -  |

<a id="folderSettingsGet"></a>
# **folderSettingsGet**
> FolderSettings folderSettingsGet(id)

Gets the settings of a folder or meter

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FolderSettingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://smart-me.com:443");

    FolderSettingsApi apiInstance = new FolderSettingsApi(defaultClient);
    String id = "id_example"; // String | 
    try {
      FolderSettings result = apiInstance.folderSettingsGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FolderSettingsApi#folderSettingsGet");
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
| **id** | **String**|  | |

### Return type

[**FolderSettings**](FolderSettings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="folderSettingsPost"></a>
# **folderSettingsPost**
> FolderMenuItem folderSettingsPost(id, folderSettings)

Add or edit a folder or a meter. To add a new folder use and empty ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FolderSettingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://smart-me.com:443");

    FolderSettingsApi apiInstance = new FolderSettingsApi(defaultClient);
    String id = "id_example"; // String | The ID of the folder or meter to edit. Use and empty ID to add a new folder
    FolderSettings folderSettings = new FolderSettings(); // FolderSettings | The folder or meter data
    try {
      FolderMenuItem result = apiInstance.folderSettingsPost(id, folderSettings);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FolderSettingsApi#folderSettingsPost");
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
| **id** | **String**| The ID of the folder or meter to edit. Use and empty ID to add a new folder | |
| **folderSettings** | [**FolderSettings**](FolderSettings.md)| The folder or meter data | |

### Return type

[**FolderMenuItem**](FolderMenuItem.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

