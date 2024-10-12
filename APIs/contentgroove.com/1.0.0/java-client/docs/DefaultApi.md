# DefaultApi

All URIs are relative to *https://api.contentgroove.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createClip**](DefaultApi.md#createClip) | **POST** /clips | create clip |
| [**createMedia**](DefaultApi.md#createMedia) | **POST** /medias | create media |
| [**createWebhookSubscription**](DefaultApi.md#createWebhookSubscription) | **POST** /webhook_subscriptions | create webhook subscription |
| [**deleteClipById**](DefaultApi.md#deleteClipById) | **DELETE** /clips/{id} | delete clip |
| [**deleteMediaById**](DefaultApi.md#deleteMediaById) | **DELETE** /medias/{id} | delete media |
| [**deleteWebhookSubscriptionById**](DefaultApi.md#deleteWebhookSubscriptionById) | **DELETE** /webhook_subscriptions/{id} | delete webhook subscription |
| [**getClipById**](DefaultApi.md#getClipById) | **GET** /clips/{id} | show clip |
| [**getClips**](DefaultApi.md#getClips) | **GET** /clips | list clips |
| [**getMediaById**](DefaultApi.md#getMediaById) | **GET** /medias/{id} | show media |
| [**getMedias**](DefaultApi.md#getMedias) | **GET** /medias | list medias |
| [**getUploadUrl**](DefaultApi.md#getUploadUrl) | **GET** /direct_uploads | prepare presigned upload url |
| [**getWebhookSubscriptionById**](DefaultApi.md#getWebhookSubscriptionById) | **GET** /webhook_subscriptions/{id} | show webhook subscription |
| [**getWebhookSubscriptions**](DefaultApi.md#getWebhookSubscriptions) | **GET** /webhook_subscriptions | list webhook subscriptions |
| [**updateClipById**](DefaultApi.md#updateClipById) | **PUT** /clips/{id} | update clip |
| [**updateMediaById**](DefaultApi.md#updateMediaById) | **PUT** /medias/{id} | update media |


<a id="createClip"></a>
# **createClip**
> ClipResponseObject createClip(createClipRequest)

create clip

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
    defaultClient.setBasePath("https://api.contentgroove.com/api/v1");
    
    // Configure API key authorization: BearerHeader
    ApiKeyAuth BearerHeader = (ApiKeyAuth) defaultClient.getAuthentication("BearerHeader");
    BearerHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //BearerHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    CreateClipRequest createClipRequest = new CreateClipRequest(); // CreateClipRequest | 
    try {
      ClipResponseObject result = apiInstance.createClip(createClipRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#createClip");
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
| **createClipRequest** | [**CreateClipRequest**](CreateClipRequest.md)|  | |

### Return type

[**ClipResponseObject**](ClipResponseObject.md)

### Authorization

[BearerHeader](../README.md#BearerHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful |  -  |
| **401** | unauthorized |  -  |
| **402** | payment required |  -  |
| **429** | too many requests |  -  |

<a id="createMedia"></a>
# **createMedia**
> MediaResponseObject createMedia(createMediaRequest)

create media

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
    defaultClient.setBasePath("https://api.contentgroove.com/api/v1");
    
    // Configure API key authorization: BearerHeader
    ApiKeyAuth BearerHeader = (ApiKeyAuth) defaultClient.getAuthentication("BearerHeader");
    BearerHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //BearerHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    CreateMediaRequest createMediaRequest = new CreateMediaRequest(); // CreateMediaRequest | 
    try {
      MediaResponseObject result = apiInstance.createMedia(createMediaRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#createMedia");
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
| **createMediaRequest** | [**CreateMediaRequest**](CreateMediaRequest.md)|  | |

### Return type

[**MediaResponseObject**](MediaResponseObject.md)

### Authorization

[BearerHeader](../README.md#BearerHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful |  -  |
| **401** | unauthorized |  -  |
| **402** | payment required |  -  |
| **429** | too many requests |  -  |

<a id="createWebhookSubscription"></a>
# **createWebhookSubscription**
> WebhookSubscriptionResponseObject createWebhookSubscription(createWebhookSubscriptionRequest)

create webhook subscription

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
    defaultClient.setBasePath("https://api.contentgroove.com/api/v1");
    
    // Configure API key authorization: BearerHeader
    ApiKeyAuth BearerHeader = (ApiKeyAuth) defaultClient.getAuthentication("BearerHeader");
    BearerHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //BearerHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    CreateWebhookSubscriptionRequest createWebhookSubscriptionRequest = new CreateWebhookSubscriptionRequest(); // CreateWebhookSubscriptionRequest | 
    try {
      WebhookSubscriptionResponseObject result = apiInstance.createWebhookSubscription(createWebhookSubscriptionRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#createWebhookSubscription");
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
| **createWebhookSubscriptionRequest** | [**CreateWebhookSubscriptionRequest**](CreateWebhookSubscriptionRequest.md)|  | |

### Return type

[**WebhookSubscriptionResponseObject**](WebhookSubscriptionResponseObject.md)

### Authorization

[BearerHeader](../README.md#BearerHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful |  -  |
| **401** | unauthorized |  -  |
| **429** | too many requests |  -  |

<a id="deleteClipById"></a>
# **deleteClipById**
> deleteClipById(id)

delete clip

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
    defaultClient.setBasePath("https://api.contentgroove.com/api/v1");
    
    // Configure API key authorization: BearerHeader
    ApiKeyAuth BearerHeader = (ApiKeyAuth) defaultClient.getAuthentication("BearerHeader");
    BearerHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //BearerHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | The id of the clip to be retrieved
    try {
      apiInstance.deleteClipById(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deleteClipById");
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
| **id** | **String**| The id of the clip to be retrieved | |

### Return type

null (empty response body)

### Authorization

[BearerHeader](../README.md#BearerHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | no content |  -  |
| **401** | not authorized |  -  |
| **404** | not found |  -  |
| **429** | too many requests |  -  |

<a id="deleteMediaById"></a>
# **deleteMediaById**
> deleteMediaById(id)

delete media

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
    defaultClient.setBasePath("https://api.contentgroove.com/api/v1");
    
    // Configure API key authorization: BearerHeader
    ApiKeyAuth BearerHeader = (ApiKeyAuth) defaultClient.getAuthentication("BearerHeader");
    BearerHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //BearerHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | id
    try {
      apiInstance.deleteMediaById(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deleteMediaById");
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
| **id** | **String**| id | |

### Return type

null (empty response body)

### Authorization

[BearerHeader](../README.md#BearerHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | no content |  -  |
| **401** | not authorized |  -  |
| **404** | not found |  -  |
| **429** | too many requests |  -  |

<a id="deleteWebhookSubscriptionById"></a>
# **deleteWebhookSubscriptionById**
> deleteWebhookSubscriptionById(id)

delete webhook subscription

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
    defaultClient.setBasePath("https://api.contentgroove.com/api/v1");
    
    // Configure API key authorization: BearerHeader
    ApiKeyAuth BearerHeader = (ApiKeyAuth) defaultClient.getAuthentication("BearerHeader");
    BearerHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //BearerHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | The id of the webhook subscription to be retrieved
    try {
      apiInstance.deleteWebhookSubscriptionById(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deleteWebhookSubscriptionById");
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
| **id** | **String**| The id of the webhook subscription to be retrieved | |

### Return type

null (empty response body)

### Authorization

[BearerHeader](../README.md#BearerHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | no content |  -  |
| **401** | not authorized |  -  |
| **404** | not found |  -  |
| **429** | too many requests |  -  |

<a id="getClipById"></a>
# **getClipById**
> ClipResponseObject getClipById(id)

show clip

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
    defaultClient.setBasePath("https://api.contentgroove.com/api/v1");
    
    // Configure API key authorization: BearerHeader
    ApiKeyAuth BearerHeader = (ApiKeyAuth) defaultClient.getAuthentication("BearerHeader");
    BearerHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //BearerHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | The id of the clip to be retrieved
    try {
      ClipResponseObject result = apiInstance.getClipById(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getClipById");
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
| **id** | **String**| The id of the clip to be retrieved | |

### Return type

[**ClipResponseObject**](ClipResponseObject.md)

### Authorization

[BearerHeader](../README.md#BearerHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful |  -  |
| **401** | not authorized |  -  |
| **404** | not found |  -  |
| **429** | too many requests |  -  |

<a id="getClips"></a>
# **getClips**
> ClipsResponseObject getClips(filter, page, sort)

list clips

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
    defaultClient.setBasePath("https://api.contentgroove.com/api/v1");
    
    // Configure API key authorization: BearerHeader
    ApiKeyAuth BearerHeader = (ApiKeyAuth) defaultClient.getAuthentication("BearerHeader");
    BearerHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //BearerHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Object filter = new HashMap(); // Object | Filters to be applied to the query.  Query params in the url must look like this: \"filter[attributeName_*matcher*]\"  (i.e. filter[name_eq]=chimp%20into%20space)  Available matchers can be found here: https://activerecord-hackery.github.io/ransack/getting-started/search-matches/  
    Object page = new HashMap(); // Object | Specify page number and page size for the query
    String sort = "created_at"; // String | Sorting to be applied to the query. For more info: https://jsonapi.org/format/#fetching-sorting
    try {
      ClipsResponseObject result = apiInstance.getClips(filter, page, sort);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getClips");
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
| **filter** | [**Object**](.md)| Filters to be applied to the query.  Query params in the url must look like this: \&quot;filter[attributeName_*matcher*]\&quot;  (i.e. filter[name_eq]&#x3D;chimp%20into%20space)  Available matchers can be found here: https://activerecord-hackery.github.io/ransack/getting-started/search-matches/   | [optional] |
| **page** | [**Object**](.md)| Specify page number and page size for the query | [optional] |
| **sort** | **String**| Sorting to be applied to the query. For more info: https://jsonapi.org/format/#fetching-sorting | [optional] [enum: created_at, -created_at, original_created_at, -original_created_at, name, -name] |

### Return type

[**ClipsResponseObject**](ClipsResponseObject.md)

### Authorization

[BearerHeader](../README.md#BearerHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful |  -  |
| **401** | unauthorized |  -  |
| **429** | too many requests |  -  |

<a id="getMediaById"></a>
# **getMediaById**
> MediaResponseObject getMediaById(id)

show media

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
    defaultClient.setBasePath("https://api.contentgroove.com/api/v1");
    
    // Configure API key authorization: BearerHeader
    ApiKeyAuth BearerHeader = (ApiKeyAuth) defaultClient.getAuthentication("BearerHeader");
    BearerHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //BearerHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | id
    try {
      MediaResponseObject result = apiInstance.getMediaById(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getMediaById");
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
| **id** | **String**| id | |

### Return type

[**MediaResponseObject**](MediaResponseObject.md)

### Authorization

[BearerHeader](../README.md#BearerHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful |  -  |
| **401** | not authorized |  -  |
| **404** | not found |  -  |
| **429** | too many requests |  -  |

<a id="getMedias"></a>
# **getMedias**
> MediasResponseObject getMedias(filter, page, sort)

list medias

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
    defaultClient.setBasePath("https://api.contentgroove.com/api/v1");
    
    // Configure API key authorization: BearerHeader
    ApiKeyAuth BearerHeader = (ApiKeyAuth) defaultClient.getAuthentication("BearerHeader");
    BearerHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //BearerHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Object filter = new HashMap(); // Object | Filters to be applied to the query.  Query params in the url must look like this: \"filter[attributeName_*matcher*]\"  (i.e. filter[name_eq]=chimp%20into%20space)  Available matchers can be found here: https://activerecord-hackery.github.io/ransack/getting-started/search-matches/  
    Object page = new HashMap(); // Object | Specify page number and page size for the query
    String sort = "created_at"; // String | Sorting to be applied to the query. For more info: https://jsonapi.org/format/#fetching-sorting
    try {
      MediasResponseObject result = apiInstance.getMedias(filter, page, sort);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getMedias");
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
| **filter** | [**Object**](.md)| Filters to be applied to the query.  Query params in the url must look like this: \&quot;filter[attributeName_*matcher*]\&quot;  (i.e. filter[name_eq]&#x3D;chimp%20into%20space)  Available matchers can be found here: https://activerecord-hackery.github.io/ransack/getting-started/search-matches/   | [optional] |
| **page** | [**Object**](.md)| Specify page number and page size for the query | [optional] |
| **sort** | **String**| Sorting to be applied to the query. For more info: https://jsonapi.org/format/#fetching-sorting | [optional] [enum: created_at, -created_at, original_created_at, -original_created_at, name, -name] |

### Return type

[**MediasResponseObject**](MediasResponseObject.md)

### Authorization

[BearerHeader](../README.md#BearerHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful |  -  |
| **401** | unauthorized |  -  |
| **429** | too many requests |  -  |

<a id="getUploadUrl"></a>
# **getUploadUrl**
> DirectUploadResponseObject getUploadUrl()

prepare presigned upload url

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
    defaultClient.setBasePath("https://api.contentgroove.com/api/v1");
    
    // Configure API key authorization: BearerHeader
    ApiKeyAuth BearerHeader = (ApiKeyAuth) defaultClient.getAuthentication("BearerHeader");
    BearerHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //BearerHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    try {
      DirectUploadResponseObject result = apiInstance.getUploadUrl();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getUploadUrl");
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

[**DirectUploadResponseObject**](DirectUploadResponseObject.md)

### Authorization

[BearerHeader](../README.md#BearerHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful |  -  |
| **401** | unauthorized |  -  |
| **429** | too many requests |  -  |

<a id="getWebhookSubscriptionById"></a>
# **getWebhookSubscriptionById**
> WebhookSubscriptionResponseObject getWebhookSubscriptionById(id)

show webhook subscription

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
    defaultClient.setBasePath("https://api.contentgroove.com/api/v1");
    
    // Configure API key authorization: BearerHeader
    ApiKeyAuth BearerHeader = (ApiKeyAuth) defaultClient.getAuthentication("BearerHeader");
    BearerHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //BearerHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | The id of the webhook subscription to be retrieved
    try {
      WebhookSubscriptionResponseObject result = apiInstance.getWebhookSubscriptionById(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getWebhookSubscriptionById");
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
| **id** | **String**| The id of the webhook subscription to be retrieved | |

### Return type

[**WebhookSubscriptionResponseObject**](WebhookSubscriptionResponseObject.md)

### Authorization

[BearerHeader](../README.md#BearerHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful |  -  |
| **401** | not authorized |  -  |
| **404** | not found |  -  |
| **429** | too many requests |  -  |

<a id="getWebhookSubscriptions"></a>
# **getWebhookSubscriptions**
> WebhookSubscriptionsResponseObject getWebhookSubscriptions(filter, sort)

list webhook subscriptions

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
    defaultClient.setBasePath("https://api.contentgroove.com/api/v1");
    
    // Configure API key authorization: BearerHeader
    ApiKeyAuth BearerHeader = (ApiKeyAuth) defaultClient.getAuthentication("BearerHeader");
    BearerHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //BearerHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Object filter = new HashMap(); // Object | Filters to be applied to the query.  Query params in the url must look like this: \"filter[attributeName_*matcher*]\"  (i.e. filter[name_eq]=chimp%20into%20space)  Available matchers can be found here: https://activerecord-hackery.github.io/ransack/getting-started/search-matches/  
    String sort = "created_at"; // String | Sorting to be applied to the query. For more info: https://jsonapi.org/format/#fetching-sorting
    try {
      WebhookSubscriptionsResponseObject result = apiInstance.getWebhookSubscriptions(filter, sort);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getWebhookSubscriptions");
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
| **filter** | [**Object**](.md)| Filters to be applied to the query.  Query params in the url must look like this: \&quot;filter[attributeName_*matcher*]\&quot;  (i.e. filter[name_eq]&#x3D;chimp%20into%20space)  Available matchers can be found here: https://activerecord-hackery.github.io/ransack/getting-started/search-matches/   | [optional] |
| **sort** | **String**| Sorting to be applied to the query. For more info: https://jsonapi.org/format/#fetching-sorting | [optional] [enum: created_at, -created_at, original_created_at, -original_created_at, name, -name] |

### Return type

[**WebhookSubscriptionsResponseObject**](WebhookSubscriptionsResponseObject.md)

### Authorization

[BearerHeader](../README.md#BearerHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful |  -  |
| **401** | unauthorized |  -  |
| **429** | too many requests |  -  |

<a id="updateClipById"></a>
# **updateClipById**
> ClipResponseObject updateClipById(id, updateClipByIdRequest)

update clip

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
    defaultClient.setBasePath("https://api.contentgroove.com/api/v1");
    
    // Configure API key authorization: BearerHeader
    ApiKeyAuth BearerHeader = (ApiKeyAuth) defaultClient.getAuthentication("BearerHeader");
    BearerHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //BearerHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | The id of the clip to be retrieved
    UpdateClipByIdRequest updateClipByIdRequest = new UpdateClipByIdRequest(); // UpdateClipByIdRequest | 
    try {
      ClipResponseObject result = apiInstance.updateClipById(id, updateClipByIdRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#updateClipById");
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
| **id** | **String**| The id of the clip to be retrieved | |
| **updateClipByIdRequest** | [**UpdateClipByIdRequest**](UpdateClipByIdRequest.md)|  | |

### Return type

[**ClipResponseObject**](ClipResponseObject.md)

### Authorization

[BearerHeader](../README.md#BearerHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful |  -  |
| **401** | not authorized |  -  |
| **429** | too many requests |  -  |

<a id="updateMediaById"></a>
# **updateMediaById**
> MediaResponseObject updateMediaById(id, updateMediaByIdRequest)

update media

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
    defaultClient.setBasePath("https://api.contentgroove.com/api/v1");
    
    // Configure API key authorization: BearerHeader
    ApiKeyAuth BearerHeader = (ApiKeyAuth) defaultClient.getAuthentication("BearerHeader");
    BearerHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //BearerHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | id
    UpdateMediaByIdRequest updateMediaByIdRequest = new UpdateMediaByIdRequest(); // UpdateMediaByIdRequest | 
    try {
      MediaResponseObject result = apiInstance.updateMediaById(id, updateMediaByIdRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#updateMediaById");
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
| **id** | **String**| id | |
| **updateMediaByIdRequest** | [**UpdateMediaByIdRequest**](UpdateMediaByIdRequest.md)|  | |

### Return type

[**MediaResponseObject**](MediaResponseObject.md)

### Authorization

[BearerHeader](../README.md#BearerHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful |  -  |
| **401** | not authorized |  -  |
| **429** | too many requests |  -  |

