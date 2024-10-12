# ApiV2Api

All URIs are relative to *https://api.zeno.fm*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createPodcast**](ApiV2Api.md#createPodcast) | **POST** /api/v2/podcasts/create |  |
| [**createPodcastEpisode**](ApiV2Api.md#createPodcastEpisode) | **POST** /api/v2/podcasts/{podcastKey}/episodes/create |  |
| [**deletePodcast**](ApiV2Api.md#deletePodcast) | **DELETE** /api/v2/podcasts/{podcastKey} |  |
| [**deletePodcast1**](ApiV2Api.md#deletePodcast1) | **DELETE** /api/v2/podcasts/{podcastKey}/episodes/{episodeKey} |  |
| [**getPartnerAggregatorStations**](ApiV2Api.md#getPartnerAggregatorStations) | **GET** /api/v2/stations/list |  |
| [**getPodcast**](ApiV2Api.md#getPodcast) | **GET** /api/v2/podcasts/{podcastKey} |  |
| [**getPodcastCategories**](ApiV2Api.md#getPodcastCategories) | **GET** /api/v2/podcasts/categories |  |
| [**getPodcastCountries**](ApiV2Api.md#getPodcastCountries) | **GET** /api/v2/podcasts/countries |  |
| [**getPodcastEpisode**](ApiV2Api.md#getPodcastEpisode) | **GET** /api/v2/podcasts/{podcastKey}/episodes/{episodeKey} |  |
| [**getPodcastEpisodes**](ApiV2Api.md#getPodcastEpisodes) | **GET** /api/v2/podcasts/{podcastKey}/episodes |  |
| [**getPodcastLanguages**](ApiV2Api.md#getPodcastLanguages) | **GET** /api/v2/podcasts/languages |  |
| [**getStationCountries**](ApiV2Api.md#getStationCountries) | **GET** /api/v2/stations/countries |  |
| [**getStationGenres**](ApiV2Api.md#getStationGenres) | **GET** /api/v2/stations/genres |  |
| [**getStationLanguages**](ApiV2Api.md#getStationLanguages) | **GET** /api/v2/stations/languages |  |
| [**searchPodcasts**](ApiV2Api.md#searchPodcasts) | **POST** /api/v2/podcasts/search |  |
| [**searchStations**](ApiV2Api.md#searchStations) | **POST** /api/v2/stations/search |  |
| [**updatePodcast**](ApiV2Api.md#updatePodcast) | **PUT** /api/v2/podcasts/{podcastKey} |  |
| [**updatePodcastEpisode**](ApiV2Api.md#updatePodcastEpisode) | **PUT** /api/v2/podcasts/{podcastKey}/episodes/{episodeKey} |  |


<a id="createPodcast"></a>
# **createPodcast**
> Podcast createPodcast(fileLogo, podcast)



Create podcast

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApiV2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.zeno.fm");
    
    // Configure API key authorization: API_Key
    ApiKeyAuth API_Key = (ApiKeyAuth) defaultClient.getAuthentication("API_Key");
    API_Key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //API_Key.setApiKeyPrefix("Token");

    ApiV2Api apiInstance = new ApiV2Api(defaultClient);
    File fileLogo = new File("/path/to/file"); // File | 
    Podcast podcast = new Podcast(); // Podcast | 
    try {
      Podcast result = apiInstance.createPodcast(fileLogo, podcast);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApiV2Api#createPodcast");
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
| **fileLogo** | **File**|  | |
| **podcast** | [**Podcast**](Podcast.md)|  | |

### Return type

[**Podcast**](Podcast.md)

### Authorization

[API_Key](../README.md#API_Key)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="createPodcastEpisode"></a>
# **createPodcastEpisode**
> PodcastEpisode createPodcastEpisode(podcastKey, episode, fileLogo, fileMedia)



Create podcast episode

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApiV2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.zeno.fm");
    
    // Configure API key authorization: API_Key
    ApiKeyAuth API_Key = (ApiKeyAuth) defaultClient.getAuthentication("API_Key");
    API_Key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //API_Key.setApiKeyPrefix("Token");

    ApiV2Api apiInstance = new ApiV2Api(defaultClient);
    String podcastKey = "podcastKey_example"; // String | 
    PodcastEpisode episode = new PodcastEpisode(); // PodcastEpisode | 
    File fileLogo = new File("/path/to/file"); // File | 
    File fileMedia = new File("/path/to/file"); // File | 
    try {
      PodcastEpisode result = apiInstance.createPodcastEpisode(podcastKey, episode, fileLogo, fileMedia);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApiV2Api#createPodcastEpisode");
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
| **podcastKey** | **String**|  | |
| **episode** | [**PodcastEpisode**](PodcastEpisode.md)|  | |
| **fileLogo** | **File**|  | |
| **fileMedia** | **File**|  | |

### Return type

[**PodcastEpisode**](PodcastEpisode.md)

### Authorization

[API_Key](../README.md#API_Key)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="deletePodcast"></a>
# **deletePodcast**
> deletePodcast(podcastKey)



Delete podcast

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApiV2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.zeno.fm");
    
    // Configure API key authorization: API_Key
    ApiKeyAuth API_Key = (ApiKeyAuth) defaultClient.getAuthentication("API_Key");
    API_Key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //API_Key.setApiKeyPrefix("Token");

    ApiV2Api apiInstance = new ApiV2Api(defaultClient);
    String podcastKey = "podcastKey_example"; // String | 
    try {
      apiInstance.deletePodcast(podcastKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApiV2Api#deletePodcast");
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
| **podcastKey** | **String**|  | |

### Return type

null (empty response body)

### Authorization

[API_Key](../README.md#API_Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="deletePodcast1"></a>
# **deletePodcast1**
> deletePodcast1(podcastKey, episodeKey)



Delete podcast episode

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApiV2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.zeno.fm");
    
    // Configure API key authorization: API_Key
    ApiKeyAuth API_Key = (ApiKeyAuth) defaultClient.getAuthentication("API_Key");
    API_Key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //API_Key.setApiKeyPrefix("Token");

    ApiV2Api apiInstance = new ApiV2Api(defaultClient);
    String podcastKey = "podcastKey_example"; // String | 
    String episodeKey = "episodeKey_example"; // String | 
    try {
      apiInstance.deletePodcast1(podcastKey, episodeKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApiV2Api#deletePodcast1");
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
| **podcastKey** | **String**|  | |
| **episodeKey** | **String**|  | |

### Return type

null (empty response body)

### Authorization

[API_Key](../README.md#API_Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="getPartnerAggregatorStations"></a>
# **getPartnerAggregatorStations**
> StationList getPartnerAggregatorStations(page, hitsPerPage)



List stations

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApiV2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.zeno.fm");
    
    // Configure API key authorization: API_Key
    ApiKeyAuth API_Key = (ApiKeyAuth) defaultClient.getAuthentication("API_Key");
    API_Key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //API_Key.setApiKeyPrefix("Token");

    ApiV2Api apiInstance = new ApiV2Api(defaultClient);
    String page = "1"; // String | 
    String hitsPerPage = "10"; // String | 
    try {
      StationList result = apiInstance.getPartnerAggregatorStations(page, hitsPerPage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApiV2Api#getPartnerAggregatorStations");
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
| **page** | **String**|  | [optional] [default to 1] |
| **hitsPerPage** | **String**|  | [optional] [default to 10] |

### Return type

[**StationList**](StationList.md)

### Authorization

[API_Key](../README.md#API_Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="getPodcast"></a>
# **getPodcast**
> Podcast getPodcast(podcastKey)



Get podcast

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApiV2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.zeno.fm");
    
    // Configure API key authorization: API_Key
    ApiKeyAuth API_Key = (ApiKeyAuth) defaultClient.getAuthentication("API_Key");
    API_Key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //API_Key.setApiKeyPrefix("Token");

    ApiV2Api apiInstance = new ApiV2Api(defaultClient);
    String podcastKey = "podcastKey_example"; // String | 
    try {
      Podcast result = apiInstance.getPodcast(podcastKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApiV2Api#getPodcast");
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
| **podcastKey** | **String**|  | |

### Return type

[**Podcast**](Podcast.md)

### Authorization

[API_Key](../README.md#API_Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="getPodcastCategories"></a>
# **getPodcastCategories**
> List&lt;PodcastCategory&gt; getPodcastCategories()



Get the list of Categories that can be used to filter podcasts in the search podcasts request

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApiV2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.zeno.fm");
    
    // Configure API key authorization: API_Key
    ApiKeyAuth API_Key = (ApiKeyAuth) defaultClient.getAuthentication("API_Key");
    API_Key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //API_Key.setApiKeyPrefix("Token");

    ApiV2Api apiInstance = new ApiV2Api(defaultClient);
    try {
      List<PodcastCategory> result = apiInstance.getPodcastCategories();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApiV2Api#getPodcastCategories");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**List&lt;PodcastCategory&gt;**](PodcastCategory.md)

### Authorization

[API_Key](../README.md#API_Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="getPodcastCountries"></a>
# **getPodcastCountries**
> List&lt;Country&gt; getPodcastCountries()



Get the list of Countries that can be used to filter podcasts in the search podcasts request

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApiV2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.zeno.fm");
    
    // Configure API key authorization: API_Key
    ApiKeyAuth API_Key = (ApiKeyAuth) defaultClient.getAuthentication("API_Key");
    API_Key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //API_Key.setApiKeyPrefix("Token");

    ApiV2Api apiInstance = new ApiV2Api(defaultClient);
    try {
      List<Country> result = apiInstance.getPodcastCountries();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApiV2Api#getPodcastCountries");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**List&lt;Country&gt;**](Country.md)

### Authorization

[API_Key](../README.md#API_Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="getPodcastEpisode"></a>
# **getPodcastEpisode**
> PodcastEpisode getPodcastEpisode(podcastKey, episodeKey)



Get podcast episode

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApiV2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.zeno.fm");
    
    // Configure API key authorization: API_Key
    ApiKeyAuth API_Key = (ApiKeyAuth) defaultClient.getAuthentication("API_Key");
    API_Key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //API_Key.setApiKeyPrefix("Token");

    ApiV2Api apiInstance = new ApiV2Api(defaultClient);
    String podcastKey = "podcastKey_example"; // String | 
    String episodeKey = "episodeKey_example"; // String | 
    try {
      PodcastEpisode result = apiInstance.getPodcastEpisode(podcastKey, episodeKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApiV2Api#getPodcastEpisode");
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
| **podcastKey** | **String**|  | |
| **episodeKey** | **String**|  | |

### Return type

[**PodcastEpisode**](PodcastEpisode.md)

### Authorization

[API_Key](../README.md#API_Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="getPodcastEpisodes"></a>
# **getPodcastEpisodes**
> PodcastEpisodeList getPodcastEpisodes(podcastKey, limit, offset)



Get podcast episodes

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApiV2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.zeno.fm");
    
    // Configure API key authorization: API_Key
    ApiKeyAuth API_Key = (ApiKeyAuth) defaultClient.getAuthentication("API_Key");
    API_Key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //API_Key.setApiKeyPrefix("Token");

    ApiV2Api apiInstance = new ApiV2Api(defaultClient);
    String podcastKey = "podcastKey_example"; // String | 
    String limit = "10"; // String | 
    String offset = "0"; // String | 
    try {
      PodcastEpisodeList result = apiInstance.getPodcastEpisodes(podcastKey, limit, offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApiV2Api#getPodcastEpisodes");
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
| **podcastKey** | **String**|  | |
| **limit** | **String**|  | [optional] [default to 10] |
| **offset** | **String**|  | [optional] [default to 0] |

### Return type

[**PodcastEpisodeList**](PodcastEpisodeList.md)

### Authorization

[API_Key](../README.md#API_Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="getPodcastLanguages"></a>
# **getPodcastLanguages**
> List&lt;Language&gt; getPodcastLanguages()



Get the list of Languages that can be used to filter podcasts in the search podcasts request

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApiV2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.zeno.fm");
    
    // Configure API key authorization: API_Key
    ApiKeyAuth API_Key = (ApiKeyAuth) defaultClient.getAuthentication("API_Key");
    API_Key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //API_Key.setApiKeyPrefix("Token");

    ApiV2Api apiInstance = new ApiV2Api(defaultClient);
    try {
      List<Language> result = apiInstance.getPodcastLanguages();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApiV2Api#getPodcastLanguages");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**List&lt;Language&gt;**](Language.md)

### Authorization

[API_Key](../README.md#API_Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="getStationCountries"></a>
# **getStationCountries**
> List&lt;Country&gt; getStationCountries()



Get the list of Countries that can be used to filter stations in the search stations request

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApiV2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.zeno.fm");
    
    // Configure API key authorization: API_Key
    ApiKeyAuth API_Key = (ApiKeyAuth) defaultClient.getAuthentication("API_Key");
    API_Key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //API_Key.setApiKeyPrefix("Token");

    ApiV2Api apiInstance = new ApiV2Api(defaultClient);
    try {
      List<Country> result = apiInstance.getStationCountries();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApiV2Api#getStationCountries");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**List&lt;Country&gt;**](Country.md)

### Authorization

[API_Key](../README.md#API_Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="getStationGenres"></a>
# **getStationGenres**
> List&lt;StationGenre&gt; getStationGenres()



Get the list of Genres that can be used to filter stations in the search stations request

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApiV2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.zeno.fm");
    
    // Configure API key authorization: API_Key
    ApiKeyAuth API_Key = (ApiKeyAuth) defaultClient.getAuthentication("API_Key");
    API_Key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //API_Key.setApiKeyPrefix("Token");

    ApiV2Api apiInstance = new ApiV2Api(defaultClient);
    try {
      List<StationGenre> result = apiInstance.getStationGenres();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApiV2Api#getStationGenres");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**List&lt;StationGenre&gt;**](StationGenre.md)

### Authorization

[API_Key](../README.md#API_Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="getStationLanguages"></a>
# **getStationLanguages**
> List&lt;Language&gt; getStationLanguages()



Get the list of Languages that can be used to filter stations in the search stations request

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApiV2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.zeno.fm");
    
    // Configure API key authorization: API_Key
    ApiKeyAuth API_Key = (ApiKeyAuth) defaultClient.getAuthentication("API_Key");
    API_Key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //API_Key.setApiKeyPrefix("Token");

    ApiV2Api apiInstance = new ApiV2Api(defaultClient);
    try {
      List<Language> result = apiInstance.getStationLanguages();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApiV2Api#getStationLanguages");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**List&lt;Language&gt;**](Language.md)

### Authorization

[API_Key](../README.md#API_Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="searchPodcasts"></a>
# **searchPodcasts**
> PodcastSearchResults searchPodcasts(podcastSearchParams)



Search podcasts

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApiV2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.zeno.fm");
    
    // Configure API key authorization: API_Key
    ApiKeyAuth API_Key = (ApiKeyAuth) defaultClient.getAuthentication("API_Key");
    API_Key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //API_Key.setApiKeyPrefix("Token");

    ApiV2Api apiInstance = new ApiV2Api(defaultClient);
    PodcastSearchParams podcastSearchParams = new PodcastSearchParams(); // PodcastSearchParams | 
    try {
      PodcastSearchResults result = apiInstance.searchPodcasts(podcastSearchParams);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApiV2Api#searchPodcasts");
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
| **podcastSearchParams** | [**PodcastSearchParams**](PodcastSearchParams.md)|  | |

### Return type

[**PodcastSearchResults**](PodcastSearchResults.md)

### Authorization

[API_Key](../README.md#API_Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="searchStations"></a>
# **searchStations**
> StationSearchResults searchStations(stationSearchParams)



Search stations

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApiV2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.zeno.fm");
    
    // Configure API key authorization: API_Key
    ApiKeyAuth API_Key = (ApiKeyAuth) defaultClient.getAuthentication("API_Key");
    API_Key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //API_Key.setApiKeyPrefix("Token");

    ApiV2Api apiInstance = new ApiV2Api(defaultClient);
    StationSearchParams stationSearchParams = new StationSearchParams(); // StationSearchParams | 
    try {
      StationSearchResults result = apiInstance.searchStations(stationSearchParams);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApiV2Api#searchStations");
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
| **stationSearchParams** | [**StationSearchParams**](StationSearchParams.md)|  | |

### Return type

[**StationSearchResults**](StationSearchResults.md)

### Authorization

[API_Key](../README.md#API_Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="updatePodcast"></a>
# **updatePodcast**
> Podcast updatePodcast(podcastKey, podcast, fileLogo)



Update podcast

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApiV2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.zeno.fm");
    
    // Configure API key authorization: API_Key
    ApiKeyAuth API_Key = (ApiKeyAuth) defaultClient.getAuthentication("API_Key");
    API_Key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //API_Key.setApiKeyPrefix("Token");

    ApiV2Api apiInstance = new ApiV2Api(defaultClient);
    String podcastKey = "podcastKey_example"; // String | 
    Podcast podcast = new Podcast(); // Podcast | 
    File fileLogo = new File("/path/to/file"); // File | 
    try {
      Podcast result = apiInstance.updatePodcast(podcastKey, podcast, fileLogo);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApiV2Api#updatePodcast");
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
| **podcastKey** | **String**|  | |
| **podcast** | [**Podcast**](Podcast.md)|  | |
| **fileLogo** | **File**|  | [optional] |

### Return type

[**Podcast**](Podcast.md)

### Authorization

[API_Key](../README.md#API_Key)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="updatePodcastEpisode"></a>
# **updatePodcastEpisode**
> PodcastEpisode updatePodcastEpisode(podcastKey, episodeKey, episode, fileLogo)



Update podcast episode

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApiV2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.zeno.fm");
    
    // Configure API key authorization: API_Key
    ApiKeyAuth API_Key = (ApiKeyAuth) defaultClient.getAuthentication("API_Key");
    API_Key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //API_Key.setApiKeyPrefix("Token");

    ApiV2Api apiInstance = new ApiV2Api(defaultClient);
    String podcastKey = "podcastKey_example"; // String | 
    String episodeKey = "episodeKey_example"; // String | 
    PodcastEpisode episode = new PodcastEpisode(); // PodcastEpisode | 
    File fileLogo = new File("/path/to/file"); // File | 
    try {
      PodcastEpisode result = apiInstance.updatePodcastEpisode(podcastKey, episodeKey, episode, fileLogo);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApiV2Api#updatePodcastEpisode");
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
| **podcastKey** | **String**|  | |
| **episodeKey** | **String**|  | |
| **episode** | [**PodcastEpisode**](PodcastEpisode.md)|  | |
| **fileLogo** | **File**|  | [optional] |

### Return type

[**PodcastEpisode**](PodcastEpisode.md)

### Authorization

[API_Key](../README.md#API_Key)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

