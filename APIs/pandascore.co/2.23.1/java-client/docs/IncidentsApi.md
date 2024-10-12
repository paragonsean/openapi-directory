# IncidentsApi

All URIs are relative to *https://api.pandascore.co*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getAdditions**](IncidentsApi.md#getAdditions) | **GET** /additions | List additions |
| [**getChanges**](IncidentsApi.md#getChanges) | **GET** /changes | List changes |
| [**getDeletions**](IncidentsApi.md#getDeletions) | **GET** /deletions | List deletions |
| [**getIncidents**](IncidentsApi.md#getIncidents) | **GET** /incidents | List changes, additions and deletions |


<a id="getAdditions"></a>
# **getAdditions**
> List&lt;NonDeletionIncident&gt; getAdditions(page, perPage, type, since, videogame)

List additions

Get the latest additions.  This endpoint only shows unchanged objects.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IncidentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.pandascore.co");
    
    // Configure HTTP bearer authorization: BearerToken
    HttpBearerAuth BearerToken = (HttpBearerAuth) defaultClient.getAuthentication("BearerToken");
    BearerToken.setBearerToken("BEARER TOKEN");

    // Configure API key authorization: QueryToken
    ApiKeyAuth QueryToken = (ApiKeyAuth) defaultClient.getAuthentication("QueryToken");
    QueryToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //QueryToken.setApiKeyPrefix("Token");

    IncidentsApi apiInstance = new IncidentsApi(defaultClient);
    GetAdditionsPageParameter page = new GetAdditionsPageParameter(); // GetAdditionsPageParameter | Pagination in the form of `page=2` or `page[size]=30&amp;page[number]=2`
    Integer perPage = 50; // Integer | Equivalent to `page[size]`
    List<String> type = Arrays.asList(); // List<String> | Filter by result type(s)
    OffsetDateTime since = OffsetDateTime.now(); // OffsetDateTime | Filter out older results
    List<VideogameIDOrSlug> videogame = Arrays.asList(); // List<VideogameIDOrSlug> | Filter by videogame(s)
    try {
      List<NonDeletionIncident> result = apiInstance.getAdditions(page, perPage, type, since, videogame);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IncidentsApi#getAdditions");
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
| **page** | [**GetAdditionsPageParameter**](.md)| Pagination in the form of &#x60;page&#x3D;2&#x60; or &#x60;page[size]&#x3D;30&amp;amp;page[number]&#x3D;2&#x60; | [optional] |
| **perPage** | **Integer**| Equivalent to &#x60;page[size]&#x60; | [optional] [default to 50] |
| **type** | [**List&lt;String&gt;**](String.md)| Filter by result type(s) | [optional] [enum: league, match, player, serie, team, tournament] |
| **since** | **OffsetDateTime**| Filter out older results | [optional] |
| **videogame** | [**List&lt;VideogameIDOrSlug&gt;**](VideogameIDOrSlug.md)| Filter by videogame(s) | [optional] |

### Return type

[**List&lt;NonDeletionIncident&gt;**](NonDeletionIncident.md)

### Authorization

[BearerToken](../README.md#BearerToken), [QueryToken](../README.md#QueryToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of created entities |  -  |
| **400** | Bad request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not found |  -  |
| **422** | Unprocessable Entity |  -  |

<a id="getChanges"></a>
# **getChanges**
> List&lt;Incident&gt; getChanges(page, perPage, type, since, videogame)

List changes

Get the latest updates.  This endpoint only provides the latest change for an object. It does not keep track of previous changes.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IncidentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.pandascore.co");
    
    // Configure HTTP bearer authorization: BearerToken
    HttpBearerAuth BearerToken = (HttpBearerAuth) defaultClient.getAuthentication("BearerToken");
    BearerToken.setBearerToken("BEARER TOKEN");

    // Configure API key authorization: QueryToken
    ApiKeyAuth QueryToken = (ApiKeyAuth) defaultClient.getAuthentication("QueryToken");
    QueryToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //QueryToken.setApiKeyPrefix("Token");

    IncidentsApi apiInstance = new IncidentsApi(defaultClient);
    GetAdditionsPageParameter page = new GetAdditionsPageParameter(); // GetAdditionsPageParameter | Pagination in the form of `page=2` or `page[size]=30&amp;page[number]=2`
    Integer perPage = 50; // Integer | Equivalent to `page[size]`
    List<String> type = Arrays.asList(); // List<String> | Filter by result type(s)
    OffsetDateTime since = OffsetDateTime.now(); // OffsetDateTime | Filter out older results
    List<VideogameIDOrSlug> videogame = Arrays.asList(); // List<VideogameIDOrSlug> | Filter by videogame(s)
    try {
      List<Incident> result = apiInstance.getChanges(page, perPage, type, since, videogame);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IncidentsApi#getChanges");
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
| **page** | [**GetAdditionsPageParameter**](.md)| Pagination in the form of &#x60;page&#x3D;2&#x60; or &#x60;page[size]&#x3D;30&amp;amp;page[number]&#x3D;2&#x60; | [optional] |
| **perPage** | **Integer**| Equivalent to &#x60;page[size]&#x60; | [optional] [default to 50] |
| **type** | [**List&lt;String&gt;**](String.md)| Filter by result type(s) | [optional] [enum: league, match, player, serie, team, tournament] |
| **since** | **OffsetDateTime**| Filter out older results | [optional] |
| **videogame** | [**List&lt;VideogameIDOrSlug&gt;**](VideogameIDOrSlug.md)| Filter by videogame(s) | [optional] |

### Return type

[**List&lt;Incident&gt;**](Incident.md)

### Authorization

[BearerToken](../README.md#BearerToken), [QueryToken](../README.md#QueryToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of changed entities |  -  |
| **400** | Bad request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not found |  -  |
| **422** | Unprocessable Entity |  -  |

<a id="getDeletions"></a>
# **getDeletions**
> List&lt;DeletionIncident&gt; getDeletions(page, perPage, type, since, videogame)

List deletions

Get the latest deleted documents

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IncidentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.pandascore.co");
    
    // Configure HTTP bearer authorization: BearerToken
    HttpBearerAuth BearerToken = (HttpBearerAuth) defaultClient.getAuthentication("BearerToken");
    BearerToken.setBearerToken("BEARER TOKEN");

    // Configure API key authorization: QueryToken
    ApiKeyAuth QueryToken = (ApiKeyAuth) defaultClient.getAuthentication("QueryToken");
    QueryToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //QueryToken.setApiKeyPrefix("Token");

    IncidentsApi apiInstance = new IncidentsApi(defaultClient);
    GetAdditionsPageParameter page = new GetAdditionsPageParameter(); // GetAdditionsPageParameter | Pagination in the form of `page=2` or `page[size]=30&amp;page[number]=2`
    Integer perPage = 50; // Integer | Equivalent to `page[size]`
    List<String> type = Arrays.asList(); // List<String> | Filter by result type(s)
    OffsetDateTime since = OffsetDateTime.now(); // OffsetDateTime | Filter out older results
    List<VideogameIDOrSlug> videogame = Arrays.asList(); // List<VideogameIDOrSlug> | Filter by videogame(s)
    try {
      List<DeletionIncident> result = apiInstance.getDeletions(page, perPage, type, since, videogame);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IncidentsApi#getDeletions");
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
| **page** | [**GetAdditionsPageParameter**](.md)| Pagination in the form of &#x60;page&#x3D;2&#x60; or &#x60;page[size]&#x3D;30&amp;amp;page[number]&#x3D;2&#x60; | [optional] |
| **perPage** | **Integer**| Equivalent to &#x60;page[size]&#x60; | [optional] [default to 50] |
| **type** | [**List&lt;String&gt;**](String.md)| Filter by result type(s) | [optional] [enum: league, match, player, serie, team, tournament] |
| **since** | **OffsetDateTime**| Filter out older results | [optional] |
| **videogame** | [**List&lt;VideogameIDOrSlug&gt;**](VideogameIDOrSlug.md)| Filter by videogame(s) | [optional] |

### Return type

[**List&lt;DeletionIncident&gt;**](DeletionIncident.md)

### Authorization

[BearerToken](../README.md#BearerToken), [QueryToken](../README.md#QueryToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of deleted entities |  -  |
| **400** | Bad request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not found |  -  |
| **422** | Unprocessable Entity |  -  |

<a id="getIncidents"></a>
# **getIncidents**
> List&lt;Incident&gt; getIncidents(page, perPage, type, since, videogame)

List changes, additions and deletions

 Get the latest updates and additions.  This endpoint only provides the latest incident for an object. It does not keep track of previous incidents.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IncidentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.pandascore.co");
    
    // Configure HTTP bearer authorization: BearerToken
    HttpBearerAuth BearerToken = (HttpBearerAuth) defaultClient.getAuthentication("BearerToken");
    BearerToken.setBearerToken("BEARER TOKEN");

    // Configure API key authorization: QueryToken
    ApiKeyAuth QueryToken = (ApiKeyAuth) defaultClient.getAuthentication("QueryToken");
    QueryToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //QueryToken.setApiKeyPrefix("Token");

    IncidentsApi apiInstance = new IncidentsApi(defaultClient);
    GetAdditionsPageParameter page = new GetAdditionsPageParameter(); // GetAdditionsPageParameter | Pagination in the form of `page=2` or `page[size]=30&amp;page[number]=2`
    Integer perPage = 50; // Integer | Equivalent to `page[size]`
    List<String> type = Arrays.asList(); // List<String> | Filter by result type(s)
    OffsetDateTime since = OffsetDateTime.now(); // OffsetDateTime | Filter out older results
    List<VideogameIDOrSlug> videogame = Arrays.asList(); // List<VideogameIDOrSlug> | Filter by videogame(s)
    try {
      List<Incident> result = apiInstance.getIncidents(page, perPage, type, since, videogame);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IncidentsApi#getIncidents");
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
| **page** | [**GetAdditionsPageParameter**](.md)| Pagination in the form of &#x60;page&#x3D;2&#x60; or &#x60;page[size]&#x3D;30&amp;amp;page[number]&#x3D;2&#x60; | [optional] |
| **perPage** | **Integer**| Equivalent to &#x60;page[size]&#x60; | [optional] [default to 50] |
| **type** | [**List&lt;String&gt;**](String.md)| Filter by result type(s) | [optional] [enum: league, match, player, serie, team, tournament] |
| **since** | **OffsetDateTime**| Filter out older results | [optional] |
| **videogame** | [**List&lt;VideogameIDOrSlug&gt;**](VideogameIDOrSlug.md)| Filter by videogame(s) | [optional] |

### Return type

[**List&lt;Incident&gt;**](Incident.md)

### Authorization

[BearerToken](../README.md#BearerToken), [QueryToken](../README.md#QueryToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of created or updated entities |  -  |
| **400** | Bad request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not found |  -  |
| **422** | Unprocessable Entity |  -  |

