# RankingsApi

All URIs are relative to *https://api.schooldigger.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**rankingsGetRank**](RankingsApi.md#rankingsGetRank) | **GET** /v1/rankings/schools/{st} | Returns a SchoolDigger school ranking list |
| [**rankingsGetRankDistrict**](RankingsApi.md#rankingsGetRankDistrict) | **GET** /v1/rankings/districts/{st} | Returns a SchoolDigger district ranking list |


<a id="rankingsGetRank"></a>
# **rankingsGetRank**
> APISchoolListRank rankingsGetRank(st, appID, appKey, year, level, page, perPage)

Returns a SchoolDigger school ranking list

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RankingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.schooldigger.com");

    RankingsApi apiInstance = new RankingsApi(defaultClient);
    String st = "st_example"; // String | Two character state (e.g. 'CA')
    String appID = "appID_example"; // String | Your API app id
    String appKey = "appKey_example"; // String | Your API app key
    Integer year = 56; // Integer | The ranking year (leave blank for most recent year)
    String level = "level_example"; // String | Level of ranking: 'Elementary', 'Middle', or 'High'
    Integer page = 56; // Integer | Page number to retrieve (optional, default: 1)
    Integer perPage = 56; // Integer | Number of schools to retrieve on a page (50 max) (optional, default: 10)
    try {
      APISchoolListRank result = apiInstance.rankingsGetRank(st, appID, appKey, year, level, page, perPage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RankingsApi#rankingsGetRank");
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
| **st** | **String**| Two character state (e.g. &#39;CA&#39;) | |
| **appID** | **String**| Your API app id | |
| **appKey** | **String**| Your API app key | |
| **year** | **Integer**| The ranking year (leave blank for most recent year) | [optional] |
| **level** | **String**| Level of ranking: &#39;Elementary&#39;, &#39;Middle&#39;, or &#39;High&#39; | [optional] |
| **page** | **Integer**| Page number to retrieve (optional, default: 1) | [optional] |
| **perPage** | **Integer**| Number of schools to retrieve on a page (50 max) (optional, default: 10) | [optional] |

### Return type

[**APISchoolListRank**](APISchoolListRank.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="rankingsGetRankDistrict"></a>
# **rankingsGetRankDistrict**
> APIDistrictListRank rankingsGetRankDistrict(st, appID, appKey, year, page, perPage)

Returns a SchoolDigger district ranking list

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RankingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.schooldigger.com");

    RankingsApi apiInstance = new RankingsApi(defaultClient);
    String st = "st_example"; // String | Two character state (e.g. 'CA')
    String appID = "appID_example"; // String | Your API app id
    String appKey = "appKey_example"; // String | Your API app key
    Integer year = 56; // Integer | The ranking year (leave blank for most recent year)
    Integer page = 56; // Integer | Page number to retrieve (optional, default: 1)
    Integer perPage = 56; // Integer | Number of districts to retrieve on a page (50 max) (optional, default: 10)
    try {
      APIDistrictListRank result = apiInstance.rankingsGetRankDistrict(st, appID, appKey, year, page, perPage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RankingsApi#rankingsGetRankDistrict");
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
| **st** | **String**| Two character state (e.g. &#39;CA&#39;) | |
| **appID** | **String**| Your API app id | |
| **appKey** | **String**| Your API app key | |
| **year** | **Integer**| The ranking year (leave blank for most recent year) | [optional] |
| **page** | **Integer**| Page number to retrieve (optional, default: 1) | [optional] |
| **perPage** | **Integer**| Number of districts to retrieve on a page (50 max) (optional, default: 10) | [optional] |

### Return type

[**APIDistrictListRank**](APIDistrictListRank.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

