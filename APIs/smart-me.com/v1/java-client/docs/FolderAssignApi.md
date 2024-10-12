# FolderAssignApi

All URIs are relative to *https://smart-me.com:443*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**folderAssignPost**](FolderAssignApi.md#folderAssignPost) | **POST** /api/folder/assign | Assign a folder (source) or meter to another folder (target). Can be used to create a folder structure. |


<a id="folderAssignPost"></a>
# **folderAssignPost**
> folderAssignPost(source, target)

Assign a folder (source) or meter to another folder (target). Can be used to create a folder structure.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FolderAssignApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://smart-me.com:443");

    FolderAssignApi apiInstance = new FolderAssignApi(defaultClient);
    String source = "source_example"; // String | The ID of the meter or folder that should be assign
    String target = "target_example"; // String | The ID of the meter or folder that should be the parent
    try {
      apiInstance.folderAssignPost(source, target);
    } catch (ApiException e) {
      System.err.println("Exception when calling FolderAssignApi#folderAssignPost");
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
| **source** | **String**| The ID of the meter or folder that should be assign | |
| **target** | **String**| The ID of the meter or folder that should be the parent | |

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

