# CreativeApi

All URIs are relative to *https://aiception.com/api/v2.1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**artisticImagePost**](CreativeApi.md#artisticImagePost) | **POST** /artistic_image | Create an artistic image [ image_url, style_url -&gt; id ] |
| [**artisticImageTaskIdGet**](CreativeApi.md#artisticImageTaskIdGet) | **GET** /artistic_image/{taskId} | Gets a artistic image by task id [ id -&gt; artistic image task ] |


<a id="artisticImagePost"></a>
# **artisticImagePost**
> Task artisticImagePost(body)

Create an artistic image [ image_url, style_url -&gt; id ]

Given an image content and a style image create a new stylized image of the content.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CreativeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://aiception.com/api/v2.1");
    
    // Configure HTTP basic authorization: UserSecurity
    HttpBasicAuth UserSecurity = (HttpBasicAuth) defaultClient.getAuthentication("UserSecurity");
    UserSecurity.setUsername("YOUR USERNAME");
    UserSecurity.setPassword("YOUR PASSWORD");

    CreativeApi apiInstance = new CreativeApi(defaultClient);
    ArtisticImagePostRequest body = new ArtisticImagePostRequest(); // ArtisticImagePostRequest | The content image and the style image
    try {
      Task result = apiInstance.artisticImagePost(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CreativeApi#artisticImagePost");
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
| **body** | [**ArtisticImagePostRequest**](ArtisticImagePostRequest.md)| The content image and the style image | |

### Return type

[**Task**](Task.md)

### Authorization

[UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Task succesfully created. |  -  |
| **400** | Task could not be created. |  -  |

<a id="artisticImageTaskIdGet"></a>
# **artisticImageTaskIdGet**
> Task artisticImageTaskIdGet(taskId)

Gets a artistic image by task id [ id -&gt; artistic image task ]

The artistic_image will have the urls of the stylized images.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CreativeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://aiception.com/api/v2.1");
    
    // Configure HTTP basic authorization: UserSecurity
    HttpBasicAuth UserSecurity = (HttpBasicAuth) defaultClient.getAuthentication("UserSecurity");
    UserSecurity.setUsername("YOUR USERNAME");
    UserSecurity.setPassword("YOUR PASSWORD");

    CreativeApi apiInstance = new CreativeApi(defaultClient);
    String taskId = "taskId_example"; // String | An internal id for the task
    try {
      Task result = apiInstance.artisticImageTaskIdGet(taskId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CreativeApi#artisticImageTaskIdGet");
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
| **taskId** | **String**| An internal id for the task | |

### Return type

[**Task**](Task.md)

### Authorization

[UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The contents of the artistic_image task. |  -  |
| **404** | The Task does not exists. |  -  |

