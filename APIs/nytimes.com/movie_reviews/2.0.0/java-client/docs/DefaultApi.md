# DefaultApi

All URIs are relative to *http://api.nytimes.com/svc/movies/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**criticsResourceTypeJsonGet**](DefaultApi.md#criticsResourceTypeJsonGet) | **GET** /critics/{resource-type}.json |  |
| [**reviewsResourceTypeJsonGet**](DefaultApi.md#reviewsResourceTypeJsonGet) | **GET** /reviews/{resource-type}.json |  |
| [**reviewsSearchJsonGet**](DefaultApi.md#reviewsSearchJsonGet) | **GET** /reviews/search.json |  |


<a id="criticsResourceTypeJsonGet"></a>
# **criticsResourceTypeJsonGet**
> CriticsResourceTypeJsonGet200Response criticsResourceTypeJsonGet(resourceType)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.nytimes.com/svc/movies/v2");
    
    // Configure API key authorization: apikey
    ApiKeyAuth apikey = (ApiKeyAuth) defaultClient.getAuthentication("apikey");
    apikey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apikey.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String resourceType = "resourceType_example"; // String | all | full-time | part-time | [reviewer-name]  Specify all to get all Times reviewers, or specify full-time or part-time to get that subset. Specify a reviewer's name to get details about a particular reviewer. 
    try {
      CriticsResourceTypeJsonGet200Response result = apiInstance.criticsResourceTypeJsonGet(resourceType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#criticsResourceTypeJsonGet");
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
| **resourceType** | **String**| all | full-time | part-time | [reviewer-name]  Specify all to get all Times reviewers, or specify full-time or part-time to get that subset. Specify a reviewer&#39;s name to get details about a particular reviewer.  | |

### Return type

[**CriticsResourceTypeJsonGet200Response**](CriticsResourceTypeJsonGet200Response.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | An array of Movie Critics |  -  |

<a id="reviewsResourceTypeJsonGet"></a>
# **reviewsResourceTypeJsonGet**
> ReviewsSearchJsonGet200Response reviewsResourceTypeJsonGet(resourceType, offset, order)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.nytimes.com/svc/movies/v2");
    
    // Configure API key authorization: apikey
    ApiKeyAuth apikey = (ApiKeyAuth) defaultClient.getAuthentication("apikey");
    apikey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apikey.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String resourceType = "all"; // String | Specify all to retrieve all reviews, including NYT Critics' Picks.  Specify picks to get NYT Critics' Picks currently in theaters.  
    Integer offset = 20; // Integer | Positive integer, multiple of 20
    String order = "by-title"; // String | Sets the sort order of the results.  Results ordered by-title are in ascending alphabetical order. Results ordered by one of the date parameters are in reverse chronological order.  If you do not specify a sort order, the results will be ordered by publication-date. 
    try {
      ReviewsSearchJsonGet200Response result = apiInstance.reviewsResourceTypeJsonGet(resourceType, offset, order);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#reviewsResourceTypeJsonGet");
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
| **resourceType** | **String**| Specify all to retrieve all reviews, including NYT Critics&#39; Picks.  Specify picks to get NYT Critics&#39; Picks currently in theaters.   | [enum: all, picks] |
| **offset** | **Integer**| Positive integer, multiple of 20 | [optional] [default to 20] |
| **order** | **String**| Sets the sort order of the results.  Results ordered by-title are in ascending alphabetical order. Results ordered by one of the date parameters are in reverse chronological order.  If you do not specify a sort order, the results will be ordered by publication-date.  | [optional] [default to by-publication-date] [enum: by-title, by-publication-date, by-opening-date] |

### Return type

[**ReviewsSearchJsonGet200Response**](ReviewsSearchJsonGet200Response.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | An array of Movies |  -  |

<a id="reviewsSearchJsonGet"></a>
# **reviewsSearchJsonGet**
> ReviewsSearchJsonGet200Response reviewsSearchJsonGet(query, criticsPick, reviewer, publicationDate, openingDate, offset, order)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.nytimes.com/svc/movies/v2");
    
    // Configure API key authorization: apikey
    ApiKeyAuth apikey = (ApiKeyAuth) defaultClient.getAuthentication("apikey");
    apikey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apikey.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String query = "query_example"; // String | Search keywords; matches movie title and indexed terms  To limit your search to exact matches only, surround your search string with single quotation marks (e.g., query='28+days+later'). Otherwise, responses will include partial matches (\"head words\") as well as exact matches (e.g., president will match president, presidents and presidential).      If you specify multiple terms without quotation marks, they will be combined in an OR search.      If you omit the query parameter, your request will be equivalent to a reviews and NYT Critics' Picks request. 
    String criticsPick = "Y"; // String | Set this parameter to Y to limit the results to NYT Critics' Picks. To get only those movies that have not been highlighted by Times critics, specify critics-pick=N. (To get all reviews regardless of critics-pick status, simply omit this parameter.) 
    String reviewer = "reviewer_example"; // String | Include this parameter to limit your results to reviews by a specific critic. Reviewer names should be formatted like this: Manohla Dargis. 
    String publicationDate = "publicationDate_example"; // String | Single date: YYYY-MM-DD  Start and end date: YYYY-MM-DD;YYYY-MM-DD  The publication-date is the date the review was first published in The Times. 
    String openingDate = "openingDate_example"; // String | Single date: YYYY-MM-DD  Start and end date: YYYY-MM-DD;YYYY-MM-DD  The opening-date is the date the movie's opening date in the New York region. 
    Integer offset = 20; // Integer | Positive integer, multiple of 20
    String order = "order_example"; // String | Sets the sort order of the results.  Results ordered by-title are in ascending alphabetical order. Results ordered by one of the date parameters are in reverse chronological order.  If you do not specify a sort order, the results will be ordered by publication-date. 
    try {
      ReviewsSearchJsonGet200Response result = apiInstance.reviewsSearchJsonGet(query, criticsPick, reviewer, publicationDate, openingDate, offset, order);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#reviewsSearchJsonGet");
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
| **query** | **String**| Search keywords; matches movie title and indexed terms  To limit your search to exact matches only, surround your search string with single quotation marks (e.g., query&#x3D;&#39;28+days+later&#39;). Otherwise, responses will include partial matches (\&quot;head words\&quot;) as well as exact matches (e.g., president will match president, presidents and presidential).      If you specify multiple terms without quotation marks, they will be combined in an OR search.      If you omit the query parameter, your request will be equivalent to a reviews and NYT Critics&#39; Picks request.  | [optional] |
| **criticsPick** | **String**| Set this parameter to Y to limit the results to NYT Critics&#39; Picks. To get only those movies that have not been highlighted by Times critics, specify critics-pick&#x3D;N. (To get all reviews regardless of critics-pick status, simply omit this parameter.)  | [optional] [enum: Y, N] |
| **reviewer** | **String**| Include this parameter to limit your results to reviews by a specific critic. Reviewer names should be formatted like this: Manohla Dargis.  | [optional] |
| **publicationDate** | **String**| Single date: YYYY-MM-DD  Start and end date: YYYY-MM-DD;YYYY-MM-DD  The publication-date is the date the review was first published in The Times.  | [optional] |
| **openingDate** | **String**| Single date: YYYY-MM-DD  Start and end date: YYYY-MM-DD;YYYY-MM-DD  The opening-date is the date the movie&#39;s opening date in the New York region.  | [optional] |
| **offset** | **Integer**| Positive integer, multiple of 20 | [optional] [default to 20] |
| **order** | **String**| Sets the sort order of the results.  Results ordered by-title are in ascending alphabetical order. Results ordered by one of the date parameters are in reverse chronological order.  If you do not specify a sort order, the results will be ordered by publication-date.  | [optional] |

### Return type

[**ReviewsSearchJsonGet200Response**](ReviewsSearchJsonGet200Response.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | An array of Movies |  -  |

