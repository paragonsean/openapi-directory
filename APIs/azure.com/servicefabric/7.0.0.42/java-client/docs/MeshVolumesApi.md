# MeshVolumesApi

All URIs are relative to *http://azure.local:19080*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**meshVolumeCreateOrUpdate**](MeshVolumesApi.md#meshVolumeCreateOrUpdate) | **PUT** /Resources/Volumes/{volumeResourceName} | Creates or updates a Volume resource. |
| [**meshVolumeDelete**](MeshVolumesApi.md#meshVolumeDelete) | **DELETE** /Resources/Volumes/{volumeResourceName} | Deletes the Volume resource. |
| [**meshVolumeGet**](MeshVolumesApi.md#meshVolumeGet) | **GET** /Resources/Volumes/{volumeResourceName} | Gets the Volume resource with the given name. |
| [**meshVolumeList**](MeshVolumesApi.md#meshVolumeList) | **GET** /Resources/Volumes | Lists all the volume resources. |


<a id="meshVolumeCreateOrUpdate"></a>
# **meshVolumeCreateOrUpdate**
> VolumeResourceDescription meshVolumeCreateOrUpdate(apiVersion, volumeResourceName, volumeResourceDescription)

Creates or updates a Volume resource.

Creates a Volume resource with the specified name, description and properties. If Volume resource with the same name exists, then it is updated with the specified description and properties.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MeshVolumesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://azure.local:19080");

    MeshVolumesApi apiInstance = new MeshVolumesApi(defaultClient);
    String apiVersion = "6.4-preview"; // String | The version of the API. This parameter is required and its value must be '6.4-preview'.
    String volumeResourceName = "volumeResourceName_example"; // String | The identity of the volume.
    VolumeResourceDescription volumeResourceDescription = new VolumeResourceDescription(); // VolumeResourceDescription | Description for creating a Volume resource.
    try {
      VolumeResourceDescription result = apiInstance.meshVolumeCreateOrUpdate(apiVersion, volumeResourceName, volumeResourceDescription);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MeshVolumesApi#meshVolumeCreateOrUpdate");
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
| **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#39;6.4-preview&#39;. | [default to 6.4-preview] [enum: 6.4-preview] |
| **volumeResourceName** | **String**| The identity of the volume. | |
| **volumeResourceDescription** | [**VolumeResourceDescription**](VolumeResourceDescription.md)| Description for creating a Volume resource. | |

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
| **201** | Created |  -  |
| **202** | Accepted |  -  |
| **0** | Error |  -  |

<a id="meshVolumeDelete"></a>
# **meshVolumeDelete**
> meshVolumeDelete(apiVersion, volumeResourceName)

Deletes the Volume resource.

Deletes the Volume resource identified by the name.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MeshVolumesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://azure.local:19080");

    MeshVolumesApi apiInstance = new MeshVolumesApi(defaultClient);
    String apiVersion = "6.4-preview"; // String | The version of the API. This parameter is required and its value must be '6.4-preview'.
    String volumeResourceName = "volumeResourceName_example"; // String | The identity of the volume.
    try {
      apiInstance.meshVolumeDelete(apiVersion, volumeResourceName);
    } catch (ApiException e) {
      System.err.println("Exception when calling MeshVolumesApi#meshVolumeDelete");
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
| **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#39;6.4-preview&#39;. | [default to 6.4-preview] [enum: 6.4-preview] |
| **volumeResourceName** | **String**| The identity of the volume. | |

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

<a id="meshVolumeGet"></a>
# **meshVolumeGet**
> VolumeResourceDescription meshVolumeGet(apiVersion, volumeResourceName)

Gets the Volume resource with the given name.

Gets the information about the Volume resource with the given name. The information include the description and other properties of the Volume.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MeshVolumesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://azure.local:19080");

    MeshVolumesApi apiInstance = new MeshVolumesApi(defaultClient);
    String apiVersion = "6.4-preview"; // String | The version of the API. This parameter is required and its value must be '6.4-preview'.
    String volumeResourceName = "volumeResourceName_example"; // String | The identity of the volume.
    try {
      VolumeResourceDescription result = apiInstance.meshVolumeGet(apiVersion, volumeResourceName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MeshVolumesApi#meshVolumeGet");
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
| **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#39;6.4-preview&#39;. | [default to 6.4-preview] [enum: 6.4-preview] |
| **volumeResourceName** | **String**| The identity of the volume. | |

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

<a id="meshVolumeList"></a>
# **meshVolumeList**
> PagedVolumeResourceDescriptionList meshVolumeList(apiVersion)

Lists all the volume resources.

Gets the information about all volume resources in a given resource group. The information include the description and other properties of the Volume.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MeshVolumesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://azure.local:19080");

    MeshVolumesApi apiInstance = new MeshVolumesApi(defaultClient);
    String apiVersion = "6.4-preview"; // String | The version of the API. This parameter is required and its value must be '6.4-preview'.
    try {
      PagedVolumeResourceDescriptionList result = apiInstance.meshVolumeList(apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MeshVolumesApi#meshVolumeList");
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
| **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#39;6.4-preview&#39;. | [default to 6.4-preview] [enum: 6.4-preview] |

### Return type

[**PagedVolumeResourceDescriptionList**](PagedVolumeResourceDescriptionList.md)

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

