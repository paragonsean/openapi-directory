# VirtualMachineImagesApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**virtualMachineImagesGet**](VirtualMachineImagesApi.md#virtualMachineImagesGet) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Compute/locations/{location}/publishers/{publisherName}/artifacttypes/vmimage/offers/{offer}/skus/{skus}/versions/{version} |  |
| [**virtualMachineImagesList**](VirtualMachineImagesApi.md#virtualMachineImagesList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Compute/locations/{location}/publishers/{publisherName}/artifacttypes/vmimage/offers/{offer}/skus/{skus}/versions |  |
| [**virtualMachineImagesListOffers**](VirtualMachineImagesApi.md#virtualMachineImagesListOffers) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Compute/locations/{location}/publishers/{publisherName}/artifacttypes/vmimage/offers |  |
| [**virtualMachineImagesListPublishers**](VirtualMachineImagesApi.md#virtualMachineImagesListPublishers) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Compute/locations/{location}/publishers |  |
| [**virtualMachineImagesListSkus**](VirtualMachineImagesApi.md#virtualMachineImagesListSkus) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Compute/locations/{location}/publishers/{publisherName}/artifacttypes/vmimage/offers/{offer}/skus |  |


<a id="virtualMachineImagesGet"></a>
# **virtualMachineImagesGet**
> VirtualMachineImage virtualMachineImagesGet(location, publisherName, offer, skus, version, apiVersion, subscriptionId)



Gets a virtual machine image.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VirtualMachineImagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    VirtualMachineImagesApi apiInstance = new VirtualMachineImagesApi(defaultClient);
    String location = "location_example"; // String | The name of a supported Azure region.
    String publisherName = "publisherName_example"; // String | A valid image publisher.
    String offer = "offer_example"; // String | A valid image publisher offer.
    String skus = "skus_example"; // String | A valid image SKU.
    String version = "version_example"; // String | A valid image SKU version.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      VirtualMachineImage result = apiInstance.virtualMachineImagesGet(location, publisherName, offer, skus, version, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VirtualMachineImagesApi#virtualMachineImagesGet");
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
| **location** | **String**| The name of a supported Azure region. | |
| **publisherName** | **String**| A valid image publisher. | |
| **offer** | **String**| A valid image publisher offer. | |
| **skus** | **String**| A valid image SKU. | |
| **version** | **String**| A valid image SKU version. | |
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

### Return type

[**VirtualMachineImage**](VirtualMachineImage.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="virtualMachineImagesList"></a>
# **virtualMachineImagesList**
> List&lt;VirtualMachineImageResource&gt; virtualMachineImagesList(location, publisherName, offer, skus, apiVersion, subscriptionId, $filter, $top, $orderby)



Gets a list of all virtual machine image versions for the specified location, publisher, offer, and SKU.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VirtualMachineImagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    VirtualMachineImagesApi apiInstance = new VirtualMachineImagesApi(defaultClient);
    String location = "location_example"; // String | The name of a supported Azure region.
    String publisherName = "publisherName_example"; // String | A valid image publisher.
    String offer = "offer_example"; // String | A valid image publisher offer.
    String skus = "skus_example"; // String | A valid image SKU.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String $filter = "$filter_example"; // String | The filter to apply on the operation.
    Integer $top = 56; // Integer | 
    String $orderby = "$orderby_example"; // String | 
    try {
      List<VirtualMachineImageResource> result = apiInstance.virtualMachineImagesList(location, publisherName, offer, skus, apiVersion, subscriptionId, $filter, $top, $orderby);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VirtualMachineImagesApi#virtualMachineImagesList");
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
| **location** | **String**| The name of a supported Azure region. | |
| **publisherName** | **String**| A valid image publisher. | |
| **offer** | **String**| A valid image publisher offer. | |
| **skus** | **String**| A valid image SKU. | |
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **$filter** | **String**| The filter to apply on the operation. | [optional] |
| **$top** | **Integer**|  | [optional] |
| **$orderby** | **String**|  | [optional] |

### Return type

[**List&lt;VirtualMachineImageResource&gt;**](VirtualMachineImageResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="virtualMachineImagesListOffers"></a>
# **virtualMachineImagesListOffers**
> List&lt;VirtualMachineImageResource&gt; virtualMachineImagesListOffers(location, publisherName, apiVersion, subscriptionId)



Gets a list of virtual machine image offers for the specified location and publisher.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VirtualMachineImagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    VirtualMachineImagesApi apiInstance = new VirtualMachineImagesApi(defaultClient);
    String location = "location_example"; // String | The name of a supported Azure region.
    String publisherName = "publisherName_example"; // String | A valid image publisher.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      List<VirtualMachineImageResource> result = apiInstance.virtualMachineImagesListOffers(location, publisherName, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VirtualMachineImagesApi#virtualMachineImagesListOffers");
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
| **location** | **String**| The name of a supported Azure region. | |
| **publisherName** | **String**| A valid image publisher. | |
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

### Return type

[**List&lt;VirtualMachineImageResource&gt;**](VirtualMachineImageResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="virtualMachineImagesListPublishers"></a>
# **virtualMachineImagesListPublishers**
> List&lt;VirtualMachineImageResource&gt; virtualMachineImagesListPublishers(location, apiVersion, subscriptionId)



Gets a list of virtual machine image publishers for the specified Azure location.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VirtualMachineImagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    VirtualMachineImagesApi apiInstance = new VirtualMachineImagesApi(defaultClient);
    String location = "location_example"; // String | The name of a supported Azure region.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      List<VirtualMachineImageResource> result = apiInstance.virtualMachineImagesListPublishers(location, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VirtualMachineImagesApi#virtualMachineImagesListPublishers");
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
| **location** | **String**| The name of a supported Azure region. | |
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

### Return type

[**List&lt;VirtualMachineImageResource&gt;**](VirtualMachineImageResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="virtualMachineImagesListSkus"></a>
# **virtualMachineImagesListSkus**
> List&lt;VirtualMachineImageResource&gt; virtualMachineImagesListSkus(location, publisherName, offer, apiVersion, subscriptionId)



Gets a list of virtual machine image SKUs for the specified location, publisher, and offer.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VirtualMachineImagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    VirtualMachineImagesApi apiInstance = new VirtualMachineImagesApi(defaultClient);
    String location = "location_example"; // String | The name of a supported Azure region.
    String publisherName = "publisherName_example"; // String | A valid image publisher.
    String offer = "offer_example"; // String | A valid image publisher offer.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      List<VirtualMachineImageResource> result = apiInstance.virtualMachineImagesListSkus(location, publisherName, offer, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VirtualMachineImagesApi#virtualMachineImagesListSkus");
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
| **location** | **String**| The name of a supported Azure region. | |
| **publisherName** | **String**| A valid image publisher. | |
| **offer** | **String**| A valid image publisher offer. | |
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

### Return type

[**List&lt;VirtualMachineImageResource&gt;**](VirtualMachineImageResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

