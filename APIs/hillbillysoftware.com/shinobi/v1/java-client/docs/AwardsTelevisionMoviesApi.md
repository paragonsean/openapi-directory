# AwardsTelevisionMoviesApi

All URIs are relative to *https://api.hillbillysoftware.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**awardsGet**](AwardsTelevisionMoviesApi.md#awardsGet) | **GET** /Awards/ByYear/{Year} | Gets all awards for requested year |
| [**awardsbyWinnerGet**](AwardsTelevisionMoviesApi.md#awardsbyWinnerGet) | **GET** /Awards/ByWinner/{AccessToken}/{Nominee} | Gets all awards by nominiee |


<a id="awardsGet"></a>
# **awardsGet**
> List&lt;Awards&gt; awardsGet(year)

Gets all awards for requested year

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AwardsTelevisionMoviesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hillbillysoftware.com");

    AwardsTelevisionMoviesApi apiInstance = new AwardsTelevisionMoviesApi(defaultClient);
    String year = "year_example"; // String | 
    try {
      List<Awards> result = apiInstance.awardsGet(year);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AwardsTelevisionMoviesApi#awardsGet");
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
| **year** | **String**|  | |

### Return type

[**List&lt;Awards&gt;**](Awards.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of awards |  -  |

<a id="awardsbyWinnerGet"></a>
# **awardsbyWinnerGet**
> List&lt;Awards&gt; awardsbyWinnerGet(accessToken, nominee)

Gets all awards by nominiee

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AwardsTelevisionMoviesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hillbillysoftware.com");

    AwardsTelevisionMoviesApi apiInstance = new AwardsTelevisionMoviesApi(defaultClient);
    String accessToken = "accessToken_example"; // String | 
    String nominee = "nominee_example"; // String | 
    try {
      List<Awards> result = apiInstance.awardsbyWinnerGet(accessToken, nominee);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AwardsTelevisionMoviesApi#awardsbyWinnerGet");
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
| **accessToken** | **String**|  | |
| **nominee** | **String**|  | |

### Return type

[**List&lt;Awards&gt;**](Awards.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of awards |  -  |

