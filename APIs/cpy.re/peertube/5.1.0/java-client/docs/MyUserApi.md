# MyUserApi

All URIs are relative to *https://peertube2.cpy.re*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiV1UsersMeAvatarDelete**](MyUserApi.md#apiV1UsersMeAvatarDelete) | **DELETE** /api/v1/users/me/avatar | Delete my avatar |
| [**apiV1UsersMeAvatarPickPost**](MyUserApi.md#apiV1UsersMeAvatarPickPost) | **POST** /api/v1/users/me/avatar/pick | Update my user avatar |
| [**apiV1UsersMeVideoQuotaUsedGet**](MyUserApi.md#apiV1UsersMeVideoQuotaUsedGet) | **GET** /api/v1/users/me/video-quota-used | Get my user used quota |
| [**apiV1UsersMeVideosGet**](MyUserApi.md#apiV1UsersMeVideosGet) | **GET** /api/v1/users/me/videos | Get videos of my user |
| [**apiV1UsersMeVideosImportsGet_0**](MyUserApi.md#apiV1UsersMeVideosImportsGet_0) | **GET** /api/v1/users/me/videos/imports | Get video imports of my user |
| [**apiV1UsersMeVideosVideoIdRatingGet**](MyUserApi.md#apiV1UsersMeVideosVideoIdRatingGet) | **GET** /api/v1/users/me/videos/{videoId}/rating | Get rate of my user for a video |
| [**getMyAbuses_0**](MyUserApi.md#getMyAbuses_0) | **GET** /api/v1/users/me/abuses | List my abuses |
| [**getUserInfo**](MyUserApi.md#getUserInfo) | **GET** /api/v1/users/me | Get my user information |
| [**putUserInfo**](MyUserApi.md#putUserInfo) | **PUT** /api/v1/users/me | Update my user information |


<a id="apiV1UsersMeAvatarDelete"></a>
# **apiV1UsersMeAvatarDelete**
> apiV1UsersMeAvatarDelete()

Delete my avatar

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MyUserApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://peertube2.cpy.re");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    MyUserApi apiInstance = new MyUserApi(defaultClient);
    try {
      apiInstance.apiV1UsersMeAvatarDelete();
    } catch (ApiException e) {
      System.err.println("Exception when calling MyUserApi#apiV1UsersMeAvatarDelete");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | successful operation |  -  |

<a id="apiV1UsersMeAvatarPickPost"></a>
# **apiV1UsersMeAvatarPickPost**
> ApiV1UsersMeAvatarPickPost200Response apiV1UsersMeAvatarPickPost(avatarfile)

Update my user avatar

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MyUserApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://peertube2.cpy.re");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    MyUserApi apiInstance = new MyUserApi(defaultClient);
    File avatarfile = new File("/path/to/file"); // File | The file to upload
    try {
      ApiV1UsersMeAvatarPickPost200Response result = apiInstance.apiV1UsersMeAvatarPickPost(avatarfile);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MyUserApi#apiV1UsersMeAvatarPickPost");
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
| **avatarfile** | **File**| The file to upload | [optional] |

### Return type

[**ApiV1UsersMeAvatarPickPost200Response**](ApiV1UsersMeAvatarPickPost200Response.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **413** | image file too large |  * X-File-Maximum-Size - Maximum file size for the video <br>  |

<a id="apiV1UsersMeVideoQuotaUsedGet"></a>
# **apiV1UsersMeVideoQuotaUsedGet**
> ApiV1UsersMeVideoQuotaUsedGet200Response apiV1UsersMeVideoQuotaUsedGet()

Get my user used quota

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MyUserApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://peertube2.cpy.re");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    MyUserApi apiInstance = new MyUserApi(defaultClient);
    try {
      ApiV1UsersMeVideoQuotaUsedGet200Response result = apiInstance.apiV1UsersMeVideoQuotaUsedGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MyUserApi#apiV1UsersMeVideoQuotaUsedGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ApiV1UsersMeVideoQuotaUsedGet200Response**](ApiV1UsersMeVideoQuotaUsedGet200Response.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="apiV1UsersMeVideosGet"></a>
# **apiV1UsersMeVideosGet**
> VideoListResponse apiV1UsersMeVideosGet(start, count, sort)

Get videos of my user

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MyUserApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://peertube2.cpy.re");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    MyUserApi apiInstance = new MyUserApi(defaultClient);
    Integer start = 56; // Integer | Offset used to paginate results
    Integer count = 15; // Integer | Number of items to return
    String sort = "-createdAt"; // String | Sort column
    try {
      VideoListResponse result = apiInstance.apiV1UsersMeVideosGet(start, count, sort);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MyUserApi#apiV1UsersMeVideosGet");
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
| **start** | **Integer**| Offset used to paginate results | [optional] |
| **count** | **Integer**| Number of items to return | [optional] [default to 15] |
| **sort** | **String**| Sort column | [optional] |

### Return type

[**VideoListResponse**](VideoListResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="apiV1UsersMeVideosImportsGet_0"></a>
# **apiV1UsersMeVideosImportsGet_0**
> VideoImportsList apiV1UsersMeVideosImportsGet_0(start, count, sort, targetUrl, videoChannelSyncId, search)

Get video imports of my user

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MyUserApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://peertube2.cpy.re");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    MyUserApi apiInstance = new MyUserApi(defaultClient);
    Integer start = 56; // Integer | Offset used to paginate results
    Integer count = 15; // Integer | Number of items to return
    String sort = "-createdAt"; // String | Sort column
    String targetUrl = "targetUrl_example"; // String | Filter on import target URL
    BigDecimal videoChannelSyncId = new BigDecimal(78); // BigDecimal | Filter on imports created by a specific channel synchronization
    String search = "search_example"; // String | Search in video names
    try {
      VideoImportsList result = apiInstance.apiV1UsersMeVideosImportsGet_0(start, count, sort, targetUrl, videoChannelSyncId, search);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MyUserApi#apiV1UsersMeVideosImportsGet_0");
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
| **start** | **Integer**| Offset used to paginate results | [optional] |
| **count** | **Integer**| Number of items to return | [optional] [default to 15] |
| **sort** | **String**| Sort column | [optional] |
| **targetUrl** | **String**| Filter on import target URL | [optional] |
| **videoChannelSyncId** | **BigDecimal**| Filter on imports created by a specific channel synchronization | [optional] |
| **search** | **String**| Search in video names | [optional] |

### Return type

[**VideoImportsList**](VideoImportsList.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="apiV1UsersMeVideosVideoIdRatingGet"></a>
# **apiV1UsersMeVideosVideoIdRatingGet**
> GetMeVideoRating apiV1UsersMeVideosVideoIdRatingGet(videoId)

Get rate of my user for a video

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MyUserApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://peertube2.cpy.re");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    MyUserApi apiInstance = new MyUserApi(defaultClient);
    Integer videoId = 56; // Integer | The video id
    try {
      GetMeVideoRating result = apiInstance.apiV1UsersMeVideosVideoIdRatingGet(videoId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MyUserApi#apiV1UsersMeVideosVideoIdRatingGet");
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
| **videoId** | **Integer**| The video id | |

### Return type

[**GetMeVideoRating**](GetMeVideoRating.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="getMyAbuses_0"></a>
# **getMyAbuses_0**
> GetAbuses200Response getMyAbuses_0(id, state, sort, start, count)

List my abuses

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MyUserApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://peertube2.cpy.re");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    MyUserApi apiInstance = new MyUserApi(defaultClient);
    Integer id = 56; // Integer | only list the report with this id
    AbuseStateSet state = AbuseStateSet.fromValue("1"); // AbuseStateSet | 
    String sort = "-id"; // String | Sort abuses by criteria
    Integer start = 56; // Integer | Offset used to paginate results
    Integer count = 15; // Integer | Number of items to return
    try {
      GetAbuses200Response result = apiInstance.getMyAbuses_0(id, state, sort, start, count);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MyUserApi#getMyAbuses_0");
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
| **id** | **Integer**| only list the report with this id | [optional] |
| **state** | [**AbuseStateSet**](.md)|  | [optional] [enum: 1, 2, 3] |
| **sort** | **String**| Sort abuses by criteria | [optional] [enum: -id, -createdAt, -state] |
| **start** | **Integer**| Offset used to paginate results | [optional] |
| **count** | **Integer**| Number of items to return | [optional] [default to 15] |

### Return type

[**GetAbuses200Response**](GetAbuses200Response.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="getUserInfo"></a>
# **getUserInfo**
> List&lt;User&gt; getUserInfo()

Get my user information

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MyUserApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://peertube2.cpy.re");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    MyUserApi apiInstance = new MyUserApi(defaultClient);
    try {
      List<User> result = apiInstance.getUserInfo();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MyUserApi#getUserInfo");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**List&lt;User&gt;**](User.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="putUserInfo"></a>
# **putUserInfo**
> putUserInfo(updateMe)

Update my user information

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MyUserApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://peertube2.cpy.re");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    MyUserApi apiInstance = new MyUserApi(defaultClient);
    UpdateMe updateMe = new UpdateMe(); // UpdateMe | 
    try {
      apiInstance.putUserInfo(updateMe);
    } catch (ApiException e) {
      System.err.println("Exception when calling MyUserApi#putUserInfo");
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
| **updateMe** | [**UpdateMe**](UpdateMe.md)|  | |

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | successful operation |  -  |

