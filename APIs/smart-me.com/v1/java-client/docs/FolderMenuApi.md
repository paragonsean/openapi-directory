# FolderMenuApi

All URIs are relative to *https://smart-me.com:443*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**folderMenuGet**](FolderMenuApi.md#folderMenuGet) | **GET** /api/FolderMenu | Gets the folder menu items (each item might contain child items) |
| [**folderMenuPost**](FolderMenuApi.md#folderMenuPost) | **POST** /api/FolderMenu | Creates and updates the folder menu items |


<a id="folderMenuGet"></a>
# **folderMenuGet**
> FolderMenuConfiguration folderMenuGet(filter)

Gets the folder menu items (each item might contain child items)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FolderMenuApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://smart-me.com:443");

    FolderMenuApi apiInstance = new FolderMenuApi(defaultClient);
    String filter = "filter_example"; // String | (optional) Filter for the folders and meters:               all: load everything              assigned: load only folders and meters that are assigend to a folder              unassigend: load only meters that are not assigend to a folder              user: load only folder and all users assigned to this folders              subuserlist: load all subusers as a list
    try {
      FolderMenuConfiguration result = apiInstance.folderMenuGet(filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FolderMenuApi#folderMenuGet");
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
| **filter** | **String**| (optional) Filter for the folders and meters:               all: load everything              assigned: load only folders and meters that are assigend to a folder              unassigend: load only meters that are not assigend to a folder              user: load only folder and all users assigned to this folders              subuserlist: load all subusers as a list | [optional] |

### Return type

[**FolderMenuConfiguration**](FolderMenuConfiguration.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="folderMenuPost"></a>
# **folderMenuPost**
> folderMenuPost(folderMenuConfiguration)

Creates and updates the folder menu items

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FolderMenuApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://smart-me.com:443");

    FolderMenuApi apiInstance = new FolderMenuApi(defaultClient);
    FolderMenuConfiguration folderMenuConfiguration = new FolderMenuConfiguration(); // FolderMenuConfiguration | 
    try {
      apiInstance.folderMenuPost(folderMenuConfiguration);
    } catch (ApiException e) {
      System.err.println("Exception when calling FolderMenuApi#folderMenuPost");
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
| **folderMenuConfiguration** | [**FolderMenuConfiguration**](FolderMenuConfiguration.md)|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |

