# StatsApi

All URIs are relative to *https://cloudsearch.googleapis.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**cloudsearchStatsGetIndex**](StatsApi.md#cloudsearchStatsGetIndex) | **GET** /v1/stats/index |  |
| [**cloudsearchStatsGetQuery**](StatsApi.md#cloudsearchStatsGetQuery) | **GET** /v1/stats/query |  |
| [**cloudsearchStatsGetSearchapplication**](StatsApi.md#cloudsearchStatsGetSearchapplication) | **GET** /v1/stats/searchapplication |  |
| [**cloudsearchStatsGetSession**](StatsApi.md#cloudsearchStatsGetSession) | **GET** /v1/stats/session |  |
| [**cloudsearchStatsGetUser**](StatsApi.md#cloudsearchStatsGetUser) | **GET** /v1/stats/user |  |
| [**cloudsearchStatsIndexDatasourcesGet**](StatsApi.md#cloudsearchStatsIndexDatasourcesGet) | **GET** /v1/stats/index/{name} |  |
| [**cloudsearchStatsQuerySearchapplicationsGet**](StatsApi.md#cloudsearchStatsQuerySearchapplicationsGet) | **GET** /v1/stats/query/{name} |  |
| [**cloudsearchStatsSessionSearchapplicationsGet**](StatsApi.md#cloudsearchStatsSessionSearchapplicationsGet) | **GET** /v1/stats/session/{name} |  |
| [**cloudsearchStatsUserSearchapplicationsGet**](StatsApi.md#cloudsearchStatsUserSearchapplicationsGet) | **GET** /v1/stats/user/{name} |  |


<a id="cloudsearchStatsGetIndex"></a>
# **cloudsearchStatsGetIndex**
> GetCustomerIndexStatsResponse cloudsearchStatsGetIndex($xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, fromDateDay, fromDateMonth, fromDateYear, toDateDay, toDateMonth, toDateYear)



Gets indexed item statistics aggreggated across all data sources. This API only returns statistics for previous dates; it doesn&#39;t return statistics for the current day. **Note:** This API requires a standard end user account to execute.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StatsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://cloudsearch.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    StatsApi apiInstance = new StatsApi(defaultClient);
    String $xgafv = "1"; // String | V1 error format.
    String accessToken = "accessToken_example"; // String | OAuth access token.
    String alt = "json"; // String | Data format for response.
    String paramCallback = "paramCallback_example"; // String | JSONP
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    String uploadProtocol = "uploadProtocol_example"; // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
    String uploadType = "uploadType_example"; // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
    Integer fromDateDay = 56; // Integer | Day of month. Must be from 1 to 31 and valid for the year and month.
    Integer fromDateMonth = 56; // Integer | Month of date. Must be from 1 to 12.
    Integer fromDateYear = 56; // Integer | Year of date. Must be from 1 to 9999.
    Integer toDateDay = 56; // Integer | Day of month. Must be from 1 to 31 and valid for the year and month.
    Integer toDateMonth = 56; // Integer | Month of date. Must be from 1 to 12.
    Integer toDateYear = 56; // Integer | Year of date. Must be from 1 to 9999.
    try {
      GetCustomerIndexStatsResponse result = apiInstance.cloudsearchStatsGetIndex($xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, fromDateDay, fromDateMonth, fromDateYear, toDateDay, toDateMonth, toDateYear);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StatsApi#cloudsearchStatsGetIndex");
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
| **$xgafv** | **String**| V1 error format. | [optional] [enum: 1, 2] |
| **accessToken** | **String**| OAuth access token. | [optional] |
| **alt** | **String**| Data format for response. | [optional] [enum: json, media, proto] |
| **paramCallback** | **String**| JSONP | [optional] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] |
| **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] |
| **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] |
| **fromDateDay** | **Integer**| Day of month. Must be from 1 to 31 and valid for the year and month. | [optional] |
| **fromDateMonth** | **Integer**| Month of date. Must be from 1 to 12. | [optional] |
| **fromDateYear** | **Integer**| Year of date. Must be from 1 to 9999. | [optional] |
| **toDateDay** | **Integer**| Day of month. Must be from 1 to 31 and valid for the year and month. | [optional] |
| **toDateMonth** | **Integer**| Month of date. Must be from 1 to 12. | [optional] |
| **toDateYear** | **Integer**| Year of date. Must be from 1 to 9999. | [optional] |

### Return type

[**GetCustomerIndexStatsResponse**](GetCustomerIndexStatsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="cloudsearchStatsGetQuery"></a>
# **cloudsearchStatsGetQuery**
> GetCustomerQueryStatsResponse cloudsearchStatsGetQuery($xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, fromDateDay, fromDateMonth, fromDateYear, toDateDay, toDateMonth, toDateYear)



Get the query statistics for customer. **Note:** This API requires a standard end user account to execute.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StatsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://cloudsearch.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    StatsApi apiInstance = new StatsApi(defaultClient);
    String $xgafv = "1"; // String | V1 error format.
    String accessToken = "accessToken_example"; // String | OAuth access token.
    String alt = "json"; // String | Data format for response.
    String paramCallback = "paramCallback_example"; // String | JSONP
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    String uploadProtocol = "uploadProtocol_example"; // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
    String uploadType = "uploadType_example"; // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
    Integer fromDateDay = 56; // Integer | Day of month. Must be from 1 to 31 and valid for the year and month.
    Integer fromDateMonth = 56; // Integer | Month of date. Must be from 1 to 12.
    Integer fromDateYear = 56; // Integer | Year of date. Must be from 1 to 9999.
    Integer toDateDay = 56; // Integer | Day of month. Must be from 1 to 31 and valid for the year and month.
    Integer toDateMonth = 56; // Integer | Month of date. Must be from 1 to 12.
    Integer toDateYear = 56; // Integer | Year of date. Must be from 1 to 9999.
    try {
      GetCustomerQueryStatsResponse result = apiInstance.cloudsearchStatsGetQuery($xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, fromDateDay, fromDateMonth, fromDateYear, toDateDay, toDateMonth, toDateYear);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StatsApi#cloudsearchStatsGetQuery");
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
| **$xgafv** | **String**| V1 error format. | [optional] [enum: 1, 2] |
| **accessToken** | **String**| OAuth access token. | [optional] |
| **alt** | **String**| Data format for response. | [optional] [enum: json, media, proto] |
| **paramCallback** | **String**| JSONP | [optional] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] |
| **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] |
| **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] |
| **fromDateDay** | **Integer**| Day of month. Must be from 1 to 31 and valid for the year and month. | [optional] |
| **fromDateMonth** | **Integer**| Month of date. Must be from 1 to 12. | [optional] |
| **fromDateYear** | **Integer**| Year of date. Must be from 1 to 9999. | [optional] |
| **toDateDay** | **Integer**| Day of month. Must be from 1 to 31 and valid for the year and month. | [optional] |
| **toDateMonth** | **Integer**| Month of date. Must be from 1 to 12. | [optional] |
| **toDateYear** | **Integer**| Year of date. Must be from 1 to 9999. | [optional] |

### Return type

[**GetCustomerQueryStatsResponse**](GetCustomerQueryStatsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="cloudsearchStatsGetSearchapplication"></a>
# **cloudsearchStatsGetSearchapplication**
> GetCustomerSearchApplicationStatsResponse cloudsearchStatsGetSearchapplication($xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, endDateDay, endDateMonth, endDateYear, startDateDay, startDateMonth, startDateYear)



Get search application stats for customer. **Note:** This API requires a standard end user account to execute.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StatsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://cloudsearch.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    StatsApi apiInstance = new StatsApi(defaultClient);
    String $xgafv = "1"; // String | V1 error format.
    String accessToken = "accessToken_example"; // String | OAuth access token.
    String alt = "json"; // String | Data format for response.
    String paramCallback = "paramCallback_example"; // String | JSONP
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    String uploadProtocol = "uploadProtocol_example"; // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
    String uploadType = "uploadType_example"; // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
    Integer endDateDay = 56; // Integer | Day of month. Must be from 1 to 31 and valid for the year and month.
    Integer endDateMonth = 56; // Integer | Month of date. Must be from 1 to 12.
    Integer endDateYear = 56; // Integer | Year of date. Must be from 1 to 9999.
    Integer startDateDay = 56; // Integer | Day of month. Must be from 1 to 31 and valid for the year and month.
    Integer startDateMonth = 56; // Integer | Month of date. Must be from 1 to 12.
    Integer startDateYear = 56; // Integer | Year of date. Must be from 1 to 9999.
    try {
      GetCustomerSearchApplicationStatsResponse result = apiInstance.cloudsearchStatsGetSearchapplication($xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, endDateDay, endDateMonth, endDateYear, startDateDay, startDateMonth, startDateYear);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StatsApi#cloudsearchStatsGetSearchapplication");
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
| **$xgafv** | **String**| V1 error format. | [optional] [enum: 1, 2] |
| **accessToken** | **String**| OAuth access token. | [optional] |
| **alt** | **String**| Data format for response. | [optional] [enum: json, media, proto] |
| **paramCallback** | **String**| JSONP | [optional] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] |
| **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] |
| **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] |
| **endDateDay** | **Integer**| Day of month. Must be from 1 to 31 and valid for the year and month. | [optional] |
| **endDateMonth** | **Integer**| Month of date. Must be from 1 to 12. | [optional] |
| **endDateYear** | **Integer**| Year of date. Must be from 1 to 9999. | [optional] |
| **startDateDay** | **Integer**| Day of month. Must be from 1 to 31 and valid for the year and month. | [optional] |
| **startDateMonth** | **Integer**| Month of date. Must be from 1 to 12. | [optional] |
| **startDateYear** | **Integer**| Year of date. Must be from 1 to 9999. | [optional] |

### Return type

[**GetCustomerSearchApplicationStatsResponse**](GetCustomerSearchApplicationStatsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="cloudsearchStatsGetSession"></a>
# **cloudsearchStatsGetSession**
> GetCustomerSessionStatsResponse cloudsearchStatsGetSession($xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, fromDateDay, fromDateMonth, fromDateYear, toDateDay, toDateMonth, toDateYear)



Get the # of search sessions, % of successful sessions with a click query statistics for customer. **Note:** This API requires a standard end user account to execute.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StatsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://cloudsearch.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    StatsApi apiInstance = new StatsApi(defaultClient);
    String $xgafv = "1"; // String | V1 error format.
    String accessToken = "accessToken_example"; // String | OAuth access token.
    String alt = "json"; // String | Data format for response.
    String paramCallback = "paramCallback_example"; // String | JSONP
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    String uploadProtocol = "uploadProtocol_example"; // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
    String uploadType = "uploadType_example"; // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
    Integer fromDateDay = 56; // Integer | Day of month. Must be from 1 to 31 and valid for the year and month.
    Integer fromDateMonth = 56; // Integer | Month of date. Must be from 1 to 12.
    Integer fromDateYear = 56; // Integer | Year of date. Must be from 1 to 9999.
    Integer toDateDay = 56; // Integer | Day of month. Must be from 1 to 31 and valid for the year and month.
    Integer toDateMonth = 56; // Integer | Month of date. Must be from 1 to 12.
    Integer toDateYear = 56; // Integer | Year of date. Must be from 1 to 9999.
    try {
      GetCustomerSessionStatsResponse result = apiInstance.cloudsearchStatsGetSession($xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, fromDateDay, fromDateMonth, fromDateYear, toDateDay, toDateMonth, toDateYear);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StatsApi#cloudsearchStatsGetSession");
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
| **$xgafv** | **String**| V1 error format. | [optional] [enum: 1, 2] |
| **accessToken** | **String**| OAuth access token. | [optional] |
| **alt** | **String**| Data format for response. | [optional] [enum: json, media, proto] |
| **paramCallback** | **String**| JSONP | [optional] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] |
| **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] |
| **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] |
| **fromDateDay** | **Integer**| Day of month. Must be from 1 to 31 and valid for the year and month. | [optional] |
| **fromDateMonth** | **Integer**| Month of date. Must be from 1 to 12. | [optional] |
| **fromDateYear** | **Integer**| Year of date. Must be from 1 to 9999. | [optional] |
| **toDateDay** | **Integer**| Day of month. Must be from 1 to 31 and valid for the year and month. | [optional] |
| **toDateMonth** | **Integer**| Month of date. Must be from 1 to 12. | [optional] |
| **toDateYear** | **Integer**| Year of date. Must be from 1 to 9999. | [optional] |

### Return type

[**GetCustomerSessionStatsResponse**](GetCustomerSessionStatsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="cloudsearchStatsGetUser"></a>
# **cloudsearchStatsGetUser**
> GetCustomerUserStatsResponse cloudsearchStatsGetUser($xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, fromDateDay, fromDateMonth, fromDateYear, toDateDay, toDateMonth, toDateYear)



Get the users statistics for customer. **Note:** This API requires a standard end user account to execute.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StatsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://cloudsearch.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    StatsApi apiInstance = new StatsApi(defaultClient);
    String $xgafv = "1"; // String | V1 error format.
    String accessToken = "accessToken_example"; // String | OAuth access token.
    String alt = "json"; // String | Data format for response.
    String paramCallback = "paramCallback_example"; // String | JSONP
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    String uploadProtocol = "uploadProtocol_example"; // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
    String uploadType = "uploadType_example"; // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
    Integer fromDateDay = 56; // Integer | Day of month. Must be from 1 to 31 and valid for the year and month.
    Integer fromDateMonth = 56; // Integer | Month of date. Must be from 1 to 12.
    Integer fromDateYear = 56; // Integer | Year of date. Must be from 1 to 9999.
    Integer toDateDay = 56; // Integer | Day of month. Must be from 1 to 31 and valid for the year and month.
    Integer toDateMonth = 56; // Integer | Month of date. Must be from 1 to 12.
    Integer toDateYear = 56; // Integer | Year of date. Must be from 1 to 9999.
    try {
      GetCustomerUserStatsResponse result = apiInstance.cloudsearchStatsGetUser($xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, fromDateDay, fromDateMonth, fromDateYear, toDateDay, toDateMonth, toDateYear);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StatsApi#cloudsearchStatsGetUser");
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
| **$xgafv** | **String**| V1 error format. | [optional] [enum: 1, 2] |
| **accessToken** | **String**| OAuth access token. | [optional] |
| **alt** | **String**| Data format for response. | [optional] [enum: json, media, proto] |
| **paramCallback** | **String**| JSONP | [optional] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] |
| **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] |
| **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] |
| **fromDateDay** | **Integer**| Day of month. Must be from 1 to 31 and valid for the year and month. | [optional] |
| **fromDateMonth** | **Integer**| Month of date. Must be from 1 to 12. | [optional] |
| **fromDateYear** | **Integer**| Year of date. Must be from 1 to 9999. | [optional] |
| **toDateDay** | **Integer**| Day of month. Must be from 1 to 31 and valid for the year and month. | [optional] |
| **toDateMonth** | **Integer**| Month of date. Must be from 1 to 12. | [optional] |
| **toDateYear** | **Integer**| Year of date. Must be from 1 to 9999. | [optional] |

### Return type

[**GetCustomerUserStatsResponse**](GetCustomerUserStatsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="cloudsearchStatsIndexDatasourcesGet"></a>
# **cloudsearchStatsIndexDatasourcesGet**
> GetDataSourceIndexStatsResponse cloudsearchStatsIndexDatasourcesGet(name, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, fromDateDay, fromDateMonth, fromDateYear, toDateDay, toDateMonth, toDateYear)



Gets indexed item statistics for a single data source. **Note:** This API requires a standard end user account to execute.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StatsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://cloudsearch.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    StatsApi apiInstance = new StatsApi(defaultClient);
    String name = "name_example"; // String | The resource id of the data source to retrieve statistics for, in the following format: \"datasources/{source_id}\"
    String $xgafv = "1"; // String | V1 error format.
    String accessToken = "accessToken_example"; // String | OAuth access token.
    String alt = "json"; // String | Data format for response.
    String paramCallback = "paramCallback_example"; // String | JSONP
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    String uploadProtocol = "uploadProtocol_example"; // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
    String uploadType = "uploadType_example"; // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
    Integer fromDateDay = 56; // Integer | Day of month. Must be from 1 to 31 and valid for the year and month.
    Integer fromDateMonth = 56; // Integer | Month of date. Must be from 1 to 12.
    Integer fromDateYear = 56; // Integer | Year of date. Must be from 1 to 9999.
    Integer toDateDay = 56; // Integer | Day of month. Must be from 1 to 31 and valid for the year and month.
    Integer toDateMonth = 56; // Integer | Month of date. Must be from 1 to 12.
    Integer toDateYear = 56; // Integer | Year of date. Must be from 1 to 9999.
    try {
      GetDataSourceIndexStatsResponse result = apiInstance.cloudsearchStatsIndexDatasourcesGet(name, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, fromDateDay, fromDateMonth, fromDateYear, toDateDay, toDateMonth, toDateYear);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StatsApi#cloudsearchStatsIndexDatasourcesGet");
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
| **name** | **String**| The resource id of the data source to retrieve statistics for, in the following format: \&quot;datasources/{source_id}\&quot; | |
| **$xgafv** | **String**| V1 error format. | [optional] [enum: 1, 2] |
| **accessToken** | **String**| OAuth access token. | [optional] |
| **alt** | **String**| Data format for response. | [optional] [enum: json, media, proto] |
| **paramCallback** | **String**| JSONP | [optional] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] |
| **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] |
| **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] |
| **fromDateDay** | **Integer**| Day of month. Must be from 1 to 31 and valid for the year and month. | [optional] |
| **fromDateMonth** | **Integer**| Month of date. Must be from 1 to 12. | [optional] |
| **fromDateYear** | **Integer**| Year of date. Must be from 1 to 9999. | [optional] |
| **toDateDay** | **Integer**| Day of month. Must be from 1 to 31 and valid for the year and month. | [optional] |
| **toDateMonth** | **Integer**| Month of date. Must be from 1 to 12. | [optional] |
| **toDateYear** | **Integer**| Year of date. Must be from 1 to 9999. | [optional] |

### Return type

[**GetDataSourceIndexStatsResponse**](GetDataSourceIndexStatsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="cloudsearchStatsQuerySearchapplicationsGet"></a>
# **cloudsearchStatsQuerySearchapplicationsGet**
> GetSearchApplicationQueryStatsResponse cloudsearchStatsQuerySearchapplicationsGet(name, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, fromDateDay, fromDateMonth, fromDateYear, toDateDay, toDateMonth, toDateYear)



Get the query statistics for search application. **Note:** This API requires a standard end user account to execute.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StatsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://cloudsearch.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    StatsApi apiInstance = new StatsApi(defaultClient);
    String name = "name_example"; // String | The resource id of the search application query stats, in the following format: searchapplications/{application_id}
    String $xgafv = "1"; // String | V1 error format.
    String accessToken = "accessToken_example"; // String | OAuth access token.
    String alt = "json"; // String | Data format for response.
    String paramCallback = "paramCallback_example"; // String | JSONP
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    String uploadProtocol = "uploadProtocol_example"; // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
    String uploadType = "uploadType_example"; // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
    Integer fromDateDay = 56; // Integer | Day of month. Must be from 1 to 31 and valid for the year and month.
    Integer fromDateMonth = 56; // Integer | Month of date. Must be from 1 to 12.
    Integer fromDateYear = 56; // Integer | Year of date. Must be from 1 to 9999.
    Integer toDateDay = 56; // Integer | Day of month. Must be from 1 to 31 and valid for the year and month.
    Integer toDateMonth = 56; // Integer | Month of date. Must be from 1 to 12.
    Integer toDateYear = 56; // Integer | Year of date. Must be from 1 to 9999.
    try {
      GetSearchApplicationQueryStatsResponse result = apiInstance.cloudsearchStatsQuerySearchapplicationsGet(name, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, fromDateDay, fromDateMonth, fromDateYear, toDateDay, toDateMonth, toDateYear);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StatsApi#cloudsearchStatsQuerySearchapplicationsGet");
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
| **name** | **String**| The resource id of the search application query stats, in the following format: searchapplications/{application_id} | |
| **$xgafv** | **String**| V1 error format. | [optional] [enum: 1, 2] |
| **accessToken** | **String**| OAuth access token. | [optional] |
| **alt** | **String**| Data format for response. | [optional] [enum: json, media, proto] |
| **paramCallback** | **String**| JSONP | [optional] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] |
| **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] |
| **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] |
| **fromDateDay** | **Integer**| Day of month. Must be from 1 to 31 and valid for the year and month. | [optional] |
| **fromDateMonth** | **Integer**| Month of date. Must be from 1 to 12. | [optional] |
| **fromDateYear** | **Integer**| Year of date. Must be from 1 to 9999. | [optional] |
| **toDateDay** | **Integer**| Day of month. Must be from 1 to 31 and valid for the year and month. | [optional] |
| **toDateMonth** | **Integer**| Month of date. Must be from 1 to 12. | [optional] |
| **toDateYear** | **Integer**| Year of date. Must be from 1 to 9999. | [optional] |

### Return type

[**GetSearchApplicationQueryStatsResponse**](GetSearchApplicationQueryStatsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="cloudsearchStatsSessionSearchapplicationsGet"></a>
# **cloudsearchStatsSessionSearchapplicationsGet**
> GetSearchApplicationSessionStatsResponse cloudsearchStatsSessionSearchapplicationsGet(name, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, fromDateDay, fromDateMonth, fromDateYear, toDateDay, toDateMonth, toDateYear)



Get the # of search sessions, % of successful sessions with a click query statistics for search application. **Note:** This API requires a standard end user account to execute.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StatsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://cloudsearch.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    StatsApi apiInstance = new StatsApi(defaultClient);
    String name = "name_example"; // String | The resource id of the search application session stats, in the following format: searchapplications/{application_id}
    String $xgafv = "1"; // String | V1 error format.
    String accessToken = "accessToken_example"; // String | OAuth access token.
    String alt = "json"; // String | Data format for response.
    String paramCallback = "paramCallback_example"; // String | JSONP
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    String uploadProtocol = "uploadProtocol_example"; // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
    String uploadType = "uploadType_example"; // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
    Integer fromDateDay = 56; // Integer | Day of month. Must be from 1 to 31 and valid for the year and month.
    Integer fromDateMonth = 56; // Integer | Month of date. Must be from 1 to 12.
    Integer fromDateYear = 56; // Integer | Year of date. Must be from 1 to 9999.
    Integer toDateDay = 56; // Integer | Day of month. Must be from 1 to 31 and valid for the year and month.
    Integer toDateMonth = 56; // Integer | Month of date. Must be from 1 to 12.
    Integer toDateYear = 56; // Integer | Year of date. Must be from 1 to 9999.
    try {
      GetSearchApplicationSessionStatsResponse result = apiInstance.cloudsearchStatsSessionSearchapplicationsGet(name, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, fromDateDay, fromDateMonth, fromDateYear, toDateDay, toDateMonth, toDateYear);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StatsApi#cloudsearchStatsSessionSearchapplicationsGet");
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
| **name** | **String**| The resource id of the search application session stats, in the following format: searchapplications/{application_id} | |
| **$xgafv** | **String**| V1 error format. | [optional] [enum: 1, 2] |
| **accessToken** | **String**| OAuth access token. | [optional] |
| **alt** | **String**| Data format for response. | [optional] [enum: json, media, proto] |
| **paramCallback** | **String**| JSONP | [optional] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] |
| **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] |
| **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] |
| **fromDateDay** | **Integer**| Day of month. Must be from 1 to 31 and valid for the year and month. | [optional] |
| **fromDateMonth** | **Integer**| Month of date. Must be from 1 to 12. | [optional] |
| **fromDateYear** | **Integer**| Year of date. Must be from 1 to 9999. | [optional] |
| **toDateDay** | **Integer**| Day of month. Must be from 1 to 31 and valid for the year and month. | [optional] |
| **toDateMonth** | **Integer**| Month of date. Must be from 1 to 12. | [optional] |
| **toDateYear** | **Integer**| Year of date. Must be from 1 to 9999. | [optional] |

### Return type

[**GetSearchApplicationSessionStatsResponse**](GetSearchApplicationSessionStatsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="cloudsearchStatsUserSearchapplicationsGet"></a>
# **cloudsearchStatsUserSearchapplicationsGet**
> GetSearchApplicationUserStatsResponse cloudsearchStatsUserSearchapplicationsGet(name, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, fromDateDay, fromDateMonth, fromDateYear, toDateDay, toDateMonth, toDateYear)



Get the users statistics for search application. **Note:** This API requires a standard end user account to execute.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StatsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://cloudsearch.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    StatsApi apiInstance = new StatsApi(defaultClient);
    String name = "name_example"; // String | The resource id of the search application session stats, in the following format: searchapplications/{application_id}
    String $xgafv = "1"; // String | V1 error format.
    String accessToken = "accessToken_example"; // String | OAuth access token.
    String alt = "json"; // String | Data format for response.
    String paramCallback = "paramCallback_example"; // String | JSONP
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    String uploadProtocol = "uploadProtocol_example"; // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
    String uploadType = "uploadType_example"; // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
    Integer fromDateDay = 56; // Integer | Day of month. Must be from 1 to 31 and valid for the year and month.
    Integer fromDateMonth = 56; // Integer | Month of date. Must be from 1 to 12.
    Integer fromDateYear = 56; // Integer | Year of date. Must be from 1 to 9999.
    Integer toDateDay = 56; // Integer | Day of month. Must be from 1 to 31 and valid for the year and month.
    Integer toDateMonth = 56; // Integer | Month of date. Must be from 1 to 12.
    Integer toDateYear = 56; // Integer | Year of date. Must be from 1 to 9999.
    try {
      GetSearchApplicationUserStatsResponse result = apiInstance.cloudsearchStatsUserSearchapplicationsGet(name, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, fromDateDay, fromDateMonth, fromDateYear, toDateDay, toDateMonth, toDateYear);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StatsApi#cloudsearchStatsUserSearchapplicationsGet");
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
| **name** | **String**| The resource id of the search application session stats, in the following format: searchapplications/{application_id} | |
| **$xgafv** | **String**| V1 error format. | [optional] [enum: 1, 2] |
| **accessToken** | **String**| OAuth access token. | [optional] |
| **alt** | **String**| Data format for response. | [optional] [enum: json, media, proto] |
| **paramCallback** | **String**| JSONP | [optional] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] |
| **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] |
| **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] |
| **fromDateDay** | **Integer**| Day of month. Must be from 1 to 31 and valid for the year and month. | [optional] |
| **fromDateMonth** | **Integer**| Month of date. Must be from 1 to 12. | [optional] |
| **fromDateYear** | **Integer**| Year of date. Must be from 1 to 9999. | [optional] |
| **toDateDay** | **Integer**| Day of month. Must be from 1 to 31 and valid for the year and month. | [optional] |
| **toDateMonth** | **Integer**| Month of date. Must be from 1 to 12. | [optional] |
| **toDateYear** | **Integer**| Year of date. Must be from 1 to 9999. | [optional] |

### Return type

[**GetSearchApplicationUserStatsResponse**](GetSearchApplicationUserStatsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

