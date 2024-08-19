# VirtualMachineExtensionImagesApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**virtualMachineExtensionImagesGet**](VirtualMachineExtensionImagesApi.md#virtualMachineExtensionImagesGet) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Compute/locations/{location}/publishers/{publisherName}/artifacttypes/vmextension/types/{type}/versions/{version} |  |
| [**virtualMachineExtensionImagesListTypes**](VirtualMachineExtensionImagesApi.md#virtualMachineExtensionImagesListTypes) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Compute/locations/{location}/publishers/{publisherName}/artifacttypes/vmextension/types |  |
| [**virtualMachineExtensionImagesListVersions**](VirtualMachineExtensionImagesApi.md#virtualMachineExtensionImagesListVersions) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Compute/locations/{location}/publishers/{publisherName}/artifacttypes/vmextension/types/{type}/versions |  |


<a id="virtualMachineExtensionImagesGet"></a>
# **virtualMachineExtensionImagesGet**
> VirtualMachineExtensionImage virtualMachineExtensionImagesGet(location, publisherName, type, version, apiVersion, subscriptionId)



Gets a virtual machine extension image.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VirtualMachineExtensionImagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    VirtualMachineExtensionImagesApi apiInstance = new VirtualMachineExtensionImagesApi(defaultClient);
    String location = "location_example"; // String | The name of a supported Azure region.
    String publisherName = "publisherName_example"; // String | 
    String type = "type_example"; // String | 
    String version = "version_example"; // String | 
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      VirtualMachineExtensionImage result = apiInstance.virtualMachineExtensionImagesGet(location, publisherName, type, version, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VirtualMachineExtensionImagesApi#virtualMachineExtensionImagesGet");
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
| **publisherName** | **String**|  | |
| **type** | **String**|  | |
| **version** | **String**|  | |
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

### Return type

[**VirtualMachineExtensionImage**](VirtualMachineExtensionImage.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="virtualMachineExtensionImagesListTypes"></a>
# **virtualMachineExtensionImagesListTypes**
> List&lt;VirtualMachineExtensionImage&gt; virtualMachineExtensionImagesListTypes(location, publisherName, apiVersion, subscriptionId)



Gets a list of virtual machine extension image types.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VirtualMachineExtensionImagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    VirtualMachineExtensionImagesApi apiInstance = new VirtualMachineExtensionImagesApi(defaultClient);
    String location = "location_example"; // String | The name of a supported Azure region.
    String publisherName = "publisherName_example"; // String | 
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      List<VirtualMachineExtensionImage> result = apiInstance.virtualMachineExtensionImagesListTypes(location, publisherName, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VirtualMachineExtensionImagesApi#virtualMachineExtensionImagesListTypes");
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
| **publisherName** | **String**|  | |
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

### Return type

[**List&lt;VirtualMachineExtensionImage&gt;**](VirtualMachineExtensionImage.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="virtualMachineExtensionImagesListVersions"></a>
# **virtualMachineExtensionImagesListVersions**
> List&lt;VirtualMachineExtensionImage&gt; virtualMachineExtensionImagesListVersions(location, publisherName, type, apiVersion, subscriptionId, $filter, $top, $orderby)



Gets a list of virtual machine extension image versions.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VirtualMachineExtensionImagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    VirtualMachineExtensionImagesApi apiInstance = new VirtualMachineExtensionImagesApi(defaultClient);
    String location = "location_example"; // String | The name of a supported Azure region.
    String publisherName = "publisherName_example"; // String | 
    String type = "type_example"; // String | 
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String $filter = "$filter_example"; // String | The filter to apply on the operation.
    Integer $top = 56; // Integer | 
    String $orderby = "$orderby_example"; // String | 
    try {
      List<VirtualMachineExtensionImage> result = apiInstance.virtualMachineExtensionImagesListVersions(location, publisherName, type, apiVersion, subscriptionId, $filter, $top, $orderby);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VirtualMachineExtensionImagesApi#virtualMachineExtensionImagesListVersions");
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
| **publisherName** | **String**|  | |
| **type** | **String**|  | |
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **$filter** | **String**| The filter to apply on the operation. | [optional] |
| **$top** | **Integer**|  | [optional] |
| **$orderby** | **String**|  | [optional] |

### Return type

[**List&lt;VirtualMachineExtensionImage&gt;**](VirtualMachineExtensionImage.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

