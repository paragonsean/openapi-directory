# VideosUploadApi

All URIs are relative to *https://api.vimeo.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**completeStreamingUpload**](VideosUploadApi.md#completeStreamingUpload) | **DELETE** /users/{user_id}/uploads/{upload} | Complete a user&#39;s streaming upload |
| [**getUploadAttempt**](VideosUploadApi.md#getUploadAttempt) | **GET** /users/{user_id}/uploads/{upload} | Get a user&#39;s upload attempt |
| [**uploadVideo**](VideosUploadApi.md#uploadVideo) | **POST** /users/{user_id}/videos | Upload a video |
| [**uploadVideoAlt1**](VideosUploadApi.md#uploadVideoAlt1) | **POST** /me/videos | Upload a video |


<a id="completeStreamingUpload"></a>
# **completeStreamingUpload**
> completeStreamingUpload(upload, userId, signature, videoFileId)

Complete a user&#39;s streaming upload

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideosUploadApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.vimeo.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    VideosUploadApi apiInstance = new VideosUploadApi(defaultClient);
    BigDecimal upload = new BigDecimal("12345"); // BigDecimal | The ID of the upload attempt.
    BigDecimal userId = new BigDecimal("152184"); // BigDecimal | The ID of the user.
    String signature = "cd89a20adde7a608f3331e71c37bdfa087bacbf3"; // String | The crypto signature of the completed upload.
    BigDecimal videoFileId = new BigDecimal("1234"); // BigDecimal | The ID of the uploaded file.
    try {
      apiInstance.completeStreamingUpload(upload, userId, signature, videoFileId);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideosUploadApi#completeStreamingUpload");
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
| **upload** | **BigDecimal**| The ID of the upload attempt. | |
| **userId** | **BigDecimal**| The ID of the user. | |
| **signature** | **String**| The crypto signature of the completed upload. | |
| **videoFileId** | **BigDecimal**| The ID of the uploaded file. | |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The streaming upload is complete. |  -  |
| **400** | Error code 2502: The format of the video file is invalid. |  -  |
| **404** | * Error code 5006: The video file doesn&#39;t exist. * Error code 5007: The signature doesn&#39;t exist. * Error code 8400: The signature is invalid. |  -  |
| **500** | Error code 4011: The upload server returns an HTTP status code other than 200. |  -  |

<a id="getUploadAttempt"></a>
# **getUploadAttempt**
> UploadAttempt getUploadAttempt(upload, userId)

Get a user&#39;s upload attempt

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideosUploadApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.vimeo.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    VideosUploadApi apiInstance = new VideosUploadApi(defaultClient);
    BigDecimal upload = new BigDecimal("12345"); // BigDecimal | The ID of the upload attempt.
    BigDecimal userId = new BigDecimal("152184"); // BigDecimal | The ID of the user.
    try {
      UploadAttempt result = apiInstance.getUploadAttempt(upload, userId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideosUploadApi#getUploadAttempt");
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
| **upload** | **BigDecimal**| The ID of the upload attempt. | |
| **userId** | **BigDecimal**| The ID of the user. | |

### Return type

[**UploadAttempt**](UploadAttempt.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.vimeo.uploadattempt+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The upload attempt was returned. |  -  |

<a id="uploadVideo"></a>
# **uploadVideo**
> Video uploadVideo(userId, uploadVideoAlt1Request)

Upload a video

Begin the video upload process. For more information, see our [upload documentation](https://developer.vimeo.com/api/upload/videos).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideosUploadApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.vimeo.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    VideosUploadApi apiInstance = new VideosUploadApi(defaultClient);
    BigDecimal userId = new BigDecimal("152184"); // BigDecimal | The ID of the user.
    UploadVideoAlt1Request uploadVideoAlt1Request = new UploadVideoAlt1Request(); // UploadVideoAlt1Request | 
    try {
      Video result = apiInstance.uploadVideo(userId, uploadVideoAlt1Request);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideosUploadApi#uploadVideo");
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
| **userId** | **BigDecimal**| The ID of the user. | |
| **uploadVideoAlt1Request** | [**UploadVideoAlt1Request**](UploadVideoAlt1Request.md)|  | |

### Return type

[**Video**](Video.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/vnd.vimeo.video+json
 - **Accept**: application/vnd.vimeo.video+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The upload procedure has begun. |  -  |
| **400** | * Error code 2205: The body of the request isn&#39;t formatted properly. * Error code 2204: The request contains invalid parameters. * Error code 2204: The request contains invalid body parameters. * Error code 2230: The upload type is invalid. * Error code 3116: If a &#x60;type&#x60; payload parameter was supplied instead of &#x60;upload.approach&#x60;. |  -  |
| **401** | Error code 8002: No user is associated with the authentication token. |  -  |
| **403** | * Error code 4102: The user&#39;s allotted quota has been reached. * Error code 4101: The user&#39;s maximum disk space has been reached. |  -  |
| **500** | Error code 4003: There is a problem initiating the upload. |  -  |

<a id="uploadVideoAlt1"></a>
# **uploadVideoAlt1**
> Video uploadVideoAlt1(uploadVideoAlt1Request)

Upload a video

Begin the video upload process. For more information, see our [upload documentation](https://developer.vimeo.com/api/upload/videos).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideosUploadApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.vimeo.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    VideosUploadApi apiInstance = new VideosUploadApi(defaultClient);
    UploadVideoAlt1Request uploadVideoAlt1Request = new UploadVideoAlt1Request(); // UploadVideoAlt1Request | 
    try {
      Video result = apiInstance.uploadVideoAlt1(uploadVideoAlt1Request);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideosUploadApi#uploadVideoAlt1");
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
| **uploadVideoAlt1Request** | [**UploadVideoAlt1Request**](UploadVideoAlt1Request.md)|  | |

### Return type

[**Video**](Video.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/vnd.vimeo.video+json
 - **Accept**: application/vnd.vimeo.video+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The upload procedure has begun. |  -  |
| **400** | * Error code 2205: The body of the request isn&#39;t formatted properly. * Error code 2204: The request contains invalid parameters. * Error code 2204: The request contains invalid body parameters. * Error code 2230: The upload type is invalid. * Error code 3116: If a &#x60;type&#x60; payload parameter was supplied instead of &#x60;upload.approach&#x60;. |  -  |
| **401** | Error code 8002: No user is associated with the authentication token. |  -  |
| **403** | * Error code 4102: The user&#39;s allotted quota has been reached. * Error code 4101: The user&#39;s maximum disk space has been reached. |  -  |
| **500** | Error code 4003: There is a problem initiating the upload. |  -  |

