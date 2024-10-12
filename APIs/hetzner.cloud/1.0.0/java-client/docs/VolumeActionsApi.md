# VolumeActionsApi

All URIs are relative to *https://api.hetzner.cloud/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**volumesIdActionsActionIdGet**](VolumeActionsApi.md#volumesIdActionsActionIdGet) | **GET** /volumes/{id}/actions/{action_id} | Get an Action for a Volume |
| [**volumesIdActionsAttachPost**](VolumeActionsApi.md#volumesIdActionsAttachPost) | **POST** /volumes/{id}/actions/attach | Attach Volume to a Server |
| [**volumesIdActionsChangeProtectionPost**](VolumeActionsApi.md#volumesIdActionsChangeProtectionPost) | **POST** /volumes/{id}/actions/change_protection | Change Volume Protection |
| [**volumesIdActionsDetachPost**](VolumeActionsApi.md#volumesIdActionsDetachPost) | **POST** /volumes/{id}/actions/detach | Detach Volume |
| [**volumesIdActionsGet**](VolumeActionsApi.md#volumesIdActionsGet) | **GET** /volumes/{id}/actions | Get all Actions for a Volume |
| [**volumesIdActionsResizePost**](VolumeActionsApi.md#volumesIdActionsResizePost) | **POST** /volumes/{id}/actions/resize | Resize Volume |


<a id="volumesIdActionsActionIdGet"></a>
# **volumesIdActionsActionIdGet**
> ActionResponse volumesIdActionsActionIdGet(id, actionId)

Get an Action for a Volume

Returns a specific Action for a Volume.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VolumeActionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hetzner.cloud/v1");

    VolumeActionsApi apiInstance = new VolumeActionsApi(defaultClient);
    Integer id = 56; // Integer | ID of the Volume
    Integer actionId = 56; // Integer | ID of the Action
    try {
      ActionResponse result = apiInstance.volumesIdActionsActionIdGet(id, actionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VolumeActionsApi#volumesIdActionsActionIdGet");
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
| **actionId** | **Integer**| ID of the Action | |

### Return type

[**ActionResponse**](ActionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The &#x60;action&#x60; key contains the Volume Action |  -  |

<a id="volumesIdActionsAttachPost"></a>
# **volumesIdActionsAttachPost**
> ActionResponse volumesIdActionsAttachPost(id, attachVolumeRequest)

Attach Volume to a Server

Attaches a Volume to a Server. Works only if the Server is in the same Location as the Volume.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VolumeActionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hetzner.cloud/v1");

    VolumeActionsApi apiInstance = new VolumeActionsApi(defaultClient);
    Integer id = 56; // Integer | ID of the Volume
    AttachVolumeRequest attachVolumeRequest = new AttachVolumeRequest(); // AttachVolumeRequest | 
    try {
      ActionResponse result = apiInstance.volumesIdActionsAttachPost(id, attachVolumeRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VolumeActionsApi#volumesIdActionsAttachPost");
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
| **attachVolumeRequest** | [**AttachVolumeRequest**](AttachVolumeRequest.md)|  | [optional] |

### Return type

[**ActionResponse**](ActionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The &#x60;action&#x60; key contains the &#x60;attach_volume&#x60; Action |  -  |

<a id="volumesIdActionsChangeProtectionPost"></a>
# **volumesIdActionsChangeProtectionPost**
> ActionResponse volumesIdActionsChangeProtectionPost(id, volumesIdActionsChangeProtectionPostRequest)

Change Volume Protection

Changes the protection configuration of a Volume.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VolumeActionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hetzner.cloud/v1");

    VolumeActionsApi apiInstance = new VolumeActionsApi(defaultClient);
    Integer id = 56; // Integer | ID of the Volume
    VolumesIdActionsChangeProtectionPostRequest volumesIdActionsChangeProtectionPostRequest = new VolumesIdActionsChangeProtectionPostRequest(); // VolumesIdActionsChangeProtectionPostRequest | 
    try {
      ActionResponse result = apiInstance.volumesIdActionsChangeProtectionPost(id, volumesIdActionsChangeProtectionPostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VolumeActionsApi#volumesIdActionsChangeProtectionPost");
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
| **volumesIdActionsChangeProtectionPostRequest** | [**VolumesIdActionsChangeProtectionPostRequest**](VolumesIdActionsChangeProtectionPostRequest.md)|  | [optional] |

### Return type

[**ActionResponse**](ActionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The &#x60;action&#x60; key contains the &#x60;change_protection&#x60; Action |  -  |

<a id="volumesIdActionsDetachPost"></a>
# **volumesIdActionsDetachPost**
> ActionResponse volumesIdActionsDetachPost(id)

Detach Volume

Detaches a Volume from the Server it’s attached to. You may attach it to a Server again at a later time.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VolumeActionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hetzner.cloud/v1");

    VolumeActionsApi apiInstance = new VolumeActionsApi(defaultClient);
    Integer id = 56; // Integer | ID of the Volume
    try {
      ActionResponse result = apiInstance.volumesIdActionsDetachPost(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VolumeActionsApi#volumesIdActionsDetachPost");
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

[**ActionResponse**](ActionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The &#x60;action&#x60; key contains the &#x60;detach_volume&#x60; Action |  -  |

<a id="volumesIdActionsGet"></a>
# **volumesIdActionsGet**
> ActionsResponse volumesIdActionsGet(id, sort, status)

Get all Actions for a Volume

Returns all Action objects for a Volume. You can &#x60;sort&#x60; the results by using the sort URI parameter, and filter them with the &#x60;status&#x60; parameter.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VolumeActionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hetzner.cloud/v1");

    VolumeActionsApi apiInstance = new VolumeActionsApi(defaultClient);
    Integer id = 56; // Integer | ID of the Volume
    String sort = "id"; // String | Can be used multiple times.
    String status = "running"; // String | Can be used multiple times, the response will contain only Actions with specified statuses
    try {
      ActionsResponse result = apiInstance.volumesIdActionsGet(id, sort, status);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VolumeActionsApi#volumesIdActionsGet");
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
| **sort** | **String**| Can be used multiple times. | [optional] [enum: id, id:asc, id:desc, command, command:asc, command:desc, status, status:asc, status:desc, progress, progress:asc, progress:desc, started, started:asc, started:desc, finished, finished:asc, finished:desc] |
| **status** | **String**| Can be used multiple times, the response will contain only Actions with specified statuses | [optional] [enum: running, success, error] |

### Return type

[**ActionsResponse**](ActionsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The &#x60;actions&#x60; key contains a list of Actions |  -  |

<a id="volumesIdActionsResizePost"></a>
# **volumesIdActionsResizePost**
> ActionResponse volumesIdActionsResizePost(id, volumesIdActionsResizePostRequest)

Resize Volume

Changes the size of a Volume. Note that downsizing a Volume is not possible.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VolumeActionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hetzner.cloud/v1");

    VolumeActionsApi apiInstance = new VolumeActionsApi(defaultClient);
    Integer id = 56; // Integer | ID of the Volume
    VolumesIdActionsResizePostRequest volumesIdActionsResizePostRequest = new VolumesIdActionsResizePostRequest(); // VolumesIdActionsResizePostRequest | 
    try {
      ActionResponse result = apiInstance.volumesIdActionsResizePost(id, volumesIdActionsResizePostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VolumeActionsApi#volumesIdActionsResizePost");
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
| **volumesIdActionsResizePostRequest** | [**VolumesIdActionsResizePostRequest**](VolumesIdActionsResizePostRequest.md)|  | [optional] |

### Return type

[**ActionResponse**](ActionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The &#x60;action&#x60; key contains the &#x60;resize_volume&#x60; Action |  -  |

