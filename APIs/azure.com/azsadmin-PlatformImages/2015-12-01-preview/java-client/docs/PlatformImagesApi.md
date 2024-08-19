# PlatformImagesApi

All URIs are relative to *https://adminmanagement.local.azurestack.external*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**platformImagesCreate**](PlatformImagesApi.md#platformImagesCreate) | **PUT** /subscriptions/{subscriptionId}/providers/Microsoft.Compute.Admin/locations/{location}/artifactTypes/platformImage/publishers/{publisher}/offers/{offer}/skus/{sku}/versions/{version} | Creates a platform image. |
| [**platformImagesDelete**](PlatformImagesApi.md#platformImagesDelete) | **DELETE** /subscriptions/{subscriptionId}/providers/Microsoft.Compute.Admin/locations/{location}/artifactTypes/platformImage/publishers/{publisher}/offers/{offer}/skus/{sku}/versions/{version} | Deletes a platform image matching publisher, offer, skus and version |
| [**platformImagesGet**](PlatformImagesApi.md#platformImagesGet) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Compute.Admin/locations/{location}/artifactTypes/platformImage/publishers/{publisher}/offers/{offer}/skus/{sku}/versions/{version} | Returns the requested platform image. |
| [**platformImagesList**](PlatformImagesApi.md#platformImagesList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Compute.Admin/locations/{location}/artifactTypes/platformImage | Returns all platform images. |


<a id="platformImagesCreate"></a>
# **platformImagesCreate**
> PlatformImage platformImagesCreate(subscriptionId, location, publisher, offer, sku, version, apiVersion, newImage)

Creates a platform image.

Creates a new platform image with given publisher, offer, skus and version.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PlatformImagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://adminmanagement.local.azurestack.external");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    PlatformImagesApi apiInstance = new PlatformImagesApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String location = "location_example"; // String | Location of the resource.
    String publisher = "publisher_example"; // String | Name of the publisher.
    String offer = "offer_example"; // String | Name of the offer.
    String sku = "sku_example"; // String | Name of the SKU.
    String version = "version_example"; // String | The version of the resource.
    String apiVersion = "2015-12-01-preview"; // String | Client API Version.
    PlatformImageParameters newImage = new PlatformImageParameters(); // PlatformImageParameters | New platform image.
    try {
      PlatformImage result = apiInstance.platformImagesCreate(subscriptionId, location, publisher, offer, sku, version, apiVersion, newImage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PlatformImagesApi#platformImagesCreate");
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
| **location** | **String**| Location of the resource. | |
| **publisher** | **String**| Name of the publisher. | |
| **offer** | **String**| Name of the offer. | |
| **sku** | **String**| Name of the SKU. | |
| **version** | **String**| The version of the resource. | |
| **apiVersion** | **String**| Client API Version. | [default to 2015-12-01-preview] |
| **newImage** | [**PlatformImageParameters**](PlatformImageParameters.md)| New platform image. | |

### Return type

[**PlatformImage**](PlatformImage.md)

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
| **202** | ACCEPTED |  -  |

<a id="platformImagesDelete"></a>
# **platformImagesDelete**
> platformImagesDelete(subscriptionId, location, publisher, offer, sku, version, apiVersion)

Deletes a platform image matching publisher, offer, skus and version

Delete a platform image

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PlatformImagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://adminmanagement.local.azurestack.external");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    PlatformImagesApi apiInstance = new PlatformImagesApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String location = "location_example"; // String | Location of the resource.
    String publisher = "publisher_example"; // String | Name of the publisher.
    String offer = "offer_example"; // String | Name of the offer.
    String sku = "sku_example"; // String | Name of the SKU.
    String version = "version_example"; // String | The version of the resource.
    String apiVersion = "2015-12-01-preview"; // String | Client API Version.
    try {
      apiInstance.platformImagesDelete(subscriptionId, location, publisher, offer, sku, version, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling PlatformImagesApi#platformImagesDelete");
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
| **location** | **String**| Location of the resource. | |
| **publisher** | **String**| Name of the publisher. | |
| **offer** | **String**| Name of the offer. | |
| **sku** | **String**| Name of the SKU. | |
| **version** | **String**| The version of the resource. | |
| **apiVersion** | **String**| Client API Version. | [default to 2015-12-01-preview] |

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

<a id="platformImagesGet"></a>
# **platformImagesGet**
> PlatformImage platformImagesGet(subscriptionId, location, publisher, offer, sku, version, apiVersion)

Returns the requested platform image.

Returns the specific platform image matching publisher, offer, skus and version.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PlatformImagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://adminmanagement.local.azurestack.external");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    PlatformImagesApi apiInstance = new PlatformImagesApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String location = "location_example"; // String | Location of the resource.
    String publisher = "publisher_example"; // String | Name of the publisher.
    String offer = "offer_example"; // String | Name of the offer.
    String sku = "sku_example"; // String | Name of the SKU.
    String version = "version_example"; // String | The version of the resource.
    String apiVersion = "2015-12-01-preview"; // String | Client API Version.
    try {
      PlatformImage result = apiInstance.platformImagesGet(subscriptionId, location, publisher, offer, sku, version, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PlatformImagesApi#platformImagesGet");
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
| **location** | **String**| Location of the resource. | |
| **publisher** | **String**| Name of the publisher. | |
| **offer** | **String**| Name of the offer. | |
| **sku** | **String**| Name of the SKU. | |
| **version** | **String**| The version of the resource. | |
| **apiVersion** | **String**| Client API Version. | [default to 2015-12-01-preview] |

### Return type

[**PlatformImage**](PlatformImage.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="platformImagesList"></a>
# **platformImagesList**
> List&lt;PlatformImage&gt; platformImagesList(subscriptionId, location, apiVersion)

Returns all platform images.

Returns a list of all platform images.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PlatformImagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://adminmanagement.local.azurestack.external");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    PlatformImagesApi apiInstance = new PlatformImagesApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String location = "location_example"; // String | Location of the resource.
    String apiVersion = "2015-12-01-preview"; // String | Client API Version.
    try {
      List<PlatformImage> result = apiInstance.platformImagesList(subscriptionId, location, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PlatformImagesApi#platformImagesList");
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
| **location** | **String**| Location of the resource. | |
| **apiVersion** | **String**| Client API Version. | [default to 2015-12-01-preview] |

### Return type

[**List&lt;PlatformImage&gt;**](PlatformImage.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

