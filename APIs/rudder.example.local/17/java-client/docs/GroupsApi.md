# GroupsApi

All URIs are relative to *https://rudder.example.local/rudder/api/latest*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createGroup**](GroupsApi.md#createGroup) | **PUT** /groups | Create a group |
| [**createGroupCategory**](GroupsApi.md#createGroupCategory) | **PUT** /groups/categories | Create a group category |
| [**deleteGroup**](GroupsApi.md#deleteGroup) | **DELETE** /groups/{groupId} | Delete a group |
| [**deleteGroupCategory**](GroupsApi.md#deleteGroupCategory) | **DELETE** /groups/categories/{groupCategoryId} | Delete group category |
| [**getGroupCategoryDetails**](GroupsApi.md#getGroupCategoryDetails) | **GET** /groups/categories/{groupCategoryId} | Get group category details |
| [**getGroupTree**](GroupsApi.md#getGroupTree) | **GET** /groups/tree | Get groups tree |
| [**groupDetails**](GroupsApi.md#groupDetails) | **GET** /groups/{groupId} | Get group details |
| [**listGroups**](GroupsApi.md#listGroups) | **GET** /groups | List all groups |
| [**reloadGroup**](GroupsApi.md#reloadGroup) | **POST** /groups/{groupId}/reload | Reload a group |
| [**updateGroup**](GroupsApi.md#updateGroup) | **POST** /groups/{groupId} | Update group details |
| [**updateGroupCategory**](GroupsApi.md#updateGroupCategory) | **POST** /groups/categories/{groupCategoryId} | Update group category details |


<a id="createGroup"></a>
# **createGroup**
> CreateGroup200Response createGroup(groupNew)

Create a group

Create a new group based in provided parameters

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
    defaultClient.setBasePath("https://rudder.example.local/rudder/api/latest");
    
    // Configure API key authorization: API-Tokens
    ApiKeyAuth API-Tokens = (ApiKeyAuth) defaultClient.getAuthentication("API-Tokens");
    API-Tokens.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //API-Tokens.setApiKeyPrefix("Token");

    GroupsApi apiInstance = new GroupsApi(defaultClient);
    GroupNew groupNew = new GroupNew(); // GroupNew | 
    try {
      CreateGroup200Response result = apiInstance.createGroup(groupNew);
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
| **groupNew** | [**GroupNew**](GroupNew.md)|  | [optional] |

### Return type

[**CreateGroup200Response**](CreateGroup200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Group information |  -  |

<a id="createGroupCategory"></a>
# **createGroupCategory**
> CreateGroupCategory200Response createGroupCategory(groupCategory)

Create a group category

Create a new group category

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
    defaultClient.setBasePath("https://rudder.example.local/rudder/api/latest");
    
    // Configure API key authorization: API-Tokens
    ApiKeyAuth API-Tokens = (ApiKeyAuth) defaultClient.getAuthentication("API-Tokens");
    API-Tokens.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //API-Tokens.setApiKeyPrefix("Token");

    GroupsApi apiInstance = new GroupsApi(defaultClient);
    GroupCategory groupCategory = new GroupCategory(); // GroupCategory | 
    try {
      CreateGroupCategory200Response result = apiInstance.createGroupCategory(groupCategory);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupsApi#createGroupCategory");
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
| **groupCategory** | [**GroupCategory**](GroupCategory.md)|  | |

### Return type

[**CreateGroupCategory200Response**](CreateGroupCategory200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Groups category information |  -  |

<a id="deleteGroup"></a>
# **deleteGroup**
> DeleteGroup200Response deleteGroup(groupId)

Delete a group

Update detailed information about a group

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
    defaultClient.setBasePath("https://rudder.example.local/rudder/api/latest");
    
    // Configure API key authorization: API-Tokens
    ApiKeyAuth API-Tokens = (ApiKeyAuth) defaultClient.getAuthentication("API-Tokens");
    API-Tokens.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //API-Tokens.setApiKeyPrefix("Token");

    GroupsApi apiInstance = new GroupsApi(defaultClient);
    UUID groupId = UUID.fromString("9a1773c9-0889-40b6-be89-f6504443ac1b"); // UUID | Id of the group
    try {
      DeleteGroup200Response result = apiInstance.deleteGroup(groupId);
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
| **groupId** | **UUID**| Id of the group | |

### Return type

[**DeleteGroup200Response**](DeleteGroup200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Groups information |  -  |

<a id="deleteGroupCategory"></a>
# **deleteGroupCategory**
> DeleteGroupCategory200Response deleteGroupCategory(groupCategoryId)

Delete group category

Delete a group category. It must have no child groups and no children categories.

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
    defaultClient.setBasePath("https://rudder.example.local/rudder/api/latest");
    
    // Configure API key authorization: API-Tokens
    ApiKeyAuth API-Tokens = (ApiKeyAuth) defaultClient.getAuthentication("API-Tokens");
    API-Tokens.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //API-Tokens.setApiKeyPrefix("Token");

    GroupsApi apiInstance = new GroupsApi(defaultClient);
    UUID groupCategoryId = UUID.fromString("e0a311fa-f7b2-4f9e-89a9-db517b9c6b90"); // UUID | 
    try {
      DeleteGroupCategory200Response result = apiInstance.deleteGroupCategory(groupCategoryId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupsApi#deleteGroupCategory");
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
| **groupCategoryId** | **UUID**|  | |

### Return type

[**DeleteGroupCategory200Response**](DeleteGroupCategory200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Groups category information |  -  |

<a id="getGroupCategoryDetails"></a>
# **getGroupCategoryDetails**
> GetGroupCategoryDetails200Response getGroupCategoryDetails(groupCategoryId)

Get group category details

Get detailed information about a group category

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
    defaultClient.setBasePath("https://rudder.example.local/rudder/api/latest");
    
    // Configure API key authorization: API-Tokens
    ApiKeyAuth API-Tokens = (ApiKeyAuth) defaultClient.getAuthentication("API-Tokens");
    API-Tokens.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //API-Tokens.setApiKeyPrefix("Token");

    GroupsApi apiInstance = new GroupsApi(defaultClient);
    UUID groupCategoryId = UUID.fromString("e0a311fa-f7b2-4f9e-89a9-db517b9c6b90"); // UUID | 
    try {
      GetGroupCategoryDetails200Response result = apiInstance.getGroupCategoryDetails(groupCategoryId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupsApi#getGroupCategoryDetails");
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
| **groupCategoryId** | **UUID**|  | |

### Return type

[**GetGroupCategoryDetails200Response**](GetGroupCategoryDetails200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Groups category information |  -  |

<a id="getGroupTree"></a>
# **getGroupTree**
> GetGroupTree200Response getGroupTree()

Get groups tree

Get all available groups and their categories in a tree

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
    defaultClient.setBasePath("https://rudder.example.local/rudder/api/latest");
    
    // Configure API key authorization: API-Tokens
    ApiKeyAuth API-Tokens = (ApiKeyAuth) defaultClient.getAuthentication("API-Tokens");
    API-Tokens.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //API-Tokens.setApiKeyPrefix("Token");

    GroupsApi apiInstance = new GroupsApi(defaultClient);
    try {
      GetGroupTree200Response result = apiInstance.getGroupTree();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupsApi#getGroupTree");
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

[**GetGroupTree200Response**](GetGroupTree200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Groups information |  -  |

<a id="groupDetails"></a>
# **groupDetails**
> GroupDetails200Response groupDetails(groupId)

Get group details

Get detailed information about a group

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
    defaultClient.setBasePath("https://rudder.example.local/rudder/api/latest");
    
    // Configure API key authorization: API-Tokens
    ApiKeyAuth API-Tokens = (ApiKeyAuth) defaultClient.getAuthentication("API-Tokens");
    API-Tokens.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //API-Tokens.setApiKeyPrefix("Token");

    GroupsApi apiInstance = new GroupsApi(defaultClient);
    UUID groupId = UUID.fromString("9a1773c9-0889-40b6-be89-f6504443ac1b"); // UUID | Id of the group
    try {
      GroupDetails200Response result = apiInstance.groupDetails(groupId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupsApi#groupDetails");
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
| **groupId** | **UUID**| Id of the group | |

### Return type

[**GroupDetails200Response**](GroupDetails200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Groups information |  -  |

<a id="listGroups"></a>
# **listGroups**
> ListGroups200Response listGroups()

List all groups

List all groups

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
    defaultClient.setBasePath("https://rudder.example.local/rudder/api/latest");
    
    // Configure API key authorization: API-Tokens
    ApiKeyAuth API-Tokens = (ApiKeyAuth) defaultClient.getAuthentication("API-Tokens");
    API-Tokens.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //API-Tokens.setApiKeyPrefix("Token");

    GroupsApi apiInstance = new GroupsApi(defaultClient);
    try {
      ListGroups200Response result = apiInstance.listGroups();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupsApi#listGroups");
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

[**ListGroups200Response**](ListGroups200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Groups information |  -  |

<a id="reloadGroup"></a>
# **reloadGroup**
> ReloadGroup200Response reloadGroup(groupId)

Reload a group

Recompute the content of a group

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
    defaultClient.setBasePath("https://rudder.example.local/rudder/api/latest");
    
    // Configure API key authorization: API-Tokens
    ApiKeyAuth API-Tokens = (ApiKeyAuth) defaultClient.getAuthentication("API-Tokens");
    API-Tokens.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //API-Tokens.setApiKeyPrefix("Token");

    GroupsApi apiInstance = new GroupsApi(defaultClient);
    UUID groupId = UUID.fromString("9a1773c9-0889-40b6-be89-f6504443ac1b"); // UUID | Id of the group
    try {
      ReloadGroup200Response result = apiInstance.reloadGroup(groupId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupsApi#reloadGroup");
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
| **groupId** | **UUID**| Id of the group | |

### Return type

[**ReloadGroup200Response**](ReloadGroup200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Groups information |  -  |

<a id="updateGroup"></a>
# **updateGroup**
> UpdateGroup200Response updateGroup(groupId, groupUpdate)

Update group details

Update detailed information about a group

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
    defaultClient.setBasePath("https://rudder.example.local/rudder/api/latest");
    
    // Configure API key authorization: API-Tokens
    ApiKeyAuth API-Tokens = (ApiKeyAuth) defaultClient.getAuthentication("API-Tokens");
    API-Tokens.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //API-Tokens.setApiKeyPrefix("Token");

    GroupsApi apiInstance = new GroupsApi(defaultClient);
    UUID groupId = UUID.fromString("9a1773c9-0889-40b6-be89-f6504443ac1b"); // UUID | Id of the group
    GroupUpdate groupUpdate = new GroupUpdate(); // GroupUpdate | 
    try {
      UpdateGroup200Response result = apiInstance.updateGroup(groupId, groupUpdate);
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
| **groupId** | **UUID**| Id of the group | |
| **groupUpdate** | [**GroupUpdate**](GroupUpdate.md)|  | |

### Return type

[**UpdateGroup200Response**](UpdateGroup200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Groups information |  -  |

<a id="updateGroupCategory"></a>
# **updateGroupCategory**
> UpdateGroupCategory200Response updateGroupCategory(groupCategoryId, groupCategoryUpdate)

Update group category details

Update detailed information about a group category

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
    defaultClient.setBasePath("https://rudder.example.local/rudder/api/latest");
    
    // Configure API key authorization: API-Tokens
    ApiKeyAuth API-Tokens = (ApiKeyAuth) defaultClient.getAuthentication("API-Tokens");
    API-Tokens.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //API-Tokens.setApiKeyPrefix("Token");

    GroupsApi apiInstance = new GroupsApi(defaultClient);
    UUID groupCategoryId = UUID.fromString("e0a311fa-f7b2-4f9e-89a9-db517b9c6b90"); // UUID | 
    GroupCategoryUpdate groupCategoryUpdate = new GroupCategoryUpdate(); // GroupCategoryUpdate | 
    try {
      UpdateGroupCategory200Response result = apiInstance.updateGroupCategory(groupCategoryId, groupCategoryUpdate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupsApi#updateGroupCategory");
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
| **groupCategoryId** | **UUID**|  | |
| **groupCategoryUpdate** | [**GroupCategoryUpdate**](GroupCategoryUpdate.md)|  | |

### Return type

[**UpdateGroupCategory200Response**](UpdateGroupCategory200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Groups category information |  -  |

