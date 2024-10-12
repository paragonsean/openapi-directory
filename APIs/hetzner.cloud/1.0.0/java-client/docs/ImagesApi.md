# ImagesApi

All URIs are relative to *https://api.hetzner.cloud/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**imagesGet**](ImagesApi.md#imagesGet) | **GET** /images | Get all Images |
| [**imagesIdDelete**](ImagesApi.md#imagesIdDelete) | **DELETE** /images/{id} | Delete an Image |
| [**imagesIdGet**](ImagesApi.md#imagesIdGet) | **GET** /images/{id} | Get an Image |
| [**imagesIdPut**](ImagesApi.md#imagesIdPut) | **PUT** /images/{id} | Update an Image |


<a id="imagesGet"></a>
# **imagesGet**
> ImagesGet200Response imagesGet(sort, type, status, boundTo, includeDeprecated, name, labelSelector, architecture)

Get all Images

Returns all Image objects. You can select specific Image types only and sort the results by using URI parameters.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ImagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hetzner.cloud/v1");

    ImagesApi apiInstance = new ImagesApi(defaultClient);
    String sort = "id"; // String | Can be used multiple times.
    String type = "system"; // String | Can be used multiple times.
    String status = "available"; // String | Can be used multiple times. The response will only contain Images matching the status.
    String boundTo = "boundTo_example"; // String | Can be used multiple times. Server ID linked to the Image. Only available for Images of type `backup`
    Boolean includeDeprecated = true; // Boolean | Can be used multiple times.
    String name = "name_example"; // String | Can be used to filter resources by their name. The response will only contain the resources matching the specified name
    String labelSelector = "labelSelector_example"; // String | Can be used to filter resources by labels. The response will only contain resources matching the label selector.
    String architecture = "architecture_example"; // String | Return only Images with the given architecture.
    try {
      ImagesGet200Response result = apiInstance.imagesGet(sort, type, status, boundTo, includeDeprecated, name, labelSelector, architecture);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ImagesApi#imagesGet");
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
| **sort** | **String**| Can be used multiple times. | [optional] [enum: id, id:asc, id:desc, name, name:asc, name:desc, created, created:asc, created:desc] |
| **type** | **String**| Can be used multiple times. | [optional] [enum: system, snapshot, backup, app] |
| **status** | **String**| Can be used multiple times. The response will only contain Images matching the status. | [optional] [enum: available, creating] |
| **boundTo** | **String**| Can be used multiple times. Server ID linked to the Image. Only available for Images of type &#x60;backup&#x60; | [optional] |
| **includeDeprecated** | **Boolean**| Can be used multiple times. | [optional] |
| **name** | **String**| Can be used to filter resources by their name. The response will only contain the resources matching the specified name | [optional] |
| **labelSelector** | **String**| Can be used to filter resources by labels. The response will only contain resources matching the label selector. | [optional] |
| **architecture** | **String**| Return only Images with the given architecture. | [optional] |

### Return type

[**ImagesGet200Response**](ImagesGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The &#x60;images&#x60; key in the reply contains an array of Image objects with this structure |  -  |

<a id="imagesIdDelete"></a>
# **imagesIdDelete**
> imagesIdDelete(id)

Delete an Image

Deletes an Image. Only Images of type &#x60;snapshot&#x60; and &#x60;backup&#x60; can be deleted.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ImagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hetzner.cloud/v1");

    ImagesApi apiInstance = new ImagesApi(defaultClient);
    Integer id = 56; // Integer | ID of the Image
    try {
      apiInstance.imagesIdDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling ImagesApi#imagesIdDelete");
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
| **id** | **Integer**| ID of the Image | |

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
| **204** | Image deleted |  -  |

<a id="imagesIdGet"></a>
# **imagesIdGet**
> ImagesIdGet200Response imagesIdGet(id)

Get an Image

Returns a specific Image object.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ImagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hetzner.cloud/v1");

    ImagesApi apiInstance = new ImagesApi(defaultClient);
    Integer id = 56; // Integer | ID of the Image
    try {
      ImagesIdGet200Response result = apiInstance.imagesIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ImagesApi#imagesIdGet");
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
| **id** | **Integer**| ID of the Image | |

### Return type

[**ImagesIdGet200Response**](ImagesIdGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The &#x60;image&#x60; key in the reply contains an Image object with this structure |  -  |

<a id="imagesIdPut"></a>
# **imagesIdPut**
> ImagesIdGet200Response imagesIdPut(id, updateImageRequest)

Update an Image

Updates the Image. You may change the description, convert a Backup Image to a Snapshot Image or change the Image labels. Only Images of type &#x60;snapshot&#x60; and &#x60;backup&#x60; can be updated.  Note that when updating labels, the current set of labels will be replaced with the labels provided in the request body. So, for example, if you want to add a new label, you have to provide all existing labels plus the new label in the request body. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ImagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hetzner.cloud/v1");

    ImagesApi apiInstance = new ImagesApi(defaultClient);
    Integer id = 56; // Integer | ID of the Image
    UpdateImageRequest updateImageRequest = new UpdateImageRequest(); // UpdateImageRequest | 
    try {
      ImagesIdGet200Response result = apiInstance.imagesIdPut(id, updateImageRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ImagesApi#imagesIdPut");
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
| **id** | **Integer**| ID of the Image | |
| **updateImageRequest** | [**UpdateImageRequest**](UpdateImageRequest.md)|  | [optional] |

### Return type

[**ImagesIdGet200Response**](ImagesIdGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The image key in the reply contains the modified Image object |  -  |

