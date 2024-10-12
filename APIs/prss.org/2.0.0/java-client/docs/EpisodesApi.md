# EpisodesApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiV2EpisodesGet**](EpisodesApi.md#apiV2EpisodesGet) | **GET** /api/v2/episodes | Gets episodes matching the given criteria. |
| [**apiV2EpisodesIdGet**](EpisodesApi.md#apiV2EpisodesIdGet) | **GET** /api/v2/episodes/{id} | Returns the episode matching the given ID. |


<a id="apiV2EpisodesGet"></a>
# **apiV2EpisodesGet**
> List&lt;Episode&gt; apiV2EpisodesGet(programId, id, beginAirDateAfter, endAirDateBefore, pageStart, pageSize, orderById)

Gets episodes matching the given criteria.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EpisodesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: cd_oauth2
    OAuth cd_oauth2 = (OAuth) defaultClient.getAuthentication("cd_oauth2");
    cd_oauth2.setAccessToken("YOUR ACCESS TOKEN");

    EpisodesApi apiInstance = new EpisodesApi(defaultClient);
    Long programId = 56L; // Long | Matches on the ID of the program that owns the episode.
    Long id = 56L; // Long | Matches on the ID of the episode.
    OffsetDateTime beginAirDateAfter = OffsetDateTime.now(); // OffsetDateTime | Matches on the begin air date of the episode (inclusive).
    OffsetDateTime endAirDateBefore = OffsetDateTime.now(); // OffsetDateTime | Matches on the end air date of the episode (inclusive).
    Integer pageStart = 0; // Integer | The start page of the results to return. The first item is indexed at 0.
    Integer pageSize = 500; // Integer | The number of items to return. Must be between 0 and 500, inclusive.
    String orderById = "asc"; // String | The sort order of the list of episodes, based on episode ID. If unspecified, the episodes are returned in random order. If using paging to iterate through the results, sort order should be specified.
    try {
      List<Episode> result = apiInstance.apiV2EpisodesGet(programId, id, beginAirDateAfter, endAirDateBefore, pageStart, pageSize, orderById);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EpisodesApi#apiV2EpisodesGet");
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
| **programId** | **Long**| Matches on the ID of the program that owns the episode. | |
| **id** | **Long**| Matches on the ID of the episode. | [optional] |
| **beginAirDateAfter** | **OffsetDateTime**| Matches on the begin air date of the episode (inclusive). | [optional] |
| **endAirDateBefore** | **OffsetDateTime**| Matches on the end air date of the episode (inclusive). | [optional] |
| **pageStart** | **Integer**| The start page of the results to return. The first item is indexed at 0. | [optional] [default to 0] |
| **pageSize** | **Integer**| The number of items to return. Must be between 0 and 500, inclusive. | [optional] [default to 500] |
| **orderById** | **String**| The sort order of the list of episodes, based on episode ID. If unspecified, the episodes are returned in random order. If using paging to iterate through the results, sort order should be specified. | [optional] [enum: asc, desc] |

### Return type

[**List&lt;Episode&gt;**](Episode.md)

### Authorization

[cd_oauth2](../README.md#cd_oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The matching episode. |  -  |
| **400** | The request is missing required data or invalid. |  -  |
| **403** | Authorization failed, or the user is not permitted to view this program or its episodes. |  -  |
| **404** | The program cannot be found. |  -  |

<a id="apiV2EpisodesIdGet"></a>
# **apiV2EpisodesIdGet**
> Episode apiV2EpisodesIdGet(id)

Returns the episode matching the given ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EpisodesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: cd_oauth2
    OAuth cd_oauth2 = (OAuth) defaultClient.getAuthentication("cd_oauth2");
    cd_oauth2.setAccessToken("YOUR ACCESS TOKEN");

    EpisodesApi apiInstance = new EpisodesApi(defaultClient);
    Long id = 56L; // Long | The ID of the episode to operate on.
    try {
      Episode result = apiInstance.apiV2EpisodesIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EpisodesApi#apiV2EpisodesIdGet");
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
| **id** | **Long**| The ID of the episode to operate on. | |

### Return type

[**Episode**](Episode.md)

### Authorization

[cd_oauth2](../README.md#cd_oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The matching episode. |  -  |
| **403** | Authorization failed, or the user is not permitted to view this episode. |  -  |
| **404** | The episode cannot be found. |  -  |

