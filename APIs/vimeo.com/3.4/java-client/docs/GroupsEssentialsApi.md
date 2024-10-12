# GroupsEssentialsApi

All URIs are relative to *https://api.vimeo.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createGroup**](GroupsEssentialsApi.md#createGroup) | **POST** /groups | Create a group |
| [**deleteGroup**](GroupsEssentialsApi.md#deleteGroup) | **DELETE** /groups/{group_id} | Delete a group |
| [**getGroup**](GroupsEssentialsApi.md#getGroup) | **GET** /groups/{group_id} | Get a specific group |
| [**getGroups**](GroupsEssentialsApi.md#getGroups) | **GET** /groups | Get all groups |


<a id="createGroup"></a>
# **createGroup**
> Group createGroup(createGroupRequest)

Create a group

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroupsEssentialsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.vimeo.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    GroupsEssentialsApi apiInstance = new GroupsEssentialsApi(defaultClient);
    CreateGroupRequest createGroupRequest = new CreateGroupRequest(); // CreateGroupRequest | 
    try {
      Group result = apiInstance.createGroup(createGroupRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupsEssentialsApi#createGroup");
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
| **createGroupRequest** | [**CreateGroupRequest**](CreateGroupRequest.md)|  | |

### Return type

[**Group**](Group.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/vnd.vimeo.group+json
 - **Accept**: application/vnd.vimeo.group+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The group was created. |  -  |
| **400** | A parameter is invalid. |  -  |
| **403** | The authenticated user can&#39;t create groups. |  -  |

<a id="deleteGroup"></a>
# **deleteGroup**
> deleteGroup(groupId)

Delete a group

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroupsEssentialsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.vimeo.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    GroupsEssentialsApi apiInstance = new GroupsEssentialsApi(defaultClient);
    BigDecimal groupId = new BigDecimal("1108"); // BigDecimal | The ID of the group.
    try {
      apiInstance.deleteGroup(groupId);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupsEssentialsApi#deleteGroup");
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
| **groupId** | **BigDecimal**| The ID of the group. | |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | The group was deleted. |  -  |
| **403** | The authenticated user isn&#39;t the group owner. |  -  |

<a id="getGroup"></a>
# **getGroup**
> Group getGroup(groupId)

Get a specific group

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroupsEssentialsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.vimeo.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    GroupsEssentialsApi apiInstance = new GroupsEssentialsApi(defaultClient);
    BigDecimal groupId = new BigDecimal("1108"); // BigDecimal | The ID of the group.
    try {
      Group result = apiInstance.getGroup(groupId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupsEssentialsApi#getGroup");
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
| **groupId** | **BigDecimal**| The ID of the group. | |

### Return type

[**Group**](Group.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.vimeo.group+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The group was returned. |  -  |

<a id="getGroups"></a>
# **getGroups**
> List&lt;Group&gt; getGroups(direction, filter, page, perPage, query, sort)

Get all groups

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroupsEssentialsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.vimeo.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    GroupsEssentialsApi apiInstance = new GroupsEssentialsApi(defaultClient);
    String direction = "asc"; // String | The sort direction of the results.
    String filter = "featured"; // String | The attribute by which to filter the results.
    BigDecimal page = new BigDecimal("1"); // BigDecimal | The page number of the results to show.
    BigDecimal perPage = new BigDecimal("10"); // BigDecimal | The number of items to show on each page of results, up to a maximum of 100.
    String query = "Stop motion"; // String | The search query to use to filter the results.
    String sort = "alphabetical"; // String | The way to sort the results.  Option descriptions:  * `relevant` - Relevant sorting is available only for search queries. 
    try {
      List<Group> result = apiInstance.getGroups(direction, filter, page, perPage, query, sort);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupsEssentialsApi#getGroups");
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
| **direction** | **String**| The sort direction of the results. | [optional] [enum: asc, desc] |
| **filter** | **String**| The attribute by which to filter the results. | [optional] [enum: featured] |
| **page** | **BigDecimal**| The page number of the results to show. | [optional] |
| **perPage** | **BigDecimal**| The number of items to show on each page of results, up to a maximum of 100. | [optional] |
| **query** | **String**| The search query to use to filter the results. | [optional] |
| **sort** | **String**| The way to sort the results.  Option descriptions:  * &#x60;relevant&#x60; - Relevant sorting is available only for search queries.  | [optional] [enum: alphabetical, date, followers, relevant, videos] |

### Return type

[**List&lt;Group&gt;**](Group.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.vimeo.group+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The groups were returned. |  -  |

