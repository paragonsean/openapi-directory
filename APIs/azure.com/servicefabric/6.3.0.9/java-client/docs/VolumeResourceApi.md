# VolumeResourceApi

All URIs are relative to *http://azure.local:19080*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createVolumeResource**](VolumeResourceApi.md#createVolumeResource) | **PUT** /Resources/Volumes/{volumeResourceName} | Creates or updates a volume resource. |
| [**deleteVolumeResource**](VolumeResourceApi.md#deleteVolumeResource) | **DELETE** /Resources/Volumes/{volumeResourceName} | Deletes the volume resource. |
| [**getVolumeResource**](VolumeResourceApi.md#getVolumeResource) | **GET** /Resources/Volumes/{volumeResourceName} | Gets the volume resource. |


<a id="createVolumeResource"></a>
# **createVolumeResource**
> createVolumeResource(apiVersion, volumeResourceName, volumeResourceDescription)

Creates or updates a volume resource.

Creates a volume resource with the specified name and description. If a volume with the same name already exists, then its description is updated to the one indicated in this request.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VolumeResourceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://azure.local:19080");

    VolumeResourceApi apiInstance = new VolumeResourceApi(defaultClient);
    String apiVersion = "6.3-preview"; // String | The version of the API. This parameter is required and its value must be '6.3-preview'.
    String volumeResourceName = "volumeResourceName_example"; // String | Service Fabric volume resource name.
    VolumeResourceDescription volumeResourceDescription = new VolumeResourceDescription(); // VolumeResourceDescription | Description for creating a volume resource.
    try {
      apiInstance.createVolumeResource(apiVersion, volumeResourceName, volumeResourceDescription);
    } catch (ApiException e) {
      System.err.println("Exception when calling VolumeResourceApi#createVolumeResource");
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
| **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#39;6.3-preview&#39;. | [default to 6.3-preview] [enum: 6.3-preview] |
| **volumeResourceName** | **String**| Service Fabric volume resource name. | |
| **volumeResourceDescription** | [**VolumeResourceDescription**](VolumeResourceDescription.md)| Description for creating a volume resource. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |
| **202** | Accepted |  -  |
| **0** | Error |  -  |

<a id="deleteVolumeResource"></a>
# **deleteVolumeResource**
> deleteVolumeResource(apiVersion, volumeResourceName)

Deletes the volume resource.

Deletes the volume identified by the name.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VolumeResourceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://azure.local:19080");

    VolumeResourceApi apiInstance = new VolumeResourceApi(defaultClient);
    String apiVersion = "6.3-preview"; // String | The version of the API. This parameter is required and its value must be '6.3-preview'.
    String volumeResourceName = "volumeResourceName_example"; // String | Service Fabric volume resource name.
    try {
      apiInstance.deleteVolumeResource(apiVersion, volumeResourceName);
    } catch (ApiException e) {
      System.err.println("Exception when calling VolumeResourceApi#deleteVolumeResource");
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
| **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#39;6.3-preview&#39;. | [default to 6.3-preview] [enum: 6.3-preview] |
| **volumeResourceName** | **String**| Service Fabric volume resource name. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **202** | Accepted |  -  |
| **204** | No Content - the specified volume was not found. |  -  |
| **0** | Error |  -  |

<a id="getVolumeResource"></a>
# **getVolumeResource**
> VolumeResourceDescription getVolumeResource(apiVersion, volumeResourceName)

Gets the volume resource.

Gets the information about the volume resource with a given name. This information includes the volume description and other runtime information.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VolumeResourceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://azure.local:19080");

    VolumeResourceApi apiInstance = new VolumeResourceApi(defaultClient);
    String apiVersion = "6.3-preview"; // String | The version of the API. This parameter is required and its value must be '6.3-preview'.
    String volumeResourceName = "volumeResourceName_example"; // String | Service Fabric volume resource name.
    try {
      VolumeResourceDescription result = apiInstance.getVolumeResource(apiVersion, volumeResourceName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VolumeResourceApi#getVolumeResource");
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
| **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#39;6.3-preview&#39;. | [default to 6.3-preview] [enum: 6.3-preview] |
| **volumeResourceName** | **String**| Service Fabric volume resource name. | |

### Return type

[**VolumeResourceDescription**](VolumeResourceDescription.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error |  -  |

