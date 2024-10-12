# ProjectApi

All URIs are relative to *https://api.botify.com/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getProjectAnalyses**](ProjectApi.md#getProjectAnalyses) | **GET** /analyses/{username}/{project_slug} | List all analyses for a project |
| [**getProjectUrlsAggs**](ProjectApi.md#getProjectUrlsAggs) | **POST** /projects/{username}/{project_slug}/urls/aggs | Project Query aggregator |
| [**getSavedFilter**](ProjectApi.md#getSavedFilter) | **GET** /projects/{username}/{project_slug}/filters/{identifier} | Retrieves a specific saved filter&#39;s name, ID and filter value |
| [**getSavedFilters**](ProjectApi.md#getSavedFilters) | **GET** /projects/{username}/{project_slug}/filters | List all the project&#39;s saved filters (each filter&#39;s name, ID and filter value) |
| [**testUrlRewritingRules**](ProjectApi.md#testUrlRewritingRules) | **POST** /projects/{username}/{project_slug}/features/url_rewriting/rules_validator | Match and replace parts of a URL based on rules passed in POST data |


<a id="getProjectAnalyses"></a>
# **getProjectAnalyses**
> GetProjectAnalyses200Response getProjectAnalyses(username, projectSlug, page, size)

List all analyses for a project

List all analyses for a project

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.botify.com/v1");
    
    // Configure API key authorization: DjangoRestToken
    ApiKeyAuth DjangoRestToken = (ApiKeyAuth) defaultClient.getAuthentication("DjangoRestToken");
    DjangoRestToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //DjangoRestToken.setApiKeyPrefix("Token");

    ProjectApi apiInstance = new ProjectApi(defaultClient);
    String username = "username_example"; // String | User's identifier
    String projectSlug = "projectSlug_example"; // String | Project's identifier
    Integer page = 56; // Integer | Page Number
    Integer size = 56; // Integer | Page Size
    try {
      GetProjectAnalyses200Response result = apiInstance.getProjectAnalyses(username, projectSlug, page, size);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectApi#getProjectAnalyses");
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
| **username** | **String**| User&#39;s identifier | |
| **projectSlug** | **String**| Project&#39;s identifier | |
| **page** | **Integer**| Page Number | [optional] |
| **size** | **Integer**| Page Size | [optional] |

### Return type

[**GetProjectAnalyses200Response**](GetProjectAnalyses200Response.md)

### Authorization

[DjangoRestToken](../README.md#DjangoRestToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |
| **0** | error payload |  -  |

<a id="getProjectUrlsAggs"></a>
# **getProjectUrlsAggs**
> Object getProjectUrlsAggs(username, projectSlug, area, lastAnalysisSlug, nbAnalyses, urlsAggsQuery)

Project Query aggregator

Project Query aggregator. It accepts multiple queries that will be executed on all completed analyses in the project

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.botify.com/v1");
    
    // Configure API key authorization: DjangoRestToken
    ApiKeyAuth DjangoRestToken = (ApiKeyAuth) defaultClient.getAuthentication("DjangoRestToken");
    DjangoRestToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //DjangoRestToken.setApiKeyPrefix("Token");

    ProjectApi apiInstance = new ProjectApi(defaultClient);
    String username = "username_example"; // String | User's identifier
    String projectSlug = "projectSlug_example"; // String | Project's identifier
    String area = "current"; // String | Analysis context to execute the queries
    String lastAnalysisSlug = "lastAnalysisSlug_example"; // String | Last analysis on the trend
    Integer nbAnalyses = 20; // Integer | Max number of analysis to return
    List<UrlsAggsQuery> urlsAggsQuery = Arrays.asList(); // List<UrlsAggsQuery> | 
    try {
      Object result = apiInstance.getProjectUrlsAggs(username, projectSlug, area, lastAnalysisSlug, nbAnalyses, urlsAggsQuery);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectApi#getProjectUrlsAggs");
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
| **username** | **String**| User&#39;s identifier | |
| **projectSlug** | **String**| Project&#39;s identifier | |
| **area** | **String**| Analysis context to execute the queries | [optional] [default to current] [enum: current, disappeared, new] |
| **lastAnalysisSlug** | **String**| Last analysis on the trend | [optional] |
| **nbAnalyses** | **Integer**| Max number of analysis to return | [optional] [default to 20] |
| **urlsAggsQuery** | [**List&lt;UrlsAggsQuery&gt;**](UrlsAggsQuery.md)|  | [optional] |

### Return type

**Object**

### Authorization

[DjangoRestToken](../README.md#DjangoRestToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Successful operation |  -  |
| **0** | error payload |  -  |

<a id="getSavedFilter"></a>
# **getSavedFilter**
> ProjectSavedFilter getSavedFilter(username, projectSlug, identifier)

Retrieves a specific saved filter&#39;s name, ID and filter value

Retrieves a specific saved filter&#39;s name, ID and filter value

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.botify.com/v1");
    
    // Configure API key authorization: DjangoRestToken
    ApiKeyAuth DjangoRestToken = (ApiKeyAuth) defaultClient.getAuthentication("DjangoRestToken");
    DjangoRestToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //DjangoRestToken.setApiKeyPrefix("Token");

    ProjectApi apiInstance = new ProjectApi(defaultClient);
    String username = "username_example"; // String | User's identifier
    String projectSlug = "projectSlug_example"; // String | Project's identifier
    String identifier = "identifier_example"; // String | Saved Filter's identifier
    try {
      ProjectSavedFilter result = apiInstance.getSavedFilter(username, projectSlug, identifier);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectApi#getSavedFilter");
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
| **username** | **String**| User&#39;s identifier | |
| **projectSlug** | **String**| Project&#39;s identifier | |
| **identifier** | **String**| Saved Filter&#39;s identifier | |

### Return type

[**ProjectSavedFilter**](ProjectSavedFilter.md)

### Authorization

[DjangoRestToken](../README.md#DjangoRestToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |
| **0** | error payload |  -  |

<a id="getSavedFilters"></a>
# **getSavedFilters**
> GetSavedFilters200Response getSavedFilters(username, projectSlug, page, size)

List all the project&#39;s saved filters (each filter&#39;s name, ID and filter value)

List all the project&#39;s saved filters (each filter&#39;s name, ID and filter value)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.botify.com/v1");
    
    // Configure API key authorization: DjangoRestToken
    ApiKeyAuth DjangoRestToken = (ApiKeyAuth) defaultClient.getAuthentication("DjangoRestToken");
    DjangoRestToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //DjangoRestToken.setApiKeyPrefix("Token");

    ProjectApi apiInstance = new ProjectApi(defaultClient);
    String username = "username_example"; // String | User's identifier
    String projectSlug = "projectSlug_example"; // String | Project's identifier
    Integer page = 56; // Integer | Page Number
    Integer size = 56; // Integer | Page Size
    try {
      GetSavedFilters200Response result = apiInstance.getSavedFilters(username, projectSlug, page, size);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectApi#getSavedFilters");
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
| **username** | **String**| User&#39;s identifier | |
| **projectSlug** | **String**| Project&#39;s identifier | |
| **page** | **Integer**| Page Number | [optional] |
| **size** | **Integer**| Page Size | [optional] |

### Return type

[**GetSavedFilters200Response**](GetSavedFilters200Response.md)

### Authorization

[DjangoRestToken](../README.md#DjangoRestToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |
| **0** | error payload |  -  |

<a id="testUrlRewritingRules"></a>
# **testUrlRewritingRules**
> URLRewritingRulesSerializer testUrlRewritingRules(username, projectSlug)

Match and replace parts of a URL based on rules passed in POST data

Match and replace parts of a URL based on rules passed in POST data.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.botify.com/v1");
    
    // Configure API key authorization: DjangoRestToken
    ApiKeyAuth DjangoRestToken = (ApiKeyAuth) defaultClient.getAuthentication("DjangoRestToken");
    DjangoRestToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //DjangoRestToken.setApiKeyPrefix("Token");

    ProjectApi apiInstance = new ProjectApi(defaultClient);
    String username = "username_example"; // String | User's identifier
    String projectSlug = "projectSlug_example"; // String | Project's identifier
    try {
      URLRewritingRulesSerializer result = apiInstance.testUrlRewritingRules(username, projectSlug);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectApi#testUrlRewritingRules");
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
| **username** | **String**| User&#39;s identifier | |
| **projectSlug** | **String**| Project&#39;s identifier | |

### Return type

[**URLRewritingRulesSerializer**](URLRewritingRulesSerializer.md)

### Authorization

[DjangoRestToken](../README.md#DjangoRestToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Successful operation |  -  |
| **0** | error payload |  -  |

