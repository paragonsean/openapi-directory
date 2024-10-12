# AbusesApi

All URIs are relative to *https://peertube2.cpy.re*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiV1AbusesAbuseIdDelete**](AbusesApi.md#apiV1AbusesAbuseIdDelete) | **DELETE** /api/v1/abuses/{abuseId} | Delete an abuse |
| [**apiV1AbusesAbuseIdMessagesAbuseMessageIdDelete**](AbusesApi.md#apiV1AbusesAbuseIdMessagesAbuseMessageIdDelete) | **DELETE** /api/v1/abuses/{abuseId}/messages/{abuseMessageId} | Delete an abuse message |
| [**apiV1AbusesAbuseIdMessagesGet**](AbusesApi.md#apiV1AbusesAbuseIdMessagesGet) | **GET** /api/v1/abuses/{abuseId}/messages | List messages of an abuse |
| [**apiV1AbusesAbuseIdMessagesPost**](AbusesApi.md#apiV1AbusesAbuseIdMessagesPost) | **POST** /api/v1/abuses/{abuseId}/messages | Add message to an abuse |
| [**apiV1AbusesAbuseIdPut**](AbusesApi.md#apiV1AbusesAbuseIdPut) | **PUT** /api/v1/abuses/{abuseId} | Update an abuse |
| [**apiV1AbusesPost**](AbusesApi.md#apiV1AbusesPost) | **POST** /api/v1/abuses | Report an abuse |
| [**getAbuses**](AbusesApi.md#getAbuses) | **GET** /api/v1/abuses | List abuses |
| [**getMyAbuses**](AbusesApi.md#getMyAbuses) | **GET** /api/v1/users/me/abuses | List my abuses |


<a id="apiV1AbusesAbuseIdDelete"></a>
# **apiV1AbusesAbuseIdDelete**
> apiV1AbusesAbuseIdDelete(abuseId)

Delete an abuse

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AbusesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://peertube2.cpy.re");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AbusesApi apiInstance = new AbusesApi(defaultClient);
    Integer abuseId = 56; // Integer | Abuse id
    try {
      apiInstance.apiV1AbusesAbuseIdDelete(abuseId);
    } catch (ApiException e) {
      System.err.println("Exception when calling AbusesApi#apiV1AbusesAbuseIdDelete");
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
| **abuseId** | **Integer**| Abuse id | |

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
| **404** | block not found |  -  |

<a id="apiV1AbusesAbuseIdMessagesAbuseMessageIdDelete"></a>
# **apiV1AbusesAbuseIdMessagesAbuseMessageIdDelete**
> apiV1AbusesAbuseIdMessagesAbuseMessageIdDelete(abuseId, abuseMessageId)

Delete an abuse message

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AbusesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://peertube2.cpy.re");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AbusesApi apiInstance = new AbusesApi(defaultClient);
    Integer abuseId = 56; // Integer | Abuse id
    Integer abuseMessageId = 56; // Integer | Abuse message id
    try {
      apiInstance.apiV1AbusesAbuseIdMessagesAbuseMessageIdDelete(abuseId, abuseMessageId);
    } catch (ApiException e) {
      System.err.println("Exception when calling AbusesApi#apiV1AbusesAbuseIdMessagesAbuseMessageIdDelete");
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
| **abuseId** | **Integer**| Abuse id | |
| **abuseMessageId** | **Integer**| Abuse message id | |

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

<a id="apiV1AbusesAbuseIdMessagesGet"></a>
# **apiV1AbusesAbuseIdMessagesGet**
> ApiV1AbusesAbuseIdMessagesGet200Response apiV1AbusesAbuseIdMessagesGet(abuseId)

List messages of an abuse

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AbusesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://peertube2.cpy.re");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AbusesApi apiInstance = new AbusesApi(defaultClient);
    Integer abuseId = 56; // Integer | Abuse id
    try {
      ApiV1AbusesAbuseIdMessagesGet200Response result = apiInstance.apiV1AbusesAbuseIdMessagesGet(abuseId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AbusesApi#apiV1AbusesAbuseIdMessagesGet");
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
| **abuseId** | **Integer**| Abuse id | |

### Return type

[**ApiV1AbusesAbuseIdMessagesGet200Response**](ApiV1AbusesAbuseIdMessagesGet200Response.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="apiV1AbusesAbuseIdMessagesPost"></a>
# **apiV1AbusesAbuseIdMessagesPost**
> apiV1AbusesAbuseIdMessagesPost(abuseId, apiV1AbusesAbuseIdMessagesPostRequest)

Add message to an abuse

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AbusesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://peertube2.cpy.re");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AbusesApi apiInstance = new AbusesApi(defaultClient);
    Integer abuseId = 56; // Integer | Abuse id
    ApiV1AbusesAbuseIdMessagesPostRequest apiV1AbusesAbuseIdMessagesPostRequest = new ApiV1AbusesAbuseIdMessagesPostRequest(); // ApiV1AbusesAbuseIdMessagesPostRequest | 
    try {
      apiInstance.apiV1AbusesAbuseIdMessagesPost(abuseId, apiV1AbusesAbuseIdMessagesPostRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling AbusesApi#apiV1AbusesAbuseIdMessagesPost");
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
| **abuseId** | **Integer**| Abuse id | |
| **apiV1AbusesAbuseIdMessagesPostRequest** | [**ApiV1AbusesAbuseIdMessagesPostRequest**](ApiV1AbusesAbuseIdMessagesPostRequest.md)|  | |

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
| **200** | successful operation |  -  |
| **400** | incorrect request parameters |  -  |

<a id="apiV1AbusesAbuseIdPut"></a>
# **apiV1AbusesAbuseIdPut**
> apiV1AbusesAbuseIdPut(abuseId, apiV1AbusesAbuseIdPutRequest)

Update an abuse

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AbusesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://peertube2.cpy.re");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AbusesApi apiInstance = new AbusesApi(defaultClient);
    Integer abuseId = 56; // Integer | Abuse id
    ApiV1AbusesAbuseIdPutRequest apiV1AbusesAbuseIdPutRequest = new ApiV1AbusesAbuseIdPutRequest(); // ApiV1AbusesAbuseIdPutRequest | 
    try {
      apiInstance.apiV1AbusesAbuseIdPut(abuseId, apiV1AbusesAbuseIdPutRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling AbusesApi#apiV1AbusesAbuseIdPut");
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
| **abuseId** | **Integer**| Abuse id | |
| **apiV1AbusesAbuseIdPutRequest** | [**ApiV1AbusesAbuseIdPutRequest**](ApiV1AbusesAbuseIdPutRequest.md)|  | [optional] |

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
| **404** | abuse not found |  -  |

<a id="apiV1AbusesPost"></a>
# **apiV1AbusesPost**
> ApiV1AbusesPost200Response apiV1AbusesPost(apiV1AbusesPostRequest)

Report an abuse

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AbusesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://peertube2.cpy.re");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AbusesApi apiInstance = new AbusesApi(defaultClient);
    ApiV1AbusesPostRequest apiV1AbusesPostRequest = new ApiV1AbusesPostRequest(); // ApiV1AbusesPostRequest | 
    try {
      ApiV1AbusesPost200Response result = apiInstance.apiV1AbusesPost(apiV1AbusesPostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AbusesApi#apiV1AbusesPost");
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
| **apiV1AbusesPostRequest** | [**ApiV1AbusesPostRequest**](ApiV1AbusesPostRequest.md)|  | |

### Return type

[**ApiV1AbusesPost200Response**](ApiV1AbusesPost200Response.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **400** | incorrect request parameters |  -  |

<a id="getAbuses"></a>
# **getAbuses**
> GetAbuses200Response getAbuses(id, predefinedReason, search, state, searchReporter, searchReportee, searchVideo, searchVideoChannel, videoIs, filter, start, count, sort)

List abuses

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AbusesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://peertube2.cpy.re");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AbusesApi apiInstance = new AbusesApi(defaultClient);
    Integer id = 56; // Integer | only list the report with this id
    List<String> predefinedReason = Arrays.asList(); // List<String> | predefined reason the listed reports should contain
    String search = "search_example"; // String | plain search that will match with video titles, reporter names and more
    AbuseStateSet state = AbuseStateSet.fromValue("1"); // AbuseStateSet | 
    String searchReporter = "searchReporter_example"; // String | only list reports of a specific reporter
    String searchReportee = "searchReportee_example"; // String | only list reports of a specific reportee
    String searchVideo = "searchVideo_example"; // String | only list reports of a specific video
    String searchVideoChannel = "searchVideoChannel_example"; // String | only list reports of a specific video channel
    String videoIs = "deleted"; // String | only list deleted or blocklisted videos
    String filter = "video"; // String | only list account, comment or video reports
    Integer start = 56; // Integer | Offset used to paginate results
    Integer count = 15; // Integer | Number of items to return
    String sort = "-id"; // String | Sort abuses by criteria
    try {
      GetAbuses200Response result = apiInstance.getAbuses(id, predefinedReason, search, state, searchReporter, searchReportee, searchVideo, searchVideoChannel, videoIs, filter, start, count, sort);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AbusesApi#getAbuses");
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
| **predefinedReason** | [**List&lt;String&gt;**](String.md)| predefined reason the listed reports should contain | [optional] [enum: violentOrAbusive, hatefulOrAbusive, spamOrMisleading, privacy, rights, serverRules, thumbnails, captions] |
| **search** | **String**| plain search that will match with video titles, reporter names and more | [optional] |
| **state** | [**AbuseStateSet**](.md)|  | [optional] [enum: 1, 2, 3] |
| **searchReporter** | **String**| only list reports of a specific reporter | [optional] |
| **searchReportee** | **String**| only list reports of a specific reportee | [optional] |
| **searchVideo** | **String**| only list reports of a specific video | [optional] |
| **searchVideoChannel** | **String**| only list reports of a specific video channel | [optional] |
| **videoIs** | **String**| only list deleted or blocklisted videos | [optional] [enum: deleted, blacklisted] |
| **filter** | **String**| only list account, comment or video reports | [optional] [enum: video, comment, account] |
| **start** | **Integer**| Offset used to paginate results | [optional] |
| **count** | **Integer**| Number of items to return | [optional] [default to 15] |
| **sort** | **String**| Sort abuses by criteria | [optional] [enum: -id, -createdAt, -state] |

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

<a id="getMyAbuses"></a>
# **getMyAbuses**
> GetAbuses200Response getMyAbuses(id, state, sort, start, count)

List my abuses

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AbusesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://peertube2.cpy.re");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AbusesApi apiInstance = new AbusesApi(defaultClient);
    Integer id = 56; // Integer | only list the report with this id
    AbuseStateSet state = AbuseStateSet.fromValue("1"); // AbuseStateSet | 
    String sort = "-id"; // String | Sort abuses by criteria
    Integer start = 56; // Integer | Offset used to paginate results
    Integer count = 15; // Integer | Number of items to return
    try {
      GetAbuses200Response result = apiInstance.getMyAbuses(id, state, sort, start, count);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AbusesApi#getMyAbuses");
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

