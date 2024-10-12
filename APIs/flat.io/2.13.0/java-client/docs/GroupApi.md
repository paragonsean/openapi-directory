# GroupApi

All URIs are relative to *https://api.flat.io/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getGroupDetails**](GroupApi.md#getGroupDetails) | **GET** /groups/{group} | Get group information |
| [**getGroupScores**](GroupApi.md#getGroupScores) | **GET** /groups/{group}/scores | List group&#39;s scores |
| [**listGroupUsers**](GroupApi.md#listGroupUsers) | **GET** /groups/{group}/users | List group&#39;s users |


<a id="getGroupDetails"></a>
# **getGroupDetails**
> GroupDetails getGroupDetails(group)

Get group information

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroupApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.flat.io/v2");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    GroupApi apiInstance = new GroupApi(defaultClient);
    String group = "group_example"; // String | Unique identifier of a Flat group 
    try {
      GroupDetails result = apiInstance.getGroupDetails(group);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupApi#getGroupDetails");
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
| **group** | **String**| Unique identifier of a Flat group  | |

### Return type

[**GroupDetails**](GroupDetails.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The group details |  -  |
| **0** | Error |  -  |

<a id="getGroupScores"></a>
# **getGroupScores**
> List&lt;ScoreDetails&gt; getGroupScores(group, parent)

List group&#39;s scores

Get the list of scores shared with a group. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroupApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.flat.io/v2");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    GroupApi apiInstance = new GroupApi(defaultClient);
    String group = "group_example"; // String | Unique identifier of a Flat group 
    String parent = "parent_example"; // String | Filter the score forked from the score id `parent`
    try {
      List<ScoreDetails> result = apiInstance.getGroupScores(group, parent);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupApi#getGroupScores");
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
| **group** | **String**| Unique identifier of a Flat group  | |
| **parent** | **String**| Filter the score forked from the score id &#x60;parent&#x60; | [optional] |

### Return type

[**List&lt;ScoreDetails&gt;**](ScoreDetails.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The group&#39;s scores |  -  |
| **0** | Error |  -  |

<a id="listGroupUsers"></a>
# **listGroupUsers**
> List&lt;UserPublic&gt; listGroupUsers(group, source)

List group&#39;s users

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroupApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.flat.io/v2");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    GroupApi apiInstance = new GroupApi(defaultClient);
    String group = "group_example"; // String | Unique identifier of a Flat group 
    String source = "googleClassroom"; // String | Filter the users by their source 
    try {
      List<UserPublic> result = apiInstance.listGroupUsers(group, source);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupApi#listGroupUsers");
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
| **group** | **String**| Unique identifier of a Flat group  | |
| **source** | **String**| Filter the users by their source  | [optional] [enum: googleClassroom, microsoftGraph, clever] |

### Return type

[**List&lt;UserPublic&gt;**](UserPublic.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The list of users member of the group |  -  |
| **0** | Error |  -  |

