# EditorialImagesApi

All URIs are relative to *https://api.shutterstock.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getEditorialCategories**](EditorialImagesApi.md#getEditorialCategories) | **GET** /v2/editorial/categories | (Deprecated) List editorial categories |
| [**getEditorialImage**](EditorialImagesApi.md#getEditorialImage) | **GET** /v2/editorial/images/{id} | Get editorial content details |
| [**getEditorialImageLicenseList**](EditorialImagesApi.md#getEditorialImageLicenseList) | **GET** /v2/editorial/images/licenses | List editorial image licenses |
| [**getEditorialImageLivefeed**](EditorialImagesApi.md#getEditorialImageLivefeed) | **GET** /v2/editorial/images/livefeeds/{id} | Get editorial livefeed |
| [**getEditorialImageLivefeedItems**](EditorialImagesApi.md#getEditorialImageLivefeedItems) | **GET** /v2/editorial/images/livefeeds/{id}/items | Get editorial livefeed items |
| [**getEditorialImageLivefeedList**](EditorialImagesApi.md#getEditorialImageLivefeedList) | **GET** /v2/editorial/images/livefeeds | Get editorial livefeed list |
| [**getEditorialLivefeed**](EditorialImagesApi.md#getEditorialLivefeed) | **GET** /v2/editorial/livefeeds/{id} | (Deprecated) Get editorial livefeed |
| [**getEditorialLivefeedItems**](EditorialImagesApi.md#getEditorialLivefeedItems) | **GET** /v2/editorial/livefeeds/{id}/items | (Deprecated) Get editorial livefeed items |
| [**getEditorialLivefeedList**](EditorialImagesApi.md#getEditorialLivefeedList) | **GET** /v2/editorial/livefeeds | (Deprecated) Get editorial livefeed list |
| [**getUpdatedEditorialImage**](EditorialImagesApi.md#getUpdatedEditorialImage) | **GET** /v2/editorial/updated | (Deprecated) List updated content |
| [**getUpdatedEditorialImages**](EditorialImagesApi.md#getUpdatedEditorialImages) | **GET** /v2/editorial/images/updated | List updated content |
| [**licenseEditorialImage**](EditorialImagesApi.md#licenseEditorialImage) | **POST** /v2/editorial/licenses | (Deprecated) License editorial content |
| [**licenseEditorialImages**](EditorialImagesApi.md#licenseEditorialImages) | **POST** /v2/editorial/images/licenses | License editorial content |
| [**listEditorialImageCategories**](EditorialImagesApi.md#listEditorialImageCategories) | **GET** /v2/editorial/images/categories | List editorial categories |
| [**searchEditorial**](EditorialImagesApi.md#searchEditorial) | **GET** /v2/editorial/search | (Deprecated) Search editorial content |
| [**searchEditorialImages**](EditorialImagesApi.md#searchEditorialImages) | **GET** /v2/editorial/images/search | Search editorial images |
| [**v2EditorialIdGet**](EditorialImagesApi.md#v2EditorialIdGet) | **GET** /v2/editorial/{id} | (Deprecated) Get editorial content details |


<a id="getEditorialCategories"></a>
# **getEditorialCategories**
> EditorialCategoryResults getEditorialCategories()

(Deprecated) List editorial categories

Deprecated; use &#x60;GET /v2/editorial/images/categories&#x60; instead. This endpoint lists the categories that editorial images can belong to, which are separate from the categories that other types of assets can belong to.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EditorialImagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.shutterstock.com");
    
    // Configure OAuth2 access token for authorization: customer_accessCode
    OAuth customer_accessCode = (OAuth) defaultClient.getAuthentication("customer_accessCode");
    customer_accessCode.setAccessToken("YOUR ACCESS TOKEN");

    // Configure HTTP basic authorization: basic
    HttpBasicAuth basic = (HttpBasicAuth) defaultClient.getAuthentication("basic");
    basic.setUsername("YOUR USERNAME");
    basic.setPassword("YOUR PASSWORD");

    EditorialImagesApi apiInstance = new EditorialImagesApi(defaultClient);
    try {
      EditorialCategoryResults result = apiInstance.getEditorialCategories();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EditorialImagesApi#getEditorialCategories");
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

[**EditorialCategoryResults**](EditorialCategoryResults.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |

<a id="getEditorialImage"></a>
# **getEditorialImage**
> EditorialContent getEditorialImage(id, country)

Get editorial content details

This endpoint shows information about an editorial image, including a URL to a preview image and the sizes that it is available in.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EditorialImagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.shutterstock.com");
    
    // Configure OAuth2 access token for authorization: customer_accessCode
    OAuth customer_accessCode = (OAuth) defaultClient.getAuthentication("customer_accessCode");
    customer_accessCode.setAccessToken("YOUR ACCESS TOKEN");

    // Configure HTTP basic authorization: basic
    HttpBasicAuth basic = (HttpBasicAuth) defaultClient.getAuthentication("basic");
    basic.setUsername("YOUR USERNAME");
    basic.setPassword("YOUR PASSWORD");

    EditorialImagesApi apiInstance = new EditorialImagesApi(defaultClient);
    String id = "9926131a"; // String | Editorial ID
    String country = "USA"; // String | Returns only if the content is available for distribution in a certain country
    try {
      EditorialContent result = apiInstance.getEditorialImage(id, country);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EditorialImagesApi#getEditorialImage");
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
| **id** | **String**| Editorial ID | |
| **country** | **String**| Returns only if the content is available for distribution in a certain country | |

### Return type

[**EditorialContent**](EditorialContent.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

<a id="getEditorialImageLicenseList"></a>
# **getEditorialImageLicenseList**
> DownloadHistoryDataList getEditorialImageLicenseList(imageId, license, page, perPage, sort, username, startDate, endDate, downloadAvailability, teamHistory)

List editorial image licenses

This endpoint lists existing editorial image licenses.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EditorialImagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.shutterstock.com");
    
    // Configure OAuth2 access token for authorization: customer_accessCode
    OAuth customer_accessCode = (OAuth) defaultClient.getAuthentication("customer_accessCode");
    customer_accessCode.setAccessToken("YOUR ACCESS TOKEN");

    EditorialImagesApi apiInstance = new EditorialImagesApi(defaultClient);
    String imageId = "12345678"; // String | Show licenses for the specified editorial image ID
    String license = "premier_editorial_all_digital"; // String | Show editorial images that are available with the specified license name
    Integer page = 1; // Integer | Page number
    Integer perPage = 20; // Integer | Number of results per page
    String sort = "newest"; // String | Sort order
    String username = "aUniqueUsername"; // String | Filter licenses by username of licensee
    OffsetDateTime startDate = OffsetDateTime.parse("2021-03-29T13:25:13.521Z"); // OffsetDateTime | Show licenses created on or after the specified date
    OffsetDateTime endDate = OffsetDateTime.parse("2021-03-29T13:25:13.521Z"); // OffsetDateTime | Show licenses created before the specified date
    String downloadAvailability = "all"; // String | Filter licenses by download availability
    Boolean teamHistory = false; // Boolean | Set to true to see license history for all members of your team.
    try {
      DownloadHistoryDataList result = apiInstance.getEditorialImageLicenseList(imageId, license, page, perPage, sort, username, startDate, endDate, downloadAvailability, teamHistory);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EditorialImagesApi#getEditorialImageLicenseList");
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
| **imageId** | **String**| Show licenses for the specified editorial image ID | [optional] |
| **license** | **String**| Show editorial images that are available with the specified license name | [optional] |
| **page** | **Integer**| Page number | [optional] [default to 1] |
| **perPage** | **Integer**| Number of results per page | [optional] [default to 20] |
| **sort** | **String**| Sort order | [optional] [default to newest] [enum: newest, oldest] |
| **username** | **String**| Filter licenses by username of licensee | [optional] |
| **startDate** | **OffsetDateTime**| Show licenses created on or after the specified date | [optional] |
| **endDate** | **OffsetDateTime**| Show licenses created before the specified date | [optional] |
| **downloadAvailability** | **String**| Filter licenses by download availability | [optional] [default to all] [enum: all, downloadable, non_downloadable] |
| **teamHistory** | **Boolean**| Set to true to see license history for all members of your team. | [optional] [default to false] |

### Return type

[**DownloadHistoryDataList**](DownloadHistoryDataList.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |

<a id="getEditorialImageLivefeed"></a>
# **getEditorialImageLivefeed**
> EditorialImageLivefeed getEditorialImageLivefeed(id, country)

Get editorial livefeed

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EditorialImagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.shutterstock.com");
    
    // Configure OAuth2 access token for authorization: customer_accessCode
    OAuth customer_accessCode = (OAuth) defaultClient.getAuthentication("customer_accessCode");
    customer_accessCode.setAccessToken("YOUR ACCESS TOKEN");

    // Configure HTTP basic authorization: basic
    HttpBasicAuth basic = (HttpBasicAuth) defaultClient.getAuthentication("basic");
    basic.setUsername("YOUR USERNAME");
    basic.setPassword("YOUR PASSWORD");

    EditorialImagesApi apiInstance = new EditorialImagesApi(defaultClient);
    String id = "2018%2F10%2F15%2FWomen%20of%20the%20Year%20Lunch%20%26%20Awards%2C%20London"; // String | Editorial livefeed ID; must be an URI encoded string
    String country = "USA"; // String | Returns only if the livefeed is available for distribution in a certain country
    try {
      EditorialImageLivefeed result = apiInstance.getEditorialImageLivefeed(id, country);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EditorialImagesApi#getEditorialImageLivefeed");
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
| **id** | **String**| Editorial livefeed ID; must be an URI encoded string | |
| **country** | **String**| Returns only if the livefeed is available for distribution in a certain country | |

### Return type

[**EditorialImageLivefeed**](EditorialImageLivefeed.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

<a id="getEditorialImageLivefeedItems"></a>
# **getEditorialImageLivefeedItems**
> EditorialImageContentDataList getEditorialImageLivefeedItems(id, country)

Get editorial livefeed items

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EditorialImagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.shutterstock.com");
    
    // Configure OAuth2 access token for authorization: customer_accessCode
    OAuth customer_accessCode = (OAuth) defaultClient.getAuthentication("customer_accessCode");
    customer_accessCode.setAccessToken("YOUR ACCESS TOKEN");

    // Configure HTTP basic authorization: basic
    HttpBasicAuth basic = (HttpBasicAuth) defaultClient.getAuthentication("basic");
    basic.setUsername("YOUR USERNAME");
    basic.setPassword("YOUR PASSWORD");

    EditorialImagesApi apiInstance = new EditorialImagesApi(defaultClient);
    String id = "2018%2F10%2F15%2FWomen%20of%20the%20Year%20Lunch%20%26%20Awards%2C%20London"; // String | Editorial livefeed ID; must be an URI encoded string
    String country = "USA"; // String | Returns only if the livefeed items are available for distribution in a certain country
    try {
      EditorialImageContentDataList result = apiInstance.getEditorialImageLivefeedItems(id, country);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EditorialImagesApi#getEditorialImageLivefeedItems");
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
| **id** | **String**| Editorial livefeed ID; must be an URI encoded string | |
| **country** | **String**| Returns only if the livefeed items are available for distribution in a certain country | |

### Return type

[**EditorialImageContentDataList**](EditorialImageContentDataList.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

<a id="getEditorialImageLivefeedList"></a>
# **getEditorialImageLivefeedList**
> EditorialImageLivefeedList getEditorialImageLivefeedList(country, page, perPage)

Get editorial livefeed list

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EditorialImagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.shutterstock.com");
    
    // Configure OAuth2 access token for authorization: customer_accessCode
    OAuth customer_accessCode = (OAuth) defaultClient.getAuthentication("customer_accessCode");
    customer_accessCode.setAccessToken("YOUR ACCESS TOKEN");

    // Configure HTTP basic authorization: basic
    HttpBasicAuth basic = (HttpBasicAuth) defaultClient.getAuthentication("basic");
    basic.setUsername("YOUR USERNAME");
    basic.setPassword("YOUR PASSWORD");

    EditorialImagesApi apiInstance = new EditorialImagesApi(defaultClient);
    String country = "USA"; // String | Returns only livefeeds that are available for distribution in a certain country
    Integer page = 1; // Integer | Page number
    Integer perPage = 20; // Integer | Number of results per page
    try {
      EditorialImageLivefeedList result = apiInstance.getEditorialImageLivefeedList(country, page, perPage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EditorialImagesApi#getEditorialImageLivefeedList");
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
| **country** | **String**| Returns only livefeeds that are available for distribution in a certain country | |
| **page** | **Integer**| Page number | [optional] [default to 1] |
| **perPage** | **Integer**| Number of results per page | [optional] [default to 20] |

### Return type

[**EditorialImageLivefeedList**](EditorialImageLivefeedList.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

<a id="getEditorialLivefeed"></a>
# **getEditorialLivefeed**
> EditorialLivefeed getEditorialLivefeed(id, country)

(Deprecated) Get editorial livefeed

Deprecated: use &#x60;GET /v2/editorial/images/livefeeds/{id}&#x60; instead to get an editorial livefeed.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EditorialImagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.shutterstock.com");
    
    // Configure OAuth2 access token for authorization: customer_accessCode
    OAuth customer_accessCode = (OAuth) defaultClient.getAuthentication("customer_accessCode");
    customer_accessCode.setAccessToken("YOUR ACCESS TOKEN");

    // Configure HTTP basic authorization: basic
    HttpBasicAuth basic = (HttpBasicAuth) defaultClient.getAuthentication("basic");
    basic.setUsername("YOUR USERNAME");
    basic.setPassword("YOUR PASSWORD");

    EditorialImagesApi apiInstance = new EditorialImagesApi(defaultClient);
    String id = "2018%2F10%2F15%2FWomen%20of%20the%20Year%20Lunch%20%26%20Awards%2C%20London"; // String | Editorial livefeed ID; must be an URI encoded string
    String country = "USA"; // String | Returns only if the livefeed is available for distribution in a certain country
    try {
      EditorialLivefeed result = apiInstance.getEditorialLivefeed(id, country);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EditorialImagesApi#getEditorialLivefeed");
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
| **id** | **String**| Editorial livefeed ID; must be an URI encoded string | |
| **country** | **String**| Returns only if the livefeed is available for distribution in a certain country | |

### Return type

[**EditorialLivefeed**](EditorialLivefeed.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **406** | Not Acceptable |  -  |

<a id="getEditorialLivefeedItems"></a>
# **getEditorialLivefeedItems**
> EditorialContentDataList getEditorialLivefeedItems(id, country)

(Deprecated) Get editorial livefeed items

Deprecated; use &#x60;GET /v2/editorial/images/livefeeds/{id}/items&#x60; instead to get editorial livefeed items.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EditorialImagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.shutterstock.com");
    
    // Configure OAuth2 access token for authorization: customer_accessCode
    OAuth customer_accessCode = (OAuth) defaultClient.getAuthentication("customer_accessCode");
    customer_accessCode.setAccessToken("YOUR ACCESS TOKEN");

    // Configure HTTP basic authorization: basic
    HttpBasicAuth basic = (HttpBasicAuth) defaultClient.getAuthentication("basic");
    basic.setUsername("YOUR USERNAME");
    basic.setPassword("YOUR PASSWORD");

    EditorialImagesApi apiInstance = new EditorialImagesApi(defaultClient);
    String id = "2018%2F10%2F15%2FWomen%20of%20the%20Year%20Lunch%20%26%20Awards%2C%20London"; // String | Editorial livefeed ID; must be an URI encoded string
    String country = "USA"; // String | Returns only if the livefeed items are available for distribution in a certain country
    try {
      EditorialContentDataList result = apiInstance.getEditorialLivefeedItems(id, country);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EditorialImagesApi#getEditorialLivefeedItems");
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
| **id** | **String**| Editorial livefeed ID; must be an URI encoded string | |
| **country** | **String**| Returns only if the livefeed items are available for distribution in a certain country | |

### Return type

[**EditorialContentDataList**](EditorialContentDataList.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **406** | Not Acceptable |  -  |

<a id="getEditorialLivefeedList"></a>
# **getEditorialLivefeedList**
> EditorialLivefeedList getEditorialLivefeedList(country, page, perPage)

(Deprecated) Get editorial livefeed list

Deprecated; use &#x60;GET /v2/editorial/images/livefeeds&#x60; instead to get a list of editorial livefeeds.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EditorialImagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.shutterstock.com");
    
    // Configure OAuth2 access token for authorization: customer_accessCode
    OAuth customer_accessCode = (OAuth) defaultClient.getAuthentication("customer_accessCode");
    customer_accessCode.setAccessToken("YOUR ACCESS TOKEN");

    // Configure HTTP basic authorization: basic
    HttpBasicAuth basic = (HttpBasicAuth) defaultClient.getAuthentication("basic");
    basic.setUsername("YOUR USERNAME");
    basic.setPassword("YOUR PASSWORD");

    EditorialImagesApi apiInstance = new EditorialImagesApi(defaultClient);
    String country = "USA"; // String | Returns only livefeeds that are available for distribution in a certain country
    Integer page = 1; // Integer | Page number
    Integer perPage = 20; // Integer | Number of results per page
    try {
      EditorialLivefeedList result = apiInstance.getEditorialLivefeedList(country, page, perPage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EditorialImagesApi#getEditorialLivefeedList");
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
| **country** | **String**| Returns only livefeeds that are available for distribution in a certain country | |
| **page** | **Integer**| Page number | [optional] [default to 1] |
| **perPage** | **Integer**| Number of results per page | [optional] [default to 20] |

### Return type

[**EditorialLivefeedList**](EditorialLivefeedList.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **406** | Not Acceptable |  -  |

<a id="getUpdatedEditorialImage"></a>
# **getUpdatedEditorialImage**
> EditorialUpdatedResults getUpdatedEditorialImage(type, dateUpdatedStart, dateUpdatedEnd, country, dateTakenStart, dateTakenEnd, cursor, sort, supplierCode, perPage)

(Deprecated) List updated content

Deprecated; use &#x60;GET /v2/editorial/images/updated&#x60; instead to get recently updated items.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EditorialImagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.shutterstock.com");
    
    // Configure OAuth2 access token for authorization: customer_accessCode
    OAuth customer_accessCode = (OAuth) defaultClient.getAuthentication("customer_accessCode");
    customer_accessCode.setAccessToken("YOUR ACCESS TOKEN");

    // Configure HTTP basic authorization: basic
    HttpBasicAuth basic = (HttpBasicAuth) defaultClient.getAuthentication("basic");
    basic.setUsername("YOUR USERNAME");
    basic.setPassword("YOUR PASSWORD");

    EditorialImagesApi apiInstance = new EditorialImagesApi(defaultClient);
    String type = "edit"; // String | Specify `addition` to return only images that were added or `edit` to return only images that were edited or deleted
    OffsetDateTime dateUpdatedStart = OffsetDateTime.parse("2021-03-29T13:25:13.521Z"); // OffsetDateTime | Show images images added, edited, or deleted after the specified date. Acceptable range is 1970-01-01T00:00:01 to 2038-01-19T00:00:00.
    OffsetDateTime dateUpdatedEnd = OffsetDateTime.parse("2021-03-29T13:25:13.521Z"); // OffsetDateTime | Show images images added, edited, or deleted before the specified date. Acceptable range is 1970-01-01T00:00:01 to 2038-01-19T00:00:00.
    String country = "USA"; // String | Show only editorial content that is available for distribution in a certain country
    LocalDate dateTakenStart = LocalDate.parse("2020-02-04"); // LocalDate | Show images that were taken on or after the specified date; use this parameter if you want recently created images from the collection instead of updated older assets
    LocalDate dateTakenEnd = LocalDate.parse("2020-02-05"); // LocalDate | Show images that were taken before the specified date
    String cursor = "eyJ2IjoxLCJzIjoyfQ=="; // String | The cursor of the page with which to start fetching results; this cursor is returned from previous requests
    String sort = "newest"; // String | Sort by
    List<String> supplierCode = Arrays.asList(); // List<String> | Show only editorial content from certain suppliers
    Integer perPage = 500; // Integer | Number of results per page
    try {
      EditorialUpdatedResults result = apiInstance.getUpdatedEditorialImage(type, dateUpdatedStart, dateUpdatedEnd, country, dateTakenStart, dateTakenEnd, cursor, sort, supplierCode, perPage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EditorialImagesApi#getUpdatedEditorialImage");
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
| **type** | **String**| Specify &#x60;addition&#x60; to return only images that were added or &#x60;edit&#x60; to return only images that were edited or deleted | [enum: edit, addition] |
| **dateUpdatedStart** | **OffsetDateTime**| Show images images added, edited, or deleted after the specified date. Acceptable range is 1970-01-01T00:00:01 to 2038-01-19T00:00:00. | |
| **dateUpdatedEnd** | **OffsetDateTime**| Show images images added, edited, or deleted before the specified date. Acceptable range is 1970-01-01T00:00:01 to 2038-01-19T00:00:00. | |
| **country** | **String**| Show only editorial content that is available for distribution in a certain country | |
| **dateTakenStart** | **LocalDate**| Show images that were taken on or after the specified date; use this parameter if you want recently created images from the collection instead of updated older assets | [optional] |
| **dateTakenEnd** | **LocalDate**| Show images that were taken before the specified date | [optional] |
| **cursor** | **String**| The cursor of the page with which to start fetching results; this cursor is returned from previous requests | [optional] |
| **sort** | **String**| Sort by | [optional] [default to newest] [enum: newest, oldest] |
| **supplierCode** | [**List&lt;String&gt;**](String.md)| Show only editorial content from certain suppliers | [optional] |
| **perPage** | **Integer**| Number of results per page | [optional] [default to 500] |

### Return type

[**EditorialUpdatedResults**](EditorialUpdatedResults.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **406** | Not Acceptable |  -  |

<a id="getUpdatedEditorialImages"></a>
# **getUpdatedEditorialImages**
> EditorialUpdatedResults getUpdatedEditorialImages(type, dateUpdatedStart, dateUpdatedEnd, country, dateTakenStart, dateTakenEnd, cursor, sort, supplierCode, perPage)

List updated content

This endpoint lists editorial images that have been updated in the specified time period to update content management systems (CMS) or digital asset management (DAM) systems. In most cases, use the date_updated_start and date_updated_end parameters to specify a range updates based on when the updates happened. You can also use the date_taken_start and date_taken_end parameters to specify a range of updates based on when the image was taken.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EditorialImagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.shutterstock.com");
    
    // Configure OAuth2 access token for authorization: customer_accessCode
    OAuth customer_accessCode = (OAuth) defaultClient.getAuthentication("customer_accessCode");
    customer_accessCode.setAccessToken("YOUR ACCESS TOKEN");

    // Configure HTTP basic authorization: basic
    HttpBasicAuth basic = (HttpBasicAuth) defaultClient.getAuthentication("basic");
    basic.setUsername("YOUR USERNAME");
    basic.setPassword("YOUR PASSWORD");

    EditorialImagesApi apiInstance = new EditorialImagesApi(defaultClient);
    String type = "edit"; // String | Specify `addition` to return only images that were added or `edit` to return only images that were edited or deleted
    OffsetDateTime dateUpdatedStart = OffsetDateTime.parse("2021-03-29T13:25:13.521Z"); // OffsetDateTime | Show images images added, edited, or deleted after the specified date. Acceptable range is 1970-01-01T00:00:01 to 2038-01-19T00:00:00.
    OffsetDateTime dateUpdatedEnd = OffsetDateTime.parse("2021-03-29T13:25:13.521Z"); // OffsetDateTime | Show images images added, edited, or deleted before the specified date. Acceptable range is 1970-01-01T00:00:01 to 2038-01-19T00:00:00.
    String country = "USA"; // String | Show only editorial content that is available for distribution in a certain country
    LocalDate dateTakenStart = LocalDate.parse("2020-02-04"); // LocalDate | Show images that were taken on or after the specified date; use this parameter if you want recently created images from the collection instead of updated older assets
    LocalDate dateTakenEnd = LocalDate.parse("2020-02-05"); // LocalDate | Show images that were taken before the specified date
    String cursor = "eyJ2IjoxLCJzIjoyfQ=="; // String | The cursor of the page with which to start fetching results; this cursor is returned from previous requests
    String sort = "newest"; // String | Sort by
    List<String> supplierCode = Arrays.asList(); // List<String> | Show only editorial content from certain suppliers
    Integer perPage = 500; // Integer | Number of results per page
    try {
      EditorialUpdatedResults result = apiInstance.getUpdatedEditorialImages(type, dateUpdatedStart, dateUpdatedEnd, country, dateTakenStart, dateTakenEnd, cursor, sort, supplierCode, perPage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EditorialImagesApi#getUpdatedEditorialImages");
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
| **type** | **String**| Specify &#x60;addition&#x60; to return only images that were added or &#x60;edit&#x60; to return only images that were edited or deleted | [enum: edit, addition] |
| **dateUpdatedStart** | **OffsetDateTime**| Show images images added, edited, or deleted after the specified date. Acceptable range is 1970-01-01T00:00:01 to 2038-01-19T00:00:00. | |
| **dateUpdatedEnd** | **OffsetDateTime**| Show images images added, edited, or deleted before the specified date. Acceptable range is 1970-01-01T00:00:01 to 2038-01-19T00:00:00. | |
| **country** | **String**| Show only editorial content that is available for distribution in a certain country | |
| **dateTakenStart** | **LocalDate**| Show images that were taken on or after the specified date; use this parameter if you want recently created images from the collection instead of updated older assets | [optional] |
| **dateTakenEnd** | **LocalDate**| Show images that were taken before the specified date | [optional] |
| **cursor** | **String**| The cursor of the page with which to start fetching results; this cursor is returned from previous requests | [optional] |
| **sort** | **String**| Sort by | [optional] [default to newest] [enum: newest, oldest] |
| **supplierCode** | [**List&lt;String&gt;**](String.md)| Show only editorial content from certain suppliers | [optional] |
| **perPage** | **Integer**| Number of results per page | [optional] [default to 500] |

### Return type

[**EditorialUpdatedResults**](EditorialUpdatedResults.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **406** | Not Acceptable |  -  |

<a id="licenseEditorialImage"></a>
# **licenseEditorialImage**
> LicenseEditorialContentResults licenseEditorialImage(licenseEditorialContentRequest)

(Deprecated) License editorial content

Deprecated; use &#x60;POST /v2/editorial/images/licenses&#x60; instead to get licenses for one or more editorial images. You must specify the country and one or more editorial images to license. The download links in the response are valid for 8 hours.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EditorialImagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.shutterstock.com");
    
    // Configure OAuth2 access token for authorization: customer_accessCode
    OAuth customer_accessCode = (OAuth) defaultClient.getAuthentication("customer_accessCode");
    customer_accessCode.setAccessToken("YOUR ACCESS TOKEN");

    EditorialImagesApi apiInstance = new EditorialImagesApi(defaultClient);
    LicenseEditorialContentRequest licenseEditorialContentRequest = new LicenseEditorialContentRequest(); // LicenseEditorialContentRequest | License editorial content
    try {
      LicenseEditorialContentResults result = apiInstance.licenseEditorialImage(licenseEditorialContentRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EditorialImagesApi#licenseEditorialImage");
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
| **licenseEditorialContentRequest** | [**LicenseEditorialContentRequest**](LicenseEditorialContentRequest.md)| License editorial content | |

### Return type

[**LicenseEditorialContentResults**](LicenseEditorialContentResults.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **406** | Not Acceptable |  -  |

<a id="licenseEditorialImages"></a>
# **licenseEditorialImages**
> LicenseEditorialContentResults licenseEditorialImages(licenseEditorialContentRequest)

License editorial content

This endpoint gets licenses for one or more editorial images. You must specify the country and one or more editorial images to license. The download links in the response are valid for 8 hours.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EditorialImagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.shutterstock.com");
    
    // Configure OAuth2 access token for authorization: customer_accessCode
    OAuth customer_accessCode = (OAuth) defaultClient.getAuthentication("customer_accessCode");
    customer_accessCode.setAccessToken("YOUR ACCESS TOKEN");

    EditorialImagesApi apiInstance = new EditorialImagesApi(defaultClient);
    LicenseEditorialContentRequest licenseEditorialContentRequest = new LicenseEditorialContentRequest(); // LicenseEditorialContentRequest | License editorial content
    try {
      LicenseEditorialContentResults result = apiInstance.licenseEditorialImages(licenseEditorialContentRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EditorialImagesApi#licenseEditorialImages");
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
| **licenseEditorialContentRequest** | [**LicenseEditorialContentRequest**](LicenseEditorialContentRequest.md)| License editorial content | |

### Return type

[**LicenseEditorialContentResults**](LicenseEditorialContentResults.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **406** | Not Acceptable |  -  |

<a id="listEditorialImageCategories"></a>
# **listEditorialImageCategories**
> EditorialImageCategoryResults listEditorialImageCategories()

List editorial categories

This endpoint lists the categories that editorial images can belong to, which are separate from the categories that other types of assets can belong to.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EditorialImagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.shutterstock.com");
    
    // Configure OAuth2 access token for authorization: customer_accessCode
    OAuth customer_accessCode = (OAuth) defaultClient.getAuthentication("customer_accessCode");
    customer_accessCode.setAccessToken("YOUR ACCESS TOKEN");

    // Configure HTTP basic authorization: basic
    HttpBasicAuth basic = (HttpBasicAuth) defaultClient.getAuthentication("basic");
    basic.setUsername("YOUR USERNAME");
    basic.setPassword("YOUR PASSWORD");

    EditorialImagesApi apiInstance = new EditorialImagesApi(defaultClient);
    try {
      EditorialImageCategoryResults result = apiInstance.listEditorialImageCategories();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EditorialImagesApi#listEditorialImageCategories");
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

[**EditorialImageCategoryResults**](EditorialImageCategoryResults.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |

<a id="searchEditorial"></a>
# **searchEditorial**
> EditorialSearchResults searchEditorial(country, query, sort, category, supplierCode, dateStart, dateEnd, perPage, cursor)

(Deprecated) Search editorial content

Deprecated; use &#x60;GET /v2/editorial/images/search&#x60; instead to search for editorial images.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EditorialImagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.shutterstock.com");
    
    // Configure OAuth2 access token for authorization: customer_accessCode
    OAuth customer_accessCode = (OAuth) defaultClient.getAuthentication("customer_accessCode");
    customer_accessCode.setAccessToken("YOUR ACCESS TOKEN");

    // Configure HTTP basic authorization: basic
    HttpBasicAuth basic = (HttpBasicAuth) defaultClient.getAuthentication("basic");
    basic.setUsername("YOUR USERNAME");
    basic.setPassword("YOUR PASSWORD");

    EditorialImagesApi apiInstance = new EditorialImagesApi(defaultClient);
    String country = "USA"; // String | Show only editorial content that is available for distribution in a certain country
    String query = "query_example"; // String | One or more search terms separated by spaces
    String sort = "relevant"; // String | Sort by
    String category = "category_example"; // String | Show editorial content within a certain editorial category; specify by category name
    List<String> supplierCode = Arrays.asList(); // List<String> | Show only editorial content from certain suppliers
    LocalDate dateStart = LocalDate.now(); // LocalDate | Show only editorial content generated on or after a specific date
    LocalDate dateEnd = LocalDate.now(); // LocalDate | Show only editorial content generated on or before a specific date
    Integer perPage = 20; // Integer | Number of results per page
    String cursor = "cursor_example"; // String | The cursor of the page with which to start fetching results; this cursor is returned from previous requests
    try {
      EditorialSearchResults result = apiInstance.searchEditorial(country, query, sort, category, supplierCode, dateStart, dateEnd, perPage, cursor);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EditorialImagesApi#searchEditorial");
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
| **country** | **String**| Show only editorial content that is available for distribution in a certain country | |
| **query** | **String**| One or more search terms separated by spaces | [optional] |
| **sort** | **String**| Sort by | [optional] [default to relevant] [enum: relevant, newest, oldest] |
| **category** | **String**| Show editorial content within a certain editorial category; specify by category name | [optional] |
| **supplierCode** | [**List&lt;String&gt;**](String.md)| Show only editorial content from certain suppliers | [optional] |
| **dateStart** | **LocalDate**| Show only editorial content generated on or after a specific date | [optional] |
| **dateEnd** | **LocalDate**| Show only editorial content generated on or before a specific date | [optional] |
| **perPage** | **Integer**| Number of results per page | [optional] [default to 20] |
| **cursor** | **String**| The cursor of the page with which to start fetching results; this cursor is returned from previous requests | [optional] |

### Return type

[**EditorialSearchResults**](EditorialSearchResults.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **406** | Not Acceptable |  -  |

<a id="searchEditorialImages"></a>
# **searchEditorialImages**
> EditorialSearchResults searchEditorialImages(country, query, sort, category, supplierCode, dateStart, dateEnd, perPage, cursor)

Search editorial images

This endpoint searches for editorial images. If you specify more than one search parameter, the API uses an AND condition. For example, if you set the &#x60;category&#x60; parameter to \&quot;Alone,Performing\&quot; and also specify a &#x60;query&#x60; parameter, the results include only images that match the query and are in both the Alone and Performing categories. You can also filter search terms out in the &#x60;query&#x60; parameter by prefixing the term with NOT.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EditorialImagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.shutterstock.com");
    
    // Configure OAuth2 access token for authorization: customer_accessCode
    OAuth customer_accessCode = (OAuth) defaultClient.getAuthentication("customer_accessCode");
    customer_accessCode.setAccessToken("YOUR ACCESS TOKEN");

    // Configure HTTP basic authorization: basic
    HttpBasicAuth basic = (HttpBasicAuth) defaultClient.getAuthentication("basic");
    basic.setUsername("YOUR USERNAME");
    basic.setPassword("YOUR PASSWORD");

    EditorialImagesApi apiInstance = new EditorialImagesApi(defaultClient);
    String country = "USA"; // String | Show only editorial content that is available for distribution in a certain country
    String query = "The Academy Awards"; // String | One or more search terms separated by spaces
    String sort = "relevant"; // String | Sort by
    String category = "Alone,Performing"; // String | Show editorial content with each of the specified editorial categories; specify category names in a comma-separated list
    List<String> supplierCode = Arrays.asList(); // List<String> | Show only editorial content from certain suppliers
    LocalDate dateStart = LocalDate.parse("2020-05-29"); // LocalDate | Show only editorial content generated on or after a specific date
    LocalDate dateEnd = LocalDate.parse("2021-05-29"); // LocalDate | Show only editorial content generated on or before a specific date
    Integer perPage = 20; // Integer | Number of results per page
    String cursor = "eyJ2IjoxLCJzIjoxfQ=="; // String | The cursor of the page with which to start fetching results; this cursor is returned from previous requests
    try {
      EditorialSearchResults result = apiInstance.searchEditorialImages(country, query, sort, category, supplierCode, dateStart, dateEnd, perPage, cursor);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EditorialImagesApi#searchEditorialImages");
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
| **country** | **String**| Show only editorial content that is available for distribution in a certain country | |
| **query** | **String**| One or more search terms separated by spaces | [optional] |
| **sort** | **String**| Sort by | [optional] [default to relevant] [enum: relevant, newest, oldest] |
| **category** | **String**| Show editorial content with each of the specified editorial categories; specify category names in a comma-separated list | [optional] |
| **supplierCode** | [**List&lt;String&gt;**](String.md)| Show only editorial content from certain suppliers | [optional] |
| **dateStart** | **LocalDate**| Show only editorial content generated on or after a specific date | [optional] |
| **dateEnd** | **LocalDate**| Show only editorial content generated on or before a specific date | [optional] |
| **perPage** | **Integer**| Number of results per page | [optional] [default to 20] |
| **cursor** | **String**| The cursor of the page with which to start fetching results; this cursor is returned from previous requests | [optional] |

### Return type

[**EditorialSearchResults**](EditorialSearchResults.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **406** | Not Acceptable |  -  |

<a id="v2EditorialIdGet"></a>
# **v2EditorialIdGet**
> EditorialContent v2EditorialIdGet(id, country, searchId)

(Deprecated) Get editorial content details

Deprecated; use &#x60;GET /v2/editorial/images/{id}&#x60; instead to show information about an editorial image, including a URL to a preview image and the sizes that it is available in.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EditorialImagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.shutterstock.com");
    
    // Configure OAuth2 access token for authorization: customer_accessCode
    OAuth customer_accessCode = (OAuth) defaultClient.getAuthentication("customer_accessCode");
    customer_accessCode.setAccessToken("YOUR ACCESS TOKEN");

    // Configure HTTP basic authorization: basic
    HttpBasicAuth basic = (HttpBasicAuth) defaultClient.getAuthentication("basic");
    basic.setUsername("YOUR USERNAME");
    basic.setPassword("YOUR PASSWORD");

    EditorialImagesApi apiInstance = new EditorialImagesApi(defaultClient);
    String id = "9926131a"; // String | Editorial ID
    String country = "USA"; // String | Returns only if the content is available for distribution in a certain country
    String searchId = "00000000-0000-0000-0000-000000000000"; // String | The ID of the search that is related to this request
    try {
      EditorialContent result = apiInstance.v2EditorialIdGet(id, country, searchId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EditorialImagesApi#v2EditorialIdGet");
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
| **id** | **String**| Editorial ID | |
| **country** | **String**| Returns only if the content is available for distribution in a certain country | |
| **searchId** | **String**| The ID of the search that is related to this request | [optional] |

### Return type

[**EditorialContent**](EditorialContent.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

