# UsersPicturesApi

All URIs are relative to *https://api.vimeo.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createPicture**](UsersPicturesApi.md#createPicture) | **POST** /users/{user_id}/pictures | Add a user picture |
| [**createPictureAlt1**](UsersPicturesApi.md#createPictureAlt1) | **POST** /me/pictures | Add a user picture |
| [**deletePicture**](UsersPicturesApi.md#deletePicture) | **DELETE** /users/{user_id}/pictures/{portraitset_id} | Delete a user picture |
| [**deletePictureAlt1**](UsersPicturesApi.md#deletePictureAlt1) | **DELETE** /me/pictures/{portraitset_id} | Delete a user picture |
| [**editPicture**](UsersPicturesApi.md#editPicture) | **PATCH** /users/{user_id}/pictures/{portraitset_id} | Edit a user picture |
| [**editPictureAlt1**](UsersPicturesApi.md#editPictureAlt1) | **PATCH** /me/pictures/{portraitset_id} | Edit a user picture |
| [**getPicture**](UsersPicturesApi.md#getPicture) | **GET** /users/{user_id}/pictures/{portraitset_id} | Get a specific user picture |
| [**getPictureAlt1**](UsersPicturesApi.md#getPictureAlt1) | **GET** /me/pictures/{portraitset_id} | Get a specific user picture |
| [**getPictures**](UsersPicturesApi.md#getPictures) | **GET** /users/{user_id}/pictures | Get all the pictures that belong to a user |
| [**getPicturesAlt1**](UsersPicturesApi.md#getPicturesAlt1) | **GET** /me/pictures | Get all the pictures that belong to a user |


<a id="createPicture"></a>
# **createPicture**
> Picture createPicture(userId)

Add a user picture

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersPicturesApi;

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

    UsersPicturesApi apiInstance = new UsersPicturesApi(defaultClient);
    BigDecimal userId = new BigDecimal("152184"); // BigDecimal | The ID of the user.
    try {
      Picture result = apiInstance.createPicture(userId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersPicturesApi#createPicture");
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

### Return type

[**Picture**](Picture.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.vimeo.picture+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The user picture was created. |  -  |

<a id="createPictureAlt1"></a>
# **createPictureAlt1**
> Picture createPictureAlt1()

Add a user picture

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersPicturesApi;

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

    UsersPicturesApi apiInstance = new UsersPicturesApi(defaultClient);
    try {
      Picture result = apiInstance.createPictureAlt1();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersPicturesApi#createPictureAlt1");
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

[**Picture**](Picture.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.vimeo.picture+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The user picture was created. |  -  |

<a id="deletePicture"></a>
# **deletePicture**
> deletePicture(portraitsetId, userId)

Delete a user picture

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersPicturesApi;

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

    UsersPicturesApi apiInstance = new UsersPicturesApi(defaultClient);
    BigDecimal portraitsetId = new BigDecimal("12345"); // BigDecimal | The ID of the picture.
    BigDecimal userId = new BigDecimal("152184"); // BigDecimal | The ID of the user.
    try {
      apiInstance.deletePicture(portraitsetId, userId);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersPicturesApi#deletePicture");
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
| **portraitsetId** | **BigDecimal**| The ID of the picture. | |
| **userId** | **BigDecimal**| The ID of the user. | |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | The picture was deleted. |  -  |

<a id="deletePictureAlt1"></a>
# **deletePictureAlt1**
> deletePictureAlt1(portraitsetId)

Delete a user picture

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersPicturesApi;

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

    UsersPicturesApi apiInstance = new UsersPicturesApi(defaultClient);
    BigDecimal portraitsetId = new BigDecimal("12345"); // BigDecimal | The ID of the picture.
    try {
      apiInstance.deletePictureAlt1(portraitsetId);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersPicturesApi#deletePictureAlt1");
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
| **portraitsetId** | **BigDecimal**| The ID of the picture. | |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | The picture was deleted. |  -  |

<a id="editPicture"></a>
# **editPicture**
> Picture editPicture(portraitsetId, userId, editPictureAlt1Request)

Edit a user picture

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersPicturesApi;

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

    UsersPicturesApi apiInstance = new UsersPicturesApi(defaultClient);
    BigDecimal portraitsetId = new BigDecimal("12345"); // BigDecimal | The ID of the picture.
    BigDecimal userId = new BigDecimal("152184"); // BigDecimal | The ID of the user.
    EditPictureAlt1Request editPictureAlt1Request = new EditPictureAlt1Request(); // EditPictureAlt1Request | 
    try {
      Picture result = apiInstance.editPicture(portraitsetId, userId, editPictureAlt1Request);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersPicturesApi#editPicture");
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
| **portraitsetId** | **BigDecimal**| The ID of the picture. | |
| **userId** | **BigDecimal**| The ID of the user. | |
| **editPictureAlt1Request** | [**EditPictureAlt1Request**](EditPictureAlt1Request.md)|  | [optional] |

### Return type

[**Picture**](Picture.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/vnd.vimeo.picture+json
 - **Accept**: application/vnd.vimeo.picture+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The picture was edited. |  -  |

<a id="editPictureAlt1"></a>
# **editPictureAlt1**
> Picture editPictureAlt1(portraitsetId, editPictureAlt1Request)

Edit a user picture

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersPicturesApi;

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

    UsersPicturesApi apiInstance = new UsersPicturesApi(defaultClient);
    BigDecimal portraitsetId = new BigDecimal("12345"); // BigDecimal | The ID of the picture.
    EditPictureAlt1Request editPictureAlt1Request = new EditPictureAlt1Request(); // EditPictureAlt1Request | 
    try {
      Picture result = apiInstance.editPictureAlt1(portraitsetId, editPictureAlt1Request);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersPicturesApi#editPictureAlt1");
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
| **portraitsetId** | **BigDecimal**| The ID of the picture. | |
| **editPictureAlt1Request** | [**EditPictureAlt1Request**](EditPictureAlt1Request.md)|  | [optional] |

### Return type

[**Picture**](Picture.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/vnd.vimeo.picture+json
 - **Accept**: application/vnd.vimeo.picture+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The picture was edited. |  -  |

<a id="getPicture"></a>
# **getPicture**
> Picture getPicture(portraitsetId, userId)

Get a specific user picture

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersPicturesApi;

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

    UsersPicturesApi apiInstance = new UsersPicturesApi(defaultClient);
    BigDecimal portraitsetId = new BigDecimal("12345"); // BigDecimal | The ID of the picture.
    BigDecimal userId = new BigDecimal("152184"); // BigDecimal | The ID of the user.
    try {
      Picture result = apiInstance.getPicture(portraitsetId, userId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersPicturesApi#getPicture");
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
| **portraitsetId** | **BigDecimal**| The ID of the picture. | |
| **userId** | **BigDecimal**| The ID of the user. | |

### Return type

[**Picture**](Picture.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.vimeo.picture+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The picture was returned. |  -  |

<a id="getPictureAlt1"></a>
# **getPictureAlt1**
> Picture getPictureAlt1(portraitsetId)

Get a specific user picture

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersPicturesApi;

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

    UsersPicturesApi apiInstance = new UsersPicturesApi(defaultClient);
    BigDecimal portraitsetId = new BigDecimal("12345"); // BigDecimal | The ID of the picture.
    try {
      Picture result = apiInstance.getPictureAlt1(portraitsetId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersPicturesApi#getPictureAlt1");
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
| **portraitsetId** | **BigDecimal**| The ID of the picture. | |

### Return type

[**Picture**](Picture.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.vimeo.picture+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The picture was returned. |  -  |

<a id="getPictures"></a>
# **getPictures**
> List&lt;Picture&gt; getPictures(userId, page, perPage)

Get all the pictures that belong to a user

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersPicturesApi;

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

    UsersPicturesApi apiInstance = new UsersPicturesApi(defaultClient);
    BigDecimal userId = new BigDecimal("152184"); // BigDecimal | The ID of the user.
    BigDecimal page = new BigDecimal("1"); // BigDecimal | The page number of the results to show.
    BigDecimal perPage = new BigDecimal("10"); // BigDecimal | The number of items to show on each page of results, up to a maximum of 100.
    try {
      List<Picture> result = apiInstance.getPictures(userId, page, perPage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersPicturesApi#getPictures");
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
| **page** | **BigDecimal**| The page number of the results to show. | [optional] |
| **perPage** | **BigDecimal**| The number of items to show on each page of results, up to a maximum of 100. | [optional] |

### Return type

[**List&lt;Picture&gt;**](Picture.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.vimeo.picture+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The pictures were returned. |  -  |

<a id="getPicturesAlt1"></a>
# **getPicturesAlt1**
> List&lt;Picture&gt; getPicturesAlt1(page, perPage)

Get all the pictures that belong to a user

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersPicturesApi;

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

    UsersPicturesApi apiInstance = new UsersPicturesApi(defaultClient);
    BigDecimal page = new BigDecimal("1"); // BigDecimal | The page number of the results to show.
    BigDecimal perPage = new BigDecimal("10"); // BigDecimal | The number of items to show on each page of results, up to a maximum of 100.
    try {
      List<Picture> result = apiInstance.getPicturesAlt1(page, perPage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersPicturesApi#getPicturesAlt1");
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
| **page** | **BigDecimal**| The page number of the results to show. | [optional] |
| **perPage** | **BigDecimal**| The number of items to show on each page of results, up to a maximum of 100. | [optional] |

### Return type

[**List&lt;Picture&gt;**](Picture.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.vimeo.picture+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The pictures were returned. |  -  |

