# EditorialVideoApi

All URIs are relative to *https://api.shutterstock.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getEditorialVideo**](EditorialVideoApi.md#getEditorialVideo) | **GET** /v2/editorial/videos/{id} | Get editorial video content details |
| [**getEditorialVideoLicenseList**](EditorialVideoApi.md#getEditorialVideoLicenseList) | **GET** /v2/editorial/videos/licenses | List editorial video licenses |
| [**licenseEditorialVideo**](EditorialVideoApi.md#licenseEditorialVideo) | **POST** /v2/editorial/videos/licenses | License editorial video content |
| [**listEditorialVideoCategories**](EditorialVideoApi.md#listEditorialVideoCategories) | **GET** /v2/editorial/videos/categories | List editorial video categories |
| [**searchEditorialVideos**](EditorialVideoApi.md#searchEditorialVideos) | **GET** /v2/editorial/videos/search | Search editorial video content |


<a id="getEditorialVideo"></a>
# **getEditorialVideo**
> EditorialVideoContent getEditorialVideo(id, country, searchId)

Get editorial video content details

This endpoint shows information about an editorial image, including a URL to a preview image and the sizes that it is available in.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EditorialVideoApi;

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

    EditorialVideoApi apiInstance = new EditorialVideoApi(defaultClient);
    String id = "9926131a"; // String | Editorial ID
    String country = "USA"; // String | Returns only if the content is available for distribution in a certain country
    String searchId = "00000000-0000-0000-0000-000000000000"; // String | The ID of the search that is related to this request
    try {
      EditorialVideoContent result = apiInstance.getEditorialVideo(id, country, searchId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EditorialVideoApi#getEditorialVideo");
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

[**EditorialVideoContent**](EditorialVideoContent.md)

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

<a id="getEditorialVideoLicenseList"></a>
# **getEditorialVideoLicenseList**
> DownloadHistoryDataList getEditorialVideoLicenseList(videoId, license, page, perPage, sort, username, startDate, endDate, downloadAvailability, teamHistory)

List editorial video licenses

This endpoint lists existing editorial video licenses.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EditorialVideoApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.shutterstock.com");
    
    // Configure OAuth2 access token for authorization: customer_accessCode
    OAuth customer_accessCode = (OAuth) defaultClient.getAuthentication("customer_accessCode");
    customer_accessCode.setAccessToken("YOUR ACCESS TOKEN");

    EditorialVideoApi apiInstance = new EditorialVideoApi(defaultClient);
    String videoId = "12345678"; // String | Show licenses for the specified editorial video ID
    String license = "premier_editorial_all_media"; // String | Show editorial videos that are available with the specified license name
    Integer page = 1; // Integer | Page number
    Integer perPage = 20; // Integer | Number of results per page
    String sort = "newest"; // String | Sort order
    String username = "aUniqueUsername"; // String | Filter licenses by username of licensee
    OffsetDateTime startDate = OffsetDateTime.parse("2021-03-29T13:25:13.521Z"); // OffsetDateTime | Show licenses created on or after the specified date
    OffsetDateTime endDate = OffsetDateTime.parse("2021-03-29T13:25:13.521Z"); // OffsetDateTime | Show licenses created before the specified date
    String downloadAvailability = "all"; // String | Filter licenses by download availability
    Boolean teamHistory = false; // Boolean | Set to true to see license history for all members of your team.
    try {
      DownloadHistoryDataList result = apiInstance.getEditorialVideoLicenseList(videoId, license, page, perPage, sort, username, startDate, endDate, downloadAvailability, teamHistory);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EditorialVideoApi#getEditorialVideoLicenseList");
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
| **videoId** | **String**| Show licenses for the specified editorial video ID | [optional] |
| **license** | **String**| Show editorial videos that are available with the specified license name | [optional] |
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

<a id="licenseEditorialVideo"></a>
# **licenseEditorialVideo**
> LicenseEditorialContentResults licenseEditorialVideo(licenseEditorialVideoContentRequest)

License editorial video content

This endpoint gets licenses for one or more editorial videos. You must specify the country and one or more editorial videos to license. The download links in the response are valid for 8 hours.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EditorialVideoApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.shutterstock.com");
    
    // Configure OAuth2 access token for authorization: customer_accessCode
    OAuth customer_accessCode = (OAuth) defaultClient.getAuthentication("customer_accessCode");
    customer_accessCode.setAccessToken("YOUR ACCESS TOKEN");

    EditorialVideoApi apiInstance = new EditorialVideoApi(defaultClient);
    LicenseEditorialVideoContentRequest licenseEditorialVideoContentRequest = new LicenseEditorialVideoContentRequest(); // LicenseEditorialVideoContentRequest | License editorial video content
    try {
      LicenseEditorialContentResults result = apiInstance.licenseEditorialVideo(licenseEditorialVideoContentRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EditorialVideoApi#licenseEditorialVideo");
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
| **licenseEditorialVideoContentRequest** | [**LicenseEditorialVideoContentRequest**](LicenseEditorialVideoContentRequest.md)| License editorial video content | |

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

<a id="listEditorialVideoCategories"></a>
# **listEditorialVideoCategories**
> EditorialVideoCategoryResults listEditorialVideoCategories()

List editorial video categories

This endpoint lists the categories that editorial videos can belong to, which are separate from the categories that other types of assets can belong to.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EditorialVideoApi;

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

    EditorialVideoApi apiInstance = new EditorialVideoApi(defaultClient);
    try {
      EditorialVideoCategoryResults result = apiInstance.listEditorialVideoCategories();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EditorialVideoApi#listEditorialVideoCategories");
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

[**EditorialVideoCategoryResults**](EditorialVideoCategoryResults.md)

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

<a id="searchEditorialVideos"></a>
# **searchEditorialVideos**
> EditorialVideoSearchResults searchEditorialVideos(country, query, sort, category, supplierCode, dateStart, dateEnd, resolution, fps, perPage, cursor)

Search editorial video content

This endpoint searches for editorial videos. If you specify more than one search parameter, the API uses an AND condition. For example, if you set the &#x60;category&#x60; parameter to \&quot;Alone,Performing\&quot; and also specify a &#x60;query&#x60; parameter, the results include only videos that match the query and are in both the Alone and Performing categories.  You can also filter search terms out in the &#x60;query&#x60; parameter by prefixing the term with NOT.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EditorialVideoApi;

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

    EditorialVideoApi apiInstance = new EditorialVideoApi(defaultClient);
    String country = "USA"; // String | Show only editorial video content that is available for distribution in a certain country
    String query = "The Academy Awards"; // String | One or more search terms separated by spaces
    String sort = "relevant"; // String | Sort by
    String category = "Alone,Performing"; // String | Show editorial content with each of the specified editorial categories; specify category names in a comma-separated list
    List<String> supplierCode = Arrays.asList(); // List<String> | Show only editorial video content from certain suppliers
    LocalDate dateStart = LocalDate.parse("2020-05-29"); // LocalDate | Show only editorial video content generated on or after a specific date
    LocalDate dateEnd = LocalDate.parse("2021-05-29"); // LocalDate | Show only editorial video content generated on or before a specific date
    String resolution = "4k"; // String | Show only editorial video content with specific resolution
    BigDecimal fps = new BigDecimal("24"); // BigDecimal | Show only editorial video content generated with specific frames per second
    Integer perPage = 20; // Integer | Number of results per page
    String cursor = "eyJ2IjoxLCJzIjoxfQ=="; // String | The cursor of the page with which to start fetching results; this cursor is returned from previous requests
    try {
      EditorialVideoSearchResults result = apiInstance.searchEditorialVideos(country, query, sort, category, supplierCode, dateStart, dateEnd, resolution, fps, perPage, cursor);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EditorialVideoApi#searchEditorialVideos");
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
| **country** | **String**| Show only editorial video content that is available for distribution in a certain country | |
| **query** | **String**| One or more search terms separated by spaces | [optional] |
| **sort** | **String**| Sort by | [optional] [default to relevant] [enum: relevant, newest, oldest] |
| **category** | **String**| Show editorial content with each of the specified editorial categories; specify category names in a comma-separated list | [optional] |
| **supplierCode** | [**List&lt;String&gt;**](String.md)| Show only editorial video content from certain suppliers | [optional] |
| **dateStart** | **LocalDate**| Show only editorial video content generated on or after a specific date | [optional] |
| **dateEnd** | **LocalDate**| Show only editorial video content generated on or before a specific date | [optional] |
| **resolution** | **String**| Show only editorial video content with specific resolution | [optional] [enum: 4k, high_definition, standard_definition] |
| **fps** | **BigDecimal**| Show only editorial video content generated with specific frames per second | [optional] |
| **perPage** | **Integer**| Number of results per page | [optional] [default to 20] |
| **cursor** | **String**| The cursor of the page with which to start fetching results; this cursor is returned from previous requests | [optional] |

### Return type

[**EditorialVideoSearchResults**](EditorialVideoSearchResults.md)

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

