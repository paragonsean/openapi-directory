# DefaultApi

All URIs are relative to *https://api.nexmo.com/v3/media*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**deleteAMediaItem**](DefaultApi.md#deleteAMediaItem) | **DELETE** /:id | Delete a media item |
| [**listAndSearchMediaItems**](DefaultApi.md#listAndSearchMediaItems) | **GET** / | List and search media items |
| [**retrieveAMediaItem**](DefaultApi.md#retrieveAMediaItem) | **GET** /:id/info | Retrieve a media item |
| [**updateAMediaItem**](DefaultApi.md#updateAMediaItem) | **PUT** /:id/info | Update a media item |


<a id="deleteAMediaItem"></a>
# **deleteAMediaItem**
> deleteAMediaItem()

Delete a media item

Delete a previously created media item by ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.nexmo.com/v3/media");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    try {
      apiInstance.deleteAMediaItem();
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deleteAMediaItem");
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

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Successfully deleted |  -  |

<a id="listAndSearchMediaItems"></a>
# **listAndSearchMediaItems**
> ListAndSearchMediaItems200Response listAndSearchMediaItems(order, pageIndex, pageSize, startTime, endTime)

List and search media items

Retrieve information about multiple media items with the ability to search and paginate.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.nexmo.com/v3/media");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String order = "ascending"; // String | The order of search results.
    Integer pageIndex = 0; // Integer | Which page to retrieve in pagination
    Integer pageSize = 20; // Integer | How many items at most per page
    String startTime = "1 week ago"; // String | Retrieve results created on or after this timestap.
    String endTime = "2020-01-01T14:00:00.000Z"; // String | Retrieve results created on or before this timestamp.
    try {
      ListAndSearchMediaItems200Response result = apiInstance.listAndSearchMediaItems(order, pageIndex, pageSize, startTime, endTime);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listAndSearchMediaItems");
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
| **order** | **String**| The order of search results. | [optional] [default to descending] [enum: ascending, descending] |
| **pageIndex** | **Integer**| Which page to retrieve in pagination | [optional] [default to 0] |
| **pageSize** | **Integer**| How many items at most per page | [optional] [default to 20] |
| **startTime** | **String**| Retrieve results created on or after this timestap. | [optional] [default to 1 week ago] |
| **endTime** | **String**| Retrieve results created on or before this timestamp. | [optional] |

### Return type

[**ListAndSearchMediaItems200Response**](ListAndSearchMediaItems200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully retrieved |  -  |

<a id="retrieveAMediaItem"></a>
# **retrieveAMediaItem**
> Media retrieveAMediaItem()

Retrieve a media item

Retrieve information about a single media item

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.nexmo.com/v3/media");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    try {
      Media result = apiInstance.retrieveAMediaItem();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#retrieveAMediaItem");
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

[**Media**](Media.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully retrieved |  -  |

<a id="updateAMediaItem"></a>
# **updateAMediaItem**
> updateAMediaItem(description, maxDownloadsAllowed, metadataPrimary, metadataSecondary, mimeType, _public, title)

Update a media item

Update a previously created media item by ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.nexmo.com/v3/media");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String description = "description_example"; // String | A description of the media file.
    Integer maxDownloadsAllowed = 56; // Integer | The maximum number of times the file may be downloaded. Unlimited when not provided.
    String metadataPrimary = "metadataPrimary_example"; // String | A string containing metadata about the media file.
    String metadataSecondary = "metadataSecondary_example"; // String | A string containing further metadata about the media file.
    String mimeType = "mimeType_example"; // String | The MIME type of the media file.
    Boolean _public = true; // Boolean | Whether the item is publicly available without authentication.
    String title = "title_example"; // String | A string containing a title for the media file.
    try {
      apiInstance.updateAMediaItem(description, maxDownloadsAllowed, metadataPrimary, metadataSecondary, mimeType, _public, title);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#updateAMediaItem");
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
| **description** | **String**| A description of the media file. | [optional] |
| **maxDownloadsAllowed** | **Integer**| The maximum number of times the file may be downloaded. Unlimited when not provided. | [optional] |
| **metadataPrimary** | **String**| A string containing metadata about the media file. | [optional] |
| **metadataSecondary** | **String**| A string containing further metadata about the media file. | [optional] |
| **mimeType** | **String**| The MIME type of the media file. | [optional] |
| **_public** | **Boolean**| Whether the item is publicly available without authentication. | [optional] |
| **title** | **String**| A string containing a title for the media file. | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Successfully updated |  -  |

