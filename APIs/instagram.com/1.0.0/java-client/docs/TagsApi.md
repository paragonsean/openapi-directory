# TagsApi

All URIs are relative to *https://api.instagram.com/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**tagsSearchGet**](TagsApi.md#tagsSearchGet) | **GET** /tags/search | Search for tags by name. |
| [**tagsTagNameGet**](TagsApi.md#tagsTagNameGet) | **GET** /tags/{tag-name} | Get information about a tag object. |
| [**tagsTagNameMediaRecentGet**](TagsApi.md#tagsTagNameMediaRecentGet) | **GET** /tags/{tag-name}/media/recent | Get a list of recently tagged media. |


<a id="tagsSearchGet"></a>
# **tagsSearchGet**
> TagSearchResponse tagsSearchGet(q)

Search for tags by name.

Search for tags by name.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TagsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.instagram.com/v1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: instagram_auth
    OAuth instagram_auth = (OAuth) defaultClient.getAuthentication("instagram_auth");
    instagram_auth.setAccessToken("YOUR ACCESS TOKEN");

    TagsApi apiInstance = new TagsApi(defaultClient);
    String q = "q_example"; // String | A valid tag name without a leading \\#. (eg. snowy, nofilter)
    try {
      TagSearchResponse result = apiInstance.tagsSearchGet(q);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TagsApi#tagsSearchGet");
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
| **q** | **String**| A valid tag name without a leading \\#. (eg. snowy, nofilter) | |

### Return type

[**TagSearchResponse**](TagSearchResponse.md)

### Authorization

[api_key](../README.md#api_key), [instagram_auth](../README.md#instagram_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of found tags and their statistics. |  -  |

<a id="tagsTagNameGet"></a>
# **tagsTagNameGet**
> TagInfoResponse tagsTagNameGet(tagName)

Get information about a tag object.

Get information about a tag object.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TagsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.instagram.com/v1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: instagram_auth
    OAuth instagram_auth = (OAuth) defaultClient.getAuthentication("instagram_auth");
    instagram_auth.setAccessToken("YOUR ACCESS TOKEN");

    TagsApi apiInstance = new TagsApi(defaultClient);
    String tagName = "tagName_example"; // String | The tag name.
    try {
      TagInfoResponse result = apiInstance.tagsTagNameGet(tagName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TagsApi#tagsTagNameGet");
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
| **tagName** | **String**| The tag name. | |

### Return type

[**TagInfoResponse**](TagInfoResponse.md)

### Authorization

[api_key](../README.md#api_key), [instagram_auth](../README.md#instagram_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Tag information response. |  -  |

<a id="tagsTagNameMediaRecentGet"></a>
# **tagsTagNameMediaRecentGet**
> TagMediaListResponse tagsTagNameMediaRecentGet(tagName, count, minTagId, maxTagId)

Get a list of recently tagged media.

Get a list of recently tagged media. Use the &#x60;max_tag_id&#x60; and &#x60;min_tag_id&#x60; parameters in the pagination response to paginate through these objects. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TagsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.instagram.com/v1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: instagram_auth
    OAuth instagram_auth = (OAuth) defaultClient.getAuthentication("instagram_auth");
    instagram_auth.setAccessToken("YOUR ACCESS TOKEN");

    TagsApi apiInstance = new TagsApi(defaultClient);
    String tagName = "tagName_example"; // String | The tag name.
    Integer count = 56; // Integer | Count of tagged media to return.
    String minTagId = "minTagId_example"; // String | Return media before this `min_tag_id`.
    String maxTagId = "maxTagId_example"; // String | Return media after this `max_tag_id`.
    try {
      TagMediaListResponse result = apiInstance.tagsTagNameMediaRecentGet(tagName, count, minTagId, maxTagId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TagsApi#tagsTagNameMediaRecentGet");
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
| **tagName** | **String**| The tag name. | |
| **count** | **Integer**| Count of tagged media to return. | [optional] |
| **minTagId** | **String**| Return media before this &#x60;min_tag_id&#x60;. | [optional] |
| **maxTagId** | **String**| Return media after this &#x60;max_tag_id&#x60;. | [optional] |

### Return type

[**TagMediaListResponse**](TagMediaListResponse.md)

### Authorization

[api_key](../README.md#api_key), [instagram_auth](../README.md#instagram_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of media entries with this tag. |  -  |

