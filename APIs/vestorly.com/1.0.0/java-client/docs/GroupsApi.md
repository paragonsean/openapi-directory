# GroupsApi

All URIs are relative to *https://staging.vestorly.com/api/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createGroup**](GroupsApi.md#createGroup) | **POST** /groups |  |
| [**deleteGroup**](GroupsApi.md#deleteGroup) | **DELETE** /groups/{id} |  |
| [**findGroupByID**](GroupsApi.md#findGroupByID) | **GET** /groups/{id} |  |
| [**findGroups**](GroupsApi.md#findGroups) | **GET** /groups |  |
| [**updateGroupById**](GroupsApi.md#updateGroupById) | **PUT** /groups/{id} |  |


<a id="createGroup"></a>
# **createGroup**
> Groupresponse createGroup(vestorlyAuth, group, accessToken)



Creates a new Group

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
    defaultClient.setBasePath("https://staging.vestorly.com/api/v2");
    
    // Configure OAuth2 access token for authorization: access_token
    OAuth access_token = (OAuth) defaultClient.getAuthentication("access_token");
    access_token.setAccessToken("YOUR ACCESS TOKEN");

    GroupsApi apiInstance = new GroupsApi(defaultClient);
    String vestorlyAuth = "vestorlyAuth_example"; // String | Vestorly Auth Token
    GroupInput group = new GroupInput(); // GroupInput | Group to add
    String accessToken = "accessToken_example"; // String | OAuth Token
    try {
      Groupresponse result = apiInstance.createGroup(vestorlyAuth, group, accessToken);
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
| **vestorlyAuth** | **String**| Vestorly Auth Token | |
| **group** | [**GroupInput**](GroupInput.md)| Group to add | |
| **accessToken** | **String**| OAuth Token | [optional] |

### Return type

[**Groupresponse**](Groupresponse.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | group response |  -  |

<a id="deleteGroup"></a>
# **deleteGroup**
> Groupresponse deleteGroup(vestorlyAuth, id, accessToken)



Deletes a Group

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
    defaultClient.setBasePath("https://staging.vestorly.com/api/v2");
    
    // Configure OAuth2 access token for authorization: access_token
    OAuth access_token = (OAuth) defaultClient.getAuthentication("access_token");
    access_token.setAccessToken("YOUR ACCESS TOKEN");

    GroupsApi apiInstance = new GroupsApi(defaultClient);
    String vestorlyAuth = "vestorlyAuth_example"; // String | Vestorly Auth Token
    String id = "id_example"; // String | id of group to delete
    String accessToken = "accessToken_example"; // String | OAuth Token
    try {
      Groupresponse result = apiInstance.deleteGroup(vestorlyAuth, id, accessToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupsApi#deleteGroup");
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
| **vestorlyAuth** | **String**| Vestorly Auth Token | |
| **id** | **String**| id of group to delete | |
| **accessToken** | **String**| OAuth Token | [optional] |

### Return type

[**Groupresponse**](Groupresponse.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | group response |  -  |

<a id="findGroupByID"></a>
# **findGroupByID**
> Groupresponse findGroupByID(vestorlyAuth, id, accessToken)



Returns a single group if user has access

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
    defaultClient.setBasePath("https://staging.vestorly.com/api/v2");
    
    // Configure OAuth2 access token for authorization: access_token
    OAuth access_token = (OAuth) defaultClient.getAuthentication("access_token");
    access_token.setAccessToken("YOUR ACCESS TOKEN");

    GroupsApi apiInstance = new GroupsApi(defaultClient);
    String vestorlyAuth = "vestorlyAuth_example"; // String | Vestorly Auth Token
    String id = "id_example"; // String | Mongo ID of group to fetch
    String accessToken = "accessToken_example"; // String | OAuth Token
    try {
      Groupresponse result = apiInstance.findGroupByID(vestorlyAuth, id, accessToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupsApi#findGroupByID");
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
| **vestorlyAuth** | **String**| Vestorly Auth Token | |
| **id** | **String**| Mongo ID of group to fetch | |
| **accessToken** | **String**| OAuth Token | [optional] |

### Return type

[**Groupresponse**](Groupresponse.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Group response |  -  |

<a id="findGroups"></a>
# **findGroups**
> Groups findGroups(vestorlyAuth, accessToken)



Returns all groups

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
    defaultClient.setBasePath("https://staging.vestorly.com/api/v2");
    
    // Configure OAuth2 access token for authorization: access_token
    OAuth access_token = (OAuth) defaultClient.getAuthentication("access_token");
    access_token.setAccessToken("YOUR ACCESS TOKEN");

    GroupsApi apiInstance = new GroupsApi(defaultClient);
    String vestorlyAuth = "vestorlyAuth_example"; // String | Vestorly Auth Token
    String accessToken = "accessToken_example"; // String | OAuth Token
    try {
      Groups result = apiInstance.findGroups(vestorlyAuth, accessToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupsApi#findGroups");
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
| **vestorlyAuth** | **String**| Vestorly Auth Token | |
| **accessToken** | **String**| OAuth Token | [optional] |

### Return type

[**Groups**](Groups.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Group response |  -  |

<a id="updateGroupById"></a>
# **updateGroupById**
> Groupresponse updateGroupById(vestorlyAuth, id, group, accessToken)



Updates a Group

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
    defaultClient.setBasePath("https://staging.vestorly.com/api/v2");
    
    // Configure OAuth2 access token for authorization: access_token
    OAuth access_token = (OAuth) defaultClient.getAuthentication("access_token");
    access_token.setAccessToken("YOUR ACCESS TOKEN");

    GroupsApi apiInstance = new GroupsApi(defaultClient);
    String vestorlyAuth = "vestorlyAuth_example"; // String | Vestorly Auth Token
    String id = "id_example"; // String | id of group to update
    GroupInput group = new GroupInput(); // GroupInput | Group to update
    String accessToken = "accessToken_example"; // String | OAuth Token
    try {
      Groupresponse result = apiInstance.updateGroupById(vestorlyAuth, id, group, accessToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupsApi#updateGroupById");
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
| **vestorlyAuth** | **String**| Vestorly Auth Token | |
| **id** | **String**| id of group to update | |
| **group** | [**GroupInput**](GroupInput.md)| Group to update | |
| **accessToken** | **String**| OAuth Token | [optional] |

### Return type

[**Groupresponse**](Groupresponse.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | group response |  -  |

