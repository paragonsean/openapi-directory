# ImageActionsApi

All URIs are relative to *https://api.hetzner.cloud/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**imagesIdActionsActionIdGet**](ImageActionsApi.md#imagesIdActionsActionIdGet) | **GET** /images/{id}/actions/{action_id} | Get an Action for an Image |
| [**imagesIdActionsChangeProtectionPost**](ImageActionsApi.md#imagesIdActionsChangeProtectionPost) | **POST** /images/{id}/actions/change_protection | Change Image Protection |
| [**imagesIdActionsGet**](ImageActionsApi.md#imagesIdActionsGet) | **GET** /images/{id}/actions | Get all Actions for an Image |


<a id="imagesIdActionsActionIdGet"></a>
# **imagesIdActionsActionIdGet**
> ActionResponse imagesIdActionsActionIdGet(id, actionId)

Get an Action for an Image

Returns a specific Action for an Image.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ImageActionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hetzner.cloud/v1");

    ImageActionsApi apiInstance = new ImageActionsApi(defaultClient);
    Integer id = 56; // Integer | ID of the Image
    Integer actionId = 56; // Integer | ID of the Action
    try {
      ActionResponse result = apiInstance.imagesIdActionsActionIdGet(id, actionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ImageActionsApi#imagesIdActionsActionIdGet");
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
| **200** | The &#x60;action&#x60; key contains the Image Action |  -  |

<a id="imagesIdActionsChangeProtectionPost"></a>
# **imagesIdActionsChangeProtectionPost**
> ActionResponse imagesIdActionsChangeProtectionPost(id, imagesIdActionsChangeProtectionPostRequest)

Change Image Protection

Changes the protection configuration of the Image. Can only be used on snapshots.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ImageActionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hetzner.cloud/v1");

    ImageActionsApi apiInstance = new ImageActionsApi(defaultClient);
    Integer id = 56; // Integer | ID of the Image
    ImagesIdActionsChangeProtectionPostRequest imagesIdActionsChangeProtectionPostRequest = new ImagesIdActionsChangeProtectionPostRequest(); // ImagesIdActionsChangeProtectionPostRequest | 
    try {
      ActionResponse result = apiInstance.imagesIdActionsChangeProtectionPost(id, imagesIdActionsChangeProtectionPostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ImageActionsApi#imagesIdActionsChangeProtectionPost");
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
| **imagesIdActionsChangeProtectionPostRequest** | [**ImagesIdActionsChangeProtectionPostRequest**](ImagesIdActionsChangeProtectionPostRequest.md)|  | [optional] |

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

<a id="imagesIdActionsGet"></a>
# **imagesIdActionsGet**
> ActionsResponse imagesIdActionsGet(id, sort, status)

Get all Actions for an Image

Returns all Action objects for an Image. You can sort the results by using the &#x60;sort&#x60; URI parameter, and filter them with the &#x60;status&#x60; parameter.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ImageActionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hetzner.cloud/v1");

    ImageActionsApi apiInstance = new ImageActionsApi(defaultClient);
    Integer id = 56; // Integer | ID of the Image
    String sort = "id"; // String | Can be used multiple times.
    String status = "running"; // String | Can be used multiple times, the response will contain only Actions with specified statuses
    try {
      ActionsResponse result = apiInstance.imagesIdActionsGet(id, sort, status);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ImageActionsApi#imagesIdActionsGet");
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

