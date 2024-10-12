# GlobalImageCategoriesApi

All URIs are relative to *https://secure.agco-ats.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**globalImageCategoriesGetFile**](GlobalImageCategoriesApi.md#globalImageCategoriesGetFile) | **GET** /api/v2/GlobalImageCategories/{ID} | Gets a file&#39;s metadata. |
| [**globalImageCategoriesGetFiles**](GlobalImageCategoriesApi.md#globalImageCategoriesGetFiles) | **GET** /api/v2/GlobalImageCategories | Get a paged response of file metadata. |
| [**globalImageCategoriesPostFile**](GlobalImageCategoriesApi.md#globalImageCategoriesPostFile) | **POST** /api/v2/GlobalImageCategories | Create the metadata for a file before uploading. The State should be &#39;Created&#39;. |


<a id="globalImageCategoriesGetFile"></a>
# **globalImageCategoriesGetFile**
> GlobalResourcesSharedModelsGlobalImageCategory globalImageCategoriesGetFile(ID)

Gets a file&#39;s metadata.

No Documentation Found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GlobalImageCategoriesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    GlobalImageCategoriesApi apiInstance = new GlobalImageCategoriesApi(defaultClient);
    String ID = "ID_example"; // String | The file's id.
    try {
      GlobalResourcesSharedModelsGlobalImageCategory result = apiInstance.globalImageCategoriesGetFile(ID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GlobalImageCategoriesApi#globalImageCategoriesGetFile");
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
| **ID** | **String**| The file&#39;s id. | |

### Return type

[**GlobalResourcesSharedModelsGlobalImageCategory**](GlobalResourcesSharedModelsGlobalImageCategory.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | API Error Response |  -  |

<a id="globalImageCategoriesGetFiles"></a>
# **globalImageCategoriesGetFiles**
> APIIPagedResponseGlobalResourcesSharedModelsGlobalImageCategory globalImageCategoriesGetFiles(limit, offset)

Get a paged response of file metadata.

No Documentation Found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GlobalImageCategoriesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    GlobalImageCategoriesApi apiInstance = new GlobalImageCategoriesApi(defaultClient);
    Integer limit = 56; // Integer | Optional. The page limit. The default page limit is 10.
    Integer offset = 56; // Integer | Optional. The page offset. The default page offset is 0.
    try {
      APIIPagedResponseGlobalResourcesSharedModelsGlobalImageCategory result = apiInstance.globalImageCategoriesGetFiles(limit, offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GlobalImageCategoriesApi#globalImageCategoriesGetFiles");
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
| **limit** | **Integer**| Optional. The page limit. The default page limit is 10. | [optional] |
| **offset** | **Integer**| Optional. The page offset. The default page offset is 0. | [optional] |

### Return type

[**APIIPagedResponseGlobalResourcesSharedModelsGlobalImageCategory**](APIIPagedResponseGlobalResourcesSharedModelsGlobalImageCategory.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | API Error Response |  -  |

<a id="globalImageCategoriesPostFile"></a>
# **globalImageCategoriesPostFile**
> String globalImageCategoriesPostFile(globalResourcesSharedModelsGlobalImageCategory)

Create the metadata for a file before uploading. The State should be &#39;Created&#39;.

No Documentation Found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GlobalImageCategoriesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    GlobalImageCategoriesApi apiInstance = new GlobalImageCategoriesApi(defaultClient);
    GlobalResourcesSharedModelsGlobalImageCategory globalResourcesSharedModelsGlobalImageCategory = new GlobalResourcesSharedModelsGlobalImageCategory(); // GlobalResourcesSharedModelsGlobalImageCategory | The file's metadata.
    try {
      String result = apiInstance.globalImageCategoriesPostFile(globalResourcesSharedModelsGlobalImageCategory);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GlobalImageCategoriesApi#globalImageCategoriesPostFile");
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
| **globalResourcesSharedModelsGlobalImageCategory** | [**GlobalResourcesSharedModelsGlobalImageCategory**](GlobalResourcesSharedModelsGlobalImageCategory.md)| The file&#39;s metadata. | |

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | API Error Response |  -  |

