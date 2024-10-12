# GalleryItemsApi

All URIs are relative to *https://adminmanagement.local.azurestack.external*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**galleryItemsCreate**](GalleryItemsApi.md#galleryItemsCreate) | **POST** /subscriptions/{subscriptionId}/providers/microsoft.gallery.admin/galleryItems | Uploads a provider gallery item to the storage. |
| [**galleryItemsDelete**](GalleryItemsApi.md#galleryItemsDelete) | **DELETE** /subscriptions/{subscriptionId}/providers/microsoft.gallery.admin/galleryItems/{galleryItemName} | Delete a specific gallery item. |
| [**galleryItemsGet**](GalleryItemsApi.md#galleryItemsGet) | **GET** /subscriptions/{subscriptionId}/providers/microsoft.gallery.admin/galleryItems/{galleryItemName} | Get a specific gallery item. |
| [**galleryItemsList**](GalleryItemsApi.md#galleryItemsList) | **GET** /subscriptions/{subscriptionId}/providers/microsoft.gallery.admin/galleryItems | Lists gallery items. |


<a id="galleryItemsCreate"></a>
# **galleryItemsCreate**
> GalleryItem galleryItemsCreate(subscriptionId, apiVersion, galleryItemUriPayload)

Uploads a provider gallery item to the storage.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GalleryItemsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://adminmanagement.local.azurestack.external");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    GalleryItemsApi apiInstance = new GalleryItemsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String apiVersion = "2016-05-01"; // String | Client API Version.
    GalleryItemUriPayload galleryItemUriPayload = new GalleryItemUriPayload(); // GalleryItemUriPayload | The URI to the gallery item JSON file.
    try {
      GalleryItem result = apiInstance.galleryItemsCreate(subscriptionId, apiVersion, galleryItemUriPayload);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GalleryItemsApi#galleryItemsCreate");
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
| **subscriptionId** | **String**| Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **apiVersion** | **String**| Client API Version. | [default to 2016-05-01] |
| **galleryItemUriPayload** | [**GalleryItemUriPayload**](GalleryItemUriPayload.md)| The URI to the gallery item JSON file. | |

### Return type

[**GalleryItem**](GalleryItem.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **201** | CREATED |  -  |

<a id="galleryItemsDelete"></a>
# **galleryItemsDelete**
> galleryItemsDelete(subscriptionId, galleryItemName, apiVersion)

Delete a specific gallery item.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GalleryItemsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://adminmanagement.local.azurestack.external");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    GalleryItemsApi apiInstance = new GalleryItemsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String galleryItemName = "galleryItemName_example"; // String | Identity of the gallery item. Includes publisher name, item name, and may include version separated by period character.
    String apiVersion = "2016-05-01"; // String | Client API Version.
    try {
      apiInstance.galleryItemsDelete(subscriptionId, galleryItemName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling GalleryItemsApi#galleryItemsDelete");
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
| **subscriptionId** | **String**| Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **galleryItemName** | **String**| Identity of the gallery item. Includes publisher name, item name, and may include version separated by period character. | |
| **apiVersion** | **String**| Client API Version. | [default to 2016-05-01] |

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **204** | NO CONTENT. |  -  |

<a id="galleryItemsGet"></a>
# **galleryItemsGet**
> GalleryItem galleryItemsGet(subscriptionId, galleryItemName, apiVersion)

Get a specific gallery item.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GalleryItemsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://adminmanagement.local.azurestack.external");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    GalleryItemsApi apiInstance = new GalleryItemsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String galleryItemName = "galleryItemName_example"; // String | Identity of the gallery item. Includes publisher name, item name, and may include version separated by period character.
    String apiVersion = "2016-05-01"; // String | Client API Version.
    try {
      GalleryItem result = apiInstance.galleryItemsGet(subscriptionId, galleryItemName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GalleryItemsApi#galleryItemsGet");
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
| **subscriptionId** | **String**| Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **galleryItemName** | **String**| Identity of the gallery item. Includes publisher name, item name, and may include version separated by period character. | |
| **apiVersion** | **String**| Client API Version. | [default to 2016-05-01] |

### Return type

[**GalleryItem**](GalleryItem.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **404** | NOT FOUND |  -  |

<a id="galleryItemsList"></a>
# **galleryItemsList**
> GalleryItemList galleryItemsList(subscriptionId, apiVersion)

Lists gallery items.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GalleryItemsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://adminmanagement.local.azurestack.external");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    GalleryItemsApi apiInstance = new GalleryItemsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String apiVersion = "2016-05-01"; // String | Client API Version.
    try {
      GalleryItemList result = apiInstance.galleryItemsList(subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GalleryItemsApi#galleryItemsList");
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
| **subscriptionId** | **String**| Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **apiVersion** | **String**| Client API Version. | [default to 2016-05-01] |

### Return type

[**GalleryItemList**](GalleryItemList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

