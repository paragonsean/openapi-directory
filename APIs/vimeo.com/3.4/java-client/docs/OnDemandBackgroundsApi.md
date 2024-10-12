# OnDemandBackgroundsApi

All URIs are relative to *https://api.vimeo.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createVodBackground**](OnDemandBackgroundsApi.md#createVodBackground) | **POST** /ondemand/pages/{ondemand_id}/backgrounds | Add a background to an On Demand page |
| [**deleteVodBackground**](OnDemandBackgroundsApi.md#deleteVodBackground) | **DELETE** /ondemand/pages/{ondemand_id}/backgrounds/{background_id} | Remove a background from an On Demand page |
| [**editVodBackground**](OnDemandBackgroundsApi.md#editVodBackground) | **PATCH** /ondemand/pages/{ondemand_id}/backgrounds/{background_id} | Edit a background of an On Demand page |
| [**getVodBackground**](OnDemandBackgroundsApi.md#getVodBackground) | **GET** /ondemand/pages/{ondemand_id}/backgrounds/{background_id} | Get a specific background of an On Demand page |
| [**getVodBackgrounds**](OnDemandBackgroundsApi.md#getVodBackgrounds) | **GET** /ondemand/pages/{ondemand_id}/backgrounds | Get all the backgrounds of an On Demand page |


<a id="createVodBackground"></a>
# **createVodBackground**
> Picture createVodBackground(ondemandId)

Add a background to an On Demand page

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OnDemandBackgroundsApi;

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

    OnDemandBackgroundsApi apiInstance = new OnDemandBackgroundsApi(defaultClient);
    BigDecimal ondemandId = new BigDecimal("61326"); // BigDecimal | The ID of the On Demand.
    try {
      Picture result = apiInstance.createVodBackground(ondemandId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OnDemandBackgroundsApi#createVodBackground");
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
| **ondemandId** | **BigDecimal**| The ID of the On Demand. | |

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
| **200** | The background was created. |  -  |
| **403** | You can&#39;t modify an On Demand page that you don&#39;t own. |  -  |
| **404** | No such On Demand page exists. |  -  |

<a id="deleteVodBackground"></a>
# **deleteVodBackground**
> Picture deleteVodBackground(backgroundId, ondemandId)

Remove a background from an On Demand page

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OnDemandBackgroundsApi;

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

    OnDemandBackgroundsApi apiInstance = new OnDemandBackgroundsApi(defaultClient);
    BigDecimal backgroundId = new BigDecimal("12345"); // BigDecimal | The ID of the background.
    BigDecimal ondemandId = new BigDecimal("61326"); // BigDecimal | The ID of the On Demand.
    try {
      Picture result = apiInstance.deleteVodBackground(backgroundId, ondemandId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OnDemandBackgroundsApi#deleteVodBackground");
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
| **backgroundId** | **BigDecimal**| The ID of the background. | |
| **ondemandId** | **BigDecimal**| The ID of the On Demand. | |

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
| **204** | The background image was deleted. |  -  |
| **403** | If you are attempting to modify an On Demand page you don&#39;t own. |  -  |
| **404** | No such On Demand page or background image exists. |  -  |

<a id="editVodBackground"></a>
# **editVodBackground**
> Picture editVodBackground(backgroundId, ondemandId, editVodBackgroundRequest)

Edit a background of an On Demand page

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OnDemandBackgroundsApi;

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

    OnDemandBackgroundsApi apiInstance = new OnDemandBackgroundsApi(defaultClient);
    BigDecimal backgroundId = new BigDecimal("12345"); // BigDecimal | The ID of the background.
    BigDecimal ondemandId = new BigDecimal("61326"); // BigDecimal | The ID of the On Demand.
    EditVodBackgroundRequest editVodBackgroundRequest = new EditVodBackgroundRequest(); // EditVodBackgroundRequest | 
    try {
      Picture result = apiInstance.editVodBackground(backgroundId, ondemandId, editVodBackgroundRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OnDemandBackgroundsApi#editVodBackground");
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
| **backgroundId** | **BigDecimal**| The ID of the background. | |
| **ondemandId** | **BigDecimal**| The ID of the On Demand. | |
| **editVodBackgroundRequest** | [**EditVodBackgroundRequest**](EditVodBackgroundRequest.md)|  | [optional] |

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
| **200** | The background was edited. |  -  |
| **403** | You can&#39;t modify an On Demand page that you don&#39;t own. |  -  |
| **404** | No such On Demand page or background image exists. |  -  |

<a id="getVodBackground"></a>
# **getVodBackground**
> Picture getVodBackground(backgroundId, ondemandId)

Get a specific background of an On Demand page

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OnDemandBackgroundsApi;

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

    OnDemandBackgroundsApi apiInstance = new OnDemandBackgroundsApi(defaultClient);
    BigDecimal backgroundId = new BigDecimal("12345"); // BigDecimal | The ID of the background.
    BigDecimal ondemandId = new BigDecimal("61326"); // BigDecimal | The ID of the On Demand.
    try {
      Picture result = apiInstance.getVodBackground(backgroundId, ondemandId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OnDemandBackgroundsApi#getVodBackground");
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
| **backgroundId** | **BigDecimal**| The ID of the background. | |
| **ondemandId** | **BigDecimal**| The ID of the On Demand. | |

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
| **200** | The background image was returned. |  -  |
| **403** | You can&#39;t view another user&#39;s On Demand page background. |  -  |
| **404** | No such On Demand page or background image exists. |  -  |

<a id="getVodBackgrounds"></a>
# **getVodBackgrounds**
> List&lt;Picture&gt; getVodBackgrounds(ondemandId, page, perPage)

Get all the backgrounds of an On Demand page

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OnDemandBackgroundsApi;

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

    OnDemandBackgroundsApi apiInstance = new OnDemandBackgroundsApi(defaultClient);
    BigDecimal ondemandId = new BigDecimal("61326"); // BigDecimal | The ID of the On Demand.
    BigDecimal page = new BigDecimal("1"); // BigDecimal | The page number of the results to show.
    BigDecimal perPage = new BigDecimal("10"); // BigDecimal | The number of items to show on each page of results, up to a maximum of 100.
    try {
      List<Picture> result = apiInstance.getVodBackgrounds(ondemandId, page, perPage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OnDemandBackgroundsApi#getVodBackgrounds");
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
| **ondemandId** | **BigDecimal**| The ID of the On Demand. | |
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
| **200** | The background images were returned. |  -  |
| **404** | No such On Demand page exists. |  -  |

