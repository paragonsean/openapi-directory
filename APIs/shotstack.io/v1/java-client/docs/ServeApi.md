# ServeApi

All URIs are relative to *https://api.shotstack.io/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**deleteAsset**](ServeApi.md#deleteAsset) | **DELETE** /assets/{id} | Delete Asset |
| [**getAsset**](ServeApi.md#getAsset) | **GET** /assets/{id} | Get Asset |
| [**getAssetByRenderId**](ServeApi.md#getAssetByRenderId) | **GET** /assets/render/{id} | Get Asset by Render ID |


<a id="deleteAsset"></a>
# **deleteAsset**
> deleteAsset(id)

Delete Asset

Delete an asset by its asset id. If a render creates multiple assets, such as thumbnail and poster images, each asset must be deleted individually by the asset id.  **base URL:** https://api.shotstack.io/serve/{version}

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.shotstack.io/v1");
    
    // Configure API key authorization: DeveloperKey
    ApiKeyAuth DeveloperKey = (ApiKeyAuth) defaultClient.getAuthentication("DeveloperKey");
    DeveloperKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //DeveloperKey.setApiKeyPrefix("Token");

    ServeApi apiInstance = new ServeApi(defaultClient);
    String id = "id_example"; // String | The id of the asset in UUID format
    try {
      apiInstance.deleteAsset(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServeApi#deleteAsset");
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
| **id** | **String**| The id of the asset in UUID format | |

### Return type

null (empty response body)

### Authorization

[DeveloperKey](../README.md#DeveloperKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | An empty response signifying the asset has been deleted |  -  |

<a id="getAsset"></a>
# **getAsset**
> AssetResponse getAsset(id)

Get Asset

The Serve API is used to interact with, and delete hosted assets including videos, images, audio files,  thumbnails and poster images. Use this endpoint to fetch an asset by asset id. Note that an asset id is unique for each asset and different from the render id.  **base URL:** https://api.shotstack.io/serve/{version}

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.shotstack.io/v1");
    
    // Configure API key authorization: DeveloperKey
    ApiKeyAuth DeveloperKey = (ApiKeyAuth) defaultClient.getAuthentication("DeveloperKey");
    DeveloperKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //DeveloperKey.setApiKeyPrefix("Token");

    ServeApi apiInstance = new ServeApi(defaultClient);
    String id = "id_example"; // String | The id of the asset in UUID format
    try {
      AssetResponse result = apiInstance.getAsset(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServeApi#getAsset");
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
| **id** | **String**| The id of the asset in UUID format | |

### Return type

[**AssetResponse**](AssetResponse.md)

### Authorization

[DeveloperKey](../README.md#DeveloperKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Get asset by asset id |  -  |

<a id="getAssetByRenderId"></a>
# **getAssetByRenderId**
> AssetRenderResponse getAssetByRenderId(id)

Get Asset by Render ID

A render may generate more than one file, such as a video, thumbnail and poster image. When the assets are created the only known id is the render id returned by the original [render request](#render-video), status  request or webhook. This endpoint lets you look up one or more assets by the render id.  **base URL:** https://api.shotstack.io/serve/{version}

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.shotstack.io/v1");
    
    // Configure API key authorization: DeveloperKey
    ApiKeyAuth DeveloperKey = (ApiKeyAuth) defaultClient.getAuthentication("DeveloperKey");
    DeveloperKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //DeveloperKey.setApiKeyPrefix("Token");

    ServeApi apiInstance = new ServeApi(defaultClient);
    String id = "id_example"; // String | The render id associated with the asset in UUID format
    try {
      AssetRenderResponse result = apiInstance.getAssetByRenderId(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServeApi#getAssetByRenderId");
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
| **id** | **String**| The render id associated with the asset in UUID format | |

### Return type

[**AssetRenderResponse**](AssetRenderResponse.md)

### Authorization

[DeveloperKey](../README.md#DeveloperKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Get one or more assets by render id |  -  |

