# OnDemandEssentialsApi

All URIs are relative to *https://api.vimeo.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createVod**](OnDemandEssentialsApi.md#createVod) | **POST** /users/{user_id}/ondemand/pages | Create an On Demand page |
| [**createVodAlt1**](OnDemandEssentialsApi.md#createVodAlt1) | **POST** /me/ondemand/pages | Create an On Demand page |
| [**deleteVodDraft**](OnDemandEssentialsApi.md#deleteVodDraft) | **DELETE** /ondemand/pages/{ondemand_id} | Delete a draft of an On Demand page |
| [**editVod**](OnDemandEssentialsApi.md#editVod) | **PATCH** /ondemand/pages/{ondemand_id} | Edit an On Demand page |
| [**getUserVods**](OnDemandEssentialsApi.md#getUserVods) | **GET** /users/{user_id}/ondemand/pages | Get all the On Demand pages of a user |
| [**getUserVodsAlt1**](OnDemandEssentialsApi.md#getUserVodsAlt1) | **GET** /me/ondemand/pages | Get all the On Demand pages of a user |
| [**getVod**](OnDemandEssentialsApi.md#getVod) | **GET** /ondemand/pages/{ondemand_id} | Get a specific On Demand page |


<a id="createVod"></a>
# **createVod**
> OnDemandPage createVod(userId, createVodAlt1Request)

Create an On Demand page

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OnDemandEssentialsApi;

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

    OnDemandEssentialsApi apiInstance = new OnDemandEssentialsApi(defaultClient);
    BigDecimal userId = new BigDecimal("152184"); // BigDecimal | The ID of the user.
    CreateVodAlt1Request createVodAlt1Request = new CreateVodAlt1Request(); // CreateVodAlt1Request | 
    try {
      OnDemandPage result = apiInstance.createVod(userId, createVodAlt1Request);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OnDemandEssentialsApi#createVod");
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
| **createVodAlt1Request** | [**CreateVodAlt1Request**](CreateVodAlt1Request.md)|  | |

### Return type

[**OnDemandPage**](OnDemandPage.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The On Demand page was created. |  -  |

<a id="createVodAlt1"></a>
# **createVodAlt1**
> OnDemandPage createVodAlt1(createVodAlt1Request)

Create an On Demand page

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OnDemandEssentialsApi;

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

    OnDemandEssentialsApi apiInstance = new OnDemandEssentialsApi(defaultClient);
    CreateVodAlt1Request createVodAlt1Request = new CreateVodAlt1Request(); // CreateVodAlt1Request | 
    try {
      OnDemandPage result = apiInstance.createVodAlt1(createVodAlt1Request);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OnDemandEssentialsApi#createVodAlt1");
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
| **createVodAlt1Request** | [**CreateVodAlt1Request**](CreateVodAlt1Request.md)|  | |

### Return type

[**OnDemandPage**](OnDemandPage.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The On Demand page was created. |  -  |

<a id="deleteVodDraft"></a>
# **deleteVodDraft**
> deleteVodDraft(ondemandId)

Delete a draft of an On Demand page

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OnDemandEssentialsApi;

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

    OnDemandEssentialsApi apiInstance = new OnDemandEssentialsApi(defaultClient);
    BigDecimal ondemandId = new BigDecimal("61326"); // BigDecimal | The ID of the On Demand.
    try {
      apiInstance.deleteVodDraft(ondemandId);
    } catch (ApiException e) {
      System.err.println("Exception when calling OnDemandEssentialsApi#deleteVodDraft");
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

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.vimeo.ondemand.page+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | The page draft was deleted. |  -  |
| **403** | You can&#39;t modify an On Demand page that you don&#39;t own. |  -  |
| **404** | No such On Demand page exists. |  -  |

<a id="editVod"></a>
# **editVod**
> OnDemandPage editVod(ondemandId, editVodRequest)

Edit an On Demand page

Enable preorders or publish the page.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OnDemandEssentialsApi;

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

    OnDemandEssentialsApi apiInstance = new OnDemandEssentialsApi(defaultClient);
    BigDecimal ondemandId = new BigDecimal("61326"); // BigDecimal | The ID of the On Demand.
    EditVodRequest editVodRequest = new EditVodRequest(); // EditVodRequest | 
    try {
      OnDemandPage result = apiInstance.editVod(ondemandId, editVodRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OnDemandEssentialsApi#editVod");
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
| **editVodRequest** | [**EditVodRequest**](EditVodRequest.md)|  | [optional] |

### Return type

[**OnDemandPage**](OnDemandPage.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/vnd.vimeo.ondemand.page+json
 - **Accept**: application/vnd.vimeo.ondemand.page+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The On Demand page was edited. |  -  |
| **403** | The authenticated user can&#39;t edit the On Demand page. |  -  |
| **404** | No such On Demand page exists. |  -  |

<a id="getUserVods"></a>
# **getUserVods**
> List&lt;OnDemandPage&gt; getUserVods(userId, direction, filter, page, perPage, sort)

Get all the On Demand pages of a user

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OnDemandEssentialsApi;

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

    OnDemandEssentialsApi apiInstance = new OnDemandEssentialsApi(defaultClient);
    BigDecimal userId = new BigDecimal("152184"); // BigDecimal | The ID of the user.
    String direction = "asc"; // String | The sort direction of the results.
    String filter = "film"; // String | The type of On Demand pages to return.
    BigDecimal page = new BigDecimal("1"); // BigDecimal | The page number of the results to show.
    BigDecimal perPage = new BigDecimal("10"); // BigDecimal | The number of items to show on each page of results, up to a maximum of 100.
    String sort = "added"; // String | The way to sort the results.
    try {
      List<OnDemandPage> result = apiInstance.getUserVods(userId, direction, filter, page, perPage, sort);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OnDemandEssentialsApi#getUserVods");
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
| **direction** | **String**| The sort direction of the results. | [optional] [enum: asc, desc] |
| **filter** | **String**| The type of On Demand pages to return. | [optional] [enum: film, series] |
| **page** | **BigDecimal**| The page number of the results to show. | [optional] |
| **perPage** | **BigDecimal**| The number of items to show on each page of results, up to a maximum of 100. | [optional] |
| **sort** | **String**| The way to sort the results. | [optional] [enum: added, alphabetical, date, modified_time, name, publish.time, rating] |

### Return type

[**List&lt;OnDemandPage&gt;**](OnDemandPage.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.vimeo.ondemand.page+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The On Demand pages were returned. |  -  |
| **404** | No such user exists. |  -  |

<a id="getUserVodsAlt1"></a>
# **getUserVodsAlt1**
> List&lt;OnDemandPage&gt; getUserVodsAlt1(direction, filter, page, perPage, sort)

Get all the On Demand pages of a user

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OnDemandEssentialsApi;

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

    OnDemandEssentialsApi apiInstance = new OnDemandEssentialsApi(defaultClient);
    String direction = "asc"; // String | The sort direction of the results.
    String filter = "film"; // String | The type of On Demand pages to return.
    BigDecimal page = new BigDecimal("1"); // BigDecimal | The page number of the results to show.
    BigDecimal perPage = new BigDecimal("10"); // BigDecimal | The number of items to show on each page of results, up to a maximum of 100.
    String sort = "added"; // String | The way to sort the results.
    try {
      List<OnDemandPage> result = apiInstance.getUserVodsAlt1(direction, filter, page, perPage, sort);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OnDemandEssentialsApi#getUserVodsAlt1");
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
| **direction** | **String**| The sort direction of the results. | [optional] [enum: asc, desc] |
| **filter** | **String**| The type of On Demand pages to return. | [optional] [enum: film, series] |
| **page** | **BigDecimal**| The page number of the results to show. | [optional] |
| **perPage** | **BigDecimal**| The number of items to show on each page of results, up to a maximum of 100. | [optional] |
| **sort** | **String**| The way to sort the results. | [optional] [enum: added, alphabetical, date, modified_time, name, publish.time, rating] |

### Return type

[**List&lt;OnDemandPage&gt;**](OnDemandPage.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.vimeo.ondemand.page+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The On Demand pages were returned. |  -  |
| **404** | No such user exists. |  -  |

<a id="getVod"></a>
# **getVod**
> OnDemandPage getVod(ondemandId)

Get a specific On Demand page

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OnDemandEssentialsApi;

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

    OnDemandEssentialsApi apiInstance = new OnDemandEssentialsApi(defaultClient);
    BigDecimal ondemandId = new BigDecimal("61326"); // BigDecimal | The ID of the On Demand.
    try {
      OnDemandPage result = apiInstance.getVod(ondemandId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OnDemandEssentialsApi#getVod");
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

[**OnDemandPage**](OnDemandPage.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.vimeo.ondemand.page+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The On Demand page was returned. |  -  |
| **404** | No such On Demand page exists. |  -  |

