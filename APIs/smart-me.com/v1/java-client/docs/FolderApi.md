# FolderApi

All URIs are relative to *https://smart-me.com:443*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**folderGet**](FolderApi.md#folderGet) | **GET** /api/Folder/{id} | Gets the Values for a folder or a meter |


<a id="folderGet"></a>
# **folderGet**
> FolderData folderGet(id)

Gets the Values for a folder or a meter

Gets the Values for a folder or a meter

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FolderApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://smart-me.com:443");

    FolderApi apiInstance = new FolderApi(defaultClient);
    String id = "id_example"; // String | 
    try {
      FolderData result = apiInstance.folderGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FolderApi#folderGet");
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

[**FolderData**](FolderData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

