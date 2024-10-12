# HistoryApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**deleteHistoryItemV1HistoryHistoryItemIdDelete**](HistoryApi.md#deleteHistoryItemV1HistoryHistoryItemIdDelete) | **DELETE** /v1/history/{history_item_id} | Delete History Item |
| [**deleteHistoryItemsV1HistoryDeletePost**](HistoryApi.md#deleteHistoryItemsV1HistoryDeletePost) | **POST** /v1/history/delete | Delete History Items |
| [**downloadHistoryItemsV1HistoryDownloadPost**](HistoryApi.md#downloadHistoryItemsV1HistoryDownloadPost) | **POST** /v1/history/download | Download History Items |
| [**getAudioFromHistoryItemV1HistoryHistoryItemIdAudioGet**](HistoryApi.md#getAudioFromHistoryItemV1HistoryHistoryItemIdAudioGet) | **GET** /v1/history/{history_item_id}/audio | Get Audio From History Item |
| [**getGeneratedItemsV1HistoryGet**](HistoryApi.md#getGeneratedItemsV1HistoryGet) | **GET** /v1/history | Get Generated Items |


<a id="deleteHistoryItemV1HistoryHistoryItemIdDelete"></a>
# **deleteHistoryItemV1HistoryHistoryItemIdDelete**
> Object deleteHistoryItemV1HistoryHistoryItemIdDelete(historyItemId, xiApiKey)

Delete History Item

Delete a history item by its ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HistoryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    HistoryApi apiInstance = new HistoryApi(defaultClient);
    String historyItemId = "VW7YKqPnjY4h39yTbx2L"; // String | History item ID to be used, you can use GET https://api.elevenlabs.io/v1/history to receive a list of history items and their IDs.
    String xiApiKey = "xiApiKey_example"; // String | Your API key. This is required by most endpoints to access our API programatically. You can view your xi-api-key using the 'Profile' tab on the website.
    try {
      Object result = apiInstance.deleteHistoryItemV1HistoryHistoryItemIdDelete(historyItemId, xiApiKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HistoryApi#deleteHistoryItemV1HistoryHistoryItemIdDelete");
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
| **historyItemId** | **String**| History item ID to be used, you can use GET https://api.elevenlabs.io/v1/history to receive a list of history items and their IDs. | |
| **xiApiKey** | **String**| Your API key. This is required by most endpoints to access our API programatically. You can view your xi-api-key using the &#39;Profile&#39; tab on the website. | [optional] |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

<a id="deleteHistoryItemsV1HistoryDeletePost"></a>
# **deleteHistoryItemsV1HistoryDeletePost**
> Object deleteHistoryItemsV1HistoryDeletePost(bodyDeleteHistoryItemsV1HistoryDeletePost, xiApiKey)

Delete History Items

Delete a number of history items by their IDs.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HistoryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    HistoryApi apiInstance = new HistoryApi(defaultClient);
    BodyDeleteHistoryItemsV1HistoryDeletePost bodyDeleteHistoryItemsV1HistoryDeletePost = new BodyDeleteHistoryItemsV1HistoryDeletePost(); // BodyDeleteHistoryItemsV1HistoryDeletePost | 
    String xiApiKey = "xiApiKey_example"; // String | Your API key. This is required by most endpoints to access our API programatically. You can view your xi-api-key using the 'Profile' tab on the website.
    try {
      Object result = apiInstance.deleteHistoryItemsV1HistoryDeletePost(bodyDeleteHistoryItemsV1HistoryDeletePost, xiApiKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HistoryApi#deleteHistoryItemsV1HistoryDeletePost");
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
| **bodyDeleteHistoryItemsV1HistoryDeletePost** | [**BodyDeleteHistoryItemsV1HistoryDeletePost**](BodyDeleteHistoryItemsV1HistoryDeletePost.md)|  | |
| **xiApiKey** | **String**| Your API key. This is required by most endpoints to access our API programatically. You can view your xi-api-key using the &#39;Profile&#39; tab on the website. | [optional] |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

<a id="downloadHistoryItemsV1HistoryDownloadPost"></a>
# **downloadHistoryItemsV1HistoryDownloadPost**
> downloadHistoryItemsV1HistoryDownloadPost(bodyDownloadHistoryItemsV1HistoryDownloadPost, xiApiKey)

Download History Items

Download one or more history items. If one history item ID is provided, we will return a single audio file. If more than one history item IDs are provided, we will provide the history items packed into a .zip file.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HistoryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    HistoryApi apiInstance = new HistoryApi(defaultClient);
    BodyDownloadHistoryItemsV1HistoryDownloadPost bodyDownloadHistoryItemsV1HistoryDownloadPost = new BodyDownloadHistoryItemsV1HistoryDownloadPost(); // BodyDownloadHistoryItemsV1HistoryDownloadPost | 
    String xiApiKey = "xiApiKey_example"; // String | Your API key. This is required by most endpoints to access our API programatically. You can view your xi-api-key using the 'Profile' tab on the website.
    try {
      apiInstance.downloadHistoryItemsV1HistoryDownloadPost(bodyDownloadHistoryItemsV1HistoryDownloadPost, xiApiKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling HistoryApi#downloadHistoryItemsV1HistoryDownloadPost");
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
| **bodyDownloadHistoryItemsV1HistoryDownloadPost** | [**BodyDownloadHistoryItemsV1HistoryDownloadPost**](BodyDownloadHistoryItemsV1HistoryDownloadPost.md)|  | |
| **xiApiKey** | **String**| Your API key. This is required by most endpoints to access our API programatically. You can view your xi-api-key using the &#39;Profile&#39; tab on the website. | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

<a id="getAudioFromHistoryItemV1HistoryHistoryItemIdAudioGet"></a>
# **getAudioFromHistoryItemV1HistoryHistoryItemIdAudioGet**
> getAudioFromHistoryItemV1HistoryHistoryItemIdAudioGet(historyItemId, xiApiKey)

Get Audio From History Item

Returns the audio of an history item.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HistoryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    HistoryApi apiInstance = new HistoryApi(defaultClient);
    String historyItemId = "VW7YKqPnjY4h39yTbx2L"; // String | History item ID to be used, you can use GET https://api.elevenlabs.io/v1/history to receive a list of history items and their IDs.
    String xiApiKey = "xiApiKey_example"; // String | Your API key. This is required by most endpoints to access our API programatically. You can view your xi-api-key using the 'Profile' tab on the website.
    try {
      apiInstance.getAudioFromHistoryItemV1HistoryHistoryItemIdAudioGet(historyItemId, xiApiKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling HistoryApi#getAudioFromHistoryItemV1HistoryHistoryItemIdAudioGet");
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
| **historyItemId** | **String**| History item ID to be used, you can use GET https://api.elevenlabs.io/v1/history to receive a list of history items and their IDs. | |
| **xiApiKey** | **String**| Your API key. This is required by most endpoints to access our API programatically. You can view your xi-api-key using the &#39;Profile&#39; tab on the website. | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: audio/mpeg, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

<a id="getGeneratedItemsV1HistoryGet"></a>
# **getGeneratedItemsV1HistoryGet**
> GetHistoryResponseModel getGeneratedItemsV1HistoryGet(xiApiKey)

Get Generated Items

Returns metadata about all your generated audio.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HistoryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    HistoryApi apiInstance = new HistoryApi(defaultClient);
    String xiApiKey = "xiApiKey_example"; // String | Your API key. This is required by most endpoints to access our API programatically. You can view your xi-api-key using the 'Profile' tab on the website.
    try {
      GetHistoryResponseModel result = apiInstance.getGeneratedItemsV1HistoryGet(xiApiKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HistoryApi#getGeneratedItemsV1HistoryGet");
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
| **xiApiKey** | **String**| Your API key. This is required by most endpoints to access our API programatically. You can view your xi-api-key using the &#39;Profile&#39; tab on the website. | [optional] |

### Return type

[**GetHistoryResponseModel**](GetHistoryResponseModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

