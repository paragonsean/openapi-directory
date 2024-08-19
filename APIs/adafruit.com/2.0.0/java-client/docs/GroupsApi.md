# GroupsApi

All URIs are relative to *https://io.adafruit.com/api/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addFeedToGroup**](GroupsApi.md#addFeedToGroup) | **POST** /{username}/groups/{group_key}/add | Add an existing Feed to a Group |
| [**allGroupFeeds**](GroupsApi.md#allGroupFeeds) | **GET** /{username}/groups/{group_key}/feeds | All feeds for current user in a given group |
| [**allGroups**](GroupsApi.md#allGroups) | **GET** /{username}/groups | All groups for current user |
| [**createGroup**](GroupsApi.md#createGroup) | **POST** /{username}/groups | Create a new Group |
| [**destroyGroup**](GroupsApi.md#destroyGroup) | **DELETE** /{username}/groups/{group_key} | Delete an existing Group |
| [**getGroup**](GroupsApi.md#getGroup) | **GET** /{username}/groups/{group_key} | Returns Group based on ID |
| [**removeFeedFromGroup**](GroupsApi.md#removeFeedFromGroup) | **POST** /{username}/groups/{group_key}/remove | Remove a Feed from a Group |
| [**replaceGroup**](GroupsApi.md#replaceGroup) | **PUT** /{username}/groups/{group_key} | Replace an existing Group |
| [**updateGroup**](GroupsApi.md#updateGroup) | **PATCH** /{username}/groups/{group_key} | Update properties of an existing Group |


<a id="addFeedToGroup"></a>
# **addFeedToGroup**
> Group addFeedToGroup(groupKey, username, feedKey)

Add an existing Feed to a Group

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://io.adafruit.com/api/v2");
    
    // Configure API key authorization: HeaderSignature
    ApiKeyAuth HeaderSignature = (ApiKeyAuth) defaultClient.getAuthentication("HeaderSignature");
    HeaderSignature.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //HeaderSignature.setApiKeyPrefix("Token");

    // Configure API key authorization: QueryKey
    ApiKeyAuth QueryKey = (ApiKeyAuth) defaultClient.getAuthentication("QueryKey");
    QueryKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //QueryKey.setApiKeyPrefix("Token");

    // Configure API key authorization: HeaderKey
    ApiKeyAuth HeaderKey = (ApiKeyAuth) defaultClient.getAuthentication("HeaderKey");
    HeaderKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //HeaderKey.setApiKeyPrefix("Token");

    GroupsApi apiInstance = new GroupsApi(defaultClient);
    String groupKey = "groupKey_example"; // String | 
    String username = "username_example"; // String | a valid username string
    String feedKey = "feedKey_example"; // String | 
    try {
      Group result = apiInstance.addFeedToGroup(groupKey, username, feedKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupsApi#addFeedToGroup");
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
| **groupKey** | **String**|  | |
| **username** | **String**| a valid username string | |
| **feedKey** | **String**|  | [optional] |

### Return type

[**Group**](Group.md)

### Authorization

[HeaderSignature](../README.md#HeaderSignature), [QueryKey](../README.md#QueryKey), [HeaderKey](../README.md#HeaderKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/csv

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Updated group |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **500** | Server Error |  -  |

<a id="allGroupFeeds"></a>
# **allGroupFeeds**
> List&lt;Feed&gt; allGroupFeeds(groupKey, username)

All feeds for current user in a given group

The Group Feeds endpoint returns information about the user&#39;s feeds. The response includes the latest value of each feed, and other metadata about each feed, but only for feeds within the given group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://io.adafruit.com/api/v2");
    
    // Configure API key authorization: HeaderSignature
    ApiKeyAuth HeaderSignature = (ApiKeyAuth) defaultClient.getAuthentication("HeaderSignature");
    HeaderSignature.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //HeaderSignature.setApiKeyPrefix("Token");

    // Configure API key authorization: QueryKey
    ApiKeyAuth QueryKey = (ApiKeyAuth) defaultClient.getAuthentication("QueryKey");
    QueryKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //QueryKey.setApiKeyPrefix("Token");

    // Configure API key authorization: HeaderKey
    ApiKeyAuth HeaderKey = (ApiKeyAuth) defaultClient.getAuthentication("HeaderKey");
    HeaderKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //HeaderKey.setApiKeyPrefix("Token");

    GroupsApi apiInstance = new GroupsApi(defaultClient);
    String groupKey = "groupKey_example"; // String | 
    String username = "username_example"; // String | a valid username string
    try {
      List<Feed> result = apiInstance.allGroupFeeds(groupKey, username);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupsApi#allGroupFeeds");
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
| **groupKey** | **String**|  | |
| **username** | **String**| a valid username string | |

### Return type

[**List&lt;Feed&gt;**](Feed.md)

### Authorization

[HeaderSignature](../README.md#HeaderSignature), [QueryKey](../README.md#QueryKey), [HeaderKey](../README.md#HeaderKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/csv

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | An array of feeds |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **500** | Server Error |  -  |

<a id="allGroups"></a>
# **allGroups**
> List&lt;Group&gt; allGroups(username)

All groups for current user

The Groups endpoint returns information about the user&#39;s groups. The response includes the latest value of each feed in the group, and other metadata about the group. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://io.adafruit.com/api/v2");
    
    // Configure API key authorization: HeaderSignature
    ApiKeyAuth HeaderSignature = (ApiKeyAuth) defaultClient.getAuthentication("HeaderSignature");
    HeaderSignature.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //HeaderSignature.setApiKeyPrefix("Token");

    // Configure API key authorization: QueryKey
    ApiKeyAuth QueryKey = (ApiKeyAuth) defaultClient.getAuthentication("QueryKey");
    QueryKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //QueryKey.setApiKeyPrefix("Token");

    // Configure API key authorization: HeaderKey
    ApiKeyAuth HeaderKey = (ApiKeyAuth) defaultClient.getAuthentication("HeaderKey");
    HeaderKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //HeaderKey.setApiKeyPrefix("Token");

    GroupsApi apiInstance = new GroupsApi(defaultClient);
    String username = "username_example"; // String | a valid username string
    try {
      List<Group> result = apiInstance.allGroups(username);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupsApi#allGroups");
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
| **username** | **String**| a valid username string | |

### Return type

[**List&lt;Group&gt;**](Group.md)

### Authorization

[HeaderSignature](../README.md#HeaderSignature), [QueryKey](../README.md#QueryKey), [HeaderKey](../README.md#HeaderKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/csv

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | An array of groups |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **500** | Server Error |  -  |

<a id="createGroup"></a>
# **createGroup**
> Group createGroup(username, group)

Create a new Group

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://io.adafruit.com/api/v2");
    
    // Configure API key authorization: HeaderSignature
    ApiKeyAuth HeaderSignature = (ApiKeyAuth) defaultClient.getAuthentication("HeaderSignature");
    HeaderSignature.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //HeaderSignature.setApiKeyPrefix("Token");

    // Configure API key authorization: QueryKey
    ApiKeyAuth QueryKey = (ApiKeyAuth) defaultClient.getAuthentication("QueryKey");
    QueryKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //QueryKey.setApiKeyPrefix("Token");

    // Configure API key authorization: HeaderKey
    ApiKeyAuth HeaderKey = (ApiKeyAuth) defaultClient.getAuthentication("HeaderKey");
    HeaderKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //HeaderKey.setApiKeyPrefix("Token");

    GroupsApi apiInstance = new GroupsApi(defaultClient);
    String username = "username_example"; // String | a valid username string
    CreateDashboardRequest group = new CreateDashboardRequest(); // CreateDashboardRequest | 
    try {
      Group result = apiInstance.createGroup(username, group);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupsApi#createGroup");
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
| **username** | **String**| a valid username string | |
| **group** | [**CreateDashboardRequest**](CreateDashboardRequest.md)|  | |

### Return type

[**Group**](Group.md)

### Authorization

[HeaderSignature](../README.md#HeaderSignature), [QueryKey](../README.md#QueryKey), [HeaderKey](../README.md#HeaderKey)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json, text/csv

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | New Group |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **500** | Server Error |  -  |

<a id="destroyGroup"></a>
# **destroyGroup**
> String destroyGroup(username, groupKey)

Delete an existing Group

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://io.adafruit.com/api/v2");
    
    // Configure API key authorization: HeaderSignature
    ApiKeyAuth HeaderSignature = (ApiKeyAuth) defaultClient.getAuthentication("HeaderSignature");
    HeaderSignature.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //HeaderSignature.setApiKeyPrefix("Token");

    // Configure API key authorization: QueryKey
    ApiKeyAuth QueryKey = (ApiKeyAuth) defaultClient.getAuthentication("QueryKey");
    QueryKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //QueryKey.setApiKeyPrefix("Token");

    // Configure API key authorization: HeaderKey
    ApiKeyAuth HeaderKey = (ApiKeyAuth) defaultClient.getAuthentication("HeaderKey");
    HeaderKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //HeaderKey.setApiKeyPrefix("Token");

    GroupsApi apiInstance = new GroupsApi(defaultClient);
    String username = "username_example"; // String | a valid username string
    String groupKey = "groupKey_example"; // String | 
    try {
      String result = apiInstance.destroyGroup(username, groupKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupsApi#destroyGroup");
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
| **username** | **String**| a valid username string | |
| **groupKey** | **String**|  | |

### Return type

**String**

### Authorization

[HeaderSignature](../README.md#HeaderSignature), [QueryKey](../README.md#QueryKey), [HeaderKey](../README.md#HeaderKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/csv

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Deleted Group successfully |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **500** | Server Error |  -  |

<a id="getGroup"></a>
# **getGroup**
> Group getGroup(username, groupKey)

Returns Group based on ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://io.adafruit.com/api/v2");
    
    // Configure API key authorization: HeaderSignature
    ApiKeyAuth HeaderSignature = (ApiKeyAuth) defaultClient.getAuthentication("HeaderSignature");
    HeaderSignature.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //HeaderSignature.setApiKeyPrefix("Token");

    // Configure API key authorization: QueryKey
    ApiKeyAuth QueryKey = (ApiKeyAuth) defaultClient.getAuthentication("QueryKey");
    QueryKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //QueryKey.setApiKeyPrefix("Token");

    // Configure API key authorization: HeaderKey
    ApiKeyAuth HeaderKey = (ApiKeyAuth) defaultClient.getAuthentication("HeaderKey");
    HeaderKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //HeaderKey.setApiKeyPrefix("Token");

    GroupsApi apiInstance = new GroupsApi(defaultClient);
    String username = "username_example"; // String | a valid username string
    String groupKey = "groupKey_example"; // String | 
    try {
      Group result = apiInstance.getGroup(username, groupKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupsApi#getGroup");
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
| **username** | **String**| a valid username string | |
| **groupKey** | **String**|  | |

### Return type

[**Group**](Group.md)

### Authorization

[HeaderSignature](../README.md#HeaderSignature), [QueryKey](../README.md#QueryKey), [HeaderKey](../README.md#HeaderKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/csv

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Group response |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **500** | Server Error\&quot; |  -  |

<a id="removeFeedFromGroup"></a>
# **removeFeedFromGroup**
> Group removeFeedFromGroup(groupKey, username, feedKey)

Remove a Feed from a Group

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://io.adafruit.com/api/v2");
    
    // Configure API key authorization: HeaderSignature
    ApiKeyAuth HeaderSignature = (ApiKeyAuth) defaultClient.getAuthentication("HeaderSignature");
    HeaderSignature.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //HeaderSignature.setApiKeyPrefix("Token");

    // Configure API key authorization: QueryKey
    ApiKeyAuth QueryKey = (ApiKeyAuth) defaultClient.getAuthentication("QueryKey");
    QueryKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //QueryKey.setApiKeyPrefix("Token");

    // Configure API key authorization: HeaderKey
    ApiKeyAuth HeaderKey = (ApiKeyAuth) defaultClient.getAuthentication("HeaderKey");
    HeaderKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //HeaderKey.setApiKeyPrefix("Token");

    GroupsApi apiInstance = new GroupsApi(defaultClient);
    String groupKey = "groupKey_example"; // String | 
    String username = "username_example"; // String | a valid username string
    String feedKey = "feedKey_example"; // String | 
    try {
      Group result = apiInstance.removeFeedFromGroup(groupKey, username, feedKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupsApi#removeFeedFromGroup");
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
| **groupKey** | **String**|  | |
| **username** | **String**| a valid username string | |
| **feedKey** | **String**|  | [optional] |

### Return type

[**Group**](Group.md)

### Authorization

[HeaderSignature](../README.md#HeaderSignature), [QueryKey](../README.md#QueryKey), [HeaderKey](../README.md#HeaderKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/csv

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Updated group |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **500** | Server Error |  -  |

<a id="replaceGroup"></a>
# **replaceGroup**
> Group replaceGroup(username, groupKey, group)

Replace an existing Group

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://io.adafruit.com/api/v2");
    
    // Configure API key authorization: HeaderSignature
    ApiKeyAuth HeaderSignature = (ApiKeyAuth) defaultClient.getAuthentication("HeaderSignature");
    HeaderSignature.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //HeaderSignature.setApiKeyPrefix("Token");

    // Configure API key authorization: QueryKey
    ApiKeyAuth QueryKey = (ApiKeyAuth) defaultClient.getAuthentication("QueryKey");
    QueryKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //QueryKey.setApiKeyPrefix("Token");

    // Configure API key authorization: HeaderKey
    ApiKeyAuth HeaderKey = (ApiKeyAuth) defaultClient.getAuthentication("HeaderKey");
    HeaderKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //HeaderKey.setApiKeyPrefix("Token");

    GroupsApi apiInstance = new GroupsApi(defaultClient);
    String username = "username_example"; // String | a valid username string
    String groupKey = "groupKey_example"; // String | 
    CreateDashboardRequest group = new CreateDashboardRequest(); // CreateDashboardRequest | 
    try {
      Group result = apiInstance.replaceGroup(username, groupKey, group);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupsApi#replaceGroup");
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
| **username** | **String**| a valid username string | |
| **groupKey** | **String**|  | |
| **group** | [**CreateDashboardRequest**](CreateDashboardRequest.md)|  | |

### Return type

[**Group**](Group.md)

### Authorization

[HeaderSignature](../README.md#HeaderSignature), [QueryKey](../README.md#QueryKey), [HeaderKey](../README.md#HeaderKey)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json, text/csv

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Updated group |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **500** | Server Error |  -  |

<a id="updateGroup"></a>
# **updateGroup**
> Group updateGroup(username, groupKey, group)

Update properties of an existing Group

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://io.adafruit.com/api/v2");
    
    // Configure API key authorization: HeaderSignature
    ApiKeyAuth HeaderSignature = (ApiKeyAuth) defaultClient.getAuthentication("HeaderSignature");
    HeaderSignature.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //HeaderSignature.setApiKeyPrefix("Token");

    // Configure API key authorization: QueryKey
    ApiKeyAuth QueryKey = (ApiKeyAuth) defaultClient.getAuthentication("QueryKey");
    QueryKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //QueryKey.setApiKeyPrefix("Token");

    // Configure API key authorization: HeaderKey
    ApiKeyAuth HeaderKey = (ApiKeyAuth) defaultClient.getAuthentication("HeaderKey");
    HeaderKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //HeaderKey.setApiKeyPrefix("Token");

    GroupsApi apiInstance = new GroupsApi(defaultClient);
    String username = "username_example"; // String | a valid username string
    String groupKey = "groupKey_example"; // String | 
    CreateDashboardRequest group = new CreateDashboardRequest(); // CreateDashboardRequest | 
    try {
      Group result = apiInstance.updateGroup(username, groupKey, group);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupsApi#updateGroup");
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
| **username** | **String**| a valid username string | |
| **groupKey** | **String**|  | |
| **group** | [**CreateDashboardRequest**](CreateDashboardRequest.md)|  | |

### Return type

[**Group**](Group.md)

### Authorization

[HeaderSignature](../README.md#HeaderSignature), [QueryKey](../README.md#QueryKey), [HeaderKey](../README.md#HeaderKey)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json, text/csv

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Updated Group |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **500** | Server Error |  -  |

