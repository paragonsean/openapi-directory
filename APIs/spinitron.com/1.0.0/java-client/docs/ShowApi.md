# ShowApi

All URIs are relative to *https://spinitron.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**showsGet**](ShowApi.md#showsGet) | **GET** /shows | Returns scheduled shows optionally filtered by {start} and/or {end} datetimes |
| [**showsIdGet**](ShowApi.md#showsIdGet) | **GET** /shows/{id} | Get a Show by id |


<a id="showsGet"></a>
# **showsGet**
> ShowsGet200Response showsGet(start, end, count, page, fields, expand)

Returns scheduled shows optionally filtered by {start} and/or {end} datetimes

**Terminology**: Spinitron defines a *show* as a radio program. A show can have one or more *schedules*, each of which may specify either an *occurence* or a *repetition*, which represents a set of occurences. Thus scheduled shows have occurences that, for example, may be displayed in a calendar.  In the response, &#x60;items&#x60; is an array of objects representing occurences of scheduled shows.  You may optionally filter &#x60;items&#x60; to a datetime *range* by including in the request {start} and/or {end} parameters, both of which must be no more than one hour in the past. An occurence starting at {end} is included in the reponse.  &#x60;itmes&#x60; can include occurences that begin *or* end within the filter range. A show that goes on air before {start} appears in &#x60;items&#x60; if it ends *after* but not *at* {start}. An occurence starting at or before {end} is included.  If the request omits the {start} parameter, the server sets its value to the current time so that the filter range&#39;s start is always defined. If the request specifies {end} then the requested range is *bounded*, otherwise it is *unbounded*.  For a bounded request, &#x60;items&#x60; includes *every* occurence of all shows occuring in the range. The only difference between objects in &#x60;items&#x60; representing a given show will be the &#x60;start&#x60; field value.  For an unbounded request, &#x60;items&#x60; includes *only one* occurence per show, specifically, the next occurrence after {start} of all shows occuring after {start}.  Use an unbounded request to get a straight list all shows. Use a bounded request to get a calendar/agenda of shows expanded into occurrences by thir shedules and repetitions.  Objects in &#x60;items&#x60; are ordered first by &#x60;datetime&#x60; and then by &#x60;id&#x60;. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ShowApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://spinitron.com/api");
    
    // Configure API key authorization: accessToken
    ApiKeyAuth accessToken = (ApiKeyAuth) defaultClient.getAuthentication("accessToken");
    accessToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //accessToken.setApiKeyPrefix("Token");

    // Configure HTTP bearer authorization: httpBearer
    HttpBearerAuth httpBearer = (HttpBearerAuth) defaultClient.getAuthentication("httpBearer");
    httpBearer.setBearerToken("BEARER TOKEN");

    ShowApi apiInstance = new ShowApi(defaultClient);
    OffsetDateTime start = OffsetDateTime.now(); // OffsetDateTime | The datetime starting from items must be returned. Maximum 1 hour in past. 
    OffsetDateTime end = OffsetDateTime.now(); // OffsetDateTime | The ending datetime. Maximum 1 hour in past. 
    Integer count = 20; // Integer | Amount of items to return
    Integer page = 56; // Integer | Offset, used together with count
    List<String> fields = Arrays.asList(); // List<String> | Allows to select only needed fields
    List<String> expand = Arrays.asList(); // List<String> | Allows to select extra fields
    try {
      ShowsGet200Response result = apiInstance.showsGet(start, end, count, page, fields, expand);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ShowApi#showsGet");
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
| **start** | **OffsetDateTime**| The datetime starting from items must be returned. Maximum 1 hour in past.  | [optional] |
| **end** | **OffsetDateTime**| The ending datetime. Maximum 1 hour in past.  | [optional] |
| **count** | **Integer**| Amount of items to return | [optional] [default to 20] |
| **page** | **Integer**| Offset, used together with count | [optional] |
| **fields** | [**List&lt;String&gt;**](String.md)| Allows to select only needed fields | [optional] |
| **expand** | [**List&lt;String&gt;**](String.md)| Allows to select extra fields | [optional] |

### Return type

[**ShowsGet200Response**](ShowsGet200Response.md)

### Authorization

[accessToken](../README.md#accessToken), [httpBearer](../README.md#httpBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The shows |  -  |
| **422** | Invalid datetimes in filter: either too old or {end} is less than {start}.  |  -  |

<a id="showsIdGet"></a>
# **showsIdGet**
> Show showsIdGet(id, fields, expand)

Get a Show by id

The response object represents the next occurence of the show specified by {id}.  Status 404 is returned if a show with {id} does not exist or if it does but all its scheduled occurences elapsed in the past. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ShowApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://spinitron.com/api");
    
    // Configure API key authorization: accessToken
    ApiKeyAuth accessToken = (ApiKeyAuth) defaultClient.getAuthentication("accessToken");
    accessToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //accessToken.setApiKeyPrefix("Token");

    // Configure HTTP bearer authorization: httpBearer
    HttpBearerAuth httpBearer = (HttpBearerAuth) defaultClient.getAuthentication("httpBearer");
    httpBearer.setBearerToken("BEARER TOKEN");

    ShowApi apiInstance = new ShowApi(defaultClient);
    Integer id = 56; // Integer | 
    List<String> fields = Arrays.asList(); // List<String> | Allows to select only needed fields
    List<String> expand = Arrays.asList(); // List<String> | Allows to select extra fields
    try {
      Show result = apiInstance.showsIdGet(id, fields, expand);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ShowApi#showsIdGet");
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
| **id** | **Integer**|  | |
| **fields** | [**List&lt;String&gt;**](String.md)| Allows to select only needed fields | [optional] |
| **expand** | [**List&lt;String&gt;**](String.md)| Allows to select extra fields | [optional] |

### Return type

[**Show**](Show.md)

### Authorization

[accessToken](../README.md#accessToken), [httpBearer](../README.md#httpBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The Show |  -  |
| **404** | Show not found or too old |  -  |

