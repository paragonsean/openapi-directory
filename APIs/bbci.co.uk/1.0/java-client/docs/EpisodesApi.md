# EpisodesApi

All URIs are relative to *https://ibl.api.bbci.co.uk/ibl/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getClips**](EpisodesApi.md#getClips) | **GET** /clips/{pid} | Get Clips |
| [**getEpisodesByCategory**](EpisodesApi.md#getEpisodesByCategory) | **GET** /categories/{category}/episodes | List all the episodes for a category. |
| [**getEpisodesByGroup**](EpisodesApi.md#getEpisodesByGroup) | **GET** /groups/{pid}/episodes | Get episodes by group, brand or series |
| [**getEpisodesByParentPID**](EpisodesApi.md#getEpisodesByParentPID) | **GET** /programmes/{pid}/episodes | Child episodes for a given programme pid. |
| [**getOnwardJourney**](EpisodesApi.md#getOnwardJourney) | **GET** /episodes/{pid}/next | Get Onward Journey |
| [**getPostRolls**](EpisodesApi.md#getPostRolls) | **GET** /episodes/{pid}/postrolls | Get Follow-ups (post-rolls) |
| [**getProgrammeByPID**](EpisodesApi.md#getProgrammeByPID) | **GET** /episodes/{pid} | Episode for a given pid. |
| [**getProgrammeRecommendations**](EpisodesApi.md#getProgrammeRecommendations) | **GET** /episodes/{pid}/recommendations | Get programme recommendations |
| [**getProgrammesPopular**](EpisodesApi.md#getProgrammesPopular) | **GET** /groups/popular/episodes | Get programmes popular |
| [**getTrailersPreRolls**](EpisodesApi.md#getTrailersPreRolls) | **GET** /episodes/{pid}/prerolls | Get Trailers (pre-rolls) |


<a id="getClips"></a>
# **getClips**
> Object getClips(pid, rights, availability)

Get Clips

Get Clips

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EpisodesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ibl.api.bbci.co.uk/ibl/v1");

    EpisodesApi apiInstance = new EpisodesApi(defaultClient);
    String pid = "pid_example"; // String | The programme identifier.
    String rights = "mobile"; // String | The rights group to limit results to.
    String availability = "all"; // String | Whether to return all, or available programmes
    try {
      Object result = apiInstance.getClips(pid, rights, availability);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EpisodesApi#getClips");
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
| **pid** | **String**| The programme identifier. | |
| **rights** | **String**| The rights group to limit results to. | [default to web] [enum: mobile, tv, web] |
| **availability** | **String**| Whether to return all, or available programmes | [default to available] [enum: all, available] |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Default response |  -  |

<a id="getEpisodesByCategory"></a>
# **getEpisodesByCategory**
> Object getEpisodesByCategory(category, lang, rights, availability, page, perPage, sort)

List all the episodes for a category.

Get the list of all the episodes for a given category in TV &amp; iPlayer.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EpisodesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ibl.api.bbci.co.uk/ibl/v1");

    EpisodesApi apiInstance = new EpisodesApi(defaultClient);
    String category = "category_example"; // String | The category identifier to return results from.
    String lang = "en"; // String | The language for any applicable localised strings.
    String rights = "mobile"; // String | The rights group to limit results to.
    String availability = "all"; // String | Whether to return all, or available programmes
    Long page = 56L; // Long | The page index.
    Long perPage = 56L; // Long | The number of results to return.
    String sort = "recent"; // String | The sort order of the results.
    try {
      Object result = apiInstance.getEpisodesByCategory(category, lang, rights, availability, page, perPage, sort);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EpisodesApi#getEpisodesByCategory");
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
| **category** | **String**| The category identifier to return results from. | |
| **lang** | **String**| The language for any applicable localised strings. | [enum: en, cy, ga, gd, pi] |
| **rights** | **String**| The rights group to limit results to. | [default to web] [enum: mobile, tv, web] |
| **availability** | **String**| Whether to return all, or available programmes | [default to available] [enum: all, available] |
| **page** | **Long**| The page index. | |
| **perPage** | **Long**| The number of results to return. | |
| **sort** | **String**| The sort order of the results. | [optional] [enum: recent, popular] |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Default response |  -  |

<a id="getEpisodesByGroup"></a>
# **getEpisodesByGroup**
> Object getEpisodesByGroup(pid, rights, page, perPage, initialChildCount, sort, sortDirection, availability, mixin)

Get episodes by group, brand or series

Get episodes by group, brand or series

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EpisodesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ibl.api.bbci.co.uk/ibl/v1");

    EpisodesApi apiInstance = new EpisodesApi(defaultClient);
    String pid = "pid_example"; // String | The programme identifier.
    String rights = "mobile"; // String | The rights group to limit results to.
    Long page = 56L; // Long | The page index.
    Long perPage = 56L; // Long | The number of results to return.
    Integer initialChildCount = 4; // Integer | The depth to return child entities.
    String sort = "sort_example"; // String | The sort order of the results.
    String sortDirection = "asc"; // String | Whether to sort ascending or descending
    String availability = "all"; // String | Whether to return all, or available programmes
    List<String> mixin = Arrays.asList(); // List<String> | Request additional data in the output
    try {
      Object result = apiInstance.getEpisodesByGroup(pid, rights, page, perPage, initialChildCount, sort, sortDirection, availability, mixin);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EpisodesApi#getEpisodesByGroup");
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
| **pid** | **String**| The programme identifier. | |
| **rights** | **String**| The rights group to limit results to. | [default to web] [enum: mobile, tv, web] |
| **page** | **Long**| The page index. | |
| **perPage** | **Long**| The number of results to return. | |
| **initialChildCount** | **Integer**| The depth to return child entities. | [default to 4] |
| **sort** | **String**| The sort order of the results. | |
| **sortDirection** | **String**| Whether to sort ascending or descending | [enum: asc, desc] |
| **availability** | **String**| Whether to return all, or available programmes | [default to available] [enum: all, available] |
| **mixin** | [**List&lt;String&gt;**](String.md)| Request additional data in the output | [optional] [enum: live, promotions] |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Default response |  -  |

<a id="getEpisodesByParentPID"></a>
# **getEpisodesByParentPID**
> Object getEpisodesByParentPID(pid, rights, availability, initialChildCount)

Child episodes for a given programme pid.

Get the child episodes belonging to a given programme identifier.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EpisodesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ibl.api.bbci.co.uk/ibl/v1");

    EpisodesApi apiInstance = new EpisodesApi(defaultClient);
    String pid = "pid_example"; // String | The programme identifier.
    String rights = "mobile"; // String | The rights group to limit results to.
    String availability = "all"; // String | Whether to return all, or available programmes
    Integer initialChildCount = 4; // Integer | The depth to return child entities.
    try {
      Object result = apiInstance.getEpisodesByParentPID(pid, rights, availability, initialChildCount);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EpisodesApi#getEpisodesByParentPID");
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
| **pid** | **String**| The programme identifier. | |
| **rights** | **String**| The rights group to limit results to. | [default to web] [enum: mobile, tv, web] |
| **availability** | **String**| Whether to return all, or available programmes | [default to available] [enum: all, available] |
| **initialChildCount** | **Integer**| The depth to return child entities. | [default to 4] |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Default response |  -  |

<a id="getOnwardJourney"></a>
# **getOnwardJourney**
> Object getOnwardJourney(pid, rights, availability)

Get Onward Journey

Get Onward Journey (next programme)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EpisodesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ibl.api.bbci.co.uk/ibl/v1");

    EpisodesApi apiInstance = new EpisodesApi(defaultClient);
    String pid = "pid_example"; // String | The programme identifier.
    String rights = "mobile"; // String | The rights group to limit results to.
    String availability = "all"; // String | Whether to return all, or available programmes
    try {
      Object result = apiInstance.getOnwardJourney(pid, rights, availability);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EpisodesApi#getOnwardJourney");
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
| **pid** | **String**| The programme identifier. | |
| **rights** | **String**| The rights group to limit results to. | [default to web] [enum: mobile, tv, web] |
| **availability** | **String**| Whether to return all, or available programmes | [default to available] [enum: all, available] |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Default response |  -  |

<a id="getPostRolls"></a>
# **getPostRolls**
> Object getPostRolls(pid, rights, availability)

Get Follow-ups (post-rolls)

Get Follow-ups (post-rolls)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EpisodesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ibl.api.bbci.co.uk/ibl/v1");

    EpisodesApi apiInstance = new EpisodesApi(defaultClient);
    String pid = "pid_example"; // String | The programme identifier.
    String rights = "mobile"; // String | The rights group to limit results to.
    String availability = "all"; // String | Whether to return all, or available programmes
    try {
      Object result = apiInstance.getPostRolls(pid, rights, availability);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EpisodesApi#getPostRolls");
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
| **pid** | **String**| The programme identifier. | |
| **rights** | **String**| The rights group to limit results to. | [default to web] [enum: mobile, tv, web] |
| **availability** | **String**| Whether to return all, or available programmes | [default to available] [enum: all, available] |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Default response |  -  |

<a id="getProgrammeByPID"></a>
# **getProgrammeByPID**
> Object getProgrammeByPID(pid, rights, availability, mixin)

Episode for a given pid.

Get the episode for a given episode identifier.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EpisodesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ibl.api.bbci.co.uk/ibl/v1");

    EpisodesApi apiInstance = new EpisodesApi(defaultClient);
    String pid = "pid_example"; // String | The programme identifier.
    String rights = "mobile"; // String | The rights group to limit results to.
    String availability = "all"; // String | Whether to return all, or available programmes
    List<String> mixin = Arrays.asList(); // List<String> | Request additional data in the output
    try {
      Object result = apiInstance.getProgrammeByPID(pid, rights, availability, mixin);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EpisodesApi#getProgrammeByPID");
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
| **pid** | **String**| The programme identifier. | |
| **rights** | **String**| The rights group to limit results to. | [default to web] [enum: mobile, tv, web] |
| **availability** | **String**| Whether to return all, or available programmes | [default to available] [enum: all, available] |
| **mixin** | [**List&lt;String&gt;**](String.md)| Request additional data in the output | [optional] [enum: live, promotions] |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Default response |  -  |

<a id="getProgrammeRecommendations"></a>
# **getProgrammeRecommendations**
> Object getProgrammeRecommendations(pid, rights, availability, page, perPage)

Get programme recommendations

Get programme recommendations

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EpisodesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ibl.api.bbci.co.uk/ibl/v1");

    EpisodesApi apiInstance = new EpisodesApi(defaultClient);
    String pid = "pid_example"; // String | The programme identifier.
    String rights = "mobile"; // String | The rights group to limit results to.
    String availability = "all"; // String | Whether to return all, or available programmes
    Long page = 56L; // Long | The page index.
    Long perPage = 56L; // Long | The number of results to return.
    try {
      Object result = apiInstance.getProgrammeRecommendations(pid, rights, availability, page, perPage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EpisodesApi#getProgrammeRecommendations");
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
| **pid** | **String**| The programme identifier. | |
| **rights** | **String**| The rights group to limit results to. | [default to web] [enum: mobile, tv, web] |
| **availability** | **String**| Whether to return all, or available programmes | [default to available] [enum: all, available] |
| **page** | **Long**| The page index. | |
| **perPage** | **Long**| The number of results to return. | |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Default response |  -  |

<a id="getProgrammesPopular"></a>
# **getProgrammesPopular**
> Object getProgrammesPopular(rights, page, perPage, initialChildCount, sort, sortDirection, availability, mixin)

Get programmes popular

Get programmes popular

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EpisodesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ibl.api.bbci.co.uk/ibl/v1");

    EpisodesApi apiInstance = new EpisodesApi(defaultClient);
    String rights = "mobile"; // String | The rights group to limit results to.
    Long page = 56L; // Long | The page index.
    Long perPage = 56L; // Long | The number of results to return.
    Integer initialChildCount = 4; // Integer | The depth to return child entities.
    String sort = "sort_example"; // String | The sort order of the results.
    String sortDirection = "asc"; // String | Whether to sort ascending or descending
    String availability = "all"; // String | Whether to return all, or available programmes
    List<String> mixin = Arrays.asList(); // List<String> | Request additional data in the output
    try {
      Object result = apiInstance.getProgrammesPopular(rights, page, perPage, initialChildCount, sort, sortDirection, availability, mixin);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EpisodesApi#getProgrammesPopular");
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
| **rights** | **String**| The rights group to limit results to. | [default to web] [enum: mobile, tv, web] |
| **page** | **Long**| The page index. | |
| **perPage** | **Long**| The number of results to return. | |
| **initialChildCount** | **Integer**| The depth to return child entities. | [default to 4] |
| **sort** | **String**| The sort order of the results. | |
| **sortDirection** | **String**| Whether to sort ascending or descending | [enum: asc, desc] |
| **availability** | **String**| Whether to return all, or available programmes | [default to available] [enum: all, available] |
| **mixin** | [**List&lt;String&gt;**](String.md)| Request additional data in the output | [optional] [enum: live, promotions] |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Default response |  -  |

<a id="getTrailersPreRolls"></a>
# **getTrailersPreRolls**
> Object getTrailersPreRolls(pid, rights, availability)

Get Trailers (pre-rolls)

Get Trailers (pre-rolls)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EpisodesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ibl.api.bbci.co.uk/ibl/v1");

    EpisodesApi apiInstance = new EpisodesApi(defaultClient);
    String pid = "pid_example"; // String | The programme identifier.
    String rights = "mobile"; // String | The rights group to limit results to.
    String availability = "all"; // String | Whether to return all, or available programmes
    try {
      Object result = apiInstance.getTrailersPreRolls(pid, rights, availability);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EpisodesApi#getTrailersPreRolls");
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
| **pid** | **String**| The programme identifier. | |
| **rights** | **String**| The rights group to limit results to. | [default to web] [enum: mobile, tv, web] |
| **availability** | **String**| Whether to return all, or available programmes | [default to available] [enum: all, available] |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Default response |  -  |

