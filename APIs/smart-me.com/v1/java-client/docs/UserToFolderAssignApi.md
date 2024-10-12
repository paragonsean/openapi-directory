# UserToFolderAssignApi

All URIs are relative to *https://smart-me.com:443*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**userToFolderAssignDelete**](UserToFolderAssignApi.md#userToFolderAssignDelete) | **DELETE** /api/folder/user/assign | Deletes a user to folder assignement |
| [**userToFolderAssignPost**](UserToFolderAssignApi.md#userToFolderAssignPost) | **POST** /api/folder/user/assign | Assign a user to a folder |


<a id="userToFolderAssignDelete"></a>
# **userToFolderAssignDelete**
> userToFolderAssignDelete(source, target)

Deletes a user to folder assignement

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserToFolderAssignApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://smart-me.com:443");

    UserToFolderAssignApi apiInstance = new UserToFolderAssignApi(defaultClient);
    String source = "source_example"; // String | The ID of the user that should be de-assign
    String target = "target_example"; // String | The ID of the folder
    try {
      apiInstance.userToFolderAssignDelete(source, target);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserToFolderAssignApi#userToFolderAssignDelete");
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
| **source** | **String**| The ID of the user that should be de-assign | |
| **target** | **String**| The ID of the folder | |

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

<a id="userToFolderAssignPost"></a>
# **userToFolderAssignPost**
> userToFolderAssignPost(source, target, oldFolder)

Assign a user to a folder

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserToFolderAssignApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://smart-me.com:443");

    UserToFolderAssignApi apiInstance = new UserToFolderAssignApi(defaultClient);
    String source = "source_example"; // String | The ID of the user that should be assign
    String target = "target_example"; // String | The ID of the folder that should be the parent
    String oldFolder = "oldFolder_example"; // String | The ID of the old folder (in case of a drag and drop to a new folder)
    try {
      apiInstance.userToFolderAssignPost(source, target, oldFolder);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserToFolderAssignApi#userToFolderAssignPost");
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
| **source** | **String**| The ID of the user that should be assign | |
| **target** | **String**| The ID of the folder that should be the parent | |
| **oldFolder** | **String**| The ID of the old folder (in case of a drag and drop to a new folder) | |

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

