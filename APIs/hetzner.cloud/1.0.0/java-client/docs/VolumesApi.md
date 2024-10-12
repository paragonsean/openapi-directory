# VolumesApi

All URIs are relative to *https://api.hetzner.cloud/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**volumesGet**](VolumesApi.md#volumesGet) | **GET** /volumes | Get all Volumes |
| [**volumesIdDelete**](VolumesApi.md#volumesIdDelete) | **DELETE** /volumes/{id} | Delete a Volume |
| [**volumesIdGet**](VolumesApi.md#volumesIdGet) | **GET** /volumes/{id} | Get a Volume |
| [**volumesIdPut**](VolumesApi.md#volumesIdPut) | **PUT** /volumes/{id} | Update a Volume |
| [**volumesPost**](VolumesApi.md#volumesPost) | **POST** /volumes | Create a Volume |


<a id="volumesGet"></a>
# **volumesGet**
> VolumesGet200Response volumesGet(status, sort, name, labelSelector)

Get all Volumes

Gets all existing Volumes that you have available.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VolumesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hetzner.cloud/v1");

    VolumesApi apiInstance = new VolumesApi(defaultClient);
    String status = "available"; // String | Can be used multiple times. The response will only contain Volumes matching the status.
    String sort = "id"; // String | Can be used multiple times.
    String name = "name_example"; // String | Can be used to filter resources by their name. The response will only contain the resources matching the specified name
    String labelSelector = "labelSelector_example"; // String | Can be used to filter resources by labels. The response will only contain resources matching the label selector.
    try {
      VolumesGet200Response result = apiInstance.volumesGet(status, sort, name, labelSelector);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VolumesApi#volumesGet");
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
| **status** | **String**| Can be used multiple times. The response will only contain Volumes matching the status. | [optional] [enum: available, creating] |
| **sort** | **String**| Can be used multiple times. | [optional] [enum: id, id:asc, id:desc, name, name:asc, name:desc, created, created:asc, created:desc] |
| **name** | **String**| Can be used to filter resources by their name. The response will only contain the resources matching the specified name | [optional] |
| **labelSelector** | **String**| Can be used to filter resources by labels. The response will only contain resources matching the label selector. | [optional] |

### Return type

[**VolumesGet200Response**](VolumesGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The &#x60;volumes&#x60; key contains a list of volumes |  -  |

<a id="volumesIdDelete"></a>
# **volumesIdDelete**
> volumesIdDelete(id)

Delete a Volume

Deletes a volume. All Volume data is irreversibly destroyed. The Volume must not be attached to a Server and it must not have delete protection enabled.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VolumesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hetzner.cloud/v1");

    VolumesApi apiInstance = new VolumesApi(defaultClient);
    String id = "id_example"; // String | ID of the Volume
    try {
      apiInstance.volumesIdDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling VolumesApi#volumesIdDelete");
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
| **id** | **String**| ID of the Volume | |

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
| **204** | Volume deleted |  -  |

<a id="volumesIdGet"></a>
# **volumesIdGet**
> VolumesIdGet200Response volumesIdGet(id)

Get a Volume

Gets a specific Volume object.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VolumesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hetzner.cloud/v1");

    VolumesApi apiInstance = new VolumesApi(defaultClient);
    Integer id = 56; // Integer | ID of the Volume
    try {
      VolumesIdGet200Response result = apiInstance.volumesIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VolumesApi#volumesIdGet");
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
| **id** | **Integer**| ID of the Volume | |

### Return type

[**VolumesIdGet200Response**](VolumesIdGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The &#x60;volume&#x60; key contains the volume |  -  |

<a id="volumesIdPut"></a>
# **volumesIdPut**
> VolumesIdGet200Response volumesIdPut(id, updateVolumeRequest)

Update a Volume

Updates the Volume properties.  Note that when updating labels, the volume’s current set of labels will be replaced with the labels provided in the request body. So, for example, if you want to add a new label, you have to provide all existing labels plus the new label in the request body. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VolumesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hetzner.cloud/v1");

    VolumesApi apiInstance = new VolumesApi(defaultClient);
    String id = "id_example"; // String | ID of the Volume to update
    UpdateVolumeRequest updateVolumeRequest = new UpdateVolumeRequest(); // UpdateVolumeRequest | 
    try {
      VolumesIdGet200Response result = apiInstance.volumesIdPut(id, updateVolumeRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VolumesApi#volumesIdPut");
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
| **id** | **String**| ID of the Volume to update | |
| **updateVolumeRequest** | [**UpdateVolumeRequest**](UpdateVolumeRequest.md)|  | [optional] |

### Return type

[**VolumesIdGet200Response**](VolumesIdGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The &#x60;volume&#x60; key contains the updated volume |  -  |

<a id="volumesPost"></a>
# **volumesPost**
> VolumesPost201Response volumesPost(createVolumeRequest)

Create a Volume

Creates a new Volume attached to a Server. If you want to create a Volume that is not attached to a Server, you need to provide the &#x60;location&#x60; key instead of &#x60;server&#x60;. This can be either the ID or the name of the Location this Volume will be created in. Note that a Volume can be attached to a Server only in the same Location as the Volume itself.  Specifying the Server during Volume creation will automatically attach the Volume to that Server after it has been initialized. In that case, the &#x60;next_actions&#x60; key in the response is an array which contains a single &#x60;attach_volume&#x60; action.  The minimum Volume size is 10GB and the maximum size is 10TB (10240GB).  A volume’s name can consist of alphanumeric characters, dashes, underscores, and dots, but has to start and end with an alphanumeric character. The total length is limited to 64 characters. Volume names must be unique per Project.  #### Call specific error codes  | Code                                | Description                                         | |-------------------------------------|-----------------------------------------------------| | &#x60;no_space_left_in_location&#x60;         | There is no volume space left in the given location | 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VolumesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hetzner.cloud/v1");

    VolumesApi apiInstance = new VolumesApi(defaultClient);
    CreateVolumeRequest createVolumeRequest = new CreateVolumeRequest(); // CreateVolumeRequest | 
    try {
      VolumesPost201Response result = apiInstance.volumesPost(createVolumeRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VolumesApi#volumesPost");
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
| **createVolumeRequest** | [**CreateVolumeRequest**](CreateVolumeRequest.md)|  | [optional] |

### Return type

[**VolumesPost201Response**](VolumesPost201Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The &#x60;volume&#x60; key contains the Volume that was just created  The &#x60;action&#x60; key contains the Action tracking Volume creation  |  -  |

